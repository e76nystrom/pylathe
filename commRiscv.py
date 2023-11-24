#*******************************************************************************
from icecream import ic
from threading import Thread
from queue import Queue, Empty
from sys import stdout
from time import sleep, time
# from platform import system
from ctypes import c_int32, c_uint32
# from sys import stdout
from threading import Lock
from datetime import datetime
from pytz import timezone
import os
import re

from accelPi import AccelData, taperCalc, intRound, syncAccelCalc
from remParmDef import remParmTable
import riscvParmDef as rp
import riscvCmdDef as rc
from remCmdDef import cmdTable
# from remParm import RemParm
import enumDef as en
# import lRegDef as rg
import fpgaLathe as bt
import ctlBitDef as ct
from remParm import RemParm

import serial

DBG_DIR = os.path.join(os.getcwd(), "dbg")

Z_AXIS = 0
X_AXIS = 1

DIR_POS = 1

CMD_OVERHEAD = 8
MOVE_OVERHEAD = 8
MAX_CMD_LEN = 80

tz = timezone("America/New_York")

def timeStr():
    now = datetime.now(tz=tz)
    return now.strftime("%a %b %d %Y %H:%M:%S\n")

dbgFile = None
def trace(txt):
    global dbgFile
    if dbgFile is None:
        dbgFile = open("riscCmd.txt", "wb")
    dbgFile.write((txt + "\n").encode())
    dbgFile.flush()

class CommTimeout(Exception):
    pass

def getResult(rsp, index):
    result = rsp.split()
    print("getResult %s index %d %s" % (rsp, index, result))
    if index < len(result):
        retVal = int(result[index], 16)
        retVal = c_int32(retVal).value
        return retVal
    return 0

def tmpCommand(_0, _1):
    pass

riscvCmd = tmpCommand

def riscvAccelData(accel, accelType, que=False):
    txt = "riscVAccelData %-10s %d" % (en.axisAccelTypeList[accelType],
                                       accelType)
    trace(txt)
    print(txt)
    cmd = rc.R_SET_ACCEL if not que else rc.R_SET_ACCEL_Q
    riscvCmd(cmd, (accelType << 8 | en.RP_INITIAL_SUM, accel.initialSum))
    riscvCmd(cmd, (accelType << 8 | en.RP_INCR1,       accel.incr1))
    riscvCmd(cmd, (accelType << 8 | en.RP_INCR2,       accel.incr2))
    riscvCmd(cmd, (accelType << 8 | en.RP_ACCEL_VAL,   accel.intAccel))
    riscvCmd(cmd, (accelType << 8 | en.RP_ACCEL_COUNT, accel.accelClocks))
    riscvCmd(cmd, (accelType << 8 | en.RP_FREQ_DIV,    accel.freqDivider))

def prtAxisCtl(axisCtl):
    s = ""
    if (axisCtl & bt.ctlInit) != 0:
        s += "Init "
    if (axisCtl & bt.ctlStart) != 0:
        s += "Start "
    s += "Dir" + ("+ " if (axisCtl & bt.ctlDir) != 0 else "- ")
    if (axisCtl & bt.ctlBacklash) != 0:
        s += "Backlash "
    if (axisCtl & bt.ctlWaitSync) != 0:
        s += "WaitSync "
    if (axisCtl & bt.ctlSetLoc) != 0:
        s += "SetLoc "
    if (axisCtl & bt.ctlChDirect) != 0:
        s += "ChDirect "
    if (axisCtl & bt.ctlSlave) != 0:
        s += "Slave "
    if (axisCtl & bt.ctlDistMode) != 0:
        s += "DistMode "
    if (axisCtl & bt.ctlDroEnd) != 0:
        s += "DroEnd "
    if (axisCtl & bt.ctlJogCmd) != 0:
        s += "JogCmd "
    if (axisCtl & bt.ctlJogMpg) != 0:
        s += "JogMpg "
    if (axisCtl & bt.ctlHome) != 0:
        s += "Home "
    if (axisCtl & bt.ctlUseLimits) != 0:
        s += "IgnoreLim "
    return s

def enableXilinx():
    pass

class CommRiscv():
    def __init__(self, mainFrame):
        self.ser = None
        self.riscv   = riscv = RiscvLathe(self, mainFrame)
        self.moveQue = self.riscv.moveQue
        self.openSerial("COM10", "19200")
        global riscvCmd
        riscvCmd = self.riscvCmd
        self.setPostUpdate = riscv.setPostUpdate
        self.setDbgDispatch = riscv.setDbgDispatch
        self.timeout = False
        self.commLock = Lock()
        self.trace = trace

        self.xDbgPrint = True
        self.lastCmd = ''

        self.cmdLen = CMD_OVERHEAD

        self.cmdQue = []
        self.cmdLen = 0
        self.cmdStr = ""
        # self.ld = None
        # self.rd = None
        # self.ldAxisCtl = None
        # self.rpi = None

    def setupCmds(self, loadMulti, loadVal, readVal):
        pass

    def setupTables(self, cmdTbl, parmTbl):
        self.cmdTable = cmdTbl
        self.parmTable = parmTbl

    def enableXilinx(self):
        pass

    def openSerial(self, port, rate):
        if port is None or rate is None:
            return
        if (len(port) == 0) or (len(rate) == 0):
            return
        
        try:
            rate = int(rate)
        except ValueError:
            return
        
        try:
            self.ser = serial.Serial(port, rate, timeout=2)
        except IOError:
            print("unable to open port %s" % (port))
            stdout.flush()

    def closeSerial(self):
        if self.ser is not None:
            self.ser.close()
            self.ser = None

    def close(self):
        self.riscv.close()
        self.closeSerial()

    def command(self, cmdVal):
        print("cmd %12s" % (cmdTable[cmdVal][0]))
        try:
            # noinspection PyCallingNonCallable
            self.riscv.cmdAction[cmdVal]()
        except TypeError:
            print("command no routine %d %s" % (cmdVal, cmdTable[cmdVal]))

    def queParm(self, parmIndex, val):
        self.setParm(parmIndex, val)

    def sendMulti(self):
        pass

    def setParm(self, parmIndex, val):
        (name, varType, varName) = remParmTable[parmIndex]
        if varType == 'float':
            val = float(val)
            valString = "%15.6f" % val
            valString = re.sub("0+$", "", valString)
            if valString.endswith('.'):
                valString += '0'
        else:
            val = int(val)
            valString = "%8d" % val
        print("set %22s %22s %s" % (name, varName, valString))
        setattr(self.riscv.parm, varName, val)

    def getParm(self, parmIndex):
        (name, varType, varName) = remParmTable[parmIndex]
        val = getattr(self.riscv.parm, varName)
        print("getParm var %s val %s" % (varName, str(val)))
        return val

    def getString(self, cmd, parm=None):
        pass

    def setXReg(self, reg, val):
        pass

    def setXRegN(self, reg, val):
        pass

    def getXReg(self, reg):
        pass

    def dspXReg(self, reg, val, label=''):
        pass

    def sendMove(self, opString, op, val):
        self.moveQue.put((opString, op, val))

    # noinspection PyMethodMayBeStatic
    def getQueueStatus(self):
        return(64)

    def riscvSend(self):
        if self.cmdLen == 0:
            return
        # if self.ser is None:
        #     return
        prefix = '\x01%02x' % (self.cmdLen + 1)
        cmd = prefix + self.cmdStr + '\r'
        stdout.flush()
        if len(self.cmdStr) > 2:
            trace(cmd.strip('\x01\r'))
        self.cmdLen = 0
        self.cmdStr = ""

        self.commLock.acquire(True)

        self.ser.write(cmd.encode())
        rsp = self.ser.read(3).decode('utf8')
        if len(rsp) == 0:
            self.commLock.release()
            if not self.timeout:
                self.timeout = True
                print("timeout")
                print(cmd.strip('\x01\r'))
                stdout.flush()
            raise CommTimeout()

        rspLen = int(rsp[1:3], 16)
        rsp += self.ser.read(rspLen).decode('utf8')
        self.commLock.release()

        self.riscv.queCount = int(rsp[3:5], 16)
        if rspLen > 7:
            rspType = int(rsp[5:7], 16)
            if rspType != rc.R_READ_ALL:
                trace(rsp)
                print("cmdLen %d" % (len(cmd)))
                print("rsp", rsp)
        if rsp[-1] == '*':
            self.timeout = False
        return rsp

    def riscvCmd(self, cmd, arg=None, flush=False):
        cmdStr = '%x' % (cmd)
        data = ""
        if arg is not None:
            argType = type(arg)
            if argType != tuple:
                cmdStr += " %x" % c_uint32(arg).value
                if arg < 0:
                    print("***", arg, cmdStr)
            elif argType == tuple:
                for val in arg:
                    cmdStr += " %x" % c_uint32(val).value
                if (cmd == rc.R_SET_ACCEL) or (cmd == rc.R_SET_ACCEL_Q):
                    x0 = arg[0] >> 8
                    x1 = arg[0] & 0xff
                    data = "%10d %d %-10s %d %-14s" % \
                        (arg[1] ,x0, en.axisAccelTypeList[x0],
                         x1, en.RiscvSyncParmTypeList[x1])
            else:
                pass
        txt = "%-16s %-16s%s" % (rc.cmdTable[cmd],
                                 cmdStr.strip('\x01\r'), data)
        cmdLen = len(cmdStr)
        if ((self.cmdLen + cmdLen) >= MAX_CMD_LEN) or flush:
            self.riscvSend()
            self.cmdLen = cmdLen
            self.cmdStr = cmdStr
        else:
            if self.cmdLen != 0:
                self.cmdStr += '|'
                self.cmdLen += 1
            self.cmdStr += cmdStr
            self.cmdLen += cmdLen

        if cmd != rc.R_READ_ALL:
            trace(txt)
            print(txt)
            stdout.flush()

    def riscvGetDbg(self, length):
        cmd = "%x %s\r" % (rc.R_READ_DBG, length)
        cmdStr = "\x01%02x" % len(cmd) + cmd

        self.commLock.acquire(True)

        self.ser.write(cmdStr.encode())
        rsp = self.ser.read(3).decode('utf8')
        if len(rsp) == 0:
            self.commLock.release()
            if not self.timeout:
                self.timeout = True
                print("timeout")
                stdout.flush()
            raise CommTimeout()

        rspLen = int(rsp[1:3], 16)
        rsp = self.ser.read(rspLen)
        self.commLock.release()
        return rsp

def renameVar(name):
    val = name.split("_")
    varName = ""
    first = True
    for s in val:
        if first:
            varName = s.lower()
            first = False
        else:
            varName = varName + s.capitalize()
    return varName

RP_TURN  = en.RP_Z_TURN  - en.RP_Z_BASE
RP_TAPER = en.RP_Z_TAPER - en.RP_Z_BASE

class Axis():
    def __init__(self, name, axis, stepsInch, accel, parm):
        self.name       = name
        self.axis       = axis
        self.stepsInch  = stepsInch
        self.accel      = accel
        self.parm       = parm
        self.homeOffset = 0
        self.savedLoc   = 0
        self.turnAccel  = None
        self.taperAccel = None
        self.accelBase  = 0
        if axis == Z_AXIS:
            self.accelBase = en.RP_Z_BASE
        if axis == X_AXIS:
            self.accelBase = en.RP_X_BASE

class RiscvLathe(Thread):
    def __init__(self, comm, mainFrame):
        Thread.__init__(self)
        print("PiLathe __init__")
        self.comm = comm
        self.riscvCmd = comm.riscvCmd
        self.mf = mainFrame
        mainFrame.updateThread = self
        self.threadRun = True
        self.threadDone = False
        self.cmdAction = [None] * len(cmdTable)
        for index, (cmd, action) in enumerate(cmdTable):
            if action is not None:
                if hasattr(self, action):
                    self.cmdAction[index] = getattr(self, action)
                else:
                    print("missing action %s" % (action))

        self.mvCtl = [None] * len(en.mStatesList)
        for i, name in enumerate(en.mStatesList[:-1]):
            stateName = renameVar(name.replace("M_", "mv_"))
            if hasattr(self, stateName):
                x = getattr(self, stateName)
                self.mvCtl[i] = x
            else:
                print("routine %s missing" % (stateName))

        self.move = [None] * len(en.mCommandsList)
        for i, name in enumerate(en.mCommandsList):
            stateName = renameVar(name)
            if hasattr(self, stateName):
                x = getattr(self, stateName)
                self.move[i] = x
            else:
                print("routine %s missing" % (stateName))

        print("initialize parameters")
        for (index, varType, name) in remParmTable:
            # print("index %s name %s" % (index, name))
            setattr(self, name, None)
        self.parm = RemParm()

        self.dbg = None
        self.baseTime = None
        self.mIdle = False
        self.passVal = None
        self.encoderCount = None
        self.lastAxis = None

        self.xCmd = None
        self.xExp = None
        self.xLoc = None
        self.xIntLoc = None
        self.xDro = None
        self.xDist = None
        self.xEncoderStart = None
        self.xEncoderCount = None
        self.lastXIdxD = None
        self.lastXIdxP = None

        self.zCmd = None
        self.zExp = None
        self.zLoc = None
        self.zIntLoc = None
        self.zDro = None
        self.zDist = None
        self.zEncoderStart = None
        self.zEncoderCount = None
        self.lastZIdxD = None
        self.lastZIdxP = None

        dbgSetup = ( \
            (en.D_PASS,  self.dbgPass),
            (en.D_DONE,  self.dbgDone),
            (en.D_TEST,  self.dbgTest),
            (en.D_HST,   self.dbgHome),
            (en.D_MSTA,  self.dbgMoveState),
            (en.D_MCMD,  self.dbgMoveCmd),

            (en.D_XMVCM, self.dbgXMovCmd),
            (en.D_XACTL, self.dbgXAxisCtl),
            (en.D_XMOV,  self.dbgXMov),
            (en.D_XCUR,  self.dbgXCur),
            (en.D_XLOC,  self.dbgXLoc),
            (en.D_XDST,  self.dbgXDist),
            (en.D_XSTP,  self.dbgXStp),
            (en.D_XST,   self.dbgXState),
            (en.D_XBSTP, self.dbgXBSteps),
            (en.D_XDRO,  self.dbgXDro),
            (en.D_XPDRO, self.dbgXPDro),
            (en.D_XEXP,  self.dbgXExp),
            (en.D_XERR,  self.dbgXErr),
            (en.D_XWT,   self.dbgXWait),
            (en.D_XDN,   self.dbgXDone),
            (en.D_XEST,  self.dbgXEncStart),
            (en.D_XEDN,  self.dbgXEncDone),
            (en.D_XX,    self.dbgXX),
            (en.D_XY,    self.dbgXY),
            (en.D_XIDXD, self.dbgXIdxD),
            (en.D_XIDXP, self.dbgXIdxP),

            (en.D_ZMVCM, self.dbgZMovCmd),
            (en.D_ZACTL, self.dbgZAxisCtl),
            (en.D_ZMOV,  self.dbgZMov),
            (en.D_ZCUR,  self.dbgZCur),
            (en.D_ZLOC,  self.dbgZLoc),
            (en.D_ZDST,  self.dbgZDist),
            (en.D_ZSTP,  self.dbgZStp),
            (en.D_ZST,   self.dbgZState),
            (en.D_ZBSTP, self.dbgZBSteps),
            (en.D_ZDRO,  self.dbgZDro),
            (en.D_ZPDRO, self.dbgZPDro),
            (en.D_ZEXP,  self.dbgZExp),
            (en.D_ZERR,  self.dbgZErr),
            (en.D_ZWT,   self.dbgZWait),
            (en.D_ZDN,   self.dbgZDone),
            (en.D_ZEST,  self.dbgZEncStart),
            (en.D_ZEDN,  self.dbgZEncDone),
            (en.D_ZX,    self.dbgZX),
            (en.D_ZY,    self.dbgZY),
            (en.D_ZIDXD, self.dbgZIdxD),
            (en.D_ZIDXP, self.dbgZIdxP),
            )
        self.dbgTbl = dbgTbl = [self.dbgNone for _ in range(en.D_MAX)]
        for (index, action) in dbgSetup:
            dbgTbl[index] = action
            # if hasattr(self, action):
            #     self.cmdAction[index] = getattr(self, action)
            # else:
            #     print("missing debug action %s" % (action))

        self.cfgCtl = 0

        self.zAxis = None
        self.xAxis = None

        self.moveQue = Queue()

        self.parm.zLoc = 0
        self.parm.xLoc = 0

        self.curRpm = 0
        self.passVal = 0
        self.droZ = 0
        self.droX = 0
        self.mvStatus = 0
        self.postUpdate = None
        self.dbgDispatch = None
        self.dbgQue = Queue()
        self.startEncoder = False
        self.lastStatus = 0xffffffff
        self.lastZAxisCtl = 0
        self.lastXAxisCtl = 0
        self.freqMult = 8

        self.feedType   = 0
        self.threadFlag = 0
        self.queCount = 0
        self.dbgCount = 0

        self.start()

    def setPostUpdate(self, postUpdate):
        self.postUpdate = postUpdate

    def setDbgDispatch(self, dbgDispatch):
        self.dbgDispatch = dbgDispatch

    # command routines

    def cZMoveAbs(self):         	# 0
        pass

    def cZMoveRel(self):                # 1
        parm = self.parm
        dist = int(parm.zMoveDist * self.zAxis.stepsInch)
        self.riscvCmd(rc.R_MOVE_REL_Z, (dist, parm.zFlag))

    def cZJogMove(self):                # 2
        dist = self.parm.zJogDir * self.zJogInitialDist
        self.riscvCmd(rc.R_JOG_Z, dist)


    def cZJogSpeed(self):               # 3
        pass

    def cZStop(self):                   # 4
        self.riscvCmd(rc.R_STOP_Z)

    def cZHomeFwd(self):                # 6
        pass

    def cZHomeRev(self):                # 7
        pass

    def cXMoveAbs(self):                # 8
        pass

    def cXMoveRel(self):                # 9
        parm = self.parm
        dist = int(parm.xMoveDist * self.xAxis.stepsInch)
        self.riscvCmd(rc.R_MOVE_REL_X, (dist, parm.xFlag))

    def cXJogMove(self):                # 10
        dist = self.parm.xJogDir * self.xJogInitialDist
        self.riscvCmd(rc.R_JOG_X, dist)

    def cXJogSpeed(self):               # 11
        pass

    def cXStop(self):                   # 12
        self.riscvCmd(rc.R_STOP_X)

    def cXHomeFwd(self):                # 14
        pass

    def cXHomeRev(self):                # 15
        pass

    def cSpindleStart(self):            # 16
        parm = self.parm
        cmd = self.riscvCmd
        if self.parm.stepperDrive:
            pass
        else:
            if self.parm.cfgVarSpeed:
                self.pwmDiv = pwmDiv = int(parm.fpgaFrequency / parm.pwmFreq)
                pwmCtr = int(parm.spRpm * pwmDiv / parm.maxSpeed)
                print("spRpm %d pwmDiv %d maxSpeed %d" % \
                      (parm.spRpm, pwmDiv, parm.maxSpeed))
                cmd(rc.R_SET_DATA, (rp.R_PWM_DIV, pwmDiv))
                cmd(rc.R_SET_DATA, (rp.R_PWM_CTR, pwmCtr), flush=True)

            if self.parm.cfgSwitch:
                cmd(rc.R_STR_SPIN, flush=True)

    def cSpindleStop(self):             # 17
        parm = self.parm
        self.riscvCmd(rc.R_STP_SPIN, flush=True)
        if parm.stepperDrive:
            pass
        else:
            if parm.cfgSwitch:
                pass

            if parm.cfgVarSpeed:
                pass

    def cSpindleUpdate(self):           # 18
        parm = self.parm
        pwmCtr = int(parm.spRpm * self.pwmDiv / parm.maxSpeed)
        ic(int(parm.spRpm), pwmCtr, self.pwmDiv, parm.maxSpeed)
        cmd = self.riscvCmd
        cmd(rc.R_SET_DATA, (rp.R_PWM_CTR, int(pwmCtr)))
        cmd(rc.R_UPD_SPIN, flush=True)
        pass

    def cSpindleJog(self):              # 19
        pass

    def cSpindleJogSpeed(self):         # 20
        pass

    def cPauseCmd(self):                # 21
        # self.cmdPause = True
        # self.mvStatus |= ct.MV_PAUSE
        self.riscvCmd(rc.R_PAUSE, flush=True)

    def cResumeCmd(self):               # 22
        # self.cmdPause = False
        # if jogPause & DISABLE_JOG:
        #     jogPause &= ~(PAUSE_ENA_X_JOG | PAUSE_ENA_Z_JOG)
        # self.mvStatus &= ~(ct.MV_PAUSE | ct.MV_MEASURE | \
        #                    ct.MV_READ_X | ct.MV_READ_Z)
        self.riscvCmd(rc.R_RESUME, flush=True)

    def cStopCmd(self):                 # 23
        self.cSpindleStop()
        self.cZStop()
        self.cXStop()
        self.cmdPause = False
        self.mvStatus &= ~(ct.MV_PAUSE | ct.MV_ACTIVE | \
                           ct.MV_X_HOME_ACTIVE | ct.MV_Z_HOME_ACTIVE)
        self.riscvCmd(rc.R_STOP)

    def cDoneCmd(self):                 # 24
        self.riscvCmd(rc.R_DONE, flush=True)

    def cMeasureCmd(self):              # 25
        pass

    def cClearCmd(self):                # 26
        pass

    def cSetup(self):                   # 27
        self.riscvCmd(rc.R_SETUP)

    def cSpindleSetup(self):            # 28
        pass

    def cSyncSetup(self):               # 29
        pass

    def cZSetup(self):                  # 30
        parm = self.parm

        stepsInch = intRound((parm.zMicro * parm.zMotor) / parm.zPitch)
        self.zAxis = zAxis = Axis("z", Z_AXIS, stepsInch, parm.zAccel, parm)
        self.riscvCmd(rc.R_SET_DATA, (rp.R_X_STEPS_INCH, stepsInch))

        self.zTurnAccel    = ac = AccelData(zAxis)
        self.zAxis.turnAccel = ac
        ac.init("turn")

        self.zTaperAccel   = ac = AccelData(zAxis)
        self.zAxis.taperAccel = ac
        ac.init("taper")

        self.zMoveAccel    = ac = AccelData(zAxis)
        ac.init("move", parm.zMoveMin, parm.zMoveMax)

        self.zJogAccel     = ac = AccelData(zAxis)
        ac.init("jog", parm.zJogMin, parm.zJogMax)

        self.zJogSlowAccel = ac = AccelData(zAxis)
        ac.init("slowJog", parm.zHomeSpeed, parm.zHomeSpeed)

        riscvAccelData(self.zMoveAccel,    en.RP_Z_MOVE)
        riscvAccelData(self.zJogAccel,     en.RP_Z_JOG)
        riscvAccelData(self.zJogSlowAccel, en.RP_Z_SLOW)

        stepsSec = self.zJogAccel.stepsSecMax
        self.zJogInitialDist = int(parm.jogTimeInitial * stepsSec)
        self.zJogIncDist = int(parm.jogTimeInc * stepsSec)
        self.zJogMaxDist = int(parm.jogTimeMax * stepsSec)

        self.riscvCmd(rc.R_SET_DATA, (rp.R_Z_JOG_INC, parm.zMpgInc))

    def cZSetLoc(self):                 # 32
        self.riscvCmd(rc.R_SET_LOC_Z, self.parm.zLoc)

    def cXSetup(self):                  # 33
        parm = self.parm

        stepsInch = (intRound((parm.xMicro * parm.xMotor) / parm.xPitch))
        self.xAxis = xAxis = Axis("x", X_AXIS, stepsInch, parm.xAccel, parm)
        self.riscvCmd(rc.R_SET_DATA, (rp.R_X_STEPS_INCH, stepsInch))

        self.xTurnAccel    = ac = AccelData(xAxis)
        self.xAxis.turnAccel = ac
        ac.init("turn")

        self.xTaperAccel   = ac = AccelData(xAxis)
        self.xAxis.taperAccel = ac
        ac.init("taper")

        self.xMoveAccel    = ac = AccelData(xAxis)
        ac.init("move", parm.xMoveMin, parm.xMoveMax)

        self.xJogAccel     = ac = AccelData(xAxis)
        ac.init("jog", parm.xJogMin, parm.xJogMax)

        self.xJogSlowAccel = ac = AccelData(xAxis)
        ac.init("slowJog", parm.xHomeSpeed, parm.xHomeSpeed)

        riscvAccelData(self.xMoveAccel,    en.RP_X_MOVE)
        riscvAccelData(self.xJogAccel,     en.RP_X_JOG)
        riscvAccelData(self.xJogSlowAccel, en.RP_X_SLOW)

        stepsSec = self.xJogAccel.stepsSecMax
        self.xJogInitialDist = int(parm.jogTimeInitial * stepsSec)
        self.xJogIncDist = int(parm.jogTimeInc * stepsSec)
        self.xJogMaxDist = int(parm.jogTimeMax * stepsSec)

        self.riscvCmd(rc.R_SET_DATA, (rp.R_X_JOG_INC, parm.xMpgInc))
        self.riscvCmd(rc.R_SET_DATA, (rp.R_JOG_PAUSE, 0))

    def cXSetLoc(self):                 # 35
        self.riscvCmd(rc.R_SET_LOC_X, self.parm.xLoc)

    def cClearQue(self):                # 43
        pass

    def cReadAll(self):                 # 47
        pass

    def cReadDbg(self):                 # 48
        pass

    def cClearDbg(self):        	# 49
        pass

    def cSendDone(self):        	# 54
        cfgLookup = (("zDirInv",   bt.cfgZDirInv),
                     ("xDirInv",   bt.cfgXDirInv),
                     ("zDroInvert", bt.cfgZDroInv),
                     ("xDroInvert", bt.cfgXDroInv),
                     ("zMpgInv",    bt.cfgZMpgInv),
                     ("xMpgInv",    bt.cfgXMpgInv),
                     ("zLimNegInv", bt.cfgZMinusInv),
                     ("zLimPosInv", bt.cfgZPlusInv),
                     ("xLimNegInv", bt.cfgXMinusInv),
                     ("xLimPosInv", bt.cfgXPlusInv),
                     ("zHomeInv",   bt.cfgZHomeInv),
                     ("xHomeInv",   bt.cfgXHomeInv),
                     ("probeInv",   bt.cfgProbeInv),
                     ("eStopEna",   bt.cfgEStopEna),
                     ("eStopInv",   bt.cfgEStopInv),
                     ("droStep",    bt.cfgDroStep),
                     )
        parm = self.parm
        cfgVal = 0
        txt = "cfg "
        for varName, flag in cfgLookup:
            val = getattr(parm, varName)
            print("%-12s %6x %s" % (varName, flag, val))
            if val is None:
                continue
            if val != 0:
                txt += " " + varName
                cfgVal |= flag
        print("%6x %s" % (cfgVal, txt))

        # cfgVal = bt.cfgDroStep | bt.cfgXDroInv | bt.cfgZDroInv

        self.riscvCmd(rc.R_SET_DATA, (rp.R_CFG_VAL, cfgVal))
        self.riscvCmd(rc.R_SEND_DONE)

    # def setZLoc(self, loc):
    #     self.parm.zLoc = loc

    # def getZLoc(self):
    #     return self.parm.zLoc

    # def setXLoc(self, loc):
    #     self.parm.xLoc = loc

    # def getXLoc(self):
    #     return self.parm.xLoc

    # def spSetup(self):
    #     pass

    # def xHomeAxis(self):
    #     pass

    def dbgMsg(self, cmd, val):
        # self.dbgQue.put((time(), cmd, val))
        self.dbgDispatch(time(), cmd, val)

    # move queue

    def run(self):
        self.cmdPause = False
        self.mvState = en.M_IDLE
        self.mvLastState = en.M_IDLE

        while self.parm.fpgaFrequency is None:
            if not self.threadRun:
                break
            sleep(0.1)
        self.jp = self.comm.jp

        while self.parm.encPerRev is None:
            if not self.threadRun:
                break
            sleep(0.1)
        self.encoderCount = self.parm.encPerRev

        if self.mf.dbgSave:
            print("***start saving debug***")
            self.openDebug()

        print("RiscvLathe starting loop")
        while True:
            stdout.flush()
            sleep(0.1)
            if not self.threadRun:
                break
            self.procMove()
            self.update()
            if self.dbgCount > 0:
                self.procDebug()
        print("RiscvLathe done")
        stdout.flush()
        self.threadDone = True

    def close(self):
        self.threadRun = False
        print("RiscvLathe threadRun %s" % (self.threadRun, ))
        while not self.threadDone:
            print("waiting for threadDone")
            stdout.flush()
            sleep(0.1)
        return

    def update(self):
        rsp = ""
        try:
            self.comm.riscvSend() # flush current commands
            self.riscvCmd(rc.R_READ_ALL)
            rsp = self.comm.riscvSend()
            if (self.postUpdate is not None) and len(rsp) >= 7:
                parm = int(rsp[5:7], 16)
                if parm == rc.R_READ_ALL:
                    splitRsp = rsp[7:-1].split(' ')
                    (z, x, rpm, curPass, droZ, droX, mvStatus, \
                     dbgCount) = splitRsp[1:9]
                    z        = c_int32(int(z, 16)).value
                    x        = c_int32(int(x, 16)).value
                    rpm      = int(rpm, 16)
                    curPass  = int(curPass, 16)
                    droZ     = c_int32(int(droZ, 16)).value
                    droX     = c_int32(int(droX, 16)).value
                    mvStatus = int(mvStatus, 16)
                    self.dbgCount = int(dbgCount, 16)
                    if self.dbgCount > 0:
                        print("dbgCount", self.dbgCount)
                        print(rsp)
                    result = (en.EV_READ_ALL, z, x, rpm, curPass,
                              droZ, droX, mvStatus)
                    self.postUpdate(result)
        except ValueError:
            print("readAll ValueError ", rsp)
            stdout.flush()
        except CommTimeout:
            pass

    def procMove(self):
        if self.cmdPause and self.mvState == en.M_IDLE:
            return
        # noinspection PyCallingNonCallable
        self.mvCtl[self.mvState]()
        if self.mvState != self.mvLastState:
            self.mvLastState = self.mvState
            trace("move   state %s" % (en.mStatesList[self.mvState]))
            # self.dbgMsg(en.D_MSTA, self.mvState)

    def mvIdle(self):
        while self.moveQue.qsize() != 0:
            if self.queCount < 8:
                break
            try:
                print("que size %d queCount %d" % \
                      (self.moveQue.qsize(), self.queCount))
                (opString, op, val) = self.moveQue.get(False)
                print("moveQue get op %6x %-18s %s" % (op, opString, str(val)))
                self.cmdFlag = op >> 16
                op &= 0xff
                self.cmd = op
                if True:
                    if type(val) == 'float':
                        valString = "%13.6f" % val
                        valString = re.sub("0+$", "", valString)
                        if valString.endswith('.'):
                            valString += '0'
                    else:
                        valString = "%6d" % val
                    txt = ("%-16s %2d %2d %-7s" % \
                           (opString, op, self.cmdFlag, valString))
                    trace(txt)
                    print(txt)
                    stdout.flush()
                # self.dbgMsg(en.D_MCMD, (self.cmdFlag << 8) | op)
                # noinspection PyCallingNonCallable
                self.move[op](val)
            # except IndexError:
            #     print("IndexError")
            #     exit()
            except Empty:
                return

            if self.mvState != en.M_IDLE or self.cmdPause:
                break

    # move queue routines

    def qMoveZ(self, val):       	# 0
        dest = val + self.zAxis.HomeOffset
        fDest = (dest - self.xAxis.HomeOffset) / self.xAxis.stepsInch
        # self.dbgMsg(en.D_ZMOV, val)
        print("moveZ dest %7.4f %d val %d zStepsInch %d zHomeOffset %d" % \
              (fDest, dest, val, self.zAxis.stepsInch, self.zAxis.HomeOffset))

        # self.mvState = en.M_WAIT_Z
        # self.zAxis.move(dest, self.cmdFlag)

        # self.zAxis.riscvSetup(self.cmdFlag)
        self.riscvCmd(rc.R_MOVE_Z, (self.cmdFlag, dest))
        # self.riscvCmd(rc.R_WAIT_Z, flush=True)

    def qMoveX(self, val):              # 1
        dest = val + self.xAxis.HomeOffset
        fDest = (dest - self.xAxis.HomeOffset) / self.xAxis.stepsInch
        # self.dbgMsg(en.D_XMOV, val)
        print("moveX dest %7.4f %d val %d xStepsInch %d xHomeOffset %d" % \
              (fDest, dest, val, self.xAxis.stepsInch, self.xAxis.HomeOffset))
        # self.dbgMsg(en.D_XMOV, dest)

        # self.mvState = en.M_WAIT_X
        # self.xAxis.move(dest, self.cmdFlag)

        # self.zAxis.riscvSetup(self.cmdFlag)
        self.riscvCmd(rc.R_MOVE_X, (self.cmdFlag, dest))
        # self.riscvCmd(rc.R_WAIT_X, flush=True)

    def qSaveZ(self, val):              # 2
        print("save z %7.4f" % (val))
        self.zAxis.savedLoc = loc = \
            (intRound(val * self.zAxis.stepsInch) + self.zAxis.HomeOffset)
        self.riscvCmd(rc.R_SET_DATA_Q, (rp.R_X_SAVED_LOC, loc))

    def qSaveX(self, val):              # 3
        print("save x %7.4f" % (val))
        self.xAxis.savedLoc = loc = \
            (intRound(val * self.xAxis.stepsInch) + self.xAxis.HomeOffset)
        self.riscvCmd(rc.R_SET_DATA_Q, (rp.R_Z_SAVED_LOC, loc))

    def qSaveZOffset(self, val):        # 4
        print("save z offset %7.4f" % (float(val) / self.zAxis.stepsInch))
        self.riscvCmd(rc.R_SET_DATA, (rp.R_Z_HOME_OFFSET, val))
        self.zAxis.HomeOffset = val

    def qSaveXOffset(self, val):        # 5
        print("save x offset %7.4f" % (float(val) / self.xAxis.stepsInch))
        self.riscvCmd(rc.R_SET_DATA, (rp.R_X_HOME_OFFSET, val))
        self.xAxis.HomeOffset = val

    def qSaveTaper(self, val):          # 6
        print("save taper %7.4f" % (val))
        self.taper = val

    # noinspection PyMethodMayBeStatic,PyUnusedLocal
    def qMoveZX(self, val):             # 7
        print("moveZX")

    # noinspection PyMethodMayBeStatic,PyUnusedLocal
    def qMoveXZ(self, val):             # 8
        print("moveXZ")

    def qTaperZX(self, val):            # 9
        print("taper zx %7.4f" % (val))
        if self.currentPass == 1:
            self.taperSetup(self.zAxis, self.xAxis)
        loc = intRound(val * self.zAxis.stepsInch) + self.zAxis.homeOffset
        riscvCmd(rc.R_MOVE_Z, (ct.CMD_SYN | ct.SYN_START | ct.SYN_TAPER, loc))

    def qTaperXZ(self, val):            # 10
        print("taper xz %7.4f" % (val))
        if self.currentPass == 1:
            self.taperSetup(self.xAxis, self.zAxis)
        loc = intRound(val * self.xAxis.stepsInch) + self.xAxis.homeOffset
        riscvCmd(rc.R_MOVE_X, (ct.CMD_SYN | ct.SYN_START | ct.SYN_TAPER, loc))

    def taperSetup(self, mvAxis, tpAxis):
        print("taperSetup")
        tpAxis.taper = self.taper

        if self.parm.turnSync == en.SEL_TU_ENC:
            taperCalc(mvAxis.turnAccel, tpAxis.taperAccel, self.taper)
            riscvAccelData(tpAxis.taperAccel, tpAxis.accelBase + RP_TAPER,
                           que=True)
        elif self.parm.turnSync == en.SEL_TU_SYN:
            self.mvState = en.M_START_SYNC

        # loc = intRound(val * mvAxis.stepsInch) + mvAxis.homeOffset
        # dist = tpAxis.savedLoc - tpAxis.loc
        # print("tpAxis.savedLoc %d tpAxis.loc %d dist %d" %
        #       (tpAxis.savedLoc, tpAxis.loc, dist))
        # tpAxis.axisCtl = (bt.ctlSlave | \
        #                   (DIR_POS if dist > 0 else 0))
        # mvDist = abs(float(dist) / mvAxis.stepsInch)
        # tpAxis.taperDist = intRound(mvDist * taper * tpAxis.stepsInch)
        # print("mvDist %7.4f taper %0.6f tpAxis.taperDist %d" % \
        #       (mvDist, taper, tpAxis.taperDist))
        # taperCalc(mvAxis.turnAccel, tpAxis.taperAccel, taper)
        # mvAxis.move(loc, ct.CMD_SYN | ct.SYN_START | ct.SYN_TAPER)

    # noinspection PyUnusedLocal
    def qStartSpindle(self, val):       # 11
        print("startSpindle")
        # self.mvSpindleCmd = self.cmd
        # self.spindleStart()
        # self.mvState = en.M_WAIT_SPINDLE
        self.riscvCmd(rc.R_STR_SPIN)

    # noinspection PyUnusedLocal
    def qStopSpindle(self, val):        # 12
        print("stopSpindle")
        # self.mvSpindleCmd = self.cmd
        # self.spindleStop()
        # self.mvState = en.M_WAIT_SPINDLE
        self.riscvCmd(rc.R_STP_SPIN)

    def qZSynSetup(self, val):          # 13
        print("zSynSetup")
        self.zFeed = val
        print("zFeed %7.3f currentOp %d %s turnSync %d %s\n" % \
              (self.zFeed,
               self.parm.currentOp, en.operationsList[self.parm.currentOp],
               self.parm.turnSync, en.selTurnList[self.parm.turnSync]))
        currentOp = self.parm.currentOp
        if currentOp == en.OP_TURN:
            pass
        elif currentOp == en.OP_TAPER:
            pass
        elif currentOp == en.OP_THREAD:
            pass

        axis = self.zAxis
        if self.parm.turnSync == en.SEL_TU_ENC:
            self.zAxis.encParm = True
            syncAccelCalc(axis.turnAccel, self.feedType, val)
            riscvAccelData(axis.turnAccel, axis.accelBase + RP_TURN,
                           que=True)
        elif self.parm.turnSync == en.SEL_TU_SYN:
            axis.encParm = False
            self.mvState = en.M_START_SYNC

    def qXSynSetup(self, val):          # 14
        print("xSynSetup")
        self.xFeed = val
        currentOp = self.parm.currentOp
        if currentOp == en.OP_FACE:
            pass
        elif currentOp == en.OP_CUTOFF:
            pass
        elif currentOp == en.OP_TAPER:
            pass
        elif currentOp == en.OP_THREAD:
            pass

        axis = self.xAxis
        if self.parm.turnSync == en.SEL_TU_ENC:
            axis.encParm = True
            syncAccelCalc(axis.turnAccel, self.feedType, val)
            riscvAccelData(axis.turnAccel, axis.accelBase + RP_TURN,
                           que=True)
        else:
            axis.encParm = False
            self.mvState = en.M_START_SYNC

    # noinspection PyMethodMayBeStatic,PyUnusedLocal
    def qSendSyncParms(self, val):      # 15
        print("sendSyncParms")

    # noinspection PyMethodMayBeStatic,PyUnusedLocal
    def qSyncCommand(self, val):        # 16
        print("syncCommand")

    def qPassNum(self, val):            # 17
        print("passNum")
        self.passVal = val
        if (val & 0xff00) == 0:
            self.currentPass = val & 0xff
        else:
            self.springInfo = val
        # self.dbgMsg(en.D_PASS, val)
        self.riscvCmd(rc.R_PASS, val)

    # noinspection PyUnusedLocal
    def qQuePause(self, val):           # 18
        print("quePause")
        # self.cmdPause = True
        # self.mvStatus |= ct.MV_PAUSE
        self.riscvCmd(rc.R_PAUSE)

    # noinspection PyMethodMayBeStatic,PyUnusedLocal
    def qMoveZOffset(self, val):        # 19
        print("moveZOffset")

    def qSaveFeedType(self, val):       # 20
        print("saveFeedType")
        self.feedType = val

    # noinspection PyMethodMayBeStatic,PyUnusedLocal
    def qZFeedSetup(self, val):         # 21
        print("zFeedSetup")

    # noinspection PyMethodMayBeStatic,PyUnusedLocal
    def qXFeedSetup(self, val):         # 22
        print("xFeedSetup")

    def qSaveFlags(self, val):          # 23
        print("saveFlags")
        self.threadFlag = val

    # noinspection PyMethodMayBeStatic,PyUnusedLocal
    def qProbeX(self, val):             # 24
        print("probeX")

    # noinspection PyMethodMayBeStatic,PyUnusedLocal
    def qProbeZ(self, val):             # 25
        print("probeZ")

    # noinspection PyMethodMayBeStatic,PyUnusedLocal
    def qSaveZDro(self, val):           # 26
        print("saveZDro")

    # noinspection PyMethodMayBeStatic,PyUnusedLocal
    def qSaveXDro(self, val):           # 27
        print("saveXDro")

    # noinspection PyMethodMayBeStatic,PyUnusedLocal
    def qQueParm(self, val):            # 28
        print("queParm")

    # noinspection PyMethodMayBeStatic,PyUnusedLocal
    def qMoveArc(self, val):            # 29
        print("moveArc")

    def qOpDone(self, val):             # 30
        print("opDone")
        # self.dbgMsg(en.D_DONE, val)
        if val == ct.PARM_START:
            # self.mvStatus &= ~ct.MV_DONE
            # self.mvStatus |= ct.MV_ACTIVE
            self.riscvCmd(rc.R_OP_START)

        elif val == ct.PARM_DONE:
            # self.mvStatus &= ~ct.MV_ACTIVE
            # self.mvStatus |= ct.MV_DONE
            self.riscvCmd(rc.R_OP_DONE)

    # move states

    def mvWaitZ(self):          # 1
        pass
        # if self.zAxis.state == en.AXIS_IDLE:
        #     self.mvState = en.M_IDLE

    def mvWaitX(self):          # 2
        pass
        # if self.xAxis.state == en.AXIS_IDLE:
        #     self.mvState = en.M_IDLE

    def mvWaitSpindle(self):    # 3
        pass
        # indexClks = self.rd(rg.F_Rd_Idx_Clks)
        # if indexClks != self.lastIdxClks:
        #     print("indexClks %d" % (indexClks))
        #     self.lastIdxClks = indexClks
        #     if indexClks != 0:
        #         delta = abs(indexClks - self.lastIdxClks)
        #         percent = float(delta) * 100.0 / indexClks
        #         indexClks += 1
        #         rpm = intRound((float(self.parm.fpgaFrequency) /
        #                         indexClks) * 60)
        #         print("delta %d percent %7.2f rpm %d" % (delta, percent, rpm))
        #         if percent < 1.0:
        #             if self.mvSpindleCmd == en.STOP_SPINDLE:
        #                 self.mvState = en.M_IDLE
        #             elif self.mvSpindleCmd == en.START_SPINDLE:
        #                 self.mvState = en.M_IDLE

    def mvWaitSyncParms(self):  # 4
        pass

    def mvWaitSyncCmd(self):    # 5
        pass

    def mvStartSync(self):      # 6
        pass
        # self.ld(rg.F_Enc_Base + rg.F_Ld_Enc_Cycle, self.parm.lSyncCycle)
        # self.ld(rg.F_Enc_Base + rg.F_Ld_Int_Cycle, self.parm.lSyncOutput)
        # self.ld(rg.F_Ld_Sync_Ctl, bt.synEncInit)
        # self.ld(rg.F_Ld_Sync_Ctl, bt.synEncEna)
        # self.mvState = en.M_WAIT_SYNC_READY

    def mvWaitSyncReady(self):  # 7
        pass
        # status = self.rd(rg.F_Rd_Status)
        # if (status & bt.syncActive) != 0:
        #     self.mvState = en.M_IDLE

    def mvWaitSyncDone(self):   # 8
        pass

    def mvWaitMeasureDone(self): # 9
        pass

    def mvWaitProbe(self):      # 10
        pass

    def mvWaitMeasure(self):    # 11
        pass

    def mvWaitSafeX(self):      # 12
        pass

    def mvWaitSafeZ(self):      # 13
        pass

    def mvWaitArc(self):        # 14
        pass

    def openDebug(self, fName="dbg.txt", action=None):
        self.dbg = open(os.path.join(DBG_DIR, fName), "ab")
        t = "\n" + timeStr()
        if action is not None:
            t = t[:-1] + " " + en.operationsList[action] + "\n"
        self.dbg.write(t.encode())
        self.dbg.flush()

    def closeDbg(self):
        if self.dbg is not None:
            self.dbg.close()
            self.dbg = None
            self.baseTime = None

    def procDebug(self):
        try:
            result = self.comm.riscvGetDbg(10)
            if not self.threadRun:
                return(True)
            if result is None:
                return(False)
            if int(result[2:4].decode('utf8'), 16) != rc.R_READ_DBG:
                return(False)
            # if not REM_DBG:
            #     return(False)

            # tmp = result.split()
            # rLen = len(tmp)
            # if rLen > 0:
            #     print("%2d (%s)" % (rLen, result))
            rLen = len(result) - 1
            index = 4
            if rLen > 4:
                print("rLen %d" % (rLen))
                j = 0
                for i in range(index, rLen):
                    if j == 5:
                        j = 0
                        print("| ", end = "")
                    print("%02x " % (result[i]), end="")
                    j += 1
                print()
            t = (("%8.3f " % (time() - self.baseTime))
                 if self.baseTime is not None else "   0.000 ")
            while index < rLen:
                cmd = result[index]
                for i in range(5):
                    print("%02x " % (result[index + i]), end="")
                print()
                val = int.from_bytes(result[index+1:index+5],
                                     byteorder='little', signed=True)
                print("cmd %d %s val %d" % (cmd, en.dMessageList[cmd], val))
                stdout.flush()
                # (cmd, val) = tmp[index-2:index]
                # index += 2
                index += 5
                try:
                    # cmd = int(cmd, 16)
                    # val = int(val, 16)
                    # print("c %2x val %4x" % (cmd, val))
                    try:
                        action = self.dbgTbl[cmd]
                        assert (callable(action))
                        axis = (None if cmd < en.D_XBASE else \
                                X_AXIS if cmd < en.D_ZBASE else Z_AXIS)
                        if (self.lastAxis is not None) and (axis is not None):
                            if axis != self.lastAxis:
                                if self.dbg is None:
                                    print()
                                else:
                                    self.dbg.write("\n".encode())
                        self.lastAxis = axis
                        # noinspection PyArgumentList
                        output = action(val)
                        print("***" + t + output)
                        stdout.flush()
                        if output is not None:
                            if self.dbg is None:
                                print(t + output)
                                stdout.flush()
                            else:
                                self.dbg.write((t + output + "\n").encode())
                                self.dbg.flush()
                        # if cmd == en.D_DONE:
                        #     if val == 0:
                        #         if not self.jp.currentPanel.control.addEnabled:
                        #             self.baseTime = time()
                        #     if val == 1:
                        #         self.baseTime = None
                        #         if self.dbg is not None:
                        #             self.dbg.close()
                        #             self.dbg = None
                    except IndexError:
                        print("procDebug IndexError %s" % result)
                        stdout.flush()
                    except TypeError:
                        print("procDebug TypeError %s %s" % \
                              (en.dMessageList[cmd], result))
                        stdout.flush()
                except ValueError:
                    print("procDebug ValueError cmd %s val %s" % (cmd, val))
                    stdout.flush()
        except CommTimeout:
            print("procDebug getString CommTimeout")
            stdout.flush()
        except serial.SerialException:
            print("procDebug getString SerialException")
            stdout.flush()
            return(True)

    def dbgDispatch(self, t0, cmd, val):
        try:
            action = self.dbgTbl[cmd]
            output = action(val)
            if output is not None:
                t = (("%8.3f " % (t0 - self.baseTime))
                     if self.baseTime is not None else "   0.000 ")
                if self.dbg is None:
                    print(t + output)
                    stdout.flush()
                else:
                    self.dbg.write((t + output + "\n").encode())
                    self.dbg.flush()
        except IndexError:
            print("dbgDispatch IndexError %d" % cmd)
            stdout.flush()
        except TypeError:
            print("dbgDispatch TypeError %s %s" % \
                  (en.dMessageList[cmd], str(val)))
            stdout.flush()

    # noinspection PyMethodMayBeStatic,PyUnusedLocal
    def dbgNone(self, val):
        return "none"

    def dbgPass(self, val):
        # tmp = val >> 8
        # if tmp == 0:
        #     return("pass %d\n")
        # elif tmp == 1:
        #     return("spring\n")
        # elif tmp == 2:
        #     return("spring %d\n" % (val & 0xff))
        self.passVal = val
        self.lastXIdxD = None
        self.lastXIdxP = None
        self.lastZIdxD = None
        self.lastZIdxP = None
        result = "spring\n" if val & 0x100 else \
                 "spring %d\n" % (val & 0xff) if val & 0x200 else \
                 "pass %d\n" % (val)
        return(result)

    def dbgDone(self, val):
        if val == ct.PARM_START:
            if not self.jp.currentPanel.control.addEnabled:
                self.baseTime = time()
            return("strt " + timeStr())
        elif val == ct.PARM_DONE:
            return("done " + timeStr())

    # noinspection PyMethodMayBeStatic
    def dbgTest(self, val):
        return("test %d" % (val))

    # noinspection PyMethodMayBeStatic
    def dbgHome(self, val):
        return("hsta %s" % (en.hStatesList[val]))

    def dbgMoveState(self, val):
        self.mIdle = val == en.RW_NONE
        return("msta %s" % (en.riscvRunWaitList[val]
                            + ("\n" if self.mIdle else "")))

    # noinspection PyMethodMayBeStatic
    def dbgMoveCmd(self, val):
        if (val & 0xff00) == 0:
            return("mcmd %s" % (rc.cmdTable[val][0]))
        else:
            return("mcmd %s %02x" % (rc.cmdTable[val & 0xff][0], val >> 8))

    # x axis ****************************************

    # noinspection PyMethodMayBeStatic
    def dbgXMovCmd(self, val):  # move command
        self.xCmd = val
        cmd = val & ct.CMD_MSK
        bits  = val & ~ct.CMD_MSK
        mask = (1 << (en.M_BIT_MAX-1))
        bitList = ""
        for i in range(en.M_BIT_MAX-1, 0, -1):
            bitList += (en.moveBitList[i] + " ") if (bits & mask) != 0 else ""
            mask >>= 1
        return("xcmd %-11s %02x %s" % (en.moveCmdList[cmd], val, bitList.rstrip()))

    # noinspection PyMethodMayBeStatic
    def dbgXAxisCtl(self, val):
        return "xctl    %04x %s" % (val, prtAxisCtl(val))

    def dbgXMov(self, val):     # move to location
        tmp = float(val) / self.mf.xStepsInch - self.jp.xHomeOffset
        return("xmov %7.4f %7.4f" % (tmp, tmp * 2.0))

    def dbgXCur(self, val):     # move current location
        tmp = float(val) / self.mf.xStepsInch - self.jp.xHomeOffset
        return("xloc %7.4f %7.4f" % (tmp, tmp * 2.0))

    def dbgXLoc(self, val):     # end of move location
        iTmp = int(val)
        self.xIntLoc = iTmp
        tmp = float(val) / self.mf.xStepsInch - self.jp.xHomeOffset
        self.xLoc = tmp
        # if self.xDro is not None:
        if self.xExp is not None:
            diff = " diff %7.4f" % (self.xExp - tmp)
            self.xDro = None
        else:
            diff = ""
        return("xloc %7.4f %7.4f %7d%s" % (tmp, tmp * 2.0, iTmp, diff))

    def dbgXDist(self, val):     # move distance
        tmp = float(val) / self.mf.xStepsInch
        return("xdst %7.4f %7d" % (tmp, val))

    def dbgXStp(self, val):     # move steps
        dist = float(val) / self.mf.xStepsInch
        if self.xEncoderCount is None or self.xEncoderCount == 0:
            return("xstp %7.4f %7d" % (dist, val))
        else:
            pitch = dist / (float(self.xEncoderCount) / self.encoderCount)
            self.xEncoderCount = None
            return("xstp %7.4f %7d pitch %7.4f" % (dist, val, pitch))

    def dbgXState(self, val):
        return(("x_st %s" % (en.RiscvAxisStateTypeList[val])) + \
                ("\n" if self.mIdle and val == en.RS_IDLE else ""))

    def dbgXBSteps(self, val):
        tmp = float(val) / self.mf.xStepsInch
        return("xbst %7.4f %7d" % (tmp, val))

    def dbgXDro(self, val):
        tmp = float(val) / self.jp.xDROInch - self.jp.xDROOffset
        self.xDro = tmp
        return("xdro %7.4f %7.4f %7d" % (tmp, tmp * 2.0, val))

    def dbgXPDro(self, val):
        tmp = float(val) / self.jp.xDROInch - self.jp.xDROOffset
        passVal = self.passVal
        spring = (passVal & 0xf00) >> 8
        passVal &= 0xff
        if spring == 0:
            spring = "  "
        else:
            spring = "s" + str(spring)
        s = "pass %s %2d xdro %7.4f xloc %7.4f diff %7.4f" % \
            (spring, passVal, tmp * 2.0, self.xLoc * 2.0, self.xLoc - tmp)
        self.jp.mf.dPrt(s + "\n", flush=True)
        return("xpdro " + s)

    def dbgXExp(self, val):     # expected location
        tmp = float(val) / self.mf.xStepsInch - self.jp.xHomeOffset
        self.xExp = tmp
        return("xexp %7.4f" % (tmp))

    def dbgXErr(self, val):
        tmp = float(val) / self.mf.xStepsInch
        return("xerr %7.4f" % (tmp))

    # noinspection PyMethodMayBeStatic
    def dbgXWait(self, val):
        return("xwt  %2x" % (val))

    # noinspection PyMethodMayBeStatic
    def dbgXDone(self, val):
        return("xdn  %2x" % (val))

    def dbgXEncStart(self, val):
        self.xEncoderStart = val
        return(None)

    # noinspection PyMethodMayBeStatic
    def dbgXX(self, val):
        return("x_x  %7d" % (val))

    # noinspection PyMethodMayBeStatic
    def dbgXY(self, val):
        return("x_y  %7d %7.4f" % (val, float(val) / self.mf.xStepsInch))

    def dbgXEncDone(self, val):
        if self.xEncoderStart is None:
            return(None)
        count = c_uint32(val - self.xEncoderStart).value
        self.xEncoderCount = count
        return("xedn %7.2f %7d" % (float(count) / self.encoderCount, count))

    def dbgXIdxD(self, val):
        result = "xixd %7.4f" % (float(val) / self.jp.xDROInch - \
                                 self.jp.xDROOffset)

        if self.lastXIdxD is not None:
            delta = abs(self.lastXIdxD - val)
            result += " %7.4f %6d %5d" % (delta / self.jp.xDROInch, val, delta)
        self.lastXIdxD = val
        return(result)

    def dbgXIdxP(self, val):
        result = "xixp %7.4f" % (float(val) / self.jp.xStepsInch - \
                                 self.jp.xHomeOffset)

        if self.lastXIdxP is not None:
            delta = abs(self.lastXIdxP - val)
            result += " %7.4f %6d %5d" % \
                (delta / self.jp.xStepsInch, val, delta)
        self.lastXIdxP = val
        return(result)

    # z axis ****************************************

    # noinspection PyMethodMayBeStatic
    def dbgZMovCmd(self, val):
        self.zCmd = val
        cmd = val & ct.CMD_MSK
        bitList = ""
        bits  = val & ~ct.CMD_MSK
        mask = (1 << (en.M_BIT_MAX-1))
        for i in range(en.M_BIT_MAX-1, 0, -1):
            bitList += (en.moveBitList[i] + " ") if (bits & mask) != 0 else ""
            mask >>= 1
        return("zcmd %-11s %02x %s" % \
               (en.moveCmdList[cmd], val, bitList.rstrip()))

    # noinspection PyMethodMayBeStatic
    def dbgZAxisCtl(self, val):
        return "zctl    %04x %s" % (val, prtAxisCtl(val))

    def dbgZMov(self, val):
        tmp = float(val) / self.mf.zStepsInch - self.jp.zHomeOffset
        return("zmov %7.4f" % (tmp))

    def dbgZCur(self, val):
        tmp = float(val) / self.mf.zStepsInch - self.jp.zHomeOffset
        return("zloc %7.4f" % (tmp))

    def dbgZLoc(self, val):
        iTmp = int(val)
        self.zIntLoc = iTmp
        tmp = float(val) / self.mf.zStepsInch - self.jp.zHomeOffset
        self.zLoc = tmp
        # if self.zDro is not None:
        if self.zExp is not None:
            diff = " diff %7.4f" % (self.zExp - tmp)
            self.zDro = None
        else:
            diff = ""
        return("zloc %7.4f %7d %s" % (tmp, iTmp, diff))

    def dbgZDist(self, val):
        tmp = float(val) / self.mf.zStepsInch
        self.zDist = tmp
        return("zdst %7.4f %7d" % (tmp, val))

    def dbgZStp(self, val):
        dist = float(val) / self.mf.zStepsInch
        if self.zEncoderCount is None or self.zEncoderCount == 0:
            return("zstp %7.4f %7d" % (dist, val))
        else:
            pitch = dist / (float(self.zEncoderCount) / self.encoderCount)
            self.zEncoderCount = None
            return("zstp %7.4f %7d pitch %7.4f" % (dist, val, pitch))

    def dbgZState(self, val):
        if self.jp.currentPanel.active:
            return(("z_st %s" % (en.RiscvAxisStateTypeList[val])) + \
                   ("\n" if self.mIdle and val == en.RS_IDLE else ""))
        else:
            rtnVal = "z_st %s" % (en.RiscvAxisStateTypeList[val])
            if val == en.RS_IDLE:
                self.baseTime = None
                rtnVal += "\n"
            elif self.baseTime is None:
                self.baseTime = time()
            return(rtnVal)

    def dbgZBSteps(self, val):
        tmp = float(val) / self.mf.zStepsInch
        return("zbst %7.4f %7d" % (tmp, val))

    def dbgZDro(self, val):
        tmp = float(val) / self.jp.zDROInch - self.jp.zDROOffset
        self.zDro = tmp
        return("zdro %7.4f" % (tmp))

    def dbgZPDro(self, val):
        tmp = float(val) / self.jp.zDROInch - self.jp.zDROOffset
        passVal = self.passVal
        spring = (passVal & 0xf00) >> 8
        passVal &= 0xff
        if spring == 0:
            spring = "  "
        else:
            spring = "s" + str(spring)
        s = "pass %s %2d zdro %7.4f zloc %7.4f diff %7.4f" % \
            (spring, passVal, tmp, self.zLoc, self.zLoc - tmp)
        self.jp.mf.dPrt(s + "\n", flush=True)
        return("zpdro " + s)

    def dbgZExp(self, val):
        tmp = float(val) / self.mf.zStepsInch - self.jp.zHomeOffset
        self.zExp = tmp
        return("zexp %7.4f" % (tmp))

    def dbgZErr(self, val):
        tmp = float(val) / self.mf.zStepsInch
        return("zerr %7.4f" % (tmp))

    # noinspection PyMethodMayBeStatic
    def dbgZWait(self, val):
        return("zwt  %2x" % (val))

    # noinspection PyMethodMayBeStatic
    def dbgZDone(self, val):
        return("zdn  %2x" % (val))

    def dbgZEncStart(self, val):
        self.zEncoderStart = val
        return(None)

    def dbgZEncDone(self, val):
        if self.zEncoderStart is None:
            return(None)
        count = c_uint32(val - self.zEncoderStart).value
        self.zEncoderCount = count
        return("zedn %7.2f %7d" % (float(count) / self.encoderCount, count))

    def dbgZX(self, val):
        if (self.zCmd is not None and self.zDist is not None and \
            ((self.zCmd & ct.CMD_MSK) == ct.CMD_SYN)):
            rev = val / self.encoderCount
            feed = self.zDist / rev
            return "z_x  %7d rev %5.2f feed %5.4f" % (val, rev, feed)
        else:
            return "z_x  %7d" % (val)

    def dbgZY(self, val):
        return("z_y  %7d %7.4f" % (val, float(val) / self.mf.zStepsInch))

    def dbgZIdxD(self, val):
        result = "zixd %7.4f" % (float(val) / self.jp.zDROInch - \
                                 self.jp.zDROOffset)

        if self.lastZIdxD is not None:
            delta = abs(self.lastZIdxD - val)
            result += " %7.4f %6d %5d" % (delta / self.jp.zDROInch, val, delta)
        self.lastZIdxD = val
        return(result)

    def dbgZIdxP(self, val):
        result = "zixp %7.4f" % (float(val) / self.jp.zStepsInch - \
                                 self.jp.zHomeOffset)

        if self.lastZIdxP is not None:
            delta = abs(self.lastZIdxP - val)
            result += " %7.4f %6d %5d" % \
                (delta / self.jp.zStepsInch, val, delta)
        self.lastZIdxP = val
        return(result)

    def abort(self):
        self.threadRun = False
