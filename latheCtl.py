#!/cygdrive/c/Python27/Python.exe

import sys
from math import ceil, floor, log
from sys import stdout
from time import sleep, time

import serial

import comm
import lathe
from comm import (command, dspXReg, getParm, getXReg, openSerial, setParm,
                  setXReg)
from interfaceX import (cmdList, parmList, regList, stateList, xilinxBitList,
                        xilinxList)
from lathe import T_ACCEL, taperCalc, tmp, xTaperInit, zTaperInit
from setup import *
from setup import (createCommands, createCtlBits, createCtlStates,
                   createParameters, createXilinxBits, createXilinxReg)

fData = False
# jLoc = '../../Java/Lathe/src/lathe/'
cLoc = '../LatheX/include/'
xLoc = '../../Xilinx/LatheCtl/'


createCommands(cmdList, cLoc, fData)
createParameters(parmList, cLoc, fData)
createCtlStates(stateList, cLoc, fData)
createCtlBits(regList, cLoc, fData)
createXilinxReg(xilinxList, cLoc, xLoc, fData)
createXilinxBits(xilinxBitList, cLoc, xLoc, fData)

# zTA = T_ACCEL()
# zPA = T_ACCEL()
# taperCalc(zTA, zPA, 0.15)
# xTaperInit(zTA, 1)
# zTaperInit(zTA, 1)
# print tmp(125)
# print 'test'

openSerial('com7', 57600)

comm.cmds = cmds
comm.parms = parms
comm.xRegs = xRegs

def bitSize(val):
    return(int(ceil(log(abs(val), 2))))

class Axis():
    def __init__(self, cFreq=50000000, mult=16):
        self.cFreq = cFreq      # clock frequency
        self.mult = mult        # freq gen multiplier
        self.axis = None        # axis name
        self.pitch = 0.0        # axis leadscrew pitch
        self.ratio = 0.0        # motor leadscrew ratio
        self.microSteps = 0     # micro steps
        self.motorSteps = 0     # motor steps
        self.accel = 0.0        # acceleration
        self.backlash = 0.0     # backlash
        self.stepsInch = 0      # axis steps per inch
        self.backlashSteps = 0  # backlash steps
    
    def setup(self):
        self.stepsInch = int((self.microSteps * self.motorSteps * self.ratio) /
                             axis.pitch)
        self.backlashSteps = int(axis.backlash * axis.stepsInch)

    def setAxis(self, axis):
        self.axis = axis

    def testInit(self):
        self.pitch = 0.1
        self.ratio = 1
        self.microSteps = 8
        self.motorSteps = 200
        self.accel = 0.75
        self.backlash = 0.023

class Move():
    def __init__(self, axis, prt=False):
        self.prt = prt
        self.axis = axis        # axis
        self.minFeed = 0        # min feed ipm
        self.maxFeed = 0        # max feed ipm

        self.freqDivider = 0    # frequency divider

    def setup(self, accel, minFeed, maxFeed):
        self.minFeed = minFeed
        self.maxFeed = maxFeed

        stepsSecMax = int((self.maxFeed / 60.0) * self.axis.stepsInch)
        stepsSecMin = int((self.minFeed / 60.0) * self.axis.stepsInch)

        freqGenMax = int(stepsSecMax) * self.axis.mult # freq gen min
        self.freqDivider = (int(floor(float(self.axis.cFreq) / freqGenMax))
                            - 1)   # calc divider
        if self.prt:
            print ("freqGenMax %d freqDivider %d" %
                   (freqGenMax, self.freqDivider))

        if self.prt:
            print("accel %0.2f minFeed %0.1f maxFeed %0.2f" %
                  (axis.accel, minFeed, maxFeed))

        if self.prt:
            print ("stepsSecMin %d stepsSecMax %d" %
                   (stepsSecMin, stepsSecMax))
        stepsSec2 = self.axis.accel * self.axis.stepsInch
        accel.accelTime = float(stepsSecMax - stepsSecMin) / stepsSec2
        accelClocks = int(accel.accelTime * freqGenMax)
        if self.prt:
            print ("stepsSec2 %d accelTime %0.6f accelClocks %d" %
                   (stepsSec2, accel.accelTime, accelClocks))

        accelMinStep = (float(stepsSecMin) / stepsSec2 * stepsSecMin) / 2.0
        accelMaxStep = (float(stepsSecMax) / stepsSec2 * stepsSecMax) / 2.0
        accel.accelSteps = accelMaxStep - accelMinStep
        if self.prt:
            print ("accelSteps %d accelMinStep %d accelMaxStep %d" %
                   (accel.accelSteps, accelMinStep, accelMaxStep))

        accel.axis = self.axis
        accel.freqDivider = self.freqDivider

        accel.dxBase = self.axis.stepsInch * self.axis.mult
        accel.dyMaxBase = self.axis.stepsInch
        accel.dyMinBase = int((self.axis.stepsInch * self.minFeed) /
                              maxFeed)

        accel.setup(accelClocks)

class Turn():
    def __init__(self, axis, minFeed, encoder, prt=False):
        self.prt = prt
        self.axis = axis        # axis
        self.minFeed = minFeed  # minimum feed for accel
        self.encoder = encoder  # encoder pulses per rev
        self.feedRate = 0       # feed ipm

        self.spindleRPM = 0     # spindle rpm
        self.encPerSec = 0      # encoder pulses per second

        self.pitch = 0          # turn pitch
        self.encPerInch = 0     # encoder pulses per inch

    def setup(self, accel, spindleRPM, pitch):
        self.spindleRPM = spindleRPM
        if pitch >= 4:
            self.pitch = 1.0 / pitchxo
        elif pitch >= 0.3:
            self.pitch = pitch / 25.4
        else:
            self.pitch = pitch
        if self.prt:
            print "tpi %0.2f pitch %0.3f" % (1.0 / pitch, pitch)
            print "minFeed %0.2f spindleRPM %d" % (self.minFeed, spindleRPM)

        self.encPerSec = int((spindleRPM * self.encoder) / 60.0) # cnts per sec
        self.encPerInch = int(self.encoder / pitch) # enc pulse inch
        if self.prt:
            print ("encPerSec %d encoderPerIn %d stepsInch %d" %
                   (self.encPerSec, self.encPerInch, self.axis.stepsInch))

        self.feedRate = feedRate = spindleRPM * pitch # feed rate inch per min
        if self.prt:
            print ("accel %0.2f minFeed %0.2f feedRate %0.2f ipm" % 
                   (self.axis.accel, self.minFeed, self.feedRate))

        if self.feedRate < self.minFeed:
            accel.dx = int(self.encPerInch)
            accel.dyMax = accel.dyIni = int(self.axis.stepsInch)
            accel.accelClocks = 0
            accel.intIncPerClock = 0
        else:
            stepsSecMax = int((feedRate * self.axis.stepsInch) / 60.0)
            stepsSecMin = int((self.minFeed  * self.axis.stepsInch) / 60.0)
            if self.prt:
                print ("stepsSecMin %d stepsSecMax %d" %
                       (stepsSecMin, stepsSecMax))

            stepsSec2 = self.axis.accel * self.axis.stepsInch
            accel.accelTime = float(stepsSecMax - stepsSecMin) / stepsSec2
            accelClocks = int(self.encPerSec * accel.accelTime)
            if self.prt:
                print ("stepsSec2 %0.0f accelTime %8.6f accelClocks %d" %
                       (stepsSec2, accel.accelTime, accelClocks))

            accelMinStep = ((float(stepsSecMin) / stepsSec2) *
                                stepsSecMin) / 2.0
            accelMaxStep = ((float(stepsSecMax) / stepsSec2) *
                                stepsSecMax) / 2.0
            accel.accelSteps = accelMaxStep - accelMinStep
            if self.prt:
                print ("accelSteps %d accelMinStep %d accelMaxStep %d" %
                       (accel.accelSteps, accelMinStep, accelMaxStep))

            accel.axis = self.axis
            accel.encoder = self.encoder

            accel.dxBase = int(self.encPerInch)
            accel.dyMaxBase = self.axis.stepsInch
            accel.dyMinBase = int((self.axis.stepsInch * self.minFeed) /
                                  feedRate)

            accel.setup(accelClocks)

class Taper():
    def __init__(self, turn, axis, prt=False):
        self.prt = prt
        self.turn = turn        # turn parameters
        self.axis = axis        # taper axis

        self.taper = 0          # taper distance
        self.dist = 0           # turn distance
        self.dx = 0             # turn steps
        self.dy = 0             # taper steps

        self.incr1 = 0          # add if negative
        self.incr2 = 0          # add if ge zero
        self.sum = 0            # initial sum

    def setup(self, taper, dist=1.0):
        self.taper = taper
        self.dist = dist
        turn = self.turn
        self.dx = dx = turn.axis.stepsInch * dist
        self.dy = dy = int(taper * self.axis.stepsInch * dist)

        self.incr1 = 2 * dy
        self.incr2 = self.incr1 - 2 * dx
        self.sum = self.incr1 - dx
        if self.prt:
            print ("dx %d dy %d" % (dx, dy))
            print ("incr1 %d incr2 %d sum %d bits %d" %
                   (self.incr1, self.incr2, self.sum, bitSize(incr2)))

class Accel():
    def __init__(self, prt=False):
        self.prt = prt

        self.encoder = 0        # encoder count

        self.accelTime = 0      # acceleration time
        self.accelSteps = 0     # acceleration steps

        self.scale = 0          # scale factor
        self.dx = 0             # dx value
        self.dyIni = 0          # initial dy
        self.dyMax = 0          # maximum dy
        self.intIncPerClock = 0 # increment per clock

        self.incr1 = 0          # add if negative
        self.incr2 = 0          # add if positive
        self.sum = 0            # initial sum
        self.accel = 0          # inc per clock
        self.accelClocks = 0    # acceleration clocks

        self.dxBase = 0
        self.dyMaxBase = 0
        self.dyMinBase = 0

    def setup(self, accelClocks):
        dxBase = self.dxBase
        dyMaxBase = self.dyMaxBase
        dyMinBase = self.dyMinBase
        if self.prt:
            print
            print ("accelClocks %d dxBase %d dyMaxBase %d dyMinBase %d" %
                   (accelClocks, dxBase, dyMaxBase, dyMinBase))

        for scale in range(0, 12):
            self.dx = dxBase << scale
            self.dyMax = dyMaxBase << scale
            dyMin = dyMinBase << scale
            dyDelta = self.dyMax - dyMin
            if self.prt:
                print ("\nscale %d dx %d dyMin %d dyMax %d dyDelta %d" %
                        (scale, self.dx, dyMin, self.dyMax, dyDelta))
            incPerClock = float(dyDelta) / accelClocks
            intIncPerClock = int(incPerClock)
            if intIncPerClock == 0:
                continue
            self.intIncPerClock = intIncPerClock
            dyDeltaC = intIncPerClock * accelClocks
            err = int(abs(dyDelta - dyDeltaC)) >> scale
            self.dyIni = self.dyMax - intIncPerClock * accelClocks
            if self.prt:
                print("dyIni %d dyMax %d intIncPerClock %d accelClocks %d" %
                      (self.dyIni, self.dyMax, intIncPerClock,
                       accelClocks))
            bits = bitSize(self.dx) + 1
            if self.prt:
                print ("dyIni %d dyMax %d dyDelta %d incPerClock %0.3f "\
                        "err %d bits %d" %
                        (self.dyIni, self.dyMax, dyDelta, incPerClock,\
                         err, bits))

            if (bits >= 30) or (err == 0):
                break
        self.scale = scale

        self.incr1 = incr1 = 2 * self.dyIni
        incr1Max = 2 * self.dyMax
        self.incr2 = incr2 = incr1 - 2 * self.dx
        incr2Max = incr1Max - 2 * self.dx
        self.sum = incr1 - self.dx
        if self.prt:
            print ("\nincr1Ini %d incr1Max %d incr2Ini %d incr2Max %d " %
                   (incr1, incr1Max, incr2, incr2Max))

        if self.intIncPerClock != 0:
            self.accel = 2 * self.intIncPerClock

            totalSum = (accelClocks * incr1) + self.sum
            totalInc = (accelClocks * (accelClocks - 1) * 
                        self.accel) / 2
            self.accelSteps = ((totalSum + totalInc) / (2 * self.dx))

            if self.prt:
                print ("accelClocks %d totalSum %d totalInc %d "\
                        "accelSteps %d" % 
                        (accelClocks, totalSum, totalInc, \
                        self.accelSteps))
        else:
            self.accelSteps = 0
            self.accelClocks = 0
            self.accel = 0

    def test(self):
        # lastT = 0
        # encPerSec = self.encPerSec
        accelClocks = self.accelClocks
        accel = self.accel
        incr1 = self.incr1
        incr2 = self.incr2
        sum = self.sum
        print ("\nincr1 %d incr2 %d sum %d inc %d accel %d" %
               (incr1, incr2, sum, self.intIncPerClock, accel))
    
        f = open("turnAccel.txt", "w")
        x = 0
        y = 0
        clocks = 0
        incAccum = 0
        while clocks < (accelClocks * 1.2):
            f.write("x %6d y %5d sum %12d incAccum %12d incr1 %8d "\
                    "incr2 %11d\n" %
                    (x, y, sum, incAccum, incr1 + incAccum, incr2 + incAccum))
            clocks += 1
            x += 1
            if sum < 0:
                sum += incr1
            else:
                y += 1
                sum += incr2
                # curT = clocks / encPerSec
                # deltaT = curT - lastT
                # if pData:
                #     if lastT != 0:
                #         time.append(curT);
                #         data.append(1.0 / deltaT)
                # lastT = curT
            sum += incAccum
            if clocks <= accelClocks:
                incAccum += accel

        print ("incr1 %d incr2 %d sum %d" %
               (incr1 + incAccum, incr2 + incAccum, sum))

        incr1 = 2 * self.dyMax
        incr2 = incr1 - 2 * self.dx
        print ("incr1 %d incr2 %d" %
               (incr1, incr2))

        stdout.flush()
        f.close()

class AccelPlot(Accel):
    def __init__(self, dbgPrint=False):
        Accel.__init__(self, dbgPrint)
        self.dbgPrint = dbgPrint
        self.clockInterval = 0

    def plot(self, runClocks, dist, file="", pData=False):
        if pData:
            from pylab import plot, grid, show
            from array import array
            time = array('f')
            data = array('f')
            time.append(0)
            data.append(0)
            lastT = 0

        f = None
        if len(file) != 0:
            f = open(file, 'w')
        incr1 = self.incr1
        incr2 = self.incr2
        sum = self.sum
        dist = abs(dist)
        distCtr = abs(self)
        if distCtr > 1:
            synAccel = self.accel
            accelClocks = self.accelClocks
            accel = True
        else:
            synAccel = 0
            accelClocks = 0
            accel = False

        print ("synAccel %d accelClocks %d accelSum %d" %
               (synAccel, accelClocks, synAccel * accelClocks))
        print ("incr1 %d incr2 %d sum %d" % (incr1, incr2, sum))

        aClk = accelClocks
        aclSteps = 0
        accelAccum = 0
        accelAccum0 = 0
        decel = False
        x = 0
        y = 0
        lastC = 0
        clocks = 0
        while (x < runClocks):
            if not decel:
                if aclSteps >= distCtr:
                    accel = False
                    decel = True
                    aClk = accelClocks
            if decel:
                if accelAccum > 0:
                    aClk -= 1
                    accelAccum -= synAccel
            x += 1
            if sum < 0:
                sum += incr1
            else:
                deltaC = clocks - lastC
                if f != None:
                    f.write(("x %6d y %5d deltaC %5d sum %12d incAccum %12d " +
                             "incr1 %8d incr2 %11d\n") % \
                            (x, y, deltaC, sum, incAccum, 
                             incr1 + incAccum, incr2 + incAccum))
                y += 1
                sum += incr2
                distCtr -= 1
                lastC = clocks
                if pData:
                    curT = clocks * clockInterval
                    deltaT = curT - lastT
                    if lastT != 0:
                        time.append(curT);
                        data.append(1.0 / deltaT)
                        lastT = curT
            sum += accelAccum0
            if distCtr == 0:
                break
            if accel:
                aclSteps = y
                # if x <= accelClocks:
                if aClk > 0:
                    aClk -= 1
                    accelAccum += synAccel
                else:
                    accel = False
            accelAccum0 = accelAccum
            clocks += 1
        if f != None:
            f.close()

        print ("y %d incr1 %d incr2 %d sum %d incAccum %d" %
               (y, incr1 + incAccum, incr2 + incAccum, sum, incAccum))

        if pData:
            stdout.flush()
            plot(time, data, 'b', aa="true")
            grid(True)
            show()

class Test(Accel):
    def __init__(self, testAxis='z', dbgClock=True, dbgPrint=False):
        Accel.__init__(self, dbgPrint)
        self.dbgPrint = dbgPrint
        self.dbgClock = dbgClock
        self.testAxis = testAxis
        self.runClocks = 0
        self.encoder = 0
        self.rpm = 0

        self.axis = None        # axis for accleration
        self.freqDivider = 0    # frequency divider

        self.dist = 0           # test distance
        self.loc = 0            # start location

    def setDbgPrint(self, val):
        self.dbgPrint = val
        comm.xDbgPrint = val

    def setRPM(self, rpm):
        self.rpm = rpm

    def setEncoder(self, encoder):
        self.encoder = encoder

    def setWaitSync(self, waitSync):
        self.waitSync = waitSync

    def testNoAccelSetup(self, dx, dy):
        self.dx = dx
        self.dy = dy

        self.incr1 = (2 * dy)
        self.incr2 = (2 * (dy - dx))
        self.sum = (self.incr1 - dx)

        print "dx %d dy %d" % (dx, dy)
        print ("incr1 %d incr2 %d sum %d" %
               (self.incr1, self.incr2, self.sum))
        print

        self.accel = 0
        self.accelClocks = 0

    def zTestSync(self, runClocks, dist=100, loc=20):
        if dist == 0:
            dist = 100
        if loc == 0:
            loc = 20

        print ("z test sync clocks %d dist %d loc %d" %
               (runClocks, dist, loc))

        if self.dbgPrint:
            print

        self.testInit(self.encoder)
        self.zSetup(dist, loc)

        setXReg('XLDZCTL', ZRESET);
        setXReg('XLDZCTL', 0);
        flag = ZDIR_POS
        if dist < 0:
            flag = ZDIR_NEG
        setXReg('XLDZCTL', ZSRC_SYN | flag)
        if self.waitSync:
            flag |= ZWAIT_SYNC
        setXReg('XLDZCTL', ZSTART | ZSRC_SYN | flag)

        self.testStart(runClocks)
        self.testWait(runClocks, 0.5)
        self.readPhase()
        if self.accel == 0:
            self.zTestCheck(None)
        else:
            self.zTestAccelCheck(None)

    def xTestSync(self, runClocks, dist=100, loc=20):
        if dist == 0:
            dist = 100
        if loc == 0:
            loc = 20

        print ("x sync test clocks %d dist %d loc %d" %
               (runClocks, dist, loc))

        if self.dbgPrint:
            print

        self.testInit(self.encoder)
        self.xSetup(dist, loc)

        dir = ZDIR_POS
        if dist < 0:
            dir = ZDIR_NEG
        setXReg('XLDXCTL', XSRC_SYN | dir)
        setXReg('XLDXCTL', XSTART | XSRC_SYN | dir)

        self.testStart(runClocks)
        self.testWait(runClocks, 0.5)
        self.readPhase()
        if self.accel == 0:
            self.xTestCheck(None)
        else:
            self.xTestAccelCheck(None)

    def zTestXTaper(self, runClocks, dist=100, loc=20, ac=None):
        if dist == 0:
            dist = 100
        if loc == 0:
            loc = 20

        print ("z sync x taper clocks %d dist %d loc %d" %
               (runClocks, dist, loc))

        if self.dbgPrint:
            print

        self.testInit(self.encoder)

        zDir = ZDIR_POS
        if dist < 0:
            zDir = ZDIR_NEG
            dist = abs(dist)

        self.zSetup(dist, loc)
        self.xSetup(0, loc, ac)

        setXReg('XLDTCTL', TENA) # set for taper x

        setXReg('XLDZCTL', ZSRC_SYN | zDir) # set source and direction
        setXReg('XLDZCTL', ZSTART | ZSRC_SYN | zDir) # start z

        self.testStart(runClocks)
        self.testWait(runClocks, 2.0)
        self.readPhase()
        self.zTestCheck(None)
        self.xTestCheck(ac)

    def xTestZTaper(self, runClocks, dist=100, loc=20, ac=None):
        if dist == 0:
            dist = 100
        if loc == 0:
            loc = 20

        print ("x sync z taper clocks %d dist %d loc %d" %
               (runClocks, dist, loc))

        if self.dbgPrint:
            print

        self.testInit(self.encoder)

        xDir = XDIR_POS
        if dist < 0:
            xDir = XDIR_NEG
            dist = abs(dist)

        self.xSetup(dist, loc)
        self.zSetup(0, loc, ac)

        setXReg('XLDTCTL', TENA | TZ) # set for taper z

        setXReg('XLDXCTL', XSRC_SYN | xDir) # set source and direction
        setXReg('XLDXCTL', XSTART | XSRC_SYN | xDir) # start x

        self.testStart(runClocks)
        self.testWait(runClocks, 2.0)
        self.readPhase()
        self.xTestCheck(None)
        self.zTestCheck(ac)

    def zTestMove(self, runClocks, dist=100, loc=20):
        if dist == 0:
            dist = 100
        if loc == 0:
            loc = 20

        print ("z move clocks %d dist %d loc %d" %
               (runClocks, dist, loc))

        if self.dbgPrint:
            print

        self.resetAll()
        dspXReg('XRDZXPOS')
        self.testMoveInit()

        zDir = ZDIR_POS
        if dist < 0:
            zDir = ZDIR_NEG
            dist = abs(dist)

        self.zSetup(dist, loc)

        setXReg('XLDZCTL',ZRESET )   # reset z
        setXReg('XLDZCTL', zDir)     # clear reset set direction
        # dspXReg('XRDZXPOS')
        setXReg('XLDZCTL', (ZSTART | # start
                            zDir))   # and direction
        # dspXReg('XRDZXPOS')

        self.testMoveStart(runClocks, self.freqDivider)

        self.testWait(runClocks, 2.0)
        self.zTestAccelCheck(None)

    def xTestMove(self, runClocks, dist=100, loc=20):
        if dist == 0:
            dist = 100
        if loc == 0:
            loc = 20

        print ("x move clocks %d dist %d loc %d" %
               (runClocks, dist, loc))

        if self.dbgPrint:
            print

        self.resetAll()
        self.testMoveInit()

        xDir = XDIR_POS
        if dist < 0:
            xDir = XDIR_NEG
            dist = abs(dist)

        self.xSetup(dist, loc)

        setXReg('XLDXCTL', xDir) # set direction
        setXReg('XLDXCTL', (XSTART | # start
                            xDir))    # and direction

        self.testMoveStart(runClocks, self.freqDivider)

        self.testWait(runClocks, 2.0)
        self.xTestAccelCheck(None)

    def resetAll(self):
        setXReg('XLDZCTL', ZRESET) # reset z
        setXReg('XLDZCTL', 0)      # clear z mode
        setXReg('XLDXCTL', XRESET) # reset x
        setXReg('XLDXCTL', 0)      # clear x mode
        setXReg('XLDTCTL', 0)      # clear taper
        setXReg('XLDDCTL', 0)      # disable debug mode
        setXReg('XLDCFG', 0)       # reset config
        command('CLRDBG')          # clear debug buffer
        # command('CMD_CLEAR')       # clear control variables

    def extClockInit(self, encoder):
        global fcy
        setXReg('XLDCFG', ENC_POL) # change polarity of direction signal
        command('ENCSTOP')
        if self.encoder != 0:
            preScaler = 1
            if self.rpm == 0:
                self.rpm = 1
            rps = self.rpm / 60.0
            encTimer = int(fcy / (encoder * rps))
            while encTimer >= 65536:
                preScaler += 1
                encTimer = int(fcy / (encoder * rps * preScaler))
            print "preScaler %d encTimer %d" % (preScaler, encTimer)
            setParm('ENC_PRE_SCALER', preScaler)
            setParm('ENC_TIMER', encTimer)
            setParm('ENC_MAX', encoder)

    def extClockStart(self, runClocks):
        self.runClocks = runClocks
        setParm('ENC_RUN_COUNT', runClocks)
        command('ENCSTART')
        self.readFreq()

    def testInit(self, encoder, dbgFreq=10000, dbgCount=4):
        self.resetAll()
        if self.dbgClock:
            setXReg('XLDDCTL', DBG_SEL) # select debug encoder

            setXReg('XLDTFREQ', dbgFreq - 1) # load test frequency
        else:
            self.extClockInit(encoder)

        setXReg('XLDPHASE', encoder-1) # load phase count
        setXReg('XLDDREG', 0x1234) # load display register

    def testMoveInit(self):
        if self.dbgClock:
            setXReg('XLDDCTL', DBG_INIT) # initialize debug
            setXReg('XLDDCTL', 0)        # initialize debug
            setXReg('XLDDCTL', DBG_MOVE) # clear init and set move
        else:
            if self.testAxis == 'z':
                pass
            elif self.testAxis == 'x':
                pass

    def testMoveStart(self, runClocks, dbgFreq):
        setXReg('XLDTFREQ', dbgFreq) # load test frequency
        if runClocks != 0:
            if self.dbgClock:
                setXReg('XLDTCOUNT', runClocks-1) # load test count 
                setXReg('XLDDCTL', DBG_MOVE) # select debug frequency clock
                setXReg('XLDDCTL', (DBG_INIT | # initialize dbg
                                    DBG_MOVE)) # keep debug clock selected
                setXReg('XLDDCTL', (DBG_ENA |  # enable debugging
                                    DBG_COUNT | # run for number in count
                                    DBG_MOVE)) # keep debug clock selected
        if not self.dbgClock:
            if self.testAxis == 'z':
                pass
            elif self.testAxis == 'x':
                pass

    def testStart(self, runClocks):
        if runClocks != 0:
            if self.dbgClock:
                setXReg('XLDTCOUNT', runClocks-1) # load test count 

                setXReg('XLDDCTL', (DBG_SEL |  # select dbg encoder
                                    DBG_INIT)) # initialize dbg and z modules
                setXReg('XLDDCTL', DBG_SEL)    # select dbg encoder

                setXReg('XLDDCTL', (DBG_ENA |   # enable debugging
                                    DBG_SEL |   # select dbg encoder
                                    DBG_COUNT | # run for number in count
                                    DBG_RSYN |  # enable sync
                                    DBG_MOVE))  # debug axis move
        if not self.dbgClock:
            self.extClockStart(runClocks)

    def zSetup(self, dist, loc, ac=None):
        if ac == None:
            ac = self
        self.dist = dist
        self.loc = loc
        setXReg('XLDZD', ac.sum)       # load d value
        setXReg('XLDZINCR1', ac.incr1) # load incr1 value
        setXReg('XLDZINCR2', ac.incr2) # load incr2 value

        if dist > 1:
            setXReg('XLDZACCEL', ac.accel)        # load z accel
            if ac.accelClocks > 0:
                setXReg('XLDZACLCNT', ac.accelClocks - 1) # load z accel count
            else:
                setXReg('XLDZACLCNT', 0) # load z accel count
        else:
            setXReg('XLDZACCEL', 0)  # load z accel
            setXReg('XLDZACLCNT', 0) # load z accel count

        setXReg('XLDZDIST', abs(dist)) # load z distance
        setXReg('XLDZLOC', loc)   # set location

        setXReg('XLDZCTL', ZRESET | ZSET_LOC) # reset z and load location
        setXReg('XLDZCTL', 0)    # clear reset

    def xSetup(self, dist, loc, ac=None):
        if ac == None:
            ac = self
        self.dist = dist
        self.loc = loc
        setXReg('XLDXD', ac.sum)       # load d value
        setXReg('XLDXINCR1', ac.incr1) # load incr1 value
        setXReg('XLDXINCR2', ac.incr2) # load incr2 value

        setXReg('XLDXACCEL', ac.accel)        # load x accel
        setXReg('XLDXACLCNT', ac.accelClocks - 1) # load x accel count

        setXReg('XLDXDIST', abs(dist)) # load x distance
        setXReg('XLDXLOC', loc)        # set location

        setXReg('XLDXCTL', XRESET | XSET_LOC) # reset x and load location
        setXReg('XLDXCTL', 0)                 # clear reset

    def testWait(self, runClocks, interval=0.5):
        tmp = comm.xDbgPrint
        if runClocks != 0 or not self.dbgClock:
            comm.xDbgPrint = False
            start = time()
            if self.dbgClock:
                while True:
                    val = dspXReg('XRDSR')
                    # print val
                    if (val & (S_DBG_DONE | S_Z_DONE_INT | S_X_DONE_INT)) != 0:
                        break
                    if (val & (S_Z_START | S_X_START)) == 0:
                        print "no start %x " % (val)
                        break
            else:
                while True:
                    val = dspXReg('XRDSR')
                    # print val
                    if (val & (S_Z_DONE_INT | S_X_DONE_INT)) != 0:
                        print "done %x" % (val)
                        break
                    if (val & (S_Z_START | S_X_START)) == 0:
                        print "no start %x" % (val)
                        break
                    encRun = getParm('ENC_RUN')
                    if encRun == 0:
                        print "encoder stop"
                        break
            delta = time() - start
        else:
            delta = 0
            val = 0

        if val & S_Z_DONE_INT:
            setXReg('XLDZCTL', 0) # clear z done flag
        if val & S_X_DONE_INT:
            setXReg('XLDXCTL', 0) # clear x done flag

        # comm.xDbgPrint = True
        zVal = getXReg('XRDZXPOS')
        xVal = getXReg('XRDXXPOS')
        # comm.xDbgPrint = False
        maxClocks = max(zVal, xVal)

        comm.xDbgPrint = tmp

        # if maxClocks & (1 << 23):
        #     maxClocks = -((maxClocks ^ 0xffffff) + 1)
        if self.dbgPrint:
            print 
        val = dspXReg('XRDSR')
        print ("results %d %d clocks sr 0x%2x %4.2f sec\n" % 
               (runClocks, maxClocks, val, delta))

    def readFreq(self):
        setXReg('XCLRFREQ', 0)
        freq = 0
        count = 20
        while freq == 0:
            freq = dspXReg('XRDFREQ', "freq")
            count -= 1
            if count <= 0:
                break
        if freq != 0:
            freq = int((600.0 * freq) / self.encoder)
            print "freq %d" % (freq)

    def readPhase(self):
        dspXReg('XREADREG', "freq")

        tmp = comm.xDbgPrint
        comm.xDbgPrint = True
        dspXReg('XRDPSYN', "phase syn")
        dspXReg('XRDTPHS', "tot phase")
        comm.xDbgPrint = tmp

    def zTestCheck(self, ac=None):
        if self.dbgPrint:
            print
        xPos = dspXReg('XRDZXPOS', "z xpos")
        yPos = dspXReg('XRDZYPOS', "z ypos")
        zSum = dspXReg('XRDZSUM', "z sum")

        dspXReg('XRDZDIST', "z dist")
        dspXReg('XRDZLOC', "z loc")
        dspXReg('XRDSTATE', "state")

        if self.dbgPrint:
            print
        self.testCheck(xPos, yPos, zSum, ac)

    def xTestCheck(self, ac=None):
        if self.dbgPrint:
            print
        xPos = dspXReg('XRDXXPOS', "x xpos")
        yPos = dspXReg('XRDXYPOS', "x ypos")
        xSum = dspXReg('XRDXSUM', "x sum")

        dspXReg('XRDXDIST', "x dist")
        dspXReg('XRDXLOC', "x loc")
        dspXReg('XRDSTATE', "state")

        if self.dbgPrint:
            print
        self.testCheck(xPos, yPos, xSum, ac)

    def testCheck(self, xPos, yPos, testSum, ac=None):
        if xPos & (1 << 23):
            xPos = -((xPos ^ 0xffffff) + 1)
        if yPos & (1 << 23):
            yPos = -((yPos ^ 0xffffff) + 1)
        if ac == None:
            ac = self
        incr1 = ac.incr1
        incr2 = ac.incr2

        clocks = 0
        x = 0
        y = 0
        sum = ac.sum
        while (clocks < xPos):
            clocks += 1
            x += 1
            if sum < 0:
                sum += incr1
            else:
                y += 1
                sum += incr2

        print ("x %d y %d yPos %d sum %d testSum %d" %
               (x, y, yPos, sum, testSum))

    def zTestAccelCheck(self, ac=None):
        xPos = dspXReg('XRDZXPOS', "xpos")
        yPos = dspXReg('XRDZYPOS', "ypos")
        zSum = dspXReg('XRDZSUM', "sum")
        zAclSum = dspXReg('XRDZACLSUM', "aclsum")

        dspXReg('XRDZDIST', "dist")
        dspXReg('XRDZASTP', "a steps")
        dspXReg('XRDZLOC', "loc")
        dspXReg('XRDSTATE', "state")

        if self.dbgPrint:
            print
        self.testAccelCheck(xPos, yPos, zSum, zAclSum)

    def xTestAccelCheck(self, ac=None):
        xPos = dspXReg('XRDXXPOS', "xpos")
        yPos = dspXReg('XRDXYPOS', "ypos")
        xSum = dspXReg('XRDXSUM', "sum")
        xAclSum = dspXReg('XRDXACLSUM', "aclsum")

        dspXReg('XRDXDIST', "dist")
        dspXReg('XRDXASTP', "a steps")
        dspXReg('XRDXLOC', "loc")
        dspXReg('XRDSTATE', "state")

        if self.dbgPrint:
            print
        self.testAccelCheck(xPos, yPos, xSum, xAclSum)

    def testAccelCheck(self, xPos, yPos, xSum, aclSum):
        incr1 = self.incr1
        incr2 = self.incr2
        sum = self.sum
        distCtr = abs(self.dist)
        if distCtr > 1:
            synAccel = self.accel
            accelClocks = self.accelClocks
            accel = True
            tmp = min(xPos, accelClocks)
            print ("synAccel %d accelClocks %d accelSum %d" %
                   (synAccel, tmp, synAccel * tmp))
            print
        else:
            synAccel = 0
            accelClocks = 0
            accel = False

        x = 0
        y = 0
        aClk = accelClocks
        aclSteps = 0
        accelAccum = 0
        accelAccum0 = 0
        decel = False
        while x < xPos:
            if self.dbgPrint:
                print ("x %5d y %3d sum %10d aSum %6d dist %3d "\
                       "aclSteps %4d aClk %6d %d %d" %
                       (x, y, sum, accelAccum, distCtr, aclSteps, aClk,\
                        accel, decel))
            if not decel:
                if aclSteps >= distCtr:
                    accel = False
                    decel = True
                    aClk = accelClocks
            if decel:
                if accelAccum > 0:
                    aClk -= 1
                    accelAccum -= synAccel
            x += 1
            if sum < 0:
                sum += incr1
            else:
                y += 1
                sum += incr2
                distCtr -= 1
            sum += accelAccum0
            if distCtr == 0:
                break
            if accel:
                aclSteps = y
                # if x <= accelClocks:
                if aClk > 0:
                    aClk -= 1
                    accelAccum += synAccel
                else:
                    accel = False
            accelAccum0 = accelAccum
        if self.dbgPrint:
            print
        print "%10s %10s %12s %12s" % ("x", "y", "sum", "accelSum")
        print "%10d %10d %12d %12d calc" % (x, y, sum, accelAccum)
        print "%10s %10d %12d %12d read" % ("", yPos, xSum, aclSum)
        print "%10s %10d %12d %12d diff" % ("", y - yPos, sum - xSum,\
                                            accelAccum - aclSum)

# z synchronized move with acceleration

def test4(runClocks=0, tpi=0, dist=20, dbgprint=True, pData=False):
    print runClocks, tpi
    if (tpi == 0):
        return
    if (tpi < 1):
        tpi = 1.0 / tpi
    if (runClocks == 0):
        runClocks = 1
    f = open('accel.txt', 'w')

    if pData:
        from pylab import plot, grid, show
        from array import array
        time = array('f')
        data = array('f')
        time.append(0)
        data.append(0)

    stepsRev = 1600             # steps per revolution
    lsPitch = .1                # leadscrew pitch
    spindleRPM = 300            # spindle speed
    encoder = 20320             # encoder counts
    threadPerIn = tpi           # threads per inch
    minFeed = 2.0               # minimum speed
    accelRate = 0.75            # acceleration inch per sec^2
    scale = 8

    print "tpi %5.2f pitch %5.3f" % (tpi, 1.0 / tpi)

    zFeedRate = spindleRPM / threadPerIn # z feed rate inch per min
    print "zFeedRate %6.2f ipm" % (zFeedRate)

    spindleRPS = spindleRPM / 60.0 # spindle rev per second

    encPerSec = spindleRPS * encoder # encoder counts per second
    print "encPerSec %5.0f" % (encPerSec)

    stepsPerInch = stepsRev / lsPitch # steps per inch
    encPerInch = encoder * threadPerIn # encoder pulse per inch
    print "stepsPerInch %d encoderPerIn %d" % (stepsPerInch, encPerInch)

    stepsPerThread = stepsPerInch / threadPerIn # steps per thread
    stepsPerSecond = zFeedRate * stepsPerInch / 60.0 # steps per second
    print ("stepsPerThread %5.0f stepsPerSecond %5.0f" %
           (stepsPerThread, stepsPerSecond))

    dx = int(encPerInch) << scale
    dy = int(stepsPerInch) << scale
    print ("dx %d dy %d scale %d" % (dx, dy, 1 << scale))

    accelTime = (zFeedRate - minFeed) / (60.0 * accelRate)
    accelClocks = int(encPerSec * accelTime)
    bits = int(floor(log(accelClocks, 2))) + 1
    print ("accelTime %8.6f accelClocks %4.0f bits %d" %
           (accelTime, accelClocks, bits))

    iniDy = dy /  (zFeedRate / minFeed)
    dyDelta = dy - iniDy
    incPerClock = dyDelta / accelClocks
    intIncPerClock = int(incPerClock)
    iniDy = dy - intIncPerClock * accelClocks
    print ("iniDy %d dy %d dyDelta %d incPerClock %6.2f" %
           (iniDy, dy, dyDelta, incPerClock))

    incr1 = 2 * dy
    incr2 = incr1 - 2 * dx
    sum = incr1 - dx

    bits = int(floor(log(abs(incr2), 2))) + 1
    print ("incr1 %d incr2 %d bits %d" %
           (incr1, incr2, bits))
    
    stdout.flush()

    # clocks = 0
    # lastT = 0
    # x = 0
    # y = 0
    # incr1 = 2 * iniDy
    # incr2 = incr1 - 2 * dx
    # sum = incr1 - dx
    # inc = 2 * intIncPerClock
    # print ("incr1 %d incr2 %d inc %d" % (incr1, incr2, intIncPerClock))
    # stdout.flush()
    # while (clocks < (accelClocks * 1.2)):
    #     clocks += 1
    #     x += 1
    #     if (sum < 0):
    #         sum += incr1
    #     else:
    #         y += 1
    #         sum += incr2
    #         curT = clocks / encPerSec
    #         deltaT = curT - lastT
    #         if pData:
    #             if (lastT != 0):
    #                 time.append(curT);
    #                 data.append(1.0 / deltaT)
    #         lastT = curT
    #         f.write("x %6d y %5d sum %11d incr1 %8d incr2 %11d\n" %
    #                 (x, y, sum, incr1, incr2))
    #     if (clocks <= accelClocks):
    #         incr1 += inc
    #         incr2 += inc
    # print "y %d incr1 %d incr2 %d sum %d" % (y, incr1, incr2, sum)
    # stdout.flush()

    clocks = 0
    lastT = 0
    x = 0
    y = 0
    incr1 = 2 * iniDy
    incr2 = incr1 - 2 * dx
    d = incr1 - dx
    sum = d

    zSynAccel = 2 * intIncPerClock
    zSynAclCnt = accelClocks

    totalSum = (accelClocks * incr1) + d
    totalInc = (accelClocks * (accelClocks - 1) * zSynAccel) / 2
    accelSteps = ((totalSum + totalInc) / (2 * dx)) + 1

    print ("accelClocks %d totalSum %d totalInc %d accelSteps %d" % 
           (accelClocks, totalSum, totalInc, accelSteps))

    incAccum = 0;
    print ("incr1 %d incr2 %d zSynAccel %d" % (incr1, incr2, zSynAccel))
    stdout.flush()
    while (clocks < (accelClocks * 1.2)):
        clocks += 1
        x += 1
        if (sum < 0):
            sum += incr1
        else:
            y += 1
            sum += incr2
            curT = clocks / encPerSec
            deltaT = curT - lastT
            if pData:
                if (lastT != 0):
                    time.append(curT);
                    data.append(1.0 / deltaT)
            lastT = curT
        sum += incAccum
        if (clocks <= accelClocks):
            incAccum += zSynAccel
        f.write("x %6d y %5d sum %12d incAccum %12d incr1 %8d incr2 %11d\n" %
                (x, y, sum, incAccum, incr1 + incAccum, incr2 + incAccum))
    print ("y %d incr1 %d incr2 %d sum %d" %
           (y, incr1 + incAccum, incr2 + incAccum, sum))
    print ("y %d incr1 %d incr2 %d incAccum %d" %
           (y, incr1, incr2, incAccum))
    f.close()

    # incr1 = 2 * iniDy
    # incr2 = incr1 - 2 * dx
    # d = incr1 - dx

    # encPhase = 10

    # setXReg('XLDDCTL', 0, dbgprint)    # disable debug mode
    # setXReg('XLDZCTL', ZRESET, dbgprint) # reset z
    # setXReg('XLDZCTL', 0, dbgprint)    # clear z mode
    # setXReg('XLDDCTL', 0, dbgprint)
    # setXReg('XLDZCTL', 0, dbgprint)

    # setXReg('XLDTFREQ', 10000, dbgprint)	# load test frequency
    # setXReg('XLDTCOUNT', runClocks-1, dbgprint) # load test count 

    # setXReg('XLDPHASE', encPhase - 1, dbgprint) # load phase count

    # setXReg('XLDZD', d, dbgprint)		# load d value
    # setXReg('XLDZINCR1', incr1, dbgprint)	# load incr1 value
    # setXReg('XLDZINCR2', incr2, dbgprint)	# load incr2 value

    # setXReg('XLDZACCEL', zSynAccel, dbgprint)   # load z accel
    # setXReg('XLDZACLCNT', zSynAclCnt, dbgprint) # load z accel count

    # setXReg('XLDDCTL', DBG_INIT, dbgprint) # initialize z modules
    # setXReg('XLDDCTL', 0, dbgprint)        # clear

    # setXReg('XLDZLOC', 20, dbgprint)       # set location
    # setXReg('XLDZCTL', ZSET_LOC, dbgprint) # set z location
    # setXReg('XLDZCTL', 0, dbgprint)        # clear

    # setXReg('XLDZDIST', dist, dbgprint) # load z distance
    # setXReg('XLDZCTL', ZRESET, dbgprint)  # reset z to load distance
    # setXReg('XLDZCTL', 0, dbgprint)     # clear reset

    # setXReg('XLDZCTL', (ZSRC_SYN    # sync source
    #                    | ZDIR_POS  # direction positive
    #                    | ZWAIT_SYN # wait for sync pulse
    #                ), dbgprint)

    # setXReg('XLDZCTL', (ZSTART      # start
    #                    | ZSRC_SYN  # sync source
    #                    | ZDIR_POS  # direction positive
    #                    | ZWAIT_SYN # wait for sync pulse
    #                ), dbgprint)

    # setXReg('XLDDCTL', (DBG_ENA     # enable debugging
    #                    | DBG_COUNT # run for number in count
    #                ), dbgprint)

    # sleep(.5);
    # if dbgprint:
    #     print "\nresults %d clocks \n" % (runClocks)

    # dspXReg('XRDFREQ', "freq", dbgprint)
    # dspXReg('XRDPSYN', "phase syn", dbgprint)
    # dspXReg('XRDTPHS', "tot phase", dbgprint)

    # xPos = dspXReg('XRDZXPOS', "xpos", dbgprint)
    # dspXReg('XRDZYPOS', "ypos", dbgprint)
    # zsum = dspXReg('XRDZSUM', "sum", dbgprint)
    # zAclSum = dspXReg('XRDZACLSUM', "aclsum", dbgprint)

    # dspXReg('XRDZDIST', "dist", dbgprint)
    # dspXReg('XRDZASTP', "a steps", dbgprint)
    # dspXReg('XRDZLOC', "loc", dbgprint)
    # dspXReg('XRDSTATE', "state", dbgprint)

    # x = 0
    # y = 0
    # clocks = 0
    # sum = d
    # accelAccum = 0
    # distCtr = dist
    # l0 = dist
    # while (clocks < xPos):
    #     clocks += 1
    #     x += 1
    #     if (sum < 0):
    #         sum += incr1
    #     else:
    #         y += 1
    #         sum += incr2
    #         distCtr -= 1
    #         if (distCtr == 0):
    #             break
    #     sum += accelAccum
    #     if (y >= l0):
    #         if (accelAccum > 0):
    #             accelAccum -= zSynAccel
    #     else:
    #         if (clocks <= accelClocks):
    #             accelAccum += zSynAccel
    #     l0 = distCtr

    # print ("\nx %d y %d sum %d delta %d accelAccum %d delta %d" %
    #        (x, y, sum, sum - zsum, accelAccum, accelAccum - zAclSum))

    if pData:
        plot(time, data, 'b', aa="true")
        grid(True)
        show()


def test6(dist=100, dbgprint=True, prt=False):
    if dist == 0:
        dist = 100

    cFreq = 50000000            # clock frequency
    mult = 64                   # freq gen multiplier
    stepsRev = 1600             # steps per revolution
    pitch = .1                  # leadscrew pitch
    scale = 8                   # scale factor

    minFeed = 10                # min feed ipm
    maxFeed = 40                # max feed ipm
    jogV = 20                   # jog velocity
    accelRate = 5               # acceleration rate in per sec^2

    stepsInch = stepsRev / pitch      # steps per inch
    stepsMinMax = maxFeed * stepsInch # max steps per min
    stepsSecMax = stepsMinMax / 60.0  # max steps per second
    freqGenMax = int(stepsSecMax) * mult # frequency generator maximum
    if prt:
        print "stepsSecMax %6.0f freqGenMax %7.0f" % (stepsSecMax, freqGenMax)

    stepsMinMin = minFeed * stepsInch # max steps per min
    stepsSecMin = stepsMinMin / 60.0  # max steps per second
    freqGenMin = stepsSecMin * mult   # frequency generator maximum
    if prt:
        print "stepsSecMin %6.0f freqGenMin %7.0f" % (stepsSecMin, freqGenMin)

    stepsMinJog = int(jogV * stepsInch)
    stepsSecJog = stepsMinJog / 60
    freqGenJog = stepsSecJog * mult
    if prt:
        print "stepsSecJog %d freqGenJog %d\n" % (stepsSecJog, freqGenJog)

    freqDivider = int(floor(cFreq / freqGenMax - 1)) # calc divider
    if prt:
        print "freqDivider %3.0f" % freqDivider

    accelTime = (maxFeed - minFeed) / (60.0 * accelRate) # acceleration time
    accelClocks = int(accelTime * freqGenMax)
    if prt:
        print "accelTime %8.6f clocks %d" % (accelTime, accelClocks)

    for scale in range(0, 10):
        dyMin = int(stepsSecMin) << scale
        dyMax = int(stepsSecMax) << scale
        dx = int(freqGenMax) << scale
        dyDelta = dyMax - dyMin
        if prt:
            print ("\ndx %d dyMin %d dyMax %d dyDelta %d" %
                   (dx, dyMin, dyMax, dyDelta))

        incPerClock = dyDelta / float(accelClocks)
        intIncPerClock = int(incPerClock)
        dyDeltaC = intIncPerClock * accelClocks
        dyIni = dyMax - dyDeltaC
        err = int(dyDelta - dyDeltaC) >> scale
        bits = bitSize(2*dx)
        if prt:
            print (("dyIni %d dyMax %d dyDelta %d incPerClock %4.2f " +
                    "err %d bits %d") %
                   (dyIni, dyMax, dyDeltaC, incPerClock, err, bits))
            if err == 0:
                break

    accel = 2 * intIncPerClock

    dyJog = stepsSecJog << scale;
    dyDelta = (dyJog - dyIni);
    jogAccelClocks = dyDelta / accel;
    dyJog = jogAccelClocks * accel;

    incr1 = 2 * dyIni
    incr2 = incr1 - 2 * dx
    d = incr1 - dx

    totalSum = (accelClocks * incr1) + d
    totalInc = (accelClocks * (accelClocks - 1) * accel) / 2
    accelSteps = ((totalSum + totalInc) / (2 * dx))

    if prt:
        print ("accelClocks %d totalSum %d totalInc %d accelSteps %d" % 
               (accelClocks, totalSum, totalInc, accelSteps))

    setXReg('XLDTCTL', 0, dbgprint)    # clear taper
    command('CMDSTOP')
    while True:
        rsp = command('READDBG')
        if len(rsp) <= 4:
            break;
        print rsp
    print "send commands"
    command('ZSTOP')
    setParm('PRMZLOCIN', 0)
    command('ZSETLOC')
    setParm('PRMZFREQ', freqDivider)
    setParm('PRMZDX', dx)
    setParm('PRMZDYINI', dyIni)
    setParm('PRMZDYJOG', dyJog)
    setParm('PRMZDYMAX', dyMax)
    setParm('PRMZACCEL', accel)
    setParm('PRMZACLJOG', jogAccelClocks)
    setParm('PRMZACLMAX', accelClocks)
    setParm('PRMZDISTIN', dist)
    command('LOADZPRM')
    command('ZMOVE')
    while True:
        rsp = command('READDBG')
        if len(rsp) > 4:
            print rsp
            stdout.flush()
            if rsp.find("z st 00000000") > 0:
                break;
    dspXReg('XRDZLOC', "x loc", dbgprint)

fcy = 84000000

testId = 0
testAxis = 'z'
waitSync = False
repeat = 1
dbgPrint = False
dbgClock = True

dx = 2540 * 8
dy = 600

aVal = 8
aClks = 100

accelRate = 0.75
minAccel = 5.0
encoder = dx

minV = 10.0
maxV = 40.0

xFrequency = 50000000
mult = 16

rpm = 300
pitch = 0.035
tpi = 0

arg1 = 0
arg2 = 0
arg3 = 0

def zSetup():
    global axis, minV, maxV
    setParm('Z_PITCH', "%0.1f" % (axis.pitch))
    setParm('Z_RATIO', "%d" % (axis.ratio))
    setParm('Z_MICRO', "%d" % (axis.microSteps))
    setParm('Z_MOTOR', "%d" % (axis.motorSteps))
    setParm('Z_ACCEL', "%0.2f" % (axis.accel))
    setParm('Z_BACKLASH', "%0.3f" % (axis.backlashSteps))

    setParm('Z_MOVE_MIN', "%0.2f" % (minV))
    setParm('Z_MOVE_MAX', "%0.2f" % (maxV))

    setParm('Z_JOG_MIN', "%0.2f" % (2))
    setParm('Z_JOG_MAX', "5")
    
    command('CMD_ZSETUP')

def xSetup():
    global axis, minV, maxV
    setParm('X_PITCH', "%0.1f" % (axis.pitch))
    setParm('X_RATIO', "%d" % (axis.ratio))
    setParm('X_MICRO', "%d" % (axis.microSteps))
    setParm('X_MOTOR', "%d" % (axis.motorSteps))
    setParm('X_ACCEL', "%0.2f" % (axis.accel))
    setParm('X_BACKLASH', "%0.3f" % (axis.backlashSteps))

    setParm('X_MOVE_MIN', "%0.2f" % (minV))
    setParm('X_MOVE_MAX', "%0.2f" % (maxV))

    setParm('X_JOG_MIN', "%0.2f" % (2))
    setParm('X_JOG_MAX', "5")
    
    command('CMD_XSETUP')

def zTurnSetup():
    global pitch
    setParm('FEED', "%0.4f" % pitch)
    setParm('FEED_TYPE', FEED_PITCH)

    command('CMD_ZSYNSETUP');

def xTurnSetup():
    global pitch
    setParm('FEED', "%0.4f" % pitch)
    setParm('FEED_TYPE', FEED_PITCH)

    command('CMD_XSYNSETUP');

def encoderStart():
    global rpm, encoder

    setParm('X_FREQUENCY', str(xFrequency))
    setParm('FREQ_MULT', str(mult))
    setParm('RPM', str(rpm))
    setParm('ENC_MAX', str(encoder))

    command('ENCSTART')

def extractVal(arg, default, integer=False):
    tmp = arg.split('=')
    if len(tmp) == 2:
        try:
            if integer:
                val = int(tmp[1])
            else:
                val = float(tmp[1])
        except:
            val = default
    else:
        val = default
    return(val)

n = 1
if len(sys.argv) > n:
    try:
        testId = int(sys.argv[n])
    except:
        pass

n += 1
while True:
    if n >= len(sys.argv):
        break
    tmp = sys.argv[n]
    if len(tmp) != 0 and tmp[0].isdigit():
        break;
    tmp = tmp.lower()
    if tmp == 'z':
        testAxis = 'z';
    elif tmp == 'x':
        testAxis = 'x';
    elif tmp == 'dbg':
        dbgPrint = True
    elif tmp == 'ext':
        dbgClock = False
    elif tmp.startswith('repeat'):
        repeat = extractVal(tmp, repeat, True)
    elif tmp.startswith('dx'):
        dx = extractVal(tmp, dx, True)
    elif tmp.startswith('dy'):
        dy = extractVal(tmp, dy, True)
    elif tmp.startswith('rpm'):
        rpm = extractVal(tmp, rpm, True)
    elif tmp.startswith('mult'):
        mult = extractVal(tmp, mult, True)
    elif tmp.startswith('minaccel'):
        minAccel = extractVal(tmp, minAccel)
    elif tmp.startswith('accelRate'):
        accelRate = extractVal(tmp, accelRate)
    elif tmp.startswith('min'):
        minV = extractVal(tmp, minV)
    elif tmp.startswith('max'):
        maxV = extractVal(tmp, maxV)
    elif tmp.startswith('pitch'):
        pitch = extractVal(tmp, pitch)
    elif tmp.startswith('tpi'):
        tpi = extractVal(tmp, pitch)
        if tpi >=4:
            pitch = 1.0 / tpi
    elif tmp.startswith('encoder'):
        encoder = extractVal(tmp, encoder)
    elif tmp.startswith('aVal'):
        aVal = extractVal(tmp, aVal, True)
    elif tmp.startswith('aClks'):
        aClks = extractVal(tmp, aClks, True)
    elif tmp.startswith('wait'):
        waitSync = True
    else:
        print "invalid argument: %s" % (tmp)
        stdout.flush()
        n += 1
        break
    n += 1

if len(sys.argv) > n:
    try:
        arg1 = abs(int(sys.argv[n]))
    except ValueError:
        arg1 = sys.argv[n]

n += 1
if len(sys.argv) > n:
    try:
        arg2 = int(sys.argv[n])
    except ValueError:
        arg2 = sys.argv[n]

n += 1
if len(sys.argv) > n:
    try:
        arg3 = int(sys.argv[n])
    except ValueError:
        arg3 = sys.argv[n]

if arg1 == 'd':
    if arg2 in xRegs:
        setXReg('XLDDREG', xRegs[arg2], False) # load display register
    else:
        print "invalid register " + arg2
else:
    comm.xDbgPrint = dbgPrint

    axis = Axis()
    axis.testInit()
    axis.mult = mult
    axis.accel = accelRate
    axis.setup()

    if testId == 1:             # no accel
        for i in range(0, repeat):
            accel = Test(testAxis, dbgClock, dbgPrint)
            accel.setRPM(rpm)
            accel.setEncoder(encoder)
            accel.testNoAccelSetup(dx, dy)
            accel.setWaitSync(waitSync)
            accel.setDbgPrint(dbgPrint)
            if testAxis == 'z':
                accel.zTestSync(arg1, arg2, arg3)
            elif testAxis == 'x':
                accel.xTestSync(arg1, arg2, arg3)
            stdout.flush()

    if testId == 2:             # taper without acceleration
        for i in range(0, repeat):
            accel = Test(testAxis, dbgClock, dbgPrint)
            accel.setRPM(rpm)
            accel.setEncoder(encoder)
            accel.testNoAccelSetup(dx, dy)
            if testAxis == 'z':
                accel.zTestXTaper(arg1, arg2, arg3)
            elif testAxis == 'x':
                accel.xTestZTaper(arg1, arg2, arg3)
            stdout.flush()

    if testId == 3:             # move with acceleration
        for i in range(0, repeat):
            if repeat > 1:
                print "pass %d" % (i + 1)
            tmp = Move(axis, dbgPrint)
            accel = Test(testAxis, dbgClock, dbgPrint)
            tmp.setup(accel, minV, maxV)
            if testAxis == 'z':
                accel.zTestMove(arg1, arg2, arg3)
                tmp = dspXReg('XRDZXPOS')
                if tmp == 0:
                    print "z pos zero"
                    break
            elif testAxis == 'x':
                accel.xTestMove(arg1, arg2, arg3)
            stdout.flush()

    if testId == 4:             # simple acceleration test
        for i in range(0, repeat):
            accel = Test(testAxis, dbgClock, dbgPrint)
            accel.setEncoder(encoder)
            accel.setRPM(rpm)
            accel.setWaitSync(waitSync)
            accel.testNoAccelSetup(dx, dy)
            accel.accel = aVal
            accel.accelClocks = aClks
            accel.setDbgPrint(dbgPrint)
            if testAxis == 'z':
                accel.zTestSync(arg1, arg2, arg3)
            elif testAxis == 'x':
                accel.xTestSync(arg1, arg2, arg3)
            stdout.flush()

    if testId == 5:             # turn with acceleration
        for i in range(0, repeat):
            accel = Test(dbgClock, dbgPrint)
            accel.setEncoder(encoder)
            accel.setRPM(rpm)
            accel.setWaitSync(waitSync)
            tmp = Turn(axis, minAccel, encoder, dbgPrint)
            tmp.setup(accel, rpm, pitch)
            accel.setDbgPrint(dbgPrint)
            if testAxis == 'z':
                accel.zTestSync(arg1, arg2, arg3)
            elif testAxis == 'x':
                accel.xTestSync(arg1, arg2, arg3)
            stdout.flush()

    if testId == 6:             # move setup
        tmp = Move(axis, dbgPrint)
        accel = Accel(dbgPrint)
        tmp.setup(accel, min, maxV)
        accel.test()

    if testId == 7:             # turn setup
        tmp = Turn(axis, minAccel, encoder, dbgPrint)
        accel = Test(testAxis, dbgClock, dbgPrint)
        tmp.setup(accel, rpm, pitch)
        accel.test()

    if testId == 8:             # acceleration plot for turn
        tmp = Turn(axis, minAccel, encoder, dbgPrint)
        accel = accelPlot(dbgPrint)
        tmp.setup(accel, rpm, pitch)
        accel.plot(arg1, arg2, "accelPlot.txt", dbgPrint)

    if testId == 9:             # test software encoder
        # global fcy
        preScaler = 1
        encTimer = int(fcy / encoder)
        while encTimer >= 65536:
            preScaler += 1
            encTimer = int(fcy / (encoder * preScaler))
        print "preScaler %d encTimer %d" % (preScaler, encTimer)
        command('ENCSTOP')
        setParm('ENC_PRE_SCALER', preScaler)
        setParm('ENC_TIMER', encTimer)
        setParm('ENC_MAX', encoder)
        setParm('ENC_RUN_COUNT', arg1)
        command('ENCSTART')

    if testId == 10:		# test for curruption of z control register
        for i in range(0, repeat):
            setXReg('XLDZCTL', 0)
            setXReg('XLDXCTL', 0)
            setXReg('XLDZCTL', ZSTART)
            setXReg('XLDXCTL', XSTART)
            k = 3
            for j in range(0, arg1):
                val = dspXReg('XRDSR')
                comm.setXRegN(k, 0)
                k += 1
                if k > 0x31:
                    k = 3
                if (val & S_Z_START) == 0:
                    print "%2d %2d no start %x" % (i, j, val)
                    stdout.flush()

    if testId == 11:            # test move accel code
        dbgPrint = True
        axis.pitch = 0.1
        axis.ratio = 1
        axis.microSteps = 8
        axis.motorSteps = 200
        axis.accel = 0.75
        axis.backlashSteps = 0.023
        axis.setup()

        tmp = Move(axis, dbgPrint)
        accel = Accel(dbgPrint)
        tmp.setup(accel, minV, 20.0)
        print
        tmp.setup(accel, minV, 5.0)
        print

        setParm('Z_PITCH', "%0.1f" % (axis.pitch))
        setParm('Z_RATIO', "%d" % (axis.ratio))
        setParm('Z_MICRO', "%d" % (axis.microSteps))
        setParm('Z_MOTOR', "%d" % (axis.motorSteps))
        setParm('Z_ACCEL', "%0.2f" % (axis.accel))
        setParm('Z_BACKLASH', "%0.3f" % (axis.backlashSteps))

        setParm('Z_MOVE_MIN', "%0.2f" % (minV))
        setParm('Z_MOVE_MAX', "%0.2f" % (maxV))

        setParm('Z_JOG_MIN', "%0.2f" % (minV))
        setParm('Z_JOG_MAX', "5")

        setParm('X_FREQUENCY', "50000000")
        setParm('RPM', "300")
        setParm('ENC_MAX', str(encoder))
        setParm('FREQ_MULT', 16)

        command('CMD_ZSETUP')

    if testId == 12:            # test turn accel code
        dbgPrint = True
        axis.pitch = 0.1
        axis.ratio = 1
        axis.microSteps = 8
        axis.motorSteps = 200
        axis.accel = accelRate
        axis.backlashSteps = 0.023
        axis.setup()

        tmp = Turn(axis, minAccel, encoder, dbgPrint)
        accel = Test(axis, dbgClock, dbgPrint)
        tmp.setup(accel, rpm, pitch)
        accel.test()

        setParm('Z_PITCH', "%0.1f" % (axis.pitch))
        setParm('Z_RATIO', "%d" % (axis.ratio))
        setParm('Z_MICRO', "%d" % (axis.microSteps))
        setParm('Z_MOTOR', "%d" % (axis.motorSteps))
        setParm('Z_ACCEL', "%0.2f" % (axis.accel))
        setParm('Z_BACKLASH', "%0.3f" % (axis.backlashSteps))

        setParm('Z_MOVE_MIN', "%0.2f" % (minV))
        setParm('Z_MOVE_MAX', "%0.2f" % (maxV))

        setParm('Z_JOG_MIN', "%0.2f" % (minV))
        setParm('Z_JOG_MAX', "5")

        setParm('X_FREQUENCY', "50000000")
        setParm('RPM', str(rpm))
        setParm('ENC_MAX', str(encoder))
        setParm('FREQ_MULT', 16)

        command('CMD_ZSETUP')

        setParm('FEED', "%0.4f" % pitch)
        setParm('FEED_TYPE', FEED_PITCH)
        command('CMD_ZSYNSETUP');

    if testId == 13:
        for pitch in (.018, .035, 0.050, .075, 0.1, 0.2):
            print "turn %0.3f\n" % (pitch)
            tmp = Turn(axis, minAccel, encoder, dbgPrint)
            accel = Test(axis, dbgClock, dbgPrint)
            tmp.setup(accel, rpm, pitch)
            print

    if testId == 14:
        for i in (9.6, 12, 18, 24, 36, 48):
            print "move %d ipm\n" % (i)
            tmp = Move(axis, dbgPrint)
            accel = Accel(dbgPrint)
            tmp.setup(accel, minAccel, float(i))
            print

    if testId == 15:
        test4(arg1, pitch, arg2, dbgPrint, False)

    if testId == 16:
        j = 0
        for i in range(0, repeat):
            setXReg('XLDZCTL', j)
            setXReg('XLDXCTL', j)
            xTest = j & ((1 << (xCtl_size)) - 1)
            zTest = j & ((1 << (zCtl_size)) - 1)
            zVal = getXReg('XRDZCTL')
            xVal = getXReg('XRDXCTL')
            if zVal != zTest:
                print "zTest %4x zVal %4x" % (zTest, zVal)
            if xVal != xTest:
                print "xTest %4x xVal %4x" % (xTest, xVal)
            stdout.flush()
            j += 1

    if testId == 17:
        command('CLRDBG');
        command('CMD_CLEAR')
        encoderStart()
        if testAxis == 'z':
            zSetup()
            zTurnSetup()
            setParm('Z_MOVE_DIST', arg1)
            setParm('Z_FLAG', ZSYN)
            command('ZMOVEREL')
        elif testAxis == 'x':
            xSetup()
            xTurnSetup()
            setParm('X_MOVE_DIST', arg1)
            setParm('X_FLAG', XSYN)
            command('XMOVEREL')

if not (comm.ser is None):
    comm.ser.close()
