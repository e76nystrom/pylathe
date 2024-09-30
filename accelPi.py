from math import floor, log
from sys import stdout

import enumDef as en
import ctlBitDef as ct

DBG_SETUP = True
DBG_DETAIL = False

MAX_SCALE = 12

def intRound(val):
    return(int(round(val)))

def bitSize(val, dbg=False):
    if val < 0:
        val = -val
        b = 1
    else:
        b = 0
    while b < 32:
        if dbg:
            print(b, val)
        if val == 0:
            break
        val >>= 1
        b += 1
    return b

class SpindleAccel:
    def __init__(self):
        self.maxRPM      = None
        self.stepsPerRev = None
        self.initialSum  = None
        self.accelRMin2  = None
        self.dx          = None
        self.dy          = None
        self.incr1       = None
        self.incr2       = None
        self.intAccel    = None
        self.accelClocks = None
        self.accelMax    = None
        self.freqDivider = None

class AccelData(SpindleAccel):
    def __init__(self, axis):
        SpindleAccel.__init__(self)
        # self.incr1       = None
        # self.incr2       = None
        # self.initialSum  = None
        # self.intAccel    = None
        # self.accelClocks = None
        # self.freqDivider = None
        self.axis          = axis
        self.accelSteps    = None
        self.accelTime     = None
        self.clockFreq     = None
        self.clocksPerInch = None
        self.dxBase        = None
        self.dyMaxBase     = None
        self.dyMinBase     = None
        self.pitch         = None # pitch for turning or threading
        self.scale         = None
        self.stepsSecMax   = None

    def init(self, accelType, minSpeed=0, maxSpeed=0):
        print("\n%s %s AccelData init" % (self.axis.name, accelType))
        self.accel     = self.axis.accel # axis acceleration units/sec^2
        self.accelType = accelType # acceleration type string
        self.maxSpeed  = maxSpeed # final speed
        self.minSpeed  = minSpeed # starting speed
        self.stepsInch = self.axis.stepsInch # axis steps per inch

        accelCalc1(self)

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

def syncCalc(aData, dx, dy):
    aData.dx     = dx = int(dx)
    aData.dy     = dy = int(dy)
    aData.incr1       = 2 * dy
    aData.incr2       = aData.incr1 - 2 * dx
    aData.initialSum  = aData.incr1 - dx
    aData.intAccel    = 0
    aData.accelClocks = 0

def syncAccelCalc(aData, feedType, feed):
    print("\n%s %s syndAccelCalc" % (aData.axis.name, aData.accelType))
    if feedType == ct.FEED_PITCH:
        aData.pitch = feed
    elif feedType == ct.FEED_TPI:
        aData.pitch = 1.0 / feed
    elif feedType == ct.FEED_METRIC:
        aData.pitch = feed / 25.4

    if DBG_SETUP:
        print("\n" "turnAccel %3.1f" % aData.accel)
    parm = aData.axis.parm
    aData.freqDivider = 0
    encPerRev = aData.axis.encPerRev
    if aData.maxSpeed == 0:
        # (pulse / rev) / (in / rev) = pulse / in
        # (pulse / in) / (steps / in) = pulse / step
        encPerInch = intRound(encPerRev / aData.pitch)
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
        aData.clocksPerInch = intRound(encPerRev * aData.pitch)
        aData.clockFreq = intRound((parm.rpm * encPerRev) / 60.0)
        accelSetup(aData)

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
            print("\n" "scale %d dx %d dyMin %d dyMax %d dyDelta %d" % \
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

        bits = bitSize(-2 * aData.dx)
        if DBG_DETAIL:
            print("dyIni %d dyMax %d dyDelta %d incPerClock %6.2f " \
                  "err %d bits %d" %
                  (aData.dyIni, aData.dyMax, dyDelta, incPerClock, \
                   err, bits))

        if (bits >= 30) or (err == 0):
            if DBG_SETUP:
                print("\n" "scale %d dx %d dyMin %d dyMax %d dyDelta %d" %
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
        print("\n" "incr1 %d incr2 %d sum %d" %
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
    stdout.flush()
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

def taperCalc(turnAccel, taperAccel, taper):
    axis = turnAccel.axis
    print("\n%s accel taperCalc" % (axis.name))
    print("taperCalc a0 %s a1 %s taper %8.6f" % \
          (turnAccel.axis.name, taperAccel.axis.name, taper))
    parm = axis.parm
    # stepsInch = turn.stepsInch
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
        encPerRev = turnAccel.axis.encPerRev
        dx = intRound((encPerRev * turnCycleDist) / turnAccel.pitch)
        dy = intRound(taperCycleDist * taperAccel.axis.stepsInch)
        taperAccel.incr1 = 2 * dy
        taperAccel.incr2 = taperAccel.incr1 - 2 * dx
        taperAccel.intAccel = 0
        taperAccel.accelClocks = 0
        taperAccel.freqDivider = 0
        taperAccel.initialSum = taperAccel.incr1 - dx
        print("encPerCycle dx %d stepsCycle dy %d " \
              "incr1 %d incr2 %d initialSum %d" %
               (dx, dy, taperAccel.incr1, taperAccel.incr2, \
                taperAccel.initialSum))
        print("dy/dx %7.4f" % (float(dy) / float(dx)))
    elif turnSync == en.SEL_TU_SYN:
        pass

def spindleAccelCalc0(parm, maxRPM):
    fpgaFrequency  = parm.fpgaFreq
    motorSteps     = parm.spSteps
    microSteps     = parm.spMicroSteps
    stepMultiplier = parm.spStepMult
    accelRPMSec2   = parm.spAccel
    # minRPM = parm.spMinRPM
    # maxRPM = parm.spMaxRPM

    stepsPerRev = motorSteps * microSteps * stepMultiplier
    revPerSec = maxRPM / 60
    stepsPerSec = revPerSec * stepsPerRev
    freqDivider = fpgaFrequency / stepsPerSec
    print(f"stepsPerRev {stepsPerRev:.0f}"
          f"stepPerSec {stepsPerSec:.0f}"
          f" freqDivider {freqDivider:.0f}")

    # stepsPerSecMin = (minRPM / 60) * stepsPerRev
    stepsPerSecMax = (maxRPM / 60) * stepsPerRev
    accelStepsSec2 = (accelRPMSec2 / 60) * stepsPerRev
    accelTime = stepsPerSecMax / accelStepsSec2
    print(f"accelStepsSec2 {accelStepsSec2:.0f} accelTime {accelTime:.3f}")

    dxBase = stepsPerRev
    dyMinBase = 0
    dyMaxBase = motorSteps * microSteps

    accelClocks = accelTime * stepsPerSec
    intIncPerClock = 0
    dx = 0
    dyIni = 0
    scale = 1
    for scale in range(MAX_SCALE):
        dx = dxBase << scale
        dyMax = dyMaxBase << scale
        dyMin = dyMinBase << scale
        dyDelta = dyMax - dyMin
        if DBG_DETAIL:
            print("\n" "scale %2d dx %8d dyMin %8d dyMax %8d dyDelta %8d" %
                  (scale, dx, dyMin, dyMax, dyDelta), end=' ')
            print("%10.4f" % (float(dx) / float(dyMax)))

        incPerClock = float(dyDelta) / accelClocks
        intIncPerClock = int(incPerClock)
        if intIncPerClock == 0:
            continue
        intIncPerClock = intIncPerClock
        dyDeltaC = intIncPerClock * accelClocks
        err = intRound(abs(dyDelta - dyDeltaC)) >> scale
        dyIni = dyMax - intIncPerClock * accelClocks
        if DBG_DETAIL:
            print("dyIni %8d dyMax %8d intIncPerClock %3d accelClocks %3d" %
                  (dyIni, dyMax, intIncPerClock, accelClocks))

        bits = bitSize(dx) + 1
        if DBG_DETAIL:
            print("dyIni %8d dyMax %8d dyDelta %8d incPerClock %6.2f "
                  "err %d bits %d" %
                  (dyIni, dyMax, dyDelta, incPerClock, err, bits))

        if (bits >= 30) or (err == 0):
            if DBG_SETUP:
                print("\n" "scale %2d dx %8d dyMin %8d dyMax %8d dyDelta %8d" %
                      (scale, dx, dyMin, dyMax, dyDelta))
                print("dyIni %8d dyMax %8d dyDelta %8d incPerClock %6.2f "
                      "err %d bits %d" %
                      (dyIni, dyMax, dyDelta, incPerClock, err, bits))
            break

    incr1      = int(2 * dyIni)
    incr2      = int(incr1 - 2 * dx)
    initialSum = int(incr1 - dx)
    intAccel   = int(2 * intIncPerClock)

    accelParm = SpindleAccel()
    accelParm.initialSum  = initialSum
    accelParm.incr1       = incr1
    accelParm.incr2       = incr2
    accelParm.scale       = scale
    accelParm.intAccel    = intAccel
    accelParm.accelClock  = accelClocks
    accelParm.freqDivider = freqDivider

    if DBG_SETUP:
        print("\n" "incr1 %d incr2 %d sum %d bits %d" %
              (incr1, incr2, initialSum, bitSize(incr2)))

    if intIncPerClock != 0:
        totalSum = accelClocks * incr1 + initialSum
        totalInc = (accelClocks * (accelClocks - 1) * intAccel) / 2
        accelSteps = intRound((totalSum + totalInc) / (2 * dx))
        if DBG_SETUP:
            print("accelClocks %d totalSum %d totalInc %d " \
                  "accelSteps %d" % \
                  (accelClocks, totalSum, totalInc, accelSteps))
    # else:
    #     accelSteps = 0

    return accelParm


    # fpgaFrequency = 50_000_000
    # motorSteps = 200
    # microSteps = 10
    # stepMultiplier = 8
    # accelRMin2 = 400
    # maxRPM = 300
def spindleAccelCalc(parm, maxRPM):
    print("\n" "spindleAccelCalc")
    fpgaFrequency  = parm.fpgaFrequency
    motorSteps     = parm.spSteps
    microSteps     = parm.spMicro
    stepMultiplier = parm.spStepMult
    accelRMin2     = parm.spAccel

    stepsPerRev = motorSteps * microSteps
    revPerSec = maxRPM / 60
    stepsPerSec = int(stepsPerRev * revPerSec)
    print(f"maxRPM {maxRPM} revPerSec {revPerSec:0.3f}"
          f" stepsPerSec {stepsPerSec}")
    freqGenMax = revPerSec * stepsPerRev * stepMultiplier
    freqDivider = fpgaFrequency / freqGenMax
    periodUSec = 1_000_000 / freqGenMax
    print(f"stepsPerRev {stepsPerRev:.0f} freqGenMax {freqGenMax:.0f}"
          f" freqDivider {freqDivider:.0f}"
          f" periodUSec {periodUSec:.0f} uSec")
    rpmCalc = (freqGenMax * 60) / (stepsPerRev * stepMultiplier)
    print(f"rpmCalc" f"{rpmCalc:.0f}")

    accelTime = maxRPM / accelRMin2
    accelStepSec2 = (accelRMin2 / 60) * stepsPerRev
    accelClocks = int(accelTime * freqGenMax)
    print(f"accelTime {accelTime:.3f}"
          f" accelStepSec2 {accelStepSec2:.0f}"
          f" accelClocks {accelClocks:.0f}")

    dx = freqGenMax
    dy = stepsPerSec * stepMultiplier
    incr1      = int(2 * dy)
    incr2      = int(incr1 - 2 * dx)
    initialSum = int(incr1 - dx)
    print("dx %d dy %d incr1 %d incr2 %d sum %d bits %d" %
          (dx, dy, incr1, incr2, initialSum, bitSize(incr2)))
    # incr1 = dy * 2
    # dy = incr1 / 2
    dy = incr1 // 2

    # incr2 = incr1 - 2 * dx
    # incr2 - incr1 = -2 * dx
    # dx = (incr1 - incr2) / 2
    dx = (incr1 - incr2) // 2
    print(f"dx {dx} dy {dy}")

    dxBase = freqGenMax
    dyBase = stepsPerSec * stepMultiplier
    incPerClockInt = 0
    dx = 0
    dyIni = 0
    scale = 1
    for scale in range(MAX_SCALE):
        dx = int(dxBase) << scale
        dyMax = dyBase << scale
        if DBG_DETAIL:
            print("\n" "scale %2d dx %8d dyMax %8d" %
                  (scale, dx, dyMax), end=' ')
            print("%10.4f" % (float(dx) / float(dyMax)))

        incPerClock = dyMax / accelClocks
        incPerClockInt = int(dyMax // accelClocks)
        if incPerClockInt == 0:
            continue

        err = (dyMax - incPerClockInt * accelClocks) >> scale
        errPercent = (err * 100) / (dyMax >> scale)
        dyIni = dyMax - incPerClockInt * accelClocks
        bits = bitSize(-2 * dx)
        if DBG_DETAIL:
            print("dyIni %8d dyMax %8d IncPerClockInt %3d" %
                  (dyIni, dyMax, incPerClockInt), end="")
            print(" incPerClock %6.2f err %d %.1f%% bits %d" %
                  (incPerClock, err, errPercent, bits))

        if (bits >= 30) or (errPercent <= 1.0):
            # if DBG_SETUP:
            #     print("\n" "scale %2d dx %8d dyMax %8d" %
            #           (scale, dx, dyMax))
            #     print("dyIni %8d dyMax %8d incPerClock %6.2f err %d bits %d" %
            #           (dyIni, dyMax, incPerClock, err, bits))
            break

    incr1      = int(2 * dyIni)
    incr2      = int(incr1 - 2 * dx)
    initialSum = int(incr1 - dx)
    intAccel   = int(2 * incPerClockInt)

    sA = SpindleAccel()
    sA.maxRPM      = maxRPM
    sA.stepsPerRev = stepsPerRev
    sA.accelRMin2  = accelRMin2
    sA.freqGenMax  = freqGenMax
    sA.dx          = dx
    sA.dy          = dy
    sA.initialSum  = initialSum
    sA.incr1       = incr1
    sA.incr2       = incr2
    sA.scale       = scale
    sA.intAccel    = intAccel
    sA.accelClocks = accelClocks
    sA.accelMax    = accelClocks * intAccel
    sA.freqDivider = intRound(freqDivider) - 1

    if DBG_SETUP:
        print("\n" "incr1 %d incr2 %d sum %d intAccel %d clocks %d bits %d" %
              (incr1, incr2, initialSum, intAccel, accelClocks, bitSize(incr2)))

    if incPerClockInt != 0:
        totalSum = accelClocks * incr1 + initialSum
        totalInc = (accelClocks * (accelClocks - 1) * intAccel) / 2
        accelSteps = intRound((totalSum + totalInc) / (2 * dx))
        if DBG_SETUP:
            print("accelClocks %d totalSum %d totalInc %d " \
                  "accelSteps %d" % \
                  (accelClocks, totalSum, totalInc, accelSteps))
    return sA

def spUpdate(sA, curRPM):
    dx         = sA.dx
    dy         = int((curRPM * sA.stepsPerRev) / sA.maxRPM)
    incr1      = int(2 * dy)
    incr2      = int(incr1 - 2 * dx)
    initialSum = int(incr1 - dx)
    print("dx %d dy %d incr1 %d incr2 %d sum %d bits %d" %
          (dx, dy, incr1, incr2, initialSum, bitSize(incr2)))
    
    curTime = curRPM / sA.accelRMin2
    curClocks = curTime * sA.freqGenMax
    print(f"curTime {curTime:.03f}"
          f" curClocks {curClocks:.0f}")

    curAccelMax = int(curClocks) * sA.intAccel
    print(f"accelMax = {sA.accelMax}"
          f" curAccelMax: {curAccelMax}")
    return curAccelMax
