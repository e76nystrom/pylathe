#!/usr/bin/python3

from math import floor, log, sqrt
from sys import stdout
from time import sleep
from platform import system
import sys
import time
import lRegDef as rg
import fpgaLathe as bt

WINDOWS = system() == 'Windows'

if WINDOWS:
    spi = None
else:
    import spidev
    bus = 0
    device = 0
    spi = spidev.SpiDev()
    spi.open(bus, device)
    spi.max_speed_hz = 500000
    spi.mode = 0

ctlEna = False
ldBuf = []
rdBuf = []

encCycle = 16-1
intCycle = 4

cmdWaitZ = 1
cmdWaitX = 2

sync = True
syncEnc = True
Z_AXIS = False

base = rg.F_ZAxis_Base if Z_AXIS else rg.F_XAxis_Base
bSyn = base + rg.F_Sync_Base
bLoc = base + rg.F_Loc_Base
bDist = base + rg.F_Dist_Base
    
def fWrite(f, txt):
    f.write(txt.encode())

cmdBuf = False

def ldStart():
    global cmdBuf, ldBuf
    ldBuf = []
    ldBuf += [rg.F_Ctrl_Base + rg.F_Ld_Ctrl_Data]
    cmdBuf = True

def ldSeq(seq):
    global ldBuf
    ldBuf += [rg.F_Ctrl_Base + rg.F_Ld_Seq]
    ldBuf += [seq]

def ldCmd(cmd):
    global ldBuf
    ldBuf += [rg.F_Ctrl_Base + rg.F_Ctrl_Cmd]
    ldBuf += [cmd]

def ldSend():
    global cmdBuf, ldBuf
    cmdBuf = False
    print(ldBuf)
    if spi is not None:
        spi.xfer2(ldBuf)

def ld(cmd, data, size, dbg=True):
    global cmdBuf, ldBuf
    if dbg:
        print("ld 0x%02x %10d %08x %s" % \
              (cmd, data, data&0xffffffff, rg.xRegTable[cmd]), end=" ")
    data &= 0xffffffff
    val = list(data.to_bytes(size, byteorder='big'))
    if cmdBuf:
        ldBuf += [cmd]
        ldBuf += [size]
        ldBuf += val
        if dbg:
            t = "b"
    else:
        msg = [cmd] + val
        if spi is not None: 
            spi.xfer2(msg)
            if dbg:
                t = "s"
    if dbg:
        print(t)

def rdInit():
    global rdBuf
    rdBuf = [rg.F_Read_Base + rg.F_Ld_Read_Data]

def rdAdd(val):
    global rdBuf
    rdBuf += [val]

def rdSend():
    global rdBuf
    if spi is not None:
        print(rdBuf)
        spi.xfer2(rdBuf)
    
def rdSetup():
    global rdBuf, rdLength
    rdInit()
    rdAdd(bSyn + rg.F_Rd_XPos)
    rdAdd(bSyn + rg.F_Rd_YPos)
    rdAdd(bSyn + rg.F_Rd_Sum)
    rdAdd(bSyn + rg.F_Rd_Accel_Sum)
    rdAdd(bSyn + rg.F_Rd_Accel_Ctr)
    rdAdd(bDist + rg.F_Rd_Dist)
    rdAdd(bDist + rg.F_Rd_Acl_Steps)
    rdAdd(bLoc + rg.F_Rd_Loc)
    rdLength = (len(rdBuf) - 1) * 4
    rdSend()

def rdTest():
    global rdLength
    if spi is None:
        return None
    spi.xfer2([rg.F_Read_Base + rg.F_Read])
    val = spi.readbytes(rdLength)
    print(len(val), val)
    count = int(len(val) / 4)
    result = [0] * count
    for i in range(count):
        j = i * 4
        tmp = val[j:j+4]
        print(i, j, tmp)
        r = int.from_bytes(tmp, byteorder='big')
        if r & 0x80000000:
            r |= -1 & ~0xffffffff
        result[i] = r
    print(result)
    return result

def rd(cmd, size):
    if spi is None:
        return(0)
    msg = [cmd]
    spi.xfer2(msg)
    val = spi.readbytes(size)
    result = int.from_bytes(val, byteorder='big')
    if result & 0x80000000:
        result |= -1 & ~0xffffffff
    return(result)

def readData(index=None, prt=True):
    global xPos, yPos, zSum, zAclSum, aclCtr, curLoc, curDist
    xPos = rd(bSyn + rg.F_Rd_XPos, 4)
    yPos = rd(bSyn + rg.F_Rd_YPos, 4)
    zSum = rd(bSyn + rg.F_Rd_Sum, 4)
    zAclSum = rd(bSyn + rg.F_Rd_Accel_Sum, 4)
    aclCtr = rd(bSyn + rg.F_Rd_Accel_Ctr, 4)
    if prt:
        if index is None:
            print("    ", end=" ")
        else:
            print("%4d" % (index), end=" ")
            
        print("xPos %7d yPos %6d zSum %12d" % (xPos, yPos, zSum), end=" ")
        print("aclSum %8d aclCtr %8d" % (zAclSum, aclCtr), end=" ")

    curDist = rd(bDist + rg.F_Rd_Dist, 4) # read z location
    curAcl = rd(bDist + rg.F_Rd_Acl_Steps, 4) # read accel steps
    curLoc = rd(bLoc + rg.F_Rd_Loc, 4)  # read z location

    if prt:
        print("dist %6d aclStp %6d loc %5d" % (curDist, curAcl, curLoc))

def test3(runClocks=100, stepClocks=0, dist=20, loc= 0, dbgprint=True, \
          dbg=False, pData=False):
    global ctlEna
    global xPos, yPos, zSum, zAclSum, aclCtr, curLoc, curDist
    if pData:
        from pylab import plot, grid, show
        from array import array
        time = array('f')
        data = array('f')
        time.append(0)
        data.append(0)

    cFreq = 50000000            # clock frequency
    mult = 8                    # freq gen multiplier
    stepsRev = 1600             # steps per revolution
    pitch = .1                  # leadscrew pitch
    scale = 8                   # scale factor

    minFeed = 0			# min feed ipm
    maxFeed = 40                # max feed ipm
    accelRate = 20              # acceleration rate in per sec^2

    stepsInch = stepsRev / pitch      # steps per inch
    stepsMinMax = maxFeed * stepsInch # max steps per min
    stepsSecMax = int(stepsMinMax / 60.0)  # max steps per second
    freqGenMax = int(stepsSecMax * mult) # frequency generator maximum
    print("stepsSecMax %6.0f freqGenMax %7.0f" % (stepsSecMax, freqGenMax))

    stepsMinMin = minFeed * stepsInch # max steps per min
    stepsSecMin = stepsMinMin / 60.0  # max steps per second
    freqGenMin = stepsSecMin * mult   # frequency generator maximum
    print("stepsSecMin %6.0f freqGenMin %7.0f" % (stepsSecMin, freqGenMin))

    freqDivider = int(floor(cFreq / freqGenMax - 1)) # calc divider
    print("freqDivider %3.0f" % freqDivider)

    accelTime = (maxFeed - minFeed) / (60.0 * accelRate) # acceleration time
    accelClocks = int(accelTime * freqGenMax)
    print("accelTime %8.6f clocks %d" % (accelTime, accelClocks))

    scalePrt = False
    for scale in range(0, 10):
        dyMin = int(stepsSecMin) << scale
        dyMax = int(stepsSecMax) << scale
        dx = int(freqGenMax) << scale
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
    # d = 0

    bits = int(floor(log(abs(incr2), 2))) + 1
    print(("\ndx %d dy %d incr1 %d incr2 %d d %d bits %d scale %d" %
           (dx, dyIni, incr1, incr2, d, bits, scale)))

    zSynAccel = 2 * intIncPerClock
    zSynAclCnt = accelClocks
    
    totalSum = (accelClocks * incr1) + d
    totalInc = zSynAccel * (accelClocks * (accelClocks + 1) / 2)
    accelSteps = ((totalSum + totalInc) / (2 * dx))

    print(("accelClocks %d totalSum %d totalInc %d accelSteps %d" % 
           (accelClocks, totalSum, totalInc, accelSteps)))

    if True:
        if dist < 2 * accelSteps:
            aSteps = int(dist / 2)
        else:
            aSteps = accelSteps

        #aSteps = (accelClocks * incr1) + d + zSynAccel * (accelClocks * (accelClocks + 1) / 2)
        #aSteps * (2 * dx) = accelClocks * incr1 + d + (zSynAccel / 2) * (accelClocks * accelClocks + 2 * accelClocks + 1)

        c0 = zSynAccel / 2

        #aSteps * (2 * dx) = accelClocks * incr1 + d + c0 * (accelClocks * accelClocks + 2 * accelClocks + 1)
        #aSteps * (2 * dx) = accelClocks * incr1 + d + c0 * accelClocks * accelClocks + c0 * 2 * accelClocks + c0
        #aSteps * (2 * dx) = c0 * accelClocks * accelClocks + accelClocks * (c0 * 2 + incr1) + (c0 + d)
        #c0 * accelClocks * accelClocks + (c0 * 2 + incr1) * accelClocks + (c0 + d) - (aSteps * (2 * dx)) = 0

        a = c0
        b = c0 * 2 + incr1
        c = c0 + d - aSteps * (2 * dx)
        term = sqrt(b * b - 4 * a * c)
        denom = 2 * a

        print("\naSteps %d c0 %d a %d b %d c %d" % (aSteps, c0, a, b, c))
        print("term %d denom %d" % (term , denom))
        print("%7.4f %7.4f" % ((-b + term) / denom, (-b - term) / denom))

    f = open('accel.txt', 'wb')
    clocks = 0
    lastT = 0
    lastC = 0
    x = 0
    y = 0
    sum = d
    inc = 2 * intIncPerClock
    incAccum = 0
    print(("\n%17s incr1 %8d incr2 %10d inc %4d" % \
           ("", incr1, incr2, intIncPerClock)))
    stdout.flush()
    prt = False
    while (clocks < (accelClocks * 1.2)):
        x += 1
        if (sum < 0):
            sum += incr1
        else:
            y += 1
            sum += incr2
            curT = clocks / freqGenMax
            deltaT = curT - lastT
            if pData:
                if (lastT != 0):
                    time.append(curT);
                    data.append(1.0 / deltaT)
            lastT = curT
        sum += incAccum
        if (clocks < accelClocks):
            incAccum += inc
        if sum > 0:
            deltaC = clocks - lastC
            fWrite(f, ("(%6d %5d) dC %5d sum %8d iAcum %8d " \
                       "i1 %8d i2 %11d\n") % \
                   (x, y, deltaC, sum, incAccum,
                    incr1 + incAccum, incr2 + incAccum))
            lastC = clocks
        clocks += 1
    f.close()

    print(("y %4d clks %5d incr1 %8d incr2 %10d sum %12d incAccum %8d" %
           (y, clocks, incr1 + incAccum, incr2 + incAccum, sum, incAccum)))

    print("\n")

    if ctlEna:
        runCtl = bt.runInit
        ld(rg.F_Ld_Run_Ctl, runCtl, 1)

        runCtl = 0
        ld(rg.F_Ld_Run_Ctl, runCtl, 1)

        ldStart()
        ldSeq(1)
    else:
        runCtl = bt.runInit
        ld(rg.F_Ld_Run_Ctl, runCtl, 1)
        runCtl = 0
        ld(rg.F_Ld_Run_Ctl, runCtl, 1)
        status = rd(rg.F_Rd_Status, 4)
        print("status {0:04b}".format(status))

    clkReg = 0
    ld(rg.F_Ld_Clk_Ctl, clkReg, 1);

    axisCtl = bt.ctlInit
    ld(base + rg.F_Ld_Axis_Ctl, axisCtl, 1);

    axisCtl = 0
    ld(base + rg.F_Ld_Axis_Ctl, axisCtl, 1);

    syncCtl = 0
    ld(rg.F_Ld_Sync_Ctl, axisCtl, 1);

    cfgCtl = 0
    ld(rg.F_Ld_Cfg_Ctl, cfgCtl, 1);

    if syncEnc:
        ld(bSyn + rg.F_Ld_D, d, 4) # load d value

        ld(bSyn + rg.F_Ld_Incr1, incr1, 4) # load incr1 value
        ld(bSyn + rg.F_Ld_Incr2, incr2, 4) # load incr2 value

        ld(bSyn + rg.F_Ld_Accel_Val, zSynAccel, 4) # load accel
        ld(bSyn + rg.F_Ld_Accel_Count, zSynAclCnt, 4) # load accel count

    ld(bLoc + rg.F_Ld_Loc, 5, 4)      # set location
    ld(bDist + rg.F_Ld_Dist, dist, 4) # load distance

    axisCtl = bt.ctlInit | bt.ctlSetLoc
    ld(base + rg.F_Ld_Axis_Ctl, axisCtl, 1);
    
    axisCtl = 0
    ld(base + rg.F_Ld_Axis_Ctl, axisCtl, 1);

    # if ctlEna:
    #     ldSend()
    #     status = rd(rg.F_Rd_Status, 4)
    #     seq = rd(rg.F_Ctrl_Base + rg.F_Rd_Seq, 4)
    #     count = rd(rg.F_Ctrl_Base + rg.F_Rd_Ctr, 4)
    #     print("status {0:04b} ".format(status), end="")
    #     print("seq %d count %d" % (seq, count))
    #     runCtl = bt.runEna
    #     ld(rg.F_Ld_Run_Ctl, runCtl, 1)

    if not ctlEna:
        readData()

    if syncEnc:
        axisCtl = bt.ctlStart | bt.ctlDir
        ld(base + rg.F_Ld_Axis_Ctl, axisCtl, 1);
    else:
        axisCtl = bt.ctlStart | bt.ctlChDirect | bt.ctlDir
        ld(base + rg.F_Ld_Axis_Ctl, axisCtl, 1);

    if ctlEna and runClocks != 0:
        ldSend()
        runCtl = bt.runEna
        ld(rg.F_Ld_Run_Ctl, runCtl, 1)
        while True:
            status = rd(rg.F_Rd_Status, 4)
            if (status & bt.queEmpty) != 0:
                break
            print("status {0:04b}".format(status))
        runCtl = 0
        ld(rg.F_Ld_Run_Ctl, runCtl, 1)

    status = rd(rg.F_Rd_Status, 4)
    print("status {0:04b}".format(status))
              
    readData()
    if ctlEna and runClocks != 0:
        rdSetup()
        rdTest()

    indexClks = rd(rg.F_Rd_Idx_Clks, 4)
    if indexClks != 0:
        curRPM = int(round((float(cFreq) / (indexClks + 1)) * 60))
        print("indexClks %d curRPM %d" % (indexClks, curRPM))
    
    doneFlag = bt.zAxisDone if Z_AXIS else bt.xAxisDone
    print("doneFlag %x" % (doneFlag))
    stepData = []
    if runClocks != 0:
        if runClocks == 0:
            runClocks = 1

        ld(rg.F_Dbg_Freq_Base + rg.F_Ld_Dbg_Freq, freqDivider, 2)
        ld(rg.F_Dbg_Freq_Base + rg.F_Ld_Dbg_Count, runClocks, 4)

        clkReg = bt.zClkDbgFreq if Z_AXIS else bt.xClkDbgFreq
        ld(rg.F_Ld_Clk_Ctl, clkReg, 1);
        clkReg |= bt.clkDbgFreqEna
        ld(rg.F_Ld_Clk_Ctl, clkReg, 1);

        if runClocks > 1:
            sleep(.25)
            readData()
            # if dbgprint:
            #     print("\nresults %d clocks %d" % (runClocks, xPos))

        if stepClocks != 0:
            for i in range(stepClocks):
                if i == 0:
                    print()
                readData(i)
                stepData.append((xPos, zSum, zAclSum))
                status = rd(rg.F_Rd_Status, 4)
                if (status & doneFlag) != 0:
                    break
                ld(rg.F_Dbg_Freq_Base + rg.F_Ld_Dbg_Count, 1, 4, False)
            print()
    else:
        print("sync %s syncEnc %s" % (str(sync), str(syncEnc)))
        if sync:
            if syncEnc:
                clkReg = bt.zClkCh if Z_AXIS else bt.xClkCh
            else:
                print("using sync")
                clkReg = (bt.zClkIntClk | bt.xClkCh) if Z_AXIS else \
                    (bt.xClkIntClk | bt.zClkCh)
                ld(rg.F_Enc_Base + rg.F_Ld_Enc_Cycle, encCycle ,2)
                ld(rg.F_Enc_Base + rg.F_Ld_Int_Cycle, intCycle ,2)
                ld(rg.F_Ld_Sync_Ctl, bt.synEncInit, 1)
                status = rd(rg.F_Rd_Status, 4)
                print("status {0:07b}".format(status))
                ld(rg.F_Ld_Sync_Ctl, bt.synEncEna, 1)
                while True:
                    status = rd(rg.F_Rd_Status, 4)
                    # print("status {0:07b}".format(status))
                    if (status & bt.syncActive) != 0:
                        print("status {0:07b}".format(status))
                        break
                    sleep(0.1)
                clks = rd(rg.F_Enc_Base + rg.F_Rd_Cmp_Cyc_Clks, 4)
                print("cycleClocks %d", clks)
        else:
            ld(base + rg.F_Ld_Freq, freqDivider, 2)
            clkReg = bt.zClkZFreq if Z_AXIS else bt.xClkXFreq
        ld(rg.F_Ld_Clk_Ctl, clkReg, 1);

        if ctlEna:
            cmd = cmdWaitZ if Z_AXIS else cmdWaitX
            ldCmd(cmd)
            axisCtl = 0
            ld(base + rg.F_Ld_Axis_Ctl, axisCtl, 1);
            ldSend()
            runCtl = bt.runEna
            ld(rg.F_Ld_Run_Ctl, runCtl, 1)
            while True:
                status = rd(rg.F_Rd_Status, 4)
                if (status & bt.queEmpty) != 0:
                    break
                sleep(0.1)
            print("status {0:04b}".format(status))
            runCtl = 0
            ld(rg.F_Ld_Run_Ctl, runCtl, 1)
        else:
            while True:
                status = rd(rg.F_Rd_Status, 4) 
                if (status & doneFlag) != 0:
                    break
                sleep(0.1)
            print("status {0:04b}".format(status))
        readData()

    status = rd(rg.F_Rd_Status, 4)
    print("status {0:04b}".format(status))

    axisCtl = bt.ctlInit
    ld(base + rg.F_Ld_Axis_Ctl, axisCtl, 1);
    axisCtl = 0
    ld(base + rg.F_Ld_Axis_Ctl, axisCtl, 1);

    status = rd(rg.F_Rd_Status, 4)
    print("status {0:04b}".format(status))

    x = 0
    y = 0
    clocks = 0
    stepClocks = len(stepData)
    if stepClocks != 0:
        tracePos = stepData[0][0]
    else:
        tracePos = xPos + 1
    # synSum = d
    synSum = 0
    accelAccum = 0
    distCtr = dist
    l0 = dist
    aclStep = 0
    aclCtr = accelClocks-1
    index = 0
    decel = False
    delayDecel = False
    if False:
        while (clocks < xPos):
            clocks += 1
            x += 1
            if aclCtr > 0:
                aclCtr -= 1
            if (synSum < 0):
                synSum += incr1
            else:
                y += 1
                synSum += incr2
                distCtr -= 1
                if (not decel) and (aclCtr > 0):
                    aclStep += 1
                if aclStep >= distCtr:
                    aclCtr = accelClocks-1
                    decel = True
            synSum += accelAccum

            if (not delayDecel) and (clocks <= accelClocks):
                accelAccum += zSynAccel

            if delayDecel:
                if (accelAccum > 0):
                    accelAccum -= zSynAccel

            if clocks >= tracePos:
                print("%4d" % (index), end=" ")
                print("xPos %7d yPos %5d zSum %10d" % (x, y, synSum), end=" ")
                print("aclSum %8d aclCtr %8d" % (accelAccum, aclCtr), end=" ")
                print("dist %5d aclStp %6d" % (distCtr, aclStep), end=" ")
                (pos, zSum, zAclSum) = stepData[index]
                print("sDiff %6d aDiff %6d" % \
                      (synSum - zSum, accelAccum - zAclSum))
                index += 1

            if (distCtr == 0):
                break

            delayDecel = decel
    else:
        f = open("run.txt", "w")
        if f is not None:
            f.write("cFreq %d mult %d stepsRev %d pitch %5.2f\n" % \
                    (cFreq, mult, stepsRev, pitch))
            f.write("minFeed %4.1f maxFeed %4.1f accelRate %4.1f\n" % \
                    (minFeed, maxFeed, accelRate))
            f.write("\nstepsSecMin %6.0f freqGenMin %7.0f\n" % \
                    (stepsSecMin, freqGenMin))
            f.write("stepsSecMax %6.0f freqGenMax %7.0f\n" % \
                    (stepsSecMax, freqGenMax))
            f.write("freqDivider %3.0f\n" % freqDivider)
            f.write("accelTime %8.6f clocks %d\n" % (accelTime, accelClocks))
            f.write("\ndyIni %d dyMax %d dyDelta %d incPerClock %4.2f "
                    "zSynAccel %d\n" %\
                    (dyIni, dyMax, dyDeltaC, incPerClock, zSynAccel))
            f.write(("\ndx %d dy %d incr1 %d incr2 %d d %d bits %d scale %d\n" %
                     (dx, dyIni, incr1, incr2, d, bits, scale)))
            f.write(("accelClocks %d totalSum %d totalInc %d accelSteps %d\n" % 
                     (accelClocks, totalSum, totalInc, accelSteps)))
            f.write("\n")

            header = "     x    y       zSum   aclsum aCtr dist aStp\n"
            f.write(header)
            f.write("%6d %4d %10d " % (x, y, synSum))
            f.write("%8d %4d " % (accelAccum, aclCtr))
            f.write("%4d %4d *\n" % (distCtr, aclStep))
            hdrCount = 0
        lastY = 0
        lastX = 0
        while (clocks < xPos):
            clocks += 1
            x += 1
            if not decel:
                if aclCtr != 0:
                    aclCtr -= 1
            else:
                if aclCtr != accelClocks-1:
                    aclCtr += 1
            if (synSum < 0):
                synSum += incr1
            else:
                y += 1
                synSum += incr2
                distCtr -= 1
                if (not decel) and (aclCtr > 0):
                    aclStep += 1
                if decel:
                    aclStep -= 1
                if not decel and aclStep > distCtr:
                    decel = True
            synSum += accelAccum

            if (not delayDecel) and (clocks <= accelClocks):
                accelAccum += zSynAccel

            if delayDecel:
                if (accelAccum > zSynAccel):
                    accelAccum -= zSynAccel

            if f is not None:
                hdrCount += 1
                if hdrCount == 40:
                    f.write(header)
                    hdrCount = 0
                f.write("%6d %4d %10d " % (x, y, synSum))
                f.write("%8d %4d " % (accelAccum, aclCtr))
                f.write("%4d %4d" % (distCtr, aclStep))
                if y != lastY:
                    f.write(" *%s%4d" % ("><"[decel], x - lastX))
                    lastX = x
                    lastY = y
                f.write("\n")

            if clocks >= tracePos:
                print("%4d" % (index), end=" ")
                print("xPos %7d yPos %5d zSum %10d" % (x, y, synSum), end=" ")
                print("aclSum %8d aclCtr %8d" % (accelAccum, aclCtr), end=" ")
                print("dist %5d aclStp %6d" % (distCtr, aclStep), end=" ")
                (pos, zSum, zAclSum) = stepData[index]
                print("sDiff %6d aDiff %6d" % \
                      (synSum - zSum, accelAccum - zAclSum))
                index += 1

            if (distCtr == 0):
                break

            delayDecel = decel

    print(("\nx %d y %d sum %d delta %d accelAccum %d delta %d" %
           (x, y, synSum, synSum - zSum, accelAccum, accelAccum - zAclSum)))
    if f is not None:
        f.close()

    if pData:
        plot(time, data, 'b', aa="true")
        grid(True)
        show()

print("starting")

arg1 = None
arg2 = None
arg3 = None
if len(sys.argv) > 1:
    if sys.argv[1] == '1':
        ctlEna = True
    
if len(sys.argv) > 2:
    try:
        arg1 = int(sys.argv[2])
    except ValueError:
        arg1 = sys.argv[2]

if len(sys.argv) > 3:
    try:
        arg2 = int(sys.argv[3])
    except ValueError:
        arg2 = sys.argv[3]

if len(sys.argv) > 4:
    try:
        arg3 = int(sys.argv[4])
    except ValueError:
        arg3 = sys.argv[4]

print("ctlEna %s" % (ctlEna))

if arg1 is None:
    test3()
elif arg2 is None:
    test3(runClocks=arg1)
elif arg3 is None:
    test3(runClocks=arg1, dist=arg2)
else:
    test3(runClocks=arg1, dist=arg2, stepClocks=arg3)
