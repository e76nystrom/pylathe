
from threading import Event, Lock, Thread
from queue import Empty, Queue
from sys import stderr, stdout
from time import sleep
from platform import system
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

def ld(cmd, data, size):
    print("ld %2d %10d %s" % (cmd, data, rg.xRegTable[cmd]))
    if spi is None:
        return
    data &= 0xffffffff
    val = list(data.to_bytes(size, byteorder='big'))
    msg = [cmd] + val
    spi.xfer2(msg)

def rd(cmd, dbg=True):
    if dbg:
        print("rd %2d %s" % (cmd, rg.xRegTable[cmd]))
    if spi is None:
        return(0)
    msg = [cmd]
    spi.xfer2(msg)
    val = spi.readbytes(rg.fpgaSizeTable[cmd])
    result = int.from_bytes(val, byteorder='big')
    if result & 0x80000000:
        result |= -1 & ~0xffffffff
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
            if os.uname().nodename == 'raspberrypi':
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
        self.curRpm = '0.0'
        self.passVal = 0
        self.droZ = 0
        self.droX = 0
        self.mvStatus = 0
        self.postUpdate = None

        self.start()

    def setPostUpdate(self, postUpdate):
        self.postUpdate = postUpdate

    def clearQue(self):
        pass

    def clearDbg(self):
        pass

    def clearCmd(self):
        pass

    def measureCmd(self):
        pass

    def pauseCmd(self):
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
        pass

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
        pass

    def spindleStop(self):
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

    # move queue

    def run(self):
        self.cmdPause = False
        self.mvState = en.M_IDLE
        self.mvCtl = [None] * len(en.mStatesList)
        self.mvCtl[en.M_IDLE] = self.mvIdle
        self.mvCtl[en.M_WAIT_Z] = self.mvWaitZ
        self.mvCtl[en.M_WAIT_X] = self.mvWaitX
        self.mvCtl[en.M_WAIT_SPINDLE] = self.mvWaitSpindle
        self.mvCtl[en.M_WAIT_SYNC_READY] = self.mvSyncReady
        self.mvCtl[en.M_WAIT_SYNC_DONE] = self.mvSyncDone
        self.mvCtl[en.M_WAIT_MEASURE_DONE] = self.mvMeasureDone
        self.mvCtl[en.M_START_SYNC] = self.mvStartSync
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
        result = (en.EV_READ_ALL, self.zLoc, self.xLoc, self.curRpm, \
                  self.passVal, self.droZ, self.droX, self.mvStatus)
        self.postUpdate(result)

    def axisCtl(self, dbg=True):
        axis = self.zAxis
        status = rd(rg.F_Rd_Status, False)
        if axis.state != en.AXIS_IDLE:
            axis.loc =  rd(rg.F_ZAxis_Base + rg.F_Loc_Base + rg.F_Rd_Loc, False)
            if axis.wait:
                if dbg:
                    status |= bt.zAxisDone
                elif (status & bt.zAxisEna) == 0:
                    axis.wait = False
                    print("z wating no enable")

            if (status & bt.zAxisDone) != 0:
                axis.done = True
                axis.wait = False
                ld(rg.F_ZAxis_Base + rg.F_Ld_Axis_Ctl, 0, 1)

            axis.control()

        axis = self.xAxis
        status = rd(rg.F_Rd_Status, False)
        if axis.state != en.AXIS_IDLE:
            axis.loc =  rd(rg.F_XAxis_Base + rg.F_Loc_Base + rg.F_Rd_Loc, False)
            if axis.wait:
                if dbg:
                    status |= bt.xAxisDone
                elif (status & bt.xAxisEna) == 0:
                    axis.wait = False
                    print("z wating no enable")

            if (status & bt.xAxisDone) != 0:
                axis.done = True
                axis.wait = False
                ld(rg.F_XAxis_Base + rg.F_Ld_Axis_Ctl, 0, 1)

            axis.control()
    
    def procMove(self):
        if self.cmdPause and self.mvState == en.M_IDLE:
            return
        self.mvCtl[self.mvState]()

    def mvIdle(self):
        while True:
            try:
                (opString, op, val) = self.moveQue.get(False)
                self.cmdFlag = op >> 16
                if True:
                    if type(val) == 'float':
                        valString = "%13.6f" % val
                        valString = re.sub("0+$", "", valString)
                        if valString.endswith('.'):
                            valString += '0'
                    else:
                        valString = "%6d" % val
                    print("%16s %2d %2d %-7s" % \
                          (opString, op&0xff, self.cmdFlag, valString))
                    stdout.flush()
                self.move[op & 0xff](val)
            except IndexError:
                pass
            except Empty:
                return

            if self.mvState != en.M_IDLE or self.cmdPause:
                break

    # move functions

    def moveZ(self, val):
        dest = intRound(val * self.zAxis.stepsInch) + self.zHomeOffset
        self.mvState = en.M_WAIT_Z
        self.zAxis.move(dest, self.cmdFlag)

    def moveX(self, val):
        dest = val + self.xHomeOffset
        self.mvState = en.M_WAIT_X
        self.xAxis.move(dest, self.cmdFlag)

    def saveZ(self, val):
        self.zVal = intRound(val * self.zAxis.stepsInch) + self.zHomeOffset

    def saveX(self, val):
        self.xVal = intRound(val * self.xAxis.stepsInch) + self.xHomeOffset

    def saveZOffset(self, val):
        self.zHomeOffset = val

    def saveXOffset(self, val):
        self.xHomeOffset = val

    def saveTaper(self, val):
        self.taper = val

    def moveZX(self, val):
        pass

    def moveXZ(self, val):
        pass
    
    def taperZX(self, val):
        pass

    def taperXZ(self, val):
        pass
    
    def startSpindle(self, val):
        pass

    def stopSpindle(self, val):
        pass

    def zSynSetup(self, val):
        self.zFeed = val
        self.zAxis.turnAccel.syncAccelCalc(self.feedType, val)

    def xSynSetup(self, val):
        self.xFeed = val
        self.xAxis.turnAccel.syncAccelCalc(self.feedType, val)

    def passNum(self, val):
        self.passVal = val
        if (val & 0xff00) == 0:
            self.currentPass = val & 0xff
        else:
            self.springInfo = val

    def quePause(self, val):
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
        pass

    def mvSyncReady(self):
        pass

    def mvSyncDone(self):
        pass

    def mvMeasureDone(self):
        pass

    def mvStartSync(self):
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
    def __init__(self, rpi):
        self.rpi = rpi
        self.freqDivider = self.d = self.incr1 =  self.incr2 = \
        self.intAccel =  self.accelClks =  self.minFeed = \
        self.maxFeed = self.accel = 0

    def update(self, label, base, stepsInch, minFeed=0, maxFeed=0, \
               accel=0):
        self.label = label
        self.base = base
        self.minFeed = minFeed
        self.maxFeed = maxFeed
        self.accel = accel
        self.stepsInch = stepsInch
        self.accelCalc()

    def load(self, axisCtl, dist):
        print("\n%s load" % (self.label))
        ld(self.base + rg.F_Ld_Axis_Ctl, bt.ctlInit, 1)

        if self.freqDivider != 0:
            ld(self.base + rg.F_Ld_Freq, self.freqDivider, 4)

        bSyn = self.base + rg.F_Sync_Base
        ld(bSyn + rg.F_Ld_D, self.d, 4)		# load d value
        ld(bSyn + rg.F_Ld_Incr1, self.incr1, 4)	# load incr1 value
        ld(bSyn + rg.F_Ld_Incr2, self.incr2, 4)	# load incr2 value

        ld(bSyn + rg.F_Ld_Accel_Val, self.intAccel, 4)   # load accel
        ld(bSyn + rg.F_Ld_Accel_Count, self.accelClks, 4) # load accel coun

        ld(self.base + rg.F_Dist_Base + rg.F_Ld_Dist, dist, 4)
        ld(self.base + rg.F_Ld_Axis_Ctl, bt.ctlStart | axisCtl, 1)

    def accelCalc(self):
        print("\n%s accelCalc" % (self.label))
        if self.accel == 0:
            return
        rpi = self.rpi
        stepsSecMax = intRound((self.maxFeed / 60.0) * self.stepsInch)
        self.clockFreq = stepsSecMax * rpi.freqMult
        self.clocksPerInch = self.stepsInch * rpi.freqMult
        self.freqDivider = int((rpi.xFrequency / self.clockFreq) - 1)
        if DBG_SETUP:
            print("stepsInch %d freqMult %d xFrequency %d" % \
                  (self.stepsInch, rpi.freqMult, rpi.xFrequency))
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
            print("\nturnAccel %3.1f" % self.accel)
        rpi = self.rpi
        self.freqDivider = 0
        if (self.accel == 0) or (self.maxFeed <= self.minFeed):
            self.dx = rpi.encPerRev
            self.dy = intRound(rpi.encPerRev * self.pitch)
            self.incr1 = 2 * self.dy
            self.incr2 = self.incr1 - 2 * self.dx
            self.initlSum = self.incr1 - self.dx
            self.intAccel = 0
            self.accelClks = 0
        else:
            self.maxFeed = rpi.rpm * self.pitch
            self.clocksPerInch = intRound(rpi.encPerRev * self.pitch)
            self.clockFreq = intRound((rpi.rpm * rpi.encPerRev) / 60.0)
            self.accelSetup()

    def bitSize(self, val):
        bits = 0
        while bits < 32:
            if val == 0:
                break
            val >>= 1
            bits += 1
        return(bits)

    def accelSetup(self):
        if DBG_SETUP:
            print("accel %0.2f minFeed %0.2f feedRate %0.2f ipm" % \
                  (self.accel, self.minFeed, self.maxFeed))
            print("clocksPerInch %d clockFreq %d stepsInch %d" % \
                  (self.clocksPerInch, self.clockFreq, self.stepsInch))

        stepsSecMax = intRound((self.maxFeed * self.stepsInch) / 60.0)
        stepsSecMin = intRound((self.minFeed * self.stepsInch) / 60.0)
        if DBG_SETUP:
            print("stepsSecMin %d stepsSecMax %d" % (stepsSecMin, stepsSecMax))

        stepsSec2 = float(self.accel) * self.stepsInch
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
        dyMaxBase = self.stepsInch
        dyMinBase = intRound((self.stepsInch * self.minFeed) / self.maxFeed)
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
        self.turnAccel = Accel(rpi)
        self.taperAccel = Accel(rpi)
        self.moveAccel = Accel(rpi)
        self.jogAccel = Accel(rpi)
        self.jogSlowAccel = Accel(rpi)
        self.dir = ct.DIR_POS
        self.dist = 0
        self.cmd = 0
        self.axisCtl = 0
        self.wait = False
        self.done = False
        self.wait = False
        self.loc = 0
        self.slvAxis = None
        
    def init(self):
        rpi = self.rpi
        if self.axis == Z_AXIS:
            self.name = 'z'
            self.base = base = rg.F_ZAxis_Base
            stepsInch = intRound((rpi.zMicro * rpi.zMotor) / rpi.zPitch)
            self.stepsInch = stepsInch
            self.turnAccel.update("zT", base, stepsInch)
            self.taperAccel.update("zP", base, stepsInch)
            self.moveAccel.update("zM", base, stepsInch, rpi.zMoveMin, \
                                  rpi.zMoveMax, rpi.zAccel)
            self.jogAccel.update("zJ", base, stepsInch, rpi.zJogMin, \
                                 rpi.zJogMax, rpi.zAccel)
            self.jogSlowAccel.update("zJS", base, stepsInch, rpi.zJogMin, \
                                     rpi.zJogMax, rpi.zAccel)
            self.backlashSteps = intRound(rpi.zBacklash * stepsInch)
            if rpi.zDirFlag:
                rpi.cfgCtl |= bt.cfgZDir
            else:
                rpi.cfgCtl &= ~bt.cfgZDir
            self.clkSel = \
                (bt.zClkNone, bt.zClkZFreq, bt.zClkCh, bt.zClkIntClk, \
                 bt.zClkXStep, bt.zClkXFreq, bt.zClkSpare, bt.zClkDbgFreq)
        else:
            self.name = 'x'
            self.base = base = rg.F_XAxis_Base
            stepsInch = intRound((rpi.xMicro * rpi.xMotor) / rpi.xPitch)
            self.stepsInch = stepsInch
            self.turnAccel.update("xT", base, stepsInch)
            self.taperAccel.update("xP", base, stepsInch)
            self.moveAccel.update("xM", base, stepsInch, rpi.xMoveMin, \
                                  rpi.xMoveMax, rpi.xAccel)
            self.jogAccel.update("xJ", base, stepsInch, rpi.xJogMin, \
                                 rpi.xJogMax, rpi.xAccel)
            self.jogSlowAccel.update("xJS", base, stepsInch, rpi.xJogMin, \
                                     rpi.xJogMax, rpi.xAccel)
            self.backlashSteps = intRound(rpi.xBacklash * stepsInch)
            if rpi.xDirFlag:
                rpi.cfgCtl |= bt.cfgXDir
            else:
                rpi.cfgCtl &= ~bt.cfgXDir
            self.clkSel = \
                (bt.xClkNone, bt.xClkXFreq, bt.xClkCh, bt.xClkIntClk, \
                 bt.xClkZStep, bt.xClkZFreq, bt.xClkSpare, bt.xClkDbgFreq)

    def loadClock(self, clkCtl):
        ld(rg.F_Ld_Clk_Ctl, clkCtl, 1);

    def move(self, pos, cmd):
        if self.state != en.AXIS_IDLE:
            return
        self.loc = rd(self.base + rg.F_Loc_Base + rg.F_Rd_Loc)
        self.expLoc = pos
        self.moveRel(pos - self.loc, cmd)

    def moveRel(self, dist, cmd):
        if self.state != en.AXIS_IDLE:
            return
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
                self.moveAccel.load(self.axisCtl, self.backlashSteps)
                self.state = en.AXIS_WAIT_BACKLASH
            else:
                self.state = en.AXIS_START_MOVE
                self.control()
        
    def control(self):
        if self.state != self.lastState:
            self.lastState = self.state
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
            self.loadClock(self.clkSel[bt.clkCh])
            self.turnAccel.load(self.axisCtl, self.dist)
        elif cmd == ct.CMD_JOG:
            self.loadClock(self.clkSel[bt.clkFreq])
            self.moveAccel.load(self.axisCtl, self.dist)
        elif cmd == ct.CMD_MAX or cmd == ct.CMD_MOV:
            self.loadClock(self.clkSel[bt.clkFreq])
            self.moveAccel.load(self.axisCtl, self.dist)
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
        self.loc = rd(self.base + rg.F_Loc_Base + rg.F_Rd_Loc)
        if self.loc != self.expLoc:
            pass
        self.state = en.AXIS_IDLE
