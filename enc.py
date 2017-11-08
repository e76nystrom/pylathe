#!/cygdrive/c/Python27/Python.exe

rpm = 60
pulsePerRev = 4000
clocksPerSecond = 45000000
print("rpm %d pulsePerRev %d clocksPerSecond %d" % \
      (rpm, pulsePerRev, clocksPerSecond))

pulsePerMin = pulsePerRev * rpm
pulsePerSec = pulsePerMin / 60
secPerPulse = 1.0 / pulsePerSec
clocksPerPulse = int(secPerPulse * clocksPerSecond)

print("pulsePerSec %d secPerPulse %8.6f clocksPerPulse %d" % \
      (pulsePerSec, secPerPulse, clocksPerPulse))

encCycLen = 21
intCycLen = 10

cyclePeriod = encCycLen * secPerPulse
clocksPerCycle = encCycLen * clocksPerPulse
print("encCycLen %d intCycLen %d cyclePeriod %8.6f clocksPerCycle %d" % \
      (encCycLen, intCycLen, cyclePeriod, clocksPerCycle))

intClocksPerPulse = int(clocksPerCycle / intCycLen)
print("intClocksPerCycle %d" % (intClocksPerPulse))

for i in range(encCycLen):
    clock = (i + 1) * clocksPerPulse
    print("%2d clock %19d" % (i, clock))

for i in range(intCycLen):
    clock = (i + 1) * intClocksPerPulse
    print("%2d clock %19d" % (i, clock))

encClocks = 0
encPulse = encCycLen
for i in range(encCycLen):
    encClocks += clocksPerPulse
    encPulse -= 1
    intClocks = (encClocks + clocksPerPulse * encPulse) / intCycLen
    print("%2d encPulse %2d intClocks %d" % (i, encPulse, intClocks))
    if encPulse <= 0:
        break;
