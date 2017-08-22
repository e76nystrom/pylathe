#!/cygdrive/c/Python27/Python.exe

class Test():
    def __init__(self):
        print(hasattr(self, self.t1))
        print(callable(self, self.t1))

    def t1(self):
        pass

a = Test()

h = -0.005
xInc = -0.0025
lastX = 10
for i in range(20):
    x = i * xInc
    diff = x - lastX
    print("x %7.4f lastX %7.4f diff %7.4f" % (x, lastX, diff))
    if diff > h:
        x = lastX + h
        print("x %7.4f" % (x))
    lastX = x
