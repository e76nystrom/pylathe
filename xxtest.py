#!/cygdrive/c/Python27/Python.exe

h = -0.005
xInc = -0.0025
xLast = 10
for i in range(20):
    x = i * xInc
    diff = x - xLast
    print("x %7.4f xLast %7.4f diff %7.4f" % (x, xLast, diff))
    if diff > h:
        x = xLast + h
        print("x %7.4f" % (x))
    xLast = x
