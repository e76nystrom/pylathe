#!/cygdrive/c/Python27/Python.exe

h = 0.005
xInc = -0.025
xLast = 10
for i in range(20):
    x = i * xInc
    diff = abs(x - xLast)
    if diff < h:
        x = xLast - h
        print("x")
    print("x %7.4f xLast %7.4f diff %7.4f" % (x, xLast, diff))
    xLast = x
