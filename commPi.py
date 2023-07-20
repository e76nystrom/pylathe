from threading import Thread
from queue import Empty, Queue
from sys import stdout
from time import sleep, time
from platform import system
from math import floor, log
import os
import re
import pickle

from remParmDef import parmTable
from remCmdDef import cmdTable
import enumDef as en
import lRegDef as rg
import fpgaLathe as bt
import ctlBitDef as ct
from remParm import RemParm

zClkStr = ("zClkNone", "zClkZFreq", "zClkCh", "zClkIntClk", \
           "zClkFreq", "zClkXCh", "zClkSpindle", "zClkDbgFreq")

xClkStr = ("xClkNone", "xClkXFreq", "xClkCh", "xClkIntClk", \
           "xClkZFreq", "xClkZCh",  "xClkSpindle", "xClkDbgFreq")

moveCmds = ("CMD_NONE", "CMD_MOV", "CMD_JOG", "CMD_SYN",
            "CMD_MAX", "CMD_SPEED", "JOG_SLOW")

UDP = True
import socket
UDP_IP = "192.168.42.7"
SND_IP = "192.168.42.65"
UDP_PORT = 5555
sock = None

def prtAxisCtl(base, axisCtl, prefix=""):
    s = prefix
    s += "***** "
    s += "Z " if base == rg.F_ZAxis_Base else "X "
    s += "Axis "
    if (axisCtl & bt.ctlInit) != 0:
        s += "ctlInit "
    if (axisCtl & bt.ctlStart) != 0:
        s += "cltStart "
        s += "P" if (axisCtl & bt.ctlDirPos) != 0 else "N"
        s += " "
    if (axisCtl & bt.ctlBacklash) != 0:
        s += "backlash "
    if (axisCtl & bt.ctlWaitSync) != 0:
        s += "waitSync "
    if (axisCtl & bt.ctlSetLoc) != 0:
        s += "setLoc "
    if (axisCtl & bt.ctlChDirect) != 0:
        s += "chDirect "
    if (axisCtl & bt.ctlSlave) != 0:
        s += "save "
    if (axisCtl & bt.ctlDroEnd) != 0:
        s += "droEnd "
    if (axisCtl & bt.ctlJogCmd) != 0:
        s += "jogCmd "
    if (axisCtl & bt.ctlJogMpg) != 0:
        s += "jogMpg "
    if (axisCtl & bt.ctlHome) != 0:
        s += "home "
    if (axisCtl & bt.ctlIgnoreLim) != 0:
        s += "ignoreLim "
    print("axisCtl %02x %04x %s" % (base, axisCtl, s))

def prtStatus(status):
    sString = ""
    if (status & bt.zAxisEna) != 0:
        sString += "z Ena "
        sString += 'P' if (status & bt.zAxisCurDir) != 0 else 'N'
        sString += " "
    if (status & bt.zAxisDone) != 0:
        sString += "z Done "
    if (status & bt.xAxisEna) != 0:
        sString += "x Ena "
        sString += 'P' if (status & bt.xAxisCurDir) != 0 else 'N'
        sString += " "
    if (status & bt.xAxisDone) != 0:
        sString += "x Done "
    if len(sString) != 0:
        print(sString)

def prtCmdStr(cmd):
    cmdStr = moveCmds[cmd & ct.CMD_MSK]
    cmdStr += "SYN_START " if ((cmd & ct.SYN_START) != 0) else ""
    cmdStr += "SYN_LEFT " if ((cmd & ct.SYN_LEFT) != 0) else ""
    cmdStr += "FIND_HOME " if ((cmd & ct.FIND_HOME) != 0) else ""
    cmdStr += "CLEAR_HOME " if ((cmd & ct.CLEAR_HOME) != 0) else ""
    cmdStr += "FIND_PROBE " if ((cmd & ct.FIND_PROBE) != 0) else ""
    cmdStr += "CLEAR_PROBE " if ((cmd & ct.CLEAR_PROBE) != 0) else ""
    cmdStr += "DRO_POS " if ((cmd & ct.DRO_POS) != 0) else ""
    cmdStr += "DRO_UPD " if ((cmd & ct.DRO_UPD) != 0) else ""
    print(cmdStr)

class Serial:
    def __init__(self):
        pass

    def close(self):
        pass

Z_AXIS = 0
X_AXIS = 1

DBG_SETUP = True
DBG_DETAIL = False

def intRound(val):
    return(int(round(val)))

class CommTimeout(Exception):
    pass

class Comm():
    def __init__(self):
        print("CommPi __init__")
        self.ser = Serial()
        self.rpi = PiLathe(self)
        self.spi = None
        self.lastRdCmd = -1
        self.lastResult = 0

        if UDP:
            global sock
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.sock.settimeout(3)
            self.sock.bind((UDP_IP, UDP_PORT))
        else:
            if system() == 'Linux':
                if os.uname().machine.startswith('arm'):
                    # noinspection PyUnresolvedReferences
                    import spidev
                    bus = 0
                    device = 0
                    self.spi = spidev.SpiDev()
                    self.spi.open(bus, device)
                    self.spi.max_speed_hz = 500000
                    self.spi.mode = 0
            print(self.rpi.parm.spSteps)

    def ld(self, cmd, data, dbg=True):
        s0 = rg.fpgaSizeTable[cmd]
        val = list(int(data).to_bytes(s0, byteorder='big', signed=True))
        if dbg:
            d = ""
            for i in val:
                d += "%02x" % i
            print("ld %d %2d 0x%02x %10d %s %s" % \
                  (s0, cmd, cmd, data, d, rg.xRegTable[cmd]))
        msg = [cmd] + val

        if UDP:
            outMsg = pickle.dumps(msg)
            self.sock.sendto(outMsg, (SND_IP, UDP_PORT))
        else:
            if self.spi is None:
                return
            self.spi.xfer2(msg)

    def rd(self, cmd, dbg=False, ext=0x80000000, mask=0xffffffff):
        if dbg:
            if cmd != self.lastRdCmd:
                print("rd %2d %s" % (cmd, rg.xRegTable[cmd]))
                self.lastRdCmd = cmd

        if UDP:
            outMsg = pickle.dumps([cmd | 0x100])
            self.sock.sendto(outMsg, (SND_IP, UDP_PORT))
            val, addr = self.sock.recvfrom(64)
            val = pickle.loads(val)
        else:
            if self.spi is None:
                return(0)
            msg = [cmd]
            self.spi.xfer2(msg)
            val = self.spi.readbytes(4)
            val = pickle.loads(val)

        result = int.from_bytes(val, byteorder='big', signed=True)
        if result & ext:
            result |= -1 & ~mask
        if dbg:
            if (cmd == rg.F_Rd_Status) and (result != self.lastResult):
                self.lastResult = result
                print("rd status %08x" % result)
        return(result)

    def ldAxisCtl(self, base, axisCtl, ident=None):
        if ident is not None:
            print("ldAxisCtl", ident)
        prtAxisCtl(base, axisCtl, "ld ")
        self.ld(base + rg.F_Ld_Axis_Ctl, axisCtl)
        value = self.rd(base + rg.F_Rd_Axis_Ctl)
        prtAxisCtl(base, value, "rd ")

    def setupCmds(self, loadMulti, loadVal, readVal):
        pass

    def setupTables(self, cmdTbl, parmTbl):
        self.cmdTable = cmdTbl
        self.parmTable = parmTbl

    def enableXilinx(self):
        pass

    def openSerial(self, port, rate):
        pass

    def closeSerial(self):
        if self.spi is not None:
            print("close spi device")
            self.spi.close()

    def command(self, cmdVal):
        print("cmd %12s" % (cmdTable[cmdVal][0]))
        # noinspection PyCallingNonCallable
        self.rpi.cmdAction[cmdVal]()

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
        setattr(self.rpi.parm, varName, val)

    def getParm(self, parmIndex):
        (name, varType, varName) = parmTable[parmIndex]
        val = getattr(self.rpi.parm, varName)
        print("getParm var %s val %s" % (varName, str(val)))
        return val

    def getString(self, command, parm=None):
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
        self.rpi.moveQue.put((opString, op, val))
        pass

    # noinspection PyMethodMayBeStatic
    def getQueueStatus(self):
        return(64)

def renameVar(name):
    tmp = name.split("_")
    varName = ""
    first = True
    for s in tmp:
        if first:
            varName = s.lower()
            first = False
        else:
            varName = varName + s.capitalize()
    return varName


class PiLathe(Thread):
    def __init__(self, comm):
        Thread.__init__(self)
        print("PiLathe __init__")
        self.comm = comm
        self.ld = comm.ld
        self.rd = comm.rd
        self.ldAxisCtl = comm.ldAxisCtl
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

        self.zAxis = Axis(self, Z_AXIS)
        self.xAxis = Axis(self, X_AXIS)

        self.zAxis.slvAxis = self.xAxis
        self.xAxis.slvAxis = self.zAxis

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

        self.start()

    def setZLoc(self, loc):
        self.parm.zLoc = loc

    def getZLoc(self):
        return self.parm.zLoc

    def setXLoc(self, loc):
        self.parm.xLoc = loc

    def getXLoc(self):
        return self.parm.xLoc

    def setPostUpdate(self, postUpdate):
        self.postUpdate = postUpdate

    def setDbgDispatch(self, dbgDispatch):
        self.dbgDispatch = dbgDispatch

    def clearQue(self):
        pass

    def clearDbg(self):
        pass

    def clearCmd(self):
        pass

    def measureCmd(self):
        pass

    def pauseCmd(self):
        self.cmdPause = True
        self.mvStatus |= ct.MV_PAUSE

    def resumeCmd(self):
        self.cmdPause = False
        # if jogPause & DISABLE_JOG:
        #     jogPause &= ~(PAUSE_ENA_X_JOG | PAUSE_ENA_Z_JOG)
        self.mvStatus &= ~(ct.MV_PAUSE | ct.MV_MEASURE | \
                           ct.MV_READ_X | ct.MV_READ_Z)

    def setup(self):
        pass

    def spSetup(self):
        pass

    def stopCmd(self):
        self.spindleStop()
        self.zStop()
        self.xStop()
        self.cmdPause = False
        self.mvStatus &= ~(ct.MV_PAUSE | ct.MV_ACTIVE | \
                           ct.MV_XHOME_ACTIVE | ct.MV_ZHOME_ACTIVE)

    def doneCmd(self):
        self.mvStatus &= ~ct.MV_DONE

    def syncSetup(self):
        pass

    def zSetup(self):
        print("\n>>>zSetup")
        self.zAxis.init()
        print("<<<\n")

    def zSetLoc(self):
        self.zAxis.initLoc()
        pass

    def xSetup(self):
        print("\n>>>xSetup")
        self.xAxis.init()
        print("<<<\n")

    def xSetLoc(self):
        self.xAxis.initLoc()
        pass

    def readAll(self):
        pass

    def readDbg(self):
        pass

    def spindleSetup(self):
        pass

    def spindleJog(self):
        pass

    def spindleJogSpeed(self):
        pass

    def spindleStart(self):
        self.lastIdxClks = 0
        if self.parm.stepperDrive:
            pass
        else:
            if self.parm.cfgSwitch:
                pass

            if self.parm.cfgVarSpeed:
                pass

    def spindleStop(self):
        if self.parm.stepperDrive:
            pass
        else:
            if self.parm.cfgSwitch:
                pass

            if self.parm.cfgVarSpeed:
                pass
        pass

    def spindleUpdate(self):
        pass

    def xHomeAxis(self):
        pass

    def xJogMove(self):
        parm = self.parm
        self.xAxis.jogMove(parm.xJogDir)

    def xJogSpeed(self):
        pass

    def xMoveAbs(self):
        pass

    def xMoveRel(self):
        parm = self.parm
        axis = self.xAxis
        dist = int(parm.xMoveDist * axis.stepsInch)
        axis.moveRel(dist, parm.xFlag)

    def xStop(self):
        self.xAxis.stop()

    def xHomeFwd(self):
        pass

    def xHomeRev(self):
        pass

    def zJogMove(self):
        parm = self.parm
        self.zAxis.jogMove(parm.zJogDir)

    def zJogSpeed(self):
        pass

    def zMoveAbs(self):
        pass

    def zMoveRel(self):
        parm = self.parm
        axis = self.zAxis
        dist = int(parm.zMoveDist * axis.stepsInch)
        axis.moveRel(dist, parm.zFlag)

    def zStop(self):
        self.zAxis.stop()

    def zHomeFwd(self):
        pass

    def zHomeRev(self):
        pass

    def dbgMsg(self, cmd, val):
        # self.dbgQue.put((time(), cmd, val))
        self.dbgDispatch(time(), cmd, val)

    # move queue

    def run(self):
        self.cmdPause = False
        self.mvState = en.M_IDLE
        self.mvLastState = en.M_IDLE
        axisDbg = False

        while self.parm.fpgaFrequency is None:
            if not self.threadRun:
                break
            sleep(0.1)

        print("PiLathe starting loop")
        while True:
            stdout.flush()
            sleep(0.1)
            if not self.threadRun:
                break
            self.axisCtl(axisDbg)
            self.procMove()
            self.update()
        print("piLathe done")
        stdout.flush()
        self.threadDone = True

    def close(self):
        self.threadRun = False
        print("PiLathe threadRun %s" % (self.threadRun, ))
        return

    def update(self):
        if self.postUpdate is not None:
            result = (en.EV_READ_ALL, self.parm.zLoc, self.parm.xLoc, \
                      self.curRPM, self.passVal, self.droZ, self.droX, \
                      self.mvStatus)
            self.postUpdate(result)

    # def readData(self, base, prt=True):
    #     global xPos, yPos, zSum, zAclSum, aclCtr, curLoc, curDist
    #     bSyn = base + rg.F_Sync_Base
    #     xPos = self.rd(bSyn + rg.F_Rd_XPos)
    #     yPos = self.rd(bSyn + rg.F_Rd_YPos)
    #     zSum = self.rd(bSyn + rg.F_Rd_Sum)
    #     zAclSum = self.rd(bSyn + rg.F_Rd_Accel_Sum)
    #     aclCtr = self.rd(bSyn + rg.F_Rd_Accel_Ctr)
    #     if prt:
    #         print("xPos %7d yPos %6d zSum %12d" % (xPos, yPos, zSum), end=" ")
    #         print("aclSum %8d aclCtr %8d" % (zAclSum, aclCtr), end=" ")

    #     bDist = base + rg.F_Sync_Base
    #     curDist = self.rd(bDist + rg.F_Rd_A_Dist) # read z location
    #     curAcl = self.rd(bDist + rg.F_Rd_Acl_Steps) # read accel steps

    #     curLoc = self.rd(base + rg.F_Sync_Base + rg.F_Rd_X_Loc, \
    #                 False, 0x20000, 0x3ffff)

    #     if prt:
    #         print("dist %6d aclStp %6d loc %5d" % (curDist, curAcl, curLoc))

    def axisCtl(self, dbg=False):
        indexClks = self.rd(rg.F_Rd_Idx_Clks)
        if indexClks != 0:
            # rpm = (clocks * sec / clocks / rev) * sec / minute
            try:
                self.curRPM = intRound((float(self.parm.fpgaFrequency) / \
                                        (indexClks + 1)) * 60)
            except ZeroDivisionError:
                self.curRPM = 0
        else:
            self.curRPM = 0

        status = self.rd(rg.F_Rd_Status, True)

        if status != self.lastStatus:
            self.lastStatus = status
            prtStatus(status)

        axis = self.zAxis
        base = rg.F_ZAxis_Base
        self.zDro =  self.rd(base + rg.F_Sync_Base + rg.F_Rd_Dro, \
                        False, 0x20000, 0x3ffff)
        if axis.state != en.AXIS_IDLE:
            value = self.rd(base + rg.F_Rd_Axis_Ctl)
            if self.lastZAxisCtl != value:
                self.lastZAxisCtl = value
                prtAxisCtl(base, value)

            tmp = self.rd(base + rg.F_Sync_Base + rg.F_Rd_X_Loc, \
                          False, 0x20000, 0x3ffff)
            dist = self.rd(base + rg.F_Sync_Base + rg.F_Rd_A_Dist, \
                           False, 0x20000, 0x3ffff)
            self.parm.zLoc = self.zAxis.loc = tmp
            if axis.loc != tmp:
                print("zLoc", tmp, dist)
                self.parm.zLoc = axis.loc = tmp

            if (status & bt.zAxisDone) != 0 or dbg:
                axis.done = True
                axis.wait = False
                axisStatus = self.rd(base + rg.F_Rd_Axis_Status)
                print("z axis done status {0:04b}".format(axisStatus))
                self.ldAxisCtl(base, bt.ctlInit, "1")
                self.ldAxisCtl(base, 0, "1")

            if axis.wait:
                if (status & bt.zAxisEna) == 0:
                    # axis.wait = False
                    print("z waiting no enable")

            axis.control()

        axis = self.xAxis
        status = self.rd(rg.F_Rd_Status, False)
        if status != self.lastStatus:
            self.lastStatus = status
            prtStatus(status)

        base = rg.F_XAxis_Base
        self.xDro =  self.rd(base + rg.F_Sync_Base + rg.F_Rd_Dro, \
                        False, 0x20000, 0x3ffff)
        if axis.state != en.AXIS_IDLE:
            value = self.rd(base + rg.F_Rd_Axis_Ctl)
            if self.lastXAxisCtl != value:
                self.lastXAxisCtl = value
                prtAxisCtl(base, value)

            tmp = self.rd(base + rg.F_Sync_Base + rg.F_Rd_X_Loc, \
                          False, 0x20000, 0x3ffff)
            self.parm.xLoc = self.xAxis.loc = tmp
            if axis.loc != tmp:
                print("zLoc", tmp)

            if (status & bt.xAxisDone) != 0 or dbg:
                axis.done = True
                axis.wait = False
                axisStatus = self.rd(base + rg.F_Rd_Axis_Status)
                print("x axis done status {0:04b}".format(axisStatus))
                self.ldAxisCtl(base, 0, "2")

            if axis.wait:
                if (status & bt.xAxisEna) == 0:
                    # axis.wait = False
                    print("x waiting no enable")

            axis.control()

    # process move command

    def procMove(self):
        if self.cmdPause and self.mvState == en.M_IDLE:
            return
        # noinspection PyCallingNonCallable
        self.mvCtl[self.mvState]()
        if self.mvState != self.mvLastState:
            self.mvLastState = self.mvState
            self.dbgMsg(en.D_MSTA, self.mvState)

    # idle state

    def mvIdle(self):
        while True:
            try:
                (opString, op, val) = self.moveQue.get(False)
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
                    print("%16s %2d %2d %-7s" % \
                          (opString, op, self.cmdFlag, valString))
                    stdout.flush()
                self.dbgMsg(en.D_MCMD, (self.cmdFlag << 8) | op)
                print("\n>>>")
                # noinspection PyCallingNonCallable
                self.move[op](val)
                print("<<<\n")
            except IndexError:
                pass
            except Empty:
                return

            if self.mvState != en.M_IDLE or self.cmdPause:
                break

    # move functions

    def moveZ(self, val):
        dest = val + self.zAxis.homeOffset
        self.dbgMsg(en.D_ZMOV, val)
        print("moveZ dest %d val %d zStepsInch %d zHomeOffset %d" % \
              (dest, val, self.zAxis.stepsInch, self.zAxis.homeOffset))
        self.mvState = en.M_WAIT_Z
        self.zAxis.move(dest, self.cmdFlag)

    def moveX(self, val):
        dest = val + self.xAxis.homeOffset
        self.dbgMsg(en.D_XMOV, val)
        print("moveX dest %d val %d xStepsInch %d xHomeOffset %d" % \
              (dest, val, self.xAxis.stepsInch, self.xAxis.homeOffset))
        self.dbgMsg(en.D_XMOV, dest)

        self.mvState = en.M_WAIT_X
        self.xAxis.move(dest, self.cmdFlag)

    def saveZ(self, val):
        print("save z %7.4f" % (val))
        self.zAxis.savedLoc = (intRound(val * self.zAxis.stepsInch) + \
                               self.zAxis.homeOffset)

    def saveX(self, val):
        print("save x %7.4f" % (val))
        self.xAxis.savedLoc = (intRound(val * self.xAxis.stepsInch) + \
                               self.xAxis.homeOffset)

    def saveZOffset(self, val):
        print("save z offset %7.4f" % (float(val) / self.zAxis.stepsInch))
        self.zAxis.homeOffset = val

    def saveXOffset(self, val):
        print("save x offset %7.4f" % (float(val) / self.xAxis.stepsInch))
        self.xAxis.homeOffset = val

    def saveTaper(self, val):
        print("save taper %7.4f" % (val))
        self.taper = val

    # noinspection PyMethodMayBeStatic,PyUnusedLocal
    def moveZX(self, val):
        print("moveZX")

    # noinspection PyMethodMayBeStatic,PyUnusedLocal
    def moveXZ(self, val):
        print("moveXZ")

    def taperZX(self, val):
        print("taper zx %7.4f" % (val))
        self.taperSetup(self.zAxis, self.xAxis, val)
        self.mvState = en.M_WAIT_Z

    def taperXZ(self, val):
        print("taper xz %7.4f" % (val))
        self.taperSetup(self.xAxis, self.zAxis, val)
        self.mvState = en.M_WAIT_X

    def taperSetup(self, mvAxis, tpAxis, val):
        print("taperSetup")
        tpAxis.taper = taper = self.taper
        loc = intRound(val * mvAxis.stepsInch) + mvAxis.homeOffset
        dist = tpAxis.savedLoc - tpAxis.loc
        print("tpAxis.savedLoc %d tpAxis.loc %d dist %d" %
              (tpAxis.savedLoc, tpAxis.loc, dist))
        tpAxis.axisCtl = (bt.ctlSlave | \
                          (bt.ctlDirPos if dist > 0 else bt.ctlDirPos))
        mvDist = abs(float(dist) / mvAxis.stepsInch)
        tpAxis.taperDist = intRound(mvDist * taper * tpAxis.stepsInch)
        print("mvDist %7.4f taper %0.6f tpAxis.taperDist %d" % \
              (mvDist, taper, tpAxis.taperDist))
        taperCalc(mvAxis.turnAccel, tpAxis.taperAccel, taper)
        mvAxis.move(loc, ct.CMD_SYN | ct.SYN_START | ct.SYN_TAPER)

    # noinspection PyUnusedLocal
    def startSpindle(self, val):
        print("startSpindle")
        self.mvSpindleCmd = self.cmd
        self.spindleStart()
        self.mvState = en.M_WAIT_SPINDLE

    # noinspection PyUnusedLocal
    def stopSpindle(self, val):
        print("stopSpindle")
        self.mvSpindleCmd = self.cmd
        self.spindleStop()
        self.mvState = en.M_WAIT_SPINDLE

    def zSynSetup(self, val):
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
            syncAccelCalc(self.zAxis.turnAccel, self.feedType, val)
        elif self.parm.turnSync == en.SEL_TU_SYN:
            self.zAxis.encParm = False
            self.mvState = en.M_START_SYNC

    def xSynSetup(self, val):
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
            syncAccelCalc(self.xAxis.turnAccel, self.feedType, val)
        else:
            self.xAxis.encParm = False
            self.mvState = en.M_START_SYNC

    # noinspection PyMethodMayBeStatic,PyUnusedLocal
    def sendSyncParms(self, val):
        print("sendSyncParms")

    # noinspection PyMethodMayBeStatic,PyUnusedLocal
    def syncCommand(self, val):
        print("syncCommand")

    def passNum(self, val):
        print("passNum")
        self.passVal = val
        if (val & 0xff00) == 0:
            self.currentPass = val & 0xff
        else:
            self.springInfo = val
        self.dbgMsg(en.D_PASS, val)

    # noinspection PyUnusedLocal
    def quePause(self, val):
        print("quePause")
        self.cmdPause = True
        self.mvStatus |= ct.MV_PAUSE

    # noinspection PyMethodMayBeStatic,PyUnusedLocal
    def moveZOffset(self, val):
        print("moveZOffset")

    def saveFeedType(self, val):
        print("saveFeedType")
        self.feedType = val

    # noinspection PyMethodMayBeStatic,PyUnusedLocal
    def zFeedSetup(self, val):
        print("zFeedSetup")

    # noinspection PyMethodMayBeStatic,PyUnusedLocal
    def xFeedSetup(self, val):
        print("xFeedSetup")

    def saveFlags(self, val):
        print("saveFlags")
        self.threadFlag = val

    # noinspection PyMethodMayBeStatic,PyUnusedLocal
    def probeX(self, val):
        print("probeX")

    # noinspection PyMethodMayBeStatic,PyUnusedLocal
    def probeZ(self, val):
        print("probeZ")

    # noinspection PyMethodMayBeStatic,PyUnusedLocal
    def saveZDro(self, val):
        print("saveZDro")

    # noinspection PyMethodMayBeStatic,PyUnusedLocal
    def saveXDro(self, val):
        print("saveXDro")

    # noinspection PyMethodMayBeStatic,PyUnusedLocal
    def queParm(self, val):
        print("queParm")

    # noinspection PyMethodMayBeStatic,PyUnusedLocal
    def moveArc(self, val):
        print("moveArc")

    def opDone(self, val):
        print("opDone")
        self.dbgMsg(en.D_DONE, val)
        if val == ct.PARM_START:
            self.mvStatus &= ~ct.MV_DONE
            self.mvStatus |= ct.MV_ACTIVE
        elif val == ct.PARM_DONE:
            self.mvStatus &= ~ct.MV_ACTIVE
            self.mvStatus |= ct.MV_DONE

    # move states

    def mvWaitZ(self):          # 1
        if self.zAxis.state == en.AXIS_IDLE:
            self.mvState = en.M_IDLE

    def mvWaitX(self):          # 2
        if self.xAxis.state == en.AXIS_IDLE:
            self.mvState = en.M_IDLE

    def mvWaitSpindle(self):    # 3
        indexClks = self.rd(rg.F_Rd_Idx_Clks)
        if indexClks != self.lastIdxClks:
            print("indexClks %d" % (indexClks))
            self.lastIdxClks = indexClks
            if indexClks != 0:
                delta = abs(indexClks - self.lastIdxClks)
                percent = float(delta) * 100.0 / indexClks
                indexClks += 1
                rpm = intRound((float(self.parm.fpgaFrequency) /
                                indexClks) * 60)
                print("delta %d percent %7.2f rpm %d" % (delta, percent, rpm))
                if percent < 1.0:
                    if self.mvSpindleCmd == en.STOP_SPINDLE:
                        self.mvState = en.M_IDLE
                    elif self.mvSpindleCmd == en.START_SPINDLE:
                        self.mvState = en.M_IDLE

    def mvWaitSyncParms(self):  # 4
        pass

    def mvWaitSyncCmd(self):    # 5
        pass

    def mvStartSync(self):      # 6
        self.ld(rg.F_Enc_Base + rg.F_Ld_Enc_Cycle, self.parm.lSyncCycle)
        self.ld(rg.F_Enc_Base + rg.F_Ld_Int_Cycle, self.parm.lSyncOutput)
        self.ld(rg.F_Ld_Sync_Ctl, bt.synEncInit)
        self.ld(rg.F_Ld_Sync_Ctl, bt.synEncEna)
        self.mvState = en.M_WAIT_SYNC_READY

    def mvWaitSyncReady(self):  # 7
        status = self.rd(rg.F_Rd_Status)
        if (status & bt.syncActive) != 0:
            self.mvState = en.M_IDLE

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

MAX_SCALE = 12

class AccelData():
    def __init__(self, axis):
        self.axis = axis
        self.accelClocks = None
        self.accelSteps = None
        self.accelTime = None
        self.clockFreq = None
        self.clocksPerInch = None
        self.dxBase = None
        self.dyMaxBase = None
        self.dyMinBase = None
        self.freqDivider = None    # frequency divider
        self.incr1 = None
        self.incr2 = None
        self.initialSum = None
        self.intAccel = None
        self.pitch = None          # pitch for turning or threading
        self.scale = None
        self.stepsSecMax = None

    def init(self, accelType, minSpeed=0, maxSpeed=0):
        print("\n%s %s AccelData init" % (self.axis.name, accelType))
        self.accel = self.axis.accel # axis acceleration units/sec^2
        self.accelType = accelType # acceleration type string
        self.maxSpeed = maxSpeed # final speed
        self.minSpeed = minSpeed # starting speed
        self.stepsInch = self.axis.stepsInch # axis steps per inch

        accelCalc1(self)

def load(aData, dist, encParm=True):
    axis = aData.axis
    print("\n%s accel load" % (axis.name))
    axisCtl = axis.axisCtl
    base = axis.base
    ld = axis.ld
    if encParm:
        if aData.freqDivider != 0:
            ld(base + rg.F_Ld_Freq, aData.freqDivider)

        bSyn = base + rg.F_Sync_Base
        ld(bSyn + rg.F_Ld_D, aData.initialSum) # load initialSum (d)  value
        ld(bSyn + rg.F_Ld_Incr1, aData.incr1)  # load incr1 value
        ld(bSyn + rg.F_Ld_Incr2, aData.incr2)  # load incr2 value

        ld(bSyn + rg.F_Ld_Accel_Val, aData.intAccel)   # load accel
        ld(bSyn + rg.F_Ld_Accel_Count, aData.accelClocks) # load acl ctr

        ld(base + rg.F_Sync_Base + rg.F_Ld_A_Dist, dist)
        axis.rd(base + rg.F_Sync_Base + rg.F_Rd_A_Dist)

        axis.ldAxisCtl(base, bt.ctlInit, "3")
        axis.ldAxisCtl(base, 0, "3a")
    else:
        ld(base + rg.F_Sync_Base + rg.F_Ld_A_Dist, dist)
        axisCtl |=  bt.ctlChDirect

    axis.ldAxisCtl(base, bt.ctlStart | axisCtl, "4")

def start(aData, axisCtl=0):
    axis = aData.axis
    print("\n%s %s accelCalc" % (axis.name, aData.accelType))
    axisCtl |= axis.axisCtl | bt.ctlStart
    axis.ldAxisCtl(axis.base, axisCtl, "5")

def accelCalc(aData):
    print("\n%s %s accelCalc" % (aData.axis.name, aData.accelType))
    if aData.maxFeed == 0:
        return
    parm = aData.axis.parm
    stepsInch = aData.stepsInch
    stepsSecMax = intRound((aData.maxFeed / 60.0) * stepsInch)
    aData.clockFreq = stepsSecMax * parm.freqMult
    aData.clocksPerInch = stepsInch * parm.freqMult
    aData.freqDivider = int((parm.fpgaFrequency / aData.clockFreq) - 1)
    if DBG_SETUP:
        print("stepsInch %d freqMult %d fpgaFrequency %d" % \
              (stepsInch, parm.freqMult, parm.fpgaFrequency))
        print("freqGenMax %d freqDivider %d" % \
              (aData.clockFreq, aData.freqDivider))
    accelSetup(aData)

def syncAccelCalc(aData, feedType, feed):
    print("\n%s %s syndAccelCalc" % (aData.axis.name, aData.accelType))
    if feedType == ct.FEED_PITCH:
        aData.pitch = feed
    elif feedType == ct.FEED_TPI:
        aData.pitch = 1.0 / feed
    elif feedType == ct.FEED_METRIC:
        aData.pitch = feed / 25.4

    if DBG_SETUP:
        print("\nturnAccel %3.1f" % aData.accel)
    parm = aData.axis.parm
    aData.freqDivider = 0
    if aData.maxSpeed == 0:
        # (pulse / rev) / (in / rev) = pulse / in
        # (pulse / in) / (steps / in) = pulse / step
        encPerInch = intRound(parm.encPerRev / aData.pitch)
        aData.dx = encPerInch
        aData.dy = aData.stepsInch
        aData.incr1 = 2 * aData.dy
        aData.incr2 = aData.incr1 - 2 * aData.dx
        aData.initialSum = aData.incr1 - aData.dx
        aData.intAccel = 0
        aData.accelClocks = 0
        if DBG_SETUP:
            print("encPerInch dx %d stepsInch dy %d\n"\
                  "incr1 %d incr2 %d initialSum %d" % \
                  (aData.dx, aData.dy, aData.incr1, \
                   aData.incr2, aData.initialSum))
    else:
        aData.maxFeed = parm.rpm * aData.pitch
        aData.clocksPerInch = intRound(parm.encPerRev * aData.pitch)
        aData.clockFreq = intRound((parm.rpm * parm.encPerRev) / 60.0)
        accelSetup(aData)

def bitSize(val):
    bits = 0
    while bits < 32:
        if val == 0:
            break
        val >>= 1
        bits += 1
    return(bits)

def accelSetup(aData):
    print("\n%s %s accelSetup" % (aData.axis.name, aData.accelType))
    stepsInch = aData.axis.stepsInch
    scale = 0
    if DBG_SETUP:
        print("accel %0.2f minFeed %0.2f feedRate %0.2f ipm" % \
              (aData.axis.accel, aData.minFeed, aData.maxFeed))
        print("clocksPerInch %d clockFreq %d stepsInch %d" % \
              (aData.clocksPerInch, aData.clockFreq, stepsInch))

    stepsSecMax = intRound((aData.maxFeed * stepsInch) / 60.0)
    stepsSecMin = intRound((aData.minFeed * stepsInch) / 60.0)
    if DBG_SETUP:
        print("stepsSecMin %d stepsSecMax %d" % (stepsSecMin, stepsSecMax))

    stepsSec2 = float(aData.axis.accel) * stepsInch
    aData.accelTime = (stepsSecMax - stepsSecMin) / stepsSec2
    aData.accelClks = intRound(aData.clockFreq * aData.accelTime)
    if DBG_SETUP:
        print("stepsSec2 %0.0f accelTime %8.6f accelClks %d" % \
              (stepsSec2, aData.accelTime, aData.accelClks))

    accelMinStep = intRound(((stepsSecMin / stepsSec2) * \
                              stepsSecMin) / 2.0)
    accelMaxStep = intRound(((stepsSecMax / stepsSec2) * \
                              stepsSecMax) / 2.0)
    aData.accelSteps = accelMaxStep - accelMinStep
    if DBG_SETUP:
        print("accelSteps %d accelMinStep %d accelMaxStep %d" % \
              (aData.accelSteps, accelMinStep, accelMaxStep))

    dxBase = aData.clocksPerInch
    dyMaxBase = stepsInch
    dyMinBase = intRound((stepsInch * aData.minFeed) / aData.maxFeed)
    if DBG_SETUP:
        print("\ndxBase %d dyMaxBase %d dyMinBase %d" % \
              (dxBase, dyMaxBase, dyMinBase))

    accelClks = aData.accelClks
    intIncPerClock = 0
    for scale in range(MAX_SCALE):
        aData.dx = dxBase << scale
        aData.dyMax = dyMaxBase << scale
        dyMin = dyMinBase << scale
        dyDelta = aData.dyMax - dyMin
        if DBG_DETAIL:
            print("\nscale %d dx %d dyMin %d dyMax %d dyDelta %d" % \
                  (scale, aData.dx, dyMin, aData.dyMax, dyDelta), end=' ')
            print("%10.4f" % (float(aData.dx) / float(aData.dyMax)))

        incPerClock = float(dyDelta) / accelClks
        intIncPerClock = int(incPerClock)
        if intIncPerClock == 0:
            continue
        aData.intIncPerClock = intIncPerClock
        dyDeltaC = intIncPerClock * accelClks
        err = intRound(abs(dyDelta - dyDeltaC)) >> scale
        aData.dyIni = aData.dyMax - intIncPerClock * accelClks
        if DBG_DETAIL:
            print("dyIni %d dyMax %d intIncPerClock %d accelClks %d" %
                  (aData.dyIni, aData.dyMax, intIncPerClock, accelClks))

        bits = aData.bitSize(aData.dx) + 1
        if DBG_DETAIL:
            print("dyIni %d dyMax %d dyDelta %d incPerClock %6.2f " \
                  "err %d bits %d" %
                  (aData.dyIni, aData.dyMax, dyDelta, incPerClock, \
                   err, bits))

        if (bits >= 30) or (err == 0):
            if DBG_SETUP:
                print("\nscale %d dx %d dyMin %d dyMax %d dyDelta %d" %
                      (scale, aData.dx, dyMin, aData.dyMax, dyDelta))
                print("dyIni %d dyMax %d dyDelta %d incPerClock %6.2f " \
                      "err %d bits %d" %
                      (aData.dyIni, aData.dyMax, dyDelta, incPerClock, \
                       err, bits))
            break

    aData.scale = scale
    aData.incr1 = 2 * aData.dyIni
    aData.incr2 = aData.incr1 - 2 * aData.dx
    aData.initialSum = aData.incr1 - aData.dx
    aData.intAccel = 2 * intIncPerClock
    if DBG_SETUP:
        print("\nincr1 %d incr2 %d sum %d" %
              (aData.incr1, aData.incr2, aData.initlSum))

    if intIncPerClock != 0:
        totalSum = accelClks * aData.incr1 + aData.initlSum
        totalInc = (accelClks * (accelClks - 1) * aData.intAccel) / 2
        aData.accelSteps = intRound((totalSum + totalInc) / (2 * aData.dx))
        if DBG_SETUP:
            print("accelClks %d totalSum %d totalInc %d " \
                  "accelSteps %d" % \
                  (aData.accelClks, totalSum, totalInc, aData.accelSteps))
    else:
        aData.accelSteps = 0

def accelCalc1(aData):
    axis = aData.axis
    print("\n%s %s accelCalc1" % (axis.name, aData.accelType))
    if aData.maxSpeed == 0:
        return
    parm = axis.parm
    stepsInch = aData.stepsInch
    aData.stepsSecMax = \
        stepsSecMax = intRound((aData.maxSpeed * stepsInch) / 60)
    freqGenMax = stepsSecMax * parm.freqMult
    #clockFreq = stepsSecMax * parm.freqMult
    print("stepsSecMax %6.0f freqGenMax %7.0f" % (stepsSecMax, freqGenMax))

    stepsSecMin = intRound((aData.minSpeed * stepsInch) / 60)
    freqGenMin = stepsSecMin * parm.freqMult
    print("stepsSecMin %6.0f freqGenMin %7.0f" % (stepsSecMin, freqGenMin))

    aData.freqDivider = int(parm.fpgaFrequency / freqGenMax) - 1
    print("freqDivider %3.0f" % aData.freqDivider)

    accelTime = (aData.maxSpeed - aData.minSpeed) / (60.0 * axis.accel)
    aData.accelClocks = intRound(accelTime * freqGenMax)
    print("accelTime %8.6f clocks %d" % (accelTime, aData.accelClocks))

    aData.dxBase = int(freqGenMax)
    aData.dyMinBase = int(stepsSecMin)
    aData.dyMaxBase = int(stepsSecMax)

    accelSetup1(aData)

def accelSetup1(aData):
    print("\n%s %s accelSetup1" % (aData.axis.name, aData.accelType))
    accelClocks = aData.accelClocks
    dx = 0
    dyIni = 0
    scale = 0
    intIncPerClock = 0
    if accelClocks == 0:
        dyIni = aData.dyMinBase
        dx = aData.dxBase
        scale = 0
        incr1 = 2 * dyIni
        incr2 = incr1 - 2 * dx
        initialSum = incr1 - dx
        synAccel = 0
    else:
        scalePrt = False
        for scale in range(0, 10):
            dx =  aData.dxBase << scale
            dyMin =  aData.dyMinBase << scale
            dyMax =  aData.dyMaxBase << scale
            dyDelta = dyMax - dyMin
            if scalePrt:
                print("\ndx %d dyMin %d dyMax %d dyDelta %d" % \
                      (dx, dyMin, dyMax, dyDelta))

            incPerClock = dyDelta / float(accelClocks)
            intIncPerClock = int(incPerClock)
            dyDeltaC = intIncPerClock * accelClocks
            dyIni = dyMax - dyDeltaC
            err = int(dyDelta - dyDeltaC) >> scale
            bits = int(floor(log(2*dx, 2))) + 1
            if scalePrt:
                print(("dyIni %d dyMax %d dyDelta %d incPerClock %4.2f "\
                       "err %d bits %d" %
                       (dyIni, dyMax, dyDeltaC, incPerClock, err, bits)))
            if (err == 0):
                break

        incr1 = 2 * dyIni
        incr2 = incr1 - 2 * dx
        initialSum = incr1 - dx

        bits = int(floor(log(abs(incr2), 2))) + 1
        print(("dx %d dy %d incr1 %d incr2 %d initialSum %d bits %d scale %d" %
               (dx, dyIni, incr1, incr2, initialSum, bits, scale)))

        synAccel = 2 * intIncPerClock

        totalSum = (accelClocks * incr1) + initialSum
        totalInc = (accelClocks * (accelClocks - 1) * synAccel) / 2
        accelSteps = ((totalSum + totalInc) / (2 * dx))

        print(("accelClocks %d totalSum %d totalInc %d accelSteps %d" %
               (accelClocks, totalSum, totalInc, accelSteps)))

    aData.scale = scale
    aData.incr1 = incr1
    aData.incr2 = incr2
    aData.initialSum = initialSum
    aData.intAccel = synAccel
    # variables = [i for i in dir(aData) if not callable(i)]
    # for i in variables:
    #     if not i.startswith("_"):
    #         print(i)

def taperCalc(aData, turnAccel, taper):
    axis = aData.axis
    print("\n%s accel taperCalc" % (axis.name))
    print("taperCalc a0 %s a1 %s taper %8.6f" % \
          (turnAccel.axis.name, aData.axis.name, taper))
    parm = axis.parm
    stepsInch = aData.stepsInch
    axis.taperDist = 1
    axis.taperInch = taper

    turnCycleDist = parm.taperCycleDist
    taperCycleDist = taper * turnCycleDist

    print("turnCycleDist %6.4f taperCycleDist %6.4f" %
          (turnCycleDist, taperCycleDist))

    turnSync = parm.turnSync
    if turnSync == en.SEL_TU_STEP:
        # turnSteps = intRound(turnCycleDist * turnAccel.axis.stepsInch)
        # taperSteps = intRound(taperCycleDist * stepsInch)
        print("**not done")
    elif turnSync == en.SEL_TU_ENC:
        dx = intRound((parm.encPerRev * turnCycleDist) / turnAccel.pitch)
        dy = intRound(taperCycleDist * stepsInch)
        aData.incr1 = 2 * dy
        aData.incr2 = aData.incr1 - 2 * dx
        aData.initialSum = aData.incr1 - dx
        print("encPerCycle dx %d stepsCycle dy %d incr1 %d incr2 %d initialSum %d" %
               (dx, dy, aData.incr1, aData.incr2, aData.initialSUm))
    elif turnSync == en.SEL_TU_SYN:
        pass

D_MOV  = en.D_XMOV  - en.D_XMOV
D_LOC  = en.D_XLOC  - en.D_XMOV
D_DST  = en.D_XDST  - en.D_XMOV
D_STP  = en.D_XSTP  - en.D_XMOV
D_ST   = en.D_XST   - en.D_XMOV
D_BSTP = en.D_XBSTP - en.D_XMOV
D_DRO  = en.D_XDRO  - en.D_XMOV
D_PDRO = en.D_XPDRO - en.D_XMOV
D_EXP  = en.D_XEXP  - en.D_XMOV
D_WT   = en.D_XWT   - en.D_XMOV
D_DN   = en.D_XDN   - en.D_XMOV
D_EST  = en.D_XEST  - en.D_XMOV
D_EDN  = en.D_XEDN  - en.D_XMOV
D_X    = en.D_XX    - en.D_XMOV
D_Y    = en.D_XY    - en.D_XMOV

class Axis():
    def __init__(self, rpi, axis):
        self.rpi = rpi
        self.ld = rpi.comm.ld
        self.rd = rpi.comm.rd
        self.ldAxisCtl = rpi.comm.ldAxisCtl
        self.axis = axis
        self.parm = rpi.parm
        self.state = en.AXIS_IDLE
        self.lastState = self.state

        self.stateDisp = [None] * en.AXIS_STATES
        for i, name in enumerate(en.axisStatesList[:-1]):
            stateName = renameVar(name.replace("AXIS_", ""))
            if hasattr(self, stateName):
                x = getattr(self, stateName)
                self.stateDisp[i] = x
            else:
                print("routine %s missing" % (stateName))

        self.turnAccel = AccelData(self)
        self.taperAccel = AccelData(self)
        self.moveAccel = AccelData(self)
        self.jogAccel = AccelData(self)
        self.jogSlowAccel = AccelData(self)

        self.dir = ct.DIR_POS
        self.dist = 0
        self.cmd = 0
        self.axisCtl = 0
        self.wait = False
        self.done = False
        self.loc = 0
        self.slvAxis = None
        self.encParm = None
        self.homeOffset = None
        self.savedLoc = None

        self.taper = None
        self.taperDist = None
        self.taperInch = None

    def init(self):
        parm = self.parm
        if self.axis == Z_AXIS:
            self.name = 'z'
            self.base = rg.F_ZAxis_Base
            stepsInch = intRound((parm.zMicro * parm.zMotor) / parm.zPitch)
            self.stepsInch = stepsInch
            self.accel = parm.zAccel

            self.turnAccel.init("turn")
            self.taperAccel.init("taper")
            self.moveAccel.init("move", parm.zMoveMin, parm.zMoveMax)
            self.jogAccel.init("jog", parm.zJogMin, parm.zJogMax)
            self.jogSlowAccel.init("jogSlow", parm.zJogMin, parm.zJogMax)

            self.backlashSteps = intRound(parm.zBacklash * stepsInch)
            if parm.zDirFlag:
               self.rpi.cfgCtl |= bt.cfgZDirInv
            else:
                self.rpi.cfgCtl &= ~bt.cfgZDirInv

            self.clkSel = \
                (bt.zClkNone, bt.zClkZFreq, bt.zClkCh, bt.zClkIntClk, \
                 bt.zClkXFreq, bt.zClkXCh, bt.zClkSpindle, bt.zClkDbgFreq)

            self.dbgBase = en.D_ZMOV
            self.getLoc = self.rpi.getZLoc
            self.setLoc = self.rpi.setZLoc
        else:
            self.name = 'x'
            self.base = rg.F_XAxis_Base
            stepsInch = intRound((parm.xMicro * parm.xMotor) / parm.xPitch)
            self.stepsInch = stepsInch
            self.backlashSteps = intRound(parm.xBacklash * stepsInch)
            self.accel = parm.xAccel

            self.turnAccel.init("turn")
            self.taperAccel.init("taper")
            self.moveAccel.init("move", parm.xMoveMin, parm.xMoveMax)
            self.jogAccel.init("jog", parm.xJogMin, parm.xJogMax)
            self.jogSlowAccel.init("jogSlow", parm.xJogMin, parm.xJogMax)

            if parm.xDirFlag:
                self.rpi.cfgCtl |= bt.cfgXDirInv
            else:
                self.rpi.cfgCtl &= ~bt.cfgXDirInv

            self.clkSel = \
                (bt.xClkNone, bt.xClkXFreq, bt.xClkCh, bt.xClkIntClk, \
                 bt.xClkZFreq, bt.xClkZCh, bt.xClkSpindle, bt.xClkDbgFreq)

            self.dbgBase = en.D_XMOV
            self.getLoc = self.rpi.getXLoc
            self.setLoc = self.rpi.setXLoc

        self.ld(self.base + rg.F_Sync_Base + rg.F_Ld_A_Dist, 0)

    def initLoc(self):
        print("%sSetLoc" % (self.name))
        base = self.base
        self.ld(base + rg.F_Sync_Base + rg.F_Ld_X_Loc, self.getLoc())
        loc = self.rd(base + rg.F_Sync_Base + rg.F_Rd_X_Loc)
        # self.ldAxisCtl(base, bt.ctlInit | bt.ctlSetLoc, "6")
        self.ldAxisCtl(base, bt.ctlInit, "6")
        # self.ldAxisCtl(base, 0, "7")

    def loadClock(self, clkCtl):
        print("clkCtl %s %s %s" % \
              (zClkStr[clkCtl & 7], xClkStr[(clkCtl >> 3) & 7],
               "dbgFreqEna" if (clkCtl & bt.clkDbgFreqEna) != 0 \
               else ""))
        self.ld(rg.F_Ld_Clk_Ctl, clkCtl)

    def move(self, pos, cmd):
        if self.state != en.AXIS_IDLE:
            return

        self.loc = self.rd(self.base + rg.F_Sync_Base + rg.F_Rd_X_Loc, \
                           True, 0x20000, 0x3ffff)
        self.expLoc = pos
        print("%sAxis move loc %d pos %d" % (self.name, self.loc, pos))
        self.rpi.dbgMsg(self.dbgBase + D_MOV, pos)
        self.moveRel(pos - self.loc, cmd)

    def moveRel(self, dist, cmd):
        print("%sAxis moveRel dist %d cmd %02x" % (self.name, dist, cmd))
        if self.state != en.AXIS_IDLE:
            return

        prtCmdStr(cmd)

        self.rpi.dbgMsg(self.dbgBase + D_DST, dist)
        self.cmd = cmd
        if dist != 0:
            self.expLoc = self.loc + dist
            if dist > 0:
                self.dist = dist
                dirChange = self.dir != ct.DIR_POS
                self.dir = ct.DIR_POS
            else:
                self.dist = -dist
                dirChange = self.dir != ct.DIR_NEG
                self.dir = ct.DIR_NEG

            self.axisCtl = 0
            if self.dir == ct.DIR_POS:
                self.axisCtl = bt.ctlDirPos

            if dirChange and self.backlashSteps != 0:
                self.wait = True
                self.axisCtl |= bt.ctlBacklash
                load(self.moveAccel, self.backlashSteps)
                self.state = en.AXIS_WAIT_BACKLASH
            else:
                self.state = en.AXIS_START_MOVE
                self.control()

    def jogMove(self, direction):
        aData = self.jogAccel
        if self.state == en.AXIS_IDLE:
            parm = self.parm
            stepsSec = aData.stepsSecMax
            self.jogInitialDist = dist = int(parm.jogTimeInitial * stepsSec)
            if direction < 0:
                dist = -dist
            self.jogIncDist = int(parm.jogTimeInc * stepsSec)
            self.jogMaxDist = int(parm.jogTimeMax * stepsSec)
            self.axisCtl = bt.ctlJogCmd
            self.moveRel(dist, ct.CMD_JOG)
        else:
            self.ld(self.base + rg.F_Sync_Base + rg.F_Ld_A_Dist, self.jogIncDist)

    def stop(self):
        self.done = False
        self.cmd = 0
        self.axisCtl = 0
        self.ldAxisCtl(self.base, 0, "S")
        self.ld(self.base + rg.F_Sync_Base + rg.F_Ld_A_Dist, 0)
        self.state = en.AXIS_IDLE


    def control(self):
        if self.state != self.lastState:
            self.lastState = self.state
            self.rpi.dbgMsg(self.dbgBase + D_ST, self.state)
            print("%s axis control %s" % (self.name, en.axisStatesList[self.state]))
        if self.state != en.AXIS_IDLE:
            # noinspection PyCallingNonCallable
            self.stateDisp[self.state]()

    def idle(self):
        pass

    def waitBacklash(self):
        if self.done:
            self.done = False
            self.wait = False
            self.loadClock(0)
            self.state = en.AXIS_START_MOVE

    def startMove(self):
        accel = None
        cmd = self.cmd & ct.CMD_MSK

        loc = self.rd(self.base + rg.F_Sync_Base + rg.F_Rd_X_Loc)
        print("+++loc %d" % (loc))

        if cmd == ct.CMD_SYN:
            if (self.cmd & ct.SYN_START) != 0:
                self.axisCtl |= bt.ctlWaitSync
            clkCtl = self.clkSel[bt.clkCh if self.encParm else bt.clkIntClk]
            if self.cmd & ct.SYN_TAPER:
                slvAxis = self.slvAxis
                load(slvAxis.taperAccel, slvAxis.taperDist, slvAxis.encParm)
                clkCtl |= slvAxis.clkSel[bt.clkSlvCh]
                self.ldAxisCtl(slvAxis.base, slvAxis.axisCtl | bt.ctlSlave, "10")
            self.loadClock(clkCtl)

            load(self.turnAccel, self.dist, self.encParm)

        elif cmd == ct.CMD_JOG:
            accel = self.jogAccel
            load(accel, self.dist)
            self.loadClock(self.clkSel[bt.clkFreq])

        elif cmd == ct.CMD_MAX or cmd == ct.CMD_MOV:
            accel = self.moveAccel
            load(accel, self.dist)
            self.loadClock(self.clkSel[bt.clkFreq])

        elif cmd == ct.CMD_SPEED:
            pass

        elif cmd == ct.JOGSLOW:
            pass

        else:
            pass

        self.wait = True
        if accel is not None:
            start(accel)
        self.state = en.AXIS_WAIT_MOVE

    def waitMove(self):
        if self.done:
            self.done = False
            self.wait = False
            self.loadClock(0)
            dist = self.rd(self.base + rg.F_Sync_Base + rg.F_Rd_A_Dist)
            loc = self.rd(self.base + rg.F_Sync_Base + rg.F_Rd_X_Loc)
            accelCtr = self.rd(self.base + rg.F_Sync_Base + rg.F_Rd_Accel_Ctr)
            aclSteps = self.rd(self.base + rg.F_Sync_Base + rg.F_Rd_A_Acl_Steps)
            print("dist %d loc %d accelCtr %d aclSteps %d" % \
                  (dist, loc, accelCtr, aclSteps))

            self.state = en.AXIS_DONE

    def delay(self):
        pass

    def done(self):
        rpi = self.rpi
        self.done = False
        self.cmd = 0

        self.loc = self.rd(self.base + rg.F_Sync_Base + rg.F_Rd_X_Loc, \
                           True, 0x20000, 0x3ffff)
        rpi.dbgMsg(self.dbgBase + D_LOC, self.loc)

        if (self.axisCtl & bt.ctlJogCmd) == 0:
            if self.loc != self.expLoc:
                rpi.dbgMsg(D_EXP, self.expLoc)

        self.axisCtl = 0
        self.state = en.AXIS_IDLE
        rpi.dbgMsg(self.dbgBase + D_ST, self.state)

        # rpi.pauseCmd()
        # print("pause")

        # variables = [i for i in dir(self) if not callable(i)]
        # for i in variables:
        #     if not i.startswith("_"):
        #         print(i)
        # stdout.flush()
