#!/cygdrive/c/Python37/Python.exe

from math import pi, sin, sqrt

xStepsInch = 8192
zStepsInch = 8192

radius = 0.125
xRadius = radius * xStepsInch
xRadiusSqrd = xRadius * xRadius

xSteps = radius * sin(pi / 4) * xStepsInch
for x in range(int(xSteps) + 1):
    z = round((sqrt(xRadiusSqrd - x * x) * zStepsInch) / xStepsInch)
    print("x %4d z %4d" % (x, z))

