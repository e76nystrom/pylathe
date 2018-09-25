#!/cygdrive/c/Python27/python

from __future__ import print_function
import math

class Sync():
    def __init__(self, maxPrime=127, dbg=False):
        self.calcPrimes(maxPrime)
        self.clockFreq = 72000000
        self.encoderPulse = 10160
        self.metricLeadscrew = True
        self.leadscrewTPI = 1
        self.leadscrewPitch = 5
        self.metricPitch = True
        self.motorSteps = 200
        self.microSteps = 8
        self.exitRevs = 1
        self.dist = False
        self.dbg = dbg

    def setClockFreq(self, freq):
        self.clockFreq = freq
        
    def setEncoder(self, encoder):
        self.encoderPulse = encoder

    def setDist(self, dist):
        self.dist = dist

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

    def calcSync(self, val, dbg=None, metric=False, rpm=None):
        dbgSave = None
        if dbg is not None:
            dbgSave = self.dbg
            self.dbg = dbg

        if type(val) is str:
            val = val.lower()
            metric =  val.endswith("mm")
            if metric:
                val = val[:-2]
                pitch = float(val)
            else:
                tpi = float(val)
        else:
            if metric:
                pitch = val
            else:
                tpi = val

        if metric:
            if self.metricLeadscrew:
                nFactor = 1
                dFactor = 1
            else:
                nFactor = 127
                dFactor = 5
        else:
            if self.metricLeadscrew:
                nFactor = 5
                dFactor = 127
            else:
                nFactor = 1
                dFactor = 1

        if self.dist:
            if metric:
                exitDist = pitch
            else:
                exitDist = tpi

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
                    for n in result:
                        print(n, end=' ')
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
                    for n in result:
                        print(n, end=' ')
            if self.dbg:
                print()
        if self.dbg:
            print()

        (nFactors, dResult) = self.remFactors(nFactors, dFactors)

        cycle = 1
        for n in nFactors:
            cycle *= n

        output = 1
        for d in dResult:
            output *= d

        result = [cycle, output]

        if rpm is not None:
            clocksMin = self.clockFreq * 60
            pulseMinIn = self.encoderPulse * rpm
            pulseMinOut = (pulseMinIn * output) / cycle
            clocksPulse = int(clocksMin / pulseMinOut)
            preScaler = clocksPulse >> 16
            if preScaler == 0:
                preScaler = 1
            result.append(preScaler)

        if self.dbg:
            print("cycle  %4d - " % (cycle), end='')
            for n in nFactors:
                print(n, end=' ')
            print()

            print("output %4d - " % (output), end='')
            for d in dResult:
                print(d, end=' ')
            print()
            
            if rpm is not None:
                print("preScaler %d" % (preScaler,))
            print()

        if dbgSave is not None:
            dbgSave = self.dbg

        return(result)

    def remFactors(self, nFactors, dFactors):
        # print("remove common factors")
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
            if sieve[i] == True:
                primes.append(i)
        self.primes = primes

    def factor(self, n):
        factors = []
        for i in self.primes:
            while n % i == 0:
                factors.append(i)
                n /= i
        return(factors)

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
              " -D val   distance\n" \
              " -R val   exit revolutions\n" \
              )
        exit()
        
    argLen = len(argv)

    sync = Sync()

    thread = None
    rpm = None
    dbg = False
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
            elif tmp == 'D':
                n += 1
                sync.dist = True
            elif tmp == 'R':
                n += 1
                if n < argLen:
                    sync.setExitRevs(float(argv[n]))
            elif tmp == 'd':
                dbg = True
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
        result = sync.calcSync(thread, dbg=dbg, rpm=rpm)

        print("cycle %d " % result[0], end='')
        print("output %d " % result[1], end='')
        if rpm is not None:
            print("preScaler %d " % result[2], end='')
        print()
