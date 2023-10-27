from threading import Thread
from queue import Queue, Empty
# from sys import stdout
from time import sleep, time
# from platform import system
from ctypes import c_int32, c_uint32
from sys import stdout
from threading import Lock
# import os
import re

from accelPi import AccelData, taperCalc, intRound, syncAccelCalc
from remParmDef import parmTable
from remCmdDef import cmdTable
# from remParm import RemParm
import enumDef as en
# import lRegDef as rg
import fpgaLathe as bt
import ctlBitDef as ct
from remParm import RemParm

import serial

Z_AXIS = 0
X_AXIS = 1

DIR_POS = 1

CMD_OVERHEAD = 8
MOVE_OVERHEAD = 8
MAX_CMD_LEN = 80

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

def riscvAccelData(accel, accelType):
    txt = "riscVAccelData %-10s %d" % (en.RiscvAccelTypeList[accelType],
                                       accelType)
    trace(txt)
    print(txt)
    riscvCmd(en.R_SET_ACCEL,
            (accelType << 8 | en.RP_INITIAL_SUM, accel.initialSum))
    riscvCmd(en.R_SET_ACCEL,
            (accelType << 8 | en.RP_INCR1,       accel.incr1))
    riscvCmd(en.R_SET_ACCEL,
            (accelType << 8 | en.RP_INCR2,       accel.incr2))
    riscvCmd(en.R_SET_ACCEL,
            (accelType << 8 | en.RP_ACCEL_VAL,   accel.intAccel))
    riscvCmd(en.R_SET_ACCEL,
            (accelType << 8 | en.RP_ACCEL_COUNT, accel.accelClocks))
    riscvCmd(en.R_SET_ACCEL,
            (accelType << 8 | en.RP_FREQ_DIV,    accel.freqDivider))
    # riscvCmd(en.R_SYNC_PARM, accelType << 8 | en.RP_, accel.)

def enableXilinx():
    pass

class CommRiscv():
    def __init__(self):
        self.ser = None
        self.riscv   = riscv = RiscvLathe(self)
        self.moveQue = self.riscv.moveQue
        self.openSerial("COM5", "19200")
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
            print("command no routine", cmdVal)

    def queParm(self, parmIndex, val):
        self.setParm(parmIndex, val)

    def sendMulti(self):
        pass

    def setParm(self, parmIndex, val):
        (name, varType, varName) = parmTable[parmIndex]
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
        (name, varType, varName) = parmTable[parmIndex]
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
                stdout.flush()
            raise CommTimeout()

        rspLen = int(rsp[1:3], 16)
        rsp += self.ser.read(rspLen).decode('utf8')
        self.commLock.release()
        if rspLen > 5:
            rspType = int(rsp[3:5], 16)
            if rspType != en.R_READ_ALL:
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
                if cmd == en.R_SET_ACCEL:
                    x0 = arg[0] >> 8
                    x1 = arg[0] & 0xff
                    data = "%10d %d %-10s %d %-14s" % \
                        (arg[1] ,x0, en.RiscvAccelTypeList[x0],
                         x1, en.RiscvSyncParmTypeList[x1])
            else:
                pass
        txt = "%-16s %-16s%s" % (en.riscvCmdList[cmd],
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

        if cmd != en.R_READ_ALL:
            trace(txt)
            print(txt)
            stdout.flush()

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
 
class RiscvLathe(Thread):
    def __init__(self, comm):
        Thread.__init__(self)
        print("PiLathe __init__")
        self.comm = comm
        # self.riscv = comm.riscv
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
        for (index, varType, name) in parmTable:
            # print("index %s name %s" % (index, name))
            setattr(self, name, None)
        self.parm = RemParm()

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
        self.comm.riscvCmd(en.R_MOVE_REL_Z, (dist, parm.zFlag))

    def cZJogMove(self):                # 2
        pass
        # parm = self.parm
        # self.zAxis.jogMove(parm.zJogDir)


    def cZJogSpeed(self):               # 3
        pass

    def cZStop(self):                   # 4
        self.comm.riscvCmd(en.R_STOP_Z)

    def cZHomeFwd(self):                # 6
        pass

    def cZHomeRev(self):                # 7
        pass

    def cXMoveAbs(self):                # 8
        pass

    def cXMoveRel(self):                # 9
        parm = self.parm
        dist = int(parm.xMoveDist * self.xAxis.stepsInch)
        self.comm.riscvCmd(en.R_MOVE_REL_X, (dist, parm.xFlag))

    def cXJogMove(self):                # 10
        pass
        # parm = self.parm
        # self.xAxis.jogMove(parm.xJogDir)

    def cXJogSpeed(self):               # 11
        pass

    def cXStop(self):                   # 12
        self.comm.riscvCmd(en.R_STOP_X)

    def cXHomeFwd(self):                # 14
        pass

    def cXHomeRev(self):                # 15
        pass

    def cSpindleStart(self):            # 16
        self.lastIdxClks = 0
        if self.parm.stepperDrive:
            pass
        else:
            if self.parm.cfgSwitch:
                pass

            if self.parm.cfgVarSpeed:
                pass

    def cSpindleStop(self):             # 17
        if self.parm.stepperDrive:
            pass
        else:
            if self.parm.cfgSwitch:
                pass

            if self.parm.cfgVarSpeed:
                pass

    def cSpindleUpdate(self):           # 18
        pass

    def cSpindleJog(self):              # 19
        pass

    def cSpindleJogSpeed(self):         # 20
        pass

    def cPauseCmd(self):                # 21
        # self.cmdPause = True
        # self.mvStatus |= ct.MV_PAUSE
        self.comm.riscvCmd(en.R_PAUSE, flush=True)

    def cResumeCmd(self):               # 22
        # self.cmdPause = False
        # if jogPause & DISABLE_JOG:
        #     jogPause &= ~(PAUSE_ENA_X_JOG | PAUSE_ENA_Z_JOG)
        # self.mvStatus &= ~(ct.MV_PAUSE | ct.MV_MEASURE | \
        #                    ct.MV_READ_X | ct.MV_READ_Z)
        self.comm.riscvCmd(en.R_RESUME, flush=True)

    def cStopCmd(self):                 # 23
        self.cSpindleStop()
        self.cZStop()
        self.cXStop()
        self.cmdPause = False
        self.mvStatus &= ~(ct.MV_PAUSE | ct.MV_ACTIVE | \
                           ct.MV_XHOME_ACTIVE | ct.MV_ZHOME_ACTIVE)
        self.comm.riscvCmd(en.R_STOP)

    def cDoneCmd(self):                 # 24
        self.mvStatus &= ~ct.MV_DONE

    def cMeasureCmd(self):              # 25
        pass

    def cClearCmd(self):                # 26
        pass

    def cSetup(self):                   # 27
        self.comm.riscvCmd(en.R_SETUP)

    def cSpindleSetup(self):            # 28
        pass

    def cSyncSetup(self):               # 29
        pass

    def cZSetup(self):                  # 30
        parm = self.parm

        stepsInch = intRound((parm.zMicro * parm.zMotor) /
                                        parm.zPitch)
        self.zAxis = zAxis = (
            Axis("z", Z_AXIS, stepsInch, parm.zAccel, parm))

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
        ac.init("slowJog", parm.zJogMin, parm.zJogMax)

    def cZSetLoc(self):                 # 32
        self.comm.riscvCmd(en.R_SET_LOC_Z, self.parm.zLoc)

    def cXSetup(self):                  # 33
        parm = self.parm

        stepsInch = (intRound((parm.xMicro * parm.xMotor) /
                              parm.xPitch))
        self.xAxis = xAxis = (
            Axis("x", X_AXIS, stepsInch, parm.xAccel, parm))

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
        ac.init("slowJog", parm.xJogMin, parm.xJogMax)

    def cXSetLoc(self):                 # 35
        self.comm.riscvCmd(en.R_SET_LOC_X, self.parm.xLoc)

    def cClearQue(self):                # 43
        pass

    def cReadAll(self):                 # 47
        pass

    def cReadDbg(self):                 # 48
        pass

    def cClearDbg(self):        	# 49
        pass

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

        print("RiscvLathe starting loop")
        while True:
            stdout.flush()
            sleep(0.1)
            if not self.threadRun:
                break
            self.procMove()
            self.update()
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
            self.comm.riscvCmd(en.R_READ_ALL)
            rsp = self.comm.riscvSend()
            if (self.postUpdate is not None) and len(rsp) >= 5:
                parm = int(rsp[3:5], 16)
                if parm == en.R_READ_ALL:
                    splitRsp = rsp[5:-1].split(' ')
                    (z, x, rpm, curPass, droZ, droX, mvStatus, \
                     queCount, dbgCount) = splitRsp[1:10]
                    z        = c_int32(int(z, 16)).value
                    x        = c_int32(int(x, 16)).value
                    rpm      = int(rpm, 16)
                    curPass  = int(curPass, 16)
                    droZ     = c_int32(int(droZ, 16)).value
                    droX     = c_int32(int(droX, 16)).value
                    mvStatus = int(mvStatus, 16)
                    self.queCount = int(queCount, 16)
                    self.dbgCount = int(dbgCount, 16)
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
            try:
                print("que size %d" % (self.moveQue.qsize()))
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
            except IndexError:
                pass
            except Empty:
                return

            if self.mvState != en.M_IDLE or self.cmdPause:
                break

    # move queue routines

    def qMoveZ(self, val):       	# 0
        dest = val + self.zAxis.HomeOffset
        # self.dbgMsg(en.D_ZMOV, val)
        print("moveZ dest %d val %d zStepsInch %d zHomeOffset %d" % \
              (dest, val, self.zAxis.stepsInch, self.zAxis.HomeOffset))

        # self.mvState = en.M_WAIT_Z
        # self.zAxis.move(dest, self.cmdFlag)

        # self.zAxis.riscvSetup(self.cmdFlag)
        self.comm.riscvCmd(en.R_MOVE_Z, (self.cmdFlag, dest))
        # self.comm.riscvCmd(en.R_WAIT_Z, flush=True)

    def qMoveX(self, val):              # 1
        dest = val + self.xAxis.HomeOffset
        # self.dbgMsg(en.D_XMOV, val)
        print("moveX dest %d val %d xStepsInch %d xHomeOffset %d" % \
              (dest, val, self.xAxis.stepsInch, self.xAxis.HomeOffset))
        # self.dbgMsg(en.D_XMOV, dest)

        # self.mvState = en.M_WAIT_X
        # self.xAxis.move(dest, self.cmdFlag)

        # self.zAxis.riscvSetup(self.cmdFlag)
        self.comm.riscvCmd(en.R_MOVE_X, (self.cmdFlag, dest))
        # self.comm.riscvCmd(en.R_WAIT_X, flush=True)

    def qSaveZ(self, val):              # 2
        print("save z %7.4f" % (val))
        self.zAxis.savedLoc = (intRound(val * self.zAxis.stepsInch) + \
                               self.zAxis.HomeOffset)

    def qSaveX(self, val):              # 3
        print("save x %7.4f" % (val))
        self.xAxis.savedLoc = (intRound(val * self.xAxis.stepsInch) + \
                            self.xAxis.HomeOffset)

    def qSaveZOffset(self, val):        # 4
        print("save z offset %7.4f" % (float(val) / self.zAxis.stepsInch))
        self.zAxis.HomeOffset = val

    def qSaveXOffset(self, val):        # 5
        print("save x offset %7.4f" % (float(val) / self.xAxis.stepsInch))
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
        self.taperSetup(self.zAxis, self.xAxis, val)
        # self.comm.riscvCmd(en.R_WAIT_Z)
        # self.mvState = en.M_WAIT_Z

    def qTaperXZ(self, val):            # 10
        print("taper xz %7.4f" % (val))
        self.taperSetup(self.xAxis, self.zAxis, val)
        # self.comm.riscvCmd(en.R_WAIT_X)
        # self.mvState = en.M_WAIT_X

    def taperSetup(self, mvAxis, tpAxis, val):
        print("taperSetup")
        tpAxis.taper = taper = self.taper
        loc = intRound(val * mvAxis.stepsInch) + mvAxis.homeOffset
        dist = tpAxis.savedLoc - tpAxis.loc
        print("tpAxis.savedLoc %d tpAxis.loc %d dist %d" %
              (tpAxis.savedLoc, tpAxis.loc, dist))
        tpAxis.axisCtl = (bt.ctlSlave | \
                          (DIR_POS if dist > 0 else 0))
        mvDist = abs(float(dist) / mvAxis.stepsInch)
        tpAxis.taperDist = intRound(mvDist * taper * tpAxis.stepsInch)
        print("mvDist %7.4f taper %0.6f tpAxis.taperDist %d" % \
              (mvDist, taper, tpAxis.taperDist))
        taperCalc(mvAxis.turnAccel, tpAxis.taperAccel, taper)
        mvAxis.move(loc, ct.CMD_SYN | ct.SYN_START | ct.SYN_TAPER)

    # noinspection PyUnusedLocal
    def qStartSpindle(self, val):       # 11
        print("startSpindle")
        # self.mvSpindleCmd = self.cmd
        # self.spindleStart()
        # self.mvState = en.M_WAIT_SPINDLE
        self.comm.riscvCmd(en.R_START_SPIN)

    # noinspection PyUnusedLocal
    def qStopSpindle(self, val):        # 12
        print("stopSpindle")
        # self.mvSpindleCmd = self.cmd
        # self.spindleStop()
        # self.mvState = en.M_WAIT_SPINDLE
        self.comm.riscvCmd(en.R_STOP_SPIN)

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

        if self.parm.turnSync == en.SEL_TU_ENC:
            self.zAxis.encParm = True
            syncAccelCalc(self.zAxis.turnAccel,
                          self.feedType, val)
            riscvAccelData(self.zAxis.turnAccel, en.RP_Z_TURN)
        elif self.parm.turnSync == en.SEL_TU_SYN:
            self.zAxis.encParm = False
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

        if self.parm.turnSync == en.SEL_TU_ENC:
            self.xAxis.encParm = True
            syncAccelCalc(self.xAxis.turnAccel,
                          self.feedType, val)
            riscvAccelData(self.xAxis.turnAccel, en.RP_Z_TURN)
        else:
            self.xAxis.encParm = False
            self.mvState = en.M_START_SYNC

    # noinspection PyMethodMayBeStatic,PyUnusedLocal
    def qSendSyncParms(self, val):      # 15
        print("sendSyncParms")

    # noinspection PyMethodMayBeStatic,PyUnusedLocal
    def qSyncCommand(self, val):        # 16
        print("syncCommand")

    def qPassNum(self, val):            # 17
        print("passNum")
        # self.passVal = val
        # if (val & 0xff00) == 0:
        #     self.currentPass = val & 0xff
        # else:
        #     self.springInfo = val
        # self.dbgMsg(en.D_PASS, val)
        self.comm.riscvCmd(en.R_PASS, val)

    # noinspection PyUnusedLocal
    def qQuePause(self, val):           # 18
        print("quePause")
        # self.cmdPause = True
        # self.mvStatus |= ct.MV_PAUSE
        self.comm.riscvCmd(en.R_PAUSE)

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
            self.comm.riscvCmd(en.R_OP_START)

            riscvAccelData(self.zMoveAccel,    en.RP_Z_MOVE)
            riscvAccelData(self.zJogAccel,     en.RP_Z_JOG)
            riscvAccelData(self.zJogSlowAccel, en.RP_Z_SLOW)

            riscvAccelData(self.xMoveAccel,    en.RP_X_MOVE)
            riscvAccelData(self.xJogAccel,     en.RP_X_JOG)
            riscvAccelData(self.xJogSlowAccel, en.RP_X_SLOW)

        elif val == ct.PARM_DONE:
            # self.mvStatus &= ~ct.MV_ACTIVE
            # self.mvStatus |= ct.MV_DONE
            self.comm.riscvCmd(en.R_OP_DONE)

    # move states

    def mvWaitZ(self):                  # 1
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
            
