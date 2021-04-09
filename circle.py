#!/cygdrive/c/Python37/Python.exe

from sys import argv
from math import cos, pi, radians, sin, sqrt
import ctlBitDef as ct

def move(cmd, rpt):
    global steps, xDir, zDir, xPos, zPos
    mvTrace = []
    if (cmd & ct.PCMD_RPT_MASK) != 0:
        rpt = cmd >> ct.PCMD_RPT_SHIFT
    cmd &= ct.PCMD_CMD_MASK
    if cmd == ct.PCMD_INCX_HLDZ_S1:		# 0
        steps += rpt
        while True:
            mvTrace.append((xPos, zPos))
            xPos += xDir
            rpt -= 1
            if rpt == 0:
                zPos += zDir
                break
    elif cmd == ct.PCMD_INCX_HLDZ_SN:		# 1
        steps += rpt
        count = 0
        while count < rpt:
            mvTrace.append((xPos, zPos))
            xPos += xDir
            if count > 0:
                zPos += zDir
            count += 1
    elif cmd == ct.PCMD_HLDX_S1_INCZ:		# 2
        steps += rpt
        while True:
            mvTrace.append((xPos, zPos))
            rpt -= 1
            zPos += zDir
            if rpt == 0:
                xPos += xDir
                break
    elif cmd == ct.PCMD_HLDX_SN_INCZ:		# 3
        steps += rpt
        count = 0
        while count < rpt:
            mvTrace.append((xPos, zPos))
            zPos += zDir
            if count > 0:
                xPos += xDir
            count += 1
    elif cmd == ct.PCMD_INCX2_INCZ:		# 4
        steps += rpt
        while True:
            mvTrace.append((xPos, zPos))
            zPos += zDir
            rpt -= 1
            if rpt <= 1:
                xPos += xDir
            if rpt == 0:
                break
    elif cmd == ct.PCMD_SET_DIR:		# 7
        xDir = 1 if (rpt & ct.PCMD_X_NEG) == 0 else -1
        zDir = 1 if (rpt & ct.PCMD_Z_NEG) == 0 else -1
        return None
    return mvTrace

def arcTest():
    global delta, lastDelta, xChange, zChange, rpt, cmd, cmdX, cmdZ
    global history, mvTrace
    global x, z, xPos, zPos
    global cmdSave
    trace = (mvTrace is not None) and (len(mvTrace) > 0)
    if trace:
        (xTmp, zTmp) = mvTrace[0]
        if (cmdX != xTmp) or (cmdZ != zTmp):
            print("%5d x %5d%s z %5d " % (count, cmdX, x45, cmdZ), end="")
            print("%5d %5d+ %2d %2d" % (xTmp, zTmp, cmdX - xTmp, cmdZ - zTmp))

            if cmdSave is not None:
                (count0, cmdX0, x450, cmdZ0, xTmp0, zTmp0, delta0, \
                 lastDelta0, xChange0, zChange0, cmd0, rpt0) = cmdSave
                print("%5d x %5d%s z %5d " % \
                      (count0, cmdX0, x450, cmdZ0), end="")
                print("%5d %5d*" % (xTmp0, zTmp0), end="")
                print("delta %4d %4s xChg %3d zChg %3d rpt %3d "\
                      "cmd %d %2x\n" % \
                (delta0, str(lastDelta0), xChange0, zChange0, rpt0, \
                 cmd0 & ct.PCMD_CMD_MASK, cmd0))
            xPos = x
            zPos = z

    print("%5d x %5d%s z %5d " % (count, cmdX, x45, cmdZ), end="")
    if trace:
        print("%5d %5d " % mvTrace[0], end="")
    print("delta %4d %4s xChg %3d zChg %3d rpt %3d cmd %d %2x" % \
          (delta, str(lastDelta), xChange, zChange, rpt, \
           cmd & ct.PCMD_CMD_MASK, cmd))

    if trace:
        cmdSave = (count, cmdX, x45, cmdZ, xTmp, zTmp, delta, lastDelta,
                   xChange, zChange, cmd, rpt)
    else:
        cmdSave = None

    historyLen = len(history)
    if historyLen > 1:
        for i in range(1, historyLen):
            print("      x %5d  z %5d" % history[i][:2], end="")
            if (mvTrace is not None) and (len(mvTrace) > 1):
                print(" %5d %5d" % mvTrace[i], end="")
            (delta, lastDelta) = history[i][2:]
            print(" delta %4d %4s" % (delta, str(lastDelta)))

    history = []

#       x-
#     \5|6/
#     4\|/7
# z- ------- z+
#     3/|\0
#     /2|1\
#       x+

def octantStart(x, z):
    global xStep45
    if x >= 0:
        if z > 0:
            return 0 if x < xStep45 else 1
        else:
            return (4 if x == 0 else 3) if x <= xStep45 else 2
    else:
        x = -x
        if z >= 0:
            return 7 if x <= xStep45 else 6
        else:
            return 4 if x < xStep45 else 5

def octantEnd(x, z):
    global xStep45
    if x >= 0:
        if z >= 0:
            return 0 if x <= xStep45 else 1
        else:
            return 3 if x < xStep45 else 2
    else:
        x = -x
        if z > 0:
            return 7 if x < xStep45 else 6
        else:
            return 4 if x <= xStep45 else 5

cwOctDir = (ct.PCMD_Z_NEG, ct.PCMD_Z_NEG, \
            ct.PCMD_X_NEG | ct.PCMD_Z_NEG, ct.PCMD_X_NEG | ct.PCMD_Z_NEG)
cwOctInc = ((1, -1), (1, -1), (-1, -1), (-1, -1))

ccwOctDir = (ct.PCMD_X_NEG, ct.PCMD_X_NEG, 0, 0)
ccwOctInc = ((-1, 1), (-1, 1), (1, 1), (1, 1))

def updOctant():
    global octant, octEnd, endCheck, lessThan45
    global cwOctDir, cwOctInc
    global inXDir, inZDir
    if octant == octEnd:
        endCheck = True
    lessThan45 = (octant == 0) or (octant == 3)
    if cwDir:
        cmd = cwOctDir[octant]
        (inXDir, inZDir) = cwOctInc[octant]
    else:
        cmd = ccwOctDir[octant]
        (inXDir, inZDir) = ccwOctInc[octant]

    cmd = (ct.PCMD_SET_DIR | \
           ((ct.PCMD_DIR_FLAG | cmd) << ct.PCMD_RPT_SHIFT))
    move(cmd, 0)

    print("\noctant %d inxDir %d inZDir %d cmd %x\n" % \
          (octant, inXDir, inZDir, cmd))

def lrint(val):
    return(int(round(val)))

def polarToRect(center, radius, a):
    (cx, cz) = center
    a0 = radians(a)
    x = lrint(cx + radius * sin(a0) * xStepsInch)
    z = lrint(cz + radius * cos(a0) * zStepsInch)
    return (x, z)

xStepsInch = int((200 * 10 * 25.4) / 4) #8192
zStepsInch = int((200 * 10 * 25.4) / 5) #8192

print("xStepsInch %5d zStepsInch %5d" % (xStepsInch, zStepsInch))

radius = .125

xRadius = int(round(radius * xStepsInch))
xRadiusSqrd = xRadius * xRadius

zRadius = xRadius * zStepsInch // xStepsInch
zRadiusSqrd = zRadius * zRadius

print("radius %6.3f xRadius %5d xRadiusSqrd %10d "
"zRadius %5d zRadiusSqrd %5d" % \
      (radius, xRadius, xRadiusSqrd, zRadius, zRadiusSqrd))

if len(argv) < 3:
    angle0 = 0
    angle1 = 90
else:
    angle0 = float(argv[1])
    angle1 = float(argv[2])
    
center = (0, 0)
p0 = polarToRect(center, radius, angle0)
p1 = polarToRect(center, radius, angle1)

(x0, z0) = p0
(x1, z1) = p1

xStep45 = lrint(radius * (sqrt(2) / 2) * xStepsInch)
zStep45 = lrint(radius * (sqrt(2) / 2) * zStepsInch)

print("xStep45 %d zStep45 %d" % (xStep45, zStep45))

# for a in range(0, 360+1, 15):
#     (x, z) = polarToRect(center, radius, a)
#     oStart = octantStart(x, z)
#     oEnd = octantEnd(x, z)
#     print("a %3d x %5d z %5d o %d %d" % (a, x, z, oStart, oEnd))

cwDir = True

octStart = octantStart(x0, z0)
octEnd = octantEnd(x1, z1)

print("p0 (%5d, %5d) o %d p1 (%5d %5d) o %d" % \
(x0, z0, octStart, x1, z1, octEnd))

lessThan45 = x0 < xStep45
if x0 < xStep45:
    x = x0
else:
    z = z0
    
xEnd = x1
zEnd = z1

octant = octStart

xLast = x0
x = xLast
xNext = xLast
cmdX = xLast
xPos = xLast

zLast = z0
z = zLast
zNext = zLast
cmdZ = zLast
zPos = zLast

endCheck = False
delta = None
lastDelta = None

cmd = 0
rpt = 0

count = 0
oneByte = 0
history = []
steps = 0

cmdCount = [0, 0, 0, 0, 0, 0, 0, 0]

updOctant()

while True:
    if lessThan45:
        if endCheck:
            if inXDir > 0:
                if xNext > xEnd:
                    break
            else:
                if xNext < xEnd:
                    break
        x45 = " "
        zLast = z
        x = xNext
        z = (lrint(sqrt(xRadiusSqrd - x * x)) * zStepsInch) // xStepsInch
        if octant > 1:
            z = -z
        lastDelta = delta
        delta = z - zLast
        xNext += inXDir
    else:
        if endCheck:
            if inZDir < 0:
                if zNext < zEnd:
                    break
            else:
                if zNext > zEnd:
                    break
        x45 = ">"
        xLast = x
        z = zNext
        if z == 0:
            x = xRadius
        else:
            x = (lrint(sqrt(zRadiusSqrd - z * z)) * xStepsInch) // zStepsInch
        lastDelta = delta
        delta = x - xLast
        zNext += inZDir

    if (lastDelta is not None) and delta != lastDelta:
        xChange = abs(x - cmdX)
        zChange = abs(z - cmdZ)

        cmd = ct.PCMD_SPARE_0
        if zChange == 1:
            rpt = xChange
            cmd = ct.PCMD_INCX_HLDZ_S1	# 0
        elif xChange == (zChange + 1):
            rpt = xChange
            cmd = ct.PCMD_INCX_HLDZ_SN	# 1
        elif xChange == 1:
            rpt = zChange
            cmd = ct.PCMD_HLDX_S1_INCZ	# 2
        elif zChange == (xChange + 1):
            rpt = zChange
            cmd = ct.PCMD_HLDX_SN_INCZ	# 3
        elif xChange == 2:
            rpt = zChange
            cmd = ct.PCMD_INCX2_INCZ	# 4

        cmdCount[cmd] += 1

        if rpt < ct.PCMD_RPT_SHORT:
            oneByte += 1
            cmd |= rpt << ct.PCMD_RPT_SHIFT
        mvTrace = move(cmd, rpt)

        arcTest()
            
        cmdX = x
        cmdZ = z
        count += 1
        delta = None
        if cwDir:
            if octant == 0:
                if xNext > xStep45:
                    octant += 1
                    updOctant()
                    xLast = x
                    zNext = z + inZDir
                    print("xLast %5d zNext %5d\n" % (xLast, zNext))
            elif octant == 1:
                if zNext <= 0:
                    octant += 1
                    updOctant()
            elif octant == 2:
                if abs(zNext) >= zStep45:
                    octant += 1
                    updOctant()
                    zLast = z
                    xNext = x + inXDir
                    print("zLast %5d xNext %5d\n" % (zLast, xNext))
            else:
                pass
        else:
            pass
                
    history.append((x, z, delta, lastDelta))

print("%5d x %5d  z %5d %5d %5d" % \
       (count, x, z, xPos, zPos))
for i in range(len(cmdCount)):
    val = cmdCount[i]
    if val != 0:
        print("%d %4d" % (i, val))
print("commands %d bytes %d steps %d oneByte %d" % \
      (count, 2 * (count - oneByte) + oneByte, steps, oneByte))
