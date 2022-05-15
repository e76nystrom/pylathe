#!/cygdrive/c/Python27/Python.exe

import csv
import sys
from operator import itemgetter

file = sys.argv[1]
print(file)

rev = False
if file == "pinsD.csv":
    pins = 50
    rev = True
elif file == "pinsL.csv":
    pins = 50
elif file == "pinsN.csv":
    pins = 38
elif file == "pinsX0.csv":
    pins = 38

f = open(sys.argv[1], "r")
tmp = f.read(3)
if tmp != "\xEF\xBB\xBF":
    print("no byte order mark at file start\n");
    sys.exit()
csv = csv.reader(f, delimiter=',', quotechar='"')
left = [None for i in range(pins)]
right = [None for i in range(pins)]
for row in csv:
    (con, tmp, pin, type, signal, label) = row[0:6]
    if pin.startswith('P'):
        if '-' in pin:
            pin = pin.split('-')[0]
        pin = pin.strip()
        if len(pin) == 3:
            pin = pin[:2] + '0' + pin[2:]
        if len(con) < 3:
            continue
        if con[0] == "*":
            continue
        conPin = int(con[1:3]) - 1
        if con[0] == "L":
            left[conPin] = (pin, label)
        else:
            right[conPin] = (pin, label)
# for row in left:
#     print(row)

for i in range(0, pins, 2):
    pinO = ""
    labelO = ""
    if left[i] is not None:
        (pinO, labelO) = left[i]
    pinE = ""
    labelE = ""
    if left[i+1] is not None:
        (pinE, labelE) = left[i+1]
    lCol = ("%8s %-4s %2d | %2d %-4s %-8s" % \
            (labelO, pinO, i+1, i+2, pinE, labelE))

    if rev:
        j = (pins - 2) - i
    else:
        j = i
    pinO = ""
    labelO = ""
    if right[j] is not None:
        (pinO, labelO) = right[j]
    pinE = ""
    labelE = ""
    if right[j+1] is not None:
        (pinE, labelE) = right[j+1]

    if rev:
        rCol = ("%8s %-4s %2d | %2d %-4s %-8s" % \
                (labelE, pinE, j+2, j+1, pinO, labelO))
    else:
        rCol = ("%8s %-4s %2d | %2d %-4s %-8s" % \
                (labelO, pinO, j+1, j+2, pinE, labelE))

    print("%-35s %-35s" % (lCol, rCol))
