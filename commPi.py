from threading import Event, Lock, Thread
from queue import Empty, Queue
from sys import stderr, stdout
from time import sleep, time
from platform import system
from math import floor, log
import os
import re

from parmDef import parmTable
from cmdDef import cmdTable
import enumDef as en
import lRegDef as rg
import fpgaLathe as bt
import ctlBitDef as ct

WINDOWS = system() == 'Windows'

spi = None

def ld(cmd, data, size, dbg=True):
    if dbg:
        print("ld 0x%02x %10d %08x %s" % \
              (cmd, data, data&0xffffffff, rg.xRegTable[cmd]))
    if spi is None:
        return
    data &= 0xffffffff
    val = list(data.to_bytes(size, byteorder='big'))
    msg = [cmd] + val
    spi.xfer2(msg)

def rd(cmd, dbg=False, ext=0x80000000, mask=0xffffffff):
    if dbg:
        print("rd %2d %s" % (cmd, rg.xRegTable[cmd]))
    if spi is None:
        return(0)
    msg = [cmd]
    spi.xfer2(msg)
    val = spi.readbytes(4)
    result = int.from_bytes(val, byteorder='big')
    if result & ext:
        result |= -1 & ~mask
    return(result)

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
        self.ser = Serial()
        self.rpi = PiLathe()
        if system() == 'Linux':
            if os.uname().machine.startswith('arm'):
                global spi
                import spidev
                bus = 0
                device = 0
                spi = spidev.SpiDev()
                spi.open(bus, device)
                spi.max_speed_hz = 500000
                spi.mode = 0
        print(self.rpi.spSteps)
    
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
        pass
    
    def command(self, cmdVal):
        print("cmd %12s" % (cmdTable[cmdVal][0]))
        self.rpi.cmdAction[cmdVal]()


    def queParm(self, parmIndex, val):
        self.setParm(parmIndex, val)

    def sendMulti(self):
        pass

    def setParm(self, parmIndex, val):
        (name, varType, varName) = parmTable[parmIndex]
        if varType == 'float':
            val = float(val)
            valString = "%13.6f" % val
            valString = re.sub("0+$", "", valString)
            if valString.endswith('.'):
                valString += '0'
        else:
            val = int(val)
            valString = "%6d" % val
        print("%24s %16s %-7s" % (name, varName, valString))
        setattr(self.rpi, varName, val)

    def getParm(self, parmIndex, dbg=False):
        pass

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

    def getQueueStatus(self):
        return(64)

class PiLathe(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.threadRun = True
        self.threadDone = False
        self.cmdAction = [None] * len(cmdTable)
        for index, (cmd, action) in enumerate(cmdTable):
            if action is not None:
                self.cmdAction[index] = getattr(self, action)

        for (index, varType, name) in parmTable:
            setattr(self, name, None)

        self.cfgCtl = 0
        
        self.zAxis = Axis(self, Z_AXIS)
        self.xAxis = Axis(self, X_AXIS)

        self.zAxis.slvAxis = self.xAxis
        self.xAxis.slvAxis = self.zAxis

        self.moveQue = Queue()

        self.zLoc = 0
        self.xLoc = 0
        self.curRpm = 0
        self.passVal = 0
        self.droZ = 0
        self.droX = 0
        self.mvStatus = 0
        self.postUpdate = None
        self.dbgDispatch = None
        self.dbgQue = Queue()
        self.startEncoder = False

        self.start()

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

        pass

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
        self.mvStatus &= ~(ct.MV_PAUSE | ct.MV_ACTIVE | ct.MV_HOME_ACTIVE)

    def syncSetup(self):
        pass

    def xSetup(self):
        self.xAxis.init()

    def zSetup(self):
        self.zAxis.init()

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
        if self.stepperDrive:
            pass
        else:
            if self.cfgSwitch:
                pass

            if self.cfgVarSpeed:
                pass

    def spindleStop(self):
        if self.stepperDrive:
            pass
        else:
            if self.cfgSwitch:
                pass

            if self.cfgVarSpeed:
                pass
        pass

    def xHomeAxis(self):
        pass

    def xJogMove(self):
        pass

    def xJogSpeed(self):
        pass

    def xMoveAbs(self):
        pass

    def xMoveRel(self):
        pass

    def xStop(self):
        pass

    def zJogMove(self):
        pass

    def zJogSpeed(self):
        pass

    def zMoveAbs(self):
        pass

    def zMoveRel(self):
        pass

    def zStop(self):
        pass

    def dbgMsg(self, cmd, val):
        # self.dbgQue.put((time(), cmd, val))
        self.dbgDispatch(time(), cmd, val)
        
    # move queue

    def run(self):
        self.cmdPause = False
        self.mvState = en.M_IDLE
        self.mvLastState = en.M_IDLE
        self.mvCtl = [None] * len(en.mStatesList)
        self.mvCtl[en.M_IDLE] = self.mvIdle
        self.mvCtl[en.M_WAIT_Z] = self.mvWaitZ
        self.mvCtl[en.M_WAIT_X] = self.mvWaitX
        self.mvCtl[en.M_WAIT_SPINDLE] = self.mvWaitSpindle
        self.mvCtl[en.M_START_SYNC] = self.mvStartSync
        self.mvCtl[en.M_WAIT_SYNC_READY] = self.mvSyncReady
        self.mvCtl[en.M_WAIT_SYNC_DONE] = self.mvSyncDone
        self.mvCtl[en.M_WAIT_MEASURE_DONE] = self.mvMeasureDone
        self.mvCtl[en.M_WAIT_PROBE] = self.mvProbe
        self.mvCtl[en.M_WAIT_MEASURE] = self.mvMeasure
        self.mvCtl[en.M_WAIT_SAFE_X] = self.mvSafeX
        self.mvCtl[en.M_WAIT_SAFE_Z] = self.mvSafeZ

        self.move = [None] * len(en.mCommandsList)
        self.move[en.MOVE_Z] = self.moveZ
        self.move[en.MOVE_X] = self.moveX
        self.move[en.SAVE_Z] = self.saveZ
        self.move[en.SAVE_X] = self.saveX
        self.move[en.SAVE_Z_OFFSET] = self.saveZOffset
        self.move[en.SAVE_X_OFFSET] = self.saveXOffset
        self.move[en.SAVE_TAPER] = self.saveTaper
        self.move[en.MOVE_ZX] = self.moveZX
        self.move[en.MOVE_XZ] = self.moveXZ
        self.move[en.TAPER_ZX] = self.taperZX
        self.move[en.TAPER_XZ] = self.taperXZ
        self.move[en.START_SPINDLE] = self.startSpindle
        self.move[en.STOP_SPINDLE] = self.stopSpindle
        self.move[en.Z_SYN_SETUP] = self.zSynSetup
        self.move[en.X_SYN_SETUP] = self.xSynSetup
        self.move[en.PASS_NUM] = self.passNum
        self.move[en.QUE_PAUSE] = self.quePause
        self.move[en.MOVE_Z_OFFSET] = self.moveZOffset
        self.move[en.SAVE_FEED_TYPE] = self.saveFeedType
        self.move[en.Z_FEED_SETUP] = self.zFeedSetup
        self.move[en.X_FEED_SETUP] = self.xFeedSetup
        self.move[en.SAVE_FLAGS] = self.saveFlags
        self.move[en.PROBE_Z] = self.probeZ
        self.move[en.PROBE_X] = self.probeX
        self.move[en.SAVE_Z_DRO] = self.saveZDro
        self.move[en.SAVE_X_DRO] = self.saveXDro
        self.move[en.OP_DONE] = self.opDone

        axisDbg = WINDOWS
        
        while self.fpgaFrequency is None:
            sleep(0.1)
            
        print("starting loop")
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

    def update(self):
        if self.postUpdate is None:
            return
        result = (en.EV_READ_ALL, self.zLoc, self.xLoc, self.curRPM, \
                  self.passVal, self.droZ, self.droX, self.mvStatus)
        self.postUpdate(result)

    def readData(self, base, prt=True):
        global xPos, yPos, zSum, zAclSum, aclCtr, curLoc, curDist
        bSyn = base + rg.F_Sync_Base
        xPos = rd(bSyn + rg.F_Rd_XPos)
        yPos = rd(bSyn + rg.F_Rd_YPos)
        zSum = rd(bSyn + rg.F_Rd_Sum)
        zAclSum = rd(bSyn + rg.F_Rd_Accel_Sum)
        aclCtr = rd(bSyn + rg.F_Rd_Accel_Ctr)
        if prt:
            print("xPos %7d yPos %6d zSum %12d" % (xPos, yPos, zSum), end=" ")
            print("aclSum %8d aclCtr %8d" % (zAclSum, aclCtr), end=" ")

        bDist = base + rg.F_Dist_Base
        curDist = rd(bDist + rg.F_Rd_Dist) # read z location
        curAcl = rd(bDist + rg.F_Rd_Acl_Steps) # read accel steps

        curLoc = rd(base + rg.F_Loc_Base + rg.F_Rd_Loc, \
                    False, 0x20000, 0x3ffff)

        if prt:
            print("dist %6d aclStp %6d loc %5d" % (curDist, curAcl, curLoc))

    def axisCtl(self, dbg=False):
        indexClks = rd(rg.F_Rd_Idx_Clks)
        if indexClks != 0:
            # rpm = (clocks * sec / clocks / rev) * sec / minute
            self.curRPM = intRound((float(self.fpgaFrequency) / \
                                    (indexClks + 1)) * 60)
        else:
            self.curRPM = 0

        status = rd(rg.F_Rd_Status, False)
        axis = self.zAxis
        if axis.state != en.AXIS_IDLE:
            if not dbg:
                tmp =  rd(rg.F_ZAxis_Base + rg.F_Loc_Base + rg.F_Rd_Loc, \
                          False, 0x20000, 0x3ffff)
            else:
                tmp = axis.expLoc
            if axis.loc != tmp:
                self.zLoc = axis.loc = tmp
                # print(tmp)

            if (status & bt.zAxisDone) != 0 or dbg:
                axis.done = True
                axis.wait = False
                ld(rg.F_ZAxis_Base + rg.F_Ld_Axis_Ctl, 0, 1)

            if axis.wait:
                if dbg:
                    status |= bt.zAxisDone
                elif (status & bt.zAxisEna) == 0:
                    # axis.wait = False
                    print("z waiting no enable")

            axis.control()

        axis = self.xAxis
        status = rd(rg.F_Rd_Status, False)
        if axis.state != en.AXIS_IDLE:
            # print("{0:04b}".format(status), end=' ')
            # self.readData(rg.F_XAxis_Base)
            if not dbg:
                tmp =  rd(rg.F_XAxis_Base + rg.F_Loc_Base + rg.F_Rd_Loc, \
                          False, 0x20000, 0x3ffff)
            else:
                tmp = axis.expLoc
            if axis.loc != tmp:
                self.xLoc = axis.loc = tmp
                # print(tmp)

            if (status & bt.xAxisDone) != 0 or dbg:
                axis.done = True
                axis.wait = False
                ld(rg.F_XAxis_Base + rg.F_Ld_Axis_Ctl, 0, 1)

            if axis.wait:
                if dbg:
                    status |= bt.xAxisDone
                elif (status & bt.xAxisEna) == 0:
                    # axis.wait = False
                    print("x waiting no enable")

            axis.control()
    
    def procMove(self):
        if self.cmdPause and self.mvState == en.M_IDLE:
            return
        self.mvCtl[self.mvState]()
        if self.mvState != self.mvLastState:
            self.mvLastState = self.mvState
            self.dbgMsg(en.D_MSTA, self.mvState)

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
                self.move[op](val)
            except IndexError:
                pass
            except Empty:
                return

            if self.mvState != en.M_IDLE or self.cmdPause:
                break

    # move functions

    def moveZ(self, val):
        dest = intRound(val * self.zAxis.stepsInch) + self.zAxis.homeOffset
        print("moveZ dest %d val %d zStepsInch %d zHomeOffset %d" % \
              (dest, val, self.zAxis.stepsInch, self.zAxis.homeOffset))
        self.mvState = en.M_WAIT_Z
        self.zAxis.move(dest, self.cmdFlag)

    def moveX(self, val):
        dest = val + self.xAxis.homeOffset
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

    def moveZX(self, val):
        pass

    def moveXZ(self, val):
        pass
    
    def taperZX(self, val):
        print("taper zx %7.4f" % (val))
        self.taperSetup(self.zAxis, self.xAxis, val)
        self.mvState = en.M_WAIT_Z

    def taperXZ(self, val):
        print("taper xz %7.4f" % (val))
        self.taperSetup(self.xAxis, self.zAxis, val)
        self.mvState = en.M_WAIT_X

    def taperSetup(self, mvAxis, tpAxis, val):
        mvAxis = self.zAxis
        tpAxis = self.xAxis
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
        tpAxis.taperAccel.taperCalc(mvAxis.turnAccel, taper)
        mvAxis.move(loc, ct.CMD_SYN | ct.SYN_START | ct.SYN_TAPER)

    def startSpindle(self, val):
        print("startSpindle")
        self.mvSpindleCmd = self.cmd
        self.spindleStart()
        self.mvState = en.M_WAIT_SPINDLE
        
    def stopSpindle(self, val):
        print("stopSpindle")
        self.mvSpindleCmd = self.cmd
        self.spindleStop()
        self.mvState = en.M_WAIT_SPINDLE

    def zSynSetup(self, val):
        print("zSynSetup")
        self.zFeed = val
        currentOp = self.currentOp
        if currentOp == en.OP_TURN:
            pass
        elif currentOp == en.OP_TAPER:
            pass
        elif currentOp == en.OP_THREAD:
            pass

        if self.turnSync == en.SEL_TU_ENC:
            self.zAxis.encParm = True
            self.zAxis.turnAccel.syncAccelCalc(self.feedType, val)
        elif self.turnSync == en.SEL_TU_SYN:
            self.zAxis.encParm = False
            self.mvState = en.M_START_SYNC

    def xSynSetup(self, val):
        print("xSynSetup")
        self.xFeed = val
        currentOp = self.currentOp
        if currentOp == en.OP_FACE:
            pass
        elif currentOp == en.OP_CUTOFF:
            pass
        elif currentOp == en.OP_TAPER:
            pass
        elif currentOp == en.THREAD:
            pass

        if self.turnSync == en.SEL_TU_ENC:
            self.xAxis.encParm = True
            self.xAxis.turnAccel.syncAccelCalc(self.feedType, val)
        else:
            self.xAxis.encParm = False
            self.mvState = en.M_START_SYNC

    def passNum(self, val):
        print("passNum")
        self.passVal = val
        if (val & 0xff00) == 0:
            self.currentPass = val & 0xff
        else:
            self.springInfo = val
        self.dbgMsg(en.D_PASS, val)

    def quePause(self, val):
        print("quePause")
        self.cmdPause = True
        self.mvStatus |= ct.MV_PAUSE

    def moveZOffset(self, val):
        pass

    def saveFeedType(self, val):
        self.feedType = val

    def zFeedSetup(self, val):
        pass

    def xFeedSetup(self, val):
        pass

    def saveFlags(self, val):
        self.threadFlag = val

    def probeX(self, val):
        pass

    def probeZ(self, val):
        pass

    def saveZDro(self, val):
        pass

    def saveXDro(self, val):
        pass

    def opDone(self, val):
        self.dbgMsg(en.D_DONE, val)
        if val == ct.PARM_START:
            self.mvStatus |= ct.MV_ACTIVE
            pass
        elif val == ct.PARM_DONE:
            self.mvStatus &= ~ct.MV_ACTIVE
            pass

    # move states

    def mvWaitZ(self):
        if self.zAxis.state == en.AXIS_IDLE:
            self.mvState = en.M_IDLE

    def mvWaitX(self):
        if self.xAxis.state == en.AXIS_IDLE:
            self.mvState = en.M_IDLE

    def mvWaitSpindle(self):
        if WINDOWS:
            self.mvState = en.M_IDLE
            return
        indexClks = rd(rg.F_Rd_Idx_Clks)
        print("indexClks %d", (indexClks))
        if indexClks != self.lastIdxClks:
            self.lastIdxClks = indexClks
            if indexClks != 0:
                delta = abs(indexClks - self.lastIdxClks)
                percent = float(delta) * 100.0 / indexClks
                indexClks += 1
                rpm = intRound((float(self.fpgaFrequency) / indexClks) * 60)
                print("delta %d percent %7.2f rpm %d" % (delta, percent, rpm))
                if percent < 1.0:
                    if self.mvSpindleCmd == en.STOP_SPINDLE:
                        self.mvState = en.M_IDLE
                    elif self.mvSpindleCmd == en.START_SPINDLE:
                        self.mvState = en.M_IDLE

    def mvStartSync(self):
        ld(rg.F_Enc_Base + rg.F_Ld_Enc_Cycle, self.lSyncCycle ,2)
        ld(rg.F_Enc_Base + rg.F_Ld_Int_Cycle, self.lSyncOutput ,2)
        ld(rg.F_Ld_Sync_Ctl, bt.synEncInit, 1)
        ld(rg.F_Ld_Sync_Ctl, bt.synEncEna, 1)
        self.mvState = en.M_WAIT_SYNC_READY

    def mvSyncReady(self):
        status = rd(rg.F_Rd_Status, 4)
        if (status & bt.syncActive) != 0:
            self.mvState = en.M_IDLE

    def mvSyncDone(self):
        pass

    def mvMeasureDone(self):
        pass

    def mvProbe(self):
        pass

    def mvMeasure(self):
        pass

    def mvSafeX(self):
        pass

    def mvSafeZ(self):
        pass

MAX_SCALE = 12

class Accel():
    def __init__(self, rpi, axis):
        self.rpi = rpi
        self.axis = axis
        self.freqDivider = self.d = self.incr1 =  self.incr2 = \
        self.intAccel =  self.accelClocks =  self.minFeed = \
        self.maxFeed = 0

    def update(self, label, minFeed=0, maxFeed=0):
        self.label = label
        self.minFeed = minFeed
        self.maxFeed = maxFeed
        self.clockFreq = self.rpi.fpgaFrequency
        self.accelCalc1()

    def load(self, dist, encParm=True):
        print("\n%s load" % (self.label))
        axis = self.axis
        axisCtl = axis.axisCtl
        base = axis.base
        if encParm:
            ld(base + rg.F_Ld_Axis_Ctl, bt.ctlInit, 1)

            if self.freqDivider != 0:
                ld(base + rg.F_Ld_Freq, self.freqDivider, 4)

            bSyn = base + rg.F_Sync_Base
            ld(bSyn + rg.F_Ld_D, self.d, 4)		# load d value
            ld(bSyn + rg.F_Ld_Incr1, self.incr1, 4)	# load incr1 value
            ld(bSyn + rg.F_Ld_Incr2, self.incr2, 4)	# load incr2 value

            ld(bSyn + rg.F_Ld_Accel_Val, self.intAccel, 4)   # load accel
            ld(bSyn + rg.F_Ld_Accel_Count, self.accelClocks, 4) # load acl ctr

            ld(base + rg.F_Dist_Base + rg.F_Ld_Dist, dist, 4)
        else:
            ld(base + rg.F_Dist_Base + rg.F_Ld_Dist, dist, 4)
            axisCtl |=  bt.ctlChDirect
        ld(base + rg.F_Ld_Axis_Ctl, bt.ctlStart | axisCtl, 1)

    def start(self, axisCtl=0):
        axisCtl |= self.axis.axisCtl | bt.ctlStart
        ld (self.axis.base, axisCtl, 1)

    def accelCalc(self):
        print("\n%s accelCalc" % (self.label))
        if self.maxFeed == 0:
            return
        rpi = self.rpi
        stepsInch = self.axis.stepsInch
        stepsSecMax = intRound((self.maxFeed / 60.0) * stepsInch)
        self.clockFreq = stepsSecMax * rpi.freqMult
        self.clocksPerInch = stepsInch * rpi.freqMult
        self.freqDivider = int((rpi.fpgaFrequency / self.clockFreq) - 1)
        if DBG_SETUP:
            print("stepsInch %d freqMult %d fpgaFrequency %d" % \
                  (stepsInch, rpi.freqMult, rpi.fpgaFrequency))
            print("freqGenMax %d freqDivider %d" % \
                  (self.clockFreq, self.freqDivider))
        self.accelSetup()

    def syncAccelCalc(self, feedType, feed):
        print("\n%s synAccelCalc" % (self.label))
        if feedType == ct.FEED_PITCH:
            self.pitch = feed
        elif feedType == ct.FEED_TPI:
            self.pitch = 1.0 / feed
        elif feedType == ct.FEED_METRIC:
            self.pitch = feed / 25.4

        if DBG_SETUP:
            print("\nturnAccel %3.1f" % self.axis.accel)
        rpi = self.rpi
        self.freqDivider = 0
        if self.maxFeed == 0:
            encPerInch = intRound(rpi.encPerRev / self.pitch)
            self.dx = encPerInch
            self.dy = self.axis.stepsInch
            self.incr1 = 2 * self.dy
            self.incr2 = self.incr1 - 2 * self.dx
            self.initlSum = self.incr1 - self.dx
            self.intAccel = 0
            self.accelClks = 0
            if DBG_SETUP:
                print("encPerInch dx %d stepsInch dy %d "\
                      "incr1 %d incr2 %d d %d" % \
                      (self.dx, self.dy, self.incr1, self.incr2, self.initlSum))
        else:
            self.maxFeed = rpi.rpm * self.pitch
            self.clocksPerInch = intRound(rpi.encPerRev * self.pitch)
            self.clockFreq = intRound((rpi.rpm * rpi.encPerRev) / 60.0)
            self.accelSetup()

    def accelCalc1(self):
        print("\n%s accelCalc" % (self.label))
        if self.maxFeed == 0:
            return
        rpi = self.rpi
        stepsInch = self.axis.stepsInch
        stepsSecMax = intRound((self.maxFeed * stepsInch) / 60)
        freqGenMax = stepsSecMax * rpi.freqMult
        print("stepsSecMax %6.0f freqGenMax %7.0f" % (stepsSecMax, freqGenMax))

        stepsSecMin = intRound((self.minFeed * stepsInch) / 60)
        freqGenMin = stepsSecMin * rpi.freqMult
        print("stepsSecMin %6.0f freqGenMin %7.0f" % (stepsSecMin, freqGenMin))

        self.freqDivider = int(self.clockFreq / freqGenMax) - 1
        print("freqDivider %3.0f" % self.freqDivider)

        accelTime = (self.maxFeed - self.minFeed) / (60.0 * self.axis.accel)
        self.accelClocks = intRound(accelTime * freqGenMax)
        print("accelTime %8.6f clocks %d" % (accelTime, self.accelClocks))

        self.dxBase = int(freqGenMax)
        self.dyMinBase = int(stepsSecMin)
        self.dyMaxBase = int(stepsSecMax)

        self.accelSetup1()

    def bitSize(self, val):
        bits = 0
        while bits < 32:
            if val == 0:
                break
            val >>= 1
            bits += 1
        return(bits)

    def accelSetup1(self):
        accelClocks = self.accelClocks
        scalePrt = False
        for scale in range(0, 10):
            dx =  self.dxBase << scale
            dyMin =  self.dyMinBase << scale
            dyMax =  self.dyMaxBase << scale
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
        d = incr1 - dx

        bits = int(floor(log(abs(incr2), 2))) + 1
        print(("dx %d dy %d incr1 %d incr2 %d d %d bits %d scale %d" %
               (dx, dyIni, incr1, incr2, d, bits, scale)))

        synAccel = 2 * intIncPerClock

        totalSum = (accelClocks * incr1) + d
        totalInc = (accelClocks * (accelClocks - 1) * synAccel) / 2
        accelSteps = ((totalSum + totalInc) / (2 * dx))

        print(("accelClocks %d totalSum %d totalInc %d accelSteps %d" % 
               (accelClocks, totalSum, totalInc, accelSteps)))

        self.scale = scale
        self.incr1 = incr1
        self.incr2 = incr2
        self.initlSum = d
        self.intAccel = synAccel

    def accelSetup(self):
        stepsInch = self.axis.stepsInch
        if DBG_SETUP:
            print("accel %0.2f minFeed %0.2f feedRate %0.2f ipm" % \
                  (self.axis.accel, self.minFeed, self.maxFeed))
            print("clocksPerInch %d clockFreq %d stepsInch %d" % \
                  (self.clocksPerInch, self.clockFreq, stepsInch))

        stepsSecMax = intRound((self.maxFeed * stepsInch) / 60.0)
        stepsSecMin = intRound((self.minFeed * stepsInch) / 60.0)
        if DBG_SETUP:
            print("stepsSecMin %d stepsSecMax %d" % (stepsSecMin, stepsSecMax))

        stepsSec2 = float(self.axis.accel) * stepsInch
        self.accelTime = (stepsSecMax - stepsSecMin) / stepsSec2
        self.accelClks = intRound(self.clockFreq * self.accelTime)
        if DBG_SETUP:
            print("stepsSec2 %0.0f accelTime %8.6f accelClks %d" % \
                  (stepsSec2, self.accelTime, self.accelClks))

        accelMinStep = intRound(((stepsSecMin / stepsSec2) * \
                                  stepsSecMin) / 2.0)
        accelMaxStep = intRound(((stepsSecMax / stepsSec2) * \
                                  stepsSecMax) / 2.0)
        self.accelSteps = accelMaxStep - accelMinStep
        if DBG_SETUP:
            print("accelSteps %d accelMinStep %d accelMaxStep %d" % \
                  (self.accelSteps, accelMinStep, accelMaxStep))

        dxBase = self.clocksPerInch
        dyMaxBase = stepsInch
        dyMinBase = intRound((stepsInch * self.minFeed) / self.maxFeed)
        if DBG_SETUP:
            print("\ndxBase %d dyMaxBase %d dyMinBase %d" % \
                  (dxBase, dyMaxBase, dyMinBase))

        accelClks = self.accelClks
        intIncPerClock = 0
        for scale in range(MAX_SCALE):
            self.dx = dxBase << scale
            self.dyMax = dyMaxBase << scale
            dyMin = dyMinBase << scale
            dyDelta = self.dyMax - dyMin
            if DBG_DETAIL:
                print("\nscale %d dx %d dyMin %d dyMax %d dyDelta %d" % \
                      (scale, self.dx, dyMin, self.dyMax, dyDelta), end=' ')
                print("%10.4f" % (float(self.dx) / float(self.dyMax)))

            incPerClock = float(dyDelta) / accelClks
            intIncPerClock = int(incPerClock)
            if intIncPerClock == 0:
                continue
            self.intIncPerClock = intIncPerClock
            dyDeltaC = intIncPerClock * accelClks
            err = intRound(abs(dyDelta - dyDeltaC)) >> scale
            self.dyIni = self.dyMax - intIncPerClock * accelClks
            if DBG_DETAIL:
                print("dyIni %d dyMax %d intIncPerClock %d accelClks %d" %
                      (self.dyIni, self.dyMax, intIncPerClock, accelClks))

            bits = self.bitSize(self.dx) + 1
            if DBG_DETAIL:
                print("dyIni %d dyMax %d dyDelta %d incPerClock %6.2f " \
                      "err %d bits %d" %
                      (self.dyIni, self.dyMax, dyDelta, incPerClock, \
                       err, bits))

            if (bits >= 30) or (err == 0):
                if DBG_SETUP:
                    print("\nscale %d dx %d dyMin %d dyMax %d dyDelta %d" %
                          (scale, self.dx, dyMin, self.dyMax, dyDelta))
                    print("dyIni %d dyMax %d dyDelta %d incPerClock %6.2f " \
                          "err %d bits %d" %
                          (self.dyIni, self.dyMax, dyDelta, incPerClock, \
                           err, bits))
                break

        self.scale = scale
        self.incr1 = 2 * self.dyIni
        self.incr2 = self.incr1 - 2 * self.dx
        self.initlSum = self.incr1 - self.dx
        self.intAccel = 2 * intIncPerClock
        if DBG_SETUP:
            print("\nincr1 %d incr2 %d sum %d" %
                  (self.incr1, self.incr2, self.initlSum))

        if intIncPerClock != 0:
            totalSum = accelClks * self.incr1 + self.initlSum
            totalInc = (accelClks * (accelClks - 1) * self.intAccel) / 2
            self.accelSteps = intRound((totalSum + totalInc) / (2 * self.dx))
            if DBG_SETUP:
                print("accelClks %d totalSum %d totalInc %d " \
                      "accelSteps %d" % \
                      (self.accelClks, totalSum, totalInc, self.accelSteps))
        else:
            self.accelSteps = 0

    def taperCalc(self, turnAccel, taper):
        print("taperCalc a0 %s a1 %s taper %8.6f" % \
              (turnAccel.label, self.label, taper))
        rpi = self.rpi
        stepsInch = self.axis.stepsInch
        self.taper = 1
        self.taperInch = taper

        turnCycleDist = rpi.taperCycleDist
        taperCycleDist = taper * turnCycleDist

        print("turnCycleDist %6.4f taperCycleDist %6.4f" %
              (turnCycleDist, taperCycleDist))

        turnSync = rpi.turnSync
        if turnSync == en.SEL_TU_STEP:
            turnSteps = intRound(turnCycleDist * turnAccel.axis.stepsInch)
            taperSteps = intRound(taperCycleDist * stepsInch)
            print("**not done")
        elif turnSync == en.SEL_TU_ENC:
            dx = intRound((rpi.encPerRev * turnCycleDist) / turnAccel.pitch)
            dy = intRound(taperCycleDist * stepsInch)
            self.incr1 = 2 * dy
            self.incr2 = self.incr1 - 2 * dx
            self.d = self.incr1 - dx
            print("encPerCycle dx %d stepsCycle dy %d incr1 %d incr2 %d d %d" %
	           (dx, dy, self.incr1, self.incr2, self.d))
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
        self.axis = axis
        self.state = en.AXIS_IDLE
        self.lastState = self.state
        self.stateDisp = [None] * en.AXIS_STATES
        self.stateDisp[en.AXIS_IDLE] = self.idle
        self.stateDisp[en.AXIS_WAIT_BACKLASH] = self.waitBacklash
        self.stateDisp[en.AXIS_START_MOVE] = self.startMove
        self.stateDisp[en.AXIS_WAIT_MOVE] = self.waitMove
        self.stateDisp[en.AXIS_DELAY] = self.delay
        self.stateDisp[en.AXIS_DONE] = self.doneMove
        self.turnAccel = Accel(rpi, self)
        self.taperAccel = Accel(rpi, self)
        self.moveAccel = Accel(rpi, self)
        self.jogAccel = Accel(rpi, self)
        self.jogSlowAccel = Accel(rpi, self)
        self.dir = ct.DIR_POS
        self.dist = 0
        self.cmd = 0
        self.axisCtl = 0
        self.wait = False
        self.done = False
        self.wait = False
        self.loc = 0
        self.slvAxis = None
        self.encParm = None
        
    def init(self):
        rpi = self.rpi
        if self.axis == Z_AXIS:
            self.name = 'z'
            self.base = base = rg.F_ZAxis_Base
            stepsInch = intRound((rpi.zMicro * rpi.zMotor) / rpi.zPitch)
            self.stepsInch = stepsInch
            self.accel = rpi.zAccel
            self.turnAccel.update("zTurn")
            self.taperAccel.update("zTaper")
            self.moveAccel.update("zMove", rpi.zMoveMin, rpi.zMoveMax)
            self.jogAccel.update("zJog", rpi.zJogMin, rpi.zJogMax)
            self.jogSlowAccel.update("zJogSlow", rpi.zJogMin, rpi.zJogMax)
            self.backlashSteps = intRound(rpi.zBacklash * stepsInch)
            if rpi.zDirFlag:
                rpi.cfgCtl |= bt.cfgZDir
            else:
                rpi.cfgCtl &= ~bt.cfgZDir
            self.clkSel = \
                (bt.zClkNone, bt.zClkZFreq, bt.zClkCh, bt.zClkIntClk, \
                 bt.zClkXStep, bt.zClkXCh, bt.zClkSpare, bt.zClkDbgFreq)
            self.dbgBase = en.D_ZMOV
        else:
            self.name = 'x'
            self.base = base = rg.F_XAxis_Base
            stepsInch = intRound((rpi.xMicro * rpi.xMotor) / rpi.xPitch)
            self.stepsInch = stepsInch
            self.backlashSteps = intRound(rpi.xBacklash * stepsInch)
            self.accel = rpi.xAccel
            self.turnAccel.update("xTurn")
            self.taperAccel.update("xTaper")
            self.moveAccel.update("xMove", rpi.xMoveMin, rpi.xMoveMax)
            self.jogAccel.update("xJog", rpi.xJogMin, rpi.xJogMax)
            self.jogSlowAccel.update("xJogSlow", rpi.xJogMin, rpi.xJogMax)
            if rpi.xDirFlag:
                rpi.cfgCtl |= bt.cfgXDir
            else:
                rpi.cfgCtl &= ~bt.cfgXDir
            self.clkSel = \
                (bt.xClkNone, bt.xClkXFreq, bt.xClkCh, bt.xClkIntClk, \
                 bt.xClkZStep, bt.xClkZCh, bt.xClkSpare, bt.xClkDbgFreq)
            self.dbgBase = en.D_ZMOV
        ld(base + rg.F_Loc_Base + rg.F_Ld_Loc, 0, 4)
        axisCtl = bt.ctlInit | bt.ctlSetLoc
        ld(base + rg.F_Ld_Axis_Ctl, axisCtl, 1)
        self.axisCtl = 0
        ld(base + rg.F_Ld_Axis_Ctl, axisCtl, 1)

    def loadClock(self, clkCtl):
        ld(rg.F_Ld_Clk_Ctl, clkCtl, 1)

    def move(self, pos, cmd):
        if self.state != en.AXIS_IDLE:
            return
        if not WINDOWS:
            self.loc = rd(self.base + rg.F_Loc_Base + rg.F_Rd_Loc, \
                          True, 0x20000, 0x3ffff)
        self.expLoc = pos
        print("%sAxis loc %d pos %d" % (self.name, self.loc, pos))
        self.rpi.dbgMsg(self.dbgBase + D_MOV, pos)
        self.moveRel(pos - self.loc, cmd)

    def moveRel(self, dist, cmd):
        if self.state != en.AXIS_IDLE:
            return
        self.rpi.dbgMsg(self.dbgBase + D_DST, dist)
        self.cmd = cmd
        if dist != 0:
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
                self.moveAccel.load(self.backlashSteps)
                self.state = en.AXIS_WAIT_BACKLASH
            else:
                self.state = en.AXIS_START_MOVE
                self.control()
        
    def control(self):
        if self.state != self.lastState:
            self.lastState = self.state
            self.rpi.dbgMsg(self.dbgBase + D_ST, self.state)
            print("%s control %s" % (self.name, en.axisStatesList[self.state]))
        if self.state != en.AXIS_IDLE:
            self.stateDisp[self.state]()

    def idle(self):
        pass

    def waitBacklash(self):
        if self.done:
            self.done = False
            self.wait = False
            self.state = en.AXIS_START_MOVE

    def startMove(self):
        cmd = self.cmd & ct.CMD_MSK
        if cmd == ct.CMD_SYN:
            if (self.cmd & ct.SYN_START) != 0:
                self.axisCtl |= bt.ctlWaitSync
            clkCtl = self.clkSel[bt.clkCh if self.encParm else bt.clkIntClk]
            if self.cmd & ct.SYN_TAPER:
                slvAxis = self.slvAxis
                slvAxis.taperAccel.load(slvAxis.taperDist, slvAxis.encParm)
                clkCtl |= slvAxis.clkSel[bt.clkSlvFreq]
                ld(slvAxis.base + rg.F_Ld_Axis_Ctl,
                   slvAxis.axisCtl | bt.ctlSlave, 1)
            self.loadClock(clkCtl)
            self.turnAccel.load(self.dist, self.encParm)
        elif cmd == ct.CMD_JOG:
            self.moveAccel.load(self.dist)
            self.loadClock(self.clkSel[bt.clkFreq])
        elif cmd == ct.CMD_MAX or cmd == ct.CMD_MOV:
            self.moveAccel.load(self.dist)
            # self.rpi.readData(self.base)
            self.loadClock(self.clkSel[bt.clkFreq])
        elif cmd == ct.CMD_SPEED:
            pass
        elif cmd == ct.JOGSLOW:
            pass
        else:
            pass
        self.wait = True
        self.state = en.AXIS_WAIT_MOVE

    def waitMove(self):
        if self.done:
            self.done = False
            self.wait = False
            self.state = en.AXIS_DONE

    def delay(self):
        pass

    def doneMove(self):
        self.done = False
        self.cmd = 0
        if not WINDOWS:
            self.loc = rd(self.base + rg.F_Loc_Base + rg.F_Rd_Loc, \
                          True, 0x20000, 0x3ffff)
        else:
            self.loc = self.expLoc
        self.rpi.dbgMsg(self.dbgBase + D_LOC, self.loc)
        if self.loc != self.expLoc:
            self.rpi.dbgMsg(D_EXP, self.expLoc)
        self.state = en.AXIS_IDLE
        self.rpi.dbgMsg(self.dbgBase + D_ST, self.state)
