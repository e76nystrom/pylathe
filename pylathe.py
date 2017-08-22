#!/cygdrive/c/Python27/Python.exe
#!/cygdrive/c/DevSoftware/Python/Python36-32/Python
#!/usr/bin/python
################################################################################
from __future__ import print_function
import wx
import wx.lib.inspection
from time import sleep, time
import sys
import os
import subprocess
from sys import stdout
import serial
from threading import Thread, Lock, Event
from math import radians, cos, tan, ceil, floor, sqrt, atan2, degrees
from Queue import Queue, Empty
from platform import system
from dxfwrite import DXFEngine as dxf
import re
WINDOWS = system() == 'Windows'
if WINDOWS:
    from pywinusb.hid import find_all_hid_devices

HOME_TEST = False
dbg = None

import configInfo
from configInfo import InfoValue, saveList, saveInfo, readInfo, initInfo, \
    newInfo, setInfo, getInfo, getBoolInfo, getFloatInfo, getIntInfo, \
    infoSetLabel, getInitialInfo, clrInfo

from setup import createConfig, createStrings, createCommands, \
    createParameters, createCtlBits, createEnums

from interface import configList, strList, cmdList, parmList, enumList, regList

(config, configTable) = createConfig(configList)

configFile = "config.txt"

clrInfo(len(config))
readInfo(configFile, config)

from setup import cfgXilinx, cfgDRO, spStepDrive

XILINX = getInitialInfo(cfgXilinx)
DRO = getInitialInfo(cfgDRO)
STEPPER_DRIVE = getInitialInfo(spStepDrive)

clrInfo(len(config))

cLoc = "../Lathe/include/"

fData = False
createCommands(cmdList, cLoc, fData)
createStrings(strList)
createParameters(parmList, cLoc, fData)
createCtlBits(regList, cLoc, fData)
createEnums(enumList, cLoc, fData)
if XILINX:
    from setup import createXilinxReg, createXilinxBits
    xLoc = '../../Xilinx/LatheCtl/'
    createXilinxReg(xilinxList, cLoc, xLoc, fData)
    createXilinxBits(xilinxBitList, cLoc, xLoc, fData)

from setup import importList
cmd = "from setup import "
for var in importList:
    cmd += var + ","
exec(cmd[:-1])

from comm import SWIG
SWIG = False
import comm
from comm import openSerial, CommTimeout, command, getParm, setParm,\
    getString, sendMove, getQueueStatus, queParm, sendMulti
comm.SWIG = SWIG

if XILINX:
    comm.enableXininx()
    from comm import setXReg, getXReg, dspXReg
    from interface import xilinxList, xilinxBitList

if SWIG:
    import lathe
    from lathe import taperCalc, T_ACCEL, zTaperInit, xTaperInit, tmp

print(sys.version)
print(wx.version())
stdout.flush()

hdrFont = None
testFont = None
emptyCell = (0, 0)
f = None
mainFrame = None
jogPanel = None
spindleDataSent = False
zDataSent = False
xDataSent = False
zHomeOffset = 0.0
xHomeOffset = 0.0
if DRO:
    zDROOffset = 0.0
    xDROOffset = 0.0
    zDROPosition = 0.0
    xDROPosition = 0.0
xHomed = False
done = False
jogShuttle = None
moveCommands = None

buttonRepeat = None

AL_LEFT   = 0x001
AL_RIGHT  = 0x002
AL_CENTER = 0x004
ABOVE     = 0x008
BELOW     = 0x010
MIDDLE    = 0x020
LEFT      = 0x040
RIGHT     = 0x080
CENTER    = 0x100

HOME_X = -1
AXIS_Z = 0
AXIS_X = 1

def commTimeout():
    jogPanel.setStatus(STR_TIMEOUT_ERROR)

class FormRoutines():
    def __init__(self):
        pass

    def formatData(self,formatList):
        success = True
        for (index, fieldType) in formatList:
            if fieldType == None:
                continue
            ctl = configInfo.info[index]
            strVal = ctl.GetValue()
            if fieldType.startswith('f'):
                strip = False
                if fieldType.endswith('s'):
                    fieldType = fieldType[:-1]
                    strip = True

                digits = 4
                if len(fieldType) > 1:
                    try:
                        digits = int(fieldType[1])
                    except ValueError:
                        pass
                format = "%%0.%df" % digits

                try:
                    val = float(strVal)
                    val = format % (val)
                    if strip:
                        if re.search("\.0*$", val):
                            val = re.sub("\.0*$", "", val)
                        else:
                            val = val.rstrip('0')
                    ctl.SetValue(val)
                except ValueError:
                    success = False
                    ctl.SetValue('')
            elif fieldType == 'd':
                try:
                    val = int(strVal)
                    ctl.SetValue("%d" % (val))
                except ValueError:
                    success = False
                    ctl.SetValue('')
        return(success)

    def fieldList(self, sizer, fields):
        for (label, index) in fields:
            if label.startswith('b'):
                self.addCheckBox(sizer, label[1:], index)
            else:
                self.addField(sizer, label, index)

    def addFieldText(self, sizer, label, key, keyText):
        if len(label) != 0:
            txt = wx.StaticText(self, -1, label)
            sizer.Add(txt, flag=wx.ALL|wx.ALIGN_RIGHT|\
                      wx.ALIGN_CENTER_VERTICAL, border=2)
            initInfo(keyText, txt)

        tc = wx.TextCtrl(self, -1, "", size=(60, -1))
        sizer.Add(tc, flag=wx.ALL, border=2)
        initInfo(key, tc)
        return(tc)

    def addField(self, sizer, label, key):
        global info
        if len(label) != 0:
            txt = wx.StaticText(self, -1, label)
            sizer.Add(txt, flag=wx.ALL|wx.ALIGN_RIGHT|\
                      wx.ALIGN_CENTER_VERTICAL, border=2)

        tc = wx.TextCtrl(self, -1, "", size=(60, -1))
        sizer.Add(tc, flag=wx.ALL, border=2)
        if key in configInfo.info:
            val = getInfo(key)
            tc.SetValue(val)
        initInfo(key, tc)
        return(tc)

    def addCheckBox(self, sizer, label, key):
        global info
        txt = wx.StaticText(self, -1, label)
        sizer.Add(txt, flag=wx.ALL|wx.ALIGN_RIGHT|\
                  wx.ALIGN_CENTER_VERTICAL, border=2)

        cb = wx.CheckBox(self, -1, style=wx.ALIGN_LEFT)
        sizer.Add(cb, flag=wx.ALL|wx.ALIGN_CENTER_VERTICAL, border=2)
        if key in configInfo.info:
            val = getInfo(key)
            cb.SetValue(val == 'True')
        initInfo(key, cb)
        return(cb)

    def addButton(self, sizer, label, action):
        btn = wx.Button(self, label=label, size=(60,-1))
        btn.Bind(wx.EVT_BUTTON, action)
        sizer.Add(btn, flag=wx.CENTER|wx.ALL, border=2)

def getFloatVal(tc):
    try:
        return(float(tc.GetValue()))
    except ValueError:
        return(0.0)

def getIntVal(tc):
    try:
        return(int(tc.GetValue()))
    except ValueError:
        return(0)

moveQue = Queue()

class MoveCommands():
    def __init__(self):
        self.d = None
        self.lastX = 0.0
        self.lastZ = 0.0
        self.passNum = 0
        self.send = False
        self.textH = 0.005
        self.vS = self.textH / 2
        self.hS = self.textH
        self.textAngle = 0.0
        self.dbg = False
        self.xText = None
        self.zText = None
        self.fileName = None

    def draw(self, type, diam, parm):
        tmp = "%s%0.3f-%0.3f" % (type, diam, parm)
        tmp = tmp.replace("." , "-")
        tmp = re.sub("-0$", "", tmp) + ".dxf"
        self.fileName = os.path.join(os.getcwd(), tmp)
        d = dxf.drawing(self.fileName)
        self.style = dxf.style("CONSOLAS", font="Consolas.ttf")
        d.add_layer(TEXT, color=0)
        d.add_layer(REF, color=1)
        self.textAngle = 0.0
        self.d = d
        self.xText = []
        self.zText = []

    def setTextAngle(self, textAngle):
        self.textAngle = textAngle

    def setLoc(self, z, x):
        if self.d != None:
            self.lastX = x
            self.lastZ = z

    def drawLineX(self, x, layer=0):
        if self.d != None:
            self.d.add(dxf.line((self.lastZ, self.lastX), \
                                (self.lastZ, x), layer=layer))
            self.lastX = x

    def drawLineZ(self, z, layer=0):
        if self.d != None:
            self.d.add(dxf.line((self.lastZ, self.lastX), \
                                (z, self.lastX), layer=layer))
            self.lastZ = z

    def drawLine(self, z, x, layer=0):
        if self.d != None:
            self.d.add(dxf.line((self.lastZ, self.lastX), \
                                (z, x), layer=layer))
            self.lastX = x
            self.lastZ = z

    def saveXText(self, val, pos):
        if self.xText != None:
            self.xText.append((val, pos))

    def printXText(self, fmt, align, internal):
        if self.xText == None:
            return
        lastY = 999 if not internal else 0
        h = self.textH + self.vS
        for (val, pos) in self.xText:
            (x, y) = pos
            if not internal:
                if lastY - y < h:
                    y = lastY - h
            else:
                if y - lastY < h:
                    y = lastY + h
            lastY = y
            self.text(fmt % val, (x, y), align)
            
    def saveZText(self, val, pos):
        if self.zText != None:
            self.zText.append((val, pos))

    def printZText(self, fmt, align):
        if self.zText == None:
            return
        self.textAngle = 90.0
        lastX = 10
        h = -(self.textH + self.vS)
        # print("h %7.4f" % (h))
        for (val, pos) in self.zText:
            (x, y) = pos
            diff = x - lastX
            # print("x %7.4f lastX %7.4f diff %7.4f %s" % \
            #       (x, lastX, diff, fmt % val))
            if diff > h:
                x = lastX + h
            self.text(fmt % val, (x, y), align)
            lastX = x
        self.textAngle = 0.0
            
    def text(self, text, p0, align=None, layer='TEXT'):
        if self.d != None:
            (x, y) = p0
            hOffset = self.hS
            vOffset = -self.textH / 2
            if align != None:
                textW = len(text) * self.textH * 0.9
                if align & RIGHT:
                    hOffset = -(textW + self.hS)
                elif align & CENTER:
                    hOffset = -textW / 2
                elif align & LEFT:
                    hOffset = self.hS

                if align & ABOVE:
                    vOffset = self.vS
                elif align & BELOW:
                    vOffset = -(self.textH + self.vS)
                elif align & MIDDLE:
                    vOffset = -(self.textH / 2)

            if self.textAngle != 0.0:
                (vOffset, hOffset) = (hOffset, -vOffset)
            self.d.add(dxf.text(text, (x + hOffset, y + vOffset), \
                                height=self.textH, rotation=self.textAngle, \
                                layer=layer, style=self.style))
    def drawClose(self):
        if self.d != None:
            try:
                if self.d != None:
                    self.d.save()
                    fileName = self.fileName
                    if WINDOWS:
                        fileName = fileName.replace("\\", "/")
                        fileName = fileName.replace("C:", "/cygdrive/c")
                    subprocess.call(["sed", "-i", "-e", \
                                     "'s/arial/consolas/g'", \
                                     fileName])
                    self.fileName = None
                    self.d = None
            except:
                print("dxf file save error")

    def queMove(self, op, val):
        if self.send:
            opString = mCommandsList[op]
            moveQue.put((opString, op, val))

    def queMoveF(self, op, flag, val):
        if self.send:
            opString = mCommandsList[op]
            op |= (flag << 8)
            moveQue.put((opString, op, val))

    def queClear(self):
        self.send = not getInfo(cfgCmdDis)
        while not moveQue.empty():
            moveQue.get()

    def queZSetup(self, feed):
        self.queMove(Z_FEED_SETUP, feed)
        self.saveZOffset();
        self.saveXOffset();

    def queXSetup(self, feed):
        self.queMove(X_FEED_SETUP, feed)
        self.saveZOffset();
        self.saveXOffset();

    def startSpindle(self, rpm):
        self.queMove(START_SPINDLE, rpm)
        self.saveZOffset();
        self.saveXOffset();

    def stopSpindle(self):
        self.queMove(STOP_SPINDLE, 0)

    def queFeedType(self, feedType):
        self.queMove(SAVE_FEED_TYPE, feedType)

    def zSynSetup(self, feed):
        self.queMove(Z_SYN_SETUP, feed)

    def xSynSetup(self, feed):
        self.queMove(X_SYN_SETUP, feed)

    def nextPass(self, passNum):
        self.passNum = passNum
        self.queMove(PASS_NUM, passNum)
        if self.dbg:
            if passNum & 0x100:
                print("spring\n")
            elif passNum & 0x200:
                print("spring %d" % (passNum & 0xff))
            else:
                print("pass %d]" % (passNum))

    def quePause(self):
        self.queMove(QUE_PAUSE, 0)

    def saveDiameter(self, val):
        self.queMove(SAVE_DIAMETER, val)

    def moveZ(self, zLoc, flag=CMD_MAX):
        self.queMoveF(MOVE_Z, flag, zLoc)
        self.drawLineZ(zLoc)
        if self.dbg:
            print("moveZ  %7.4f" % (zLoc))

    def moveX(self, xLoc, flag=CMD_MAX):
        self.queMoveF(MOVE_X, flag, xLoc)
        self.drawLineX(xLoc)
        if self.dbg:
            print("moveX  %7.4f" % (xLoc))

    def saveZOffset(self):
        global zHomeOffset
        self.queMove(SAVE_Z_OFFSET, zHomeOffset)
        if self.dbg:
            print("saveZOffset  %7.4f" % (zHomeOffset))

    def saveXOffset(self):
        global xHomeOffset
        self.queMove(SAVE_X_OFFSET, xHomeOffset)
        if self.dbg:
            print("savexOffset  %7.4f" % (xHomeOffset))

    def moveXZ(self, zLoc, xLoc):
        self.queMove(SAVE_Z, zLoc)
        self.queMove(MOVE_XZ, xLoc)
        if self.dbg:
            print("moveZX %7.4f %7.4f" % (zLoc, xLoc))

    def moveZX(self, zLoc, xLoc):
        self.queMove(SAVE_X, xLoc)
        self.queMove(MOVE_ZX, zLoc)
        if self.dbg:
            print("moveXZ %7.4f %7.4f" % (zLoc, xLoc))

    def saveTaper(self, taper):
        taper = "%0.6f" % (taper)
        self.queMove(SAVE_TAPER, taper)
        if self.dbg:
            print("saveTaper %s" % (taper))

    def saveRunout(self, runout):
        self.queMove(SAVE_RUNOUT, runout)
        if self.dbg:
            print("saveRunout %7.4f" % (runout))

    def saveDepth(self, depth):
        self.queMove(SAVE_DEPTH, depth)
        if self.dbg:
            print("saveDepth %7.4f" % (depth))

    def taperZX(self, zLoc, xLoc):
        self.queMove(SAVE_X, xLoc)
        self.queMoveF(TAPER_ZX, 1, zLoc)
        if self.dbg:
            print("taperZX %7.4f" % (zLoc))

    def taperXZ(self, xLoc, zLoc):
        self.queMove(SAVE_Z, zLoc)
        self.queMoveF(TAPER_XZ, 1, xLoc)
        if self.dbg:
            print("taperXZ %7.4f" % (xLoc))

    def probeZ(self, zDist):
        self.queMove(PROBE_Z, zDist)
        if self.dbg:
            print("probeZ %7.4f" % (zDist))

    def probeX(self, xDist):
        self.queMove(PROBE_X, xDist)
        if self.dbg:
            print("probeX %7.4f" % (xDist))

    def done(self, parm):
        self.queMove(OP_DONE, parm)

def sendClear():
    global spindleDataSent, zDataSent, xDataSent
    try:
        command(CLRDBG);
        command(CMD_CLEAR)
    except CommTimeout:
        commTimeout()
    spindleDataSent = False
    zDataSent = False
    xDataSent = False

def xilinxTestMode():
    global fcy
    testMode = False
    try:
        testMode = getInfo(cfgTestMode)
    except KeyError:
        testMode = False
    if testMode:
        encoder = 0
        try:
            encoder = getIntInfo(cfgEncoder)
        except KeyError:
            encoder = 0
        rpm = 0
        try:
            rpm = int(getFloatInfo(cfgTestRPM))
        except KeyError:
            rpm = 0
        if encoder != 0:
            preScaler = 1
            if rpm == 0:
                rpm = 1
            rps = rpm / 60.0
            encTimer = int(fcy / (encoder * rps))
            while encTimer >= 65536:
                preScaler += 1
                encTimer = int(fcy / (encoder * rps * preScaler))
            print("preScaler %d encTimer %d" % (preScaler, encTimer))
            queParm(ENC_ENABLE, '1')
            queParm(ENC_PRE_SCALER, preScaler)
            queParm(ENC_TIMER, encTimer)
    else:
        queParm(ENC_ENABLE, '0')

def sendSpindleData(send=False, rpm=None):
    global spindleDataSent, XILINX
    try:
        if send or (not spindleDataSent):
            queParm(STEPPER_DRIVE, getBoolInfo(spStepDrive))
            if STEPPER_DRIVE:
                queParm(SP_STEPS, getInfo(spMotorSteps))
                queParm(SP_MICRO, getInfo(spMicroSteps))
                queParm(SP_MIN_RPM, getInfo(spMinRPM))
                if rpm != None:
                    queParm(SP_MAX_RPM, rpm)
                else:
                    queParm(SP_MAX_RPM, getInfo(spMaxRPM))
                # queParm(SP_ACCEL_TIME, getInfo(spAccelTime))
                queParm(SP_ACCEL, getInfo(spAccel))
                queParm(SP_JOG_MIN_RPM, getInfo(spJogMin))
                queParm(SP_JOG_MAX_RPM, getInfo(spJogMax))
                # queParm(SP_JOG_ACCEL_TIME, getInfo(spAccelTime))
                queParm(SP_DIR_FLAG, getBoolInfo(spInvDir))
                queParm(SP_TEST_INDEX, getBoolInfo(spTestIndex))
                command(CMD_SPSETUP)
            elif XILINX:
                queParm(ENC_MAX, getInfo(cfgEncoder))
                queParm(X_FREQUENCY, getInfo(cfgXFreq))
                queParm(FREQ_MULT, getInfo(cfgFreqMult))
                xilinxTestMode()
                queParm(RPM, getInfo(cfgTestRPM))
                cfgReg = 0
                if getBoolInfo(cfgInvEncDir):
                    cfgReg |= ENC_POL
                if getBoolInfo(zInvDir):
                    cfgReg |= ZDIR_POL
                if getBoolInfo(xInvDir):
                     cfgReg |= XDIR_POL
                queParm(X_CFG_REG, cfgReg)
                sendMulti()
            spindleDataSent = True
    except CommTimeout:
        commTimeout()

def sendZData(send=False):
    global zDataSent, jogPanel
    try:
        if send or (not zDataSent):
            pitch = getFloatInfo(zPitch)
            motorSteps = getIntInfo(zMotorSteps)
            microSteps = getIntInfo(zMicroSteps)
            motorRatio = getFloatInfo(zMotorRatio)
            jogPanel.zStepsInch = (microSteps * motorSteps * \
                                   motorRatio) / pitch
            jogPanel.zDROInch = getIntInfo(zDROInch)
            jogPanel.zDROInvert = -1 if getBoolInfo(zInvDRO) else 1
            stdout.flush()
            val = jogPanel.combo.GetValue()
            try:
                val = float(val)
                if val > 0.020:
                    val = 0.020
            except ValueError:
                val = 0.001
            queParm(Z_MPG_INC, val * jogPanel.zStepsInch)

            queParm(Z_PITCH, getInfo(zPitch))
            queParm(Z_RATIO, getInfo(zMotorRatio))
            queParm(Z_MICRO, getInfo(zMicroSteps))
            queParm(Z_MOTOR, getInfo(zMotorSteps))
            queParm(Z_ACCEL, getInfo(zAccel))
            queParm(Z_BACKLASH, getInfo(zBacklash))

            queParm(Z_MOVE_MIN, getInfo(zMinSpeed))
            queParm(Z_MOVE_MAX, getInfo(zMaxSpeed))

            queParm(Z_JOG_MIN, getInfo(zJogMin))
            queParm(Z_JOG_MAX, getInfo(zJogMax))

            queParm(Z_DIR_FLAG, getBoolInfo(zInvDir))
            queParm(Z_MPG_FLAG, getBoolInfo(zInvMpg))
                
            command(CMD_ZSETUP)
            zDataSent = True
    except CommTimeout:
        commTimeout()
    except:
        print("setZData exception")
        stdout.flush()

def sendXData(send=False):
    global xDataSent, jogPanel
    try:
        if send or (not xDataSent):
            pitch = getFloatInfo(xPitch)
            motorSteps = getIntInfo(xMotorSteps)
            microSteps = getIntInfo(xMicroSteps)
            motorRatio = getFloatInfo(xMotorRatio)
            jogPanel.xStepsInch = (microSteps * motorSteps * \
                                   motorRatio) / pitch
            jogPanel.xDROInch = getIntInfo(xDROInch)
            jogPanel.xDROInvert = -1 if getBoolInfo(xInvDRO) else 1
            val = jogPanel.combo.GetValue()
            try:
                val = float(val)
                if val > 0.020:
                    val = 0.020
            except ValueError:
                val = 0.001
            queParm(X_MPG_INC, val * jogPanel.xStepsInch)

            queParm(X_PITCH, getInfo(xPitch))
            queParm(X_RATIO, getInfo(xMotorRatio))
            queParm(X_MICRO, getInfo(xMicroSteps))
            queParm(X_MOTOR, getInfo(xMotorSteps))
            queParm(X_ACCEL, getInfo(xAccel))
            queParm(X_BACKLASH, getInfo(xBacklash))

            queParm(X_MOVE_MIN, getInfo(xMinSpeed))
            queParm(X_MOVE_MAX, getInfo(xMaxSpeed))

            queParm(X_JOG_MIN, getInfo(xJogMin))
            queParm(X_JOG_MAX, getInfo(xJogMax))

            queParm(X_DIR_FLAG, getBoolInfo(xInvDir))
            queParm(X_MPG_FLAG, getBoolInfo(xInvMpg))

            global HOME_TEST
            if HOME_TEST:
                stepsInch = jogPanel.xStepsInch
                start = str(int(getFloatInfo(xHomeStart) * stepsInch))
                end = str(int(getFloatInfo(xHomeEnd) * stepsInch))
                if end > start:
                    (start, end) = (end, start)
                queParm(X_HOME_START, start)
                queParm(X_HOME_END, end)

            command(CMD_XSETUP)
            xDataSent = True
    except CommTimeout:
        commTimeout()

class UpdatePass():
    def __init__(self):
        self.passes = 0
        self.passInt = 0
        self.sPasses = 0
        self.actualFeed = 0.0
        self.cutAmount = 0.0
        self.calcPass = None
        self.genPass = None

    def calcFeed(self, feed, cutAmount, finish=0):
        self.cutAmount = cutAmount
        cutToFinish = cutAmount - finish
        self.passes = int(ceil(cutToFinish / abs(feed)))
        self.actualFeed = cutToFinish / self.passes
        if finish != 0:
            self.passes += 1
        self.initPass()
        
    def setupFeed(self, actualFeed, cutAmount):
        self.actualFeed = actualFeed
        self.cutAmount = cutAmount

    def setupSpringPasses(self, panel):
        self.sPassInt = getIntVal(panel.sPInt)
        self.sPasses = getIntVal(panel.spring)

    def setupAction(self, calcPass, genPass):
        self.calcPass = calcPass
        self.genPass = genPass

    def initPass(self):
        setParm(TOTAL_PASSES, self.passes)
        self.passCount = 1
        self.sPassCtr = 0
        self.spring = 0
        self.feed = 0.0
        self.springFlag = False

    def updatePass(self):
        global moveCommands
        if self.passCount <= self.passes:
            self.springFlag = False
            if self.sPassInt != 0:
                self.sPassCtr += 1
                if self.sPassCtr > self.sPassInt:
                    self.sPassCtr = 0
                    self.springFlag = True
            if self.springFlag:
                moveCommands.nextPass(0x100 | self.passCount)
            else:
                moveCommands.nextPass(self.passCount)
                self.calcPass(self.passCount == self.passes)
                self.passCount += 1
            self.genPass()
        else:
            if self.springFlag:
                self.springFlag = False
                self.spring += 1
            if self.spring < self.sPasses:
                self.spring += 1
                moveCommands.nextPass(0x200 | self.spring)
                self.genPass()
            else:
                return(False)
        return(True)

class Turn(UpdatePass):
    def __init__(self, turnPanel):
        UpdatePass.__init__(self)
        self.turnPanel = turnPanel
        global moveCommands
        self.m = moveCommands

    def getTurnParameters(self):
        tu = self.turnPanel
        self.zStart = getFloatVal(tu.zStart)
        self.zEnd = getFloatVal(tu.zEnd)
        self.zRetract = getFloatVal(tu.zRetract)

        self.xStart = getFloatVal(tu.xStart) / 2.0
        self.xEnd = getFloatVal(tu.xEnd) / 2.0
        self.xFeed = abs(getFloatVal(tu.xFeed) / 2.0)
        self.xRetract = abs(getFloatVal(tu.xRetract))

    def turn(self):
        self.getTurnParameters()

        if self.xStart < 0:
            if self.xEnd <= 0:
                self.neg = True
            else:
                print("error")
                return
        else:
            if self.xEnd >= 0:
                self.neg = False
            else:
                print("error")
                return

        self.xCut = abs(self.xStart) - abs(self.xEnd)
        self.internal = self.xCut < 0
        self.xCut = abs(self.xCut)

        self.calcFeed(self.xFeed, self.xCut)
        self.setupSpringPasses(self.turnPanel)
        self.setupAction(self.calculateTurnPass, self.turnPass)

        self.turnPanel.passes.SetValue("%d" % (self.passes))
        print("xCut %5.3f passes %d internal %s" % \
              (self.xCut, self.passes, self.internal))

        if self.internal:
            if not self.neg:
                self.xRetract = -self.xRetract
        else:
            if self.neg:
                self.xRetract = -self.xRetract

        self.safeX = self.xStart + self.xRetract
        self.safeZ = self.zStart + self.zRetract

        if getInfo(cfgDraw):
            self.m.draw("turn", self.zStart, self.zEnd)
            
        self.turnSetup()

        while self.updatePass():
            pass

        self.m.moveX(self.xStart + self.xRetract)
        if STEPPER_DRIVE:
            self.m.stopSpindle();
        self.m.done(1)
        self.m.drawClose()
        stdout.flush()

    def turnSetup(self):
        m = self.m
        m.setLoc(self.zEnd, self.xStart)
        m.drawLineZ(self.zStart, REF)
        m.drawLineX(self.xEnd, REF)
        m.setLoc(self.safeZ, self.safeX)
        m.quePause()
        self.m.done(0)
        if STEPPER_DRIVE:
            m.startSpindle(getIntInfo(tuRPM))
            m.queFeedType(FEED_PITCH)
            m.zSynSetup(getFloatInfo(tuZFeed))
        else:
            m. queZSetup(getFloatInfo(tuZFeed))
        m.moveX(self.safeX)
        m.moveZ(self.safeZ)
        m.text("%7.3f" % (self.xStart * 2.0), \
               (self.safeZ, self.xStart))
        m.text("%7.3f" % (self.zStart), \
               (self.zStart, self.xEnd), \
               CENTER | (ABOVE if self.internal else BELOW))
        m.text("%7.3f %6.3f" % (self.safeX * 2.0, self.actualFeed), \
               (self.safeZ, self.safeX))
        m.text("%7.3f" % (self.zEnd), \
               (self.zEnd, self.safeX), CENTER)

    def calculateTurnPass(self, final=False):
        feed = self.cutAmount if final else self.passCount * self.actualFeed
        self.feed = feed
        if self.internal:
            if self.neg:
                feed = -feed
        else:
            if not self.neg:
                feed = -feed
        self.curX = self.xStart + feed
        self.safeX = self.curX + self.xRetract
        print("pass %2d feed %5.3f x %5.3f diameter %5.3f" % \
              (self.passCount, feed, self.curX, self.curX * 2.0))

    def turnPass(self):
        m = self.m
        m.moveX(self.curX, CMD_JOG)
        m.saveDiameter(self.curX * 2.0)
        if self.turnPanel.pause.GetValue():
            print("pause")
            self.m.quePause()
        if m.passNum & 0x300 == 0:
            m.text("%2d %7.3f" % (m.passNum, self.curX * 2.0), \
                   (self.safeZ, self.curX))
        m.moveZ(self.zStart)
        m.moveZ(self.zEnd, CMD_SYN)
        m.moveX(self.safeX)
        if m.passNum & 0x300 == 0:
            m.text("%2d %7.3f" % (m.passNum, self.safeX * 2.0), \
                   (self.zEnd, self.safeX), RIGHT)
        m.moveZ(self.safeZ)

    def turnAdd(self):
        if self.feed >= self.xCut:
            add = getFloatVal(self.turnPanel.add)
            self.cutAmount += add
            self.calculateTurnPass(True)
            self.turnSetup()
            self.turnPass()
            self.m.moveX(self.xStart + self.xRetract)
            self.m.stopSpindle()
            command(CMD_RESUME)

class TurnPanel(wx.Panel, FormRoutines):
    def __init__(self, parent, *args, **kwargs):
        super(TurnPanel, self).__init__(parent, *args, **kwargs)
        self.InitUI()
        self.configList = None
        self.turn = Turn(self)
        self.formatList = ((tuAddFeed, 'f'), \
                           (tuPasses, 'd'), \
                           (tuPause, None), \
                           (tuRPM, 'd'), \
                           (tuSPInt, 'd'), \
                           (tuSpring, 'd'), \
                           (tuXEnd, 'f'), \
                           (tuXFeed, 'f'), \
                           (tuXRetract, 'f'), \
                           (tuXStart, 'f'),\
                           (tuZEnd, 'f'), \
                           (tuZFeed, 'f'), \
                           (tuZRetract, 'f'), \
                           (tuZStart, 'f'))

    def InitUI(self):
        global hdrFont

        self.sizerV = sizerV = wx.BoxSizer(wx.VERTICAL)

        txt = wx.StaticText(self, -1, "Turn")
        txt.SetFont(hdrFont)

        sizerV.Add(txt, flag=wx.CENTER|wx.ALL, border=2)

        sizerG = wx.GridSizer(8, 0, 0)

        # z parameters

        self.zEnd = self.addField(sizerG, "Z End", tuZEnd)
        
        self.zStart = self.addField(sizerG, "Z Start", tuZStart)

        self.zFeed = self.addField(sizerG, "Z Feed", tuZFeed)

        self.zRetract = self.addField(sizerG, "Z Retract", tuZRetract)

        # x parameters

        self.xStart = self.addField(sizerG, "X Start D", tuXStart)

        self.xEnd = self.addField(sizerG, "X End D", tuXEnd)

        self.xFeed = self.addField(sizerG, "X Feed D", tuXFeed)

        self.xRetract = self.addField(sizerG, "X Retract", tuXRetract)

        # pass info

        self.passes = self.addField(sizerG, "Passes", tuPasses)
        self.passes.SetEditable(False)

        self.sPInt = self.addField(sizerG, "SP Int", tuSPInt)

        self.spring = self.addField(sizerG, "Spring", tuSpring)

        sizerG.Add(emptyCell)
        sizerG.Add(emptyCell)

        # buttons

        self.addButton(sizerG, 'Send', self.OnSend)
        # btn = wx.Button(self, label='Send', size=(60,-1))
        # btn.Bind(wx.EVT_BUTTON, self.OnSend)
        # sizerG.Add(btn, flag=wx.CENTER|wx.ALL, border=2)

        self.addButton(sizerG, 'Start', self.OnStart)
        # btn = wx.Button(self, label='Start', size=(60,-1))
        # btn.Bind(wx.EVT_BUTTON, self.OnStart)
        # sizerG.Add(btn, flag=wx.CENTER|wx.ALL, border=2)

        self.addButton(sizerG, 'Add', self.OnAdd)
        # btn = wx.Button(self, label='Add', size=(60,-1))
        # btn.Bind(wx.EVT_BUTTON, self.OnAdd)
        # sizerG.Add(btn, flag=wx.CENTER|wx.ALL, border=2)

        self.add = self.addField(sizerG, "", tuAddFeed)

        self.rpm = self.addField(sizerG, "RPM", tuRPM)

        self.pause = self.addCheckBox(sizerG, "Pause", tuPause)
        # sizerG.Add(wx.StaticText(self, -1, "Pause"), border=2, \
        #            flag=wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.ALL)
        # self.pause = cb = wx.CheckBox(self, -1, \
        #                                  style=wx.ALIGN_LEFT)
        # sizerG.Add(cb, flag=wx.ALIGN_CENTER_VERTICAL|wx.ALL, border=2)
        # initInfo(tuPause, cb)
        
        sizerV.Add(sizerG, flag=wx.CENTER|wx.ALL, border=2)

        self.SetSizer(sizerV)
        self.sizerV.Fit(self)

    def getConfigList(self):
        if self.configList == None:
            self.configList = []
            for i, (name) in enumerate(configTable):
                if name.startswith('tu'):
                    self.configList.append(i)
        return(self.configList)

    def update(self):
        self.formatData(self.formatList)

    def sendData(self):
        global moveCommands
        try:
            moveCommands.queClear()
            sendClear()

            sendSpindleData()
            sendZData()
            sendXData()

        except CommTimeout:
            commTimeout()

    def OnSend(self, e):
        global xHomed, jogPanel
        if self.formatData(self.formatList):
            if xHomed:
                jogPanel.setStatus(STR_CLR)
                self.sendData()
                self.turn.turn()
            else:
                jogPanel.setStatus(STR_NOT_HOMED)
        else:
            jogPanel.setStatus(STR_FIELD_ERROR)
        jogPanel.focus()

    def OnStart(self, e):
        global dbg, jogPanel
        command(CMD_RESUME)
        if getBoolInfo(cfgDbgSave):
            dbg = open('dbg.txt', 'w')
        jogPanel.focus()
    
    def OnAdd(self, e):
        global jogPanel
        self.turn.turnAdd()
        jogPanel.focus()

class Face(UpdatePass):
    def __init__(self, facePanel):
        UpdatePass.__init__(self)
        self.facePanel = facePanel
        global moveCommands
        self.m = moveCommands

    def getFaceParameters(self):
        fa = self.facePanel
        self.xStart = getFloatVal(fa.xStart) / 2.0
        self.xEnd = getFloatVal(fa.xEnd) / 2.0
        self.xFeed = abs(getFloatVal(fa.xFeed))
        self.xRetract = abs(getFloatVal(fa.xRetract))

        self.zStart = getFloatVal(fa.zStart)
        self.zEnd = getFloatVal(fa.zEnd)
        self.zFeed = getFloatVal(fa.zFeed)
        self.zRetract = abs(getFloatVal(fa.zRetract))

    def face(self):
        self.getFaceParameters()

        self.internal = self.xStart < self.xEnd
        self.zCut = abs(self.zStart - self.zEnd)

        self.calcFeed(self.zFeed, self.zCut)
        self.setupSpringPasses(self.facePanel)
        self.setupAction(self.calculateFacePass, self.facePass)

        self.facePanel.passes.SetValue("%d" % (self.passes))
        print("zCut %5.3f passes %d internal %s" % \
              (self.zCut, self.passes, self.internal))

        if self.internal:
            self.xRetract = -self.xRetract
        self.safeX = self.xStart + self.xRetract
        self.safeZ = self.zStart + self.zRetract

        if getInfo(cfgDraw):
            self.m.draw("face", self.xStart, self.xEnd)
            self.m.setTextAngle(90)

        self.faceSetup()

        while self.updatePass():
            pass

        self.m.moveX(self.safeX)
        self.m.moveZ(self.zStart + self.zRetract)

        if STEPPER_DRIVE:
            self.m.stopSpindle()
        self.m.done(1)
        self.m.drawClose()
        stdout.flush()

    def faceSetup(self):
        m = self.m
        m.setLoc(self.zEnd, self.xStart)
        m.drawLineZ(self.zStart, REF)
        m.drawLineX(self.xEnd, REF)
        m.setLoc(self.zStart, self.safeX)
        m.quePause()
        self.m.done(0)
        if STEPPER_DRIVE:
            m.startSpindle(getIntInfo(faRPM))
            m.queFeedType(FEED_PITCH)
            m.xSynSetup(getFloatInfo(faXFeed))
        else:
            m.queXSetup(getFloatInfo(faxFeed))
        m.moveX(self.safeX)
        m.moveZ(self.zStart)
        m.text("%7.3f" % (self.zStart), \
               (self.zStart, self.xEnd), None if self.internal else RIGHT)
        m.text("%7.3f %6.3f" % \
               (self.safeX * 2.0, self.actualFeed), \
               (self.safeZ, self.safeX))
        m.text("%7.3f" % (self.xStart * 2.0), \
               (self.zEnd, self.xStart), CENTER)
        m.text("%7.3f" % (self.xEnd * 2.0), \
               (self.zEnd, self.xEnd), CENTER)

    def calculateFacePass(self, final=False):
        feed = self.cutAmount if final else self.passCount * self.actualFeed
        self.feed = feed
        self.curZ = self.zStart - feed
        self.safeZ = self.curZ + self.zRetract
        print("pass %2d feed %5.3f z %5.3f" % \
              (self.passCount, feed, self.curZ))

    def facePass(self):
        m = self.m
        m.moveZ(self.curZ, CMD_JOG)
        if self.facePanel.pause.GetValue():
            print("pause")
            m.quePause()
        if m.passNum & 0x300 == 0:
            m.text("%2d %7.3f" % (m.passNum, self.curZ), \
                   (self.curZ, self.safeX), RIGHT if self.internal else None)
        m.moveX(self.xStart)
        m.moveX(self.xEnd, CMD_SYN)
        m.moveZ(self.safeZ)
        if m.passNum & 0x300 == 0:
            m.text("%2d %7.3f" % (m.passNum, self.safeZ), \
                   (self.safeZ, self.xEnd), None if self.internal else RIGHT)
        m.moveX(self.safeX)

    def faceAdd(self):
        if self.feed >= self.zCut:
            add = getFloatVal(self.facePanel.add)
            self.cutAmount += add
            self.faceSetup()
            self.calculateFacePass(True)
            self.facePass()
            self.m.moveX(self.safeX)
            self.m.moveZ(self.zStart + self.zRetract)
            self.m.stopSpindle()
            command(CMD_RESUME)

class FacePanel(wx.Panel, FormRoutines):
    def __init__(self, parent, *args, **kwargs):
        super(FacePanel, self).__init__(parent, *args, **kwargs)
        self.InitUI()
        self.configList = None
        self.face = Face(self)
        self.formatList = ((faAddFeed, 'f'), \
                           (faPasses, 'f'), \
                           (faPause, None), \
                           (faRPM, 'd'), \
                           (faSPInt, 'd'), \
                           (faSpring, 'd'), \
                           (faXEnd, 'f'), \
                           (faXFeed, 'f'), \
                           (faXRetract, 'f'), \
                           (faXStart, 'f'), \
                           (faZEnd, 'f'), \
                           (faZFeed, 'f'), \
                           (faZRetract, 'f'), \
                           (faZStart, 'f'))

    def InitUI(self):
        global hdrFont, emptyCell
        self.sizerV = sizerV = wx.BoxSizer(wx.VERTICAL)

        txt = wx.StaticText(self, -1, "Face")
        txt.SetFont(hdrFont)

        sizerV.Add(txt, flag=wx.CENTER|wx.ALL, border=2)

        # x parameters

        sizerG = wx.GridSizer(8, 0, 0)

        self.xStart = self.addField(sizerG, "X Start D", faXStart)

        self.xEnd = self.addField(sizerG, "X End D", faXEnd)
        
        self.xFeed = self.addField(sizerG, "X Feed", faXFeed)
        
        self.xRetract = self.addField(sizerG, "X Retract", faXRetract)

        # z parameters

        self.zEnd = self.addField(sizerG, "Z End", faZEnd)

        self.zStart = self.addField(sizerG, "Z Start", faZStart)

        self.zFeed = self.addField(sizerG, "Z Feed", faZFeed)

        self.zRetract = self.addField(sizerG, "Z Retract", faZRetract)
        
        # pass info

        self.passes = self.addField(sizerG, "Passes", faPasses)
        self.passes.SetEditable(False)

        self.sPInt = self.addField(sizerG, "SP Int", faSPInt)

        self.spring = self.addField(sizerG, "Spring", faSpring)

        sizerG.Add(emptyCell)
        sizerG.Add(emptyCell)

        # buttons

        self.addButton(sizerG, 'Send', self.OnSend)
        # btn = wx.Button(self, label='Send', size=(60,-1))
        # btn.Bind(wx.EVT_BUTTON, self.OnSend)
        # sizerG.Add(btn, flag=wx.CENTER|wx.ALL, border=2)

        self.addButton(sizerG, 'Start', self.OnStart)
        # btn = wx.Button(self, label='Start', size=(60,-1))
        # btn.Bind(wx.EVT_BUTTON, self.OnStart)
        # sizerG.Add(btn, flag=wx.CENTER|wx.ALL, border=2)

        self.addButton(sizerG, 'Add', self.OnAdd)
        # btn = wx.Button(self, label='Add', size=(60,-1))
        # btn.Bind(wx.EVT_BUTTON, self.OnAdd)
        # sizerG.Add(btn, flag=wx.CENTER|wx.ALL, border=2)

        self.add = self.addField(sizerG, "", faAddFeed)

        self.rpm = self.addField(sizerG, "RPM", faRPM)

        self.pause = self.addCheckBox(sizerG, "Pause", faPause)
        # sizerG.Add(wx.StaticText(self, -1, "Pause"), border=2, \
        #            flag=wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.ALL)
        # self.pause = cb = wx.CheckBox(self, -1, \
        #                                  style=wx.ALIGN_LEFT)
        # sizerG.Add(cb, flag=wx.ALIGN_CENTER_VERTICAL|wx.ALL, border=2)
        # initInfo(faPause, cb)

        sizerV.Add(sizerG, flag=wx.CENTER|wx.ALL, border=2)

        self.SetSizer(sizerV)
        self.sizerV.Fit(self)

    def getConfigList(self):
        if self.configList == None:
            self.configList = []
            for i, (name) in enumerate(configTable):
                if name.startswith('fa'):
                    self.configList.append(i)
        return(self.configList)

    def update(self):
        self.formatData(self.formatList)

    def sendData(self):
        global moveCommands
        try:
            moveCommands.queClear()
            sendClear()
            sendSpindleData()
            sendZData()
            sendXData()

        except CommTimeout:
            commTimeout()

    def OnSend(self, e):
        global xHomed, jogPanel
        if self.formatData(self.formatList):
            if xHomed:
                jogPanel.setStatus(STR_CLR)
                self.sendData()
                self.face.face()
            else:
                jogPanel.setStatus(STR_NOT_HOMED)
        else:
            jogPanel.setStatus(STR_FIELD_ERROR)
        jogPanel.focus()

    def OnStart(self, e):
        global dbg, jogPanel
        command(CMD_RESUME)
        if getBoolInfo(cfgDbgSave):
            dbg = open('dbg.txt', 'w')
        jogPanel.focus()
    
    def OnAdd(self, e):
        global jogPanel
        self.face.faceAdd()
        jogPanel.focus()

class Cutoff():
    def __init__(self, cutoffPanel):
        self.cutoffPanel = cutoffPanel
        global moveCommands
        self.m = moveCommands

    def getCutoffParameters(self):
        cu = self.cutoffPanel
        self.xStart = getFloatVal(cu.xStart) / 2.0
        self.xEnd = getFloatVal(cu.xEnd) / 2.0
        self.xFeed = abs(getFloatVal(cu.xFeed))
        self.xRetract = abs(getFloatVal(cu.xRetract))
        if self.xStart < 0:
            self.xRetract = -self.xRetract

        self.zStart = getFloatVal(cu.zStart)
        self.zCutoff = getFloatVal(cu.zCutoff)

    def cutoff(self):
        self.getCutoffParameters()

        self.safeX = self.xStart + self.xRetract

        if getInfo(cfgDraw):
            self.m.draw("cutoff", self.xStart, self.zStart)

        self.cutoffSetup()

        if self.cutoffPanel.pause.GetValue():
            print("pause")
            self.m.quePause()
        self.m.moveX(self.xEnd, CMD_SYN)
        self.m.moveX(self.safeX)
        self.m.moveZ(self.zStart)

        if STEPPER_DRIVE:
            self.m.stopSpindle()
        self.m.done(1)
        self.m.drawClose()
        stdout.flush()

    def cutoffSetup(self):
        m = self.m
        m.quePause()
        self.m.done(0)
        if STEPPER_DRIVE:
            m.startSpindle(getIntInfo(cuRPM))
            m.queFeedType(FEED_PITCH)
            m.xSynSetup(getFloatInfo(cuXFeed))
        else:
            m.queXSetup(getFloatInfo(cuXFeed))
        m.moveX(self.safeX)
        m.moveZ(self.zCutoff)
        m.moveX(self.xStart)

class CutoffPanel(wx.Panel, FormRoutines):
    def __init__(self, parent, *args, **kwargs):
        super(CutoffPanel, self).__init__(parent, *args, **kwargs)
        self.InitUI()
        self.configList = None
        self.cutoff = Cutoff(self)
        self.formatList = ((cuPause, None), \
                           (cuRPM, 'd'), \
                           (cuXEnd, 'f'), \
                           (cuXFeed, 'f'), \
                           (cuXRetract, 'f'), \
                           (cuXStart, 'f'), \
                           (cuZCutoff, 'f'), \
                           (cuZStart, 'f'))

    def InitUI(self):
        global hdrFont, emptyCell
        self.sizerV = sizerV = wx.BoxSizer(wx.VERTICAL)

        txt = wx.StaticText(self, -1, "Cutoff")
        txt.SetFont(hdrFont)

        sizerV.Add(txt, flag=wx.CENTER|wx.ALL, border=2)

        # x parameters

        sizerG = wx.GridSizer(8, 0, 0)

        self.xStart = self.addField(sizerG, "X Start D", cuXStart)

        self.xEnd = self.addField(sizerG, "X End D", cuXEnd)
        
        self.xFeed = self.addField(sizerG, "X Feed", cuXFeed)
        
        self.xRetract = self.addField(sizerG, "X Retract", cuXRetract)

        # z parameters

        self.zStart = self.addField(sizerG, "Z Start", cuZStart)

        self.zCutoff = self.addField(sizerG, "Z Cutoff", cuZCutoff)

        sizerG.Add(emptyCell)
        sizerG.Add(emptyCell)
        sizerG.Add(emptyCell)
        sizerG.Add(emptyCell)
        
        # buttons

        self.addButton(sizerG, 'Send', self.OnSend)
        # btn = wx.Button(self, label='Send', size=(60,-1))
        # btn.Bind(wx.EVT_BUTTON, self.OnSend)
        # sizerG.Add(btn, flag=wx.CENTER|wx.ALL, border=2)

        self.addButton(sizerG, 'Start', self.OnStart)
        # btn = wx.Button(self, label='Start', size=(60,-1))
        # btn.Bind(wx.EVT_BUTTON, self.OnStart)
        # sizerG.Add(btn, flag=wx.CENTER|wx.ALL, border=2)

        sizerG.Add(emptyCell)
        sizerG.Add(emptyCell)

        self.rpm = self.addField(sizerG, "RPM", cuRPM)

        self.pause = self.addCheckBox(sizerG, "Pause", cuPause)
        # sizerG.Add(wx.StaticText(self, -1, "Pause"), border=2, \
        #            flag=wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.ALL)
        # self.pause = cb = wx.CheckBox(self, -1, \
        #                                  style=wx.ALIGN_LEFT)
        # sizerG.Add(cb, flag=wx.ALIGN_CENTER_VERTICAL|wx.ALL, border=2)
        # initInfo(cuPause, cb)

        sizerV.Add(sizerG, flag=wx.CENTER|wx.ALL, border=2)

        self.SetSizer(sizerV)
        self.sizerV.Fit(self)

    def getConfigList(self):
        if self.configList == None:
            self.configList = []
            for i, (name) in enumerate(configTable):
                if name.startswith('cu'):
                    self.configList.append(i)
        return(self.configList)

    def update(self):
        self.formatData(self.formatList)

    def sendData(self):
        global moveCommands
        try:
            moveCommands.queClear()
            sendClear()
            sendSpindleData()
            sendZData()
            sendXData()
        except CommTimeout:
            commTimeout()

    def OnSend(self, e):
        global xHomed, jogPanel
        if self.formatData(self.formatList):
            if xHomed:
                jogPanel.setStatus(STR_CLR)
                self.sendData()
                self.cutoff.cutoff()
            else:
                jogPanel.setStatus(STR_NOT_HOMED)
        else:
            jogPanel.setStatus(STR_FIELD_ERROR)
        jogPanel.focus()

    def OnStart(self, e):
        global dbg, jogPanel
        command(CMD_RESUME)
        if getBoolInfo(cfgDbgSave):
            dbg = open('dbg.txt', 'w')
        jogPanel.focus()

class Taper(UpdatePass):
    def __init__(self, taperPanel):
        UpdatePass.__init__(self)
        self.taperPanel = taperPanel
        global moveCommands
        self.m = moveCommands
        # morse #3 taper
        # taper = 0.0502
        # length = 3.190
        # largeEnd = .938
        # smallEnd = .778
    
    def getTaperParameters(self, taperInch):
        tp = self.taperPanel
        # taper = x / z
        # taperInch = totalTaper / self.zLength
        # taperX True  - move z taper x
        # taperX False - move x taper z
        self.taperX = taperInch <= 1.0
        self.taper = taperInch
        self.backInc = 0.002

        self.zStart = getFloatVal(tp.zStart)
        self.zLength = getFloatVal(tp.zLength)
        self.zEnd = self.zStart - self.zLength
        self.zLength = abs(self.zLength)
        self.zFeed = abs(getFloatVal(tp.zFeed))
        self.zRetract = abs(getFloatVal(tp.zRetract))

        self.largeDiameter = getFloatVal(tp.largeDiam)
        self.smallDiameter = getFloatVal(tp.smallDiam)
        self.xFeed = getFloatVal(tp.xFeed) / 2.0
        self.xRetract = abs(getFloatVal(tp.xRetract))

        self.finish = abs(getFloatVal(tp.finish))
        self.pause = self.taperPanel.pause.GetValue()

        totalTaper = taperInch * self.zLength
        print("taperX %s totalTaper %5.3f taperInch %6.4f" % \
              (self.taperX, totalTaper, taperInch))

    def taperSetup(self):
        m = self.m
        m.setLoc(self.zEnd, self.xStart)
        m.drawLineZ(self.zStart, REF)
        m.drawLineX(self.xEnd, REF)
        m.setLoc(self.safeZ, self.safeX)
        m.quePause()
        self.m.done(0)
        if self.taperX:
            m.saveTaper(self.taper)
        else:
            m.saveTaper(1.0 / self.taper)
        m.startSpindle(getIntInfo(tpRPM))
        m.queFeedType(FEED_PITCH)

        m.zSynSetup(getFloatInfo(tpZFeed))
        m.xSynSetup(getFloatInfo(tpXInFeed))

        m.moveX(self.safeX)
        m.moveZ(self.safeZ)
        m.text("%0.3f" % (self.zStart), \
               (self.zStart, self.xEnd), \
               CENTER | (ABOVE if self.internal else BELOW))
        m.text("%0.3f" % (self.safeZ), \
               (self.safeZ, self.safeX), \
               CENTER | (BELOW if self.internal else ABOVE))
        m.text("%0.3f" % (self.xStart * 2.0), \
               (self.zEnd, self.xStart), RIGHT | MIDDLE)
        m.text("%0.3f Feed %0.3f" % (self.safeX * 2.0, self.actualFeed), \
               (self.safeZ, self.safeX), ABOVE if self.internal else BELOW)
        m.text("%0.3f" % (self.zEnd), \
               (self.zEnd, self.safeX), RIGHT | MIDDLE)

    def externalTaper(self, taperInch):
        print("externalTaper")
        self.internal = False
        self.getTaperParameters(taperInch)

        self.xStart = self.largeDiameter / 2.0
        self.xEnd = self.smallDiameter / 2.0

        if self.taperX:
            zCut = self.zLength * taperInch # x feed from z length
            xCut = self.xStart - self.xEnd  # x feed from start - end
            self.cut = min(zCut, xCut)      # choose minimum

            feed = self.xFeed
            finish = self.finish / 2
        else:
            zCut = self.zLength # z feed from length
            self.xLength = self.xStart - self.xEnd
            xCut = self.xLength / taperInch # z feed from x
            self.cut = min(zCut, xCut) # choose minimum

            feed = self.zFeed
            finish = self.finish

        self.safeZ = self.zStart + self.zRetract
        self.safeX = self.xStart + self.xRetract

        self.calcFeed(feed, self.cut, finish)
        self.setupSpringPasses(self.taperPanel)
        self.setupAction(self.calcExternalPass, self.externalPass)

        self.taperPanel.passes.SetValue("%d" % (self.passes))
        print("passes %d cutAmount %5.3f feed %6.3f" % \
              (self.passes, self.cutAmount, self.actualFeed))

        if getInfo(cfgDraw):
            self.m.draw("taper", self.zStart, self.taper)
            
        self.taperSetup()

        while self.updatePass():
            pass

        self.m.printXText("%2d %7.4f %7.4f", LEFT, False)
        self.m.printZText("%2d %7.4f", LEFT|MIDDLE)
        self.m.moveZ(self.safeZ)
        if STEPPER_DRIVE:
            self.m.stopSpindle()
        self.m.done(1)
        self.m.drawClose()
        stdout.flush()

    def calcExternalPass(self, final=False):
        if self.taperX:
            feed = self.cutAmount if final else self.passCount * self.actualFeed
            self.feed = feed
            self.endX = self.xStart - feed
            self.taperLength = self.feed / self.taper
            if self.taperLength < self.zLength:
                self.startZ = self.zStart - self.taperLength
                self.startX = self.xStart
            else:
                self.startZ = self.zStart - self.zLength
                self.startX = self.endX + self.taper * self.zLength
        else:
            feed = self.cutAmount if final else self.passCount * self.actualFeed
            self.feed = feed
            self.startZ = self.zStart - feed
            self.startX = self.xStart
            self.endZ = self.zStart
            taperLength = self.feed * self.taper
            self.endX = self.xStart - taperLength \
                        if taperLength < self.xLength else self.xEnd
        print("%2d start (%6.3f,%6.3f) end (%6.3f %6.3f) "\
              "%6.3f %6.3f" % \
              (self.passCount, self.startZ, self.startX, \
               self.endZ, self.endX, 2.0 * self.startX, 2.0 * self.endX))

    def externalPass(self):
        m = self.m
        m.moveZ(self.startZ - self.backInc) # move past start
        m.moveZ(self.startZ, CMD_JOG) # move to takeout backlash
        if self.pause:
            print("pause")
            m.quePause()
        if self.taperX:
            if m.passNum & 0x300 == 0:
                if self.taperLength < self.zLength:
                    m.text("%2d %7.3f" % (m.passNum, self.startZ), \
                           (self.startZ, self.safeX), CENTER | ABOVE)
                else:
                    m.text("%2d %7.3f" % (m.passNum, self.startX * 2.0), \
                           (self.endZ, self.startX), RIGHT)
            m.moveX(self.startX, CMD_SYN)
            m.taperZX(self.endZ, self.endX)
        else:
            if m.passNum & 0x300 == 0:
                m.saveZText((m.passNum, self.startZ), \
                            (self.startZ, self.safeX))
            m.moveX(self.startX)
            m.taperXZ(self.endX, self.endZ)
        m.drawLine(self.endZ, self.endX)
        m.moveZ(self.safeZ)
        if m.passNum & 0x300 == 0:
            m.saveXText((m.passNum, self.endX * 2.0, self.endX), \
                       (self.safeZ, self.endX))
        m.moveX(self.safeX)

    def externalAdd(self):
        if self.feed >= self.cutAmount:
            add = getFloatVal(self.taperPanel.add) / 2
            self.cutAmount += add
            self.taperSetup()
            self.calcExternalPass(True)
            self.externalPass()
            if self.taperX:
                self.m.moveX(self.safeX)
                self.m.moveZ(self.startZ)
            else:
                pass
            self.m.stopSpindle();
            command(CMD_RESUME)

    def internalTaper(self, taperInch):
        print("internalTaper")
        self.internal = True
        self.getTaperParameters(taperInch)

        self.boreRadius = self.xStart = self.largeDiameter / 2.0
        self.xEnd = self.smallDiameter / 2.0
        self.cut = self.xEnd - self.boreRadius

        self.calcFeed(self.xFeed, self.cut, self.finish)
        self.setupSpringPasses(self.taperPanel)
        self.setupAction(self.calcInternalPass, self.internalPass)

        self.taperPanel.passes.SetValue("%d" % (self.passes))
        print("passes %d cutAmount %5.3f feed %6.3f" % \
              (self.passes, self.cutAmount, self.actualFeed))

        self.endZ = self.zStart

        self.safeX = self.boreRadius - self.xRetract
        self.safeZ = self.zStart + self.zRetract

        if getInfo(cfgDraw):
            self.m.draw("taper", self.zStart, self.taper)
            
        self.taperSetup()

        while self.updatePass():
            pass

        self.m.printXText("%2d %7.4f %7.4f", LEFT, True)
        self.m.printZText("%2d %7.4f %7.4f %7.4f", RIGHT|MIDDLE)
        self.m.moveX(self.safeX)
        self.m.moveZ(self.safeZ)
        self.m.stopSpindle();
        self.m.done(1)
        self.m.drawClose()
        stdout.flush()

    def calcInternalPass(self, final=False):
        feed = self.cutAmount if final else self.passCount * self.actualFeed
        self.feed = feed
        self.endX = self.boreRadius + feed
        self.startZ = self.zStart - self.feed / self.taper
        if self.startZ > self.zEnd:
            self.startX = self.boreRadius
        else:
            self.startZ = self.zEnd
            self.startX = (self.boreRadius + self.feed - \
                           self.zLength * self.taper)
        print("%2d feed %6.3f start (%6.3f,%6.3f) end (%6.3f %6.3f) "\
              "%6.3f %6.3f" % \
              (self.passCount, self.feed, self.startX, self.startZ, \
               self.endX, self.endZ, \
               2.0 * self.startX, 2.0 * self.endX))

    def internalPass(self):
        m = self.m
        m.moveZ(self.startZ - self.backInc) # past the start point
        m.moveZ(self.startZ, CMD_JOG) # back to start to remove backlash
        m.moveX(self.startX, CMD_SYN)
        if self.pause:
            print("pause")
            m.quePause()
        if m.passNum & 0x300 == 0:
            m.saveZText((m.passNum, self.startZ, self.startX, \
                         self.startX * 2.0), (self.startZ, self.safeX))
        m.taperZX(self.endZ, self.endX) if self.taperX else \
            m.taperXZ(self.endX, self.endZ)
        m.drawLine(self.endZ, self.endX)
        if m.passNum & 0x300 == 0:
            m.saveXText((m.passNum, self.endX * 2.0, self.endX), \
                        (self.safeZ, self.endX))
        m.moveZ(self.safeZ)
        m.moveX(self.safeX)

    def internalAdd(self):
        if self.feed >= self.cutAmount:
            add = getFloatVal(self.taperPanel.add) / 2
            self.feed += add
            self.passCount += 1
            self.taperSetup()
            self.m.moveZ(self.safeZ)
            self.calcInternalPass()
            self.internalPass()
            self.m.moveX(self.safeX)
            self.m.moveZ(self.safeZ)
            self.m.stopSpindle();
            command(CMD_RESUME)
            stdout.flush()

class TaperPanel(wx.Panel, FormRoutines):
    def __init__(self, parent, *args, **kwargs):
        super(TaperPanel, self).__init__(parent, *args, **kwargs)
        self.taperDef = [("Custom",), \
                         ("MT1",  0.4750, 0.3690, 2.13, 0.5986/12), \
                         ("MT2",  0.7000, 0.5720, 2.56, 0.5994/12), \
                         ("MT3",  0.9380, 0.7780, 3.19, 0.6024/12), \
                         ("MT4",  1.2310, 1.0200, 4.06, 0.5233/12), \
                         ("BS5",  0.5388, 0.4500, 2.13, 0.5016/12), \
                         ("BS11", 1.4978, 1.2500, 5.94, 0.5010/12), \
                         ("5C",   1.4800, 1.2500, 0.61, 20.0), \
                         ("ER32", 1.2598, 0.9252, 0, 16.0), \
                         ("R8",   1.2500, 0.9400, 0.95, 16.51), \
                         ("", 0., 0., 0, 0.), \
                         ("", 0., 0., 0, 0.), \
                         ("", 0., 0., 0, 0.), \
        ]
        self.taperList = []
        for t in self.taperDef:
            self.taperList.append(t[0])
        self.InitUI()
        self.configList = None
        self.taper = Taper(self)
        self.m = moveCommands
        self.formatList = ((tpAddFeed, 'f'), \
                           (tpAngle, 'fs'), \
                           (tpAngleBtn, None), \
                           (tpDeltaBtn, None), \
                           (tpInternal, None), \
                           (tpLargeDiam, 'f'), \
                           (tpLargeDiamText, None), \
                           (tpPasses, 'd'), \
                           (tpPause, None), \
                           (tpRPM, 'd'), \
                           (tpSPInt, 'd'), \
                           (tpSmallDiam, 'f'), \
                           (tpSmallDiamText, None), \
                           (tpSpring, 'd'), \
                           (tpTaperSel, None), \
                           (tpXDelta, 'f6'), \
                           (tpXFeed, 'f'), \
                           (tpXFinish, 'f'), \
                           (tpXInFeed, 'f'), \
                           (tpXRetract, 'f'), \
                           (tpZDelta, 'f'), \
                           (tpZFeed, 'f'), \
                           (tpZLength, 'f'), \
                           (tpZRetract, 'f'), \
                           (tpZStart, 'f'))

    def InitUI(self):
        global hdrFont, info
        self.sizerV = sizerV = wx.BoxSizer(wx.VERTICAL)

        txt = wx.StaticText(self, -1, "Taper")
        txt.SetFont(hdrFont)

        sizerV.Add(txt, flag=wx.CENTER|wx.ALL, border=2)

        sizerH = wx.BoxSizer(wx.HORIZONTAL)

        txt = wx.StaticText(self, -1, "Select Taper")
        sizerH.Add(txt, flag=wx.ALL|wx.ALIGN_CENTER_VERTICAL, border=2)

        self.taperSel = combo = wx.ComboBox(self, -1, self.taperList[0], \
                                            choices=self.taperList, \
                                            style=wx.CB_READONLY)
        initInfo(tpTaperSel, combo)
        combo.Bind(wx.EVT_COMBOBOX, self.OnCombo)
        sizerH.Add(combo, flag=wx.ALL, border=2)

        sizerV.Add(sizerH, flag=wx.CENTER|wx.ALL, border=2)
 
        sizerG = wx.GridSizer(8, 0, 0)

        # z parameters

        self.zStart = self.addField(sizerG, "Z Start", tpZStart)

        self.zLength = self.addField(sizerG, "Z Length", tpZLength)
        
        self.zFeed = self.addField(sizerG, "Z Feed", tpZFeed)
        
        self.zRetract = self.addField(sizerG, "Z Retract", tpZRetract)

        # x parameters

        self.largeDiam = self.addFieldText(sizerG, "Large Diam", \
                                           tpLargeDiam, tpLargeDiamText)

        self.smallDiam = self.addFieldText(sizerG, "Small Diam", \
                                           tpSmallDiam, tpSmallDiamText)

        self.xInFeed = self.addField(sizerG, "X In Feed R", tpXInFeed)

        self.xFeed = self.addField(sizerG, "X Pass D", tpXFeed)

        # taper parameters

        self.deltaBtn = btn = wx.RadioButton(self, label="Z")
        sizerG.Add(btn, flag=wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.ALL, \
                   border=2)
        btn.Bind(wx.EVT_RADIOBUTTON, self.OnDelta)
        initInfo(tpDeltaBtn, btn)

        self.zDelta = self.addField(sizerG, "", tpZDelta)
        self.zDelta.Bind(wx.EVT_KILL_FOCUS, self.OnDeltaFocus)

        self.xDelta = self.addField(sizerG, "X", tpXDelta)
        self.xDelta.Bind(wx.EVT_KILL_FOCUS, self.OnDeltaFocus)

        self.angleBtn = btn = wx.RadioButton(self, label="Angle")
        sizerG.Add(btn, flag=wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.ALL, \
                   border=2)
        btn.Bind(wx.EVT_RADIOBUTTON, self.OnAngle)
        initInfo(tpAngleBtn, btn)

        self.angle = self.addField(sizerG, "", tpAngle)
        self.angle.Bind(wx.EVT_KILL_FOCUS, self.OnAngleFocus)

        self.xRetract = self.addField(sizerG, "X Retract", tpXRetract)
        
        # pass info

        self.passes = self.addField(sizerG, "Passes", tpPasses)
        self.passes.SetEditable(False)

        self.sPInt = self.addField(sizerG, "SP Int", tpSPInt)

        self.spring = self.addField(sizerG, "Spring", tpSpring)

        self.finish = self.addField(sizerG, "Finish", tpXFinish)

        # control buttons

        self.addButton(sizerG, 'Send', self.OnSend)
        # btn = wx.Button(self, label='Send', size=(60,-1))
        # btn.Bind(wx.EVT_BUTTON, self.OnSend)
        # sizerG.Add(btn, flag=wx.CENTER|wx.ALL, border=2)

        self.addButton(sizerG, 'Start', self.OnStart)
        # btn = wx.Button(self, label='Start', size=(60,-1))
        # btn.Bind(wx.EVT_BUTTON, self.OnStart)
        # sizerG.Add(btn, flag=wx.CENTER|wx.ALL, border=2)

        self.addButton(sizerG, 'Add', self.OnAdd)
        # btn = wx.Button(self, label='Add', size=(60,-1))
        # btn.Bind(wx.EVT_BUTTON, self.OnAdd)
        # sizerG.Add(btn, flag=wx.CENTER|wx.ALL, border=2)

        self.add = self.addField(sizerG, "", tpAddFeed)

        self.rpm = self.addField(sizerG, "RPM", tpRPM)

        sizerH = wx.BoxSizer(wx.HORIZONTAL)

        self.pause = self.addCheckBox(sizerH, "Internal", tpInternal)
        # sizerH.Add(wx.StaticText(self, -1, "Internal"), border=2, \
        #            flag=wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.ALL)
        # self.internal = cb = wx.CheckBox(self, -1, \
        #                                  style=wx.ALIGN_LEFT)
        # self.Bind(wx.EVT_CHECKBOX, self.OnInternal, cb)
        # sizerH.Add(cb, flag=wx.ALIGN_CENTER_VERTICAL|wx.ALL, border=2)
        # initInfo(tpInternal, cb)

        sizerG.Add(sizerH)

        sizerH = wx.BoxSizer(wx.HORIZONTAL)

        self.pause = self.addCheckBox(sizerH, "Pause", tpPause)
        # sizerH.Add(wx.StaticText(self, -1, "Pause"), border=2, \
        #            flag=wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.ALL)
        # self.pause = cb = wx.CheckBox(self, -1, \
        #                                  style=wx.ALIGN_LEFT)
        # sizerH.Add(cb, flag=wx.ALIGN_CENTER_VERTICAL|wx.ALL, border=2)
        # initInfo(tpPause, cb)

        sizerG.Add(sizerH)
        # sizerG.Add(wx.StaticText(self, -1), border=2)

        # btn = wx.Button(self, label='Debug', size=(60,-1))
        # btn.Bind(wx.EVT_BUTTON, self.OnDebug)
        # sizerG.Add(btn, flag=wx.CENTER|wx.ALL, border=2)

        sizerV.Add(sizerG, flag=wx.CENTER|wx.ALL, border=2)

        self.SetSizer(sizerV)
        sizerV.Fit(self)

    def getConfigList(self):
        if self.configList == None:
            self.configList = []
            for i, (name) in enumerate(configTable):
                if name.startswith('ta'):
                    self.configList.append(i)
        return(self.configList)

    def update(self):
        self.updateUI()
        self.updateDelta()
        self.updateAngle()
        self.formatData(self.formatList)

    def updateUI(self):
        global info
        val = self.deltaBtn.GetValue()
        self.zDelta.SetEditable(val)
        self.xDelta.SetEditable(val)
        self.angle.SetEditable(not val)
        if self.internal.GetValue():
            infoSetLabel(tpLargeDiamText, "Bore Diam")
            infoSetLabel(tpSmallDiamText, "Large Diam")
        else:
            infoSetLabel(tpLargeDiamText, "Large Diam")
            infoSetLabel(tpSmallDiamText, "Small Diam")
        self.sizerV.Layout()

    def updateAngle(self):
        if self.angleBtn.GetValue():
            try:
                angle = getFloatVal(self.angle)
                deltaX = tan(radians(angle))
                self.zDelta.ChangeValue("1.000")
                self.xDelta.ChangeValue("%0.5f" % (deltaX))
            except ValueError:
                pass

    def updateDelta(self):
        if self.deltaBtn.GetValue():
            deltaZ = getFloatVal(self.zDelta)
            deltaX = getFloatVal(self.xDelta)
            try:
                angle = degrees(atan2(deltaX, deltaZ))
                self.angle.ChangeValue("%5.3f" % (angle))
            except:
                pass

    def OnCombo(self, e):
        index = self.taperSel.GetSelection()
        if index != 0:
            (name, large, small, length, taper) = self.taperDef[index]
            self.zLength.SetValue("%0.3f" % (length))
            self.largeDiam.SetValue("%0.3f" % (large))
            self.smallDiam.SetValue("%0.3f" % (small))
            if taper < 1.0:
                self.deltaBtn.SetValue(True)
                self.zDelta.SetValue("1.000")
                self.xDelta.SetValue("%0.5f" % (taper / 2))
            else:
                self.angleBtn.SetValue(True)
                self.angle.SetValue("%0.3f" % (taper / 2))
            self.update()

    def OnDeltaFocus(self, e):
        self.updateDelta()
        e.Skip()

    def OnAngleFocus(self, e):
        self.updateAngle()
        e.Skip()

    def OnInternal(self, e):
        self.updateUI()

    def OnDelta(self, e):
        self.updateUI()

    def OnAngle(self, e):
        self.updateUI()

    def sendData(self):
        global moveCommands
        try:
            moveCommands.queClear()
            sendClear()
            sendSpindleData()
            sendZData()
            sendXData()

        except CommTimeout:
            commTimeout()

    def OnSend(self, e):
        global xHomed, jogPanel
        if self.formatData(self.formatList):
            if xHomed:
                jogPanel.setStatus(STR_CLR)
                self.sendData()
                taper = getFloatVal(self.xDelta) / getFloatVal(self.zDelta)
                self.taper.internalTaper(taper) \
                    if self.internal.GetValue() else \
                       self.taper.externalTaper(taper)
            else:
                jogPanel.setStatus(STR_NOT_HOMED)
        else:
            jogPanel.setStatus(STR_FIELD_ERROR)
        jogPanel.focus()

    def OnStart(self, e):
        global dbg, jogPanel
        command(CMD_RESUME)
        if getBoolInfo(cfgDbgSave):
            dbg = open('dbg.txt', 'w')
        jogPanel.focus()
    
    def OnAdd(self, e):
        global jogPanel
        self.taper.internalAdd() if self.internal.GetValue() else \
            self.taper.externalAdd()
        jogPanel.focus()

    # def OnDebug(self, e):
    #     self.sendData()
    #     moveX(1.000)
    #     moveZ(0.010)
    #     taperZX(-0.25, 0.0251)

REF   = 'REF'
TEXT  = 'TEXT'

class ScrewThread(UpdatePass):
    def __init__(self, threadPanel):
        UpdatePass.__init__(self)
        self.threadPanel = threadPanel
        global moveCommands
        self.m = moveCommands
        self.d = None

    def draw(self, diam, tpi):
        tmp = "tfeed%0.3f-%0.1f" % (diam, tpi)
        tmp = tmp.replace("." , "-")
        tmp = re.sub("-0$", "", tmp) + ".dxf"
        d = dxf.drawing(tmp)
        d.add_layer(REF, color=0)
        d.add_layer(TEXT, color=0)
        self.d = d

    def drawLine(self, p0, p1, layer=0):
        if self.d != None:
            self.d.add(dxf.line(p0, p1, layer=layer))

    def drawClose(self):
        try:
            if self.d != None:
                self.d.save()
                self.d = None
        except:
            print("dxf file save error")

    def getThreadParameters(self):
        th = self.threadPanel
        self.internal = th.internal.GetValue()

        self.zStart = getFloatVal(th.zStart)
        self.zEnd = getFloatVal(th.zEnd)
        self.zRetract = getFloatVal(th.zRetract)
        self.zAccel = 0.0
        self.zBackInc = 0.003
        self.safeZ = self.zStart + self.zRetract

        if th.tpi.GetValue():
            self.tpi = getFloatVal(th.thread)
            self.pitch = 1.0 / self.tpi
        else:
            self.pitch = getFloatVal(th.thread) / 25.4
            self.tpi = 1.0 / self.pitch
        
        self.xStart = getFloatVal(th.xStart) / 2.0

        self.firstFeed = getFloatVal(th.firstFeed)
        self.lastFeed = getFloatVal(th.lastFeed)
        self.depth = getFloatVal(th.depth)

        self.xEnd = self.xStart + self.depth if self.internal else \
                    self.xStart - self.depth

        self.xRetract = abs(getFloatVal(th.xRetract))
        
        self.angle = radians(getFloatVal(th.angle))

    def thread(self):
        self.getThreadParameters()

        print("tpi %4.1f pitch %5.3f lastFeed %6.4f" % \
              (self.tpi, self.pitch, self.lastFeed))
        
        if self.depth == 0:
            self.depth = (cos(self.angle) * self.pitch)
        self.tanAngle = tan(self.angle)
        actualWidth = 2 * self.depth * self.tanAngle
        self.safeZ += actualWidth / 2.0
        self.area = area = 0.5 * self.depth * actualWidth
        print("depth %6.4f actualWdith %6.4f area %8.6f" % \
              (self.depth, actualWidth, area))
        
        firstWidth = 2 * self.firstFeed * self.tanAngle
        firstArea = 0.5 * self.firstFeed * firstWidth
        passes = int(ceil(area / firstArea))
        print("firstFeed %6.4f firstWidth %6.4f firstArea %8.6f passes %d" % \
              (self.firstFeed, firstWidth, firstArea, passes))
        
        lastDepth = self.depth - self.lastFeed
        lastArea = (lastDepth * lastDepth) * self.tanAngle
        self.areaPass = area - lastArea
        print("area %8.6f lastDepth %6.4f lastArea %8.6f areaPass %8.6f" % \
              (area, lastDepth, lastArea, self.areaPass))

        self.passes = int(ceil(area / self.areaPass))
        self.threadPanel.passes.SetValue("%d" % (self.passes))
        self.areaPass = area / self.passes
        print("passes %d areaPass %8.6f" % \
              (self.passes, self.areaPass))
        
        self.setupSpringPasses(self.threadPanel)
        self.setupAction(self.calculateThread, self.threadPass)
        self.initPass()

        if self.internal:
            self.xRetract = -self.xRetract
        
        self.safeX = self.xStart + self.xRetract
        self.startZ = self.zStart + self.zAccel

        if getInfo(cfgDraw):
            self.draw(self.xStart * 2.0, self.tpi)
            self.p0 = (0, 0)

        if getInfo(cfgDraw):
            self.m.draw("threada", self.xStart * 2.0, self.tpi)
            
        self.threadSetup()

        self.curArea = 0.0
        self.prevFeed = 0.0
        print("pass     area  xfeed  zfeed  delta")

        while self.updatePass():
            pass

        self.m.printXText("%2d Z %6.4f Zofs %6.4f D %6.4f F %6.4f", \
                          LEFT, self.internal)
            
        self.drawClose()
        self.m.drawClose()
        self.m.stopSpindle();
        self.m.done(1)
        stdout.flush()

    def threadSetup(self, add=False):
        m = self.m
        if not add:
            m.setLoc(self.zEnd, self.xStart)
            m.drawLineZ(self.zStart, REF)
            m.drawLineX(self.xEnd, REF)
            m.setLoc(self.safeZ, self.safeX)
        m.quePause()
        self.m.done(0)
        m.startSpindle(getIntInfo(thRPM))
        feedType = FEED_TPI if self.threadPanel.tpi.GetValue() else FEED_METRIC
        m.queFeedType(feedType)
        m.saveTaper(getFloatInfo(thXTaper))
        m.saveRunout(getFloatInfo(thExitRev))
        m.saveDepth(self.depth)
        m.zSynSetup(getFloatInfo(thPitch))
        m.moveX(self.safeX)
        m.moveZ(self.safeZ)
        if not add:
            m.text("%7.3f" % (self.xStart * 2.0), \
                   (self.zEnd, self.xStart), RIGHT)
            m.text("%0.3f" % (self.zStart), \
                   (self.zStart, self.xEnd), \
                   CENTER | (ABOVE if self.internal else BELOW))
            m.text("%7.3f" % (self.safeX * 2.0,), \
                   (self.safeZ, self.safeX))
            m.text("%7.3f" % (self.zEnd), \
                   (self.zEnd, self.safeX), \
                   CENTER | (BELOW if self.internal else ABOVE))

    def calculateThread(self, final=False, add=False):
        if not add:
            if final:
                self.curArea = self.area
            else:
                self.curArea += self.areaPass
            feed = sqrt(self.curArea / self.tanAngle)
            self.feed = feed
        else:
            feed = self.feed

        if True:
            self.zOffset = feed * self.tanAngle
        else:
            offset = (feed - self.prevFeed) * self.tanAngle
            if self.passCount & 1:
                offset = -offset
            self.zOffset += offset

        print("%4d %8.6f %6.4f %6.4f %6.4f" % \
              (self.passCount, self.curArea, feed, self.zOffset, \
               feed - self.prevFeed))
        self.prevFeed = feed
        if self.internal:
            feed = -feed
        self.curX = self.xStart - feed

        if self.d != None:
            p1 = (self.zOffset, feed)
            pa = (self.zOffset - feed * self.tanAngle, 0)
            pb = (self.zOffset + feed * self.tanAngle, 0)
            self.drawLine(self.p0, p1)
            self.drawLine(p1, pa)
            self.drawLine(p1, pb)
            self.p0 = p1

    def threadPass(self):
        m = self.m
        startZ = self.safeZ - self.zOffset
        self.m.moveZ(startZ + self.zBackInc)
        self.m.moveZ(startZ)
        self.m.moveX(self.curX, CMD_JOG)
        if self.threadPanel.pause.GetValue():
            print("pause")
            self.m.quePause()
        if m.passNum & 0x300 == 0:
            m.saveXText((m.passNum, startZ, self.zOffset, \
                        self.curX * 2.0, self.feed), (self.safeZ, self.curX))
        self.m.moveZ(self.zEnd, CMD_SYN | Z_SYN_START)
        self.m.moveX(self.safeX)

    def threadAdd(self):
        try:
            curPass = getParm(CURRENT_PASS)
            if curPass >= self.passes:
                add = getFloatVal(self.threadPanel.add)
                self.feed += add
                self.threadSetup(True)
                self.calculateThread(add=True)
                self.threadPass()
                self.m.stopSpindle();
                self.m.done(1)
                command(CMD_RESUME)
            else:
                jogPanel.setStatus(STR_NO_ADD)
        except CommTimeout:
            commTimeout()
        stdout.flush()

class ThreadPanel(wx.Panel, FormRoutines):
    def __init__(self, parent, *args, **kwargs):
        super(ThreadPanel, self).__init__(parent, *args, **kwargs)
        self.InitUI()
        self.Bind(wx.EVT_SHOW, self.OnShow)
        self.configList = None
        self.active = False
        self.screwThread = ScrewThread(self)
        self.formatList =  ((thAddFeed, 'f'), \
                            (thAngle, 'fs'), \
                            (thExitRev, 'fs'), \
                            (thHFactor, 'f'), \
                            (thInternal, None), \
                            (thMM, None), \
                            (thPasses, 'd'), \
                            (thPause, None), \
                            (thPitch, 'fs'), \
                            (thRPM, 'd'), \
                            (thSPInt, 'n'), \
                            (thSpring, 'n'), \
                            (thTPI, None), \
                            (thXDepth, 'f'), \
                            (thXFirstFeed, 'f'), \
                            (thXLastFeed, 'f'), \
                            (thXRetract, 'f'), \
                            (thXStart, 'f'), \
                            (thXTaper, 'f'), \
                            (thZEnd, 'f'), \
                            (thZRetract, 'f'), \
                            (thZStart, 'f'))

    def InitUI(self):
        global hdrFont, info, emptyCell
        self.sizerV = sizerV = wx.BoxSizer(wx.VERTICAL)

        txt = wx.StaticText(self, -1, "Thread")
        txt.SetFont(hdrFont)

        sizerV.Add(txt, flag=wx.CENTER|wx.ALL, border=2)

        # z parameters

        sizerG = wx.GridSizer(8, 0, 0)

        self.zEnd = self.addField(sizerG, "Z End", thZEnd)
        
        self.zStart = self.addField(sizerG, "Z Start", thZStart)

        self.zRetract = self.addField(sizerG, "Z Retract", thZRetract)

        self.pause = self.addCheckBox(sizerG, "Internal", thInternal)
        # sizerG.Add(wx.StaticText(self, -1, "Internal"), border=2, \
        #            flag=wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.ALL)
        # self.internal = cb = wx.CheckBox(self, -1, \
        #                                  style=wx.ALIGN_LEFT)
        # self.Bind(wx.EVT_CHECKBOX, self.OnInternal, cb)
        # sizerG.Add(cb, flag=wx.ALIGN_CENTER_VERTICAL|wx.ALL, border=2)
        # initInfo(thInternal, cb)

        # x parameters

        self.xStart = self.addField(sizerG, "X Start D", thXStart)

        self.xRetract = self.addField(sizerG, "X Retract", thXRetract)

        self.depth = self.addField(sizerG, "Depth", thXDepth)

        self.firstFeed = self.addField(sizerG, "First Feed", thXFirstFeed)

        # self.final = btn = wx.RadioButton(self, label="Final", \
        #                                   style = wx.RB_GROUP)
        # sizerH.Add(btn, flag=wx.CENTER|wx.ALL, border=2)
        # initInfo(thFinal, btn)

        # self.depth = btn = wx.RadioButton(self, label="Depth")
        # sizerH.Add(btn, flag=wx.CENTER|wx.ALL, border=2)
        # initInfo(thDepth, btn)

        self.thread = self.addField(sizerG, "Thread", thPitch)
        
        self.tpi = btn = wx.RadioButton(self, label="TPI", style = wx.RB_GROUP)
        sizerG.Add(btn, flag=wx.ALIGN_CENTER_VERTICAL|wx.ALL, border=2)
        initInfo(thTPI, btn)

        self.mm = btn = wx.RadioButton(self, label="mm")
        sizerG.Add(btn, flag=wx.ALIGN_CENTER_VERTICAL|wx.ALL, border=2)
        initInfo(thMM, btn)

        self.angle = self.addField(sizerG, "Angle", thAngle)

        sizerG.Add(emptyCell)
        sizerG.Add(emptyCell)

        #

        self.xTaper = self.addField(sizerG, "Taper", thXTaper)

        self.xExitRev = self.addField(sizerG, "Exit Rev", thExitRev)
        
        self.lastFeed = self.addField(sizerG, "Last Feed", thXLastFeed)

        sizerG.Add(emptyCell)
        sizerG.Add(emptyCell)

        # pass info

        self.passes = self.addField(sizerG, "Passes", thPasses)
        self.passes.SetEditable(False)

        self.sPInt = self.addField(sizerG, "SP Int", thSPInt)

        self.spring = self.addField(sizerG, "Spring", thSpring)

        sizerG.Add(emptyCell)
        sizerG.Add(emptyCell)

        # buttons

        self.addButton(sizerG, 'Send', self.OnSend)
        # btn = wx.Button(self, label='Send', size=(60,-1))
        # btn.Bind(wx.EVT_BUTTON, self.OnSend)
        # sizerG.Add(btn, flag=wx.CENTER|wx.ALL, border=2)

        self.addButton(sizerG, 'Start', self.OnStart)
        # btn = wx.Button(self, label='Start', size=(60,-1))
        # btn.Bind(wx.EVT_BUTTON, self.OnStart)
        # sizerG.Add(btn, flag=wx.CENTER|wx.ALL, border=2)

        self.addButton(sizerG, 'Add', self.OnAdd)
        # btn = wx.Button(self, label='Add', size=(60,-1))
        # btn.Bind(wx.EVT_BUTTON, self.OnAdd)
        # sizerG.Add(btn, flag=wx.CENTER|wx.ALL, border=2)

        self.add = self.addField(sizerG, "", thAddFeed)

        self.rpm = self.addField(sizerG, "RPM", thRPM)

        self.pause = self.addCheckBox(sizerG, "Pause", thPause)
        # sizerG.Add(wx.StaticText(self, -1, "Pause"), border=2, \
        #            flag=wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.ALL)
        # self.pause = cb = wx.CheckBox(self, -1, \
        #                                  style=wx.ALIGN_LEFT)
        # sizerG.Add(cb, flag=wx.ALIGN_CENTER_VERTICAL|wx.ALL, border=2)
        # initInfo(thPause, cb)

        sizerV.Add(sizerG, flag=wx.CENTER|wx.ALL, border=2)

        self.SetSizer(sizerV)
        self.sizerV.Fit(self)

    def OnShow(self, e):
        if done:
            return
        if not self.IsShown():
            self.active = False
            print("OnShow clear active")
            stdout.flush()

    def getConfigList(self):
        if self.configList == None:
            self.configList = []
            for i, (name) in enumerate(configTable):
                if name.startswith('th'):
                    self.configList.append(i)
        return(self.configList)

    def update(self):
        self.formatData(self.formatList)

    def OnInternal(self, e):
        pass

    def sendData(self):
        moveCommands.queClear()
        sendClear()
        sendSpindleData()
        sendZData()
        sendXData()

    def OnSend(self, e):
        global xHomed, jogPanel
        if self.formatData(self.formatList):
            if not xHomed:
                jogPanel.setStatus(STR_NOT_HOMED)
            elif self.active or jogPanel.mvStatus & (MV_ACTIVE | MV_PAUSE):
                jogPanel.setStatus(STR_OP_IN_PROGRESS)
            else:
                jogPanel.setStatus(STR_CLR)
                self.active = True
                try:
                    self.sendData()
                    self.screwThread.thread()
                except CommTimeout:
                    commTimeout()
        else:
            jogPanel.setStatus(STR_FIELD_ERROR)
        jogPanel.focus()

    def OnStart(self, e):
        global dbg, jogPanel
        if not self.active:
            jogPanel.setStatus(STR_NOT_SENT)
        elif (jogPanel.mvStatus & MV_PAUSE) == 0:
            jogPanel.setStatus(STR_NOT_PAUSED)
        else:
            jogPanel.setStatus(STR_CLR)
            command(CMD_RESUME)
            if getBoolInfo(cfgDbgSave):
                dbg = open('dbg.txt', 'w')
        jogPanel.focus()
    
    def OnAdd(self, e):
        global jogPanel
        if not self.active:
            jogPanel.setStatus(STR_OP_NOT_ACTIVE)
        elif jogPanel.mvStatus & (MV_ACTIVE | MV_PAUSE):
            jogPanel.setStatus(STR_OP_IN_PROGRESS)
        else:
            jogPanel.setStatus(STR_CLR)
            self.screwThread.threadAdd()
        jogPanel.focus()

class ButtonRepeat(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.threadRun = True
        self.event = Event()
        self.action = None
        self.code = None
        self.val = None
        self.start()

    def run(self):
        while True:
            timeout = .5
            self.event.wait(.2)
            if not self.threadRun:
                break
            while self.event.isSet():
                if self.action != None:
                    self.action(self.code, self.val)
                sleep(timeout)
                timeout = .05

class JogShuttle():
    def __init__(self):
        allHids = None
        if WINDOWS:
            allHids = find_all_hid_devices()
        if allHids:
            for index, device in enumerate(allHids):
                if (device.vendor_id == 0xb33) and (device.product_id == 0x20):
                    try:
                        device.open()
                        device.set_raw_data_handler(self.ShuttleInput)
                    except:
                        pass
                    break

        self.lastOuterRing = 0
        self.lastKnob = None
        self.lastButton = 0
        self.buttonAction = ((16, self.setZ), (32, self.setX), \
                             (64, self.setSpindle), \
                             (128, None), (1, None))
        self.axisAction = None
        self.factor = (0.00, 0.01, 0.02, 0.05, 0.10, 0.20, 0.50, 1.00)

        self.zSpeed = [None, None, None, None, None, None, None, None]
        self.zCurIndex = -1
        self.zCurSpeed = 0.0

        self.xSpeed = [None, None, None, None, None, None, None, None]
        self.xCurIndex = -1
        self.xCurSpeed = 0.0

        self.spindleSpeed = [None, None, None, None, None, None, None, None]
        self.spindleCurIndex = -1
        self.spindleCurSpeed = 0.0

        # 0.0 0.5 1.0 5.0 10.0 20.0 150.0 240.0

    def ShuttleInput(self, data):
        global jogShuttle, buttonRepeat
        print(data)
        stdout.flush()
        outerRing = data[1]
        if outerRing != jogShuttle.lastOuterRing:
            if jogShuttle.axisAction != None:
                if outerRing > 128:
                    outerRing = -(256 - outerRing)
                # jogShuttle.axisAction(outerRing)
                buttonRepeat.action = jogShuttle.axisAction
                buttonRepeat.code = 0
                buttonRepeat.val = outerRing
                buttonRepeat.event.set()
            jogShuttle.lastOuterRing = outerRing
        knob = data[2]
        if knob != jogShuttle.lastKnob:
            if jogShuttle.lastKnob != None:
                pass
            jogShuttle.lastKnob = knob
        button = data[4] | data[5]
        if button | jogShuttle.lastButton:
            changed = button ^ jogShuttle.lastButton
            for action in jogShuttle.buttonAction:
                (val, function) = action
                if changed & val:
                    if function != None:
                        function(button, val)
            jogShuttle.lastButton = button

    def setZ(self, button, val):
        if button & val:
            jogShuttle.axisAction = jogShuttle.jogZ
            maxSpeed = getFloatInfo(zMaxSpeed)
            for val in range(len(jogShuttle.factor)):
                jogShuttle.zSpeed[val] = maxSpeed * jogShuttle.factor[val]
            # print("set z")
            # stdout.flush()

    def setX(self, button, val):
        if button & val:
            jogShuttle.axisAction = jogShuttle.jogX
            maxSpeed = getFloatInfo(xMaxSpeed)
            for val in range(len(jogShuttle.factor)):
                jogShuttle.xSpeed[val] = maxSpeed * jogShuttle.factor[val]
            # print("set x")
            # stdout.flush()

    def setSpindle(self, button, val):
        if button & val:
            jogShuttle.axisAction = jogShuttle.jogSpindle
            maxSpeed = getFloatInfo(spMaxRPM)
            for val in range(len(jogShuttle.factor)):
                jogShuttle.spindleSpeed[val] = maxSpeed * jogShuttle.factor[val]
            # print("set spindle")
            # stdout.flush()

    def jogZ(self, code, val):
        global jogShuttle, buttonRepeat
        # print("jog z %d %d" % (val, jogShuttle.zCurIndex))
        # stdout.flush()
        index = abs(val)
        speed = jogShuttle.zSpeed[index]
        if val < 0:
            speed = -speed
        if ((jogShuttle.zCurSpeed >= 0 and speed >= 0) or 
            (jogShuttle.zCurSpeed <= 0 and speed <= 0)):
            jogShuttle.zCurSpeed = speed
            try:
                if index != jogShuttle.zCurIndex:
                    jogShuttle.zCurIndex = index
                    setParm(Z_JOG_SPEED, speed)
                command(ZJSPEED)
            except CommTimeout:
                commTimeout()
            if index == 0:
                buttonRepeat.action = None
                buttonRepeat.event.clear()
                jogShuttle.zCurIndex = -1
                # print("jogZ done")
                # stdout.flush()

    def jogX(self, code, val):
        global jogShuttle, buttonRepeat
        # print("jog x %d" % (val))
        # stdout.flush()
        index = abs(val)
        speed = jogShuttle.xSpeed[index]
        if val > 0:
            speed = -speed
        if ((jogShuttle.xCurSpeed >= 0 and speed >= 0) or 
            (jogShuttle.xCurSpeed <= 0 and speed <= 0)):
            jogShuttle.xCurSpeed = speed
            try:
                if index != jogShuttle.xCurIndex:
                    jogShuttle.xCurIndex = index
                    setParm(X_JOG_SPEED, speed)
                command(XJSPEED)
            except CommTimeout:
                commTimeout()
            if index == 0:
                buttonRepeat.action = None
                buttonRepeat.event.clear()
                jogShuttle.xCurIndex = -1
                # print("jogX done")
                # stdout.flush()

    def jogSpindle(self, code, val):
        global jogShuttle, buttonRepeat
        # print("jog spindle %d %d" % (val, jogShuttle.spindleCurIndex))
        # stdout.flush()
        index = abs(val)
        speed = jogShuttle.spindleSpeed[index]
        if val < 0:
            speed = -speed
        if ((jogShuttle.spindleCurSpeed >= 0 and speed >= 0) or 
            (jogShuttle.spindleCurSpeed <= 0 and speed <= 0)):
            jogShuttle.spindleCurSpeed = speed
            try:
                if index != jogShuttle.spindleCurIndex:
                    jogShuttle.spindleCurIndex = index
                    setParm(SP_JOG_RPM, speed)
                command(SPINDLE_JOG_SPEED)
            except CommTimeout:
                commTimeout()
            if index == 0:
                buttonRepeat.action = None
                buttonRepeat.event.clear()
                jogShuttle.spindleCurIndex = -1
                # print("jogspindle done")
                # stdout.flush()

class JogPanel(wx.Panel, FormRoutines):
    def __init__(self, parent, *args, **kwargs):
        global buttonRepeat
        super(JogPanel, self).__init__(parent, *args, **kwargs)
        self.jogCode = None
        self.repeat = 0
        # self.lastTime = 0
        self.btnRpt = buttonRepeat = ButtonRepeat()
        self.initUI()
        self.setZPosDialog = None
        self.setXPosDialog = None
        self.fixXPosDialog = None
        self.xHome = False
        self.probeAxis = 0
        self.probeLoc = 0.0
        self.zStepsInch = 0
        self.xStepsInch = 0
        self.zDROInch = 0
        self.xDROInch = 0
        self.zDROInvert = 1
        self.xDROInvert = 1
        self.zMenu = None
        self.xMenu = None
        self.mvStatus = 0

    def initUI(self):
        global emptyCell
        self.Bind(wx.EVT_LEFT_UP, self.OnMouseEvent)

        sizerV = wx.BoxSizer(wx.VERTICAL)

        sizerG = wx.FlexGridSizer(6, 0, 0)

        posFont = wx.Font(20, wx.MODERN, wx.NORMAL, \
                          wx.NORMAL, False, u'Consolas')
        txtFont = wx.Font(16, wx.MODERN, wx.NORMAL, \
                          wx.NORMAL, False, u'Consolas')

        # first row
        # z position

        txt = wx.StaticText(self, -1, "Z")
        txt.SetFont(txtFont)
        sizerG.Add(txt, flag=wx.LEFT|wx.RIGHT|wx.ALIGN_RIGHT| \
                   wx.ALIGN_CENTER_VERTICAL, border=10)

        self.zPos = tc = wx.TextCtrl(self, -1, "0.0000", size=(120, -1), \
                                     style=wx.TE_RIGHT)
        initInfo(jogZPos, tc)
        tc.SetFont(posFont)
        tc.SetEditable(False)
        tc.Bind(wx.EVT_RIGHT_DOWN, self.OnZMenu)
        sizerG.Add(tc, flag=wx.CENTER|wx.ALL, border=2)

        # x Position

        txt = wx.StaticText(self, -1, "X")
        txt.SetFont(txtFont)
        sizerG.Add(txt, flag=wx.LEFT|wx.RIGHT|wx.ALIGN_RIGHT| \
                   wx.ALIGN_CENTER_VERTICAL, border=10)

        self.xPos = tc = wx.TextCtrl(self, -1, "0.0000", size=(120, -1), \
                                     style=wx.TE_RIGHT)
        initInfo(jogXPos, tc)
        tc.SetFont(posFont)
        tc.SetEditable(False)
        tc.Bind(wx.EVT_RIGHT_DOWN, self.OnXMenu)
        sizerG.Add(tc, flag=wx.CENTER|wx.ALL, border=2)

        # rpm

        txt = wx.StaticText(self, -1, "RPM")
        txt.SetFont(txtFont)
        sizerG.Add(txt, flag=wx.LEFT|wx.RIGHT|wx.ALIGN_RIGHT| \
                   wx.ALIGN_CENTER_VERTICAL, border=10)

        self.rpm = tc = wx.TextCtrl(self, -1, "0", size=(80, -1), \
                                    style=wx.TE_RIGHT)
        tc.SetFont(posFont)
        tc.SetEditable(False)
        sizerG.Add(tc, flag=wx.CENTER|wx.ALL, border=2)

        # second row
        # blank space

        sizerG.Add(emptyCell)
        self.statusText = txt = wx.StaticText(self, -1, "")
        txt.SetFont(txtFont)
        sizerG.Add(txt, flag=wx.ALL|wx.ALIGN_LEFT| \
                   wx.ALIGN_CENTER_VERTICAL, border=10)

        # x diameter

        txt = wx.StaticText(self, -1, "X D")
        txt.SetFont(txtFont)
        sizerG.Add(txt, flag=wx.LEFT|wx.RIGHT|wx.ALIGN_RIGHT| \
                   wx.ALIGN_CENTER_VERTICAL, border=10)

        self.xPosDiam = tc = wx.TextCtrl(self, -1, "0.0000", size=(120, -1), \
                                         style=wx.TE_RIGHT)
        initInfo(jogXPosDiam, tc)
        tc.SetFont(posFont)
        tc.SetEditable(False)
        # tc.Bind(wx.EVT_LEFT_DOWN, self.OnSetXPos)
        tc.Bind(wx.EVT_RIGHT_DOWN, self.OnXMenu)
        sizerG.Add(tc, flag=wx.CENTER|wx.ALL, border=2)

        # pass

        txt = wx.StaticText(self, -1, "Pass")
        txt.SetFont(txtFont)
        sizerG.Add(txt, flag=wx.LEFT|wx.RIGHT|wx.ALIGN_RIGHT| \
                   wx.ALIGN_CENTER_VERTICAL, border=10)

        self.curPass = tc = wx.TextCtrl(self, -1, "0", size=(40, -1), \
                                        style=wx.TE_RIGHT)
        tc.SetFont(posFont)
        tc.SetEditable(False)
        sizerG.Add(tc, flag=wx.CENTER|wx.ALL, border=2)

        if DRO:
            # third row
            # z dro position

            txt = wx.StaticText(self, -1, "Z")
            txt.SetFont(txtFont)
            sizerG.Add(txt, flag=wx.LEFT|wx.RIGHT|wx.ALIGN_RIGHT| \
                       wx.ALIGN_CENTER_VERTICAL, border=10)

            self.zDROPos = tc = wx.TextCtrl(self, -1, "0.0000", \
                                            size=(120, -1), style=wx.TE_RIGHT)
            initInfo(encZPos, tc)
            tc.SetFont(posFont)
            tc.SetEditable(False)
            sizerG.Add(tc, flag=wx.CENTER|wx.ALL, border=2)

            # x dro Position

            txt = wx.StaticText(self, -1, "X")
            txt.SetFont(txtFont)
            sizerG.Add(txt, flag=wx.LEFT|wx.RIGHT|wx.ALIGN_RIGHT| \
                       wx.ALIGN_CENTER_VERTICAL, border=10)

            self.xDROPos = tc = wx.TextCtrl(self, -1, "0.0000", \
                                            size=(120, -1), style=wx.TE_RIGHT)
            initInfo(droXPos, tc)
            tc.SetFont(posFont)
            tc.SetEditable(False)
            sizerG.Add(tc, flag=wx.CENTER|wx.ALL, border=2)

        sizerV.Add(sizerG, flag=wx.ALIGN_CENTER_VERTICAL|wx.CENTER|wx.ALL, \
                   border=2)

        # status line

        self.statusLine = txt = wx.StaticText(self, -1, "")
        txt.SetFont(txtFont)
        sizerV.Add(txt, flag=wx.ALL|wx.ALIGN_LEFT| \
                   wx.ALIGN_CENTER_VERTICAL, border=2)

        # control buttons and jog

        sizerH = wx.BoxSizer(wx.HORIZONTAL)

        sizerG = wx.GridSizer(3, 0, 0)

        self.addButton(sizerG, 'E Stop', self.OnEStop)
        # btn = wx.Button(self, label='E Stop')
        # btn.Bind(wx.EVT_BUTTON, self.OnEStop)
        # sizerG.Add(btn, flag=wx.CENTER|wx.ALL, border=2)

        self.addButton(sizerG, 'Pause', self.OnPause)
        # btn = wx.Button(self, label='Pause')
        # btn.Bind(wx.EVT_BUTTON, self.OnPause)
        # sizerG.Add(btn, flag=wx.CENTER|wx.ALL, border=2)

        if STEPPER_DRIVE:
            btn = wx.Button(self, label='Jog Spindle')
            btn.Bind(wx.EVT_LEFT_DOWN, self.OnJogSpindle)
            btn.Bind(wx.EVT_LEFT_UP, self.OnJogUp)
            sizerG.Add(btn, flag=wx.CENTER|wx.ALL, border=2)
        else:
            sizerG.Add(emptyCell)

        self.addButton(sizerG, 'Done', self.OnDone)
        # btn = wx.Button(self, label='Done')
        # btn.Bind(wx.EVT_BUTTON, self.OnDone)
        # sizerG.Add(btn, flag=wx.CENTER|wx.ALL, border=2)

        sizerG.Add(emptyCell)
        sizerG.Add(emptyCell)

        self.addButton(sizerG, 'Stop', self.OnStop)
        # btn = wx.Button(self, label='Stop')
        # btn.Bind(wx.EVT_BUTTON, self.OnStop)
        # sizerG.Add(btn, flag=wx.CENTER|wx.ALL, border=2)

        self.addButton(sizerG, 'Resume', self.OnResume)
        # btn = wx.Button(self, label='Resume')
        # btn.Bind(wx.EVT_BUTTON, self.OnResume)
        # sizerG.Add(btn, flag=wx.CENTER|wx.ALL, border=2)

        if STEPPER_DRIVE:
            self.addButton(sizerG, 'Start Spindle', self.OnStartSpindle)
            # btn = wx.Button(self, label='Start Spindle')
            # btn.Bind(wx.EVT_BUTTON, self.OnStartSpindle)
            # sizerG.Add(btn, flag=wx.CENTER|wx.ALL, border=2)
        else:
            sizerG.Add(emptyCell)

        sizerH.Add(sizerG)

        sizerG = wx.FlexGridSizer(5, 0, 0)
        sFlag = wx.ALL|wx.CENTER|wx.ALIGN_CENTER_VERTICAL

        # first row

        sizerG.Add(emptyCell)
        sizerG.Add(emptyCell)
        sizerG.Add(emptyCell)

        bmp = wx.Bitmap("north.gif", wx.BITMAP_TYPE_ANY)
        btn = wx.BitmapButton(self, id=wx.ID_ANY, bitmap=bmp, \
                              size=(bmp.GetWidth()+10, bmp.GetHeight()+10))
        self.xNegButton = btn
        btn.Bind(wx.EVT_LEFT_DOWN, self.OnXNegDown)
        btn.Bind(wx.EVT_LEFT_UP, self.OnXUp)
        sizerG.Add(btn, flag=sFlag|wx.EXPAND, border=2)

        sizerG.Add(emptyCell)

        # second row

        bmp = wx.Bitmap("west.gif", wx.BITMAP_TYPE_ANY)
        btn = wx.BitmapButton(self, id=wx.ID_ANY, bitmap=bmp, \
                              size=(bmp.GetWidth()+10, bmp.GetHeight()+10))
        self.zNegButton = btn
        btn.Bind(wx.EVT_LEFT_DOWN, self.OnZNegDown)
        btn.Bind(wx.EVT_LEFT_UP, self.OnZUp)
        sizerG.Add(btn, flag=sFlag, border=2)

        btn = wx.Button(self, label='H', style=wx.BU_EXACTFIT)
        btn.Bind(wx.EVT_BUTTON, self.OnZHome)
        sizerG.Add(btn, flag=sFlag, border=2)

        bmp = wx.Bitmap("east.gif", wx.BITMAP_TYPE_ANY)
        btn = wx.BitmapButton(self, id=wx.ID_ANY, bitmap=bmp, \
                              size=(bmp.GetWidth()+10, bmp.GetHeight()+10))
        self.zPosButton = btn
        btn.Bind(wx.EVT_LEFT_DOWN, self.OnZPosDown)
        btn.Bind(wx.EVT_LEFT_UP, self.OnZUp)
        sizerG.Add(btn, flag=sFlag, border=2)

        btn = wx.Button(self, label='H', style=wx.BU_EXACTFIT)
        btn.Bind(wx.EVT_BUTTON, self.OnXHome)
        sizerG.Add(btn, flag=sFlag, border=2)

        self.step = step = ["Cont", "0.001", "0.002", "0.005", \
                            "0.010", "0.020", "0.050", \
                            "0.100", "0.200", "0.500", "1.000"]

        self.combo = combo = wx.ComboBox(self, -1, step[1], choices=step, \
                                         style=wx.CB_READONLY)
        initInfo(jogInc, combo)
        combo.Bind(wx.EVT_COMBOBOX, self.OnCombo)
        combo.Bind(wx.EVT_KEY_DOWN, self.OnKeyDown)
        combo.Bind(wx.EVT_KEY_UP, self.OnKeyUp)
        combo.Bind(wx.EVT_CHAR, self.OnKeyChar)
        combo.Bind(wx.EVT_SET_FOCUS, self.OnSetFocus)
        combo.Bind(wx.EVT_KILL_FOCUS, self.OnKillFocus)
        combo.SetFocus()
        sizerG.Add(combo, flag=sFlag, border=2)

        # third row

        sizerG.Add(emptyCell)
        sizerG.Add(emptyCell)
        sizerG.Add(emptyCell)

        bmp = wx.Bitmap("south.gif", wx.BITMAP_TYPE_ANY)
        btn = wx.BitmapButton(self, id=wx.ID_ANY, bitmap=bmp, \
                              size=(bmp.GetWidth()+10, bmp.GetHeight()+10))
        self.xPosButton = btn
        btn.Bind(wx.EVT_LEFT_DOWN, self.OnXPosDown)
        btn.Bind(wx.EVT_LEFT_UP, self.OnXUp)
        sizerG.Add(btn, flag=sFlag|wx.EXPAND, border=2)

        sizerG.Add(emptyCell)

        sizerH.Add(sizerG)

        sizerV.Add(sizerH, flag=wx.ALIGN_CENTER_VERTICAL|wx.CENTER|wx.ALL, \
                   border=2)

        # sizerV.Add(sizerH, flag=wx.CENTER|wx.ALL, border=2)

        self.SetSizer(sizerV)
        sizerV.Fit(self)

    def menuPos(self, e, ctl):
        (xPos, yPos) = ctl.GetPosition()
        (x, y) = e.GetPosition()
        xPos += x
        yPos += y
        return(xPos, yPos)
    
    def OnZMenu(self, e):
        menu = PosMenu(AXIS_Z)
        self.PopupMenu(menu, self.menuPos(e, self.zPos))
        menu.Destroy()

    def OnXMenu(self, e):
        menu = PosMenu(AXIS_X)
        self.PopupMenu(menu, self.menuPos(e, self.xPos))
        menu.Destroy()

    def focus(self):
        self.combo.SetFocus()

    def getInc(self):
        val = self.combo.GetValue()
        # print("combo %d" % (self.combo.GetSelection()))
        # stdout.flush()
        return(val)

    def zJogCmd(self, code, val):
        self.repeat += 1
        sendZData()
        if val == 'Cont':
            if self.jogCode != code: # new jog code
                if self.jogCode == None: # jogging stopped
                    self.jogCode = code
                    self.repeat = 0
                    dir = 1
                    if code == wx.WXK_LEFT:
                        dir = -1
                    print("zJogCmd %d" % (dir))
                    stdout.flush()
                    try:
                        queParm(Z_JOG_MAX, getInfo(zJogMax))
                        queParm(Z_JOG_DIR, dir)
                        command(ZJMOV)
                    except CommTimeout:
                        commTimeout()
            else:
                try:
                    command(ZJMOV)
                except CommTimeout:
                    commTimeout()
        else:
            if self.jogCode == None:
                self.jogCode = code
                if code == wx.WXK_LEFT:
                    val = '-' + val
                print("zJogCmd %s" % (val))
                stdout.flush()
                try:
                    queParm(Z_FLAG, CMD_JOG)
                    queParm(Z_MOVE_DIST, val)
                    command(ZMOVEREL)
                except CommTimeout:
                    commTimeout()

    def jogDone(self, cmd):
        self.jogCode = None
        val = self.getInc()
        if val == "Cont":
            print("jogDone %d" % (self.repeat))
            stdout.flush()
            try:
                command(cmd)
            except CommTimeout:
                commTimeout()

    def zDown(self, code):
        val = self.getInc()
        if val != "Cont":
            self.zJogCmd(code, val)
        else:
            self.btnRpt.action = self.zJogCmd
            self.btnRpt.code = code
            self.btnRpt.val = val
            self.btnRpt.event.set()

    def OnZUp(self, e):
        val = self.getInc()
        if val == "Cont":
            self.btnRpt.event.clear()
            self.btnRpt.action = None
            self.jogDone("ZSTOP")
        self.jogCode = None
        self.combo.SetFocus()

    def OnZNegDown(self, e):
        self.zNegButton.SetFocus()
        self.zDown(wx.WXK_LEFT)

    def OnZHome(self, e):
        command(ZGOHOME)
        self.combo.SetFocus()

    def OnZPosDown(self, e):
        self.zPosButton.SetFocus()
        self.zDown(wx.WXK_RIGHT)

    def xJogCmd(self, code, val):
        self.repeat += 1
        sendXData()
        if val == 'Cont':
            if self.jogCode != code:
                if self.jogCode == None:
                    self.jogCode = code
                    self.repeat = 0
                    dir = 1
                    if code == wx.WXK_UP:
                        dir = -1
                    print("xJogCmd %d" % (dir))
                    stdout.flush()
                    try:
                        queParm(X_JOG_MAX, getInfo(xJogMax))
                        queParm(X_JOG_DIR, dir)
                        command(XJMOV)
                    except CommTimeout:
                        commTimeout()
            else:
                try:
                    command("XJMOV")
                except CommTimeout:
                    commTimeout()
        else:
            if self.jogCode == None:
                self.jogCode = code
                if code == wx.WXK_UP:
                    val = '-' + val
                print("xJogCmd %s" % (val))
                stdout.flush()
                try:
                    queParm(X_FLAG, CMD_JOG)
                    queParm(X_MOVE_DIST, val)
                    command(XMOVEREL)
                except CommTimeout:
                    commTimeout()

    def xDown(self, code):
        val = self.getInc()
        if val != "Cont":
            self.xJogCmd(code, val)
        else:
            self.btnRpt.action = self.xJogCmd
            self.btnRpt.code = code
            self.btnRpt.val = val
            self.btnRpt.event.set()

    def OnXUp(self, e):
        val = self.getInc()
        if val == "Cont":
            self.btnRpt.event.clear()
            self.btnRpt.action = None
            self.jogDone("XSTOP")
        self.jogCode = None
        self.combo.SetFocus()

    def OnXPosDown(self, e):
        self.xPosButton.SetFocus()
        self.xDown(wx.WXK_DOWN)

    def OnXHome(self, e):
        command(XGOHOME)
        self.combo.SetFocus()

    def OnXNegDown(self, e):
        self.xNegButton.SetFocus()
        self.xDown(wx.WXK_UP)

    def OnCombo(self, e):
        val = self.combo.GetValue();
        print("combo val %s" % (val))
        try:
            val = float(val)
            if val > 0.020:
                val = 0.020
        except ValueError:
            val = 0.001
        queParm(Z_MPG_INC, val * self.zStepsInch)
        queParm(X_MPG_INC, val * self.xStepsInch)
        sendMulti()

    def OnMouseEvent(self, evt):
        self.combo.SetFocus()
        evt.Skip()

    def OnSetFocus(self, evt):
        # print("focus set")
        # stdout.flush()
        evt.Skip()

    def OnKillFocus(self, evt):
        # print("focus kill")
        # stdout.flush()
        evt.Skip()

    def OnKeyDown(self, evt):
        code = evt.GetKeyCode()
        val = self.getInc()
        if code == wx.WXK_LEFT:
            self.zJogCmd(code, val)
            return
        elif code == wx.WXK_RIGHT:
            self.zJogCmd(code, val)
            return
        elif code == wx.WXK_UP:
            self.xJogCmd(code, val)
            return
        elif code == wx.WXK_DOWN:
            self.xJogCmd(code, val)
            return
        elif code == wx.WXK_NUMPAD_PAGEDOWN:
            self.spindleJogCmd(code, 0)
            return
        # print("key down %x" % (code))
        # stdout.flush()
        evt.Skip()
    
    def OnKeyUp(self, evt):
        code = evt.GetKeyCode()
        if code == wx.WXK_LEFT:
            self.jogDone("ZSTOP")
            return
        elif code == wx.WXK_RIGHT:
            self.jogDone("ZSTOP")
            return
        elif code == wx.WXK_UP:
            self.jogDone("XSTOP")
            return
        elif code == wx.WXK_DOWN:
            self.jogDone("XSTOP")
            return
        elif code == wx.WXK_NUMPAD_PAGEDOWN:
            command("SPINDLE_STOP")
            return
        # print("key up %x" % (code))
        # stdout.flush()
        evt.Skip()

    def OnKeyChar(self, evt):
        global mainFrame
        code = evt.GetKeyCode()
        if code == ord('c'):
            self.combo.SetSelection(0)
            return
        elif code == ord('i'):
            combo = self.combo
            val = combo.GetSelection()
            if val == 0:
                combo.SetSelection(1)
            else:
                combo.SetSelection(1) if val >= len(self.step) - 1 else \
                    combo.SetSelection(val + 1)
            return
        elif code == ord('I'):
            combo = self.combo
            val = combo.GetSelection()
            if val > 0:
                if val > 1:
                    combo.SetSelection(val - 1)
            return
        elif code == ord('r'):
            panel = getInfo(mainPanel)
            panel = mainFrame.panels[panel]
            panel.OnSend(None)
            return
        elif code == ord('s'):
            self.OnResume(None)
            return
        elif code == ord('p'):
            self.OnPause(None)
            return
        elif code == wx.WXK_F9:
            self.OnStartSpindle(None)
            return
        elif code == wx.WXK_ESCAPE:
            self.OnStop(None)
            return

        print("key char %x" % (code))
        stdout.flush()
        evt.Skip()

    def updateZ(self, val):
        txt = "%7.3f" % (float(val) / self.zStepsInch) \
              if self.zStepsInch != 0.0 else '0.000'
        self.zPos.SetValue(txt)

    def updateX(self, val):
        txt = "%7.3f" % (float(val) / self.xStepsInch) \
              if self.xStepsInch != 0.0 else '0.000'
        self.xPos.SetValue(txt)

    def updateRPM(self, val):
        print(val)
        stdout.flush()

    def probe(self, axis, probeLoc=None):
        self.xHome = True
        self.probeAxis = axis
        if probeLoc != None:
            self.probeLoc = probeLoc

    def homeDone(self, status):
        self.xHome = False
        self.probeStatus = 0
        print(status)
        stdout.flush()
        
    def updateAll(self, val):
        global zHomeOffset, xHomeOffset, zDROOffset, xDROOffset, xHomed
        if len(val) == 7:
            (z, x, rpm, curPass, zDROPos, xDROPos, mvStatus) = val
            if z != '#':
                zLoc = float(z) / self.zStepsInch
                self.zPos.SetValue("%0.4f" % (zLoc - zHomeOffset))
            if x != '#':
                xLoc = float(x) / self.xStepsInch - xHomeOffset
                self.xPos.SetValue("%0.4f" % (xLoc))
                self.xPosDiam.SetValue("%0.4f" % (abs(xLoc * 2)))
            self.rpm.SetValue(rpm)
            self.curPass.SetValue(curPass)

            if DRO:
                zDroLoc = float(self.zDroInvert * zDROPos) / self.zDROInch - \
                          zDROOffset
                self.zDROPos.SetValue("%0.4f" % (zDroLoc))

                xDroLoc = float(self.xDroInvert * xDROPos) / self.xDROInch - \
                          xDROOffset
                self.xDROPos.SetValue("%0.4f" % (xDroLoc))

            text = ''
            if xHomed:
                text = 'H'
            mvStatus = int(mvStatus)
            self.mvStatus = mvStatus
            if mvStatus & MV_PAUSE:
                text  = text + 'P'
            if mvStatus & MV_ACTIVE:
                text = text + 'A';
            self.statusText.SetLabel(text)

            if self.xHome:
                if self.probeAxis == HOME_X:
                    val = getParm(X_HOME_STATUS)
                    if val != None:
                        if val & HOME_SUCCESS:
                            self.homeDone("home success")
                            xHomed = True
                        elif val & HOME_FAIL:
                            self.homeDone("home success")
                elif self.probeAxis == AXIS_Z:
                    val = getParm(Z_HOME_STATUS)
                    if val & PROBE_SUCCESS:
                        zHomeOffset = zLoc - self.probeLoc
                        setInfo(zSvHomeOffset, "%0.4f" % (zHomeOffset))
                        print("z %s zLoc %7.4f probeLoc %7.4f "\
                              "zHomeOffset %7.4f" % \
                              (z, zLoc, self.probeLoc, zHomeOffset))
                        if DRO:
                            zDROOffset = zDroLoc - self.probeLoc
                            setInfo(zSvDROOffset, "%0.4f" % (zDROOffset))
                            setParm(Z_DRO_OFFSET, zDROOffset)
                        self.probeLoc = 0.0
                        self.homeDone("z probe success")
                    elif val & PROBE_FAIL:
                        self.homeDone("z probe failure")
                elif self.probeAxis == AXIS_X:
                    val = getParm(X_HOME_STATUS)
                    if val & PROBE_SUCCESS:
                        xHomeOffset = xLoc - self.probeLoc
                        setInfo(xSvHomeOffset, "%0.4f" % (xHomeOffset))
                        if DRO:
                            xDROOffset = xDroPos - self.probeLoc
                            setInfo(xSvDROOffset, "%0.4f" % (xDROOffset))
                            setParm(X_DRO_OFFSET, xDROOffset)
                        print("x %s xLoc %7.4f probeLoc %7.4f "\
                              "xHomeOffset %7.4f" % \
                              (x, xLoc, self.probeLoc, xHomeOffset))
                        self.probeLoc = 0.0
                        self.homeDone("x probe success")
                        stdout.flush()
                    elif val & PROBE_FAIL:
                        self.homeDone("x probe failure")

    def updateError(self, text):
        self.setStatus(text)

    def OnEStop(self, e):
        global moveCommands, spindleDataSend, zDataSent, xDataSent
        moveCommands.queClear()
        command(CMD_CLEAR)
        spindleDataSent = False
        zDataSent = False
        xDataSent = False
        self.clrActive()
        self.combo.SetFocus()

    def OnStop(self, e):
        global moveCommands
        moveCommands.queClear()
        command(CMD_STOP)
        self.clrActive()
        self.combo.SetFocus()

    def OnPause(self, e):
        command(CMD_PAUSE)
        self.combo.SetFocus()

    def OnResume(self, e):
        command(CMD_RESUME)
        self.combo.SetFocus()

    def OnDone(self, e):
        self.clrActive()
        self.setStatus(STR_CLR)
        self.combo.SetFocus()

    def getPanel(self):
        panel = getInfo(mainPanel)
        return(mainFrame.panels[panel])

    def clrActive(self):
        panel = self.getPanel()
        panel.active = False

    def OnStartSpindle(self, e):
        if STEPPER_DRIVE:
            panel = self.getPanel()
            rpm = panel.rpm.GetValue()
            sendSpindleData(True, rpm)
            command(SPINDLE_START)
        self.combo.SetFocus()

    def spindleJogCmd(self, code, val):
        self.repeat += 1
        if self.jogCode != code:
            if self.jogCode == None:
                sendSpindleData()
                self.jogCode = code
                self.repeat = 0
        try:
            command("SPINDLE_JOG")
        except CommTimeout:
            commTimeout()
        self.combo.SetFocus()

    def OnJogSpindle(self, e):
        print("jog spingle")
        stdout.flush()
        self.btnRpt.action = self.spindleJogCmd
        self.btnRpt.code = wx.WXK_NUMPAD_PAGEDOWN
        self.btnRpt.val = 0
        self.btnRpt.event.set()

    def OnJogUp(self, e):
        self.btnRpt.event.clear()
        self.btnRpt.action = None
        try:
            command("SPINDLE_STOP")
        except CommTimeout:
            commTimeout()
        self.combo.SetFocus()

    def setStatus(self, text):
        global done, jogPanel
        if done:
            return
        if isinstance(text, int):
            self.statusLine.SetLabel(strTable[text])
        elif isinstance(text, str):
            self.statusLine.SetLabel(text)
        self.Refresh()
        self.Update()

def jogPanelPos(ctl):
        global jogPanel, mainFrame
        (xPos, yPos) = mainFrame.GetPosition()
        (x, y) = jogPanel.GetPosition()
        xPos += x
        yPos += y
        (x, y) = ctl.GetPosition()
        xPos += x
        yPos += y
        return(xPos, yPos)

class PosMenu(wx.Menu):
    def __init__(self, axis):
        wx.Menu.__init__(self)
        self.axis = axis
        item = wx.MenuItem(self, wx.NewId(), "Set")
        self.Append(item)
        self.Bind(wx.EVT_MENU, self.OnSet, item)

        item = wx.MenuItem(self, wx.NewId(), "Zero")
        self.Append(item)
        self.Bind(wx.EVT_MENU, self.OnZero, item)

        item = wx.MenuItem(self, wx.NewId(), "Probe")
        self.Append(item)
        self.Bind(wx.EVT_MENU, self.OnProbe, item)

        if self.axis == AXIS_X:
            item = wx.MenuItem(self, wx.NewId(), "Home")
            self.Append(item)
            self.Bind(wx.EVT_MENU, self.OnHomeX, item)

        item = wx.MenuItem(self, wx.NewId(), "Go to")
        self.Append(item)
        self.Bind(wx.EVT_MENU, self.OnGoto, item)

        if self.axis == AXIS_X:
            item = wx.MenuItem(self, wx.NewId(), "Fix X")
            self.Append(item)
            self.Bind(wx.EVT_MENU, self.OnFixX, item)

    def getPosCtl(self):
        ctl = jogPanel.zPos if self.axis == AXIS_Z else jogPanel.xPos
        return(jogPanelPos(ctl))

    def OnSet(self, e):
        dialog = SetPosDialog(jogPanel, self.axis)
        dialog.SetPosition(self.getPosCtl())
        dialog.Raise()
        dialog.Show(True)

    def OnZero(self, e):
        global jogPanel
        updateZPos(0) if self.axis == AXIS_Z else updateXPos(0)
        jogPanel.focus()

    def OnProbe(self, e):
        dialog = ProbeDialog(jogPanel, self.axis)
        dialog.SetPosition(self.getPosCtl())
        dialog.Raise()
        dialog.Show(True)

    def OnHomeX(self, e):
        queParm(X_HOME_DIST, getInfo(xHomeDist))
        queParm(X_HOME_BACKOFF_DIST, getInfo(xHomeBackoffDist))
        queParm(X_HOME_SPEED, getInfo(xHomeSpeed))
        queParm(X_HOME_DIR, 1 if getBoolInfo(xHomeDir) else -1)
        command(XHOMEAXIS)
        jogPanel.probe(HOME_X)
        jogPanel.focus()

    def OnGoto(self, e):
        dialog = GotoDialog(jogPanel, self.axis)
        dialog.SetPosition(self.getPosCtl())
        dialog.Raise()
        dialog.Show(True)

    def OnFixX(self, e):
        dialog = jogPanel.fixXPosDialog
        if dialog == None:
            self.FixXPosDialog = dialog = FixXPosDialog(jogPanel)
        dialog.SetPosition(self.getPosCtl())
        dialog.Raise()
        dialog.Show(True)

class SetPosDialog(wx.Dialog):
    def __init__(self, frame, axis):
        self.axis = axis
        pos = (10, 10)
        title = "Position %s" % ('Z' if axis == AXIS_Z else 'X')
        wx.Dialog.__init__(self, frame, -1, title, pos, \
                            wx.DefaultSize, wx.DEFAULT_DIALOG_STYLE)
        self.Bind(wx.EVT_SHOW, self.OnShow)
        self.sizerV = sizerV = wx.BoxSizer(wx.VERTICAL)

        posFont = wx.Font(20, wx.MODERN, wx.NORMAL, \
                          wx.NORMAL, False, u'Consolas')
        self.pos = tc = wx.TextCtrl(self, -1, "0.000", size=(120, -1), \
                                    style=wx.TE_RIGHT|wx.TE_PROCESS_ENTER)
        tc.SetFont(posFont)
        tc.Bind(wx.EVT_CHAR, self.OnKeyChar)
        sizerV.Add(tc, flag=wx.CENTER|wx.ALL, border=10)

        btn = wx.Button(sel, label='Ok', size=(60,-1))
        btn.Bind(wx.EVT_BUTTON, self.OnOk)
        sizerV.Add(btn, 0, wx.BOTTOM|wx.CENTER, 10)

        self.SetSizer(sizerV)
        self.sizerV.Fit(self)
        self.Show(False)
       
    def OnShow(self, e):
        global done, jogPanel
        if done:
            return
        if self.IsShown():
            val = jogPanel.zPos.GetValue() if self.axis == AXIS_Z else \
               jogPanel.xPos.GetValue()
            self.pos.SetValue(val)
            self.pos.SetSelection(-1, -1)

    def OnKeyChar(self, e):
        keyCode = e.GetKeyCode()
        if keyCode == wx.WXK_RETURN:
            self.OnOk(None)
        e.Skip()
    
    def OnOk(self, e):
        global jogPanel
        val = self.pos.GetValue()
        try:
            val = float(val)
            self.updateZPos(val) if self.axis == AXIS_Z else \
               self.updateXPOS(val)
        except ValueError:
            print("ValueError on %s" % (val))
            stdout.flush()
        self.Show(False)
        jogPanel.focus()

    def updateZPos(val):
        global jogPanel, zHomeOffset, zDROOffset
        sendZData()
        zLoc = getParm(Z_LOC)
        if zLoc != None:
            zLoc /= jogPanel.zStepsInch
            zHomeOffset = zLoc - val
            setInfo(zSvHomeOffset, "%0.4f" % (zHomeOffset))
            setParm(Z_HOME_OFFSET, zHomeOffset)
            print("zHomeOffset %0.4f" % (zHomeOffset))
        if DRO:
            zDROPos = getParm(Z_DRO_POS)
            print("zDROPos %0.4f" % (zDROPos / jogPanel.zDROInch))
            if zDROPos != None:
                droPos = float(zDROPos) / jogPanel.zDROInch
                setInfo(zSvDROPosition, "%0.4f" % (droPos))
                if jogPanel.zDROInvert:
                    droPos = -droPos
                zDROOffset = droPos - val
                setInfo(zSvDROOffset, "%0.4f" % (zDROOffset))
                setParm(Z_DRO_OFFSET, zDROOffset)
                print("zDROOffset %0.4f" % (zDROOffset))
        stdout.flush()

    def updateXPos(val):
        global jogPanel, xHomeOffset, xDROOffset
        val /= 2.0
        sendXData()
        xLoc = getParm(X_LOC)
        if xLoc != None:
            xLoc /= jogPanel.xStepsInch
            xHomeOffset = xLoc - val
            setInfo(xSvHomeOffset, "%0.4f" % (xHomeOffset))
            setParm(X_HOME_OFFSET, xHomeOffset)
            print("xHomeOffset %0.4f" % (xHomeOffset))
        if DRO:
            xDROPos = getParm(X_DRO_POS)
            print("xDROPos %0.4f" % (xDROPos / jogPanel.xDROInch))
            if xDROPos != None:
                droPos = float(xDROPos) / jogPanel.xDROInch
                setInfo(xSvDROPosition, "%0.4f" % (droPos))
                if jogPanel.xDROInvert:
                    droPos = -droPos
                xDROOffset = droPos - val
                setInfo(xSvDROOffset, "%0.4f" % (xDROOffset))
                setParm(X_DRO_OFFSET, xDROOffset)
                print("xDROOffset %0.4f" % (xDROOffset))
        stdout.flush()

class ProbeDialog(wx.Dialog):
    def __init__(self, frame, axis):
        self.axis = axis
        pos = (10, 10)
        title = "Probe %s" % ('Z' if axis == AXIS_Z else 'X Diameter')
        wx.Dialog.__init__(self, frame, -1, title, pos, \
                            wx.DefaultSize, wx.DEFAULT_DIALOG_STYLE)
        self.Bind(wx.EVT_SHOW, self.OnShow)
        self.sizerV = sizerV = wx.BoxSizer(wx.VERTICAL)

        posFont = wx.Font(20, wx.MODERN, wx.NORMAL, \
                          wx.NORMAL, False, u'Consolas')

        sizerG = wx.FlexGridSizer(2, 0, 0)

        txt = wx.StaticText(self, -1, \
                            'Z Position' if axis == AXIS_Z else 'X Diameter')
        sizerG.Add(txt, flag=wx.LEFT|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, \
                   border=10)

        self.probeLoc = tc = wx.TextCtrl(self, -1, "0.000", size=(120, -1), \
                                         style=wx.TE_RIGHT)
        tc.SetFont(posFont)
        sizerG.Add(tc, flag=wx.CENTER|wx.ALL, border=10)

        txt = wx.StaticText(self, -1, "Distance")
        sizerG.Add(txt, flag=wx.LEFT|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, \
                   border=10)

        self.probeDist = tc = wx.TextCtrl(self, -1, "0.0000", size=(120, -1), \
                                          style=wx.TE_RIGHT|\
                                          wx.TE_PROCESS_ENTER)
        tc.SetFont(posFont)
        tc.Bind(wx.EVT_CHAR, self.OnKeyChar)
        sizerG.Add(tc, flag=wx.CENTER|wx.ALL, border=10)

        sizerV.Add(sizerG, 0, wx.ALIGN_RIGHT)

        # txt = wx.StaticText(self, -1, ('Z Position', 'X Diameter')[axis])
        # sizerV.Add(txt, flag=wx.CENTER|wx.ALIGN_CENTER_VERTICAL|wx.TOP, \
        #            border=10)

        # posFont = wx.Font(20, wx.MODERN, wx.NORMAL, \
        #                   wx.NORMAL, False, u'Consolas')
        # self.probeLoc = tc = wx.TextCtrl(self, -1, "0.000", size=(120, -1), \
        #                                  style=wx.TE_RIGHT|wx.TE_PROCESS_ENTER)
        # tc.SetFont(posFont)
        # tc.Bind(wx.EVT_CHAR, self.OnKeyChar)
        # sizerV.Add(tc, flag=wx.CENTER|wx.ALL, border=10)

        btn = wx.Button(self, label='Ok', size=(60,-1))
        btn.Bind(wx.EVT_BUTTON, self.OnOk)
        sizerV.Add(btn, 0, wx.BOTTOM|wx.CENTER, 10)

        self.SetSizer(sizerV)
        self.sizerV.Fit(self)
        self.Show(False)

    def OnShow(self, e):
        global done, jogPanel
        if done:
            return
        if self.IsShown():
            if self.axis == AXIS_Z:
                probeLoc = "0.0000"
                probeDist = getFloatInfo(zProbeDist)
            else:
                probeLoc = jogPanel.xPos.GetValue()
                probeDist = getFloatInfo(xProbeDist)
            self.probeLoc.SetValue(probeLoc)
            self.probeLoc.SetSelection(-1, -1)
            self.probeDist.SetValue("%7.4f" % probeDist)

    def OnKeyChar(self, e):
        keyCode = e.GetKeyCode()
        if keyCode == wx.WXK_RETURN:
            self.OnOk(None)
        e.Skip()
    
    def OnOk(self, e):
        global jogPanel
        val = self.probeLoc.GetValue()
        try:
            probeLoc = float(val)
            self.probeZ(probeLoc) if self.axis == AXIS_Z else \
               self.probeX(probeLoc / 2.0)
        except ValueError:
            print("probe ValueError on %s" % (val))
            stdout.flush()
        self.Show(False)
        jogPanel.focus()

    def probeZ(self, probeLoc):
        global jogPanel, moveCommands
        moveCommands.queClear()
        queParm(PROBE_INV, getBoolInfo(cfgPrbInv))
        queParm(Z_PROBE_SPEED, getInfo(zProbeSpeed))
        queParm(Z_HOME_STATUS, '0');
        sendMulti()
        moveCommands.probeZ(getFloatVal(self.probeDist))
        self.Show(False)
        jogPanel.probe(AXIS_Z, probeLoc)
        jogPanel.focus()

    def probeX(self, probeLoc):
        global jogPanel, moveCommands
        moveCommands.queClear()
        queParm(PROBE_INV, getBoolInfo(cfgPrbInv))
        queParm(X_HOME_SPEED, getInfo(xHomeSpeed))
        queParm(X_HOME_STATUS, '0');
        sendMulti()
        moveCommands.probeX(getFloatVal(self.probeDist))
        self.Show(False)
        jogPanel.probe(AXIS_X, probeLoc)
        jogPanel.focus()

class GotoDialog(wx.Dialog):
    def __init__(self, frame, axis):
        self.axis = axis
        pos = (10, 10)
        title = "Go to %s" % ('Z Position' if AXIS == AXIS_Z else 'X Diameter')
        wx.Dialog.__init__(self, frame, -1, title, pos, \
                            wx.DefaultSize, wx.DEFAULT_DIALOG_STYLE)
        self.Bind(wx.EVT_SHOW, self.OnShow)
        self.sizerV = sizerV = wx.BoxSizer(wx.VERTICAL)

        posFont = wx.Font(20, wx.MODERN, wx.NORMAL, \
                          wx.NORMAL, False, u'Consolas')
        self.pos = tc = wx.TextCtrl(self, -1, "0.000", size=(120, -1), \
                                    style=wx.TE_RIGHT|wx.TE_PROCESS_ENTER)
        tc.SetFont(posFont)
        tc.Bind(wx.EVT_CHAR, self.OnKeyChar)
        sizerV.Add(tc, flag=wx.CENTER|wx.ALL, border=10)

        btn = wx.Button(self, label='Ok', size=(60,-1))
        btn.Bind(wx.EVT_BUTTON, self.OnOk)
        sizerV.Add(btn, 0, wx.BOTTOM|wx.CENTER, 10)

        self.SetSizer(sizerV)
        self.sizerV.Fit(self)
        self.Show(False)

    def OnShow(self, e):
        global done, jogPanel
        if done:
            return
        if self.IsShown():
            val = jogPanel.zPos.GetValue() if self.axis == AXIS_Z else \
               jogPanel.xPos.GetValue()
            try:
                val = float(val)
            except ValueError:
                val = 0.0
            self.pos.SetValue("%0.4f" % (val))
            self.pos.SetSelection(-1, -1)

    def OnKeyChar(self, e):
        keyCode = e.GetKeyCode()
        if keyCode == wx.WXK_RETURN:
            self.OnOk(None)
        e.Skip()
    
    def OnOk(self, e):
        global moveCommands, jogPanel
        try:
            loc = float(self.pos.GetValue())
            m = moveCommands
            m.queClear()
            command(CMD_PAUSE)
            command(CLEARQUE)
            if self.axis == AXIS_Z:
                sendZData()
                m.saveZOffset()
                m.moveZ(loc)
            else:
                sendXData()
                m.saveXOffset()
                m.moveX(loc / 2.0)
            command(CMD_RESUME)
            self.Show(False)
            jogPanel.focus()
        except ValueError:
            print("ValueError on goto")
            stdout.flush()

class FixXPosDialog(wx.Dialog):
    def __init__(self, frame):
        pos = (10, 10)
        wx.Dialog.__init__(self, frame, -1, "Fix X Size", pos, \
                            wx.DefaultSize, wx.DEFAULT_DIALOG_STYLE)
        self.Bind(wx.EVT_SHOW, self.OnShow)
        self.sizerV = sizerV = wx.BoxSizer(wx.VERTICAL)

        posFont = wx.Font(20, wx.MODERN, wx.NORMAL, \
                          wx.NORMAL, False, u'Consolas')

        sizerG = wx.FlexGridSizer(2, 0, 0)

        txt = wx.StaticText(self, -1, "Current")
        sizerG.Add(txt, flag=wx.LEFT|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, \
                   border=10)

        self.curXPos = tc = wx.TextCtrl(self, -1, "0.000", size=(120, -1), \
                                        style=wx.TE_RIGHT)
        tc.SetFont(posFont)
        sizerG.Add(tc, flag=wx.CENTER|wx.ALL, border=10)

        txt = wx.StaticText(self, -1, "Measured")
        sizerG.Add(txt, flag=wx.LEFT|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, \
                   border=10)

        self.actualXPos = tc = wx.TextCtrl(self, -1, "0.0000", size=(120, -1), \
                                           style=wx.TE_RIGHT|\
                                           wx.TE_PROCESS_ENTER)
        tc.SetFont(posFont)
        tc.Bind(wx.EVT_CHAR, self.OnKeyChar)
        sizerG.Add(tc, flag=wx.CENTER|wx.ALL, border=10)

        sizerV.Add(sizerG, 0, wx.ALIGN_RIGHT)

        btn = wx.Button(self, label='Fix', size=(60,-1))
        btn.Bind(wx.EVT_BUTTON, self.OnFix)
        sizerV.Add(btn, 0, wx.ALL|wx.CENTER, 5)

        self.SetSizer(sizerV)
        self.sizerV.Fit(self)
        self.Show(False)

    def OnShow(self, e):
        global done
        if done:
            return
        if self.IsShown():
            try:
                xDiameter = float(getParm(X_DIAMETER)) / jogPanel.xStepsInch
            except (ValueError, TypeError):
                xDiameter = 0.0
            self.curXPos.SetValue("%0.4f" % (xDiameter));
            self.actualXPos.SetFocus()
            self.actualXPos.SetSelection(-1, -1)

    def OnKeyChar(self, e):
        keyCode = e.GetKeyCode()
        if keyCode == wx.WXK_RETURN:
            self.OnFix(None)
        e.Skip()
    
    def OnFix(self, e):
        global xHomeOffset
        try:
            curX = float(self.curXPos.GetValue())
        except ValueError:
            self.curXPos.SetValue('0.000')
            return
        try:
            actualX = float(self.actualXPos.GetValue())
        except ValueError:
            self.actualXPos.SetValue('0.000')
            return
        offset = (actualX - curX) / 2.0
        xHomeOffset -= offset

        setInfo(xSvHomeOffset, "%0.4f" % (xHomeOffset))
        print("curX %0.4f actualX %0.4f offset %0.4f xHomeOffset %0.4f" % \
              (curX, actualX, offset, xHomeOffset))
        stdout.flush()

        self.Show(False)
        jogPanel.focus()
        pass

EVT_UPDATE_ID = wx.NewId()

def evtUpdate(win, func):
    win.Connect(-1, -1, EVT_UPDATE_ID, func)

class UpdateEvent(wx.PyEvent):
    def __init__(self, data):
        wx.PyEvent.__init__(self)
        self.SetEventType(EVT_UPDATE_ID)
        self.data = data

class UpdateThread(Thread):
    def __init__(self, notifyWindow):
        Thread.__init__(self)
        self.readAllError = False
        self.notifyWindow = notifyWindow
        self.threadRun = True
        self.parmList = (self.readAll, )
        self.zDro = None
        self.xDro = None
        self.start()

    # def zLoc(self):
    #     val = getParm(Z_LOC)
    #     if val != None:
    #         result = (EV_ZLOC, val)
    #         wx.PostEvent(self.notifyWindow, UpdateEvent(result))

    # def xLoc(self):
    #     val = getParm(X_LOC)
    #     if val != None:
    #         result = (EV_XLOC, val)
    #         wx.PostEvent(self.notifyWindow, UpdateEvent(result))

    # def rpm(self):
    #     period = getParm(INDEX_PERIOD)
    #     if period != None:
    #         preScaler = getParm(INDEX_PRE_SCALER)
    #         result = (EV_RPM, period * preScaler)
    #         wx.PostEvent(self.notifyWindow, UpdateEvent(result))

    def readAll(self):
        if done:
            return
        tmp = comm.xDbgPrint
        comm.xDbgPrint = False
        try:
            result = command(READLOC)
            if result == None:
                return

        except CommTimeout:
            if done:
                return
            self.readAllError = True
            wx.PostEvent(self.notifyWindow, \
                         UpdateEvent((EV_ERROR, STR_READALL_ERROR)))
            print("readAll error")
            stdout.flush()
            return
    
        except serial.SerialException:
            print("readAll SerialException")
            stdout.flush()
            return

        comm.xDbgPrint = True
        if self.readAllError:
            self.readAllError = False
            wx.PostEvent(self.notifyWindow,
                         UpdateEvent((EV_ERROR, STR_CLR)))
        try:
            (z, x, rpm, curPass, droZ, droX, flag) = \
                result.rstrip().split(' ')[1:]
            result = (EV_READ_ALL, z, x, rpm, curPass, droZ, droX, flag)
            wx.PostEvent(self.notifyWindow, UpdateEvent(result))
        except ValueError:
            print("readAll ValueError %s" % (result))
            stdout.flush()

    def run(self):
        global dbg
        dbgSetup = (\
                    (D_PASS, self.dbgPass), \
                    (D_DONE, self.dbgDone), \
                    (D_TEST, self.dbgTest), \

                    (D_XMOV, self.dbgXMov), \
                    (D_XLOC, self.dbgXLoc), \
                    (D_XDST, self.dbgXDst), \
                    (D_XSTP, self.dbgXStp),
                    (D_XST, self.dbgXState), \
                    (D_XBSTP, self.dbgXBSteps), \
                    (D_XDRO, self.dbgXDro), \
                    (D_XEXP, self.dbgXExp), \
                    (D_XWT, self.dbgXWait), \
                    (D_XDN, self.dbgXDone), \

                    (D_ZMOV, self.dbgZMov), \
                    (D_ZLOC, self.dbgZLoc), \
                    (D_ZDST, self.dbgZDst), \
                    (D_ZSTP, self.dbgZStp),
                    (D_ZST, self.dbgZState), \
                    (D_ZBSTP, self.dbgZBSteps), \
                    (D_ZDRO, self.dbgZDro), \
                    (D_ZEXP, self.dbgZExp), \
                    (D_ZWT, self.dbgZWait), \
                    (D_ZDN, self.dbgZDone), \

                    (D_HST, self.dbgHome), \
        )
        dbgTbl = [None for i in range(len(dbgSetup))]
        for (index, action) in dbgSetup:
            dbgTbl[index] = action
        for i, (val) in enumerate(dbgTbl):
            if val == None:
                print("dbgTbl action for %s missing" % (dMessageList[i]))
                stdout.flush()
        i = 0
        op = None
        scanMax = len(self.parmList)
        baseTime = None
        while True:
            sleep(0.1)
            if not self.threadRun:
                break

            # read update variables

            if i < len(self.parmList):
                func = self.parmList[i]
                try:
                    func()
                except CommTimeout:
                    print("CommTimeout on func")
                    stdout.flush()
                except serial.SerialException:
                    print("func SerialException")
                    stdout.flush()
                    break
                except RuntimeError:
                    if done:
                        break
            i += 1
            if i >= scanMax:
                i = 0

            # process move queue

            if not moveQue.empty() or (op != None):
                if not self.threadRun:
                    break
                try:
                    num = getQueueStatus()
                    if not self.threadRun:
                        break
                    while num > 0:
                        num -= 1
                        if op == None:
                            try:
                                (opString, op, val) = moveQue.get(False)
                            except Empty:
                                break
                        sendMove(opString, op, val)
                        op = None
                except CommTimeout:
                    print("CommTimeout on queue")
                    stdout.flush()
                except serial.SerialException:
                    print("SerialException on queue")
                    stdout.flush()
                    break

            # get debug data

            try:
                result = getString(READDBG, 10)
                if not self.threadRun:
                    break
                tmp = result.split()
                rLen = len(tmp)
                # if rLen > 0:
                #     print("%2d (%s)" % (rLen, result))
                index = 2
                t = ("%8.3f " % (time() - baseTime)) if baseTime != None else \
                    "   0.000 "
                while index <= rLen:
                    (cmd, val) = tmp[index-2:index]
                    index += 2
                    try:
                        cmd = int(cmd, 16)
                        val = int(val, 16)
                        try:
                            action = dbgTbl[cmd]
                            output = action(val)                        
                            if dbg == None:
                                print(t + output)
                                stdout.flush()
                            else:
                                dbg.write(t + output + "\n")
                                dbg.flush()
                            if cmd == D_DONE:
                                if val == 0:
                                    baseTime = time()
                                if val == 1:
                                    baseTime = None
                                    if dbg != None:
                                        dbg.close()
                                    dbg = None
                        except IndexError:
                            print("index error %s" % result)
                            stdout.flush()
                        except TypeError:
                            print("type error %s" % result)
                            stdout.flush()
                    except ValueError:
                        print("value error cmd %s val %s" % (cmd, val))
                        stdout.flush()
            except CommTimeout:
                print("getString CommTimeout")
                stdout.flush()
            except serial.SerialException:
                print("getString SerialException")
                stdout.flush()
                break
        print("UpdateThread done")
        stdout.flush()

    def dbgPass(self, val):
        # tmp = val >> 8
        # if tmp == 0:
        #     return("pass %d\n")
        # elif tmp == 1:
        #     return("spring\n")
        # elif tmp == 2:
        #     return("spring %d\n" % (val & 0xff))
        result = "spring\n" if val & 0x100 else \
                 "spring %d\n" % (val & 0xff) if val & 0x200 else \
                 "pass %d\n" % (val)
        return(result)

    def dbgDone(self, val):
         if val == 0:
             return("strt")
         elif val == 1:
             return("done")

    def dbgTest(self, val):
        return("test %d" % (val))

    def dbgXMov(self, val):
        tmp = float(val) / jogPanel.xStepsInch - xHomeOffset
        return("xmov %7.4f %7.4f" % (tmp, tmp * 2.0))

    def dbgXLoc(self, val):
        tmp = float(val) / jogPanel.xStepsInch - xHomeOffset
        if self.xDro != None:
            diff = " %0.4f" % (self.xDro - tmp)
            self.xDro = None
        else:
            diff = ""
        return("xloc %7.4f %7.4f%s" % (tmp, tmp * 2.0, diff))

    def dbgXDst(self, val):
        tmp = float(val) / jogPanel.xStepsInch
        return("xdst %7.4f %6d" % (tmp, val))

    def dbgXStp(self, val):
        tmp = float(val) / jogPanel.xStepsInch
        return("xstp %7.4f %6d" % (tmp, val))

    def dbgXState(self, val):
        tmp = xStatesList[val]
        return("x_st %s" % (tmp + ("\n" if val == XIDLE else "")))

    def dbgXBSteps(self, val):
        tmp = float(val) / jogPanel.xStepsInch
        return("xbst %7.4f %6d" % (tmp, val))

    def dbgXDro(self, val):
        tmp = float(jogPanel.xDroInvert * xDROPos) / jogPanel.xDROInch - \
              xDROOffset
        self.xDro = tmp
        return("xdro %7.4f %7.4f" % (tmp, tmp * 2.0))

    def dbgXExp(self, val):
        tmp = float(val) / jogPanel.xStepsInch - xHomeOffset
        return("xexp %7.4f" % (tmp))

    def dbgXWait(self, val):
        return("xwt  %2x" % (val))

    def dbgXDone(self, val):
        return("xdn  %2x" % (val))

    def dbgZMov(self, val):
        tmp = float(val) / jogPanel.zStepsInch - zHomeOffset
        return("zmov %7.4f" % (tmp))

    def dbgZLoc(self, val):
        tmp = float(val) / jogPanel.zStepsInch - zHomeOffset
        if self.zDro != None:
            diff = " %0.4f" % (self.zDro - tmp)
            self.zDro = None
        else:
            diff = ""
        return("zloc %7.4f%s" % (tmp, diff))

    def dbgZDst(self, val):
        tmp = float(val) / jogPanel.zStepsInch
        return("zdst %7.4f %6d" % (tmp, val))

    def dbgZStp(self, val):
        tmp = float(val) / jogPanel.zStepsInch
        return("zstp %7.4f %6d" % (tmp, val))

    def dbgZState(self, val):
        tmp = zStatesList[val]
        return("z_st %s" % (tmp + ("\n" if val == XIDLE else "")))

    def dbgZBSteps(self, val):
        tmp = float(val) / jogPanel.zStepsInch
        return("zbst %7.4f %6d" % (tmp, val))

    def dbgZDro(self, val):
        tmp = float(jogPanel.zDroInvert * zDROPos) / jogPanel.zDROInch - \
              zDROOffset
        self.zDro = val
        return("zdro %7.4f" % (tmp))

    def dbgZExp(self, val):
        tmp = float(val) / jogPanel.zStepsInch - zHomeOffset
        return("zexp %7.4f" % (tmp))

    def dbgZWait(self, val):
        return("zwt  %2x" % (val))

    def dbgZDone(self, val):
        return("zdn  %2x" % (val))

    def dbgHome(self, val):
        return("hsta %s" % (hStatesList[val]))

    def abort(self):
        self.run = False

# class KeyEventFilter(wx.EventFilter):
#     def __init__(self):
#         wx.EventFilter.__init__(self)
#         wx.EvtHandler.AddFilter(self)

#     def __del__(self):
#         wx.EvtHandler.RemoveFilter(self)

#     def FilterEvent(self, event):
#         t = event.GetEventType()
#         if t == wx.EVT_KEY_DOWN:
#             print("key down")
#         event.Skip()

class MainFrame(wx.Frame):
    def __init__(self, parent, title):
        global moveCommands, hdrFont, testFont, jogShuttle
        wx.Frame.__init__(self, parent, -1, title)
        self.Bind(wx.EVT_CLOSE, self.onClose)
        evtUpdate(self, self.OnUpdate)
        hdrFont = wx.Font(20, wx.MODERN, wx.NORMAL, 
                          wx.NORMAL, False, u'Consolas')
        testFont = wx.Font(10, wx.MODERN, wx.NORMAL, 
                          wx.NORMAL, False, u'Consolas')

        moveCommands = MoveCommands()

        self.zDialog = ZDialog(self)
        self.xDialog = XDialog(self)
        self.spindleDialog = SpindleDialog(self)
        self.portDialog = PortDialog(self)
        self.configDialog = ConfigDialog(self)

        self.testSpindleDialog = None
        self.testSyncDialog = None
        self.testTaperDialog = None
        self.testMoveDialog = None

        self.dirName = os.getcwd()

        self.initUI()

        self.jogShuttle = jogShuttle = JogShuttle()
        openSerial(getInfo(commPort), 57600)
        if XILINX:
            comm.xRegs = xRegs

        sendClear()
        stdout.flush()

        if comm.ser != None:
            try:
                queParm(CFG_XILINX, getInfo(cfgXilinx))
                queParm(CFG_FCY, getInfo(cfgFcy))
                queParm(CFG_MPG, getInfo(cfgMPG))
                queParm(CFG_DRO, getInfo(cfgDRO))
                queParm(CFG_LCD, getInfo(cfgLCD))
                command(CMD_SETUP)
                sendZData()
                val = getInfo(jogZPos)
                setParm(Z_SET_LOC, val)
                command(ZSETLOC)
                sendXData()
                val = getInfo(jogXPos)
                setParm(X_SET_LOC, val)
                command(XSETLOC)
                if DRO:
                    val = int(getFloatInfo(zSvDROPosition) * \
                              jogPanel.zStepsInch)
                    queParm(Z_DRO_POS, val)
                    val = int(getFloatInfo(xSvDROPosition) * \
                              jogPanel.xStepsInch)
                    queParm(X_DRO_POS, val)
                    queParm(Z_DRO_OFFSET, zDROOffset)
                    queParm(X_DRO_OFFSET, xDROOffset)
                    queParm(Z_DRO_INCH, jogPanel.zDROInch)
                    queParm(X_DRO_INCH, jogPanel.xDROInch)
                    sendMulti()
                val = str(int(getFloatInfo(xHomeLoc) * jogPanel.xStepsInch))
                queParm(X_HOME_LOC, val)
                queParm(Z_HOME_OFFSET, zHomeOffset)
                queParm(X_HOME_OFFSET, xHomeOffset)
                queParm(X_HOME_STATUS, HOME_SUCCESS if xHomed else HOME_ACTIVE)
                val = -1 if getBoolInfo(zInvDRO) else 1
                queParm(Z_DRO_DIR, val)
                val = -1 if getBoolInfo(xInvDRO) else 1
                queParm(X_DRO_DIR, val)
                sendMulti()
                sendSpindleData()
            except CommTimeout:
                commTimeout()

        eventTable = (\
                      (EV_ZLOC, self.jogPanel.updateZ), \
                      (EV_XLOC, self.jogPanel.updateX), \
                      (EV_RPM, self.jogPanel.updateRPM), \
                      (EV_READ_ALL, self.jogPanel.updateAll), \
                      (EV_ERROR, self.jogPanel.updateError), \
                      )
                       
        self.procUpdate = [None for i in range(EV_MAX)]
        for (event, action) in eventTable:
            self.procUpdate[event] = action

        self.update = UpdateThread(self)

    def onClose(self, event):
        global done, jogPanel
        done = True
        self.update.threadRun = False
        buttonRepeat.threadRun = False
        self.Destroy()

    def OnUpdate(self, e):
        index = e.data[0]
        if index < len(self.procUpdate):
            update = self.procUpdate[index]
            if update != None:
                val = e.data[1:]
                if len(val) == 1:
                    val = val[0]
                update(val)
            
    def initUI(self):
        global jogPanel, info, zHomeOffset, xHomeOffset, \
            zDROOffset, xDROOffset

        # file menu
        fileMenu = wx.Menu()

        ID_FILE_SAVE = wx.NewId()
        menu = fileMenu.Append(ID_FILE_SAVE, 'Save')
        self.Bind(wx.EVT_MENU, self.OnSave, menu)

        ID_FILE_SAVE_RESTART = wx.NewId()
        menu = fileMenu.Append(ID_FILE_SAVE_RESTART, 'Save and Restart')
        self.Bind(wx.EVT_MENU, self.OnRestat, menu)

        ID_FILE_SAVE_PANEL = wx.NewId()
        menu = fileMenu.Append(ID_FILE_SAVE_PANEL, 'Save Panel')
        self.Bind(wx.EVT_MENU, self.OnSavePanel, menu)

        ID_FILE_LOAD_PANEL = wx.NewId()
        menu = fileMenu.Append(ID_FILE_LOAD_PANEL, 'Load Panel')
        self.Bind(wx.EVT_MENU, self.OnLoadPanel, menu)

        ID_FILE_EXIT = wx.NewId()
        menu = fileMenu.Append(ID_FILE_EXIT, 'Exit')
        self.Bind(wx.EVT_MENU, self.OnExit, menu)

        # setup menu
        setupMenu = wx.Menu()

        ID_Z_SETUP = wx.NewId()
        menu = setupMenu.Append(ID_Z_SETUP, 'Z')
        self.Bind(wx.EVT_MENU, self.OnZSetup, menu)

        ID_X_SETUP = wx.NewId()
        menu = setupMenu.Append(ID_X_SETUP, 'X')
        self.Bind(wx.EVT_MENU, self.OnXSetup, menu)

        ID_SPINDLE_SETUP = wx.NewId()
        menu = setupMenu.Append(ID_SPINDLE_SETUP, 'Spindle')
        self.Bind(wx.EVT_MENU, self.OnSpindleSetup, menu)

        ID_PORT_SETUP = wx.NewId()
        menu = setupMenu.Append(ID_PORT_SETUP, 'Port')
        self.Bind(wx.EVT_MENU, self.OnPortSetup, menu)

        ID_PORT_SETUP = wx.NewId()
        menu = setupMenu.Append(ID_PORT_SETUP, 'Config')
        self.Bind(wx.EVT_MENU, self.OnConfigSetup, menu)

        # operation menu
        operationMenu = wx.Menu()

        ID_TURN = wx.NewId()
        menu = operationMenu.Append(ID_TURN, 'Turn')
        self.Bind(wx.EVT_MENU, self.OnTurn, menu)

        ID_FACE = wx.NewId()
        menu = operationMenu.Append(ID_FACE, 'Face')
        self.Bind(wx.EVT_MENU, self.OnFace, menu)

        ID_CUTOFF = wx.NewId()
        menu = operationMenu.Append(ID_CUTOFF, 'Cutoff')
        self.Bind(wx.EVT_MENU, self.OnCutoff, menu)

        ID_TAPER = wx.NewId()
        menu = operationMenu.Append(ID_TAPER, 'Taper')
        self.Bind(wx.EVT_MENU, self.OnTaper, menu)

        if STEPPER_DRIVE:
            ID_THREAD = wx.NewId()
            menu = operationMenu.Append(ID_THREAD, 'Thread')
            self.Bind(wx.EVT_MENU, self.OnThread, menu)

        # test menu
        testMenu = wx.Menu()

        ID_TEST_SPINDLE = wx.NewId()
        menu = testMenu.Append(ID_TEST_SPINDLE, 'Spindle')
        self.Bind(wx.EVT_MENU, self.OnTestSpindle, menu)

        ID_TEST_SYNC = wx.NewId()
        menu = testMenu.Append(ID_TEST_SYNC, 'Sync')
        self.Bind(wx.EVT_MENU, self.OnTestSync, menu)

        ID_TEST_TAPER = wx.NewId()
        menu = testMenu.Append(ID_TEST_TAPER, 'Taper')
        self.Bind(wx.EVT_MENU, self.OnTestTaper, menu)

        ID_TEST_MOVE = wx.NewId()
        menu = testMenu.Append(ID_TEST_MOVE, 'Move')
        self.Bind(wx.EVT_MENU, self.OnTestMove, menu)

        menuBar = wx.MenuBar()
        menuBar.Append(fileMenu, 'File')
        menuBar.Append(setupMenu, 'Setup')
        menuBar.Append(operationMenu, 'Operation')
        menuBar.Append(testMenu, 'Test')

        self.SetMenuBar(menuBar)

        # filter = KeyEventFilter()
        # self.Bind(wx.EVT_KEY_DOWN, self.OnKeyDown)
        # self.Bind(wx.EVT_KEY_UP, self.OnKeyUp)
        # self.Bind(wx.EVT_CHAR_HOOK, self.OnKeyChar)

        sizerV = wx.BoxSizer(wx.VERTICAL)

        self.panels = {}
        self.turnPanel = panel = TurnPanel(self)
        self.panels['turnPanel'] = panel
        sizerV.Add(panel, 0, wx.EXPAND|wx.ALL, border=2)
        panel.Hide()

        self.facePanel = panel = FacePanel(self)
        self.panels['facePanel'] = panel
        sizerV.Add(panel, 0, wx.EXPAND|wx.ALL, border=2)
        panel.Hide()

        self.cutoffPanel = panel = CutoffPanel(self)
        self.panels['cutoffPanel'] = panel
        sizerV.Add(panel, 0, wx.EXPAND|wx.ALL, border=2)
        panel.Hide()

        self.taperPanel = panel = TaperPanel(self)
        self.panels['taperPanel'] = panel
        sizerV.Add(panel, 0, wx.EXPAND|wx.ALL, border=2)
        panel.Hide()

        if STEPPER_DRIVE:
            self.threadPanel = panel = ThreadPanel(self)
            self.panels['threadPanel'] = panel
            sizerV.Add(panel, 0, wx.EXPAND|wx.ALL, border=2)
            panel.Hide()

        self.jogPanel = jogPanel = JogPanel(self, style=wx.WANTS_CHARS)
        sizerV.Add(jogPanel, 0, wx.EXPAND|wx.ALL, border=2)

        self.SetSizer(sizerV)
        self.SetSizerAndFit(sizerV)

        readInfo(configFile, config)

        vars = ((zSvHomeOffset, 'zHomeOffset'), \
                (xSvHomeOffset, 'xHomeOffset'))
        if DRO:
            vars += ((zSvDROOffset, 'zDROOffset'), \
                     (xSvDROOffset, 'xDROOffset'), \
                     (zSvDROPosition, 'zDROPostion'), \
                     (xSvDROPosition, 'xDROPositon'))

        for (key, var) in vars:
            exec('global ' + var)
            if not key in configInfo.info:
               newInfo(key, "%0.4f" % (eval(var)))
            else:
                exp = var + ' = getFloatInfo(' + key + ')'
                exec(exp)
                print("%s = %s" % (var, eval(var)))
            stdout.flush()

        dw, dh = wx.DisplaySize()
        w, h = self.GetSize()
        self.SetPosition(((3 * dw) / 4 - w, 0))

        self.showPanel()

        self.turnPanel.update()
        self.facePanel.update()
        self.cutoffPanel.update()
        self.taperPanel.update()
        if STEPPER_DRIVE:
            self.threadPanel.update()

        self.taperPanel.updateUI()

    def OnSave(self, e):
        saveInfo(configFile, configTable)
        
    def OnRestat(self, e):
        saveInfo(configFile, configTable)
        os.execl(sys.executable, sys.executable, *sys.argv)

    def OnSavePanel(self, e):
        panel = getInfo(mainPanel)
        p = panel.replace('Panel', '')
        p = p[:1].upper() + p[1:].lower()
        dlg = wx.FileDialog(self, "Save " + p + " Config", self.dirName,
                            p + ".txt", "", wx.FD_SAVE)
        if dlg.ShowModal() == wx.ID_OK:
            self.dirName = dlg.GetDirectory()
            path = dlg.GetPath()
            saveList(path, configTable, self.panels[panel].getConfigList())

    def OnLoadPanel(self, e):
        panel = getInfo(mainPanel)
        p = panel.replace('Panel', '')
        p = p[:1].upper() + p[1:].lower()
        dlg = wx.FileDialog(self, "Load " + p + " Config", self.dirName,
                            p + ".txt", "", wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            self.dirName = dlg.GetDirectory()
            path = dlg.GetPath()
            readInfo(path, config, self.panels[panel].getConfigList())

    def OnExit(self, e):
        self.Close(True)

    def showDialog(self, dialog):
        global mainFrame
        (xPos, yPos) = mainFrame.GetPosition()
        dialog.Raise()
        dialog.Show(True)
        (w, h) = dialog.GetSize()
        xPos -= w
        if xPos < 1:
            xPos = 1
        dialog.SetPosition((xPos, yPos))

    def OnZSetup(self, e):
        self.showDialog(self.zDialog)

    def OnXSetup(self, e):
        self.showDialog(self.xDialog)

    def OnSpindleSetup(self, e):
        self.showDialog(self.spindleDialog)

    def OnPortSetup(self, e):
        self.showDialog(self.portDialog)

    def OnConfigSetup(self, e):
        self.showDialog(self.configDialog)

    def showPanel(self):
        key = mainPanel
        # if not key in info:
        if configInfo.info[key] == None:
            initInfo(key, InfoValue('turnPanel'))
        showPanel = getInfo(key)

        for key in self.panels:
            panel = self.panels[key]
            panel.Show() if key == showPanel else panel.Hide()
        self.Layout()
        self.Fit()

    def OnTurn(self, e):
        setInfo(mainPanel, 'turnPanel')
        self.showPanel()

    def OnFace(self, e):
        setInfo(mainPanel, 'facePanel')
        self.showPanel()

    def OnCutoff(self, e):
        setInfo(mainPanel, 'cutoffPanel')
        self.showPanel()

    def OnTaper(self, e):
        setInfo(mainPanel, 'taperPanel')
        self.showPanel()

    def OnThread(self, e):
        setInfo(mainPanel, 'threadPanel')
        self.showPanel()

    def OnTestSpindle(self, e):
        if self.testSpindleDialog == None:
            self.testSpindleDialog = TestSpindleDialog(self)
        else:
            self.testSpindleDialog.Raise()
        self.testSpindleDialog.spindleTest.test()
        self.testSpindleDialog.Show()

    def OnTestSync(self, e):
        if self.testSyncDialog == None:
            self.testSyncDialog = TestSyncDialog(self)
        else:
            self.testSyncDialog.Raise()
        self.testSyncDialog.syncTest.test()
        self.testSyncDialog.Show()

    def OnTestTaper(self, e):
        if self.testTaperDialog == None:
            self.testTaperDialog = TestTaperDialog(self)
        else:
            self.testTaperDialog.Raise()
        self.testTaperDialog.taperTest.test()
        self.testTaperDialog.Show()

    def OnTestMove(self, e):
        if self.testMoveDialog == None:
            self.testMoveDialog = TestMoveDialog(self)
        else:
            self.testMoveDialog.Raise()
        self.testMoveDialog.moveTest.test()
        self.testMoveDialog.Show()

class ZDialog(wx.Dialog, FormRoutines):
    def __init__(self, frame):
        pos = (10, 10)
        wx.Dialog.__init__(self, frame, -1, "Z Setup", pos, \
                            wx.DefaultSize, wx.DEFAULT_DIALOG_STYLE)
        self.Bind(wx.EVT_SHOW, self.OnShow)
        self.sizerV = sizerV = wx.BoxSizer(wx.VERTICAL)

        sizerG = wx.FlexGridSizer(2, 0, 0)

        self.fields = (
            ("Pitch", zPitch), \
            ("Motor Steps", zMotorSteps), \
            ("Micro Steps", zMicroSteps), \
            ("Motor Ratio", zMotorRatio), \
            ("Backlash", zBacklash), \
            ("Accel Unit/Sec2", zAccel), \
            ("Min Speed U/Min", zMinSpeed), \
            ("Max Speed U/Min", zMaxSpeed), \
            ("Jog Min U/Min", zJogMin), \
            ("Jog Max U/Min", zJogMax), \
            ("Probe Dist", zProbeDist), \
            ("Probe Speed", zProbeSpeed), \
            ("bInvert Dir", zInvDir), \
            ("bInvert MPG", zInvMpg), \
            ("DRO Inch", zDROInch), \
            ("bInv DRO", zInvDRO), \
        )        
        self.fieldList(sizerG, self.fields)

        sizerV.Add(sizerG, flag=wx.LEFT|wx.ALL, border=2)

        btn = wx.Button(self, label='Setup Z', size=(60,-1))
        btn.Bind(wx.EVT_BUTTON, self.OnSetup)
        sizerV.Add(btn, 0, wx.ALL|wx.CENTER, 5)

        sizerH = wx.BoxSizer(wx.HORIZONTAL)

        sizerH.Add((0, 0), 0, wx.EXPAND)
        btn = wx.Button(self, wx.ID_OK)
        btn.SetDefault()
        sizerH.Add(btn, 0, wx.ALL, 5)

        btn = wx.Button(self, wx.ID_CANCEL)
        btn.Bind(wx.EVT_BUTTON, self.OnCancel)
        sizerH.Add(btn, 0, wx.ALL, 5)

        sizerV.Add(sizerH, 0, wx.ALIGN_RIGHT)

        self.SetSizer(sizerV)
        self.sizerV.Fit(self)
        self.Show(False)

    def OnSetup(self, e):
        global moveCommands
        moveCommands.queClear()
        sendZData(True)

    def OnShow(self, e):
        global done, zDataSent
        if done:
            return
        if self.IsShown():
            self.fieldInfo = {}
            for (label, index) in self.fields:
                self.fieldInfo[index] = getInfo(index)
        else:
            for (label, index) in self.fields:
                if self.fieldInfo[index] != getInfo(index):
                    zDataSent = False
                    break

    def OnCancel(self, e):
        for (label, index) in self.fields:
            setInfo(index, self.fieldInfo[index])
        self.Show(False)

class XDialog(wx.Dialog, FormRoutines):
    def __init__(self, frame):
        pos = (10, 10)
        wx.Dialog.__init__(self, frame, -1, "X Setup", pos, \
                            wx.DefaultSize, wx.DEFAULT_DIALOG_STYLE)
        self.Bind(wx.EVT_SHOW, self.OnShow)
        self.sizerV = sizerV = wx.BoxSizer(wx.VERTICAL)

        sizerG = wx.FlexGridSizer(2, 0, 0)

        self.fields = (
            ("Pitch", xPitch), \
            ("Motor Steps", xMotorSteps), \
            ("Micro Steps", xMicroSteps), \
            ("Motor Ratio", xMotorRatio), \
            ("Backlash", xBacklash), \
            ("Accel Unit/Sec2", xAccel), \
            ("Min Speed U/Min", xMinSpeed), \
            ("Max Speed U/Min", xMaxSpeed), \
            ("Jog Min U/Min", xJogMin), \
            ("Jog Max U/Min", xJogMax), \
            ("bInvert Dir", xInvDir), \
            ("bInvert MPG", xInvMpg), \
            ("Probe Dist", xProbeDist), \
            ("Home Dist", xHomeDist), \
            ("Backoff Dist", xHomeBackoffDist), \
            ("Home Speed", xHomeSpeed), \
            ("bHome Dir", xHomeDir), \
            ("DRO Inch", xDROInch), \
            ("bInv DRO", xInvDRO), \
        )        
        global HOME_TEST
        if HOME_TEST:
            self.fields += (
                ("Home Start", xHomeStart), \
                ("Home End", xHomeEnd), \
                ("Home Loc", xHomeLoc))
        self.fieldList(sizerG, self.fields)

        sizerV.Add(sizerG, flag=wx.LEFT|wx.ALL, border=2)

        if HOME_TEST:
            btn = wx.Button(self, label='Set Home Loc')#, size=(60,-1))
            btn.Bind(wx.EVT_BUTTON, self.OnSetHomeLoc)
            sizerV.Add(btn, 0, wx.ALL|wx.CENTER, 5)

        btn = wx.Button(self, label='Setup X', size=(60,-1))
        btn.Bind(wx.EVT_BUTTON, self.OnSetup)
        sizerV.Add(btn, 0, wx.ALL|wx.CENTER, 5)

        sizerH = wx.BoxSizer(wx.HORIZONTAL)

        sizerH.Add((0, 0), 0, wx.EXPAND)
        btn = wx.Button(self, wx.ID_OK)
        btn.SetDefault()
        sizerH.Add(btn, 0, wx.ALL, 5)

        btn = wx.Button(self, wx.ID_CANCEL)
        btn.Bind(wx.EVT_BUTTON, self.OnCancel)
        sizerH.Add(btn, 0, wx.ALL, 5)

        sizerV.Add(sizerH, 0, wx.ALIGN_RIGHT)

        self.SetSizer(sizerV)
        self.sizerV.Fit(self)
        self.Show(False)

    def OnSetHomeLoc(self, e):
        global jogPanel
        loc = str(int(getFloatInfo(xHomeLoc) * jogPanel.xStepsInch))
        setParm(X_HOME_LOC, loc)
        
    def OnSetup(self, e):
        moveCommans.queClear()
        sendXData(True)

    def OnShow(self, e):
        global done, xDataSent
        if done:
            return
        if self.IsShown():
            self.fieldInfo = {}
            for (label, index) in self.fields:
                self.fieldInfo[index] = getInfo(index)
        else:
            for (label, index) in self.fields:
                if self.fieldInfo[index] != getInfo(index):
                    xDataSent = False
                    break

    def OnCancel(self, e):
        for (label, index) in self.fields:
            setInfo(index, self.fieldInfo[index])
        self.Show(False)

class SpindleDialog(wx.Dialog, FormRoutines):
    def __init__(self, frame):
        pos = (10, 10)
        wx.Dialog.__init__(self, frame, -1, "Spindle Setup", pos, \
                            wx.DefaultSize, wx.DEFAULT_DIALOG_STYLE)
        self.sizerV = sizerV = wx.BoxSizer(wx.VERTICAL)
        self.Bind(wx.EVT_SHOW, self.OnShow)
        sizerG = wx.FlexGridSizer(2, 0, 0)

        self.fields = (
            ("bStepper Drive", spStepDrive), \
        )
        if STEPPER_DRIVE:
            self.fields += (
                ("Motor Steps", spMotorSteps), \
                ("Micro Steps", spMicroSteps), \
                ("Min RPM", spMinRPM), \
                ("Max RPM", spMaxRPM), \
                ("Accel RPM/Sec2", spAccel), \
                ("Jog Min", spJogMin), \
                ("Jog Max", spJogMax), \
                # ("Jog Accel Time", spJogAccelTime), \
                ("bInvert Dir", spInvDir), \
                ("bTest Index", spTestIndex), \
            )
        self.fieldList(sizerG, self.fields)

        sizerV.Add(sizerG, flag=wx.LEFT|wx.ALL, border=2)

        # spindle start and stop

        if STEPPER_DRIVE:
            sizerH = wx.BoxSizer(wx.HORIZONTAL)

            btn = wx.Button(self, label='Start', size=(60,-1))
            btn.Bind(wx.EVT_BUTTON, self.OnStart)
            sizerH.Add(btn, 0, wx.ALL, 5)

            btn = wx.Button(self, label='Stop', size=(60,-1))
            btn.Bind(wx.EVT_BUTTON, self.OnStop)
            sizerH.Add(btn, 0, wx.ALL, 5)

            sizerV.Add(sizerH, 0, wx.CENTER)

        # ok and cancel buttons

        sizerH = wx.BoxSizer(wx.HORIZONTAL)

        btn = wx.Button(self, wx.ID_OK)
        btn.SetDefault()
        sizerH.Add(btn, 0, wx.ALL, 5)

        btn = wx.Button(self, wx.ID_CANCEL)
        btn.Bind(wx.EVT_BUTTON, self.OnCancel)
        sizerH.Add(btn, 0, wx.ALL, 5)

        sizerV.Add(sizerH, 0, wx.ALIGN_RIGHT)

        self.SetSizer(sizerV)
        self.sizerV.Fit(self)

    def OnStart(self, e):
        global spindleDataSent
        for (label, index) in self.fields:
            tmp = getInfo(index)
            if self.fieldInfo[index] != tmp:
                self.fieldInfo[index] = tmp 
                spindleDataSent = False
        if not spindleDataSent:
            sendSpindleData()
        else:
            command(CMD_SPSETUP)
        command(SPINDLE_START)

    def OnStop(self, e):
        command(SPINDLE_STOP)

    def OnShow(self, e):
        global done, spindleDataSent
        if done:
            return
        if self.IsShown():
            self.fieldInfo = {}
            self.cancelInfo = {}
            for (label, index) in self.fields:
                tmp = getInfo(index)
                self.cancelInfo[index] = tmp
                self.fieldInfo[index] = tmp
            spindleDataSent = False
        else:
            for (label, index) in self.fields:
                if self.fieldInfo[index] != getInfo(index):
                    spindleDataSent = False
                    break

    def OnCancel(self, e):
        for (label, index) in self.fields:
            setInfo(index, self.cancelInfo[index])
        self.Show(False)

class PortDialog(wx.Dialog, FormRoutines):
    def __init__(self, frame):
        pos = (10, 10)
        wx.Dialog.__init__(self, frame, -1, "Port Setup", pos, \
                            wx.DefaultSize, wx.DEFAULT_DIALOG_STYLE)
        self.sizerV = sizerV = wx.BoxSizer(wx.VERTICAL)
        self.Bind(wx.EVT_SHOW, self.OnShow)
        sizerG = wx.GridSizer(2, 0, 0)

        self.fields = (
            ("Comm Port", commPort),)
        self.fieldList(sizerG, self.fields)

        sizerV.Add(sizerG, flag=wx.LEFT|wx.ALL, border=2)
        sizerH = wx.BoxSizer(wx.HORIZONTAL)

        sizerH.Add((0, 0), 0, wx.EXPAND)
        btn = wx.Button(self, wx.ID_OK)
        btn.SetDefault()
        sizerH.Add(btn, 0, wx.ALL, 5)

        btn = wx.Button(self, wx.ID_CANCEL)
        btn.Bind(wx.EVT_BUTTON, self.OnCancel)
        sizerH.Add(btn, 0, wx.ALL, 5)

        sizerV.Add(sizerH, 0, wx.ALIGN_RIGHT)

        self.SetSizer(sizerV)
        self.sizerV.Fit(self)
        self.Show(False)

    def OnShow(self, e):
        global done
        if done:
            return
        if self.IsShown():
            self.fieldInfo = {}
            for (label, index) in self.fields:
                self.fieldInfo[index] = getInfo(index)

    def OnCancel(self, e):
        for (label, index) in self.fields:
            setInfo(index, self.fieldInfo[index])
        self.Show(False)

class ConfigDialog(wx.Dialog, FormRoutines):
    def __init__(self, frame):
        global XILINX
        pos = (10, 10)
        wx.Dialog.__init__(self, frame, -1, "Config Setup", pos, \
                            wx.DefaultSize, wx.DEFAULT_DIALOG_STYLE)
        self.sizerV = sizerV = wx.BoxSizer(wx.VERTICAL)
        self.Bind(wx.EVT_SHOW, self.OnShow)
        sizerG = wx.GridSizer(2, 0, 0)

        self.fields = (
            ("bHW Control", cfgXilinx), \
            ("bMPG", cfgMPG), \
            ("bDRO", cfgDRO), \
            ("bLCD", cfgLCD), \
            ("bProbe Inv", cfgPrbInv), \
            ("fcy", cfgFcy), \
            ("bDisable Commands", cfgCmdDis), \
            ("bDraw Moves", cfgDraw), \
            ("bSave Debug", cfgDbgSave), \
        )
        if XILINX:
            self.fields += (
                ("Encoder", cfgEncoder), \
                ("Xilinx Freq", cfgXFreq), \
                ("Freq Mult", cfgFreqMult), \
                ("bTest Mode", cfgTestMode), \
                ("Test RPM", cfgTestRPM), \
                ("bInvert Enc Dir", cfgInvEncDir), \
            )
        self.fieldList(sizerG, self.fields)

        sizerV.Add(sizerG, flag=wx.CENTER|wx.ALL, border=2)

        sizerH = wx.BoxSizer(wx.HORIZONTAL)

        sizerH.Add((0, 0), 0, wx.EXPAND)
        btn = wx.Button(self, wx.ID_OK)
        btn.SetDefault()
        sizerH.Add(btn, 0, wx.ALL, 5)

        btn = wx.Button(self, wx.ID_CANCEL)
        btn.Bind(wx.EVT_BUTTON, self.OnCancel)
        sizerH.Add(btn, 0, wx.ALL, 5)

        sizerV.Add(sizerH, 0, wx.ALIGN_RIGHT)

        self.SetSizer(sizerV)
        self.sizerV.Fit(self)
        self.Show(False)

    def OnShow(self, e):
        global done
        if done:
            return
        if self.IsShown():
            self.fieldInfo = {}
            for (label, index) in self.fields:
                self.fieldInfo[index] = getInfo(index)

    def OnCancel(self, e):
        for (label, index) in self.fields:
            setInfo(index, self.fieldInfo[index])
        self.Show(False)

def testText(dialog):
    global testFont
    dialog.sizerV = sizerV = wx.BoxSizer(wx.VERTICAL)

    txt = wx.TextCtrl(dialog, style=wx.TE_MULTILINE, size=(650,350))
    txt.SetFont(testFont)
    # w, h = txt.GetTextExtent("0123456789")
    # w *= 8
    # h *= 24
    # txt.SetSize((w, h))
    sizerV.Add(txt)

    dialog.SetSizer(sizerV)
    dialog.sizerV.Fit(dialog)
    return(txt)

class TestSpindleDialog(wx.Dialog):
    def __init__(self, frame):
        pos = (10, 10)
        wx.Dialog.__init__(self, frame, -1, "Test Spindle", pos, \
                            wx.DefaultSize, wx.DEFAULT_DIALOG_STYLE)

        txt = testText(self)
        self.spindleTest = SpindleTest(txt)
        
class TestSyncDialog(wx.Dialog):
    def __init__(self, frame):
        pos = (10, 10)
        wx.Dialog.__init__(self, frame, -1, "Test Sync", pos, \
                            wx.DefaultSize, wx.DEFAULT_DIALOG_STYLE)

        txt = testText(self)
        self.syncTest = SyncTest(txt)

class TestTaperDialog(wx.Dialog):
    def __init__(self, frame):
        pos = (10, 10)
        wx.Dialog.__init__(self, frame, -1, "Test Taper", pos, \
                            wx.DefaultSize, wx.DEFAULT_DIALOG_STYLE)

        txt = testText(self)
        self.taperTest = TaperTest(txt)

class TestMoveDialog(wx.Dialog):
    def __init__(self, frame):
        pos = (10, 10)
        wx.Dialog.__init__(self, frame, -1, "Test Move", pos, \
                            wx.DefaultSize, wx.DEFAULT_DIALOG_STYLE)

        txt = testText(self)
        self.moveTest = MoveTest(txt)

def dbgPrt(txt, format, values):
    global f
    txt.AppendText((format + "\n") % values)
    f.write((format + "\n") % values)

fcy = 90000000

class SpindleTest():
    def __init__(self, txt):
        self.txt = txt

    def test(self):
        global f
        global fcy
        txt = self.txt
        txt.SetValue("")
        minRPM = getFloatInfo(spMinRPM) # minimum rpm
        maxRPM = getFloatInfo(spMaxRPM) # maximum rpm
        accel = getFloatInfo(spAccel)   # accel rpm per sec
        
        f = open('spindle.txt','w')
        
        dbgPrt(txt,"minRPM %d maxRPM %d", (minRPM, maxRPM))
        
        spindleMicroSteps = getIntInfo(spMicroSteps)
        spindleMotorSteps = getIntInfo(spMotorSteps)
        spindleStepsRev = spindleMotorSteps * spindleMicroSteps
        dbgPrt(txt,"spindleStepsRev %d", (spindleStepsRev))
        
        spindleStepsSec = (maxRPM * spindleStepsRev) / 60.0
        spindleClocksStep = int(fcy / spindleStepsSec + .5)
        spindleClockPeriod = (float(spindleClocksStep) / fcy) * 1000000
        spindleClocksRev = spindleStepsRev * spindleClocksStep
        dbgPrt(txt,"spindleClocksStep %d spindleClockPeriod %6.3f us " +
               "spindleClocksRev %d", 
               (spindleClocksStep, spindleClockPeriod, spindleClocksRev))
        
        # accelStepsSec2 = (accel * spindleStepsRev) / 60
        
        sStepsSecMin = float(minRPM * spindleStepsRev) / 60
        sStepsSecMax = float(maxRPM * spindleStepsRev) / 60
        deltaV = sStepsSecMax - sStepsSecMin
        dbgPrt(txt,"deltaV %4.1f sStepsSecMin %4.1f sStepsSecMax %4.1f", \
               (deltaV, sStepsSecMin, sStepsSecMax))
        if False:
            accelStepsSec2 = deltaV / aTime
            accel = (accelStepsSec2 / spindleStepsRev) * 60
        else:
            accelStepsSec2 = (accel / 60) * spindleStepsRev
            aTime = deltaV / accelStepsSec2

        dbgPrt(txt,"accel %0.1f rpm per sec", (accel))
        
        accelMinTime = sStepsSecMin / accelStepsSec2
        accelMaxTime = sStepsSecMax / accelStepsSec2
        dbgPrt(txt,"accelMinTime %5.5f accelMaxTime %5.2f", \
               (accelMinTime, accelMaxTime))
        
        accelMinSteps = int((sStepsSecMin * accelMinTime) / 2.0 + 0.5)
        accelMaxSteps = int((sStepsSecMax * accelMaxTime) / 2.0 + 0.5)
        dbgPrt(txt,"accelMinSteps %d accelMaxSteps %d ", \
               (accelMinSteps, accelMaxSteps))
        
        accelTime = deltaV / accelStepsSec2
        accelSteps = accelMaxSteps - accelMinSteps
        accelClocks = accelTime * fcy;
        dbgPrt(txt,"accelStepsSec2 %0.1f accelTime %5.3f accelSteps %d "\
               "accelClocks %d", \
               (accelStepsSec2, accelTime, accelSteps, accelClocks))
        
        accelRev = float(accelSteps) / spindleStepsRev
        dbgPrt(txt,"accelRev %5.3f", (accelRev))
        
        cFactorA = (fcy * sqrt(2)) / sqrt(accelStepsSec2)
        cFactorB = spindleClocksStep / (sqrt(accelMaxSteps) -
                                        sqrt(accelMaxSteps - 1))
        dbgPrt(txt,"cFactorA %0.2f cFactorB %0.2f", (cFactorA, cFactorB))
        cFactor = cFactorB
        
        lastCount = int(cFactor * sqrt(accelMinSteps))
        lastTime = float(lastCount) / fcy
        
        dbgPrt(txt,"accelMinSteps %d lastCount %d lastTime %0.6f", \
               (accelMinSteps, lastCount, lastTime))
        
        f.write("\n")
        
        lastCtr = 0
        step = accelMinSteps
        while step < accelMaxSteps:
            step += 1
            count = int(cFactor * sqrt(step))
            pre = 1
            ctr = count - lastCount
            if ctr > 65535:
                pre <<= 1
                ctr >>= 1
                while ctr > 65535:
                    pre <<= 1
                    ctr >>= 1
                actCount = lastCount + ctr * pre
            else:
                actCount = count
            time = float(actCount) / fcy
            delta = time - lastTime
            freq = 1.0 / delta
            rpm = (freq / spindleStepsRev) * 60
            f.write("step %4d count %9d %9d pre %d %5d %6d t %8.6f %8.6f "\
                    "f %8.2f rpm %4.1f\n" % \
                    (step, count, actCount, pre, ctr, ctr * pre - lastCtr, \
                     time, delta, freq, rpm))
            lastCount = actCount
            lastCtr = ctr * pre
            lastTime = time
        
        f.write("\n")
        
        finalCount = int(cFactor * sqrt(accelMaxSteps))
        finalCount -= int(cFactor * sqrt(accelMaxSteps - 1))
        dbgPrt(txt,"finalCount %d lastCtr %d spindleClocksStep %d", \
               (finalCount, ctr, spindleClocksStep))
        
        f.write("\n***\n\n");
        
        while step > accelMinSteps:
            step -= 1
            count = int(cFactor * sqrt(step))
            ctr = lastCount - count
            time = float(count) / fcy
            delta = lastTime - time
            freq = 1.0 / delta
            rpm = (freq / spindleStepsRev) * 60
            f.write("step %4d count %9d %7d %5d t %8.6f %8.6f "\
                    "f %8.2f rpm %4.1f\n" % \
                    (step, count, ctr, ctr - lastCtr, time, delta, freq, rpm))
            lastCount = count
            lastCtr = ctr
            lastTime = time
        
        lastCount = int(cFactor * sqrt(accelMinSteps))
        f.write("\naccelMinSteps %d lastCount %d\n" % \
                (accelMinSteps, lastCount))
        
        f.close()
    
class SyncTest(object):
    def __init__(self, txt):
        self.txt = txt

    def test(self):
        global f, fcy, info
        txt = self.txt
        txt.SetValue("")
        print("")
        f = open('zsync.txt','w')
   
        zAxis = True
        panel = getInfo(mainPanel)
        if panel == 'threadPanel':
            arg1 = getFloatInfo(thPitch)
        elif panel == 'turnPanel':
            arg1 = getFloatInfo(tuZFeed)
        elif panel == 'facePanel':
            arg1 = getFloatInfo(faXFeed)
            zAxis = False
        elif panel == 'CutoffPanel':
            arg1 = getFloatInfo(cuXFeed)
            zAxis = False
        elif panel == 'taperPanel':
            arg1 = getFloatInfo(tpZFeed)

        maxRPM = getFloatInfo(spMaxRPM) # maximum rpm

        spindleMicroSteps = getIntInfo(spMicroSteps)
        spindleMotorSteps = getIntInfo(spMotorSteps)
        spindleStepsRev = spindleMotorSteps * spindleMicroSteps
        dbgPrt(txt,"spindleStepsRev %d", (spindleStepsRev))
        
        spindleStepsSec = (maxRPM * spindleStepsRev) / 60.0
        spindleClocksStep = int(fcy / spindleStepsSec + .5)
        spindleClockPeriod = (float(spindleClocksStep) / fcy) * 1000000
        spindleClocksRev = spindleStepsRev * spindleClocksStep
        dbgPrt(txt,"spindleClocksStep %d spindleClockPeriod %6.3f us "\
               "spindleClocksRev %d", \
               (spindleClocksStep, spindleClockPeriod, spindleClocksRev))
        dbgPrt(txt, "", ())

        if zAxis:
            pitch = getFloatInfo(zPitch)
            microSteps = getFloatInfo(zMicroSteps)
            motorSteps = getFloatInfo(zMotorSteps)
            motorRatio = getFloatInfo(zMotorRatio)
        else:
            pitch = getFloatInfo(xPitch)
            microSteps = getFloatInfo(xMicroSteps)
            motorSteps = getFloatInfo(xMotorSteps)
            motorRatio = getFloatInfo(xMotorRatio)

        zStepsInch = ((microSteps * motorSteps * motorRatio) / pitch)
        dbgPrt(txt,"zStepsInch %d", (zStepsInch))

        if arg1 >= 8:
            inch = True
            inchPitch = False
            tpi = arg1
        else:
            inch = False
            pitch = arg1;
            if pitch < .3:
                inchPitch = True
        
        if inchPitch:
            revCycle = int(1.0 / pitch + 0.5)
            if revCycle > 20:
                revCycle = 20
            cycleDist = revCycle * pitch
            dbgPrt(txt,"pitch %5.3f revCycle %d cycleDist %5.3f", \
                   (pitch, revCycle, cycleDist))
            clocksCycle = spindleClocksRev * revCycle
            spindleStepsCycle = spindleStepsRev * revCycle
            zStepsCycle = zStepsInch * revCycle * pitch
        elif inch:
            clocksCycle = spindleClocksRev * tpi
            spindleStepsCycle = spindleStepsRev * tpi
            zStepsCycle = zStepsInch
            pitch = 1.0 / tpi
            dbgPrt(txt,"tpi %d pitch %5.3f", (tpi, pitch))
        else:
            revolutions = 127
            inches = (pitch * revolutions) / 25.4
            dbgPrt(txt,"pitch %4.2f mm inches %5.3f", (pitch, inches))
        
            clocksCycle = spindleClocksRev * revolutions
            spindleStepsCycle = spindleStepsRev * revolutions
            zStepsCycle = zStepsInch * inches
        
        cycleTime = float(clocksCycle) / fcy
        dbgPrt(txt,"clocksCycle %d cycleTime %4.2f\nspindleStepsCycle %d "\
               "zStepsCycle %d", \
               (clocksCycle, cycleTime, spindleStepsCycle, zStepsCycle))
        
        zClocksStep = int(clocksCycle / zStepsCycle + 0.5)
        zRemainder = (clocksCycle - zClocksStep * zStepsCycle)
        dbgPrt(txt,"zClocksStep %d remainder %d", \
               (zClocksStep, zRemainder))
        
        dx = zStepsCycle
        dy = zRemainder
        incr1 = 2 * dy
        incr2 = incr1 - 2 * dx
        d = incr1 - dx
        dbgPrt(txt,"incr1 %d incr2 %d d %d", (incr1, incr2, d))
        
        sum = d
        x = 0
        y = 0
        clocks = 0
        while (x < zStepsCycle):
            x += 1
            clocks += zClocksStep
            if sum < 0:
                sum += incr1
            else:
                y += 1
                sum += incr2
                clocks += 1
        dbgPrt(txt,"clocks %d x %d y %d", (clocks, x, y))
        
        dbgPrt(txt,"", ())
        
        zSpeedIPM = pitch * maxRPM
        zStepsPerSec = int((zSpeedIPM * zStepsInch) / 60)
        dbgPrt(txt,"zSpeedIPM %4.2f in/min zStepsSec %d steps/sec", \
               (zSpeedIPM, zStepsPerSec))
        
        zAccel = .5                      # acceleration in per sec^2
        zAccelTime = ((zSpeedIPM / 60.0) / zAccel) # acceleration time
        dbgPrt(txt,"zAccel %5.3f in/sec^2 zAccelTime %8.6f sec", \
               (zAccel, zAccelTime))
        
        zAccelStepsSec2 = zAccel * zStepsInch
        dbgPrt(txt,"zAccelStepsSec2 %3.0f steps/sec^2", (zAccelStepsSec2))
        
        zAccelSteps = int((zAccelTime * zStepsPerSec) / 2.0)
        if zAccelSteps != 0:
            cFactorA = (fcy * sqrt(2)) / sqrt(zAccelStepsSec2)
            cFactorB = zClocksStep / (sqrt(zAccelSteps) -
                                      sqrt(zAccelSteps - 1))
            dbgPrt(txt,"cFactorA %0.2f cFactorB %0.2f", (cFactorA, cFactorB))
            cFactor1 = cFactorB
        
            zAccelClocks = int(cFactor1 * sqrt(zAccelSteps))
            zAccelTime = float(zAccelClocks) / fcy
            zAccelDist = float(zAccelSteps) / zStepsInch
            dbgPrt(txt,"zAccelTime %8.6f zAccelSteps %d zAccelClocks %d "\
                   "zAccelDist %5.3f", \
                   (zAccelTime, zAccelSteps, zAccelClocks, zAccelDist))
        
            initialCount = int(cFactor1 * sqrt(1))
            initialCount -= int(cFactor1 * sqrt(0))
            finalCount = int(cFactor1 * sqrt(zAccelSteps))
        
            isrCount = finalCount + initialCount
        
            dbgPrt(txt,"initialCount %d initialTime %8.6f accelTime %8.6f "\
                   "hwTime %8.6f", \
                   (initialCount, float(initialCount) / fcy, \
                    float(finalCount) / fcy, float(isrCount) / fcy))
        
            zAccelSpindleSteps = int(isrCount / spindleClocksStep)
            remainder = isrCount - zAccelSpindleSteps * spindleClocksStep
            dbgPrt(txt,"zAccelSpindleSteps %d remainder %d", \
                   (zAccelSpindleSteps, remainder))
        
            f.write("\n");
        
            lastCount = 0
            lastTime = 0
            lastCtr = 0
            # dbgPrt(txt,"lastCount %d lastTime %0.6f" % (lastCount, lastTime)
            for step in range(1, zAccelSteps + 1):
                count = int(cFactor1 * sqrt(step))
                ctr = count - lastCount
                time = float(count) / fcy
                delta = time - lastTime
                freq = 1.0 / delta
                ipm = (freq / zStepsInch) * 60
                f.write("step %4d count %9d %9d %9d t %8.6f %8.6f "\
                        "f %7.2f ipm %4.1f\n" % \
                        (step, count, ctr, ctr - lastCtr, time, delta, \
                         freq, ipm))
                lastCount = count
                lastCtr = ctr
                lastTime = time
        
            f.write("\n");
        
            # countRemainder = zAccelClocks - lastCount
            # div = int(countRemainder / zAccelSteps)
            # rem = countRemainder - zAccelSteps * div
            # dbgPrt(txt,"lastCount %d countRemainder %d div %d rem %d" % \
            #        (lastCount, countRemainder, div, rem))
        
            lastCount1 = int(cFactor1 * sqrt(zAccelSteps))
            lastTime1 = time = float(count) / fcy
            dbgPrt(txt,"lastCount1 %d lastTime1 %0.6f", \
                   (lastCount1, lastTime1))
        
            # spindleSteps = lastCount1 / spindleClocksStep
            # spindleCount = spindleSteps * spindleClocksStep
            # countRemainder = lastCount1 - (spindleSteps * spindleClocksStep)
        
            # div = int(countRemainder / zAccelSteps)
            # rem = countRemainder - zAccelSteps * div
            # dbgPrt(txt,"spindleSteps %d lastCount %d countRemainder %d div "\
            #"%d rem %d", \
            #        (spindleSteps, lastCount, countRemainder, div, rem))
        
            finalCount -= int(cFactor1 * sqrt(zAccelSteps - 1))
            dbgPrt(txt,"finalCount %d lastCtr %d zClocksStep %d", \
                   (finalCount, lastCtr, zClocksStep))
        
        f.close()

class TaperTest(object):
    def __init__(self, txt):
        self.txt = txt

    def test(self):
        global f
        global fcy
        txt = self.txt
        txt.SetValue("")
        f = open('taper.txt','w')
        
        maxRPM = getFloatInfo(spMaxRPM) # maximum rpm
        spindleMicroSteps = getIntInfo(spMicroSteps)
        spindleMotorSteps = getIntInfo(spMotorSteps)
        spindleStepsRev = spindleMotorSteps * spindleMicroSteps
        dbgPrt(txt,"spindleStepsRev %d", (spindleStepsRev))

        spindleStepsSec = (maxRPM * spindleStepsRev) / 60.0
        spindleClocksStep = int(fcy / spindleStepsSec + .5)
        spindleClockPeriod = (float(spindleClocksStep) / fcy) * 1000000
        spindleClocksRev = spindleStepsRev * spindleClocksStep
        dbgPrt(txt,"spindleClocksStep %d spindleClockPeriod %6.3f us "\
               "spindleClocksRev %d", \
               (spindleClocksStep, spindleClockPeriod, spindleClocksRev))
        dbgPrt(txt, "", ())

        pitch = getFloatInfo(zPitch)
        microSteps = getFloatInfo(zMicroSteps)
        motorSteps = getFloatInfo(zMotorSteps)
        motorRatio = getFloatInfo(zMotorRatio)

        zStepsInch = ((microSteps * motorSteps * motorRatio) / pitch)
        dbgPrt(txt,"zStepsInch %d", (zStepsInch))

        pitch = getFloatInfo(xPitch)
        microSteps = getFloatInfo(xMicroSteps)
        motorSteps = getFloatInfo(xMotorSteps)
        motorRatio = getFloatInfo(xMotorRatio)
        xStepsInch = ((microSteps * motorSteps * motorRatio) / pitch)
        dbgPrt(txt,"xStepsInch %d", (xStepsInch))

        pitch = getFloatInfo(tpZFeed)
        revCycle = int(1.0 / pitch + 0.5)
        if revCycle > 20:
            revCycle = 20
        cycleDist = revCycle * pitch
        dbgPrt(txt,"pitch %5.3f revCycle %d cycleDist %5.3f", \
               (pitch, revCycle, cycleDist))
        clocksCycle = spindleClocksRev * revCycle
        spindleStepsCycle = spindleStepsRev * revCycle
        zStepsCycle = zStepsInch * revCycle * pitch

        zClocksStep = int(clocksCycle / zStepsCycle + 0.5)
        zRemainder = (clocksCycle - zClocksStep * zStepsCycle)
        dbgPrt(txt,"zClocksStep %d remainder %d", \
               (zClocksStep, zRemainder))

        arg2 = getFloatInfo(tpZDelta)
        arg3 = getFloatInfo(tpXDelta)
        
        d0 = arg2
        d1 = arg3
        
        zCycleDist = float(zStepsCycle) / zStepsInch
        xCycleDist = (d1 / d0) * zCycleDist
        dbgPrt(txt,"zCycleDist %5.3f xCycleDist %5.3f", \
               (zCycleDist, xCycleDist))
        
        d0Steps = int(zCycleDist * zStepsInch)
        d1Steps = int(xCycleDist * xStepsInch)
        d0Clocks = d0Steps * zClocksStep
        dbgPrt(txt,"d0Steps %d d1Steps %d d0Clocks %d", \
               (d0Steps, d1Steps, d0Clocks));
        
        # d1ClocksStep = int(d0Clocks / d1Steps)
        # d1Remainder = d0Clocks - d1Steps * d1ClocksStep
        # dbgPrt(txt,"d1ClocksStep %d d1Remainder %d", \
        #        (d1ClocksStep, d1Remainder))
        
        d1ClocksStep = int(clocksCycle / d1Steps)
        d1Remainder = clocksCycle - d1Steps * d1ClocksStep
        dbgPrt(txt,"d1ClocksStep %d d1Remainder %d", \
               (d1ClocksStep, d1Remainder))
        
        dx = d1Steps;
        dy = d1Remainder;
        incr1 = 2 * dy;
        incr2 = incr1 - 2 * dx;
        d = incr1 - dx;
        dbgPrt(txt,"incr1 %d incr2 %d d %d", \
               (incr1, incr2, d));
        
        f.close()

class MoveTest(object):
    def __init__(self, txt):
        self.txt = txt

    def test(self):
        global f
        global fcy
        txt = self.txt
        txt.SetValue("")
        
        f = open('move.txt','w')

        pitch = getFloatInfo(zPitch)
        microSteps = getFloatInfo(zMicroSteps)
        motorSteps = getFloatInfo(zMotorSteps)
        motorRatio = getFloatInfo(zMotorRatio)

        zStepsInch = ((microSteps * motorSteps * motorRatio) / pitch)
        dbgPrt(txt,"zStepsInch %d", (zStepsInch))
        
        minSpeed = getFloatInfo(zMinSpeed) # minimum speed ipm
        maxSpeed = getFloatInfo(zMaxSpeed) # maximum speed ipm
        zMoveAccelTime = getFloatInfo(zAccel) # accel time seconds
        dbgPrt(txt,"zMinSpeed %d zMaxSpeed %d zMoveAccelTime %4.2f", \
               (minSpeed, maxSpeed, zMoveAccelTime))
        
        zMStepsSec = int((maxSpeed * zStepsInch) / 60.0)
        zMClocksStep = int(fcy / zMStepsSec)
        dbgPrt(txt,"zMStepsSec %d zMClocksStep %d", (zMStepsSec, zMClocksStep))
        
        zMinStepsSec = int((zStepsInch * minSpeed) / 60.0)
        zMaxStepsSec = int((zStepsInch * maxSpeed) / 60.0)
        dbgPrt(txt,"zMinStepsSec %d zMaxStepsSec %d", \
               (zMinStepsSec, zMaxStepsSec))
        
        zMDeltaV = zMaxStepsSec - zMinStepsSec
        zMAccelStepsSec2 = zMDeltaV / zMoveAccelTime
        dbgPrt(txt,"zMDeltaV %d zMAccelStepsSec2 %6.3f", \
               (zMDeltaV, zMAccelStepsSec2))
        
        if zMAccelStepsSec2 != 0:
            zMAccelMinTime = zMinStepsSec / zMAccelStepsSec2
            zMAccelMaxTime = zMaxStepsSec / zMAccelStepsSec2
            dbgPrt(txt,"zMAccelMinTime %d zMAccelMaxTime %d", \
                   (zMAccelMinTime, zMAccelMaxTime))
        
            zMAccelMinSteps = int((zMinStepsSec * zMAccelMinTime) / 2.0 + 0.5)
            zMAccelMaxSteps = int((zMaxStepsSec * zMAccelMaxTime) / 2.0 + 0.5)
            dbgPrt(txt,"zMAccelMinSteps %d zMAccelMaxSteps %d", \
                   (zMAccelMinSteps, zMAccelMaxSteps))
        
            zMAccelTime = zMDeltaV / zMAccelStepsSec2
            zMAccelSteps = zMAccelMaxSteps - zMAccelMinSteps
            zMAccelClocks = int(zMAccelTime * fcy)
            dbgPrt(txt,"zMAccelTime %5.3f zMAccelSteps %d zMAccelClocks %d", \
                   (zMAccelTime, zMAccelSteps, zMAccelClocks))
        
            zMAccelDist = float(zMAccelSteps) / zStepsInch
            dbgPrt(txt,"zMAccelDist %5.3f", (zMAccelDist))
        
            cFactorA = (fcy * sqrt(2)) / sqrt(zMAccelStepsSec2)
            cFactorB = zMClocksStep / (sqrt(zMAccelSteps) -
                                       sqrt(zMAccelSteps - 1))
            dbgPrt(txt,"cFactorA %0.2f cFactorB %0.2f", (cFactorA, cFactorB))
            zMCFactor = cFactorB
        
            lastCount = int(zMCFactor * sqrt(zMAccelMinSteps))
            lastTime = float(lastCount) / fcy
        
            f.write("\n")
        
            lastCtr = 0
            step = zMAccelMinSteps
            while step < zMAccelMaxSteps:
                step += 1
                count = int(zMCFactor * sqrt(step))
                ctr = count - lastCount
                time = float(count) / fcy
                delta = time - lastTime
                freq = 1.0 / delta
                ipm = (freq / zStepsInch) * 60
                f.write("step %4d count %9d %7d %7d t %8.6f %8.6f "\
                        "f %7.2f rpm %3.1f\n" % \
                        (step, count, ctr, abs(ctr - lastCtr), time, \
                         delta, freq, ipm))
                lastCount = count
                lastCtr = ctr
                lastTime = time
        
            f.write("\n")
        
            finalCount = int(zMCFactor * (sqrt(zMAccelSteps) - 
                                          sqrt(zMAccelSteps - 1)))
            dbgPrt(txt,"finalCount %d lastCtr %d zMClocksStep %d", \
                   (finalCount, ctr, zMClocksStep))
        
            f.write("\n***\n\n");
        
            while step > zMAccelMinSteps:
                step -= 1
                count = int(zMCFactor * sqrt(step))
                ctr = lastCount - count
                time = float(count) / fcy
                delta = lastTime - time
                freq = 1.0 / delta
                ipm = (freq / zStepsInch) * 60
                f.write("step %4d count %9d %7d %7d t %8.6f %8.6f "\
                        "f %7.2f ipm %3.1f\n" % \
                        (step, count, ctr, abs(ctr - lastCtr), time, \
                         delta, freq, ipm))
                lastCount = count
                lastCtr = ctr
                lastTime = time
        
            lastCount = int(zMCFactor * sqrt(zMAccelMinSteps))
            f.write("\nzMAccelMinSteps %d lastCount %d\n" % \
                    (zMAccelMinSteps, lastCount))
        
            f.close()

n = 1
while True:
    if n >= len(sys.argv):
        break
    tmp = sys.argv[n]
    # if len(tmp) != 0 and tmp[0].isdigit():
    #     break;
    tmp = tmp.lower()
    if tmp == 'xhomed':
        xHomed = True
    else:
        print("invalid argument: %s" % (tmp))
        stdout.flush()
        break
    n += 1

class MainApp(wx.App):
    def OnInit(self):
        """Init Main App."""
        print("mainapp")
        global mainFrame
        mainFrame = self.frame = MainFrame(None, "Lathe Control")
        self.frame.Show(True)
        self.SetTopWindow(self.frame)
        return True

    def FilterEvent(self, evt):
        if evt.EventType == wx.EVT_KEY_DOWN:
            print(evt)
        return(-1)

app = MainApp(redirect=False)
# app.SetCallFilterEvent(True)
# wx.lib.inspection.InspectionTool().Show()
app.MainLoop()

if not (comm.ser is None):
    comm.ser.close()
