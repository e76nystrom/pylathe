#!/cygdrive/c/Python27/Python.exe
#!/usr/bin/python
################################################################################
import wx
import wx.lib.inspection
from time import sleep, time
import sys
from sys import stdout
import serial
from threading import Thread, Lock, Event
from math import radians, cos, tan, ceil, floor, sqrt, atan2, degrees
from Queue import Queue, Empty

HOME_TEST = False
dbg = None

class InfoValue():
    def __init__(self, val):
        self.value = val

    def GetValue(self):
        return(self.value)

    def SetValue(self, val):
        self.value = val

def saveInfo(file):
    global info
    f = open(file, 'w')
    keyList = info.keys()
    keyList.sort()
    for key in keyList:
        val = info[key]
        valClass = val.__class__.__name__
        # print key, valClass
        # stdout.flush()
        if valClass == 'TextCtrl':
            f.write("%s=%s\n" % (key, val.GetValue()))
        elif valClass == 'RadioButton':
            f.write("%s=%s\n" % (key, val.GetValue()))
        elif valClass == 'CheckBox':
            f.write("%s=%s\n" % (key, val.GetValue()))
        elif valClass == 'ComboBox':
            f.write("%s=%s\n" % (key, val.GetValue()))
        elif valClass == 'InfoValue':
            f.write("%s=%s\n" % (key, val.GetValue()))
        elif valClass == 'StaticText':
            pass
    f.close()

def readInfo(file):
    global info
    try:
        f = open(file, 'r')
        for line in f:
            line = line.rstrip()
            if len(line) == 0:
                continue
            [key, val] = line.split('=')
            if key in info:
                func = info[key]
                funcClass = func.__class__.__name__
                # print key, val, funcClass
                if funcClass == 'TextCtrl':
                    func.SetValue(val)
                elif funcClass == 'RadioButton':
                    if val == 'True':
                        func.SetValue(True)
                elif funcClass == 'CheckBox':
                    if val == 'True':
                        func.SetValue(True)
                elif funcClass == 'ComboBox':
                    func.SetValue(val)
            else:
                # print key, val
                func = InfoValue(val)
                info[key] = func
            # stdout.flush()
        f.close()
    except Exception, e:
        print line, "readInfo error"
        print e
        stdout.flush()

configFile = "config.txt"
info = {}
readInfo(configFile)

XILINX = False
try:
    XILINX = info['cfgXilinx'].GetValue() == 'True'
except KeyError as e:
    print("no xilinx info")
    pass
TEPPER_DRIVE = True
try:
    STEPPER_DRIVE = info['spStepDrive'].GetValue() == 'True'
except KeyError as e:
    print("no stepper info")
    pass
stdout.flush()
info = {}                       # clear info

from setup import createCommands, createParameters,\
    createCtlBits, createCtlStates

from comm import SWIG
SWIG = False
import comm
from comm import openSerial, commTimeout, command, getParm, setParm,\
    getString, sendMove, getQueueStatus
comm.SWIG = SWIG

from interface import cmdList, parmList, stateList, regList

if XILINX:
    from setup import createXilinxReg, createXilinxBits
    from comm import setXReg, getXReg, dspXReg
    from interfaceX import xilinxList, xilinxBitList

if SWIG:
    import lathe
    from lathe import taperCalc, T_ACCEL, zTaperInit, xTaperInit, tmp

print sys.version
print wx.version()
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
zEncOffset = 0.0
xEncOffset = 0.0
xHomed = False
done = False

if XILINX:
    cLoc = "../LatheX/include/"
else:
    cLoc = "../Lathe/include/"

fData = False
createCommands(cmdList, cLoc, fData)
createParameters(parmList, cLoc, fData)
createCtlBits(regList, cLoc, fData)
createCtlStates(stateList, cLoc, fData)
if XILINX:
    xLoc = '../../Xilinx/LatheCtl/'
    createXilinxReg(xilinxList, cLoc, xLoc, fData)
    createXilinxBits(xilinxBitList, cLoc, xLoc, fData)

from setup import *

def fieldList(panel, sizer, fields):
    for (label, index) in fields:
        if label.startswith('b'):
            addCheckBox(panel, sizer, label[1:], index)
        else:
            addField(panel, sizer, label, index)

def addFieldText(panel, sizer, label, key):
    global info
    if len(label) != 0:
        txt = wx.StaticText(panel, -1, label)
        sizer.Add(txt, flag=wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL,
                  border=2)
        info[key + 'Text'] = txt

    tc = wx.TextCtrl(panel, -1, "", size=(60, -1))
    sizer.Add(tc, flag=wx.ALL, border=2)
    info[key] = tc
    return(tc)

def addField(panel, sizer, label, key):
    global info
    if len(label) != 0:
        txt = wx.StaticText(panel, -1, label)
        sizer.Add(txt, flag=wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL,
                  border=2)

    tc = wx.TextCtrl(panel, -1, "", size=(60, -1))
    sizer.Add(tc, flag=wx.ALL, border=2)
    if key in info:
        tmp = info[key]
        val = tmp.GetValue()
        tc.SetValue(val)
    info[key] = tc
    return(tc)

def addCheckBox(panel, sizer, label, key):
    global info
    txt = wx.StaticText(panel, -1, label)
    sizer.Add(txt, flag=wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL,
              border=2)

    cb = wx.CheckBox(panel, -1, style=wx.ALIGN_LEFT)
    sizer.Add(cb, flag=wx.ALL|wx.ALIGN_CENTER_VERTICAL, border=2)
    if key in info:
        tmp = info[key]
        val = tmp.GetValue()
        cb.SetValue(val == 'True')
    info[key] = cb
    return(cb)

def getInfo(key):
    global info
    try:
        tmp = info[key]
        return(tmp.GetValue())
    except KeyError:
        return('')

def getBoolInfo(key):
    global info
    try:
        tmp = info[key].GetValue()
        if tmp:
            return(1)
        else:
            return(0)
    except KeyError:
        print("getBoolInfo IndexError %s" % (key))
        stdout.flush()
        return('')

def getFloatInfo(key):
    global info
    try:
        tmp = info[key]
        try:
            return(float(tmp.GetValue()))
        except ValueError:
            pass
    except KeyError:
        print("invalid key %s" % (key))
        stdout.flush()
    return(0.0)

def getIntInfo(key):
    global info
    try:
        tmp = info[key]
        try:
            return(int(tmp.GetValue()))
        except ValueError as e:
            return(0)
    except KeyError as e:
        print("invalid key %s" % (key))
        stdout.flush()
    return(0)

def getFloatVal(tc):
    try:
        return(float(tc.GetValue()))
    except ValueError as e:
        return(0.0)

def getIntVal(tc):
    try:
        return(int(tc.GetValue()))
    except ValueError as e:
        return(0)

moveQue = Queue()

def queMove(op, val):
    moveQue.put((op, val))

def queClear():
    while not moveQue.empty():
        moveQue.get()

def queZSetup(feed):
    moveQue.put((Z_FEED_SETUP, feed))
    saveZOffset();
    saveXOffset();

def queXSetup(feed):
    moveQue.put((X_FEED_SETUP, feed))
    saveZOffset();
    saveXOffset();

def startSpindle(rpm):
    moveQue.put((QUE_START, rpm))
    saveZOffset();
    saveXOffset();

def stopSpindle():
    moveQue.put((QUE_STOP, 0))

def queFeedType(feedType):
    moveQue.put((SAVE_FEED_TYPE, feedType))

def zSynSetup(feed):
    moveQue.put((Z_SYN_SETUP, feed))

def xSynSetup(feed):
    moveQue.put((X_SYN_SETUP, feed))

def nextPass(passNum):
    moveQue.put((PASS_NUM, passNum))

def quePause():
    moveQue.put((QUE_PAUSE, 0))

def saveDiameter(val):
    moveQue.put((SAVE_DIAMETER, val))

def moveZ(zLoc, flag=ZMAX):
    queMove(MOVE_Z | flag << 8, zLoc)
    print("moveZ  %7.4f" % (zLoc))

def moveX(xLoc, flag=XMAX):
    queMove(MOVE_X | flag << 8, xLoc)
    print("moveX  %7.4f" % (xLoc))

def saveZOffset():
    global zHomeOffset
    queMove(SAVE_Z_OFFSET, zHomeOffset)
    print("saveZOffset  %7.4f" % (zHomeOffset))

def saveXOffset():
    global xHomeOffset
    queMove(SAVE_X_OFFSET, xHomeOffset)
    print("savexOffset  %7.4f" % (xHomeOffset))

def moveXZ(zLoc, xLoc):
    queMove(SAVE_Z, zLoc)
    queMove(MOVE_XZ, xLoc)
    print("moveZX %7.4f %7.4f" % (zLoc, xLoc))

def moveZX(zLoc, xLoc):
    queMove(SAVE_X, xLoc)
    queMove(MOVE_ZX, zLoc)
    print("moveXZ %7.4f %7.4f" % (zLoc, xLoc))

def taperZX(zLoc, taper):
    queMove(SAVE_TAPER, taper)
    queMove(TAPER_ZX | (1 << 8), zLoc)
    print("taperZX %7.4f %7.4f" % (zLoc, taper))

def taperXZ(xLoc, taper):
    queMove(SAVE_TAPER, taper)
    queMove(TAPER_XZ, xLoc)
    print("taperZX %7.4f %7.4f" % (xLoc, taper))

def sendClear():
    global spindleDataSent, zDataSent, xDataSent
    command('CLRDBG');
    command('CMD_CLEAR')
    spindleDataSent = False
    zDataSent = False
    xDataSent = False

def xilinxTestMode():
    global info, fcy
    testMode = False
    try:
        testMode = info['cfgTestMode'].GetValue()
    except KeyError as e:
        testMode = False
    if testMode:
        encoder = 0
        try:
            encoder = int(info['cfgEncoder'].GetValue())
        except KeyError as e:
            encoder = 0
        rpm = 0
        try:
            rpm = int(float(info['cfgTestRPM'].GetValue()))
        except KeyError as e:
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
            setParm('ENC_ENABLE', '1')
            setParm('ENC_PRE_SCALER', preScaler)
            setParm('ENC_TIMER', encTimer)
    else:
        setParm('ENC_ENABLE', '0')

def sendSpindleData(send=False, rpm=None):
    global info, spindleDataSent, XILINX
    try:
        if send or (not spindleDataSent):
            setParm('STEPPER_DRIVE', getBoolInfo('spStepDrive'))
            if STEPPER_DRIVE:
                setParm('SP_STEPS', getInfo('spMotorSteps'))
                setParm('SP_MICRO', getInfo('spMicroSteps'))
                setParm('SP_MIN_RPM', getInfo('spMinRPM'))
                if rpm != None:
                    setParm('SP_MAX_RPM', rpm)
                else:
                    setParm('SP_MAX_RPM', getInfo('spMaxRPM'))
                setParm('SP_ACCEL_TIME', getInfo('spAccelTime'))
                setParm('SP_JOG_MIN_RPM', getInfo('spJogMin'))
                setParm('SP_JOG_MAX_RPM', getInfo('spJogMax'))
                setParm('SP_JOG_ACCEL_TIME', getInfo('spAccelTime'))
                setParm('SP_DIR_FLAG', getBoolInfo('spInvDir'))
                setParm('SP_TEST_INDEX', getBoolInfo('spTestIndex'))
                command('CMD_SPSETUP')
            elif XILINX:
                setParm('ENC_MAX', getInfo('cfgEncoder'))
                setParm('X_FREQUENCY', getInfo('cfgXFreq'))
                setParm('FREQ_MULT', getInfo('cfgFreqMult'))
                xilinxTestMode()
                setParm('RPM', getInfo('cfgTestRPM'))
                cfgReg = 0
                if info['cfgInvEncDir'].GetValue():
                    cfgReg |= ENC_POL
                if info['zInvDir'].GetValue():
                    cfgReg |= ZDIR_POL
                if info['xInvDir'].GetValue():
                    cfgReg |= XDIR_POL
                setParm('X_CFG_REG', cfgReg)
            spindleDataSent = True
    except commTimeout as e:
        print("sendSpindleData Timeout")
        stdout.flush()

def sendZData(send=False):
    global zDataSent, jogPanel
    try:
        if send or (not zDataSent):
            pitch = getFloatInfo('zPitch')
            motorSteps = getIntInfo('zMotorSteps')
            microSteps = getIntInfo('zMicroSteps')
            motorRatio = getFloatInfo('zMotorRatio')
            jogPanel.zStepsInch = (microSteps * motorSteps * \
                                   motorRatio) / pitch
            jogPanel.zEncInch = getIntInfo('zEncInch')
            jogPanel.zEncInvert = getBoolInfo('zInvEnc') == 1
            stdout.flush()
            val = jogPanel.combo.GetValue()
            try:
                val = float(val)
                if val > 0.020:
                    val = 0.020
            except ValueError:
                val = 0.001
            setParm('Z_MPG_INC', val * jogPanel.zStepsInch)

            setParm('Z_PITCH', getInfo('zPitch'))
            setParm('Z_RATIO', getInfo('zMotorRatio'))
            setParm('Z_MICRO', getInfo('zMicroSteps'))
            setParm('Z_MOTOR', getInfo('zMotorSteps'))
            setParm('Z_ACCEL', getInfo('zAccel'))
            setParm('Z_BACKLASH', getInfo('zBacklash'))

            setParm('Z_MOVE_MIN', getInfo('zMinSpeed'))
            setParm('Z_MOVE_MAX', getInfo('zMaxSpeed'))

            setParm('Z_JOG_MIN', getInfo('zJogMin'))
            setParm('Z_JOG_MAX', getInfo('zJogMax'))

            setParm('Z_DIR_FLAG', getBoolInfo('zInvDir'))
            setParm('Z_MPG_FLAG', getBoolInfo('zInvMpg'))
                
            command('CMD_ZSETUP')
            zDataSent = True
    except commTimeout as e:
        print("sendZData Timeout")
        stdout.flush()
    except:
        print("setZData exception")
        stdout.flush()

def sendXData(send=False):
    global xDataSent, jogPanel
    try:
        if send or (not xDataSent):
            pitch = getFloatInfo('xPitch')
            motorSteps = getIntInfo('xMotorSteps')
            microSteps = getIntInfo('xMicroSteps')
            motorRatio = getFloatInfo('xMotorRatio')
            jogPanel.xStepsInch = (microSteps * motorSteps * \
                                   motorRatio) / pitch
            jogPanel.xEncInch = getIntInfo('xEncInch')
            jogPanel.xEncInvert = getBoolInfo('xInvEnc') == 1
            val = jogPanel.combo.GetValue()
            try:
                val = float(val)
                if val > 0.020:
                    val = 0.020
            except ValueError:
                val = 0.001
            setParm('X_MPG_INC', val * jogPanel.xStepsInch)

            setParm('X_PITCH', getInfo('xPitch'))
            setParm('X_RATIO', getInfo('xMotorRatio'))
            setParm('X_MICRO', getInfo('xMicroSteps'))
            setParm('X_MOTOR', getInfo('xMotorSteps'))
            setParm('X_ACCEL', getInfo('xAccel'))
            setParm('X_BACKLASH', getInfo('xBacklash'))

            setParm('X_MOVE_MIN', getInfo('xMinSpeed'))
            setParm('X_MOVE_MAX', getInfo('xMaxSpeed'))

            setParm('X_JOG_MIN', getInfo('xJogMin'))
            setParm('X_JOG_MAX', getInfo('xJogMax'))

            setParm('X_DIR_FLAG', getBoolInfo('xInvDir'))
            setParm('X_MPG_FLAG', getBoolInfo('xInvMpg'))

            global HOME_TEST
            if HOME_TEST:
                stepsInch = jogPanel.xStepsInch
                start = str(int(getFloatInfo('xHomeStart') * stepsInch))
                end = str(int(getFloatInfo('xHomeEnd') * stepsInch))
                if end > start:
                    (start, end) = (end, start)
                setParm('X_HOME_START', start)
                setParm('X_HOME_END', end)

            command('CMD_XSETUP')
            xDataSent = True
    except commTimeout as e:
        print("sendZData Timeout")
        stdout.flush()

class UpdatePass():
    def __init__(self, passCount, sPassInt, sPasses, actualFeed, cutAmount):
        self.passes = 0
        self.passInt = 0
        self.sPasses = 0
        self.actualFeed = 0.0
        self.cutAmount = 0.0
        self.calcPass = None
        self.genPass = None

    def setupFeed(self, actualFeed, cutAmount):
        self.actualFeed = actualFeed
        self.cutAmount = cutAmount

    def setupPasses(self, passes, sPassInt, sPasses):
        self.passes = passes
        self.sPassInt = sPassInt
        self.sPasses = sPasses

    def setupAction(self, calcPass, genPass):
        self.calcPass = calcPass
        self.getPass = genPass

    def init(self):
        self.passCount = 0
        self.sPassCtr = 0
        self.spring = 0
        self.feed = 0.0

    def update(self):
        print("pass %d" % (self.passCount))
        if self.passCount < self.passes:
            self.springFlag = False
            if self.sPassInt != 0:
                self.sPassCtr += 1
                if self.sPassCtr > self.sPassInt:
                    self.sPassCtr = 0
                    self.springFlag = True
            if self.springFlag:
                print("spring")
                nextPass(0x100 | self.passCount)
            else:
                self.passCount += 1
                self.feed = self.passCount * self.actualFeed
                nextPass(self.passCount)
                self.calcPass()
            self.genPass(self.feed)
        elif self.passCount == self.passes:
            self.passCount += 1
            nextPass(self.passCount)
            self.feed = self.cutAmount
            self.calcPass()
            self.genPass()
        else:
            if self.springFlag:
                self.springFlag = False
                self.spring += 1
            if self.spring < self.sPasses:
                self.spring += 1
                nextPass(0x200 | self.spring)
                print("spring")
                self.genPass(self.feed)
            else:
                return(False)
        return(True)

class Turn():
    def __init__(self, turnPanel):
        self.turnPanel = turnPanel

    def getTurnParameters(self):
        tu = self.turnPanel
        self.zStart = getFloatVal(tu.zStart)
        self.zEnd = getFloatVal(tu.zEnd)

        self.xStart = getFloatVal(tu.xStart) / 2.0
        self.xEnd = getFloatVal(tu.xEnd) / 2.0
        self.xFeed = abs(getFloatVal(tu.xFeed) / 2.0)
        self.xRetract = abs(getFloatVal(tu.xRetract))

        self.sPassInt = getIntVal(tu.sPInt)
        self.sPasses = getIntVal(tu.spring)

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
        self.passes = int(ceil(self.xCut / abs(self.xFeed)))
        self.turnPanel.passes.SetValue("%d" % (self.passes))
        print ("xCut %5.3f passes %d internal %s" %
               (self.xCut, self.passes, self.internal))

        if self.internal:
            if not self.neg:
                self.xRetract = -self.xRetract
        else:
            if self.neg:
                self.xRetract = -self.xRetract

        self.safeX = self.xStart + self.xRetract

        self.turnSetup()

        self.passCount = 0
        self.sPassCtr = 0
        self.spring = 0

        while self.turnUpdate():
            pass

        moveX(self.xStart + self.xRetract)
        if STEPPER_DRIVE:
            stopSpindle();
        stdout.flush()

    def turnSetup(self):
        quePause()
        if STEPPER_DRIVE:
            startSpindle(getIntInfo('tuRPM'))
            queFeedType(FEED_PITCH)
            zSynSetup(getFloatInfo('tuZFeed'))
        else:
            queZSetup(getFloatInfo('tuZFeed'))
        moveX(self.safeX)
        moveZ(self.zStart)

    def turnUpdate(self):
        if self.passCount < self.passes:
            self.springFlag = False
            if self.sPassInt != 0:
                self.sPassCtr += 1
                if self.sPassCtr > self.sPassInt:
                    self.sPassCtr = 0
                    self.springFlag = True
            if self.springFlag:
                print("spring")
                nextPass(0x100 | self.passCount)
            else:
                self.passCount += 1
                nextPass(self.passCount)
                feed = self.passCount * self.xFeed
                if feed > self.xCut:
                    feed = self.xCut
                self.feed = feed
                self.calculateTurnPass()
            self.turnPass()
        else:
            if self.springFlag:
                self.springFlag = False
                self.spring += 1
            if self.spring < self.sPasses:
                self.spring += 1
                print("spring")
                nextPass(0x200 | self.spring)
                self.turnPass()
            else:
                return(False)
        return(True)

    def calculateTurnPass(self):
        feed = self.feed
        if self.internal:
            if self.neg:
                feed = -feed
        else:
            if not self.neg:
                feed = -feed
        self.curX = self.xStart + feed
        self.safeX = self.curX + self.xRetract
        print ("pass %2d feed %5.3f x %5.3f diameter %5.3f" %
               (self.passCount, feed, self.curX, self.curX * 2.0))

    def turnPass(self):
        moveX(self.curX, XJOG)
        saveDiameter(self.curX * 2.0)
        if self.turnPanel.pause.GetValue():
            print("pause")
            quePause()
        moveZ(self.zEnd, ZSYN)
        moveX(self.safeX)
        moveZ(self.zStart)

    def turnAdd(self):
        if self.feed >= self.xCut:
            add = getFloatVal(self.turnPanel.add)
            self.feed += add
            self.calculateTurnPass()
            self.turnSetup()
            self.turnPass()
            moveX(self.xStart + self.xRetract)
            stopSpindle()
            command('CMD_RESUME')

class TurnPanel(wx.Panel):
    def __init__(self, parent, *args, **kwargs):
        super(TurnPanel, self).__init__(parent, *args, **kwargs)
        self.InitUI()
        self.turn = Turn(self)

    def InitUI(self):
        global hdrFont
        self.sizerV = sizerV = wx.BoxSizer(wx.VERTICAL)

        txt = wx.StaticText(self, -1, "Turn")
        txt.SetFont(hdrFont)

        sizerV.Add(txt, flag=wx.CENTER|wx.ALL, border=2)

        sizerG = wx.GridSizer(8, 0, 0)

        # z parameters

        self.zStart = addField(self, sizerG, "Z Start", "tuZStart")

        self.zEnd = addField(self, sizerG, "Z End", "tuZEnd")
        
        self.zFeed = addField(self, sizerG, "Z Feed", "tuZFeed")

        sizerG.Add(wx.StaticText(self, -1), border=2)
        sizerG.Add(wx.StaticText(self, -1), border=2)

        # x parameters

        self.xStart = addField(self, sizerG, "X Start D", "tuXStart")

        self.xEnd = addField(self, sizerG, "X End D", "tuXEnd")

        self.xFeed = addField(self, sizerG, "X Feed D", "tuXFeed")

        self.xRetract = addField(self, sizerG, "X Retract", "tuXRetract")
        
        # pass info

        self.passes = addField(self, sizerG, "Passes", "tuPasses")
        self.passes.SetEditable(False)

        self.sPInt = addField(self, sizerG, "SP Int", "tuSPInt")

        self.spring = addField(self, sizerG, "Spring", "tuSpring")

        sizerG.Add(emptyCell)
        sizerG.Add(emptyCell)

        # buttons

        btn = wx.Button(self, label='Send', size=(60,-1))
        btn.Bind(wx.EVT_BUTTON, self.OnSend)
        sizerG.Add(btn, flag=wx.CENTER|wx.ALL, border=2)

        btn = wx.Button(self, label='Start', size=(60,-1))
        btn.Bind(wx.EVT_BUTTON, self.OnStart)
        sizerG.Add(btn, flag=wx.CENTER|wx.ALL, border=2)

        # sizerG.Add(wx.StaticText(self, -1), border=2)

        btn = wx.Button(self, label='Add', size=(60,-1))
        btn.Bind(wx.EVT_BUTTON, self.OnAdd)
        sizerG.Add(btn, flag=wx.CENTER|wx.ALL, border=2)

        self.add = addField(self, sizerG, "", "tuAddFeed")

        self.rpm = addField(self, sizerG, "RPM", "tuRPM")

        sizerG.Add(wx.StaticText(self, -1, "Pause"), border=2,
                   flag=wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.ALL)
        self.pause = cb = wx.CheckBox(self, -1,
                                         style=wx.ALIGN_LEFT)
        sizerG.Add(cb, flag=wx.ALIGN_CENTER_VERTICAL|wx.ALL, border=2)
        info['tuPause'] = cb
        
        sizerV.Add(sizerG, flag=wx.LEFT|wx.ALL, border=2)

        self.SetSizer(sizerV)
        self.sizerV.Fit(self)

    def update(self):
        pass

    def sendData(self):
        try:
            queClear()
            sendClear()

            sendSpindleData()
            sendZData()
            sendXData()

        except commTimeout as e:
            print("timeout error")
            stdout.flush()

    def OnSend(self, e):
        global xHomed, jogPanel
        if xHomed:
            self.sendData()
            self.turn.turn()
        jogPanel.focus()

    def OnStart(self, e):
        global dbg, jogPanel
        command('CMD_RESUME')
        dbg = open('dbg.txt', 'w')
        jogPanel.focus()
    
    def OnAdd(self, e):
        global jogPanel
        self.turn.turnAdd()
        passes = getParm('TOTAL_PASSES')
        self.passes.SetLabel("%d" % (passes))
        jogPanel.focus()

class Face():
    def __init__(self, facePanel):
        self.facePanel = facePanel

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

        self.sPassInt = getIntVal(fa.sPInt)
        self.sPasses = getIntVal(fa.spring)

    def face(self):
        self.getFaceParameters()

        self.internal = self.xStart < self.xEnd
        self.zCut = abs(self.zStart - self.zEnd)
        self.passes = int(ceil(self.zCut / self.zFeed))
        self.facePanel.passes.SetValue("%d" % (self.passes))
        print ("zCut %5.3f passes %d internal %s" %
               (self.zCut, self.passes, self.internal))

        if self.internal:
            self.xRetract = -self.xRetract
        self.safeX = self.xStart + self.xRetract
        self.safeZ = self.zStart + self.zRetract

        self.faceSetup()

        self.passCount = 0
        self.sPassCtr = 0
        self.spring = 0

        while self.faceUpdate():
            pass

        moveX(self.safeX)
        moveZ(self.zStart + self.zRetract)

        stopSpindle()
        stdout.flush()

    def faceSetup(self):
        quePause()
        if STEPPER_DRIVE:
            startSpindle(getIntInfo('faRPM'))
            queFeedType(FEED_PITCH)
            xSynSetup(getFloatInfo('faXFeed'))
        else:
            queXSetup(getFloatInfo('faxFeed'))
        moveX(self.safeX)
        moveZ(self.zStart)
        moveX(self.xStart)

    def faceUpdate(self):
        if self.passCount < self.passes:
            self.springFlag = False
            if self.sPassInt != 0:
                self.sPassCtr += 1
                if self.sPassCtr > self.sPassInt:
                    self.sPassCtr = 0
                    self.springFlag = True
            if self.springFlag:
                print("spring")
                nextPass(0x100 | self.passCount)
            else:
                self.passCount += 1
                nextPass(self.passCount)
                feed = self.passCount * self.zFeed
                if feed > self.zCut:
                    feed = self.zCut
                self.feed = feed
                self.calculateFacePass()
            self.facePass()
        else:
            if self.springFlag:
                self.springFlag = False
                self.spring += 1
            if self.spring < self.sPasses:
                self.spring += 1
                nextPass(0x200 | self.spring)
                print("spring")
                self.facePass()
            else:
                return(False)
        return(True)

    def calculateFacePass(self):
        feed = self.feed
        if self.internal:
            feed = -feed
        self.curZ = self.zStart - feed
        self.safeZ = self.curZ + self.zRetract
        print ("pass %2d feed %5.3f z %5.3f" %
               (self.passCount, feed, self.curZ))

    def facePass(self):
        moveZ(self.curZ, XJOG)
        if self.facePanel.pause.GetValue():
            print("pause")
            quePause()
        moveX(self.xEnd, ZSYN)
        moveZ(self.safeZ)
        moveX(self.xStart)

    def faceAdd(self):
        if self.feed >= self.zCut:
            add = getFloatVal(self.facePanel.add)
            self.feed += add
            self.faceSetup()
            self.calculateFacePass()
            self.facePass()
            moveX(self.safeX)
            moveZ(self.zStart + self.zRetract)
            stopSpindle()
            command('CMD_RESUME')

class FacePanel(wx.Panel):
    def __init__(self, parent, *args, **kwargs):
        super(FacePanel, self).__init__(parent, *args, **kwargs)
        self.InitUI()
        self.face = Face(self)

    def InitUI(self):
        global hdrFont, emptyCell
        self.sizerV = sizerV = wx.BoxSizer(wx.VERTICAL)

        txt = wx.StaticText(self, -1, "Face")
        txt.SetFont(hdrFont)

        sizerV.Add(txt, flag=wx.CENTER|wx.ALL, border=2)

        # x parameters

        sizerG = wx.GridSizer(8, 0, 0)

        self.xStart = addField(self, sizerG, "X Start D", "faXStart")

        self.xEnd = addField(self, sizerG, "X End D", "faXEnd")
        
        self.xFeed = addField(self, sizerG, "X Feed", "faXFeed")
        
        self.xRetract = addField(self, sizerG, "X Retract", "faXRetract")

        # z parameters

        self.zStart = addField(self, sizerG, "Z Start", "faZStart")

        self.zEnd = addField(self, sizerG, "Z End", "faZEnd")

        self.zFeed = addField(self, sizerG, "Z Feed", "faZFeed")

        self.zRetract = addField(self, sizerG, "Z Retract", "faZRetract")
        
        # pass info

        self.passes = addField(self, sizerG, "Passes", "faPasses")
        self.passes.SetEditable(False)

        self.sPInt = addField(self, sizerG, "SP Int", "faSPInt")

        self.spring = addField(self, sizerG, "Spring", "faSpring")

        sizerG.Add(emptyCell)
        sizerG.Add(emptyCell)

        # buttons

        btn = wx.Button(self, label='Send', size=(60,-1))
        btn.Bind(wx.EVT_BUTTON, self.OnSend)
        sizerG.Add(btn, flag=wx.CENTER|wx.ALL, border=2)

        btn = wx.Button(self, label='Start', size=(60,-1))
        btn.Bind(wx.EVT_BUTTON, self.OnStart)
        sizerG.Add(btn, flag=wx.CENTER|wx.ALL, border=2)

        # sizerG.Add(wx.StaticText(self, -1), border=2)

        btn = wx.Button(self, label='Add', size=(60,-1))
        btn.Bind(wx.EVT_BUTTON, self.OnAdd)
        sizerG.Add(btn, flag=wx.CENTER|wx.ALL, border=2)

        self.add = addField(self, sizerG, "", "faAddFeed")

        self.rpm = addField(self, sizerG, "RPM", "faRPM")

        sizerG.Add(wx.StaticText(self, -1, "Pause"), border=2,
                   flag=wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.ALL)
        self.pause = cb = wx.CheckBox(self, -1,
                                         style=wx.ALIGN_LEFT)
        sizerG.Add(cb, flag=wx.ALIGN_CENTER_VERTICAL|wx.ALL, border=2)
        info['fdPause'] = cb

        sizerV.Add(sizerG, flag=wx.LEFT|wx.ALL, border=2)

        self.SetSizer(sizerV)
        self.sizerV.Fit(self)

    def update(self):
        pass

    def sendData(self):
        try:
            queClear()
            sendClear()
            sendSpindleData()
            sendZData()
            sendXData()

        except commTimeout as e:
            print("timeout error")
            stdout.flush()

    def OnSend(self, e):
        global xHomed, jogPanel
        if xHomed:
            self.sendData()
            self.face.face()
        jogPanel.focus()

    def OnStart(self, e):
        global jogPanel
        command('CMD_RESUME')
        jogPanel.focus()
    
    def OnAdd(self, e):
        global jogPanel
        self.face.faceAdd()
        jogPanel.focus()

class Cutoff():
    def __init__(self, cutoffPanel):
        self.cutoffPanel = cutoffPanel

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

        self.cutoffSetup()

        if self.cutoffPanel.pause.GetValue():
            print("pause")
            quePause()
        moveX(self.xEnd, ZSYN)
        moveX(self.safeX)
        moveZ(self.zStart)

        stopSpindle()
        stdout.flush()

    def cutoffSetup(self):
        quePause()
        if STEPPER_DRIVE:
            startSpindle(getIntInfo('cuRPM'))
            queFeedType(FEED_PITCH)
            xSynSetup(getFloatInfo('cuXFeed'))
        else:
            queXSetup(getFloatInfo('cuxFeed'))
        moveX(self.safeX)
        moveZ(self.zCutoff)
        moveX(self.xStart)

class CutoffPanel(wx.Panel):
    def __init__(self, parent, *args, **kwargs):
        super(CutoffPanel, self).__init__(parent, *args, **kwargs)
        self.InitUI()
        self.cutoff = Cutoff(self)

    def InitUI(self):
        global hdrFont, emptyCell
        self.sizerV = sizerV = wx.BoxSizer(wx.VERTICAL)

        txt = wx.StaticText(self, -1, "Cutoff")
        txt.SetFont(hdrFont)

        sizerV.Add(txt, flag=wx.CENTER|wx.ALL, border=2)

        # x parameters

        sizerG = wx.GridSizer(8, 0, 0)

        self.xStart = addField(self, sizerG, "X Start D", "cuXStart")

        self.xEnd = addField(self, sizerG, "X End D", "cuXEnd")
        
        self.xFeed = addField(self, sizerG, "X Feed", "cuXFeed")
        
        self.xRetract = addField(self, sizerG, "X Retract", "cuXRetract")

        # z parameters

        self.zStart = addField(self, sizerG, "Z Start", "cuZStart")

        self.zCutoff = addField(self, sizerG, "Z Cutoff", "cuZCutoff")

        sizerG.Add(emptyCell)
        sizerG.Add(emptyCell)
        sizerG.Add(emptyCell)
        sizerG.Add(emptyCell)
        
        # buttons

        btn = wx.Button(self, label='Send', size=(60,-1))
        btn.Bind(wx.EVT_BUTTON, self.OnSend)
        sizerG.Add(btn, flag=wx.CENTER|wx.ALL, border=2)

        btn = wx.Button(self, label='Start', size=(60,-1))
        btn.Bind(wx.EVT_BUTTON, self.OnStart)
        sizerG.Add(btn, flag=wx.CENTER|wx.ALL, border=2)

        sizerG.Add(emptyCell)
        sizerG.Add(emptyCell)

        self.rpm = addField(self, sizerG, "RPM", "cuRPM")

        sizerG.Add(wx.StaticText(self, -1, "Pause"), border=2,
                   flag=wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.ALL)
        self.pause = cb = wx.CheckBox(self, -1,
                                         style=wx.ALIGN_LEFT)
        sizerG.Add(cb, flag=wx.ALIGN_CENTER_VERTICAL|wx.ALL, border=2)
        info['cuPause'] = cb

        sizerV.Add(sizerG, flag=wx.LEFT|wx.ALL, border=2)

        self.SetSizer(sizerV)
        self.sizerV.Fit(self)

    def update(self):
        pass

    def sendData(self):
        try:
            queClear()
            sendClear()
            sendSpindleData()
            sendZData()
            sendXData()
        except commTimeout as e:
            print("timeout error")
            stdout.flush()

    def OnSend(self, e):
        global xHomed, jogPanel
        if xHomed:
            self.sendData()
            self.cutoff.cutoff()
        jogPanel.focus()

    def OnStart(self, e):
        global jogPanel
        command('CMD_RESUME')
        jogPanel.focus()

class Taper():
    def __init__(self, taperPanel):
        self.taperPanel = taperPanel
        # morse #3 taper
        # taper = 0.0502
        # length = 3.190
        # largeEnd = .938
        # smallEnd = .778
    
    def getTaperParameters(self, taperInch):
        tp = self.taperPanel
        self.taperX = taperInch <= 1.0
        self.taper = taperInch
        self.zSafe = abs(getFloatVal(tp.zSafe))
        self.zStart = getFloatVal(tp.zStart)
        self.zLength = abs(getFloatVal(tp.zLength))
        self.zFeed = abs(getFloatVal(tp.zFeed))

        self.stockDiameter = getFloatVal(tp.stockDiam)
        self.refDiameter = getFloatVal(tp.diam)
        self.xFinal = abs(getFloatVal(tp.xFinal))
        self.retract = abs(getFloatVal(tp.xRetract))

        self.feedPass = getFloatVal(tp.xFeed) / 2.0
        self.finishPass = getFloatVal(tp.xFinal)

        self.sPassInt = getIntVal(tp.sPInt)
        self.sPasses = getIntVal(tp.spring)

        totalTaper = taperInch * self.zLength
        taperInch = totalTaper / self.zLength
        print ("totalTaper %5.3f taperInch %6.4f" %
               (totalTaper, taperInch))

    def externalTaper(self, taperInch):
        print("externalTaper")
        self.getTaperParameters(taperInch)

        self.xStart = self.stockDiameter / 2.0
        self.xEnd = self.refDiameter / 2.0

        if self.taperX:
            self.cutAmount = self.xStart - self.xEnd

            self.startZ = 0.0
            self.endZ = self.startZ
            self.safeZ = self.startZ + self.zSafe
            self.endX = 0.0
            self.safeX = self.xStart + self.retract
        else:
            self.cutAmount = self.zLength

        cutToFinish = self.cutAmount - self.finishPass
        self.passes = int(ceil(cutToFinish / self.zFeed))
        self.taperPanel.passes.SetValue("%d" % (self.passes + 1))
        self.actualFeed = cutToFinish / self.passes
        print ("passes %d cutAmount %5.3f feed %6.3f" %
               (self.passes, self.cutAmount, self.actualFeed))
        self.passCount = 0
        self.sPassCtr = 0
        self.spring = 0

        self.taperSetup()

        while self.externalTaperUpdate():
            pass

        moveX(self.safeX)
        moveZ(self.startZ)
        stopSpindle();
        stdout.flush()

    def taperSetup(self):
        quePause()
        startSpindle(getIntInfo('tpRPM'))
        queFeedType(FEED_PITCH)
        zSynSetup(getFloatInfo('tpZFeed'))
        xSynSetup(getFloatInfo('tpXFeed'))
        moveX(self.safeX)

    def externalTaperUpdate(self):
        print("pass %d" % (self.passCount))
        if self.passCount < self.passes:
            self.springFlag = False
            if self.sPassInt != 0:
                self.sPassCtr += 1
                if self.sPassCtr > self.sPassInt:
                    self.sPassCtr = 0
                    self.springFlag = True
            if self.springFlag:
                print("spring")
                nextPass(0x100 | self.passCount)
            else:
                self.passCount += 1
                self.feed = self.passCount * self.actualFeed
                nextPass(self.passCount)
                self.calcExternalPass()
            self.externalPass()
        elif self.passCount == self.passes:
            self.passCount += 1
            nextPass(self.passCount)
            self.feed = self.cutAmount
            self.calcExternalPass()
            self.externalPass()
        else:
            if self.springFlag:
                self.springFlag = False
                self.spring += 1
            if self.spring < self.sPasses:
                self.spring += 1
                nextPass(0x200 | self.spring)
                print("spring")
                self.externalPass()
            else:
                return(False)
        return(True)

    def calcExternalPass(self):
        if self.taperX:
            self.endX = self.startX - self.feed
            taperLength = self.feed / self.taper
            if taperLength < self.zLength:
                self.startZ = taperLength
                self.startX = self.xStart
            else:
                self.startZ = self.zLength
                self.startX = self.endX + self.taper * self.zLength
            self.startZ = -self.startZ
        else:
            self.startZ = self.zStart - self.feed
            self.startX = self.xStart
            self.endZ = self.zStart
            taperLength = self.feed * self.taper
            if taperLength < self.xLength:
                self.endX = self.xStart -taperLength
            else:
                self.endX = self.xEnd
        print ("%2d start (%6.3f,%6.3f) end (%6.3f %6.3f) "\
               "%6.3f %6.3f" %
               (self.passCount, self.startZ, self.startX, 
                self.endZ, self.endX, 2.0 * self.startX, 2.0 * self.endX))

    def externalPass(self):
        moveZ(self.startZ)
        if self.taperPanel.pause.GetValue():
            print("pause")
            quePause()
        if self.taperX:
            moveX(self.startX, XSYN)
            taperZX(self.endZ, self.taper)
        else:
            moveX(self.startX)
            taperXZ(self.endZ, self.taper)
            pass
        moveX(self.safeX)

    def externalAdd(self):
        if self.feed >= self.cutAmount:
            add = getFloatVal(self.taperPanel.add) / 2
            self.feed += add
            self.taperSetup()
            self.calcExternalPass()
            self.externalPass()
            moveX(self.safeX)
            moveZ(self.startZ)
            stopSpindle();
            command('CMD_RESUME')

    def internalTaper(self, taperInch):
        print("internalTaper")
        self.getTaperParameters(taperInch)

        self.boreRadius = self.stockDiameter / 2.0
        largeRadius = self.refDiameter / 2.0
        self.cutAmount = largeRadius - self.boreRadius
        cutToFinish = self.cutAmount - self.finishPass
        self.passes = int(ceil(cutToFinish / self.feedPass))
        self.taperPanel.passes.SetValue("%d" % (self.passes + 1))
        self.actualFeed = cutToFinish / self.passes
        print ("passes %d cutAmount %5.3f feed %6.3f" %
               (self.passes, self.cutAmount, self.actualFeed))

        self.startZ = 0.0
        self.endZ = 0.0
        self.safeX = self.boreRadius - self.retract
        self.safeZ = self.retract
        self.passCount = 0
        self.sPassCtr = 0
        self.spring = 0

        self.taperSetup()
        moveZ(self.safeZ)

        while self.internalTaperUpdate():
            pass

        moveX(self.safeX)
        moveZ(self.safeZ)
        stopSpindle();
        stdout.flush()

    def internalTaperUpdate(self):
        if self.passCount < self.passes:
            self.springFlag = False
            if self.sPassInt != 0:
                self.sPassCtr += 1
                if self.sPassCtr > self.sPassInt:
                    self.sPassCtr = 0
                    self.springFlag = True
            if self.springFlag:
                print("spring")
                nextPass(0x100 | self.passCount)
            else:
                self.passCount += 1
                nextPass(self.passCount)
                self.feed = self.passCount * self.actualFeed
                self.calcInternalPass()
            self.internalPass()
        elif self.passCount == self.passes:
            self.passCount += 1
            nextPass(self.passCount)
            self.feed = self.cutAmount
            self.calcInternalPass()
            self.internalPass()
        else:
            if self.springFlag:
                self.springFlag = False
                self.spring += 1
            if self.spring < self.sPasses:
                self.spring += 1
                nextPass(0x200 | self.spring)
                print("spring")
                self.internalPass()
            else:
                return(False)
        return(True)

    def calcInternalPass(self):
        self.startX = self.boreRadius + self.feed
        self.endZ = self.feed / self.taper
        print("endZ %6.3f" % (self.endZ))
        if self.endZ <= self.zLength:
            self.endX = self.boreRadius
        else:
            self.endZ = self.zLength
            self.endX = (self.boreRadius + self.feed - 
                         self.zLength * self.taper)
        self.endZ = -self.endZ
        print ("%2d feed %6.3f start (%6.3f,%6.3f) end (%6.3f %6.3f) "\
                "%6.3f %6.3f" %
                (self.passCount, self.feed, self.startX, self.startZ, 
                self.endX, self.endZ,
                2.0 * self.startX, 2.0 * self.endX))

    def internalPass(self):
        moveX(self.startX + 0.002, XJOG)
        moveX(self.startX, XJOG)
        moveZ(self.startZ, XJOG)
        if self.taperPanel.pause.GetValue():
            print("pause")
            quePause()
        taperZX(self.endZ, self.taper)
        moveX(self.boreRadius, XSYN)
        moveX(self.safeX)
        moveZ(self.safeZ)

    def internalAdd(self):
        if self.feed >= self.cutAmount:
            add = getFloatVal(self.taperPanel.add) / 2
            self.feed += add
            self.passCount += 1
            self.taperSetup()
            moveZ(self.safeZ)
            self.calcInternalPass()
            self.internalPass()
            moveX(self.safeX)
            moveZ(self.safeZ)
            stopSpindle();
            command('CMD_RESUME')
            stdout.flush()

class TaperPanel(wx.Panel):
    def __init__(self, parent, *args, **kwargs):
        super(TaperPanel, self).__init__(parent, *args, **kwargs)
        self.InitUI()
        self.taper = Taper(self)

    def InitUI(self):
        global hdrFont, info
        self.sizerV = sizerV = wx.BoxSizer(wx.VERTICAL)

        txt = wx.StaticText(self, -1, "Taper")
        txt.SetFont(hdrFont)

        sizerV.Add(txt, flag=wx.CENTER|wx.ALL, border=2)

        sizerG = wx.GridSizer(8, 0, 0)

        # z parameters

        self.zSafe = addField(self, sizerG, "Z Safe", "tpZSafe")

        self.zStart = addField(self, sizerG, "Z Start", "tpZStart")

        self.zLength = addField(self, sizerG, "Z Length", "tpZLength")
        
        self.zFeed = addField(self, sizerG, "Z Feed", "tpZFeed")
        
        # x parameters

        self.stockDiam = addFieldText(self, sizerG, "Stock Diam",
                                      "tpStockDiam")

        self.diam = addFieldText(self, sizerG, "Small Diam", "tpDiam")

        self.xFeed = addField(self, sizerG, "X Feed D", "tpXFeed")

        self.xRetract = addField(self, sizerG, "X Retract", "tpXRetract")
        
        # taper parameters

        self.deltaBtn = btn = wx.RadioButton(self, label="Z")
        sizerG.Add(btn, flag=wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.ALL,
                   border=2)
        btn.Bind(wx.EVT_RADIOBUTTON, self.OnDelta)
        info['tpDeltaBtn'] = btn

        self.zDelta = addField(self, sizerG, "", "tpZDelta")
        self.zDelta.Bind(wx.EVT_KILL_FOCUS, self.OnDeltaFocus)
        self.xDelta = addField(self, sizerG, "X", "tpXDelta")
        self.xDelta.Bind(wx.EVT_KILL_FOCUS, self.OnDeltaFocus)

        self.angleBtn = btn = wx.RadioButton(self, label="Angle")
        sizerG.Add(btn, flag=wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.ALL,
                   border=2)
        btn.Bind(wx.EVT_RADIOBUTTON, self.OnAngle)
        info['tpAngleBtn'] = btn

        self.angle = addField(self, sizerG, "", "tpAngle")
        self.angle.Bind(wx.EVT_KILL_FOCUS, self.OnAngleFocus)

        sizerG.Add(wx.StaticText(self, -1, "Internal"), border=2,
                   flag=wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.ALL)
        self.internal = cb = wx.CheckBox(self, -1,
                                         style=wx.ALIGN_LEFT)
        self.Bind(wx.EVT_CHECKBOX, self.OnInternal, cb)
        sizerG.Add(cb, flag=wx.ALIGN_CENTER_VERTICAL|wx.ALL, border=2)
        info['tpInternal'] = cb

        # pass info

        self.passes = addField(self, sizerG, "Passes", "tpPasses")
        self.passes.SetEditable(False)

        self.sPInt = addField(self, sizerG, "SP Int", "tpSPInt")

        self.spring = addField(self, sizerG, "Spring", "tpSpring")

        self.xFinal = addField(self, sizerG, "X Final", "tpXFinal")

        # control buttons

        btn = wx.Button(self, label='Send', size=(60,-1))
        btn.Bind(wx.EVT_BUTTON, self.OnSend)
        sizerG.Add(btn, flag=wx.CENTER|wx.ALL, border=2)

        btn = wx.Button(self, label='Start', size=(60,-1))
        btn.Bind(wx.EVT_BUTTON, self.OnStart)
        sizerG.Add(btn, flag=wx.CENTER|wx.ALL, border=2)

        # sizerG.Add(wx.StaticText(self, -1), border=2)

        btn = wx.Button(self, label='Add', size=(60,-1))
        btn.Bind(wx.EVT_BUTTON, self.OnAdd)
        sizerG.Add(btn, flag=wx.CENTER|wx.ALL, border=2)

        self.add = addField(self, sizerG, "", "tpAddFeed")

        self.rpm = addField(self, sizerG, "RPM", "tpRPM")

        sizerG.Add(wx.StaticText(self, -1, "Pause"), border=2,
                   flag=wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.ALL)
        self.pause = cb = wx.CheckBox(self, -1,
                                         style=wx.ALIGN_LEFT)
        sizerG.Add(cb, flag=wx.ALIGN_CENTER_VERTICAL|wx.ALL, border=2)
        info['tpPause'] = cb

        # sizerG.Add(wx.StaticText(self, -1), border=2)

        # btn = wx.Button(self, label='Debug', size=(60,-1))
        # btn.Bind(wx.EVT_BUTTON, self.OnDebug)
        # sizerG.Add(btn, flag=wx.CENTER|wx.ALL, border=2)

        sizerV.Add(sizerG, flag=wx.LEFT|wx.ALL, border=2)

        self.SetSizer(sizerV)
        sizerV.Fit(self)

    def update(self):
        self.updateUI()
        self.updateDelta()
        self.updateAngle()

    def updateUI(self):
        global info
        val = self.deltaBtn.GetValue()
        self.zDelta.SetEditable(val)
        self.xDelta.SetEditable(val)
        self.angle.SetEditable(not val)
        if self.internal.GetValue():
            info['tpStockDiamText'].SetLabel("Bore Diam")
            info['tpDiamText'].SetLabel("Large Diam")
        else:
            info['tpStockDiamText'].SetLabel("Stock Diam")
            info['tpDiamText'].SetLabel("Small Diam")
        self.sizerV.Layout()

    def updateAngle(self):
        if self.angleBtn.GetValue():
            try:
                angle = getFloatVal(self.angle)
                deltaX = tan(radians(angle))
                self.zDelta.ChangeValue("1.000")
                self.xDelta.ChangeValue("%0.5f" % (deltaX))
            except ValueError as e:
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
        try:
            queClear()
            sendClear()
            sendSpindleData()
            sendZData()
            sendXData()

        except commTimeout as e:
            print("timeout error")
            stdout.flush()

    def OnSend(self, e):
        global xHomed, jogPanel
        if xHomed:
            self.sendData()
            taper = getFloatVal(self.xDelta) / getFloatVal(self.zDelta)
            if self.internal.GetValue():
                self.taper.internalTaper(taper)
            else:
                self.taper.externalTaper(taper)
        jogPanel.focus()

    def OnStart(self, e):
        global jogPanel
        command('CMD_RESUME')
        jogPanel.focus()
    
    def OnAdd(self, e):
        global jogPanel
        if self.internal.GetValue():
            self.taper.internalAdd()
        else:
            self.taper.externalAdd()

        passes = getParm('TOTAL_PASSES')
        self.passes.SetLabel("%d" % (passes))
        jogPanel.focus()

    # def OnDebug(self, e):
    #     self.sendData()
    #     moveX(1.000)
    #     moveZ(0.010)
    #     taperZX(-0.25, 0.0251)

class ScrewThread():
    def __init__(self, threadPanel):
        self.threadPanel = threadPanel

    def getThreadParameters(self):
        th = self.threadPanel
        self.internal = th.internal.GetValue()

        self.zStart = getFloatVal(th.zStart)
        self.zEnd = getFloatVal(th.zEnd)
        self.zAccel = 0.0
        self.zBackInc = 0.003

        self.xScale = 16000

        if th.tpi.GetValue():
            self.tpi = getFloatVal(th.thread)
            self.pitch = 1.0 / self.tpi
        else:
            self.pitch = getFloatVal(th.thread) / 25.4
            self.tpi = 1.0 / self.pitch
        
        self.xStart = getFloatVal(th.xStart) / 2.0

        self.lastFeed = getFloatVal(th.lastFeed)
        self.depth = getFloatVal(th.depth)
        
        self.xRetract = getFloatVal(th.xRetract)
        
        self.hFactor = getFloatVal(th.hFactor)
        self.angle = radians(getFloatVal(th.angle))

        self.sPassInt = getIntVal(th.sPInt)
        self.sPasses = getIntVal(th.spring)

    def thread(self):
        self.getThreadParameters()

        cosAngle = cos(self.angle)
        self.tanAngle = tan(self.angle)
        print ("tpi %4.1f pitch %5.3f hFactor %5.3f lastFeed %6.4f" %
               (self.tpi, self.pitch, self.hFactor, self.lastFeed))
        
        if self.depth == 0:
            self.depth = (cosAngle * self.pitch) * self.hFactor
        
        actualWidth = 2 * self.depth * self.tanAngle
        print ("depth %6.4f actualWdith %6.4f" %
               (self.depth, actualWidth))
        
        area = 0.5 * self.depth * actualWidth
        lastDepth = self.depth - self.lastFeed
        lastArea = (lastDepth * lastDepth) * self.tanAngle
        self.areaPass = area - lastArea
        print ("area %8.6f lastDepth %6.4f lastArea %8.6f areaPass %8.6f" % 
               (area, lastDepth, lastArea, self.areaPass))
        self.passes = int(ceil(area / self.areaPass))
        self.threadPanel.passes.SetValue("%d" % (self.passes))
        self.areaPass = area / self.passes
        print ("passes %d areaPass %8.6f" %
               (self.passes, self.areaPass))
        
        if self.internal:
            self.xRetract = -self.xRetract
        
        self.safeX = self.xStart + self.xRetract
        self.startZ = self.zStart + self.zAccel

        self.threadSetup()

        self.curArea = 0.0
        self.prevFeed = 0.0
        self.passCount = 0
        self.sPassCtr = 0
        self.spring = 0
        print("pass     area  xfeed  zfeed  delta")

        while self.threadUpdate():
            pass

        stopSpindle();
        stdout.flush()

    def threadSetup(self):
        quePause()
        startSpindle(getIntInfo('thRPM'))
        feedType = FEED_TPI
        if self.threadPanel.mm.GetValue():
            feedType = FEED_METRIC
        queFeedType(feedType)
        zSynSetup(getFloatInfo('thPitch'))
        moveX(self.safeX)
        moveZ(self.startZ + self.zBackInc)
        moveZ(self.startZ)

    def threadUpdate(self):
        if self.passCount < self.passes:
            self.springFlag = False
            if self.sPassInt != 0:
                self.sPassCtr += 1
                if self.sPassCtr > self.sPassInt:
                    self.sPassCtr = 0
                    self.springFlag = True
            if self.springFlag:
                print("spring")
                nextPass(0x100 | self.passCount)
            else:
                self.passCount += 1
                nextPass(self.passCount)
                self.curArea += self.areaPass
                self.feed = sqrt(self.curArea / self.tanAngle)
                self.calculateThread()
            self.threadPass()
        else:
            if self.springFlag:
                self.springFlag = False
                self.spring += 1
            if self.spring < self.sPasses:
                self.spring += 1
                nextPass(0x200 | self.spring)
                print("spring")
                self.threadPass()
            else:
                return(False)
        return(True)

    def calculateThread(self):
        feed = self.feed
        self.zOffset = feed * self.tanAngle
        print ("%4d %8.6f %6.4f %6.4f %6.4f" % 
               (self.passCount, self.curArea, feed, self.zOffset,
                feed - self.prevFeed))
        self.prevFeed = feed
        if self.internal:
            feed = -feed
        self.curX = self.xStart - feed

    def threadPass(self):
        moveX(self.curX, XJOG)
        if self.threadPanel.pause.GetValue():
            print("pause")
            quePause()
        moveZ(self.zEnd, ZSYN | Z_SYN_START)
        moveX(self.safeX)
        startZ = self.startZ - self.zOffset
        moveZ(startZ + self.zBackInc)
        moveZ(startZ)

    def threadAdd(self):
        if self.feed >= self.depth:
            add = getFloatVal(self.threadPanel.add)
            self.feed += add
            self.threadSetup()
            self.calculateThread()
            self.threadPass()
            stopSpindle();
            command('CMD_RESUME')
            stdout.flush()

class ThreadPanel(wx.Panel):
    def __init__(self, parent, *args, **kwargs):
        super(ThreadPanel, self).__init__(parent, *args, **kwargs)
        self.InitUI()
        self.screwThread = ScrewThread(self)

    def InitUI(self):
        global hdrFont, info, emptyCell
        self.sizerV = sizerV = wx.BoxSizer(wx.VERTICAL)

        txt = wx.StaticText(self, -1, "Thread")
        txt.SetFont(hdrFont)

        sizerV.Add(txt, flag=wx.CENTER|wx.ALL, border=2)

        # z parameters

        sizerG = wx.GridSizer(8, 0, 0)

        self.zStart = addField(self, sizerG, "Z Start", "thZStart")

        self.zEnd = addField(self, sizerG, "Z End", "thZEnd")
        
        self.thread = addField(self, sizerG, "Thread", "thPitch")
        
        self.tpi = btn = wx.RadioButton(self, label="TPI", style = wx.RB_GROUP)
        sizerG.Add(btn, flag=wx.ALIGN_CENTER_VERTICAL|wx.ALL, border=2)
        info['thTPI'] = btn

        self.mm = btn = wx.RadioButton(self, label="mm")
        sizerG.Add(btn, flag=wx.ALIGN_CENTER_VERTICAL|wx.ALL, border=2)
        info['thMM'] = btn

        # x parameters

        self.xStart = addField(self, sizerG, "X Start D", "thXStart")

        self.xRetract = addField(self, sizerG, "X Retract", "thXRetract")

        self.depth = addField(self, sizerG, "Depth", "thXDepth")

        self.lastFeed = addField(self, sizerG, "Last Feed", "thXLastFeed")
        
        # self.final = btn = wx.RadioButton(self, label="Final",
        #                                   style = wx.RB_GROUP)
        # sizerH.Add(btn, flag=wx.CENTER|wx.ALL, border=2)
        # info['thFinal'] = btn

        # self.depth = btn = wx.RadioButton(self, label="Depth")
        # sizerH.Add(btn, flag=wx.CENTER|wx.ALL, border=2)
        # info['thDepth'] = btn

        self.angle = addField(self, sizerG, "Angle", "thAngle")

        self.hFactor = addField(self, sizerG, "H Factor", "thHFactor")

        sizerG.Add(wx.StaticText(self, -1, "Internal"), border=2,
                   flag=wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.ALL)
        self.internal = cb = wx.CheckBox(self, -1,
                                         style=wx.ALIGN_LEFT)
        self.Bind(wx.EVT_CHECKBOX, self.OnInternal, cb)
        sizerG.Add(cb, flag=wx.ALIGN_CENTER_VERTICAL|wx.ALL, border=2)
        info['thInternal'] = cb

        sizerG.Add(emptyCell)
        sizerG.Add(emptyCell)

        # pass info

        self.passes = addField(self, sizerG, "Passes", "thPasses")
        self.passes.SetEditable(False)

        self.sPInt = addField(self, sizerG, "SP Int", "thSPInt")

        self.spring = addField(self, sizerG, "Spring", "thSpring")

        sizerG.Add(emptyCell)
        sizerG.Add(emptyCell)

        # buttons

        btn = wx.Button(self, label='Send', size=(60,-1))
        btn.Bind(wx.EVT_BUTTON, self.OnSend)
        sizerG.Add(btn, flag=wx.CENTER|wx.ALL, border=2)

        btn = wx.Button(self, label='Start', size=(60,-1))
        btn.Bind(wx.EVT_BUTTON, self.OnStart)
        sizerG.Add(btn, flag=wx.CENTER|wx.ALL, border=2)

        # sizerG.Add(wx.StaticText(self, -1), border=2)

        btn = wx.Button(self, label='Add', size=(60,-1))
        btn.Bind(wx.EVT_BUTTON, self.OnAdd)
        sizerG.Add(btn, flag=wx.CENTER|wx.ALL, border=2)

        self.add = addField(self, sizerG, "", "thAddFeed")

        self.rpm = addField(self, sizerG, "RPM", "thRPM")

        sizerG.Add(wx.StaticText(self, -1, "Pause"), border=2,
                   flag=wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.ALL)
        self.pause = cb = wx.CheckBox(self, -1,
                                         style=wx.ALIGN_LEFT)
        sizerG.Add(cb, flag=wx.ALIGN_CENTER_VERTICAL|wx.ALL, border=2)
        info['thPause'] = cb

        sizerV.Add(sizerG, flag=wx.LEFT|wx.ALL, border=2)

        self.SetSizer(sizerV)
        self.sizerV.Fit(self)

    def update(self):
        pass

    def OnInternal(self, e):
        self.hFactor.SetValue(("0.75", "0.65")[self.internal.GetValue()])

    def sendData(self):
        try:
            sendClear()
            sendSpindleData()
            sendZData()
            sendXData()


        except commTimeout as e:
            print("timeout error")
            stdout.flush()

    def OnSend(self, e):
        global xHomed, jogPanel
        if xHomed:
            self.sendData()
            self.screwThread.thread()
        jogPanel.focus()

    def OnStart(self, e):
        global jogPanel
        command('CMD_RESUME')
        jogPanel.focus()
    
    def OnAdd(self, e):
        global jogPanel
        self.screwThread.threadAdd()
        passes = getParm('TOTAL_PASSES')
        self.passes.SetLabel("%d" % (passes))
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

class JogPanel(wx.Panel):
    def __init__(self, parent, *args, **kwargs):
        super(JogPanel, self).__init__(parent, *args, **kwargs)
        self.jogCode = None
        self.repeat = 0
        # self.lastTime = 0
        self.btnRpt = ButtonRepeat()
        self.initUI()
        self.setZPosDialog = None
        self.setXPosDialog = None
        self.fixXPosDialog = None
        self.xHome = False
        self.zStepsInch = 0
        self.xStepsInch = 0
        self.zEncInch = 0
        self.xEncInch = 0
        self.zEncInvert = 0
        self.xEncInvert = 0

    def initUI(self):
        global info, emptyCell
        self.Bind(wx.EVT_LEFT_UP, self.OnMouseEvent)

        sizerV = wx.BoxSizer(wx.VERTICAL)

        sizerG = wx.FlexGridSizer(6, 0, 0)

        posFont = wx.Font(20, wx.MODERN, wx.NORMAL,
                          wx.NORMAL, False, u'Consolas')
        txtFont = wx.Font(16, wx.MODERN, wx.NORMAL,
                          wx.NORMAL, False, u'Consolas')

        # first row
        # z position

        txt = wx.StaticText(self, -1, "Z")
        txt.SetFont(txtFont)
        sizerG.Add(txt, flag=wx.LEFT|wx.RIGHT|wx.ALIGN_RIGHT| \
                   wx.ALIGN_CENTER_VERTICAL, border=10)

        self.zPos = tc = wx.TextCtrl(self, -1, "0.0000", size=(120, -1),
                                     style=wx.TE_RIGHT)
        info['jogZPos'] = tc
        tc.SetFont(posFont)
        tc.SetEditable(False)
        tc.Bind(wx.EVT_RIGHT_DOWN, self.OnZMenu)
        sizerG.Add(tc, flag=wx.CENTER|wx.ALL, border=2)

        # x Position

        txt = wx.StaticText(self, -1, "X")
        txt.SetFont(txtFont)
        sizerG.Add(txt, flag=wx.LEFT|wx.RIGHT|wx.ALIGN_RIGHT| \
                   wx.ALIGN_CENTER_VERTICAL, border=10)

        self.xPos = tc = wx.TextCtrl(self, -1, "0.0000", size=(120, -1),
                                     style=wx.TE_RIGHT)
        info['jogXPos'] = tc
        tc.SetFont(posFont)
        tc.SetEditable(False)
        # tc.Bind(wx.EVT_LEFT_DOWN, self.OnSetXPos)
        tc.Bind(wx.EVT_RIGHT_DOWN, self.OnXMenu)
        sizerG.Add(tc, flag=wx.CENTER|wx.ALL, border=2)

        # rpm

        txt = wx.StaticText(self, -1, "RPM")
        txt.SetFont(txtFont)
        sizerG.Add(txt, flag=wx.LEFT|wx.RIGHT|wx.ALIGN_RIGHT| \
                   wx.ALIGN_CENTER_VERTICAL, border=10)

        self.rpm = tc = wx.TextCtrl(self, -1, "0", size=(80, -1),
                                    style=wx.TE_RIGHT)
        tc.SetFont(posFont)
        tc.SetEditable(False)
        sizerG.Add(tc, flag=wx.CENTER|wx.ALL, border=2)

        # second row
        # blank space

        sizerG.Add(emptyCell)
        sizerG.Add(emptyCell)

        # x diameter

        txt = wx.StaticText(self, -1, "X D")
        txt.SetFont(txtFont)
        sizerG.Add(txt, flag=wx.LEFT|wx.RIGHT|wx.ALIGN_RIGHT| \
                   wx.ALIGN_CENTER_VERTICAL, border=10)

        self.xPosDiam = tc = wx.TextCtrl(self, -1, "0.0000", size=(120, -1),
                                         style=wx.TE_RIGHT)
        info['jogXPosDiam'] = tc
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

        self.curPass = tc = wx.TextCtrl(self, -1, "0", size=(40, -1),
                                        style=wx.TE_RIGHT)
        tc.SetFont(posFont)
        tc.SetEditable(False)
        sizerG.Add(tc, flag=wx.CENTER|wx.ALL, border=2)

        # third row
        # z encoder position

        txt = wx.StaticText(self, -1, "Z")
        txt.SetFont(txtFont)
        sizerG.Add(txt, flag=wx.LEFT|wx.RIGHT|wx.ALIGN_RIGHT| \
                   wx.ALIGN_CENTER_VERTICAL, border=10)

        self.zEncPos = tc = wx.TextCtrl(self, -1, "0.0000", size=(120, -1),
                                        style=wx.TE_RIGHT)
        info['encZPos'] = tc
        tc.SetFont(posFont)
        tc.SetEditable(False)
        sizerG.Add(tc, flag=wx.CENTER|wx.ALL, border=2)

        # x encoder Position

        txt = wx.StaticText(self, -1, "X")
        txt.SetFont(txtFont)
        sizerG.Add(txt, flag=wx.LEFT|wx.RIGHT|wx.ALIGN_RIGHT| \
                   wx.ALIGN_CENTER_VERTICAL, border=10)

        self.xEncPos = tc = wx.TextCtrl(self, -1, "0.0000", size=(120, -1),
                                        style=wx.TE_RIGHT)
        info['encXPos'] = tc
        tc.SetFont(posFont)
        tc.SetEditable(False)
        sizerG.Add(tc, flag=wx.CENTER|wx.ALL, border=2)

        sizerV.Add(sizerG, flag=wx.ALIGN_CENTER_VERTICAL|wx.CENTER|wx.ALL,
                   border=2)

        sizerG = wx.FlexGridSizer(5, 0, 0)
        sFlag = wx.ALL|wx.CENTER|wx.ALIGN_CENTER_VERTICAL

        # first row

        sizerG.Add(emptyCell)
        sizerG.Add(emptyCell)
        sizerG.Add(emptyCell)

        bmp = wx.Bitmap("north.gif", wx.BITMAP_TYPE_ANY)
        btn = wx.BitmapButton(self, id=wx.ID_ANY, bitmap=bmp,
                              size=(bmp.GetWidth()+10, bmp.GetHeight()+10))
        self.xNegButton = btn
        btn.Bind(wx.EVT_LEFT_DOWN, self.OnXNegDown)
        btn.Bind(wx.EVT_LEFT_UP, self.OnXUp)
        sizerG.Add(btn, flag=sFlag|wx.EXPAND, border=2)

        sizerG.Add(emptyCell)

        # second row

        bmp = wx.Bitmap("west.gif", wx.BITMAP_TYPE_ANY)
        btn = wx.BitmapButton(self, id=wx.ID_ANY, bitmap=bmp,
                              size=(bmp.GetWidth()+10, bmp.GetHeight()+10))
        self.zNegButton = btn
        btn.Bind(wx.EVT_LEFT_DOWN, self.OnZNegDown)
        btn.Bind(wx.EVT_LEFT_UP, self.OnZUp)
        sizerG.Add(btn, flag=sFlag, border=2)

        btn = wx.Button(self, label='H', style=wx.BU_EXACTFIT)
        btn.Bind(wx.EVT_BUTTON, self.OnZHome)
        sizerG.Add(btn, flag=sFlag, border=2)

        bmp = wx.Bitmap("east.gif", wx.BITMAP_TYPE_ANY)
        btn = wx.BitmapButton(self, id=wx.ID_ANY, bitmap=bmp,
                              size=(bmp.GetWidth()+10, bmp.GetHeight()+10))
        self.zPosButton = btn
        btn.Bind(wx.EVT_LEFT_DOWN, self.OnZPosDown)
        btn.Bind(wx.EVT_LEFT_UP, self.OnZUp)
        sizerG.Add(btn, flag=sFlag, border=2)

        btn = wx.Button(self, label='H', style=wx.BU_EXACTFIT)
        btn.Bind(wx.EVT_BUTTON, self.OnXHome)
        sizerG.Add(btn, flag=sFlag, border=2)

        self.step = step = ["Cont", "0.001", "0.002", "0.005",
                            "0.010", "0.020", "0.050",
                            "0.100", "0.200", "0.500", "1.000"]

        self.combo = combo = wx.ComboBox(self, -1, step[1], choices=step,
                                         style=wx.CB_READONLY)
        info['jogInc'] = combo
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
        btn = wx.BitmapButton(self, id=wx.ID_ANY, bitmap=bmp,
                              size=(bmp.GetWidth()+10, bmp.GetHeight()+10))
        self.xPosButton = btn
        btn.Bind(wx.EVT_LEFT_DOWN, self.OnXPosDown)
        btn.Bind(wx.EVT_LEFT_UP, self.OnXUp)
        sizerG.Add(btn, flag=sFlag|wx.EXPAND, border=2)

        sizerG.Add(emptyCell)

        sizerV.Add(sizerG, flag=wx.ALIGN_CENTER_VERTICAL|wx.CENTER|wx.ALL,
                   border=2)

        sizerH = wx.BoxSizer(wx.HORIZONTAL)

        btn = wx.Button(self, label='Stop')
        btn.Bind(wx.EVT_BUTTON, self.OnStop)
        sizerH.Add(btn, flag=wx.CENTER|wx.ALL, border=2)

        btn = wx.Button(self, label='E Stop')
        btn.Bind(wx.EVT_BUTTON, self.OnEStop)
        sizerH.Add(btn, flag=wx.CENTER|wx.ALL, border=2)

        btn = wx.Button(self, label='Pause')
        btn.Bind(wx.EVT_BUTTON, self.OnPause)
        sizerH.Add(btn, flag=wx.CENTER|wx.ALL, border=2)

        btn = wx.Button(self, label='Resume')
        btn.Bind(wx.EVT_BUTTON, self.OnResume)
        sizerH.Add(btn, flag=wx.CENTER|wx.ALL, border=2)

        if STEPPER_DRIVE:
            btn = wx.Button(self, label='Start Spindle')
            btn.Bind(wx.EVT_BUTTON, self.OnStartSpindle)
            sizerH.Add(btn, flag=wx.CENTER|wx.ALL, border=2)

            btn = wx.Button(self, label='Jog Spindle')
            btn.Bind(wx.EVT_LEFT_DOWN, self.OnJogSpindle)
            btn.Bind(wx.EVT_LEFT_UP, self.OnJogUp)
            sizerH.Add(btn, flag=wx.CENTER|wx.ALL, border=2)

        sizerV.Add(sizerH, flag=wx.CENTER|wx.ALL, border=2)

        self.SetSizer(sizerV)
        sizerV.Fit(self)

    def menuPos(self, e, ctl):
        (xPos, yPos) = ctl.GetPosition()
        (x, y) = e.GetPosition()
        xPos += x
        yPos += y
        return(xPos, yPos)
    
    def OnZMenu(self, e):
        menu = PosMenu(0)
        self.PopupMenu(menu, self.menuPos(e, self.zPos))
        menu.Destroy()

    def OnXMenu(self, e):
        menu = PosMenu(1)
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
            if self.jogCode != code:
                if self.jogCode == None:
                    self.jogCode = code
                    self.repeat = 0
                    dir = 1
                    if code == wx.WXK_LEFT:
                        dir = -1
                    print("zJogCmd %d" % (dir))
                    stdout.flush()
                    try:
                        setParm('Z_JOG_DIR', dir)
                        command("ZJMOV")
                    except commTimeout as e:
                        pass
            else:
                try:
                    command("ZJMOV")
                except commTimeout as e:
                    pass
        else:
            if self.jogCode == None:
                self.jogCode = code
                if code == wx.WXK_LEFT:
                    val = '-' + val
                print("zJogCmd %s" % (val))
                stdout.flush()
                try:
                    setParm('Z_MOVE_DIST', val)
                    command('ZMOVE')
                except commTimeout as e:
                    pass

    def jogDone(self, cmd):
        self.jogCode = None
        val = self.getInc()
        if val == "Cont":
            print("jogDone %d" % (self.repeat))
            stdout.flush()
            try:
                command(cmd)
            except commTimeout as e:
                pass

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
        command('ZGOHOME')
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
                        setParm('X_JOG_DIR', dir)
                        command("XJMOV")
                    except commTimeout as e:
                        pass
            else:
                try:
                    command("XJMOV")
                except commTimeout as e:
                    pass
        else:
            if self.jogCode == None:
                self.jogCode = code
                if code == wx.WXK_UP:
                    val = '-' + val
                print("xJogCmd %s" % (val))
                stdout.flush()
                try:
                    setParm('X_MOVE_DIST', val)
                    command('XMOVE')
                except commTimeout as e:
                    pass

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
        command('XGOHOME')
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
        setParm('Z_MPG_INC', val * self.zStepsInch)
        setParm('X_MPG_INC', val * self.xStepsInch)

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
        global info, mainFrame
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
                if val >= len(self.step) - 1:
                    combo.SetSelection(1)
                else:
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
            mainPanel = info['mainPanel'].GetValue()
            panel = mainFrame.panels[mainPanel]
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
        if self.zStepsInch != 0.0:
            txt = "%7.3f" % (float(val) / self.zStepsInch)
        else:
            txt = '0.000'
        self.zPos.SetValue(txt)

    def updateX(self, val):
        if self.xStepsInch != 0.0:
            txt = "%7.3f" % (float(val) / self.xStepsInch)
        else:
            txt = '0.000'
        self.xPos.SetValue(txt)

    def updateRPM(self, val):
        print val
        stdout.flush()

    def updateAll(self, val):
        global zHomeOffset, xHomeOffset, zEncOffset, xEncOffset
        if len(val) == 6:
            (z, x, rpm, curPass, zEncPos, xEncPos) = val
            if z != '#':
                self.zPos.SetValue("%0.4f" % (float(z) - zHomeOffset))
            if x != '#':
                val = float(x) - xHomeOffset
                self.xPos.SetValue("%0.4f" % (val))
                self.xPosDiam.SetValue("%0.4f" % (val * 2))
            self.rpm.SetValue(rpm)
            self.curPass.SetValue(curPass)

            encPos = float(zEncPos) / self.zEncInch
            if self.zEncInvert:
                encPos = -encPos
            encPos -= zEncOffset
            self.zEncPos.SetValue("%0.4f" % (encPos))

            encPos = float(xEncPos) / self.xEncInch
            if self.xEncInvert:
                encPos = -encPos
            encPos -= xEncOffset
            self.xEncPos.SetValue("%0.4f" % (encPos))

            if self.xHome:
                global xHomed
                val = getParm('X_HOME_STATUS')
                if val != None:
                    if val & HOME_SUCCESS:
                        self.xHome = False
                        print("home success")
                        xHomed = True
                        stdout.flush()
                    elif val & HOME_FAIL:
                        self.xHome = False
                        print("home success")
                        stdout.flush()

    def OnEStop(self, e):
        global spindleDataSend, zDataSent, xDataSent
        queClear()
        command('CMD_CLEAR')
        spindleDataSent = False
        zDataSent = False
        xDataSent = False
        self.combo.SetFocus()

    def OnStop(self, e):
        queClear()
        command('CMD_STOP')
        self.combo.SetFocus()

    def OnPause(self, e):
        command('CMD_PAUSE')
        self.combo.SetFocus()

    def OnResume(self, e):
        command('CMD_RESUME')
        self.combo.SetFocus()

    def OnStartSpindle(self, e):
        if STEPPER_DRIVE:
            mainPanel = info['mainPanel'].GetValue()
            panel = mainFrame.panels[mainPanel]
            rpm = panel.rpm.GetValue()
            sendSpindleData(True, rpm)
            command('SPINDLE_START')
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
        except commTimeout as e:
            pass
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
        except commTimeout as e:
            pass
        self.combo.SetFocus()

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

        if self.axis == 1:
            item = wx.MenuItem(self, wx.NewId(), "Home")
            self.Append(item)
            self.Bind(wx.EVT_MENU, self.OnHomeX, item)

        item = wx.MenuItem(self, wx.NewId(), "Go to")
        self.Append(item)
        self.Bind(wx.EVT_MENU, self.OnGoto, item)

        if self.axis == 1:
            item = wx.MenuItem(self, wx.NewId(), "Fix X")
            self.Append(item)
            self.Bind(wx.EVT_MENU, self.OnFixX, item)

    def getPosCtl(self):
        if self.axis == 0:
            ctl = jogPanel.zPos
        else:
            ctl = jogPanel.xPos
        return(jogPanelPos(ctl))

    def OnSet(self, e):
        dialog = SetPosDialog(jogPanel, self.axis)
        dialog.SetPosition(self.getPosCtl())
        dialog.Raise()
        dialog.Show(True)

    def OnZero(self, e):
        if self.axis == 0:
            sendZData()
            setParm('Z_SET_LOC', 0)
            command('ZSETLOC')
        else:
            sendXData()
            setParm('X_SET_LOC', 0)
            command('XSETLOC')
        jogPanel.focus()

    def OnHomeX(self, e):
        setParm('X_HOME_DIST', getInfo('xHomeDist'))
        setParm('X_HOME_BACKOFF_DIST', getInfo('xHomeBackoffDist'))
        setParm('X_HOME_SPEED', getInfo('xHomeSpeed'))
        val = (-1, 1)[info['xHomeDir'].GetValue()]
        setParm('X_HOME_DIR', val)
        command('XHOMEAXIS')
        jogPanel.xHome = True
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
        global info
        self.axis = axis
        pos = (10, 10)
        title = "Set %s" % (('Z Position', 'X Diameter')[axis])
        wx.Dialog.__init__(self, frame, -1, title, pos,
                            wx.DefaultSize, wx.DEFAULT_DIALOG_STYLE)
        self.Bind(wx.EVT_SHOW, self.OnShow)
        self.sizerV = sizerV = wx.BoxSizer(wx.VERTICAL)

        posFont = wx.Font(20, wx.MODERN, wx.NORMAL,
                          wx.NORMAL, False, u'Consolas')
        self.pos = tc = wx.TextCtrl(self, -1, "0.000", size=(120, -1),
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
            if self.axis == 0:
                val = jogPanel.zPos.GetValue()
            else:
                val = jogPanel.xPos.GetValue()
            self.pos.SetValue(val)
            self.pos.SetSelection(-1, -1)

    def OnKeyChar(self, e):
        keyCode = e.GetKeyCode()
        if keyCode == wx.WXK_RETURN:
            self.OnOk(None)
        e.Skip()
    
    def OnOk(self, e):
        global jogPanel, zHomeOffset, xHomeOffset
        val = self.pos.GetValue()
        if self.axis == 0:
            try:
                val = float(val)
                sendZData()
                zLoc = getParm('Z_LOC')
                if zLoc != None:
                    zLoc /= jogPanel.zStepsInch
                    zHomeOffset = zLoc - val
                    info['zHomeOffset'].SetValue("%0.4f" % (zHomeOffset))
                    print("zHomeOffset %0.4f" % (zHomeOffset))
                    stdout.flush()
                self.Show(False)
                jogPanel.focus()
            except ValueError:
                val = jogPanel.zPos.GetValue()
                self.zPos.SetValue(val)
        else:
            try:
                val = float(val)
                sendXData()
                xLoc = getParm('X_LOC')
                if xLoc != None:
                    xLoc /= jogPanel.xStepsInch
                    xHomeOffset = xLoc - val
                    info['xHomeOffset'].SetValue("%0.4f" % (xHomeOffset))
                    print("xHomeOffset %0.4f" % (xHomeOffset))
                    stdout.flush()
                self.Show(False)
                jogPanel.focus()
            except ValueError:
                val = jogPanel.xPos.GetValue()
                self.xPos.SetValue(val)

class GotoDialog(wx.Dialog):
    def __init__(self, frame, axis):
        global info
        self.axis = axis
        pos = (10, 10)
        title = "Go to %s" % (('Z Position', 'X Diameter')[axis])
        wx.Dialog.__init__(self, frame, -1, title, pos,
                            wx.DefaultSize, wx.DEFAULT_DIALOG_STYLE)
        self.Bind(wx.EVT_SHOW, self.OnShow)
        self.sizerV = sizerV = wx.BoxSizer(wx.VERTICAL)

        posFont = wx.Font(20, wx.MODERN, wx.NORMAL,
                          wx.NORMAL, False, u'Consolas')
        self.pos = tc = wx.TextCtrl(self, -1, "0.000", size=(120, -1),
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
            if self.axis == 0:
                val = jogPanel.zPos.GetValue()
            else:
                val = jogPanel.xPos.GetValue()
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
        global jogPanel
        try:
            loc = float(self.pos.GetValue())
            queClear()
            command('CMD_PAUSE')
            command('CLEARQUE')
            if self.axis == 0:
                sendZData()
                saveZOffset()
                moveZ(loc)
            else:
                sendXData()
                saveXOffset()
                moveX(loc / 2.0)
            command('CMD_RESUME')
            self.Show(False)
            jogPanel.focus()
        except ValueError:
            print("ValueError")
            stdout.flush()

class FixXPosDialog(wx.Dialog):
    def __init__(self, frame):
        pos = (10, 10)
        wx.Dialog.__init__(self, frame, -1, "Fix X Size", pos,
                            wx.DefaultSize, wx.DEFAULT_DIALOG_STYLE)
        self.Bind(wx.EVT_SHOW, self.OnShow)
        self.sizerV = sizerV = wx.BoxSizer(wx.VERTICAL)

        posFont = wx.Font(20, wx.MODERN, wx.NORMAL,
                          wx.NORMAL, False, u'Consolas')

        sizerG = wx.FlexGridSizer(2, 0, 0)

        txt = wx.StaticText(self, -1, "Current")
        sizerG.Add(txt, flag=wx.LEFT|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL,
                   border=10)

        self.curXPos = tc = wx.TextCtrl(self, -1, "0.000", size=(120, -1),
                                        style=wx.TE_RIGHT)
        tc.SetFont(posFont)
        sizerG.Add(tc, flag=wx.CENTER|wx.ALL, border=10)

        txt = wx.StaticText(self, -1, "Measured")
        sizerG.Add(txt, flag=wx.LEFT|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL,
                   border=10)

        self.actualXPos = tc = wx.TextCtrl(self, -1, "0.0000", size=(120, -1),
                                           style=wx.TE_RIGHT|wx.TE_PROCESS_ENTER)
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
                xDiameter = float(getParm('X_DIAMETER')) / jogPanel.xStepsInch
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

        info['xHomeOffset'].SetValue("%0.4f" % (xHomeOffset))
        print ("curX %0.4f actualX %0.4f offset %0.4f xHomeOffset %0.4f" %
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
        self.notifyWindow = notifyWindow
        self.threadRun = True
        self.parmList = (self.readAll, )
        self.start()
        # self.getParm = (self.zLoc, self.xLoc, self.rpm)

    def zLoc(self):
        val = getParm('Z_LOC')
        if val != None:
            result = (0, val)
            wx.PostEvent(self.notifyWindow, UpdateEvent(result))

    def xLoc(self):
        val = getParm('X_LOC')
        if val != None:
            result = (1, val)
            wx.PostEvent(self.notifyWindow, UpdateEvent(result))

    def rpm(self):
        period = getParm('INDEX_PERIOD')
        if period != None:
            preScaler = getParm('INDEX_PRE_SCALER')
            result = (2, period * preScaler)
            wx.PostEvent(self.notifyWindow, UpdateEvent(result))

    def readAll(self):
        tmp = comm.xDbgPrint
        comm.xDbgPrint = False
        try:
            result = command('READLOC')
        except commTimeout:
            printf("readAll error")
            stdout.flush()
            return
        except serial.SerialException:
            print("readAll SerialException")
            stdout.flush()
            return
        comm.xDbgPrint = True
        if result == None:
            return
        try:
            (z, x, rpm, curPass, encZ, encX) = result.rstrip().split(' ')[1:]
            result = (3, z, x, rpm, curPass, encZ, encX)
            wx.PostEvent(self.notifyWindow, UpdateEvent(result))
        except ValueError:
            print("readAll ValueError %s" % (result))
            stdout.flush()

    def run(self):
        global dbg
        i = 0
        op = None
        scanMax = len(self.parmList) + 1
        while True:
            sleep(0.1)
            if not self.threadRun:
                break
            if i < len(self.parmList):
                func = self.parmList[i]
                try:
                    func()
                except commTimeout as e:
                    pass
            else:
                if not moveQue.empty() or (op != None):
                    try:
                        num = getQueueStatus()
                        if num != None:
                            while num > 0:
                                num -= 1
                                if op == None:
                                    try:
                                        (op, val) = moveQue.get(False)
                                    except Empty as e:
                                        break
                                try:
                                    sendMove(op, val)
                                    op = None
                                except commTimeout as e:
                                    break
                    except commTimeout as e:
                        pass
            i += 1
            if i >= scanMax:
                i = 0
            for count in range(0, 10):
                try:
                    result = getString()
                    if result:
                        if dbg != None:
                            dbg.write(result + '\n')
                            dbg.flush()
                        else:
                            print result
                            stdout.flush()
                    else:
                        break
                except commTimeout:
                    break
                except serial.SerialException:
                    print("getString SerialException")
                    stdout.flush()
                    break
        print("done")
        stdout.flush()

    def abort(self):
        self.run = False

class KeyEventFilter(wx.EventFilter):
    def __init__(self):
        wx.EventFilter.__init__(self)
        wx.EvtHandler.AddFilter(self)

    def __del__(self):
        wx.EvtHandler.RemoveFilter(self)

    def FilterEvent(self, event):
        t = event.GetEventType()
        if t == wx.EVT_KEY_DOWN:
            print("key down")
        event.Skip()

class MainFrame(wx.Frame):
    def __init__(self, parent, title):
        global hdrFont, testFont
        wx.Frame.__init__(self, parent, -1, title)
        self.Bind(wx.EVT_CLOSE, self.onClose)
        evtUpdate(self, self.OnUpdate)
        hdrFont = wx.Font(20, wx.MODERN, wx.NORMAL, 
                          wx.NORMAL, False, u'Consolas')
        testFont = wx.Font(10, wx.MODERN, wx.NORMAL, 
                          wx.NORMAL, False, u'Consolas')

        self.zDialog = ZDialog(self)
        self.xDialog = XDialog(self)
        self.spindleDialog = SpindleDialog(self)
        self.portDialog = PortDialog(self)
        self.configDialog = ConfigDialog(self)

        self.testSpindleDialog = None
        self.testSyncDialog = None
        self.testTaperDialog = None
        self.testMoveDialog = None

        self.initUI()

        openSerial(getInfo('commPort'), 57600)
        global cmds, parms
        comm.cmds = cmds
        comm.parms = parms
        if XILINX:
            comm.xRegs = xRegs

        sendClear()
        stdout.flush()

        if comm.ser != None:
            sendZData()
            val = getInfo('jogZPos')
            setParm('Z_SET_LOC', val)
            command('ZSETLOC')
            sendXData()
            val = getInfo('jogXPos')
            setParm('X_SET_LOC', val)
            command('XSETLOC')
            loc = str(int(getFloatInfo('xHomeLoc') * jogPanel.xStepsInch))
            setParm('X_HOME_LOC', loc)

        self.procUpdate = (self.jogPanel.updateZ,
                           self.jogPanel.updateX,
                           self.jogPanel.updateRPM,
                           self.jogPanel.updateAll)

        self.update = UpdateThread(self)

    def onClose(self, event):
        global done, jogPanel
        done = True
        self.update.threadRun = False
        jogPanel.btnRpt.threadRun = False
        self.Destroy()

    def initUI(self):
        global jogPanel, info, zHomeOffset, xHomeOffset, \
            zEncOffset, xEncOffset
        fileMenu = wx.Menu()

        ID_FILE_SAVE = wx.NewId()
        menu = fileMenu.Append(ID_FILE_SAVE, 'Save')
        self.Bind(wx.EVT_MENU, self.OnSave, menu)

        ID_FILE_EXIT = wx.NewId()
        menu = fileMenu.Append(ID_FILE_EXIT, 'Exit')
        self.Bind(wx.EVT_MENU, self.OnExit, menu)

        ID_Z_SETUP = wx.NewId()
        setupMenu = wx.Menu()
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

        readInfo(configFile)

        key = 'zHomeOffset'
        if not key in info:
            info[key] = InfoValue("%0.4f" % (zHomeOffset))
        else:
            zHomeOffset = float(info[key].GetValue())

        key = 'xHomeOffset'
        if not key in info:
            info[key] = InfoValue("%0.4f" % (xHomeOffset))
        else:
            xHomeOffset = float(info[key].GetValue())

        key = 'zEncOffset'
        if not key in info:
            info[key] = InfoValue("%0.4f" % (zEncOffset))
        else:
            zEncOffset = float(info[key].GetValue())

        key = 'xEncOffset'
        if not key in info:
            info[key] = InfoValue("%0.4f" % (xEncOffset))
        else:
            xEncOffset = float(info[key].GetValue())

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
        saveInfo('config.txt')
        
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
        self.showDialog(self.zDialog)

    def OnSpindleSetup(self, e):
        self.showDialog(self.spindleDialog)

    def OnPortSetup(self, e):
        self.showDialog(self.portDialog)

    def OnConfigSetup(self, e):
        self.showDialog(self.configDialog)

    def showPanel(self):
        global info
        key = 'mainPanel'
        if not key in info:
            info[key] = InfoValue('turnPanel')
        mainPanel = info[key].GetValue()

        for key in self.panels:
            panel = self.panels[key]
            if key == mainPanel:
                panel.Show()
            else:
                panel.Hide()
        self.Layout()
        self.Fit()

    def OnTurn(self, e):
        global info
        info['mainPanel'].SetValue('turnPanel')
        self.showPanel()

    def OnFace(self, e):
        global info
        info['mainPanel'].SetValue('facePanel')
        self.showPanel()

    def OnCutoff(self, e):
        global info
        info['mainPanel'].SetValue('cutoffPanel')
        self.showPanel()

    def OnTaper(self, e):
        global info
        info['mainPanel'].SetValue('taperPanel')
        self.showPanel()

    def OnThread(self, e):
        global info
        info['mainPanel'].SetValue('threadPanel')
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

    def OnUpdate(self, e):
        index = e.data[0]
        if index < len(self.procUpdate):
            update = self.procUpdate[index]
            val = e.data[1:]
            if len(val) == 1:
                val = val[0]
            update(val)

class ZDialog(wx.Dialog):
    def __init__(self, frame):
        global info
        pos = (10, 10)
        wx.Dialog.__init__(self, frame, -1, "Z Setup", pos,
                            wx.DefaultSize, wx.DEFAULT_DIALOG_STYLE)
        self.Bind(wx.EVT_SHOW, self.OnShow)
        self.sizerV = sizerV = wx.BoxSizer(wx.VERTICAL)

        sizerG = wx.FlexGridSizer(2, 0, 0)

        self.fields = (
            ("Pitch", "zPitch"),
            ("Motor Steps", "zMotorSteps"),
            ("Micro Steps", "zMicroSteps"),
            ("Motor Ratio", "zMotorRatio"),
            ("Backlash", "zBacklash"),
            ("Accel", "zAccel"),
            ("Min Speed", "zMinSpeed"),
            ("Max Speed", "zMaxSpeed"),
            ("Jog Min", "zJogMin"),
            ("Jog Max", "zJogMax"),
            ("bInvert Dir", 'zInvDir'),
            ("bInvert MPG", 'zInvMpg'),
            ("Enc Inch", "zEncInch"),
            ("bInv Encoder", 'zInvEnc'),
        )        
        fieldList(self, sizerG, self.fields)

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
        queClear()
        sendZData(True)

    def OnShow(self, e):
        global done, info, zDataSent
        if done:
            return
        if self.IsShown():
            self.fieldInfo = {}
            for (label, index) in self.fields:
                self.fieldInfo[index] = info[index].GetValue()
        else:
            for (label, index) in self.fields:
                if self.fieldInfo[index] != info[index].GetValue():
                    zDataSent = False
                    break

    def OnCancel(self, e):
        global info
        for (label, index) in self.fields:
            info[index].SetValue(self.fieldInfo[index])
        self.Show(False)

class XDialog(wx.Dialog):
    def __init__(self, frame):
        global info
        pos = (10, 10)
        wx.Dialog.__init__(self, frame, -1, "X Setup", pos,
                            wx.DefaultSize, wx.DEFAULT_DIALOG_STYLE)
        self.Bind(wx.EVT_SHOW, self.OnShow)
        self.sizerV = sizerV = wx.BoxSizer(wx.VERTICAL)

        sizerG = wx.FlexGridSizer(2, 0, 0)

        self.fields = (
            ("Pitch", "xPitch"),
            ("Motor Steps", "xMotorSteps"),
            ("Micro Steps", "xMicroSteps"),
            ("Motor Ratio", "xMotorRatio"),
            ("Backlash", "xBacklash"),
            ("Accel", "xAccel"),
            ("Min Speed", "xMinSpeed"),
            ("Max Speed", "xMaxSpeed"),
            ("Jog Min", "xJogMin"),
            ("Jog Max", "xJogMax"),
            ("bInvert Dir", 'xInvDir'),
            ("bInvert MPG", 'xInvMpg'),
            ("Home Dist", "xHomeDist"),
            ("Backoff Dist", "xHomeBackoffDist"),
            ("Home Speed", "xHomeSpeed"),
            ("bHome Dir", 'xHomeDir'),
            ("Enc Inch", "xEncInch"),
            ("bInv Encoder", 'xInvEnc'),
        )        
        global HOME_TEST
        if HOME_TEST:
            self.fields += (
                ("Home Start", "xHomeStart"),
                ("Home End", "xHomeEnd"),
                ("Home Loc", "xHomeLoc"))
        fieldList(self, sizerG, self.fields)

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
        loc = str(int(getFloatInfo('xHomeLoc') * jogPanel.xStepsInch))
        setParm('X_HOME_LOC', loc)
        
    def OnSetup(self, e):
        queClear()
        sendXData(True)

    def OnShow(self, e):
        global done, info, xDataSent
        if done:
            return
        if self.IsShown():
            self.fieldInfo = {}
            for (label, index) in self.fields:
                self.fieldInfo[index] = info[index].GetValue()
        else:
            for (label, index) in self.fields:
                if self.fieldInfo[index] != info[index].GetValue():
                    xDataSent = False
                    break

    def OnCancel(self, e):
        global info
        for (label, index) in self.fields:
            info[index].SetValue(self.fieldInfo[index])
        self.Show(False)

class SpindleDialog(wx.Dialog):
    def __init__(self, frame):
        global info
        pos = (10, 10)
        wx.Dialog.__init__(self, frame, -1, "Spindle Setup", pos,
                            wx.DefaultSize, wx.DEFAULT_DIALOG_STYLE)
        self.sizerV = sizerV = wx.BoxSizer(wx.VERTICAL)
        self.Bind(wx.EVT_SHOW, self.OnShow)
        sizerG = wx.FlexGridSizer(2, 0, 0)

        self.fields = (
            ("bStepper Drive", 'spStepDrive'),
        )
        if STEPPER_DRIVE:
            self.fields += (
                ("Motor Steps", "spMotorSteps"),
                ("Micro Steps", "spMicroSteps"),
                ("Min RPM", "spMinRPM"),
                ("Max RPM", "spMaxRPM"),
                ("Accel Time", "spAccelTime"),
                ("Jog Min", "spJogMin"),
                ("Jog Max", "spJogMax"),
                ("Jog Accel Time", "spJogAccelTime"),
                ("bInvert Dir", 'spInvDir'),
                ("bTest Index", 'spTestIndex'),
            )
        fieldList(self, sizerG, self.fields)

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
        global info, spindleDataSent
        for (label, index) in self.fields:
            tmp = info[index].GetValue()
            if self.fieldInfo[index] != tmp:
                self.fieldInfo[index] = tmp 
                spindleDataSent = False
        if not spindleDataSent:
            sendSpindleData()
        else:
            command('CMD_SPSETUP')
        command('SPINDLE_START')

    def OnStop(self, e):
        command('SPINDLE_STOP')

    def OnShow(self, e):
        global done, info, spindleDataSent
        if done:
            return
        if self.IsShown():
            self.fieldInfo = {}
            self.cancelInfo = {}
            for (label, index) in self.fields:
                tmp = info[index].GetValue()
                self.cancelInfo[index] = tmp
                self.fieldInfo[index] = tmp
            spindleDataSent = False
        else:
            for (label, index) in self.fields:
                if self.fieldInfo[index] != info[index].GetValue():
                    spindleDataSent = False
                    break

    def OnCancel(self, e):
        global info
        for (label, index) in self.fields:
            info[index].SetValue(self.cancelInfo[index])
        self.Show(False)

class PortDialog(wx.Dialog):
    def __init__(self, frame):
        pos = (10, 10)
        wx.Dialog.__init__(self, frame, -1, "Port Setup", pos,
                            wx.DefaultSize, wx.DEFAULT_DIALOG_STYLE)
        self.sizerV = sizerV = wx.BoxSizer(wx.VERTICAL)
        self.Bind(wx.EVT_SHOW, self.OnShow)
        sizerG = wx.GridSizer(2, 0, 0)

        self.fields = (
            ("Comm Port", "commPort"),)
        fieldList(self, sizerG, self.fields)

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
        global done, info
        if done:
            return
        if self.IsShown():
            self.fieldInfo = {}
            for (label, index) in self.fields:
                self.fieldInfo[index] = info[index].GetValue()

    def OnCancel(self, e):
        global info
        for (label, index) in self.fields:
            info[index].SetValue(self.fieldInfo[index])
        self.Show(False)

class ConfigDialog(wx.Dialog):
    def __init__(self, frame):
        global XILINX, info
        pos = (10, 10)
        wx.Dialog.__init__(self, frame, -1, "Config Setup", pos,
                            wx.DefaultSize, wx.DEFAULT_DIALOG_STYLE)
        self.sizerV = sizerV = wx.BoxSizer(wx.VERTICAL)
        self.Bind(wx.EVT_SHOW, self.OnShow)
        sizerG = wx.GridSizer(2, 0, 0)

        self.fields = (
            ("bHW Control", 'cfgXilinx'),)
        global XILINX
        if XILINX:
            self.fields += (
                ("Encoder", "cfgEncoder"),
                ("Xilinx Freq", "cfgXFreq"),
                ("Freq Mult", "cfgFreqMult"),
                ("bTest Mode", 'cfgTestMode'),
                ("Test RPM", "cfgTestRPM"),
                ("bInvert Enc Dir", 'cfgInvEncDir'))
        fieldList(self, sizerG, self.fields)

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
        global done, info
        if done:
            return
        if self.IsShown():
            self.fieldInfo = {}
            for (label, index) in self.fields:
                self.fieldInfo[index] = info[index].GetValue()

    def OnCancel(self, e):
        global info
        for (label, index) in self.fields:
            info[index].SetValue(self.fieldInfo[index])
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
        wx.Dialog.__init__(self, frame, -1, "Test Spindle", pos,
                            wx.DefaultSize, wx.DEFAULT_DIALOG_STYLE)

        txt = testText(self)
        self.spindleTest = SpindleTest(txt)
        
class TestSyncDialog(wx.Dialog):
    def __init__(self, frame):
        pos = (10, 10)
        wx.Dialog.__init__(self, frame, -1, "Test Sync", pos,
                            wx.DefaultSize, wx.DEFAULT_DIALOG_STYLE)

        txt = testText(self)
        self.syncTest = SyncTest(txt)

class TestTaperDialog(wx.Dialog):
    def __init__(self, frame):
        pos = (10, 10)
        wx.Dialog.__init__(self, frame, -1, "Test Taper", pos,
                            wx.DefaultSize, wx.DEFAULT_DIALOG_STYLE)

        txt = testText(self)
        self.taperTest = TaperTest(txt)

class TestMoveDialog(wx.Dialog):
    def __init__(self, frame):
        pos = (10, 10)
        wx.Dialog.__init__(self, frame, -1, "Test Move", pos,
                            wx.DefaultSize, wx.DEFAULT_DIALOG_STYLE)

        txt = testText(self)
        self.moveTest = MoveTest(txt)

def dbgPrt(txt, format, values):
    global f
    txt.AppendText((format + "\n") % values)
    f.write((format + "\n") % values)

fcy = 84000000

class SpindleTest():
    def __init__(self, txt):
        self.txt = txt

    def test(self):
        global f
        global fcy
        txt = self.txt
        txt.SetValue("")
        minRPM = float(getInfo('spMinRPM')) # minimum rpm
        maxRPM = float(getInfo('spMaxRPM')) # maximum rpm
        aTime = float(getInfo('spAccelTime'))  # accel time sec
        # accel = 10                      # rpm per sec
        
        f = open('spindle.txt','w')
        
        dbgPrt(txt,"minRPM %d maxRPM %d", (minRPM, maxRPM))
        
        spindleMicroSteps = int(getInfo('spMicroSteps'))
        spindleMotorSteps = int(getInfo('spMotorSteps'))
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
        accelStepsSec2 = deltaV / aTime
        dbgPrt(txt,"accel %0.1f rpm per sec", ((accelStepsSec2 / 
                                            spindleStepsRev) * 60))
        dbgPrt(txt,"deltaV %4.1f sStepsSecMin %4.1f sStepsSecMax %4.1f",
               (deltaV, sStepsSecMin, sStepsSecMax))
        
        accelMinTime = sStepsSecMin / accelStepsSec2
        accelMaxTime = sStepsSecMax / accelStepsSec2
        dbgPrt(txt,"accelMinTime %5.5f accelMaxTime %5.2f",
               (accelMinTime, accelMaxTime))
        
        accelMinSteps = int((sStepsSecMin * accelMinTime) / 2.0 + 0.5)
        accelMaxSteps = int((sStepsSecMax * accelMaxTime) / 2.0 + 0.5)
        dbgPrt(txt,"accelMinSteps %d accelMaxSteps %d ",
               (accelMinSteps, accelMaxSteps))
        
        accelTime = deltaV / accelStepsSec2
        accelSteps = accelMaxSteps - accelMinSteps
        accelClocks = accelTime * fcy;
        dbgPrt(txt,"accelStepsSec2 %0.1f accelTime %5.3f accelSteps %d "\
               "accelClocks %d",
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
        
        dbgPrt(txt,"accelMinSteps %d lastCount %d lastTime %0.6f",
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
                    "f %8.2f rpm %4.1f\n" %
                    (step, count, actCount, pre, ctr, ctr * pre - lastCtr,
                     time, delta, freq, rpm))
            lastCount = actCount
            lastCtr = ctr * pre
            lastTime = time
        
        f.write("\n")
        
        finalCount = int(cFactor * sqrt(accelMaxSteps))
        finalCount -= int(cFactor * sqrt(accelMaxSteps - 1))
        dbgPrt(txt,"finalCount %d lastCtr %d spindleClocksStep %d",
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
                    "f %8.2f rpm %4.1f\n" %
                    (step, count, ctr, ctr - lastCtr, time, delta, freq, rpm))
            lastCount = count
            lastCtr = ctr
            lastTime = time
        
        lastCount = int(cFactor * sqrt(accelMinSteps))
        f.write("\naccelMinSteps %d lastCount %d\n" % 
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
        mainPanel = info['mainPanel'].GetValue()
        if mainPanel == 'threadPanel':
            arg1 = float(getInfo('thPitch'))
        elif mainPanel == 'turnPanel':
            arg1 = float(getInfo('tuZFeed'))
        elif mainPanel == 'facePanel':
            arg1 = float(getInfo('faXFeed'))
            zAxis = False
        elif mainPanel == 'CutoffPanel':
            arg1 = float(getInfo('cuXFeed'))
            zAxis = False
        elif mainPanel == 'taperPanel':
            arg1 = float(getInfo('tpZFeed'))

        maxRPM = float(getInfo('spMaxRPM')) # maximum rpm

        spindleMicroSteps = int(getInfo('spMicroSteps'))
        spindleMotorSteps = int(getInfo('spMotorSteps'))
        spindleStepsRev = spindleMotorSteps * spindleMicroSteps
        dbgPrt(txt,"spindleStepsRev %d", (spindleStepsRev))
        
        spindleStepsSec = (maxRPM * spindleStepsRev) / 60.0
        spindleClocksStep = int(fcy / spindleStepsSec + .5)
        spindleClockPeriod = (float(spindleClocksStep) / fcy) * 1000000
        spindleClocksRev = spindleStepsRev * spindleClocksStep
        dbgPrt(txt,"spindleClocksStep %d spindleClockPeriod %6.3f us "\
               "spindleClocksRev %d",
               (spindleClocksStep, spindleClockPeriod, spindleClocksRev))
        dbgPrt(txt, "", ())

        if zAxis:
            zPitch = float(getInfo('zPitch'))
            zMicroSteps = float(getInfo('zMicroSteps'))
            zMotorSteps = float(getInfo('zMotorSteps'))
            zMotorRatio = float(getInfo('zMotorRatio'))
        else:
            zPitch = float(getInfo('xPitch'))
            zMicroSteps = float(getInfo('xMicroSteps'))
            zMotorSteps = float(getInfo('xMotorSteps'))
            zMotorRatio = float(getInfo('xMotorRatio'))

        zStepsInch = ((zMicroSteps * zMotorSteps * zMotorRatio) / zPitch)
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
            dbgPrt(txt,"pitch %5.3f revCycle %d cycleDist %5.3f",
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
               "zStepsCycle %d",
               (clocksCycle, cycleTime, spindleStepsCycle, zStepsCycle))
        
        zClocksStep = int(clocksCycle / zStepsCycle + 0.5)
        zRemainder = (clocksCycle - zClocksStep * zStepsCycle)
        dbgPrt(txt,"zClocksStep %d remainder %d",
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
        dbgPrt(txt,"zSpeedIPM %4.2f in/min zStepsSec %d steps/sec",
               (zSpeedIPM, zStepsPerSec))
        
        zAccel = .5                      # acceleration in per sec^2
        zAccelTime = ((zSpeedIPM / 60.0) / zAccel) # acceleration time
        dbgPrt(txt,"zAccel %5.3f in/sec^2 zAccelTime %8.6f sec",
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
                   "zAccelDist %5.3f",
                   (zAccelTime, zAccelSteps, zAccelClocks, zAccelDist))
        
            initialCount = int(cFactor1 * sqrt(1))
            initialCount -= int(cFactor1 * sqrt(0))
            finalCount = int(cFactor1 * sqrt(zAccelSteps))
        
            isrCount = finalCount + initialCount
        
            dbgPrt(txt,"initialCount %d initialTime %8.6f accelTime %8.6f "\
                   "hwTime %8.6f",
                   (initialCount, float(initialCount) / fcy,
                    float(finalCount) / fcy, float(isrCount) / fcy))
        
            zAccelSpindleSteps = int(isrCount / spindleClocksStep)
            remainder = isrCount - zAccelSpindleSteps * spindleClocksStep
            dbgPrt(txt,"zAccelSpindleSteps %d remainder %d",
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
                        "f %7.2f ipm %4.1f\n" %
                        (step, count, ctr, ctr - lastCtr, time, delta,
                         freq, ipm))
                lastCount = count
                lastCtr = ctr
                lastTime = time
        
            f.write("\n");
        
            # countRemainder = zAccelClocks - lastCount
            # div = int(countRemainder / zAccelSteps)
            # rem = countRemainder - zAccelSteps * div
            # dbgPrt(txt,"lastCount %d countRemainder %d div %d rem %d" % 
            #        (lastCount, countRemainder, div, rem))
        
            lastCount1 = int(cFactor1 * sqrt(zAccelSteps))
            lastTime1 = time = float(count) / fcy
            dbgPrt(txt,"lastCount1 %d lastTime1 %0.6f",
                   (lastCount1, lastTime1))
        
            # spindleSteps = lastCount1 / spindleClocksStep
            # spindleCount = spindleSteps * spindleClocksStep
            # countRemainder = lastCount1 - (spindleSteps * spindleClocksStep)
        
            # div = int(countRemainder / zAccelSteps)
            # rem = countRemainder - zAccelSteps * div
            # dbgPrt(txt,"spindleSteps %d lastCount %d countRemainder %d div "\
            #"%d rem %d",
            #        (spindleSteps, lastCount, countRemainder, div, rem))
        
            finalCount -= int(cFactor1 * sqrt(zAccelSteps - 1))
            dbgPrt(txt,"finalCount %d lastCtr %d zClocksStep %d",
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
        
        maxRPM = float(getInfo('spMaxRPM')) # maximum rpm
        spindleMicroSteps = int(getInfo('spMicroSteps'))
        spindleMotorSteps = int(getInfo('spMotorSteps'))
        spindleStepsRev = spindleMotorSteps * spindleMicroSteps
        dbgPrt(txt,"spindleStepsRev %d", (spindleStepsRev))

        spindleStepsSec = (maxRPM * spindleStepsRev) / 60.0
        spindleClocksStep = int(fcy / spindleStepsSec + .5)
        spindleClockPeriod = (float(spindleClocksStep) / fcy) * 1000000
        spindleClocksRev = spindleStepsRev * spindleClocksStep
        dbgPrt(txt,"spindleClocksStep %d spindleClockPeriod %6.3f us "\
               "spindleClocksRev %d",
               (spindleClocksStep, spindleClockPeriod, spindleClocksRev))
        dbgPrt(txt, "", ())

        zPitch = float(getInfo('zPitch'))
        zMicroSteps = float(getInfo('zMicroSteps'))
        zMotorSteps = float(getInfo('zMotorSteps'))
        zMotorRatio = float(getInfo('zMotorRatio'))

        zStepsInch = ((zMicroSteps * zMotorSteps * zMotorRatio) / zPitch)
        dbgPrt(txt,"zStepsInch %d", (zStepsInch))

        xPitch = float(getInfo('xPitch'))
        xMicroSteps = float(getInfo('xMicroSteps'))
        xMotorSteps = float(getInfo('xMotorSteps'))
        xMotorRatio = float(getInfo('xMotorRatio'))
        xStepsInch = ((xMicroSteps * xMotorSteps * xMotorRatio) / xPitch)
        dbgPrt(txt,"xStepsInch %d", (xStepsInch))

        pitch = float(getInfo('tpZFeed'))
        revCycle = int(1.0 / pitch + 0.5)
        if revCycle > 20:
            revCycle = 20
        cycleDist = revCycle * pitch
        dbgPrt(txt,"pitch %5.3f revCycle %d cycleDist %5.3f",
               (pitch, revCycle, cycleDist))
        clocksCycle = spindleClocksRev * revCycle
        spindleStepsCycle = spindleStepsRev * revCycle
        zStepsCycle = zStepsInch * revCycle * pitch

        zClocksStep = int(clocksCycle / zStepsCycle + 0.5)
        zRemainder = (clocksCycle - zClocksStep * zStepsCycle)
        dbgPrt(txt,"zClocksStep %d remainder %d",
               (zClocksStep, zRemainder))

        arg2 = float(getInfo('tpZDelta'))
        arg3 = float(getInfo('tpXDelta'))
        
        d0 = arg2
        d1 = arg3
        
        zCycleDist = float(zStepsCycle) / zStepsInch
        xCycleDist = (d1 / d0) * zCycleDist
        dbgPrt(txt,"zCycleDist %5.3f xCycleDist %5.3f",
               (zCycleDist, xCycleDist))
        
        d0Steps = int(zCycleDist * zStepsInch)
        d1Steps = int(xCycleDist * xStepsInch)
        d0Clocks = d0Steps * zClocksStep
        dbgPrt(txt,"d0Steps %d d1Steps %d d0Clocks %d",
               (d0Steps, d1Steps, d0Clocks));
        
        # d1ClocksStep = int(d0Clocks / d1Steps)
        # d1Remainder = d0Clocks - d1Steps * d1ClocksStep
        # dbgPrt(txt,"d1ClocksStep %d d1Remainder %d",
        #        (d1ClocksStep, d1Remainder))
        
        d1ClocksStep = int(clocksCycle / d1Steps)
        d1Remainder = clocksCycle - d1Steps * d1ClocksStep
        dbgPrt(txt,"d1ClocksStep %d d1Remainder %d",
               (d1ClocksStep, d1Remainder))
        
        dx = d1Steps;
        dy = d1Remainder;
        incr1 = 2 * dy;
        incr2 = incr1 - 2 * dx;
        d = incr1 - dx;
        dbgPrt(txt,"incr1 %d incr2 %d d %d",
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

        zPitch = float(getInfo('zPitch'))
        zMicroSteps = float(getInfo('zMicroSteps'))
        zMotorSteps = float(getInfo('zMotorSteps'))
        zMotorRatio = float(getInfo('zMotorRatio'))

        zStepsInch = ((zMicroSteps * zMotorSteps * zMotorRatio) / zPitch)
        dbgPrt(txt,"zStepsInch %d", (zStepsInch))
        
        zMinSpeed = float(getInfo('zMinSpeed')) # minimum speed ipm
        zMaxSpeed = float(getInfo('zMaxSpeed')) # maximum speed ipm
        zMoveAccelTime = float(getInfo('zAccel')) # accel time seconds
        dbgPrt(txt,"zMinSpeed %d zMaxSpeed %d zMoveAccelTime %4.2f",
               (zMinSpeed, zMaxSpeed, zMoveAccelTime))
        
        zMStepsSec = int((zMaxSpeed * zStepsInch) / 60.0)
        zMClocksStep = int(fcy / zMStepsSec)
        dbgPrt(txt,"zMStepsSec %d zMClocksStep %d", (zMStepsSec, zMClocksStep))
        
        zMinStepsSec = int((zStepsInch * zMinSpeed) / 60.0)
        zMaxStepsSec = int((zStepsInch * zMaxSpeed) / 60.0)
        dbgPrt(txt,"zMinStepsSec %d zMaxStepsSec %d",
               (zMinStepsSec, zMaxStepsSec))
        
        zMDeltaV = zMaxStepsSec - zMinStepsSec
        zMAccelStepsSec2 = zMDeltaV / zMoveAccelTime
        dbgPrt(txt,"zMDeltaV %d zMAccelStepsSec2 %6.3f",
               (zMDeltaV, zMAccelStepsSec2))
        
        if zMAccelStepsSec2 != 0:
            zMAccelMinTime = zMinStepsSec / zMAccelStepsSec2
            zMAccelMaxTime = zMaxStepsSec / zMAccelStepsSec2
            dbgPrt(txt,"zMAccelMinTime %d zMAccelMaxTime %d",
                   (zMAccelMinTime, zMAccelMaxTime))
        
            zMAccelMinSteps = int((zMinStepsSec * zMAccelMinTime) / 2.0 + 0.5)
            zMAccelMaxSteps = int((zMaxStepsSec * zMAccelMaxTime) / 2.0 + 0.5)
            dbgPrt(txt,"zMAccelMinSteps %d zMAccelMaxSteps %d",
                   (zMAccelMinSteps, zMAccelMaxSteps))
        
            zMAccelTime = zMDeltaV / zMAccelStepsSec2
            zMAccelSteps = zMAccelMaxSteps - zMAccelMinSteps
            zMAccelClocks = int(zMAccelTime * fcy)
            dbgPrt(txt,"zMAccelTime %5.3f zMAccelSteps %d zMAccelClocks %d",
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
                        "f %7.2f rpm %3.1f\n" %
                        (step, count, ctr, abs(ctr - lastCtr), time,
                         delta, freq, ipm))
                lastCount = count
                lastCtr = ctr
                lastTime = time
        
            f.write("\n")
        
            finalCount = int(zMCFactor * (sqrt(zMAccelSteps) - 
                                          sqrt(zMAccelSteps - 1)))
            dbgPrt(txt,"finalCount %d lastCtr %d zMClocksStep %d",
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
                        "f %7.2f ipm %3.1f\n" %
                        (step, count, ctr, abs(ctr - lastCtr), time,
                         delta, freq, ipm))
                lastCount = count
                lastCtr = ctr
                lastTime = time
        
            lastCount = int(zMCFactor * sqrt(zMAccelMinSteps))
            f.write("\nzMAccelMinSteps %d lastCount %d\n" % 
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
        print "invalid argument: %s" % (tmp)
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
            print evt
        return(-1)

app = MainApp(redirect=False)
# app.SetCallFilterEvent(True)
# wx.lib.inspection.InspectionTool().Show()
app.MainLoop()

if not (comm.ser is None):
    comm.ser.close()
