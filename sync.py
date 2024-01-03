#!/cygdrive/c/Python310/python

import math
from sys import stdout

class Sync():
    def __init__(self, maxPrime=127, dbg=True, fpga=False):
        self.calcPrimes(maxPrime)
        self.clockFreq = 72000000
        self.encoderPulse = 1600
        self.metricLeadscrew = True
        self.leadscrewTPI = 8
        self.leadscrewPitch = 5
        self.metricPitch = True
        self.motorSteps = 200
        self.microSteps = 8
        self.exitRevs = 1
        self.dist = False
        self.turn = False
        self.dbg = dbg
        self.fpga = fpga

    def setClockFreq(self, freq):
        self.clockFreq = freq
        
    def setEncoder(self, encoder):
        self.encoderPulse = encoder

    def setDist(self, dist):
        self.dist = dist

    def setTurn(self, turn):
        self.turn = turn

    def setLeadscrew(self, val):
        self.metricLeadscrew = False
        if type(val) is str:
            val = val.lower()
            self.metricLeadscrew = val.endswith('mm')
            if self.metricLeadscrew:
                val = val[:-2]
                self.leadscrewPitch = float(val)
                self.leadscrewTPI = 1
            else:
                val = float(val)
        if not self.metricLeadscrew:
            num = 1
            while int(val) != val:
                val *= 10
                num *= 10
            d = self.factor(int(val))
            n = self.factor(num)
            (n, d) = self.remFactors(n, d)
            val = 1
            for i in n:
                val *= i
            self.leadscrewTPI = val
            val = 1
            for i in d:
                val *= i
            self.leadscrewPitch = val

    def setMotorSteps(self, steps):
        self.motorSteps = steps

    def setMicroSteps(self, steps):
        self.microSteps = steps

    def setExitRevs(self, rev):
        self.exitRevs = rev

    def calcSync(self, syncVal, dbg=None, metric=False, rpm=None,
                 dist=None, turn=None):
        if self.dbg:
            print("calcSync syncVal %s metric %s rpm %s" %
                  (syncVal, metric, rpm))
            print("clockFreq %d encoder %d" %
                  (self.clockFreq, self.encoderPulse))
        pitch = 0
        tpi   = 0
        inPreScaler = 1
        outPreScaler = 1
        scale = 1
        sFactors = []
        iFactors = []
        dbgSave = None
        distSave = None
        turnSave = None
        if dbg is not None:
            dbgSave = self.dbg
            self.dbg = dbg
        if dist is not None:
            distSave = self.dist
            self.dist = dist
        if turn is not None:
            turnSave = self.turn
            self.turn = turn

        if type(syncVal) is str:
            syncVal = syncVal.lower()
            metric =  syncVal.endswith("mm")
            if metric:
                syncVal = syncVal[:-2]
            syncVal = float(syncVal)

        if metric:
            if self.dbg:
                print("metric")
            pitch = syncVal
            if self.metricLeadscrew:
                nFactor = 1
                dFactor = 1
            else:
                nFactor = 127
                dFactor = 5
        else:
            if self.dbg:
                print("tpi")
            tpi = syncVal
            if self.metricLeadscrew:
                nFactor = 5
                if not self.turn:
                    dFactor = 127
                else:
                    dFactor = 128
            else:
                nFactor = 1
                dFactor = 1

        if self.turn:
            if self.dbg:
                print("turn")
            pitch = syncVal
            count = 0
            while int(pitch) != pitch:
                pitch *= 10
                nFactor *= 10
                count += 1
                if count >= 4:
                    break
            pitch = int(pitch)
            # pitch = int(math.ceil(pitch / 10) * 10)
        
            num = \
                  ( \
                    (nFactor, "nfactor"), \
                    (self.encoderPulse, "encoderPulse"), \
                    (self.leadscrewPitch, "leadscrewPitch"), \
                  )

            denom = \
                    ( \
                      (dFactor, "dFactor"), \
                      (pitch, "pitch"), \
                      (self.motorSteps, "motorSteps"), \
                      (self.microSteps, "microSteps"), \
                      (self.leadscrewTPI, "leadscrewTPI"), \
                    )
        elif self.dist:
            if self.dbg:
                print("distance")
            exitDist = syncVal

            #=exitDist*motorSteps*microSteps*127/(metricPitch*5)
            stepsInch = float(self.motorSteps * self.microSteps * \
                                dFactor) / (self.leadscrewPitch * nFactor)
            xSteps = exitDist * stepsInch
            xStepsInt = int(math.ceil(xSteps / 10) * 10)

            encoderPulse = self.exitRevs * self.encoderPulse

            if self.dbg:
                print("stepsInch %d exitDist %0.4f xSteps %0.2f %0.4f "\
                      "xStepsInt %d %0.4f" % \
                      (int(stepsInch), exitDist, xSteps, xSteps / stepsInch,
                       xStepsInt, float(xStepsInt / stepsInch)))
                print("encoderRev %d exitRevs %0.2f encoderPulse %d\n" % \
                      (self.encoderPulse, self.exitRevs, int(encoderPulse)))
                stdout.flush()

            num = \
                    ( \
                      (encoderPulse, "encoderPulse"), \
                    )

            denom = \
                    ( \
                      (xStepsInt, "xStepsInt"), \
                    )
        else:
            if metric:
                if self.dbg:
                    print("metric")
                while int(pitch) != pitch:
                    pitch *= 10
                    nFactor *= 10
                    pitch = int(pitch)
        
                num = \
                      ( \
                        (nFactor, "nfactor"), \
                        (self.encoderPulse, "encoderPulse"), \
                        (self.leadscrewPitch, "leadscrewPitch"), \
                      )

                denom = \
                        ( \
                          (dFactor, "dFactor"), \
                          (pitch, "pitch"), \
                          (self.motorSteps, "motorSteps"), \
                          (self.microSteps, "microSteps"), \
                          (self.leadscrewTPI, "leadscrewTPI"), \
                        )
            else:                   # tpi lead
                if self.dbg:
                    print("tpi")
                while int(tpi) != tpi:
                    tpi *= 10
                    dFactor *= 10
                tpi = int(tpi)

                num = \
                      ( \
                        (nFactor, "nfactor"), \
                        (self.encoderPulse, "encoderPulse"), \
                        (tpi, "tpi"), \
                        (self.leadscrewPitch, "leadscrewPitch"), \
                      )

                denom = \
                        ( \
                          (dFactor, "dFactor"), \
                          (self.motorSteps, "motorSteps"), \
                          (self.microSteps, "microSteps"), \
                        )

        if self.dbg:
            print("numerator")
        nFactors = []
        for (n, name) in num:
            if n <= 1:
                continue
            if self.dbg:
                print("factor %-14s %5d -" % (name, n), end = " ")
            result = self.factor(n)
            if len(result) != 0:
                nFactors += result
                if self.dbg:
                    for j in result:
                        print(j, end=' ')
            if self.dbg:
                print()
        if self.dbg:
            print()

        if self.dbg:
            print("denominator")
        dFactors = []
        for (n, name) in denom:
            if n == 1:
                continue
            if self.dbg:
                print("factor %-14s %5d -" % (name, n), end = " ")
            result = self.factor(n)
            if len(result) != 0:
                dFactors += result
                if self.dbg:
                    for j in result:
                        print(j, end=' ')
            if self.dbg:
                print()
        if self.dbg:
            print()
            stdout.flush()

        nFactors.sort()
        dFactors.sort()
        (nFactors, dResult) = self.remFactors(nFactors, dFactors)

        cycle = math.prod(nFactors)
        output = math.prod(dResult)

        while cycle < 16:
            cycle *= 2
            nFactors.insert(0, 2)
            output *= 2
            dResult.insert(0,2)

        if not self.fpga:
            result = [cycle, output]

            if rpm is not None:
                encPerSec = (rpm * self.encoderPulse) / 60.0
                clockPerEncPulse = self.clockFreq / encPerSec
                inPreScaler = math.ceil(clockPerEncPulse / 49152)
                result.append(inPreScaler)
                clockPerCycle = clockPerEncPulse * cycle
                outClockPerPulse = clockPerCycle / output
                # clocksMin = self.clockFreq * 60
                # pulseMinIn = self.encoderPulse * rpm
                # pulseMinOut = (pulseMinIn * output) / cycle
                # clocksPulse = int(clocksMin / pulseMinOut)
                if not self.fpga:
                    outPreScaler = math.ceil(outClockPerPulse / 49152)
                else:
                    outPreScaler = 1
                result.append(outPreScaler)
        else:
            if rpm is not None:
                encPerSec = (rpm * self.encoderPulse) / 60.0
                encPeriodUSec = 1_000_000 / encPerSec
                clockPerEncPulse = self.clockFreq / encPerSec
                clockPerCycle = clockPerEncPulse * cycle
                clockPerOutPulse = clockPerCycle / output
                cyclePeriodMSec = (clockPerCycle * 1000) / self.clockFreq
                if self.dbg:
                    bits = int(math.ceil(math.log2(clockPerCycle)))
                    print(f"encPeriodUSec {encPeriodUSec:.0f}" \
                          f" cyclePeriodMSec {cyclePeriodMSec:.1f}" \
                          f" clockPerCycle {clockPerCycle:,.0f}" \
                          f" bitCount {bits:d}")

                    bitsIn = int(math.ceil(math.log2(clockPerEncPulse)))
                    bitsOut = int(math.ceil(math.log2(clockPerOutPulse)))
                    print(f"clockPerInpPulse {clockPerEncPulse:,.0f} {bitsIn:d} bits" \
                          f" clockPerOutPulse {clockPerOutPulse:,.0f} {bitsOut:d} bits")
            nFactors.sort()

            count = len(nFactors)
            maxVal = (1 << count)
            minVal = math.prod(nFactors) - output
            sel = [0 for j in range(count)]
            r = []
            for i in range(maxVal):
                mask = 1
                for j in range(count):
                    sel[j] = 1 if (mask & i) != 0 else 0
                    mask <<= 1
                factors = [a * b for a,b in zip(sel, nFactors)]
                value = 1
                for j in factors:
                    if j != 0:
                        value *= j
                delta = value - output
                if delta > 0:
                    if delta < minVal:
                        minVal = delta
                        r = sel.copy()
                # print(sel, f"{i:08b}", factors,
                #       f"{value:4d} {delta:4d} {minVal:4d}", r)
            scale = 1
            sFactors = []
            if len(r) != 0:
                factors = []
                for r, f in zip(r, nFactors):
                    if r != 0:
                        factors.append(f)
                    else:
                        sFactors.append(f)
                        scale *= f
                cycle = math.prod(factors)
                iFactors = nFactors.copy()
                nFactors = factors
                
            if self.dbg:
                print(f"scale {scale:d} cycle {cycle:d} output {output:d}")
            result = (cycle, output, scale)

        if self.dbg:
            if self.fpga and scale != 1:
                print("cycle  %4d - " % (math.prod(iFactors)), end="")
                for n in iFactors:
                    print(n, end=' ')
                print()

                print("scale  %4d - " % (scale), end="")
                for n in sFactors:
                    print(n, end=' ')
                print()

            print("cycle  %4d - " % (cycle), end='')
            for n in nFactors:
                print(n, end=' ')
            print()

            print("output %4d - " % (output), end='')
            for d in dResult:
                print(d, end=' ')
            print()

            if not self.fpga and rpm is not None:
                print("inPrescaler %d outPreScaler %d" % \
                (inPreScaler, outPreScaler))

            print()
            stdout.flush()

        if dbgSave is not None:
            self.dbg = dbgSave
        if distSave is not None:
            self.dist = distSave
        if turnSave is not None:
            self.turn = turnSave

        return(result)

    def remFactors(self, nFactors, dFactors):
        # print("remove common factors")
        if self.dbg:
            print("nFactors", nFactors)
            print("dFactors", dFactors)
        dResult = []
        for d in dFactors:
            found = False
            # print("d %d" % (d))
            for (i, n) in enumerate(nFactors):
                if d == n:
                    # print("found %d at %d\n" % (d, i))
                    del nFactors[i]
                    found = True
                    break
            if not found:
                dResult.append(d)
        return(nFactors, dResult)

    def calcPrimes(self, maxPrime):
        maxPrime += 1
        sieve = [True] * maxPrime
        sieve[0] = False
        sieve[1] = False

        for i in range(2, int(math.sqrt(maxPrime)) + 1):
            index = i * 2
            while index < maxPrime:
                sieve[index] = False
                index += i

        primes = []
        for i in range(maxPrime):
            if sieve[i]:
                primes.append(i)
        self.primes = primes

    def factor(self, n):
        factors = []
        for i in self.primes:
            while n % i == 0:
                factors.append(i)
                n /= i
        return(factors)

# ./sync.py -d -e 8000 -r 100 -l 5mm -s 200 -m 10 -f 50000000 -t -F -R 1 .125

if __name__ == '__main__':
    from sys import argv, exit

    def help():
        print("Usage: sync [options] val[mm]")
        print(" ?        help\n" \
              " -d       debug\n" \
              " -e n     encoder\n" \
              " -r n     rpm\n" \
              " -l n[mm] leadscrew \n" \
              " -s n     motor steps\n" \
              " -m n     micro steps\n" \
              " -f n     clock frequency\n" \
              " -t       turn\n" \
              " -D       distance\n" \
              " -F       fpga" \
              " -R val   exit revolutions\n" \
              )
        exit()
        
    argLen = len(argv)

    sync = Sync()

    thread = None
    rpm = None
    argDbg = False
    n = 1
    while True:
        if n >= argLen:
            break
        val = argv[n]
        if val.startswith('-'):
            tmp = val[1]
            if tmp == "e":
                n += 1
                if n < argLen:
                    sync.setEncoder(int(argv[n]))
            elif tmp == "r":
                n += 1
                if n < argLen:
                    rpm = int(argv[n])
            elif tmp == "l":
                n += 1
                if n < argLen:
                    sync.setLeadscrew(argv[n])
            elif tmp == 'm':
                n += 1
                if n < argLen:
                    sync.setMicroSteps(int(argv[n]))
            elif tmp == 's':
                n += 1
                if n < argLen:
                    sync.setMotorSteps(int(argv[n]))
            elif tmp == 'f':
                n += 1
                if n < argLen:
                    sync.setClockFreq(int(argv[n]))
            elif tmp == 't':
                sync.turn = True
            elif tmp == 'D':
                sync.dist = True
            elif tmp == 'F':
                sync.fpga = True
            elif tmp == 'R':
                n += 1
                if n < argLen:
                    sync.setExitRevs(float(argv[n]))
            elif tmp == 'd':
                argDbg = True
            elif tmp == 'h':
                help()
            else:
                help()
        elif val == '?':
            help()
        else:
            thread = val
        n += 1

    if thread is None:
        help()
    else:
        result = sync.calcSync(thread, dbg=argDbg, rpm=rpm)

        print("cycle %d " % result[0], end='')
        print("output %d " % result[1], end='')
        if rpm is not None:
            print("preScaler %d " % result[2], end='')
        print()
