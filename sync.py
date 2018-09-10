#!/cygdrive/c/Python27/python

from __future__ import print_function
import math

class Sync():
    def __init__(self, maxPrime=127, dbg=False):
        self.calcPrimes(maxPrime)
        self.encoderPulse = 10160
        self.metricLeadscrew = True
        self.leadscrewTPI = 1
        self.leadscrewPitch = 5
        self.metricPitch = True
        self.motorSteps = 200
        self.microSteps = 8
        self.dbg = dbg

    def setEncoder(self, encoder):
        self.encoderPulse = encoder

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

    def calcSync(self, val, dbg=None, metric=False):
        dbgSave = None
        if dbg is not None:
            dbgSave = self.dbg
            self.dbg = dbg

        if type(val) is str:
            val = val.lower()
            if val.endswith("mm"):
                metric = True
                pitch = float(val[:-2])
            else:
                metric = False
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

            while int(pitch) != pitch:
                pitch *= 10
                nFactor *= 10
            pitch = int(pitch)
        
            num = \
                  (\
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
        else:
            if self.metricLeadscrew:
                nFactor = 5
                dFactor = 127
            else:
                nFactor = 1
                dFactor = 1

            while int(tpi) != tpi:
                tpi *= 10
                dFactor *= 10
            tpi = int(tpi)

            num = \
                  (\
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
            if n == 1:
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

        if self.dbg:
            print("cycle  %4d - " % (cycle), end='')
            for n in nFactors:
                print(n, end=' ')
            print()

            print("output %4d - " % (output), end='');
            for d in dResult:
                print(d, end=' ')
            print("\n")

        if dbgSave is not None:
            dbgSave = self.dbg

        return(cycle, output)

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
    from sys import argv

    argLen = len(argv)

    if argLen < 2:
        exit()

    sync = Sync()

    if argLen >= 3:
        sync.setEncoder(int(argv[2]))

    if argLen >= 4:
        sync.setLeadscrew(argv[3])

    result = sync.calcSync(argv[1], dbg=True)

    print("cycle %d output %d" % result)
