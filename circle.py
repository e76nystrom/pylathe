#!/cygdrive/c/Python37/Python.exe

from math import pi, sin, sqrt
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
        mvTrace.append((xPos, zPos))
        xPos += xDir
        xPos += xDir
        while True:
            mvTrace.append((xPos, zPos))
            zPos += zDir
            rpt -= 1
            if rpt == 0:
                break
    elif cmd == ct.PCMD_SET_DIR:		# 7
        xDir = 1 if (rpt & ct.PCMD_X_NEG) == 0 else -1
        zDir = 1 if (rpt & ct.PCMD_Z_NEG) == 0 else -1
        return None
    return mvTrace

xStepsInch = int((200 * 10 * 25.4) / 4) #8192
zStepsInch = int((200 * 10 * 25.4) / 5) #8192

print("xStepsInch %5d zStepsInch %5d" % (xStepsInch, zStepsInch))

radius = .125
xRadius = int(round(radius * xStepsInch))
xRadiusSqrd = xRadius * xRadius

zRadius = xRadius * zStepsInch // xStepsInch
zRadiusSqrd = zRadius * zRadius

print("radius %6.3f xRadius %5d xRadiusSqrd %10d zRadius %5d zRadiusSqrd %5d" % \
      (radius, xRadius, xRadiusSqrd, zRadius, zRadiusSqrd))

xStep45 = round(radius * sin(pi / 4) * xStepsInch)

print("xStep45 %d" % (xStep45))

lessThan45 = True

inXDir = 1
xLast = 0
x = 0
x0 = 0
cmdX = xLast
xPos = xLast

inZDir = -1
zLast = zRadius
z = zLast
z0 = 0
cmdZ = zLast
zPos = zLast

delta = None
lastDelta = None

cmd = 0
rpt = 0

count = 0
oneByte = 0
history = []
steps = 0

cmdCount = [0, 0, 0, 0, 0, 0, 0, 0]

move(ct.PCMD_SET_DIR | ((ct.PCMD_DIR_FLAG | ct.PCMD_Z_NEG) << ct.PCMD_RPT_SHIFT), 0)

while True:
    if lessThan45:
        x45 = " "
        zLast = z
        x = x0
        z = (int(round(sqrt(xRadiusSqrd - x * x))) * zStepsInch) // xStepsInch
        lastDelta = delta
        delta = z - zLast
        x0 += inXDir
    else:
        if z0 < 0:
            break
        x45 = ">"
        xLast = x
        z = z0
        if z == 0:
            x = xRadius
        else:
            x = (int(round(sqrt(zRadiusSqrd - z * z))) * xStepsInch) // zStepsInch
        lastDelta = delta
        delta = x - xLast
        z0 += inZDir

    if ((lastDelta is not None) and delta != lastDelta):
        xChange = abs(x - cmdX)
        zChange = abs(z - cmdZ)

        cmd = 0x7
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

        if len(mvTrace) > 0:
            (xTmp, zTmp) = mvTrace[0]
            if (cmdX != xTmp) or (cmdZ != zTmp):
                print("%5d x %5d%s z %5d " % (count, cmdX, x45, cmdZ), end="")
                print("%5d %5d+ %2d %2d" % (xTmp, zTmp, cmdX - xTmp, cmdZ - zTmp))

                (count0, cmdX0, x450, cmdZ0, xTmp0, zTmp0, delta0, lastDelta0, xChange0, \
                 zChange0, cmd0, rpt0) = cmdSave
                print("%5d x %5d%s z %5d " % (count0, cmdX0, x450, cmdZ0), end="")
                print("%5d %5d*" % (xTmp0, zTmp0), end="")
                print("delta %4d %4s xChg %3d zChg %3d rpt %3d cmd %d %2x" % \
                (delta0, str(lastDelta0), xChange0, zChange0, rpt0, \
                 cmd0 & ct.PCMD_CMD_MASK, cmd0))
                xPos = x
                zPos = z

        print("%5d x %5d%s z %5d " % (count, cmdX, x45, cmdZ), end="")
        if len(mvTrace) != 0:
            print("%5d %5d " % mvTrace[0], end="")
        print("delta %4d %4s xChg %3d zChg %3d rpt %3d cmd %d %2x" % \
              (delta, str(lastDelta), xChange, zChange, rpt, cmd & ct.PCMD_CMD_MASK, cmd))

        cmdSave = (count, cmdX, x45, cmdZ, xTmp, zTmp, delta, lastDelta,
                   xChange, zChange, cmd, rpt)

        historyLen = len(history)
        if historyLen > 1:
            for i in range(1, historyLen):
                print("      x %5d  z %5d" % history[i][:2], end="")
                if len(mvTrace) > 1:
                    print(" %5d %5d" % mvTrace[i], end="")
                (delta, lastDelta) = history[i][2:]
                print(" delta %4d %4s" % (delta, str(lastDelta)))

        history = []
            
        cmdX = x
        cmdZ = z
        count += 1
        delta = None
        if lessThan45:
            if x0 > xStep45:
                lessThan45 = False
                xLast = x
                z0 = z + inZDir;
                
    history.append((x, z, delta, lastDelta))

print("%5d x %5d  z %5d %5d %5d" % \
       (count, x, z, xPos, zPos))
for i in range(len(cmdCount)):
    val = cmdCount[i]
    if val != 0:
        print("%d %4d" % (i, val))
print("commands %d bytes %d steps %d oneByte %d" % \
      (count, 2 * (count - oneByte) + oneByte, steps, oneByte))
