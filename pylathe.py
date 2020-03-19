#!/cygdrive/c/Python37/Python.exe
#!/usr/bin/python
#!/cygdrive/c/DevSoftware/Python/Python36-32/Python
################################################################################
from __future__ import print_function

import math
import os
import re
import subprocess
import sys
import traceback
from ctypes import c_uint32
from math import atan2, ceil, cos, degrees, floor, pi, radians, sqrt, tan
from platform import system
#from Queue import Empty, Queue
from queue import Empty, Queue
from sys import stderr, stdout
from threading import Event, Lock, Thread
from time import localtime, sleep, strftime, time
# from contextlib import redirect_stderr
#     with open(os.path.join(DBG_DIR, "err.log")) as stderr, \
#          redirect_stderr(stderr):

import serial
import wx
import wx.lib.inspection
from dxfwrite import DXFEngine as dxf

import cmdDef as cm
import configDef as cf
import ctlBitDef as ct
import enumDef as en
import parmDef as pm
import stringDef as st
import syncCmdDef as sc
import syncParmDef as sp
from configInfo import ConfigInfo, InfoValue
from sync import Sync

DBG_DIR = os.path.join(os.getcwd(), "dbg")
DXF_DIR = os.path.join(os.getcwd(), "dxf")
DBG_LOG = os.path.join(DBG_DIR, "dbgLog.txt")

stdError = stderr
stderr = open(os.path.join(DBG_DIR, "err.log"), 'w')
stderr.write("testing\n")

R_PI = False
WINDOWS = system() == 'Windows'
if WINDOWS:
    from pywinusb.hid import find_all_hid_devices
    from comm import Comm, CommTimeout
    if os.path.isfile("rpi.txt"):
        from commPi import Comm, CommTimeout
        R_PI = True
        print("rpi test mode")
else:
    print(os.uname())
    if not os.uname().machine.startswith('arm'):
        from comm import Comm, CommTimeout
    else:
        from commPi import Comm, CommTimeout
        R_PI = True

SWIG = False
HOME_TEST = False
SETUP = False

FPGA = False
DRO = False
EXT_DRO = False
X_DRO_POS = False
REM_DBG = False
STEP_DRV = False
MOTOR_TEST = False
SPINDLE_ENCODER = False
SPINDLE_SYNC_BOARD = False
TURN_SYNC = en.SEL_TU_SPEED
THREAD_SYNC = en.SEL_TH_NO_ENC
SPINDLE_SWITCH = False
SPINDLE_VAR_SPEED = False
HOME_IN_PLACE = False

cLoc = "../Lathe/include/"
fData = False

if SETUP:
    from interface import configList, strList, cmdList, parmList, \
        enumList, regList

    from setup import Setup
    setup = Setup()
    (config, configTable) = setup.createConfig(configList)

    setupCmd = "from setup import "
    for var in setup.configImports:
        setupCmd += var + ","
    exec(setupCmd[:-1])
    
    setup.createCommands(cmdList, cLoc, fData)
    setup.createStrings(strList)
    setup.createParameters(parmList, cLoc, fData)
    setup.createCtlBits(regList, cLoc, fData)
    setup.createEnums(enumList, cLoc, fData)
    if FPGA:
        xLoc = '../../Xilinx/LatheCtl/'
        from interface import xilinxList, xilinxBitList
        setup.createXilinxReg(xilinxList, cLoc, xLoc, fData)
        setup.createXilinxBits(xilinxBitList, cLoc, xLoc, fData)

    importList = setup.importList
    setupCmd = "from setup import "
    for var in importList:
        setupCmd += var + ","
    exec(setupCmd[:-1])

if SWIG:
    import lathe
    from lathe import taperCalc, T_ACCEL, zTaperInit, xTaperInit

print(sys.version)
print(wx.version())
stdout.flush()

cfg = None
comm = None
fcy = None
TEXT = None
REF = None
dro = None
eDro = None
EXT_DRO = None
EVT_UPDATE_ID = None
xDROOffset = None
zDROOffset = None
xDROPosition = None
zDROPosition = None
f = None
xSyncInt = None
zSyncInt = None
xSyncExt = None
zSyncExt = None
syncComm = None
mainFrame = None
updateThread = None
moveCommands = None
buttonRepeat = None
jogPanel = None
jogShuttle = None

spindleDataSent = False
zDataSent = False
xDataSent = False

zPosition = 0.0
zHomeOffset = 0.0
xPosition = 0.0
xHomeOffset = 0.0

xHomed = False
done = False

MAX_PRIME = 127
factor = None

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
    jogPanel.setStatus(st.STR_TIMEOUT_ERROR)

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

class Factor:
    def __init__(self, maxPrime):
        self.primes = self.calcPrimes(maxPrime)
        
    def remFactors(self, nFactors, dFactors):
        # print("remove common factors")
        dResult = []
        for d in dFactors:
            found = False
            # print("d %d" % (d))
            for (i, n) in enumerate(nFactors):
                if d == n:
                    # print("found %d at %d\n" % (d, i))
                    del nFactors[i]
                    found = True
                    break
            if not found:
                dResult.append(d)
        return(nFactors, dResult)

    def combineFactors(self, factors):
        result = 1
        for val in factors:
            result *= val
        return result

    def calcPrimes(self, maxPrime):
        maxPrime += 1
        sieve = [True] * maxPrime
        sieve[0] = False
        sieve[1] = False

        for i in range(2, int(math.sqrt(maxPrime)) + 1):
            index = i * 2
            while index < maxPrime:
                sieve[index] = False
                index += i

        primes = []
        for i in range(maxPrime):
            if sieve[i] == True:
                primes.append(i)
        return(primes)

    def factor(self, n):
        factors = []
        for i in self.primes:
            while n % i == 0:
                factors.append(i)
                n /= i
        return(factors)

class Offset():
    def __init__(self, scale):
        self.scale = scale
        self.val = None

    def intVal(self):
        return(self.val * self.scale)

class ComboBox(wx.ComboBox): 
    def __init__(self, parent, label, indexList,  choiceList, *args, **kwargs):
        self.label = label
        self.indexList = indexList
        self.choiceList = choiceList
        self.text = None
        super(ComboBox, self).__init__(parent, *args, **kwargs)

    def GetValue(self):
        val = self.GetCurrentSelection()
        rtnVal = self.indexList[val]
        if self.text is not None:
            print("%s GetValue %d %s index %d" % \
                  (self.label, rtnVal, self.text[val], val))
            print(self.indexList)
        return str(rtnVal)

    def SetValue(self, val):
        if isinstance(val, str):
            val = int(val)
        for (n, index) in enumerate(self.indexList):
            if val == index:
                self.SetSelection(n)
                if self.text is not None:
                    print("%s SetValue %d %s index %d" % \
                          (self.label, val, self.text[index], n))
                    print(self.indexList)
    
class FormRoutines():
    def __init__(self, panel=True):
        self.emptyCell = (0, 0)
        self.configList = None
        self.prefix = ""
        self.focusField = None
        self.formatList = None
        self.width = 60 if WINDOWS else 75

    def formatData(self, formatList):
        if formatList is None:
            return(True)
        success = True
        for fmt in formatList:
            if len(fmt) == 2:
                (index, fieldType) = fmt
            else:
                (name, index, fieldType) = fmt[:3]
            if fieldType is None:
                continue
            ctl = cfg.info[index]
            strVal = ctl.GetValue()
            if fieldType.startswith('f'):
                strip = False
                strVal = strVal.lower()
                metric = strVal.endswith('mm')
                if metric:
                    strVal = strVal[:-2]
                    strip = True
                if fieldType.endswith('s'):
                    fieldType = fieldType[:-1]
                    strip = True

                digits = 4
                if len(fieldType) > 1:
                    try:
                        digits = int(fieldType[1])
                    except ValueError:
                        pass
                if metric:
                    digits -= 2
                fmt = "%%0.%df" % digits

                try:
                    if len(strVal) != 0:
                        val = float(strVal)
                        val = fmt % (val)
                        if strip:
                            if re.search("\.0*$", val):
                                val = re.sub("\.0*$", "", val)
                            else:
                                val = val.rstrip('0')
                        if metric:
                            val += 'mm'
                            strVal += 'mm'
                        ctl.SetValue(val)
                except ValueError:
                    success = False
                    strVal = ''
                    ctl.SetValue('')
            elif fieldType == 'd':
                try:
                    if len(strVal) != 0:
                        val = int(strVal)
                        ctl.SetValue("%d" % (val))
                except ValueError:
                    success = False
                    strVal = ''
                    ctl.SetValue('')
            elif fieldType == 'c':
                pass
            cfg.setInfoData(index, strVal)
        return(success)

    def fieldList(self, sizer, fields):
        for field  in fields:
            (label, index) = field[:2]
            if label.startswith('b'):
                self.addCheckBox(sizer, label[1:], index)
            elif label.startswith('c'):
                action = field[3]
                self.addComboBox(sizer, label[1:], index, action) 
            elif label.startswith('w'):
                self.addField(sizer, label[1:], index, (80, -1))
            else:
                self.addField(sizer, label, index)

    def getConfigList(self):
        if self.configList is None:
            self.configList = []
            for i, name in enumerate(cf.configTable):
                if name.startswith(self.prefix):
                    self.configList.append(i)
        return(self.configList)

    def addFieldText(self, sizer, label, key, keyText=None):
        if len(label) != 0:
            txt = wx.StaticText(self, -1, label)
            sizer.Add(txt, flag=wx.ALL|wx.ALIGN_RIGHT|\
                      wx.ALIGN_CENTER_VERTICAL, border=2)
            if keyText is not None:
                cfg.initInfo(keyText, txt)

        tc = wx.TextCtrl(self, -1, "", size=(self.width, -1), \
                         style=wx.TE_PROCESS_ENTER)
        tc.Bind(wx.EVT_TEXT_ENTER, self.OnEnter)
        sizer.Add(tc, flag=wx.ALL, border=2)
        cfg.initInfo(key, tc)
        return(tc, txt)

    def addField(self, sizer, label, index, size=None):
        if size is None:
            size = (self.width, -1)
        if label is not None:
            txt = wx.StaticText(self, -1, label)
            sizer.Add(txt, flag=wx.ALL|wx.ALIGN_RIGHT|\
                      wx.ALIGN_CENTER_VERTICAL, border=2)

        tc = wx.TextCtrl(self, -1, "", size=size, \
                         style=wx.TE_PROCESS_ENTER)
        tc.Bind(wx.EVT_TEXT_ENTER, self.OnEnter)
        sizer.Add(tc, flag=wx.ALL, border=2)
        if cfg.info[index] is not None:
            val = cfg.getInfo(index)
            tc.SetValue(val)
        cfg.initInfo(index, tc)
        return(tc)

    def addCheckBox(self, sizer, label, index, action=None):
        txt = wx.StaticText(self, -1, label)
        sizer.Add(txt, flag=wx.ALL|wx.ALIGN_RIGHT|\
                  wx.ALIGN_CENTER_VERTICAL, border=2)

        cb = wx.CheckBox(self, -1, style=wx.ALIGN_LEFT)
        if action is not None:
            self.Bind(wx.EVT_CHECKBOX, action, cb)
        sizer.Add(cb, flag=wx.ALL|wx.ALIGN_CENTER_VERTICAL, border=2)
        if cfg.info[index] is not None:
            val = cfg.getInfo(index)
            cb.SetValue(val == 'True')
        cfg.initInfo(index, cb)
        return(cb)

    def addComboBox(self, sizer, label, index, action, border=2,
                    flag=wx.CENTER|wx.ALL):
        txt = wx.StaticText(self, -1, label)
        sizer.Add(txt, flag=wx.ALL|wx.ALIGN_RIGHT|\
                  wx.ALIGN_CENTER_VERTICAL, border=2)

        (indexList, choiceList, text) = action()
        combo = ComboBox(self, label, indexList, choiceList, \
                         id=-1, value=choiceList[0], choices=choiceList, \
                         style=wx.CB_READONLY)
        combo.text = text
        if cfg.info[index] is not None:
            val = cfg.getInfo(index)
            combo.SetValue(val)
        sizer.Add(combo, flag=flag, border=border)
        cfg.initInfo(index, combo)

    def addButton(self, sizer, label, action, size=(60, -1), border=2, \
                  style=0, flag=wx.CENTER|wx.ALL):
        btn = wx.Button(self, label=label, style=style, size=size)
        btn.Bind(wx.EVT_BUTTON, action)
        sizer.Add(btn, flag=flag, border=border)
        return(btn)

    def addControlButton(self, sizer, label, downAction, upAction, \
                         flag=wx.CENTER|wx.ALL):
        btn = wx.Button(self, label=label)
        btn.Bind(wx.EVT_LEFT_DOWN, downAction)
        btn.Bind(wx.EVT_LEFT_UP, upAction)
        sizer.Add(btn, flag=flag, border=2)
        return(btn)

    def addBitmapButton(self, sizer, bitmap, downAction, upAction, flag=0):
        bmp = wx.Bitmap(bitmap, wx.BITMAP_TYPE_ANY)
        btn = wx.BitmapButton(self, id=wx.ID_ANY, bitmap=bmp, \
                              size=(bmp.GetWidth()+10, bmp.GetHeight()+10))
        btn.Bind(wx.EVT_LEFT_DOWN, downAction)
        btn.Bind(wx.EVT_LEFT_UP, upAction)
        sizer.Add(btn, flag=flag, border=2)
        return(btn)

    def addDialogButton(self, sizer, idx, action=None, border=5):
        btn = wx.Button(self, idx)
        if action is None:
            btn.SetDefault()
        else:
            btn.Bind(wx.EVT_BUTTON, action)
        sizer.Add(btn, 0, wx.ALL|wx.CENTER, border=border)
        return(btn)

    def addRadioButton(self, sizer, label, key, style=0, action=None):
        btn = wx.RadioButton(self, label=label, style=style)
        if action is not None:
            btn.Bind(wx.EVT_RADIOBUTTON, action)
        sizer.Add(btn, flag=wx.ALIGN_CENTER_VERTICAL|wx.ALL, border=2)
        cfg.initInfo(key, btn)
        return(btn)

    def addDialogField(self, sizer, label=None, tcDefault="", textFont=None, \
                       tcFont=None, size=wx.DefaultSize, action=None, \
                       border=None, index=None, edit=True, text=False):
        if border is None:
            b0 = 10
            b1 = 10
        elif isinstance(border, tuple) or isinstance(border, list):
            b0 = border[0]
            b1 = border[1] if len(border) >= 2 else b0
        else:
            b0 = border
            b1 = border

        if label is not None:
            txt = wx.StaticText(self, -1, label)
            if textFont is not None:
                txt.SetFont(textFont)
            sizer.Add(txt, flag=wx.LEFT|wx.RIGHT|wx.ALIGN_RIGHT|\
                      wx.ALIGN_CENTER_VERTICAL, border=b0)

        tc = wx.TextCtrl(self, -1, tcDefault, size=size, \
                         style=wx.TE_RIGHT|wx.TE_PROCESS_ENTER)
        if tcFont is not None:
            tc.SetFont(tcFont)
        if action is not None:
            tc.Bind(wx.EVT_CHAR, action)
        if not edit:
            tc.SetEditable(False)
        if index is not None:
            cfg.initInfo(index, tc)
        sizer.Add(tc, flag=wx.CENTER|wx.ALL, border=b1)
        return(tc if not text else (tc, txt))

    def setFocus(self):
        field = self.focusField
        if field is not None:
            field.SetFocus()
            field.SetSelection(-1, -1)
            
    def setAddFocus(self):
        field = self.add
        if field is not None:
            field.SetFocus()
            field.SetSelection(-1, -1)

    def OnEnter(self, e):
        if self.formatList is None:
            return
        if self.formatData(self.formatList):
            jogPanel.setStatus(st.STR_CLR)
            jogPanel.focus()
        else:
            jogPanel.setStatus(st.STR_FIELD_ERROR)
            
class ActionRoutines():
    def __init__(self, control, op):
        self.control = control
        self.op = op
        self.active = False
        self.Bind(wx.EVT_SHOW, self.OnShow)
        self.safeX = None
        self.safeZ = None
        self.formatList = None

    def formatData(self, formatList):
        print("ActionRoutines formatData stub called")
        stdout.flush()
        return(True)

    def sendAction(self):
        print("ActionRoutines sendAction stub called")
        stdout.flush()
        return(False)

    def startAction(self):
        print("ActionRoutines startAction stub called")
        stdout.flush()

    def addAction(self):
        print("ActionRoutines addAction stub called")
        stdout.flush()

    def update(self):
        print("ActionRoutines update stub called")
        stdout.flush()

    def nextOperation(self):
        pass

    def getSafeLoc(self):
        control = self.control
        control.getParameters()
        self.safeX = control.xStart + control.xRetract
        self.safeZ = control.zStart + control.zRetract
        return(self.safeZ, self.safeX)

    def OnShow(self, e):
        if done:
            return
        # print("OnShow %s %d" % (str(self.IsShown()), self.op))
        if self.IsShown():
            jogPanel.currentPanel = self
            jogPanel.currentControl = self.control
            self.update()
        else:
            self.active = False

    def OnSend(self, e):
        if self.formatData(self.formatList):
            if not xHomed:
                jogPanel.setStatus(st.STR_NOT_HOMED)
            elif self.active or \
                 jogPanel.mvStatus & (ct.MV_ACTIVE | ct.MV_PAUSE):
                jogPanel.setStatus(st.STR_OP_IN_PROGRESS)
            else:
                jogPanel.setStatus(st.STR_CLR)
                try:
                    if callable(self.sendAction):
                        if self.sendAction():
                            self.active = True
                except CommTimeout:
                    commTimeout()
                except:
                    traceback.print_exc()
        else:
            jogPanel.setStatus(st.STR_FIELD_ERROR)
        jogPanel.focus()

    def OnStart(self, e):
        if not self.active:
            jogPanel.setStatus(st.STR_NOT_SENT)
        elif (jogPanel.mvStatus & ct.MV_PAUSE) == 0:
            jogPanel.setStatus(st.STR_NOT_PAUSED)
        else:
            jogPanel.setStatus(st.STR_CLR)
            try:
                if callable(self.startAction):
                    self.startAction()
            except CommTimeout:
                commTimeout()
            except AttributeError:
                print("ActionRoutines OnStart AttributeError")
                stdout.flush()
        jogPanel.focus()

    def OnAdd(self, e):
        if not self.active:
            jogPanel.setStatus(st.STR_OP_NOT_ACTIVE)
        elif jogPanel.mvStatus & (ct.MV_ACTIVE | ct.MV_PAUSE):
            jogPanel.setStatus(st.STR_OP_IN_PROGRESS)
        else:
            jogPanel.setStatus(st.STR_CLR)
            try:
                curPass = comm.getParm(pm.CURRENT_PASS)
                if curPass >= self.control.passes:
                    if callable(self.addAction):
                        self.addAction()
                else:
                    jogPanel.setStatus(st.STR_PASS_ERROR)
            except CommTimeout:
                commTimeout()
            except AttributeError:
                print("ActionRoutines OnAdd AttributeError")
                stdout.flush()
        jogPanel.focus()

class DialogActions():
    def __init__(self):
        self.fields = None
        self.fieldInfo = None
        self.sendData = False
        self.changed = False
        self.Bind(wx.EVT_SHOW, self.OnShow)

    def setupAction(self):
        print("DialogAction setupAction stub called")
        stdout.flush()

    def showAction(self, changed):
        print("DialogAction showAction stub called")
        stdout.flush()

    def formatData(self, fields):
        print("DialogAction formatData stub called")
        stdout.flush()

    def OnSetup(self, e):
        if not self.formatData(self.fields):
            return
        moveCommands.queClear()
        try:
            if callable(self.setupAction):
                self.setupAction()
        except AttributeError:
            print("Dialog OnSetup AttributeError")
            stdout.flush()

    def OnShow(self, e):
        if done:
            return
        changed = False
        if self.IsShown():
            self.formatData(self.fields)
            self.fieldInfo = {}
            for fmt in self.fields:
                (label, index) = fmt[:2]
                self.fieldInfo[index] = cfg.getInfo(index)
        else:
            for fmt in self.fields:
                (label, index) = fmt[:2]
                val = cfg.getInfo(index)
                if self.fieldInfo[index] != val:
                    cfg.setInfoData(index, val)
                    self.sendData = True
                    changed = True
        if changed:
            try:
                if callable(self.showAction):
                    self.showAction(changed)
            except AttributeError:
                print("Dialog OnShow AttributeError")
                stdout.flush()

    def OnOk(self, e):
        if self.formatData(self.fields):
            self.Show(False)

    def OnCancel(self, e):
        for field in self.fields:
            index = field[1]
            cfg.setInfo(index, self.fieldInfo[index])
        self.Show(False)

class MoveCommands():
    def __init__(self):
        if not R_PI:
            self.moveQue = Queue()
        else:
            self.moveQue = comm.rpi.moveQue
        self.passNum = 0
        self.send = False
        self.dbg = True
        self.zOffset = 0.0
        self.xOffset = 0.0

        self.d = None
        self.lastX = 0.0
        self.lastZ = 0.0
        self.textH = 0.005
        self.vS = self.textH / 2
        self.hS = self.textH
        self.textAngle = 0.0
        self.xText = None
        self.zText = None
        self.fileName = None
        self.style = None

    def draw(self, cmd, diam, parm):
        tmp = "%s%0.3f-%0.3f" % (cmd, diam, parm)
        tmp = tmp.replace(".", "-")
        tmp = re.sub("-0$", "", tmp) + ".dxf"
        self.fileName = os.path.join(DXF_DIR, tmp)
        if not os.path.exists(DXF_DIR):
            os.makedirs(DXF_DIR)
        d = dxf.drawing(self.fileName)
        self.style = dxf.style("CONSOLAS", font="Consolas.ttf")
        d.add_layer(TEXT, color=0)
        d.add_layer(REF, color=1)
        self.textAngle = 0.0
        self.d = d
        self.xText = []
        self.zText = []
        self.flip = -1

    def setTextAngle(self, textAngle):
        self.textAngle = textAngle

    def setLoc(self, z, x):
        if self.d is not None:
            self.lastX = x
            self.lastZ = z

    def addLine(self, p0, p1, layer=0):
        if self.d is not None:
            (p0X, p0Y) = p0
            (p1X, p1Y) = p1
            self.d.add(dxf.line((p0X, self.flip * p0Y), \
                                (p1X, self.flip * p1Y), layer=layer))
            
    def drawLineX(self, x, layer=0):
        if self.d is not None:
            self.d.add(dxf.line((self.lastZ, self.flip * self.lastX), \
                                (self.lastZ, self.flip * x), layer=layer))
            self.lastX = x

    def drawLineZ(self, z, layer=0):
        if self.d is not None:
            self.d.add(dxf.line((self.lastZ, self.flip * self.lastX), \
                                (z, self.flip * self.lastX), layer=layer))
            self.lastZ = z

    def drawLine(self, z, x, layer=0):
        if self.d is not None:
            self.d.add(dxf.line((self.lastZ, self.flip * self.lastX), \
                                (z, self.flip * x), layer=layer))
            self.lastX = x
            self.lastZ = z

    def saveXText(self, val, pos):
        if self.xText is not None:
            self.xText.append((val, pos))

    def printXText(self, fmt, align, internal):
        if self.xText is None:
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
        if self.zText is not None:
            self.zText.append((val, pos))

    def printZText(self, fmt, align):
        if self.zText is None:
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
        if self.d is not None:
            (x, y) = p0
            hOffset = self.hS
            vOffset = -self.textH / 2
            if align is not None:
                if align & CENTER:
                    text = text.strip()
                textW = len(text) * self.textH * 0.9
                if align & RIGHT:
                    hOffset = -(textW + self.hS)
                elif align & CENTER:
                    hOffset = -textW / 2
                elif align & LEFT:
                    hOffset = self.hS

                if self.flip == 1:
                    if align & ABOVE:
                        vOffset = self.vS
                    elif align & BELOW:
                        vOffset = -(self.textH + self.vS)
                    elif align & MIDDLE:
                        vOffset = -(self.textH / 2)
                else:
                    if align & ABOVE:
                        vOffset = -(self.textH + self.vS)
                    elif align & BELOW:
                        vOffset = self.vS
                    elif align & MIDDLE:
                        vOffset = -(self.textH / 2)

            if self.textAngle != 0.0:
                (vOffset, hOffset) = (hOffset, -vOffset)
            self.d.add(dxf.text(text, (x + hOffset, \
                                       self.flip * y + vOffset), \
                                height=self.textH, rotation=self.textAngle, \
                                layer=layer, style=self.style))

    def drawClose(self):
        if self.d is not None:
            try:
                self.d.save()
                fileName = self.fileName
                if WINDOWS:
                    fileName = fileName.replace("\\", "/")
                    fileName = fileName.replace("C:", "/cygdrive/c")
                    subprocess.call(["sed", "-i", "-e", \
                                     "'s/arial/consolas/g'", \
                                     fileName])
            except IOError:
                print("dxf file save error")
                # traceback.print_exc()
            self.fileName = None
            self.d = None

    def queInit(self):
        comm.sendMulti()        # send parameters first
        self.zOffset = None
        self.xOffset = None

    def queMove(self, op, val):
        if self.send:
            opString = en.mCommandsList[op]
            self.moveQue.put((opString, op, val))

    def queMoveF(self, op, flag, val):
        if self.send:
            opString = en.mCommandsList[op]
            op |= (flag << 16)
            self.moveQue.put((opString, op, val))

    def queClear(self):
        self.send = not cfg.getBoolInfoData(cf.cfgCmdDis)
        while not self.moveQue.empty():
            self.moveQue.get()
        self.queInit()

    def queZSetup(self, feed):
        self.queMove(en.Z_FEED_SETUP, feed)
        self.saveZOffset()
        self.saveXOffset()

    def queXSetup(self, feed):
        self.queMove(en.X_FEED_SETUP, feed)
        self.saveZOffset()
        self.saveXOffset()

    def startSpindle(self, rpm):
        self.queMove(en.START_SPINDLE, rpm)
        self.saveZOffset()
        self.saveXOffset()

    def stopSpindle(self):
        self.queMove(en.STOP_SPINDLE, 0)

    def queFeedType(self, feedType):
        self.queMove(en.SAVE_FEED_TYPE, feedType)

    def zSynSetup(self, feed):
        self.queMove(en.Z_SYN_SETUP, feed)

    def xSynSetup(self, feed):
        self.queMove(en.X_SYN_SETUP, feed)

    def nextPass(self, passNum):
        self.passNum = passNum
        self.queMove(en.PASS_NUM, passNum)
        if self.dbg:
            if passNum & 0x100:
                print("spring\n")
            elif passNum & 0x200:
                print("spring %d" % (passNum & 0xff))
            else:
                print("pass %d" % (passNum))

    def quePause(self, val=0):
        self.queMove(en.QUE_PAUSE, val)

    def moveZOffset(self):
        self.queMove(en.MOVE_Z_OFFSET, 0)

    def moveZ(self, zLocation, flag=ct.CMD_MAX, backlash=0.0):
        self.queMoveF(en.MOVE_Z, flag, zLocation + backlash)
        self.drawLineZ(zLocation)
        if self.dbg:
            print("moveZ   %7.4f" % (zLocation))
            stdout.flush()

    def moveX(self, xLocation, flag=ct.CMD_MAX, backlash=0.0):
        if (flag & ct.DRO_POS) == 0:
            val = round((xLocation + backlash) * jogPanel.xStepsInch)
        else:
            val = round((xLocation + backlash) * jogPanel.xDROInch)
        self.queMoveF(en.MOVE_X, flag, val)
        self.drawLineX(xLocation)
        if self.dbg:
            print("moveX   %7.4f" % (xLocation))
            stdout.flush()

    def saveZOffset(self):
        if self.zOffset != zHomeOffset:
            self.zOffset = zHomeOffset
            # zHomeOffset floating, zHomeOffset sent as integer
            self.queMove(en.SAVE_Z_OFFSET,
                         round(zHomeOffset * jogPanel.zStepsInch))
            if self.dbg:
                print("saveZOffset  %7.4f" % (zHomeOffset))
                stdout.flush()

    def saveXOffset(self):
        if self.xOffset != xHomeOffset:
            self.xOffset = xHomeOffset
            # xHomeOffset floating, xHomeOffset sent as integer
            self.queMove(en.SAVE_X_OFFSET,
                         round(xHomeOffset * jogPanel.xStepsInch))
            if self.dbg:
                print("savexOffset  %7.4f" % (xHomeOffset))
                stdout.flush()

    def moveXZ(self, zLocation, xLocation):
        self.queMove(en.SAVE_Z, zLocation)
        self.queMove(en.MOVE_XZ, xLocation)
        if self.dbg:
            print("moveZX %7.4f %7.4f" % (zLocation, xLocation))

    def moveZX(self, zLocation, xLocation):
        self.queMove(en.SAVE_X, xLocation)
        self.queMove(en.MOVE_ZX, zLocation)
        if self.dbg:
            print("moveXZ %7.4f %7.4f" % (zLocation, xLocation))

    def saveTaper(self, taper):
        if not R_PI:
            taper = "%0.6f" % (taper)
        self.queMove(en.SAVE_TAPER, taper)
        if self.dbg:
            print("saveTaper %s" % (taper))

    def saveThreadFlags(self, flags):
        self.queMove(en.SAVE_FLAGS, flags)
        if self.dbg:
            print("saveThreadFlags %02x" % (flags))

    def taperZX(self, zLocation, xLocation):
        self.queMove(en.SAVE_X, xLocation)
        self.queMoveF(en.TAPER_ZX, 1, zLocation)
        if self.dbg:
            print("taperZX %7.4f" % (zLocation))

    def taperXZ(self, xLocation, zLocation):
        self.queMove(en.SAVE_Z, zLocation)
        self.queMoveF(en.TAPER_XZ, 1, xLocation)
        if self.dbg:
            print("taperXZ %7.4f" % (xLocation))

    def probeZ(self, zDist):
        self.queMove(en.PROBE_Z, zDist)
        if self.dbg:
            print("probeZ %7.4f" % (zDist))

    def probeX(self, xDist):
        self.queMove(en.PROBE_X, xDist)
        if self.dbg:
            print("probeX %7.4f" % (xDist))

    def saveZDro(self):
        self.queMove(en.SAVE_Z_DRO, 0)

    def saveXDro(self):
        self.queMove(en.SAVE_X_DRO, 0)

    def done(self, parm):
        self.queMove(en.OP_DONE, parm)

def sendClear():
    global spindleDataSent, zDataSent, xDataSent
    try:
        comm.command(cm.CLRDBG)
        comm.command(cm.CMD_CLEAR)
    except CommTimeout:
        commTimeout()
    spindleDataSent = False
    zDataSent = False
    xDataSent = False

def xilinxTestMode():
    testMode = False
    try:
        testMode = cfg.getBoolInfoData(cf.cfgTestMode)
    except KeyError:
        testMode = False
    if testMode:
        encoder = 0
        try:
            encoder = cfg.getIntInfoData(cf.cfgEncoder)
        except KeyError:
            encoder = 0
        rpm = 0
        try:
            rpm = int(cfg.getFloatInfoData(cf.cfgTestRPM))
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
            comm.queParm(pm.ENC_ENABLE, '1')
            comm.queParm(pm.ENC_PRE_SCALER, preScaler)
            comm.queParm(pm.ENC_TIMER, encTimer)
    else:
        comm.queParm(pm.ENC_ENABLE, '0')

def sendSpindleData(send=False, rpm=None):
    global spindleDataSent
    queParm = comm.queParm
    try:
        if send or (not spindleDataSent):
            queParm(pm.STEPPER_DRIVE, cfg.getBoolInfoData(cf.spStepDrive))
            queParm(pm.MOTOR_TEST, cfg.getBoolInfoData(cf.spMotorTest))
            queParm(pm.SPINDLE_ENCODER, cfg.getBoolInfoData(cf.cfgSpEncoder))
            queParm(pm.SPINDLE_SYNC_BOARD, \
                    cfg.getBoolInfoData(cf.cfgSpSyncBoard))
            queParm(pm.TURN_SYNC, cfg.getInfoData(cf.cfgTurnSync))
            queParm(pm.THREAD_SYNC, cfg.getInfoData(cf.cfgThreadSync))
            if STEP_DRV or MOTOR_TEST:
                queParm(pm.SP_STEPS, cfg.getInfoData(cf.spMotorSteps))
                queParm(pm.SP_MICRO, cfg.getInfoData(cf.spMicroSteps))
                queParm(pm.SP_MIN_RPM, cfg.getInfoData(cf.spMinRPM))
                # if rpm is not None:
                #     queParm(pm.SP_MAX_RPM, rpm)
                # else:
                #     queParm(pm.SP_MAX_RPM, cfg.getInfoData(cf.spMaxRPM))

                queParm(pm.SP_ACCEL, cfg.getInfoData(cf.spAccel))
                queParm(pm.SP_JOG_MIN_RPM, cfg.getInfoData(cf.spJogMin))
                queParm(pm.SP_JOG_MAX_RPM, cfg.getInfoData(cf.spJogMax))

                queParm(pm.SP_JOG_TIME_INITIAL, \
                        cfg.getInfoData(cf.spJTimeInitial))
                queParm(pm.SP_JOG_TIME_INC, cfg.getInfoData(cf.spJTimeInc))
                queParm(pm.SP_JOG_TIME_MAX, cfg.getInfoData(cf.spJTimeMax))

                queParm(pm.SP_DIR_FLAG, cfg.getBoolInfoData(cf.spInvDir))
                queParm(pm.SP_TEST_INDEX, \
                        cfg.getBoolInfoData(cf.spTestIndex))
                count = (cfg.getIntInfoData(cf.spMotorSteps) * \
                         cfg.getIntInfoData(cf.spMicroSteps))
                queParm(pm.ENC_PER_REV, count)
                updateThread.encoderCount = count
                if MOTOR_TEST and SPINDLE_ENCODER:
                    queParm(pm.SP_TEST_ENCODER, \
                            cfg.getBoolInfoData(cf.spTestEncoder))
            elif FPGA:
                queParm(pm.ENC_PER_REV, cfg.getInfoData(cf.cfgEncoder))
                queParm(pm.FPGA_FREQUENCY, cfg.getInfoData(cf.cfgFpgaFreq))
                # queParm(pm.FREQ_MULT, cfg.getInfoData(cf.cfgFreqMult))
                queParm(pm.FREQ_MULT, 8)
                xilinxTestMode()
                queParm(pm.RPM, cfg.getInfoData(cf.cfgTestRPM))
                print(R_PI)
                if not R_PI:
                    cfgReg = 0
                    if cfg.getBoolInfoData(cf.cfgInvEncDir):
                        cfgReg |= xb.ENC_POL
                    if cfg.getBoolInfoData(cf.zInvDir):
                        cfgReg |= xb.ZDIR_POL
                    if cfg.getBoolInfoData(cf.xInvDir):
                        cfgReg |= xb.XDIR_POL
                    queParm(pm.X_CFG_REG, cfgReg)
                else:
                    pass
                comm.sendMulti()
            elif SPINDLE_ENCODER:
                count = cfg.getIntInfoData(cf.cfgEncoder)
                if zSyncExt is not None:
                    zSyncExt.setEncoder(count)
                if xSyncExt is not None:
                    xSyncExt.setEncoder(count)
                if zSyncInt is not None:
                    zSyncInt.setEncoder(count)
                if xSyncInt is not None:
                    xSyncInt.setEncoder(count)
                queParm(pm.ENC_PER_REV, count)
                updateThread.encoderCount = count

            if SPINDLE_VAR_SPEED:
                queParm(pm.PWM_FREQ, cfg.getIntInfoData(cf.spPWMFreq))
                range = cfg.getIntInfoData(cf.spCurRange)
                if range >= 1 and range <= cfg.getIntInfoData(cf.spRanges):
                    range -= 1
                    queParm(pm.MIN_SPEED, \
                            cfg.getIntInfoData(cf.spRangeMin1 + range))
                    queParm(pm.MAX_SPEED, \
                            cfg.getIntInfoData(cf.spRangeMax1 + range))
                else:
                    queParm(pm.MIN_SPEED, 0)
                    queParm(pm.MAX_SPEED, 0)
            if STEP_DRV or MOTOR_TEST or SPINDLE_VAR_SPEED:
                if rpm is not None:
                    queParm(pm.SP_MAX_RPM, rpm)
                else:
                    queParm(pm.SP_MAX_RPM, cfg.getInfoData(cf.spMaxRPM))

            comm.command(cm.CMD_SPSETUP)
            spindleDataSent = True
    except CommTimeout:
        commTimeout()

def sendZData(send=False):
    global zDataSent
    queParm = comm.queParm
    try:
        pitch = cfg.getDistInfoData(cf.zPitch)
        motorSteps = cfg.getIntInfoData(cf.zMotorSteps)
        microSteps = cfg.getIntInfoData(cf.zMicroSteps)
        motorRatio = cfg.getFloatInfoData(cf.zMotorRatio)
        jogPanel.zStepsInch = stepsInch = (microSteps * motorSteps * \
                                           motorRatio) / pitch

        if zSyncInt is not None:
            zSyncInt.setLeadscrew(cfg.getInfoData(cf.zPitch))
            zSyncInt.setMotorSteps(motorSteps)
            zSyncInt.setMicroSteps(microSteps)
            if not FPGA:
                zSyncInt.setClockFreq(cfg.getIntInfoData(cf.cfgFcy))
            else:
                zSyncInt.setClockFreq(cfg.getIntInfoData(cf.cfgFpgaFreq))

        if zSyncExt is not None:
            zSyncExt.setLeadscrew(cfg.getInfoData(cf.zPitch))
            zSyncExt.setMotorSteps(motorSteps)
            zSyncExt.setMicroSteps(microSteps)
                       
        if DRO:
            jogPanel.zDROInch = cfg.getIntInfoData(cf.zDROInch)

        # print("zStepsInch %0.2f" % (jogPanel.zStepsInch))
        # stdout.flush()

        if send or (not zDataSent):
            if DRO:
                queParm(pm.Z_DRO_COUNT_INCH, jogPanel.zDROInch)
                queParm(pm.Z_DRO_INVERT, cfg.getBoolInfoData(cf.zInvDRO))
                queParm(pm.Z_USE_DRO, cfg.getBoolInfoData(cf.zDROPos))

            val = jogPanel.combo.GetValue()
            try:
                val = float(val)
                if val > 0.020:
                    val = 0.020
            except ValueError:
                # val = cfg.getFloatInfoData(cf.zMpgInc)
                val = 0
            queParm(pm.Z_MPG_INC, round(val * stepsInch))
            queParm(pm.Z_MPG_MAX, \
                    round(cfg.getFloatInfoData(cf.zMpgMax) * stepsInch))

            queParm(pm.Z_PITCH, cfg.getDistInfoData(cf.zPitch, 6))
            queParm(pm.Z_RATIO, cfg.getInfoData(cf.zMotorRatio))
            queParm(pm.Z_MICRO, cfg.getInfoData(cf.zMicroSteps))
            queParm(pm.Z_MOTOR, cfg.getInfoData(cf.zMotorSteps))
            queParm(pm.Z_ACCEL, cfg.getInfoData(cf.zAccel))
            queParm(pm.Z_BACKLASH, cfg.getInfoData(cf.zBacklash))

            queParm(pm.Z_MOVE_MIN, cfg.getInfoData(cf.zMinSpeed))
            queParm(pm.Z_MOVE_MAX, cfg.getInfoData(cf.zMaxSpeed))

            queParm(pm.Z_JOG_MIN, cfg.getInfoData(cf.zJogMin))
            queParm(pm.Z_JOG_MAX, cfg.getInfoData(cf.zJogMax))

            queParm(pm.JOG_TIME_INITIAL,\
                         cfg.getFloatInfoData(cf.jogTimeInitial))
            queParm(pm.JOG_TIME_INC, cfg.getFloatInfoData(cf.jogTimeInc))
            queParm(pm.JOG_TIME_MAX, cfg.getFloatInfoData(cf.jogTimeMax))

            queParm(pm.Z_DIR_FLAG, cfg.getBoolInfoData(cf.zInvDir))
            queParm(pm.Z_MPG_FLAG, cfg.getBoolInfoData(cf.zInvMpg))

            queParm(pm.JOG_DEBUG, cfg.getBoolInfoData(cf.cfgJogDebug))

            comm.command(cm.CMD_ZSETUP)

            zDataSent = True
    except CommTimeout:
        commTimeout()
    except:
        print("setZData exception")
        stdout.flush()
        traceback.print_exc()

def sendXData(send=False):
    global xDataSent
    queParm = comm.queParm
    try:
        pitch = cfg.getDistInfoData(cf.xPitch)
        motorSteps = cfg.getIntInfoData(cf.xMotorSteps)
        microSteps = cfg.getIntInfoData(cf.xMicroSteps)
        motorRatio = cfg.getFloatInfoData(cf.xMotorRatio)
        if motorRatio == 0:
            motorRatio = 1
        jogPanel.xStepsInch = stepsInch = (microSteps * motorSteps * \
                                           motorRatio) / pitch

        if xSyncInt is not None:
            xSyncInt.setLeadscrew(cfg.getInfoData(cf.xPitch))
            xSyncInt.setMotorSteps(motorSteps)
            xSyncInt.setMicroSteps(microSteps)
            if not FPGA:
                xSyncInt.setClockFreq(cfg.getIntInfoData(cf.cfgFcy))
            else:
                xSyncInt.setClockFreq(cfg.getIntInfoData(cf.cfgFpgaFreq))

        if xSyncExt is not None:
            xSyncExt.setLeadscrew(cfg.getInfoData(cf.xPitch))
            xSyncExt.setMotorSteps(motorSteps)
            xSyncExt.setMicroSteps(microSteps)

        if DRO:
            jogPanel.xDROInch = droInch = cfg.getIntInfoData(cf.xDROInch)

        # print("xStepsInch %0.2f" % (jogPanel.xStepsInch))
        # stdout.flush()

        if send or (not xDataSent):
            if DRO:
                queParm(pm.X_DRO_COUNT_INCH, jogPanel.xDROInch)
                queParm(pm.X_DRO_INVERT, cfg.getBoolInfoData(cf.xInvDRO))
                queParm(pm.X_USE_DRO, cfg.getBoolInfoData(cf.xDROPos))
                queParm(pm.X_DONE_DELAY, cfg.getIntInfoData(cf.xDoneDelay))
                queParm(pm.X_DRO_FINAL_DIST,
                        round(cfg.getFloatInfoData(cf.xDroFinalDist) * \
                              droInch))
                stepF = factor.factor(stepsInch)
                droF = factor.factor(droInch)
                (stepF, droF) = factor.remFactors(stepF, droF)
                stepFactor = factor.combineFactors(stepF)
                droFactor = factor.combineFactors(droF)
                queParm(pm.X_STEP_FACTOR, stepFactor)
                queParm(pm.X_DRO_FACTOR, droFactor)
            else:
                queParm(pm.X_DONE_DELAY, 0)

            val = jogPanel.combo.GetValue()
            try:
                val = float(val)
                if val > 0.020:
                    val = 0.020
            except ValueError:
                # val = cfg.getFloatInfoData(cf.xMpgInc)
                val = 0
            queParm(pm.X_MPG_INC, round(val * stepsInch))
            queParm(pm.X_MPG_MAX, \
                    round(cfg.getFloatInfoData(cf.xMpgMax) * stepsInch))

            queParm(pm.X_PITCH, cfg.getDistInfoData(cf.xPitch, 6))
            queParm(pm.X_RATIO, cfg.getInfoData(cf.xMotorRatio))
            queParm(pm.X_MICRO, cfg.getInfoData(cf.xMicroSteps))
            queParm(pm.X_MOTOR, cfg.getInfoData(cf.xMotorSteps))
            queParm(pm.X_ACCEL, cfg.getInfoData(cf.xAccel))
            queParm(pm.X_BACKLASH, cfg.getInfoData(cf.xBacklash))

            queParm(pm.X_MOVE_MIN, cfg.getInfoData(cf.xMinSpeed))
            queParm(pm.X_MOVE_MAX, cfg.getInfoData(cf.xMaxSpeed))

            queParm(pm.X_JOG_MIN, cfg.getInfoData(cf.xJogMin))
            queParm(pm.X_JOG_MAX, cfg.getInfoData(cf.xJogMax))

            queParm(pm.JOG_TIME_INITIAL,\
                         cfg.getFloatInfoData(cf.jogTimeInitial))
            queParm(pm.JOG_TIME_INC, cfg.getFloatInfoData(cf.jogTimeInc))
            queParm(pm.JOG_TIME_MAX, cfg.getFloatInfoData(cf.jogTimeMax))

            queParm(pm.X_DIR_FLAG, cfg.getBoolInfoData(cf.xInvDir))
            queParm(pm.X_MPG_FLAG, cfg.getBoolInfoData(cf.xInvMpg))

            queParm(pm.JOG_DEBUG, cfg.getBoolInfoData(cf.cfgJogDebug))

            if HOME_TEST:
                stepsInch = jogPanel.xStepsInch
                start = str(int(cfg.getFloatInfoData(cf.xHomeStart) * \
                                stepsInch))
                end = str(int(cfg.getFloatInfoData(cf.xHomeEnd) * stepsInch))
                if end > start:
                    (start, end) = (end, start)
                queParm(pm.X_HOME_START, start)
                queParm(pm.X_HOME_END, end)

            comm.command(cm.CMD_XSETUP)
            xDataSent = True
    except CommTimeout:
        commTimeout()

class LatheOp():
    def __init__(self, panel):
        self.panel = panel
        self.m = moveCommands
        self.zStart = 0.0
        self.zEnd = 0.0
        self.zFeed = 0.0
        self.zRetract = 0.0

        self.xStart = 0.0
        self.xEnd = 0.0
        self.xFeed = 0.0
        self.xRetract = 0.0

        self.safeX = 0.0
        self.safeZ = 0.0

class UpdatePass():
    def __init__(self):
        self.calcPassN = None    # calculate values for a pass
        self.runPassN = None     # run a pass with current values

        self.add = False
        self.passes = 0
        self.passCount = 0
        self.passSize = [0.0, ]

        self.springFlag = False
        self.sPassInt = 0
        self.sPasses = 0
        self.sPassCtr = 0
        self.spring = 0

        self.cutAmount = 0.0
        self.feed = 0.0
        self.actualFeed = 0.0

        self.pause = False

    def calcFeed(self, feed, cutAmount, finish=0):
        self.add = False
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

    def setupAction(self, calcPass, runpass):
        self.calcPassN = calcPass
        self.runpassN = runpass

    def initPass(self):
        comm.setParm(pm.TOTAL_PASSES, self.passes)
        self.passSize = [None for i in range(self.passes + 1)]
        self.passSize[0] = 0.0
        self.passCount = 0
        self.sPassCtr = 0
        self.spring = 0
        self.feed = 0.0
        self.springFlag = False
        self.lastPass = False
        self.pause = self.panel.pause.GetValue()

    def updatePass(self):
        if (self.passCount < self.passes) or self.springFlag:
            if self.springFlag:
                self.springFlag = False
                moveCommands.nextPass(0x100 | self.passCount)
                self.runpassN()
            else:
                self.passCount += 1
                moveCommands.nextPass(self.passCount)
                self.calcPassN(self.passCount == self.passes)
                self.lastPass = self.passCount == self.passes and \
                                self.sPasses == 0
                # print("passCount %d lastPass %s" % \
                #       (self.passCount, self.lastPass))
                self.runpassN()
                if self.sPassInt != 0:
                    self.sPassCtr += 1
                    if self.sPassCtr >= self.sPassInt:
                        self.sPassCtr = 0
                        if (self.passCount != self.passes) or \
                           (self.sPasses == 0):
                            self.springFlag = True
                        else:
                            return(True)
        else:
            if self.spring < self.sPasses:
                self.spring += 1
                moveCommands.nextPass(0x200 | self.spring)
                self.lastPass = self.spring == self.sPasses
                # print("spring %d lastPass %s" % \
                #       (self.spring, self.lastPass))
                self.runpassN()
            else:
                return(False)
        # print("updatePass %d %s" % (self.passCount, self.springFlag))
        return(True)

    def passDone(self):
        m = self.m
        m.drawClose()
        if STEP_DRV or MOTOR_TEST or SPINDLE_SWITCH:
            m.stopSpindle()
        m.done(ct.PARM_DONE)
        stdout.flush()

    def addInit(self, label):
        jogPanel.dPrt("\n%s addPass\n" % (label))
        self.pause = self.panel.pause.GetValue()
        self.add = True
        add = getFloatVal(self.panel.add)
        if add != 0.0:
            self.panel.add.SetValue("0.0000")
        else:
            self.pause = True
        return(add)

    def addDone(self):
        m = self.m
        if STEP_DRV or MOTOR_TEST or SPINDLE_SWITCH:
            m.stopSpindle()
        m.done(ct.PARM_DONE)
        comm.command(cm.CMD_RESUME)

    def fixCut(self, offset=0.0):
        pass

class Turn(LatheOp, UpdatePass):
    def __init__(self, turnPanel):
        LatheOp.__init__(self, turnPanel)
        UpdatePass.__init__(self)
        self.xCut = 0.0
        self.curX = 0.0
        self.internal = False
        self.neg = False

    def getParameters(self):
        tu = self.panel
        self.internal = tu.internal.GetValue()

        if self.internal:
            self.xStart = getFloatVal(tu.xDiam1) / 2.0
            self.xEnd = getFloatVal(tu.xDiam0) / 2.0
        else:
            self.xStart = getFloatVal(tu.xDiam0) / 2.0
            self.xEnd = getFloatVal(tu.xDiam1) / 2.0
        self.xFeed = abs(getFloatVal(tu.xFeed) / 2.0)
        self.xRetract = abs(getFloatVal(tu.xRetract))

        self.zStart = getFloatVal(tu.zStart)
        self.zEnd = getFloatVal(tu.zEnd)
        self.zRetract = getFloatVal(tu.zRetract)

        val = getFloatVal(tu.zFeed)
        rpm = getIntVal(tu.rpm)
        if TURN_SYNC == en.SEL_TU_ISYN or TURN_SYNC == en.SEL_TU_SYN:
            (self.cycle, self.output, self.preScaler) = \
                zSyncInt.calcSync(val, metric=False, rpm=rpm, turn=True)
        elif TURN_SYNC == en.SEL_TU_ESYN:
            (self.cycle, self.output, self.preScaler) = \
                zSyncExt.calcSync(val, metric=False, rpm=rpm, turn=True)

    def runOperation(self):
        self.getParameters()

        if self.xStart < 0:
            if self.xEnd <= 0:
                self.neg = True
            else:
                jogPanel.setStatus(st.STR_SIGN_ERROR)
                return(False)
        else:
            if self.xEnd >= 0:
                self.neg = False
            else:
                jogPanel.setStatus(st.STR_SIGN_ERROR)
                return(False)

        self.xCut = abs(self.xStart) - abs(self.xEnd)
        if self.internal:
            if self.xCut > 0:
                jogPanel.setStatus(st.STR_INTERNAL_ERROR)
                return(False)
        else:
            if self.xCut < 0:
                jogPanel.setStatus(st.STR_EXTERNAL_ERROR)
                return(False)
        self.xCut = abs(self.xCut)

        self.calcFeed(self.xFeed, self.xCut)
        self.setupSpringPasses(self.panel)
        self.setupAction(self.calcPass, self.runPass)

        self.panel.passes.SetValue("%d" % (self.passes))
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

        if cfg.getBoolInfoData(cf.cfgDraw):
            self.m.draw("turn", self.zStart, self.zEnd)

        jogPanel.dPrt("\nturn runOperation\n")
        self.setup()

        while self.updatePass():
            pass

        self.m.moveX(self.xStart + self.xRetract)

        self.passDone()
        return(True)

    def setup(self, add=False): # turn
        comm.queParm(pm.CURRENT_OP, en.OP_TURN)
        m = self.m
        if not add:
            m.setLoc(self.zEnd, self.xStart)
            m.drawLineZ(self.zStart, REF)
            m.drawLineX(self.xEnd, REF)
            m.setLoc(self.safeZ, self.safeX)

            if TURN_SYNC == en.SEL_TU_ISYN or TURN_SYNC == en.SEL_TU_SYN:
                comm.queParm(pm.L_SYNC_CYCLE, self.cycle)
                comm.queParm(pm.L_SYNC_OUTPUT, self.output)
                comm.queParm(pm.L_SYNC_PRESCALER, self.preScaler)
            elif TURN_SYNC == en.SEL_TU_ESYN:
                syncComm.setParm(sp.SYNC_ENCODER, \
                                 cfg.getIntInfoData(cf.cfgEncoder))
                syncComm.setParm(sp.SYNC_CYCLE, self.cycle)
                syncComm.setParm(sp.SYNC_OUTPUT, self.output)
                syncComm.setParm(sp.SYNC_PRESCALER, self.preScaler)
                syncComm.command(sc.SYNC_SETUP)

        m.queInit()
        if (not add) or (add and not self.pause):
            m.quePause()
        m.done(ct.PARM_START)

        comm.command(cm.CMD_SYNCSETUP)
        
        m.startSpindle(cfg.getIntInfoData(cf.tuRPM))

        m.queFeedType(ct.FEED_PITCH)
        m.zSynSetup(cfg.getFloatInfoData(cf.tuZFeed))
            
        m.moveX(self.safeX)
        m.moveZ(self.safeZ)
        
        if not add:
            m.text("%7.3f" % (self.xStart * 2.0), \
                   (self.safeZ, self.xStart))
            m.text("%7.3f" % (self.zStart), \
                   (self.zStart, self.xEnd), \
                   CENTER | (ABOVE if self.internal else BELOW))
            m.text("%7.3f %6.3f" % (self.safeX * 2.0, self.actualFeed), \
                   (self.safeZ, self.safeX))
            m.text("%7.3f" % (self.zEnd), \
                   (self.zEnd, self.safeX), CENTER)

    def calcPass(self, final=False):
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
        self.passSize[self.passCount] = self.curX * 2.0
        jogPanel.dPrt("pass %2d feed %5.3f x %5.3f diameter %5.3f\n" % \
                      (self.passCount, feed, self.curX, self.curX * 2.0), \
                      True, True)

    def runPass(self, addPass=False): # turn
        m = self.m
        flag = ct.CMD_MOV | ((ct.DRO_POS | ct.DRO_UPD) if X_DRO_POS else 0)
        m.moveX(self.curX, flag)
        if DRO:
            m.saveXDro()
        if self.pause:
            flag = (ct.PAUSE_ENA_X_JOG | ct.PAUSE_READ_X) if addPass else 0
            m.quePause(flag)
        if not addPass:
            if m.passNum & 0x300 == 0:
                m.text("%2d %7.3f" % (m.passNum, self.curX * 2.0), \
                       (self.safeZ, self.curX))
        m.moveZ(self.zStart)
        m.moveZ(self.zEnd, ct.CMD_SYN)
        if DRO:
            m.saveZDro()
        if not addPass:
            if m.passNum & 0x300 == 0:
                m.text("%2d %7.3f" % (m.passNum, self.safeX * 2.0), \
                       (self.zEnd, self.safeX), RIGHT)
        m.moveX(self.safeX)
        m.moveZ(self.safeZ)

    def addPass(self):
        add = self.addInit("turn") / 2.0
        self.cutAmount += add
        self.setup(True)
        self.calcPass(True)
        moveCommands.nextPass(self.passCount)
        self.runPass(True)
        self.m.moveX(self.xStart + self.xRetract)
        self.addDone()

    def fixCut(self, offset=0.0): # turn
        passNum = jogPanel.lastPass
        if offset == 0.0:
            actual = float(jogPanel.xPos.GetValue())
            self.passSize[passNum] = 2 * actual
            if self.internal:
                self.cutAmount = actual - self.xStart
            else:
                self.cutAmount = self.xStart - actual
        else:
            self.passSize[passNum] += offset

class TurnPanel(wx.Panel, FormRoutines, ActionRoutines):
    def __init__(self, parent, hdrFont, *args, **kwargs):
        super(TurnPanel, self).__init__(parent, *args, **kwargs)
        self.hdrFont = hdrFont
        FormRoutines.__init__(self)
        ActionRoutines.__init__(self, Turn(self), en.OP_TURN)
        self.InitUI()
        self.configList = None
        self.prefix = 'tu'
        self.formatList = ((cf.tuAddFeed, 'f'), \
                           (cf.tuInternal, None), \
                           (cf.tuPasses, 'd'), \
                           (cf.tuPause, None), \
                           (cf.tuRPM, 'd'), \
                           (cf.tuSPInt, 'd'), \
                           (cf.tuSpring, 'd'), \
                           (cf.tuXDiam0, 'f'), \
                           (cf.tuXDiam1, 'f'), \
                           (cf.tuXFeed, 'f'), \
                           (cf.tuXRetract, 'f'), \
                           (cf.tuZEnd, 'f'), \
                           (cf.tuZFeed, 'f'), \
                           (cf.tuZRetract, 'f'), \
                           (cf.tuZStart, 'f'))

    def InitUI(self):
        self.sizerV = sizerV = wx.BoxSizer(wx.VERTICAL)

        txt = wx.StaticText(self, -1, "Turn", size=(120, 30))
        txt.SetFont(self.hdrFont)

        sizerV.Add(txt, flag=wx.CENTER|wx.ALL, border=2)

        sizerG = wx.FlexGridSizer(cols=8, rows=0, vgap=0, hgap=0)

        # x parameters

        (self.xDiam0, self.diam0Txt) = \
            self.addFieldText(sizerG, "X Start D", cf.tuXDiam0)
        self.focusField = self.xDiam0

        (self.xDiam1, self.diam1Txt) = \
            self.addFieldText(sizerG, "X End D", cf.tuXDiam1)

        self.xFeed = self.addField(sizerG, "X Feed D", cf.tuXFeed)

        self.xRetract = self.addField(sizerG, "X Retract", cf.tuXRetract)

        # z parameters

        self.zEnd = self.addField(sizerG, "Z End", cf.tuZEnd)

        self.zStart = self.addField(sizerG, "Z Start", cf.tuZStart)

        self.zFeed = self.addField(sizerG, "Z Feed", cf.tuZFeed)

        self.zRetract = self.addField(sizerG, "Z Retract", cf.tuZRetract)

        # pass info

        self.passes = self.addField(sizerG, "Passes", cf.tuPasses)
        self.passes.SetEditable(False)

        self.sPInt = self.addField(sizerG, "SP Int", cf.tuSPInt)

        self.spring = self.addField(sizerG, "Spring", cf.tuSpring)

        self.internal = self.addCheckBox(sizerG, "Internal", cf.tuInternal, \
                                         self.OnInternal)
        
        # buttons

        self.addButton(sizerG, 'Send', self.OnSend)

        self.addButton(sizerG, 'Start', self.OnStart)

        self.addButton(sizerG, 'Add', self.OnAdd)

        self.add = self.addField(sizerG, None, cf.tuAddFeed)

        self.rpm = self.addField(sizerG, "RPM", cf.tuRPM)

        self.pause = self.addCheckBox(sizerG, "Pause", cf.tuPause)

        sizerV.Add(sizerG, flag=wx.CENTER|wx.ALL, border=2)

        self.SetSizer(sizerV)
        sizerV.Fit(self)

    def OnInternal(self, e):
        self.updateUI()
            
    def updateUI(self):
        if self.internal.GetValue():
            self.diam0Txt.SetLabel("X End D")
            self.diam1Txt.SetLabel("X Start D")
        else:
            self.diam0Txt.SetLabel("X Start D")
            self.diam1Txt.SetLabel("X End D")
        self.sizerV.Layout()

    def update(self):
        self.updateUI()
        self.formatData(self.formatList)
        jogPanel.setPassText("Diam")

    def sendData(self):
        try:
            moveCommands.queClear()
            sendClear()
            sendSpindleData()
            sendZData()
            sendXData()
        except CommTimeout:
            commTimeout()

    def sendAction(self):
        self.sendData()
        return(self.control.runOperation())

    def startAction(self):
        comm.command(cm.CMD_RESUME)
        control = self.control
        if control.add:
            if jogPanel.mvStatus & ct.MV_READ_X:
                control.fixCut()
        else:
            if cfg.getBoolInfoData(cf.cfgDbgSave):
                updateThread.openDebug()

    def addAction(self):
        self.control.addPass()

    def nextOperation(self):
        if not self.active:
            jogPanel.setStatus(st.STR_OP_NOT_ACTIVE)
            return
        
        if self.internal.GetValue():
            dCur = self.xDiam1
            dNxt = self.xDiam0
        else:
            dCur = self.xDiam0
            dNxt = self.xDiam1
        dCur.SetValue(jogPanel.passSize.GetValue())
        dNxt.SetFocus()
        dNxt.SetSelection(-1, -1)
        self.active = False
        jogPanel.setStatus(st.STR_CLR)

class Face(LatheOp, UpdatePass):
    def __init__(self, facePanel):
        LatheOp.__init__(self, facePanel)
        UpdatePass.__init__(self)

        self.internal = False
        self.zCut = 0.0
        self.curZ = 0.0

    def getParameters(self):
        fa = self.panel
        self.xStart = getFloatVal(fa.xStart) / 2.0
        self.xEnd = getFloatVal(fa.xEnd) / 2.0
        self.xFeed = abs(getFloatVal(fa.xFeed))
        self.xRetract = abs(getFloatVal(fa.xRetract))

        self.zStart = getFloatVal(fa.zStart)
        self.zEnd = getFloatVal(fa.zEnd)
        self.zFeed = getFloatVal(fa.zFeed)
        self.zRetract = abs(getFloatVal(fa.zRetract))

        val = getFloatVal(fa.xFeed)
        rpm = getIntVal(fa.rpm)
        if TURN_SYNC == en.SEL_TU_ISYN or TURN_SYNC == en.SEL_TU_SYN:
            (self.cycle, self.output, self.preScaler) = \
                xSyncInt.calcSync(val, metric=False, rpm=rpm, turn=True)
        elif TURN_SYNC == en.SEL_TU_ESYN:
            (self.cycle, self.output, self.preScaler) = \
                xSyncExt.calcSync(val, metric=False, rpm=rpm, turn=True)

    def runOperation(self):
        self.getParameters()

        self.internal = self.xStart < self.xEnd
        self.zCut = abs(self.zStart - self.zEnd)

        self.calcFeed(self.zFeed, self.zCut)
        self.setupSpringPasses(self.panel)
        self.setupAction(self.calcPass, self.runPass)

        self.panel.passes.SetValue("%d" % (self.passes))
        print("zCut %5.3f passes %d internal %s" % \
              (self.zCut, self.passes, self.internal))

        if self.internal:
            self.xRetract = -self.xRetract
        self.safeX = self.xStart + self.xRetract
        self.safeZ = self.zStart + self.zRetract

        m = self.m
        if cfg.getBoolInfoData(cf.cfgDraw):
            m.draw("face", self.xStart, self.xEnd)
            m.setTextAngle(90)

        jogPanel.dPrt("\nface runOperation\n")
        self.setup()

        while self.updatePass():
            pass

        m.moveX(self.safeX)
        m.moveZ(self.zStart + self.zRetract)

        self.passDone()
        return(True)

    def setup(self, add=False): # face
        comm.queParm(pm.CURRENT_OP, en.OP_FACE)
        m = self.m
        if not add:
            m.setLoc(self.zEnd, self.xStart)
            m.drawLineZ(self.zStart, REF)
            m.drawLineX(self.xEnd, REF)
            m.setLoc(self.zStart, self.safeX)

        if TURN_SYNC == en.SEL_TU_ISYN or TURN_SYNC == en.SEL_TU_SYN:
            comm.queParm(pm.L_SYNC_CYCLE, self.cycle)
            comm.queParm(pm.L_SYNC_OUTPUT, self.output)
            comm.queParm(pm.L_SYNC_PRESCALER, self.preScaler)
        elif TURN_SYNC == en.SEL_TU_ESYN:
            syncComm.setParm(sp.SYNC_ENCODER, \
                             cfg.getIntInfoData(cf.cfgEncoder))
            syncComm.setParm(sp.SYNC_CYCLE, self.cycle)
            syncComm.setParm(sp.SYNC_OUTPUT, self.output)
            syncComm.setParm(sp.SYNC_PRESCALER, self.preScaler)
            syncComm.command(sc.SYNC_SETUP)

        m.queInit()
        if (not add) or (add and not self.pause):
            m.quePause()
        m.done(ct.PARM_START)

        comm.command(cm.CMD_SYNCSETUP)

        m.startSpindle(cfg.getIntInfoData(cf.faRPM))

        m.queFeedType(ct.FEED_PITCH)
        m.xSynSetup(cfg.getFloatInfoData(cf.faXFeed))

        m.moveX(self.safeX)
        m.moveZ(self.zStart)

        if not add:
            m.text("%7.3f" % (self.zStart), \
                   (self.zStart, self.xEnd), None if self.internal else RIGHT)
            m.text("%7.3f %6.3f" % \
                   (self.safeX * 2.0, self.actualFeed), \
                   (self.safeZ, self.safeX))
            m.text("%7.3f" % (self.xStart * 2.0), \
                   (self.zEnd, self.xStart), CENTER)
            m.text("%7.3f" % (self.xEnd * 2.0), \
                   (self.zEnd, self.xEnd), CENTER)

    def calcPass(self, final=False):
        feed = self.cutAmount if final else self.passCount * self.actualFeed
        self.feed = feed
        self.curZ = self.zStart - feed
        self.safeZ = self.curZ + self.zRetract
        self.passSize[self.passCount] = self.curZ
        jogPanel.dPrt("pass %2d feed %5.3f z %5.3f\n" % \
                      (self.passCount, feed, self.curZ), True, True)

    def runPass(self, addPass=False):
        m = self.m
        m.moveZ(self.curZ, ct.CMD_JOG)
        if DRO:
            m.saveZDro()
        if self.pause:
            m.quePause(ct.PAUSE_ENA_Z_JOG | ct.PAUSE_READ_Z if addPass else 0)
        if not addPass:
            if m.passNum & 0x300 == 0:
                m.text("%2d %7.3f" % (m.passNum, self.curZ), \
                       (self.curZ, self.safeX), \
                       RIGHT if self.internal else None)
        m.moveX(self.xStart)
        m.moveX(self.xEnd, ct.CMD_SYN)
        if DRO:
            m.saveXDro()
        m.moveZ(self.safeZ)
        if not addPass:
            if m.passNum & 0x300 == 0:
                m.text("%2d %7.3f" % (m.passNum, self.safeZ), \
                       (self.safeZ, self.xEnd), \
                       None if self.internal else RIGHT)
        m.moveX(self.safeX)

    def addPass(self):
        add = self.addInit("face")
        self.cutAmount += add
        self.setup(True)
        self.calcPass(True)
        moveCommands.nextPass(self.passCount)
        self.runPass(True)
        m = self.m
        m.moveX(self.safeX)
        m.moveZ(self.zStart + self.zRetract)
        self.addDone()

    def fixCut(self, offset=0.0): # turn
        passNum = jogPanel.lastPass
        if offset == 0.0:
            actual = float(jogPanel.zPos.GetValue())
            self.passSize[passNum] = actual
            self.cutAmount = self.zStart - actual
        else:
            self.passSize[passNum] += offset
        
class FacePanel(wx.Panel, FormRoutines, ActionRoutines):
    def __init__(self, parent, hdrFont, *args, **kwargs):
        super(FacePanel, self).__init__(parent, *args, **kwargs)
        self.hdrFont = hdrFont
        FormRoutines.__init__(self)
        ActionRoutines.__init__(self, Face(self), en.OP_FACE)
        self.InitUI()
        self.configList = None
        self.prefix = 'fa'
        self.formatList = ((cf.faAddFeed, 'f'), \
                           (cf.faPasses, 'd'), \
                           (cf.faPause, None), \
                           (cf.faRPM, 'd'), \
                           (cf.faSPInt, 'd'), \
                           (cf.faSpring, 'd'), \
                           (cf.faXEnd, 'f'), \
                           (cf.faXFeed, 'f'), \
                           (cf.faXRetract, 'f'), \
                           (cf.faXStart, 'f'), \
                           (cf.faZEnd, 'f'), \
                           (cf.faZFeed, 'f'), \
                           (cf.faZRetract, 'f'), \
                           (cf.faZStart, 'f'))

    def InitUI(self):
        self.sizerV = sizerV = wx.BoxSizer(wx.VERTICAL)

        txt = wx.StaticText(self, -1, "Face", size=(120, 30))
        txt.SetFont(self.hdrFont)

        sizerV.Add(txt, flag=wx.CENTER|wx.ALL, border=2)

        sizerG = wx.FlexGridSizer(cols=8, rows=0, vgap=0, hgap=0)

        # z parameters

        self.zEnd = self.addField(sizerG, "Z End", cf.faZEnd)

        self.zStart = self.addField(sizerG, "Z Start", cf.faZStart)

        self.zFeed = self.addField(sizerG, "Z Feed", cf.faZFeed)

        self.zRetract = self.addField(sizerG, "Z Retract", cf.faZRetract)

        # x parameters

        self.xStart = self.addField(sizerG, "X Start D", cf.faXStart)

        self.xEnd = self.addField(sizerG, "X End D", cf.faXEnd)

        self.xFeed = self.addField(sizerG, "X Feed", cf.faXFeed)

        self.xRetract = self.addField(sizerG, "X Retract", cf.faXRetract)

        # pass info

        self.passes = self.addField(sizerG, "Passes", cf.faPasses)
        self.passes.SetEditable(False)

        self.sPInt = self.addField(sizerG, "SP Int", cf.faSPInt)

        self.spring = self.addField(sizerG, "Spring", cf.faSpring)

        sizerG.Add(self.emptyCell)
        sizerG.Add(self.emptyCell)

        # buttons

        self.addButton(sizerG, 'Send', self.OnSend)

        self.addButton(sizerG, 'Start', self.OnStart)

        self.addButton(sizerG, 'Add', self.OnAdd)

        self.add = self.addField(sizerG, None, cf.faAddFeed)

        self.rpm = self.addField(sizerG, "RPM", cf.faRPM)

        self.pause = self.addCheckBox(sizerG, "Pause", cf.faPause)

        sizerV.Add(sizerG, flag=wx.CENTER|wx.ALL, border=2)

        self.SetSizer(sizerV)
        self.sizerV.Fit(self)

    def update(self):
        self.formatData(self.formatList)
        jogPanel.setPassText("Len")

    def sendData(self):
        try:
            moveCommands.queClear()
            sendClear()
            sendSpindleData()
            sendZData()
            sendXData()

        except CommTimeout:
            commTimeout()

    def sendAction(self):
        jogPanel.setStatus(st.STR_CLR)
        self.sendData()
        return(self.control.runOperation())

    def startAction(self):
        comm.command(cm.CMD_RESUME)
        control = self.control
        if control.add:
            if jogPanel.mvStatus & ct.MV_READ_Z:
                control.fixCut()
        else:
            if cfg.getBoolInfoData(cf.cfgDbgSave):
                updateThread.openDebug()

    def addAction(self):
        self.control.addPass()

class Cutoff(LatheOp):
    def __init__(self, cutoffPanel):
        LatheOp.__init__(self, cutoffPanel)
        self.add = False
        self.passSize = [0.0, ]

        self.zCutoff = 0.0
        self.toolWidth = 0.0

        self.cutoffZ = 0.0

    def getParameters(self):
        cu = self.panel
        self.xStart = getFloatVal(cu.xStart) / 2.0
        self.xEnd = getFloatVal(cu.xEnd) / 2.0
        self.xFeed = abs(getFloatVal(cu.xFeed))
        self.xRetract = abs(getFloatVal(cu.xRetract))
        if self.xStart < 0:
            self.xRetract = -self.xRetract

        self.zStart = getFloatVal(cu.zStart)
        self.zRetract = getFloatVal(cu.zRetract)
        self.zCutoff = getFloatVal(cu.zCutoff)
        self.toolWidth = getFloatVal(cu.toolWidth)

        val = getFloatVal(cu.xFeed)
        rpm = getIntVal(cu.rpm)

        if TURN_SYNC == en.SEL_TU_ISYN or TURN_SYNC == en.SEL_TU_SYN:
            (self.cycle, self.output, self.preScaler) = \
                xSyncInt.calcSync(val, metric=False, rpm=rpm, turn=True)
        elif TURN_SYNC == en.SEL_TU_ESYN:
            (self.cycle, self.output, self.preScaler) = \
                xSyncExt.calcSync(val, metric=False, rpm=rpm, turn=True)

    def runOperation(self):
        self.getParameters()

        self.safeX = self.xStart + self.xRetract
        self.cutoffZ = self.zCutoff - self.toolWidth

        self.passSize[0] = self.cutoffZ
        m = self.m
        if cfg.getBoolInfoData(cf.cfgDraw):
            m.draw("cutoff", self.xStart, self.zStart)

        self.setup()

        if self.panel.pause.GetValue():
            m.quePause(ct.PAUSE_ENA_X_JOG | ct.PAUSE_ENA_Z_JOG)
            
        m.moveX(self.xEnd, ct.CMD_SYN)
        m.moveX(self.safeX)
        m.moveZ(self.zStart)

        if STEP_DRV or MOTOR_TEST or SPINDLE_SWITCH:
            m.stopSpindle()
        m.done(ct.PARM_DONE)
        stdout.flush()
        return(True)

    def setup(self):            # cutoff
        comm.queParm(pm.CURRENT_OP, en.OP_CUTOFF)
        m = self.m

        if TURN_SYNC == en.SEL_TU_ISYN or TURN_SYNC == en.SEL_TU_SYN:
            comm.queParm(pm.L_SYNC_CYCLE, self.cycle)
            comm.queParm(pm.L_SYNC_OUTPUT, self.output)
            comm.queParm(pm.L_SYNC_PRESCALER, self.preScaler)
        elif TURN_SYNC == en.SEL_TU_ESYN:
            syncComm.setParm(sp.SYNC_ENCODER, \
                             cfg.getIntInfoData(cf.cfgEncoder))
            syncComm.setParm(sp.SYNC_CYCLE, self.cycle)
            syncComm.setParm(sp.SYNC_OUTPUT, self.output)
            syncComm.setParm(sp.SYNC_PRESCALER, self.preScaler)
            syncComm.command(sc.SYNC_SETUP)

        m.queInit()
        m.quePause()
        m.done(ct.PARM_START)

        comm.command(cm.CMD_SYNCSETUP)

        m.startSpindle(cfg.getIntInfoData(cf.cuRPM))

        m.queFeedType(ct.FEED_PITCH)
        m.xSynSetup(cfg.getFloatInfoData(cf.cuXFeed))

        m.moveX(self.safeX)
        m.moveZ(self.cutoffZ)
        m.moveX(self.xStart)

class CutoffPanel(wx.Panel, FormRoutines, ActionRoutines):
    def __init__(self, parent, hdrFont, *args, **kwargs):
        super(CutoffPanel, self).__init__(parent, *args, **kwargs)
        self.hdrFont = hdrFont
        FormRoutines.__init__(self)
        ActionRoutines.__init__(self, Cutoff(self), en.OP_CUTOFF)
        self.InitUI()
        self.configList = None
        self.prefix = 'cf'
        self.formatList = ((cf.cuPause, None), \
                           (cf.cuRPM, 'd'), \
                           (cf.cuToolWidth, 'f'), \
                           (cf.cuXEnd, 'f'), \
                           (cf.cuXFeed, 'f'), \
                           (cf.cuXRetract, 'f'), \
                           (cf.cuXStart, 'f'), \
                           (cf.cuZCutoff, 'f'), \
                           (cf.cuZStart, 'f'), \
                           (cf.cuZRetract, 'f'), \
        )

    def InitUI(self):
        self.sizerV = sizerV = wx.BoxSizer(wx.VERTICAL)

        txt = wx.StaticText(self, -1, "Cutoff", size=(120, 30))
        txt.SetFont(self.hdrFont)

        sizerV.Add(txt, flag=wx.CENTER|wx.ALL, border=2)

        sizerG = wx.FlexGridSizer(cols=8, rows=0, vgap=0, hgap=0)

        # z parameters

        self.zCutoff = self.addField(sizerG, "Z Cutoff", cf.cuZCutoff)

        self.zStart = self.addField(sizerG, "Z Start", cf.cuZStart)

        self.zRetract = self.addField(sizerG, "Z Retract", cf.cuZRetract)

        self.toolWidth = self.addField(sizerG, "Tool Width", cf.cuToolWidth)

        # x parameters

        self.xStart = self.addField(sizerG, "X Start D", cf.cuXStart)

        self.xEnd = self.addField(sizerG, "X End D", cf.cuXEnd)

        self.xFeed = self.addField(sizerG, "X Feed", cf.cuXFeed)

        self.xRetract = self.addField(sizerG, "X Retract", cf.cuXRetract)

        # buttons

        self.addButton(sizerG, 'Send', self.OnSend)

        self.addButton(sizerG, 'Start', self.OnStart)

        sizerG.Add(self.emptyCell)
        sizerG.Add(self.emptyCell)

        self.rpm = self.addField(sizerG, "RPM", cf.cuRPM)

        self.pause = self.addCheckBox(sizerG, "Pause", cf.cuPause)

        sizerV.Add(sizerG, flag=wx.CENTER|wx.ALL, border=2)

        self.SetSizer(sizerV)
        self.sizerV.Fit(self)

    def update(self):
        self.formatData(self.formatList)
        jogPanel.setPassText("Len")

    def sendData(self):
        try:
            moveCommands.queClear()
            sendClear()
            sendSpindleData()
            sendZData()
            sendXData()
        except CommTimeout:
            commTimeout()

    def sendAction(self):
        self.sendData()
        return(self.control.runOperation())

    def startAction(self):
        comm.command(cm.CMD_RESUME)
        if cfg.getBoolInfoData(cf.cfgDbgSave):
            updateThread.openDebug()

class Taper(LatheOp, UpdatePass):
    def __init__(self, taperPanel):
        LatheOp.__init__(self, taperPanel)
        UpdatePass.__init__(self)

        self.zLength = 0.0
        self.largeDiameter = 0.0
        self.smallDiameter = 0.0

        self.xLength = 0.0
        self.finish = 0.0

        self.taperX = False
        self.taper = 0.0

        self.cut = 0.0
        self.internal = False
        self.boreRadius = 0.0

        self.startZ = 0.0
        self.startX = 0.0
        self.taperLength = 0.0
        self.endZ = 0.0
        self.endX = 0.0
        self.zbackInc = 0.0

        # morse #3 taper
        # taper = 0.0502
        # length = 3.190
        # largeEnd = .938
        # smallEnd = .778

    def getParameters(self, taperInch):
        tp = self.panel
        # taper = x / z
        # taperInch = totalTaper / self.zLength
        # taperX True  - move z taper x
        # taperX False - move x taper z
        self.taperX = taperInch <= 1.0
        self.taper = taperInch

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

        self.zBackInc = abs(cfg.getFloatInfoData(cf.zBackInc))
        self.finish = abs(getFloatVal(tp.finish))

        val = getFloatVal(tp.zFeed)
        rpm = getIntVal(tp.rpm)
        if TURN_SYNC == en.SEL_TU_ISYN or TURN_SYNC == en.SEL_TU_SYN:
            (self.cycle, self.output, self.preScaler) = \
                zSyncInt.calcSync(val, metric=False, rpm=rpm, turn=True)
        elif TURN_SYNC == en.SEL_TU_ESYN:
            (self.cycle, self.output, self.preScaler) = \
                zSyncExt.calcSync(val, metric=False, rpm=rpm, turn=True)

        totalTaper = taperInch * self.zLength
        print("taperX %s totalTaper %5.3f taperInch %6.4f" % \
              (self.taperX, totalTaper, taperInch))

    def setup(self, add=False): # taper
        comm.queParm(pm.CURRENT_OP, en.OP_TAPER)
        m = self.m
        if not add:
            m.setLoc(self.zEnd, self.xStart)
            m.drawLineZ(self.zStart, REF)
            m.drawLineX(self.xEnd, REF)
            m.setLoc(self.safeZ, self.safeX)

        if TURN_SYNC == en.SEL_TU_ISYN or TURN_SYNC == en.SEL_TU_SYN:
            comm.queParm(pm.L_SYNC_CYCLE, self.cycle)
            comm.queParm(pm.L_SYNC_OUTPUT, self.output)
            comm.queParm(pm.L_SYNC_PRESCALER, self.preScaler)
        elif TURN_SYNC == en.SEL_TU_ESYN:
            syncComm.setParm(sp.SYNC_ENCODER, \
                             cfg.getIntInfoData(cf.cfgEncoder))
            syncComm.setParm(sp.SYNC_CYCLE, self.cycle)
            syncComm.setParm(sp.SYNC_OUTPUT, self.output)
            syncComm.setParm(sp.SYNC_PRESCALER, self.preScaler)
            syncComm.command(sc.SYNC_SETUP)

        m.queInit()
        if (not add) or (add and not self.pause):
            m.quePause(ct.PAUSE_ENA_X_JOG | ct.PAUSE_ENA_Z_JOG)
        m.done(ct.PARM_START)

        comm.command(cm.CMD_SYNCSETUP)
        
        if self.taperX:
            m.saveTaper(self.taper)
        else:
            m.saveTaper(1.0 / self.taper)
            
        m.startSpindle(cfg.getIntInfoData(cf.tpRPM))

        m.queFeedType(ct.FEED_PITCH)
        m.zSynSetup(cfg.getFloatInfoData(cf.tpZFeed))
        m.xSynSetup(cfg.getFloatInfoData(cf.tpXInFeed))

        m.moveX(self.safeX)
        m.moveZ(self.safeZ)
        
        if not add:
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

    def externalRunOperation(self, taperInch):
        print("externalTaper")
        self.internal = False
        self.getParameters(taperInch)

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
        self.setupSpringPasses(self.panel)
        self.setupAction(self.externalCalcPass, self.externalRunPass)

        self.panel.passes.SetValue("%d" % (self.passes))
        print("passes %d cutAmount %5.3f feed %6.3f" % \
              (self.passes, self.cutAmount, self.actualFeed))

        m = self.m
        if cfg.getBoolInfoData(cf.cfgDraw):
            m.draw("taper", self.zStart, self.taper)

        jogPanel.dPrt("\ntaper nexternalRunOperation\n")
        self.setup()

        while self.updatePass():
            pass

        m.printXText("%2d %7.4f %7.4f", LEFT, False)
        m.printZText("%2d %7.4f", LEFT|MIDDLE)
        m.moveZ(self.safeZ)

        self.passDone()
        return(True)

    def externalCalcPass(self, final=False):
        if self.taperX:
            feed = self.cutAmount if final else \
                   self.passCount * self.actualFeed
            self.feed = feed
            self.endX = self.xStart - feed
            self.taperLength = self.feed / self.taper
            if self.taperLength < self.zLength:
                self.startZ = self.zStart - self.taperLength
                self.startX = self.xStart
            else:
                self.startZ = self.zStart - self.zLength
                self.startX = self.endX + self.taper * self.zLength
            self.passSize[self.passCount] = self.endX * 2.0
        else:
            feed = self.cutAmount if final else \
                   self.passCount * self.actualFeed
            self.feed = feed
            self.startZ = self.zStart - feed
            self.startX = self.xStart
            self.endZ = self.zStart
            taperLength = self.feed * self.taper
            self.endX = self.xStart - taperLength \
                        if taperLength < self.xLength else self.xEnd
            self.passSize[self.passCount] = self.startZ
        jogPanel.dPrt("%2d start (%6.3f %6.3f) end (%6.3f %6.3f) "\
                      "%6.3f %6.3f\n" % \
                      (self.passCount, self.startZ, self.startX, \
                       self.endZ, self.endX, self.startX * 2.0, \
                       self.endX * 2.0), True, True)

    def externalRunPass(self, addPass=False):
        m = self.m
        if self.zBackInc != 0.0:
            m.moveZ(self.startZ, backlash=-self.zBackInc) # move past start
            m.moveZ(self.startZ, ct.CMD_JOG) # move to takeout backlash
        else:
            m.moveZ(self.startZ)
        if self.pause:
            m.quePause(ct.PAUSE_ENA_X_JOG | ct.PAUSE_READ_X if addPass else 0)
        if self.taperX:
            if not addPass and m.passNum & 0x300 == 0:
                if self.taperLength < self.zLength:
                    m.text("%2d %7.3f" % (m.passNum, self.startZ), \
                           (self.startZ, self.safeX), CENTER | ABOVE)
                else:
                    m.text("%2d %7.3f" % (m.passNum, self.startX * 2.0), \
                           (self.endZ, self.startX), RIGHT)
            m.moveX(self.startX, ct.CMD_SYN)
            if DRO:
                m.saveZDro()
                m.saveXDro()
            m.taperZX(self.endZ, self.endX)
            if DRO:
                m.saveZDro()
                m.saveXDro()
        else:
            if not addPass and m.passNum & 0x300 == 0:
                m.saveZText((m.passNum, self.startZ), \
                            (self.startZ, self.safeX))
            m.moveX(self.startX)
            if DRO:
                m.saveZDro()
                m.saveXDro()
            m.taperXZ(self.endX, self.endZ)
            if DRO:
                m.saveZDro()
                m.saveXDro()
        if not addPass and m.passNum & 0x300 == 0:
            m.drawLine(self.endZ, self.endX)
            m.saveXText((m.passNum, self.endX * 2.0, self.endX), \
                       (self.safeZ, self.endX))
        m.moveZ(self.safeZ)
        m.moveX(self.safeX)

    def externalAddPass(self):
        add = self.addInit("external taper") / 2.0
        self.cutAmount += add
        self.setup(True)
        self.externalCalcPass(True)
        m = self.m
        m.nextPass(self.passCount)
        self.externalRunPass(True)
        m.moveX(self.safeX)
        m.moveZ(self.startZ)
        self.addDone()
            
    def fixCut(self, offset=0.0): # taper
        if offset == 0:
            actual = float(jogPanel.xPos.GetValue())
            passNum = jogPanel.lastPass
            self.passSize[passNum] = 2 * actual
            if self.internal:
                self.cutAmount = actual - self.xStart
            else:
                self.cutAmount = self.xStart - actual
        else:
            pass

    def internalRunOperation(self, taperInch):
        print("internalTaper")
        self.internal = True
        self.getParameters(taperInch)

        self.boreRadius = self.xStart = self.largeDiameter / 2.0
        self.xEnd = self.smallDiameter / 2.0
        self.cut = self.xEnd - self.boreRadius

        self.calcFeed(self.xFeed, self.cut, self.finish)
        self.setupSpringPasses(self.panel)
        self.setupAction(self.internalCalcPass, self.internalRunPass)

        self.panel.passes.SetValue("%d" % (self.passes))
        print("passes %d cutAmount %5.3f feed %6.3f" % \
              (self.passes, self.cutAmount, self.actualFeed))

        self.endZ = self.zStart

        self.safeX = self.boreRadius - self.xRetract
        self.safeZ = self.zStart + self.zRetract

        m = self.m
        if cfg.getBoolInfoData(cf.cfgDraw):
            m.draw("taper", self.zStart, self.taper)

        jogPanel.dPrt("\ntaper internalRunOperation\n")
        self.setup()

        while self.updatePass():
            pass

        m.printXText("%2d %7.4f %7.4f", LEFT, True)
        m.printZText("%2d %7.4f %7.4f %7.4f", RIGHT|MIDDLE)
        m.moveX(self.safeX)
        m.moveZ(self.safeZ)

        self.passDone()
        return(True)

    def internalCalcPass(self, final=False):
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
        self.passSize[self.passCount] = self.endX * 2.0
        jogPanel.dPrt("%2d feed %6.3f start (%6.3f,%6.3f) end (%6.3f %6.3f) "\
                      "%6.3f %6.3f\n" % \
                      (self.passCount, self.feed, self.startX,
                       self.startZ, self.endX, self.endZ, \
                       self.startX * 2.0, self.endX * 2.0), True, True)

    def internalRunPass(self, addPass=False):
        m = self.m
        if self.zBackInc != 0.0:
            m.moveZ(self.startZ, backlash=-self.ZBackInc) # past the start
        m.moveZ(self.startZ, ct.CMD_JOG) # back to start to remove backlash
        m.moveX(self.startX, ct.CMD_SYN)
        if self.pause:
            m.quePause(ct.PAUSE_ENA_X_JOG | ct.PAUSE_READ_X if addPass else 0)
        if not addPass and m.passNum & 0x300 == 0:
            m.saveZText((m.passNum, self.startZ, self.startX, \
                         self.startX * 2.0), (self.startZ, self.safeX))
        if DRO:
            m.saveZDro()
            m.saveXDro()
        if self.taperX:
            m.taperZX(self.endZ, self.endX)
        else:
            m.taperXZ(self.endX, self.endZ)
        if DRO:
            m.saveZDro()
            m.saveXDro()
        if not addPass:
            m.drawLine(self.endZ, self.endX)
            if m.passNum & 0x300 == 0:
                m.saveXText((m.passNum, self.endX * 2.0, self.endX), \
                            (self.safeZ, self.endX))
        m.moveZ(self.safeZ)
        m.moveX(self.safeX)

    def internalAddPass(self):
        add = self.addInit("internal taper") / 2.0
        self.cutAmount += add
        self.setup(True)
        self.internalCalcPass(True)
        m = self.m
        m.nextPass(self.passCount)
        self.internalRunPass(True)
        m.moveX(self.safeX)
        m.moveZ(self.safeZ)
        self.addDone()

class TaperPanel(wx.Panel, FormRoutines, ActionRoutines):
    def __init__(self, parent, hdrFont, *args, **kwargs):
        super(TaperPanel, self).__init__(parent, *args, **kwargs)
        self.hdrFont = hdrFont
        FormRoutines.__init__(self)
        ActionRoutines.__init__(self, Taper(self), en.OP_TAPER)
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
        self.m = moveCommands
        self.prefix = 'tp'
        self.formatList = ((cf.tpAddFeed, 'f'), \
                           (cf.tpAngle, 'fs'), \
                           (cf.tpAngleBtn, None), \
                           (cf.tpDeltaBtn, None), \
                           (cf.tpInternal, None), \
                           (cf.tpLargeDiam, 'f'), \
                           (cf.tpPasses, 'd'), \
                           (cf.tpPause, None), \
                           (cf.tpRPM, 'd'), \
                           (cf.tpSPInt, 'd'), \
                           (cf.tpSmallDiam, 'f'), \
                           (cf.tpSpring, 'd'), \
                           (cf.tpTaperSel, None), \
                           (cf.tpXDelta, 'f5'), \
                           (cf.tpXFeed, 'f'), \
                           (cf.tpXFinish, 'f'), \
                           (cf.tpXInFeed, 'f'), \
                           (cf.tpXRetract, 'f'), \
                           (cf.tpZDelta, 'f'), \
                           (cf.tpZFeed, 'f'), \
                           (cf.tpZLength, 'f'), \
                           (cf.tpZRetract, 'f'), \
                           (cf.tpZStart, 'f'))

    def InitUI(self):
        self.sizerV = sizerV = wx.BoxSizer(wx.VERTICAL)

        txt = wx.StaticText(self, -1, "Taper", size=(120, 30))
        txt.SetFont(self.hdrFont)

        sizerV.Add(txt, flag=wx.CENTER|wx.ALL, border=2)

        sizerH = wx.BoxSizer(wx.HORIZONTAL)

        # standard taper select

        txt = wx.StaticText(self, -1, "Select Taper")
        sizerH.Add(txt, flag=wx.ALL|wx.ALIGN_CENTER_VERTICAL, border=2)

        self.taperSel = combo = wx.ComboBox(self, -1, self.taperList[0], \
                                            choices=self.taperList, \
                                            style=wx.CB_READONLY)
        cfg.initInfo(cf.tpTaperSel, combo)
        combo.Bind(wx.EVT_COMBOBOX, self.OnCombo)
        sizerH.Add(combo, flag=wx.ALL, border=2)

        sizerV.Add(sizerH, flag=wx.CENTER|wx.ALL, border=2)

        sizerG = wx.FlexGridSizer(cols=8, rows=0, vgap=0, hgap=0)

        # z parameters

        self.zLength = self.addField(sizerG, "Z Length", cf.tpZLength)

        self.zStart = self.addField(sizerG, "Z Start", cf.tpZStart)

        self.zFeed = self.addField(sizerG, "Z Feed", cf.tpZFeed)

        self.zRetract = self.addField(sizerG, "Z Retract", cf.tpZRetract)

        # x parameters

        (self.largeDiam, self.largeDiamTxt) = \
            self.addFieldText(sizerG, "Large Diam", cf.tpLargeDiam)

        (self.smallDiam, self.smallDiamTxt) = \
            self.addFieldText(sizerG, "Small Diam", cf.tpSmallDiam)

        self.xInFeed = self.addField(sizerG, "X In Feed R", cf.tpXInFeed)

        self.xFeed = self.addField(sizerG, "X Pass D", cf.tpXFeed)

        # taper parameters

        self.deltaBtn = self.addRadioButton(sizerG, "Delta Z", cf.tpDeltaBtn, \
                                            style=wx.RB_GROUP, \
                                            action=self.OnDelta)

        self.zDelta = self.addField(sizerG, None, cf.tpZDelta)
        self.zDelta.Bind(wx.EVT_KILL_FOCUS, self.OnDeltaFocus)

        self.xDelta = self.addField(sizerG, "Delta X", cf.tpXDelta)
        self.xDelta.Bind(wx.EVT_KILL_FOCUS, self.OnDeltaFocus)

        self.angleBtn = self.addRadioButton(sizerG, "Angle", cf.tpAngleBtn, \
                                            action=self.OnAngle)

        self.angle = self.addField(sizerG, None, cf.tpAngle)
        self.angle.Bind(wx.EVT_KILL_FOCUS, self.OnAngleFocus)

        self.xRetract = self.addField(sizerG, "X Retract", cf.tpXRetract)

        # pass info

        self.passes = self.addField(sizerG, "Passes", cf.tpPasses)
        self.passes.SetEditable(False)

        self.sPInt = self.addField(sizerG, "SP Int", cf.tpSPInt)

        self.spring = self.addField(sizerG, "Spring", cf.tpSpring)

        self.finish = self.addField(sizerG, "Finish", cf.tpXFinish)

        # control buttons

        self.addButton(sizerG, 'Send', self.OnSend)

        self.addButton(sizerG, 'Start', self.OnStart)

        self.addButton(sizerG, 'Add', self.OnAdd)

        self.add = self.addField(sizerG, None, cf.tpAddFeed)

        self.rpm = self.addField(sizerG, "RPM", cf.tpRPM)

        sizerH = wx.BoxSizer(wx.HORIZONTAL)

        self.internal = self.addCheckBox(sizerH, "Internal", cf.tpInternal, \
                                         self.OnInternal)

        sizerG.Add(sizerH)

        sizerH = wx.BoxSizer(wx.HORIZONTAL)

        self.pause = self.addCheckBox(sizerH, "Pause", cf.tpPause)

        sizerG.Add(sizerH)

        sizerV.Add(sizerG, flag=wx.CENTER|wx.ALL, border=2)

        self.SetSizer(sizerV)
        sizerV.Fit(self)

    def update(self):
        self.updateUI()
        self.updateDelta()
        self.updateAngle()
        self.formatData(self.formatList)

    def updateUI(self):
        val = self.deltaBtn.GetValue()
        self.zDelta.SetEditable(val)
        self.xDelta.SetEditable(val)
        self.angle.SetEditable(not val)
        taper = getFloatVal(self.xDelta) / getFloatVal(self.zDelta)
        if self.internal.GetValue():
            self.largeDiamTxt.SetLabel("Bore Diam")
            self.smallDiamTxt.SetLabel("Large Diam")
            jogPanel.setPassText("L Diam")

        else:
            self.largeDiamTxt.SetLabel("Large Diam")
            self.smallDiamTxt.SetLabel("Small Diam")
            jogPanel.setPassText("S Diam" if taper < 1.0 else \
                                       "Z Start")
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
                traceback.print_exc()

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
        self.updateUI()
        e.Skip()

    def OnAngleFocus(self, e):
        self.updateAngle()
        self.updateUI()
        e.Skip()

    def OnInternal(self, e):
        self.updateUI()

    def OnDelta(self, e):
        self.updateUI()

    def OnAngle(self, e):
        self.updateUI()

    def sendData(self):
        try:
            moveCommands.queClear()
            sendClear()
            sendSpindleData()
            sendZData()
            sendXData()
            comm.setParm(pm.TAPER_CYCLE_DIST, \
                         cfg.getInfoData(cf.cfgTaperCycleDist))
        except CommTimeout:
            commTimeout()

    def sendAction(self):
        self.sendData()
        taper = getFloatVal(self.xDelta) / getFloatVal(self.zDelta)
        if self.internal.GetValue():
            return(self.control.internalRunOperation(taper))
        else:
            return(self.control.externalRunOperation(taper))

    def startAction(self):      # taper
        comm.command(cm.CMD_RESUME)
        control = self.control
        if control.add:
            if jogPanel.mvStatus & ct.MV_READ_X:
                control.fixCut()
        else:
            if cfg.getBoolInfoData(cf.cfgDbgSave):
                updateThread.openDebug()

    def addAction(self):
        self.control.internalAddPass() if self.internal.GetValue() else \
            self.control.externalAddPass()

    # def OnDebug(self, e):
    #     self.sendData()
    #     moveX(1.000)
    #     moveZ(0.010)
    #     taperZX(-0.25, 0.0251)

REF   = 'REF'
TEXT  = 'TEXT'

class ScrewThread(LatheOp, UpdatePass):
    def __init__(self, threadPanel):
        LatheOp.__init__(self, threadPanel)
        UpdatePass.__init__(self)
        self.rightHand = False
        self.internal = False
        self.tpi = 0.0
        self.pitch = 0.0

        self.zBackInc = 0.0
        self.firstFeed = 0.0
        self.lastFeed = 0.0
        self.depth = 0.0

        self.angle = 0.0
        self.tanAngle = 0.0
        self.area = 0.0
        self.areaPass = 0.0
        self.curArea = 0.0
        self.curX = 0.0
        self.startZ = 0.0
        self.prevFeed = 0.0
        self.depth = 0.0
        self.zAccelDist = 0.0
        self.zOffset = 0.0
        # self.p0 = 0.0
        # self.d = None

    # def draw(self, diam, tpi):
    #     tmp = "tfeed%0.3f-%0.1f" % (diam, tpi)
    #     tmp = tmp.replace(".", "-")
    #     tmp = re.sub("-0$", "", tmp) + ".dxf"
    #     d = dxf.drawing(tmp)
    #     d.add_layer(REF, color=0)
    #     d.add_layer(TEXT, color=0)
    #     self.d = d

    # def drawLine(self, p0, p1, layer=0):
    #     if self.d is not None:
    #         self.d.add(dxf.line(p0, p1, layer=layer))

    # def drawClose(self):
    #     try:
    #         if self.d is not None:
    #             self.d.save()
    #             self.d = None
    #     except:
    #         print("dxf file save error")
    #         traceback.print_exc()

    def getParameters(self):
        th = self.panel
        self.internal = th.internal.GetValue()

        self.rightHand = not th.leftHand.GetValue()
        self.zRetract = abs(getFloatVal(th.zRetract))
        if self.rightHand:      # right hand threads
            self.zStart = getFloatVal(th.z1)
            self.zEnd = getFloatVal(th.z0)
            self.safeZ = self.zStart + self.zRetract
            self.startZ = self.safeZ 

        else:                   # left and threads
            self.zStart = getFloatVal(th.z0)
            self.zEnd = getFloatVal(th.z1)
            self.safeZ = self.zEnd - self.zRetract
            self.startZ = self.zStart

        self.zAccelDist = 0.0
        self.zBackInc = abs(cfg.getFloatInfoData(cf.zBackInc))

        self.tpiBtn = th.tpi.GetValue()
        self.alternate = th.alternate.GetValue()
        self.firstFeedBtn = th.firstFeedBtn.GetValue()

        val =  getFloatVal(th.thread)
        rpm = getIntVal(th.rpm)
        if self.tpiBtn:
            self.tpi = val
            self.pitch = 1.0 / val
            metric = False
        else:
            self.pitch = val / 25.4
            self.tpi = 1.0 / self.pitch
            metric = True

        if THREAD_SYNC == en.SEL_TH_ISYN_RENC or THREAD_SYNC == en.SEL_TH_SYN:
            (self.cycle, self.output, self.preScaler) = \
                zSyncInt.calcSync(val, dbg=True, metric=metric, rpm=rpm)
        elif (THREAD_SYNC == en.SEL_TH_ESYN_RENC or
              THREAD_SYNC == en.SEL_TH_ESYN_RSYN):
            (self.cycle, self.output, self.preScaler) = \
                zSyncExt.calcSync(val, dbg=True, metric=metric, rpm=rpm)

        self.xStart = getFloatVal(th.xStart) / 2.0
        self.xRetract = abs(getFloatVal(th.xRetract))
        self.safeX = self.xStart + self.xRetract

        self.firstFeed = getFloatVal(th.firstFeed)
        self.lastFeed = getFloatVal(th.lastFeed)
        self.depth = getFloatVal(th.depth)

        self.xEnd = self.xStart + self.depth if self.internal else \
                    self.xStart - self.depth

        self.angle = radians(getFloatVal(th.angle))
        self.runout = getFloatVal(th.runout)

        if self.runout != 0:
            if THREAD_SYNC == en.SEL_TH_ESYN_RSYN:
                xSync.setExitRevs(self.runout)
                (self.xCycle, self.xOutput, self.xPreScaler) = \
                    xSync.calcSync(self.depth, rpm=rpm, dist=True)

        self.endZ = self.zEnd

    def setup(self, add=False): # thread
        global zHomeOffset, xHomeOffset
        comm.queParm(pm.CURRENT_OP, en.OP_THREAD)
        m = self.m
        if not add:
            m.setLoc(self.endZ, self.xStart)
            m.drawLineZ(self.zStart, REF)
            m.drawLineX(self.xEnd, REF)
            m.setLoc(self.safeZ, self.safeX)

        if THREAD_SYNC == en.SEL_TH_ISYN_RENC or THREAD_SYNC == en.SEL_TH_SYN:
            comm.queParm(pm.L_SYNC_CYCLE, self.cycle)
            comm.queParm(pm.L_SYNC_OUTPUT, self.output)
            comm.queParm(pm.L_SYNC_PRESCALER, self.preScaler)
        elif (THREAD_SYNC == en.SEL_TH_ESYN_RENC or \
              THREAD_SYNC == en.SEL_TH_ESYN_RSYN):
            syncComm.setParm(sp.SYNC_ENCODER, \
                             cfg.getIntInfoData(cf.cfgEncoder))
            syncComm.setParm(sp.SYNC_CYCLE, self.cycle)
            syncComm.setParm(sp.SYNC_OUTPUT, self.output)
            syncComm.setParm(sp.SYNC_PRESCALER, self.preScaler)
            syncComm.command(sc.SYNC_SETUP)
            if (self.runout != 0 and
                THREAD_SYNC == en.SEL_TH_ESYN_RSYN):
                comm.queParm(pm.L_SYNC_CYCLE, self.xCycle)
                comm.queParm(pm.L_SYNC_OUTPUT, self.xOutput)
                comm.queParm(pm.L_SYNC_PRESCALER, self.xPreScaler)
   
        comm.queParm(pm.RUNOUT_DEPTH, self.runoutDepth)
        comm.queParm(pm.RUNOUT_DISTANCE, self.runoutDist)

        m.queInit()
        if (not add) or (add and not self.pause):
            m.quePause()
        m.done(ct.PARM_START)

        comm.command(cm.CMD_SYNCSETUP)

        th = self.panel

        m.queFeedType(ct.FEED_TPI if self.tpiBtn else ct.FEED_METRIC)
        m.saveTaper(getFloatVal(th.xTaper))

        flag = ct.TH_THREAD     # threading
        if not self.rightHand:  # left hand threads
            flag |= ct.TH_LEFT
        if self.runoutDist != 0:
            flag |= ct.TH_RUNOUT
        if self.internal:
            flag |= ct.TH_INTERNAL
        m.saveThreadFlags(flag)

        m.zSynSetup(cfg.getFloatInfoData(cf.thThread))

        if not self.rightHand:  # left hand threads
            if self.runoutDist == 0.0: # wihout runout
                m.queFeedType(ct.FEED_PITCH)
                m.xSynSetup(getFloatVal(th.lastFeed))

        m.startSpindle(cfg.getIntInfoData(cf.thRPM))

        m.moveX(self.safeX)
        m.moveZ(self.safeZ if self.rightHand else self.startZ)

        if not add:
            m.text("%7.3f" % (self.xStart * 2.0), \
                   (self.endZ, self.xStart), MIDDLE | \
                   (RIGHT if self.rightHand else LEFT))
            m.text("%0.3f" % (self.zStart), \
                   (self.zStart, self.xEnd), \
                   CENTER | (ABOVE if self.internal else BELOW))
            m.text("%7.3f" % (self.safeX * 2.0,), \
                   (self.startZ, self.safeX), \
                   CENTER | (BELOW if self.internal else ABOVE))
            m.text("%7.3f" % (self.endZ), \
                   (self.endZ, self.safeX), \
                   CENTER | (BELOW if self.internal else ABOVE))

    def runOperation(self):
        self.getParameters()

        print("tpi %4.1f pitch %5.3f" % (self.tpi, self.pitch))

        if self.depth == 0:
            self.depth = (cos(self.angle) * self.pitch)
        self.tanAngle = tan(self.angle)

        w = halfWidth = self.depth * self.tanAngle
        if self.rightHand:      # right hand threads
            if not self.alternate:
                w *= 2.0
            self.startZ += w
        else:                   # left hand threads
            self.startZ -= w
                
        self.area = area = self.depth * halfWidth
        print("depth %6.4f halfWdith %6.4f area %8.6f startZ %6.4f" % \
              (self.depth, halfWidth, area, self.startZ))

        if self.runout != 0.0:
            self.runoutDist = self.runout * self.pitch
            self.runoutDepth = self.depth + 0.005

            if self.rightHand:      # right hand threads
                self.endZ = self.zEnd - self.runoutDist
                print("runout %4.2f runoutDist %7.4f endZ %7.4f\n" % \
                      (self.runout, self.runoutDist, self.endZ))
            else:       		# left hand threads
                # depth / runoutDist = runoutDepth / total
                # total = runoutDepth / (depth / runoutDist)
                # total = (runoutDepth / depth) * runoutDist
                totalDist = (self.runoutDepth / self.depth) * self.runoutDist
                print("runout %4.2f runoutDist %7.4f totalDist %7.4f\n" % \
                      (self.runout, self.runoutDist, totalDist))
                self.runoutDist = totalDist
                self.runoutDepth = -self.runoutDepth

            if self.internal:
                self.runoutDepth = -self.runoutDepth
        else:
            self.runoutDist = 0.0
            self.runoutDepth = 0.0

        if self.firstFeedBtn:
            firstWidth = 2 * self.firstFeed * self.tanAngle
            self.areaPass = 0.5 * self.firstFeed * firstWidth
            print("firstFeed %6.4f firstWidth %6.4f areaPass %8.6f" % \
                  (self.firstFeed, firstWidth, self.areaPass))
        else:
            lastDepth = self.depth - self.lastFeed
            lastArea = (lastDepth * lastDepth) * self.tanAngle
            self.areaPass = area - lastArea
            print("area %8.6f lastDepth %6.4f " \
                  "lastArea %8.6f areaPass %8.6f" % \
                  (area, lastDepth, lastArea, self.areaPass))

        self.passes = int(ceil(area / self.areaPass))
        self.panel.passes.SetValue("%d" % (self.passes))
        self.areaPass = area / self.passes
        print("passes %d areaPass %8.6f" % \
              (self.passes, self.areaPass))

        if self.firstFeedBtn:
            lastA = self.area - self.areaPass
            lastD = self.depth - sqrt(lastA / self.tanAngle)
            self.panel.lastFeed.SetValue("%0.4f" % (lastD))
        else:
            firstF = sqrt(self.areaPass / self.tanAngle)
            self.panel.firstFeed.SetValue("%0.4f" % (firstF))

        self.setupSpringPasses(self.panel)
        self.setupAction(self.calcPass, self.runPass)
        self.initPass()

        if self.internal:
            self.xRetract = -self.xRetract

        self.safeX = self.xStart + self.xRetract
        # self.startZ = self.zStart + self.zAccelDist

        # if cfg.getBoolInfoData(cf.cfgDraw):
        #     self.draw(self.xStart * 2.0, self.tpi)
        #     self.p0 = (0, 0)

        if cfg.getBoolInfoData(cf.cfgDraw):
            self.m.draw("threada", self.xStart * 2.0, self.tpi)

        jogPanel.dPrt("\nthread runOperation\n")
        self.setup()

        self.curArea = 0.0
        self.prevFeed = 0.0
        self.zOffset = 0.0
        if not self.alternate:
            jogPanel.dPrt("pass     area   xfeed  xdelta zoffset  " \
                          "xsize startz\n", True, True)
        else:
            jogPanel.dPrt("pass     area   xfeed  xdelta  offset " \
                          "zoffset  xsize startz\n", True, True)

        while self.updatePass():
            pass

        self.m.printXText("%2d Z %6.4f Zofs %6.4f D %6.4f F %6.4f", \
                          LEFT if self.rightHand else RIGHT, \
                          self.internal)

        self.passDone()
        return(True)

    def calcPass(self, final=False, add=False):
        if not add:
            if final:
                self.curArea = self.area
            else:
                self.curArea += self.areaPass
            self.feed = sqrt(self.curArea / self.tanAngle)

        feed = self.feed
        passFeed = feed - self.prevFeed
        self.prevFeed = feed
 
        if not self.alternate:
            self.zOffset = -feed * self.tanAngle
        else:
            offset = passFeed * self.tanAngle
            if (self.passCount & 1) == 0:
                offset = -offset
            self.zOffset += offset
            # print("zOffset %7.4f offset %7.4f" % (self.zOffset, offset))

        if not self.rightHand:  # left hand threads
            self.zOffset = -self.zOffset

        if self.internal:
            feed = -feed
        self.curX = self.xStart - feed
        self.passSize[self.passCount] = self.feed

        self.startZPass = self.startZ + self.zOffset
        startZPass = self.startZPass

        if not self.alternate:
            jogPanel.dPrt("%4d %8.6f %7.4f %7.4f %7.4f %6.4f %6.4f\n" % \
                          (self.passCount, self.curArea, feed, \
                           passFeed, self.zOffset, \
                           self.curX * 2.0, startZPass), \
                          True, True)
        else:
            jogPanel.dPrt("%4d %8.6f %7.4f %7.4f %7.4f %7.4f %6.4f %6.4f\n" % \
                          (self.passCount, self.curArea, feed, \
                           passFeed, offset, self.zOffset, \
                           self.curX * 2.0, startZPass), \
                          True, True)

        if self.m.d is not None:
            addLine = self.m.addLine
            w = feed * self.tanAngle
            p0 = (startZPass, self.curX)
            pa = (startZPass + w, self.xStart)
            pb = (startZPass - w, self.xStart)
            addLine(p0, pa)
            addLine(p0, pb)
            addLine(pa, pb)

    def runPass(self, addPass=False): # thread
        m = self.m
        startZPass = self.startZPass
        startZ = self.startZPass

        if not self.rightHand:  # left Hand threads
            startZPass -= self.runoutDist

        if self.zBackInc:
            backInc = self.zBackInc if self.rightHand else -self.zBackInc
            m.moveZ(startZPass, backlash=backInc)

        m.moveZ(startZPass)

        if self.rightHand:      # right hand threads
            flag = ct.CMD_JOG | ((ct.DRO_POS | ct.DRO_UPD) if X_DRO_POS else 0)
            m.moveX(self.curX, flag)
        else:                   # left hand threads
            if self.runoutDist != 0:
                m.drawLine(startZ, self.curX)
                xBackInc = 0.0
                if self.depth > self.xRetract:
                    xBackInc = self.zBackInc

                if not self.internal:	# external threads
                    if xBackInc != 0.0:
                        m.moveX(self.xStart + self.depth, backlash=xBackInc)
                    m.moveX(self.curX + self.depth)
                else:           	# internal threads
                    if xBackInc != 0.0:
                        m.moveX(self.xStart - self.depth, backlash=-xBackInc)
                    m.moveX(self.curX - self.depth)
            else:
                flag = ct.CMD_JOG | ((ct.DRO_POS | ct.DRO_UPD) \
                                     if X_DRO_POS else 0)
                m.moveX(self.xStart, flag)
                m.moveX(self.curX, ct.CMD_SYN)

        if self.pause:
            flag = (ct.PAUSE_ENA_X_JOG | ct.PAUSE_READ_X) if addPass else 0
            m.quePause(flag)
            if addPass:
                m.moveZOffset()
            
        if DRO:
            m.saveXDro()
            m.saveZDro()
        
        if not addPass and m.passNum & 0x300 == 0:
            m.saveXText((m.passNum, startZPass, self.zOffset, \
                        self.curX * 2.0, self.feed), \
                        (self.startZ, self.curX))

        m.moveZ(self.endZ, ct.CMD_SYN | \
                (ct.Z_SYN_START if self.rightHand else ct.Z_SYN_LEFT))

        m.moveX(self.safeX)
        m.moveZ(self.safeZ if self.rightHand or self.lastPass else \
                self.startZ)

    def addPass(self):
        add = self.addInit("thread") / 2.0
        self.feed += add
        self.setup(True)

        comm.queParm(pm.TH_Z_START, \
                     round((self.startZ + zHomeOffset) * jogPanel.zStepsInch))
        comm.queParm(pm.TH_X_START, \
                     round((self.xStart + xHomeOffset) * jogPanel.xStepsInch))
        comm.queParm(pm.TAN_THREAD_ANGLE, self.tanAngle)
        
        self.calcPass(add=True)
        moveCommands.nextPass(self.passCount)
        self.runPass(True)
        self.addDone()

    def fixCut(self, offset=0.0): # thread
        if offset == 0.0:
            actual = float(jogPanel.xPos.GetValue())
            passNum = jogPanel.lastPass
            if self.internal:
                self.feed = actual - self.xStart
            else:
                self.feed = self.xStart - actual
            self.passSize[passNum] = self.feed
        else:
            pass

class ThreadPanel(wx.Panel, FormRoutines, ActionRoutines):
    def __init__(self, parent, hdrFont, *args, **kwargs):
        super(ThreadPanel, self).__init__(parent, *args, **kwargs)
        self.hdrFont = hdrFont
        FormRoutines.__init__(self)
        ActionRoutines.__init__(self, ScrewThread(self), en.OP_THREAD)
        self.InitUI()
        self.configList = None
        self.prefix = 'th'
        self.formatList = ((cf.thAddFeed, 'f'), \
                           (cf.thAlternate, None), \
                           (cf.thAngle, 'fs'), \
                           (cf.thFirstFeed, 'f'), \
                           (cf.thFirstFeedBtn, None), \
                           (cf.thInternal, None), \
                           (cf.thLastFeed, 'f'), \
                           (cf.thLastFeedBtn, None), \
                           (cf.thLeftHand, None), \
                           (cf.thMM, None), \
                           (cf.thPasses, 'd'), \
                           (cf.thPause, None), \
                           (cf.thRPM, 'd'), \
                           (cf.thSPInt, 'n'), \
                           (cf.thSpring, 'n'), \
                           (cf.thTPI, None), \
                           (cf.thThread, 'fs'), \
                           (cf.thXDepth, 'f'), \
                           (cf.thXRetract, 'f'), \
                           (cf.thRunout, 'fs'), \
                           (cf.thXStart, 'f'), \
                           (cf.thXTaper, 'f'), \
                           (cf.thZ0, 'f'), \
                           (cf.thZ1, 'f'), \
                           (cf.thZRetract, 'f'))

    def InitUI(self):
        self.sizerV = sizerV = wx.BoxSizer(wx.VERTICAL)

        txt = wx.StaticText(self, -1, "Thread", size=(120, 30))
        txt.SetFont(self.hdrFont)

        sizerV.Add(txt, flag=wx.CENTER|wx.ALL, border=2)

        self.sizerG = sizerG = wx.FlexGridSizer(cols=8, rows=0, vgap=0, hgap=0)
        
        # z parameters

        (self.z0, self.z0Txt) = \
            self.addFieldText(sizerG, "Z End", cf.thZ0)

        (self.z1, self.z1Txt) = \
            self.addFieldText(sizerG, "Z Start", cf.thZ1)

        self.zRetract = self.addField(sizerG, "Z Retract", cf.thZRetract)

        self.leftHand = self.addCheckBox(sizerG, "Left Hand", cf.thLeftHand, \
                                         action=self.OnLeftHand)

        # x parameters

        self.xStart = self.addField(sizerG, "X Start D", cf.thXStart)

        self.xRetract = self.addField(sizerG, "X Retract", cf.thXRetract)

        self.depth = self.addField(sizerG, "Depth", cf.thXDepth)

        self.alternate = self.addCheckBox(sizerG, "Alternate", cf.thAlternate)


        # self.final = btn = wx.RadioButton(self, label="Final", \
        #                                   style = wx.RB_GROUP)
        # sizerH.Add(btn, flag=wx.CENTER|wx.ALL, border=2)
        # cfg.initInfo(thFinal, btn)

        # self.depth = btn = wx.RadioButton(self, label="Depth")
        # sizerH.Add(btn, flag=wx.CENTER|wx.ALL, border=2)
        # cfg.initInfo(thDepth, btn)

        # thread parameters

        self.thread = self.addField(sizerG, "Thread", cf.thThread)

        self.tpi = self.addRadioButton(sizerG, "TPI", cf.thTPI, \
                                       style=wx.RB_GROUP)

        self.mm = self.addRadioButton(sizerG, "mm", cf.thMM)

        self.angle = self.addField(sizerG, "Angle", cf.thAngle)


        self.firstFeedBtn = self.addRadioButton(sizerG, "First Feed", \
                                                cf.thFirstFeedBtn, \
                                                style=wx.RB_GROUP, \
                                                action=self.OnFirstFeed)

        self.firstFeed = self.addField(sizerG, None, cf.thFirstFeed)

        # special thread parameters

        self.xTaper = self.addField(sizerG, "Taper", cf.thXTaper)

        self.runout = self.addField(sizerG, "Exit Rev", cf.thRunout)

        sizerG.Add(self.emptyCell)
        sizerG.Add(self.emptyCell)

        self.lastFeedBtn = self.addRadioButton(sizerG, "Last Feed", \
                                               cf.thLastFeedBtn, \
                                               action=self.OnLastFeed)

        self.lastFeed = self.addField(sizerG, None, cf.thLastFeed)

        # pass info

        self.passes = self.addField(sizerG, "Passes", cf.thPasses)
        self.passes.SetEditable(False)

        self.sPInt = self.addField(sizerG, "SP Int", cf.thSPInt)

        self.spring = self.addField(sizerG, "Spring", cf.thSpring)

        self.internal = self.addCheckBox(sizerG, "Internal", cf.thInternal, \
                                         action=self.OnInternal)

        # buttons

        self.addButton(sizerG, 'Send', self.OnSend)

        self.addButton(sizerG, 'Start', self.OnStart)

        self.addButton(sizerG, 'Add', self.OnAdd)

        self.add = self.addField(sizerG, None, cf.thAddFeed)

        self.rpm = self.addField(sizerG, "RPM", cf.thRPM)

        self.pause = self.addCheckBox(sizerG, "Pause", cf.thPause)

        sizerV.Add(sizerG, flag=wx.CENTER|wx.ALL, border=2)

        self.SetSizer(sizerV)
        self.sizerV.Fit(self)

    def update(self):
        self.formatData(self.formatList)
        self.updateLeftHand()
        self.updateFirstFeed()
        self.updateLastFeed()
        self.sizerV.Layout()
        jogPanel.setPassText("Feed")

    def updateFirstFeed(self):
        if self.firstFeedBtn.GetValue():
            self.firstFeed.SetEditable(True)
            self.lastFeed.SetEditable(False)

    def updateLastFeed(self):
        if self.lastFeedBtn.GetValue():
            self.lastFeed.SetEditable(True)
            self.firstFeed.SetEditable(False)

    def updateLeftHand(self):
        if self.leftHand.GetValue():
            self.z0Txt.SetLabel("Z Start")
            self.z1Txt.SetLabel("Z End")
        else:
            self.z0Txt.SetLabel("Z End")
            self.z1Txt.SetLabel("Z Start")

    def OnLeftHand(self, e):
        self.updateLeftHand()
        self.sizerV.Layout()

    def OnInternal(self, e):
        pass

    def OnFirstFeed(self, e):
        self.updateFirstFeed()

    def OnLastFeed(self, e):
        self.updateLastFeed()

    def sendData(self):
        moveCommands.queClear()
        sendClear()
        sendSpindleData()
        sendZData()
        sendXData()

    def sendAction(self):
        self.sendData()
        return(self.control.runOperation())

    def startAction(self):      # thread
        comm.command(cm.CMD_RESUME)
        control = self.control
        if control.add:
            if jogPanel.mvStatus & ct.MV_READ_X:
                control.fixCut()
        else:
            if cfg.getBoolInfoData(cf.cfgDbgSave):
                updateThread.openDebug()

    def addAction(self):
        self.control.addPass()

class ButtonRepeat(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.threadRun = True
        self.threadDone = False
        self.event = Event()
        self.action = None
        self.code = None
        self.val = None
        # self.jogCode = None
        # self.repeat = 0
        self.start()

    def run(self):
        while True:
            flag = True
            timeout = .25
            self.event.wait(.2)
            if not self.threadRun:
                break
            while self.event.isSet():
                if flag:
                    flag = False
                    print("buttonRepeat running %s" % (self.action))
                    stdout.flush()
                if self.action is not None:
                    self.action(self.code, self.val)
                sleep(timeout)
                timeout = .05
        print("ButtonRepeat done")
        stdout.flush()
        self.threadDone = True

    def close(self):
        self.threadRun = False

EVT_KEYPAD_ID = wx.Window.NewControlId()

class KeypadEvent(wx.PyEvent):
    def __init__(self, data):
        wx.PyEvent.__init__(self)
        self.SetEventType(EVT_KEYPAD_ID)
        self.data = data
    
class Keypad(Thread):
    def __init__(self, port, rate):
        if port is None:
            return
        if len(port) == 0:
            return
        Thread.__init__(self)
        self.threadRun = True
        self.threadDone = False
        self.port = port
        self.rate = rate
        try:
            self.ser = serial.Serial(port, rate, timeout=1)
        except IOError:
            print("unable to open port %s" % (port))
            stdout.flush()
            self.ser = None

        self.start()

    def run(self):
        prtErr = True
        while self.threadRun:
            if self.ser is not None:
                try:
                    tmp = str(self.ser.read(1))
                except serial.SerialException:
                    self.ser = None
                    pass
                if len(tmp) != 0:
                    wx.PostEvent(jogPanel, KeypadEvent(ord(tmp[0])))
            else:
                try:
                    self.ser = serial.Serial(self.port, self.rate, timeout=1)
                    prtErr = True
                except IOError:
                    if prtErr:
                        print("unable to open port %s" % (self.port))
                        prtErr = False
                    stdout.flush()
                    self.ser = None
                    sleep(5)
        print("Keypad done")
        stdout.flush()
        self.threadDone = True

    def close(self):
        self.threadRun = False

class JogShuttle(Thread):
    def __init__(self):
        allHids = None
        self.threadRun = True
        self.threadDone = False
        self.device = None
        if WINDOWS:
            allHids = find_all_hid_devices()
        if allHids:
            for index, device in enumerate(allHids):
                if device.vendor_id == 0xb33 and \
                   device.product_id == 0x20:
                    try:
                        self.device = device
                        device.open()
                        device.set_raw_data_handler(self.ShuttleInput)
                        self.run
                    except:
                        traceback.print_exc()
                    break
        if self.device == None:
            self.threadDone = True
            return

        self.lastOuterRing = 0
        self.lastKnob = None
        self.lastButton = 0
        self.buttonAction = ((16, self.setZ), \
                             (32, self.setX))
        if STEP_DRV:
            self.buttonAction += ((64, self.setSpindle),)
        else:
            self.buttonAction += ((64, None),)
        self.buttonAction += ((128, None), \
                              (1, None))
        self.axisAction = None
        self.factor = (0.00, 0.01, 0.02, 0.05, 0.10, 0.20, 0.50, 1.00)

        self.zSpeed = [None, None, None, None, None, None, None, None]
        self.zCurSpeed = 0.0

        self.xSpeed = [None, None, None, None, None, None, None, None]
        self.xCurSpeed = 0.0

        self.spindleSpeed = [None, None, None, None, None, None, None, None]
        self.spindleCurSpeed = 0.0

        self.start()

    def run(self):
        t = 1
        while True:
            if not self.threadRun:
                break

            if self.device is not None:
                if not self.device.is_plugged():
                    print("shuttle unplugged");
                    stdout.flush()
                    self.device = None
                    t = 5
            else:
                allHids = find_all_hid_devices()
                if allHids:
                    for index, device in enumerate(allHids):
                        if device.vendor_id == 0xb33 and \
                           device.product_id == 0x20:
                            try:
                                self.device = device
                                device.open()
                                device.set_raw_data_handler(self.KeypadInput)
                                print("open shuttle");
                                stdout.flush()
                                t = 1
                            except:
                                traceback.print_exc()
            sleep(t)
        print("JogShuttle done")
        stdout.flush()
        self.threadDone = True

    def close(self):
        self.threadRun = False

        # 0.0 0.5 1.0 5.0 10.0 20.0 150.0 240.0

    def ShuttleInput(self, data):
        print(data)
        stdout.flush()
        outerRing = data[1]
        if outerRing != self.lastOuterRing:
            self.lastOuterRing = outerRing
            if self.axisAction is not None:
                if outerRing > 128:
                    outerRing = -(256 - outerRing)
                print("outerRing %d self.axisAction %s" % \
                      (outerRing, self.axisAction))
                self.axisAction(0, outerRing)
                buttonRepeat.action = self.axisAction
                buttonRepeat.code = 0
                buttonRepeat.val = outerRing
                if outerRing != 0:
                    buttonRepeat.event.set()
                    print("buttonRepeat.event.set()")
                    stdout.flush()
        knob = data[2]
        if knob != self.lastKnob:
            if self.lastKnob is not None:
                pass
            self.lastKnob = knob
        button = data[4] | data[5]
        if button | self.lastButton:
            changed = button ^ self.lastButton
            for action in self.buttonAction:
                (val, function) = action
                if changed & val:
                    if function is not None:
                        function(button, val)
            self.lastButton = button

    def setZ(self, button, val):
        if button & val:
            self.axisAction = self.jogZ
            maxSpeed = cfg.getFloatInfoData(cf.zMaxSpeed)
            for val in range(len(self.factor)):
                self.zSpeed[val] = maxSpeed * self.factor[val]
            # print("set z")
            # stdout.flush()

    def setX(self, button, val):
        if button & val:
            self.axisAction = self.jogX
            maxSpeed = cfg.getFloatInfoData(cf.xMaxSpeed)
            for val in range(len(self.factor)):
                self.xSpeed[val] = maxSpeed * self.factor[val]
            # print("set x")
            # stdout.flush()

    def setSpindle(self, button, val):
        if button & val:
            self.axisAction = self.jogSpindle
            maxSpeed = cfg.getFloatInfoData(cf.spMaxRPM)
            for val in range(len(self.factor)):
                self.spindleSpeed[val] = \
                    maxSpeed * self.factor[val]
            # print("set spindle")
            # stdout.flush()

    def jogDone(self, cmd):
            buttonRepeat.action = None
            buttonRepeat.event.clear()
            self.xCurIndex = -1
            try:
                comm.command(cmd)
            except CommTimeout:
                commTimeout()

    def jogZ(self, code, val):
        if val == 0:
            self.jogDone(cm.ZSTOP)
            
            print("jogZ done")
            stdout.flush()
        else:
            index = abs(val)
            speed = self.zSpeed[index]
            if val < 0:
                speed = -speed
            print("jog z val %2d speed %7.4f" % (val, speed))
            stdout.flush()
            try:
                if self.zCurSpeed != speed:
                    self.zCurSpeed = speed
                    comm.setParm(pm.Z_JOG_SPEED, speed)
                comm.command(cm.ZJSPEED)
            except CommTimeout:
                commTimeout()

    def jogX(self, code, val):
        if val == 0:
            self.jogDone(cm.XSTOP)
            print("jogX done")
            stdout.flush()
        else:
            index = abs(val)
            speed = self.xSpeed[index]
            if val > 0:
                speed = -speed
            print("jog x val %2d speed %7.4f" % (val, speed))
            stdout.flush()
            try:
                if self.xCurSpeed != speed:
                    self.xCurSpeed = speed
                    comm.setParm(pm.X_JOG_SPEED, speed)
                comm.command(cm.XJSPEED)
            except CommTimeout:
                commTimeout()

    def jogSpindle(self, code, val):
        if val == 0:
            self.jogDone(cm.SPINDLE_STOP)
            print("jogSpindle done")
            stdout.flush()
        else:
            index = abs(val)
            speed = self.spindleSpeed[index]
            if val < 0:
                speed = -speed
            print("jog spindle val %2d %d" % (val, speed))
            stdout.flush()
            try:
                if self.spindleCurSpeed != speed:
                    self.spindleCurSpeed = speed
                    comm.setParm(pm.SP_JOG_RPM, speed)
                comm.command(cm.SPINDLE_JOG_SPEED)
            except CommTimeout:
                commTimeout()

class JogPanel(wx.Panel, FormRoutines):
    def __init__(self, parent, *args, **kwargs):
        global buttonRepeat
        super(JogPanel, self).__init__(parent, *args, **kwargs)
        FormRoutines.__init__(self, False)
        self.Connect(-1, -1, EVT_UPDATE_ID, self.OnUpdate)
        self.Connect(-1, -1, EVT_KEYPAD_ID, self.keypadEvent)
        # self.Bind(wx.EVT_CHAR_HOOK, self.OnCharHook)
        self.jogCode = None
        self.repeat = 0
        self.btnRpt = buttonRepeat = ButtonRepeat()
        self.surfaceSpeed = cfg.newInfo(cf.jpSurfaceSpeed, False)
        self.fixXPosDialog = None
        self.xHome = False
        self.probeAxis = 0
        self.probeLoc = 0.0
        self.probeStatus = 0
        self.mvStatus = 0
        self.lastPass = 0
        self.currentPanel = None
        self.currentControl = None
        self.lastZOffset = 0.0
        self.lastXOffset = 0.0
        self.zStepsInch = 0
        self.xStepsInch = 0
        self.zPosition = None
        self.zHomeOffset = None
        self.xPosition = None
        self.xHomeOffset = None
        if DRO:
            self.zDROInch = 0
            self.xDROInch = 0
            self.zDROPostition = None
            self.zDROOffset = None
            self.xDROPostition = None
            self.xDROOffset = None
            # self.xDroDiam = False
            self.xDroDiam = cfg.newInfo(cf.jpXDroDiam, False)
        self.overrideSet = False

        if not os.path.exists(DBG_DIR):
            os.makedirs(DBG_DIR)
        self.dbg = open(DBG_LOG, "ab")
        t = strftime("\n%a %b %d %Y %H:%M:%S\n", localtime())
        self.dbg.write(t.encode())
        self.dbg.flush()

        eventTable = (\
                      (en.EV_ZLOC, self.updateZ), \
                      (en.EV_XLOC, self.updateX), \
                      (en.EV_RPM, self.updateRPM), \
                      (en.EV_READ_ALL, self.updateAll), \
                      (en.EV_ERROR, self.updateError), \
                      )

        self.procUpdate = [None for i in range(en.EV_MAX)]
        for (event, action) in eventTable:
            self.procUpdate[event] = action

        self.initKeyTable()
        self.initKeypadTable()
        self.initUI()

    def OnCharHook(self, e):
        code = e.GetUnicodeKey()
        if code != wx.WXK_NONE:
            print("code %c" % (code,))
        else:
            code = e.GetKeyCode()
            print("code %c" % code)
        stdout.flush()
        e.Skip()

    def postUpdate(self, result):
        wx.PostEvent(self, UpdateEvent(result))
        
    def OnUpdate(self, e):
        index = e.data[0]
        if index < len(self.procUpdate):
            update = self.procUpdate[index]
            if update is not None:
                val = e.data[1:]
                if len(val) == 1:
                    val = val[0]
                update(val)

    def close(self):
        if self.dbg is not None:
            self.dbg.close()
            self.dbg = None

    def dPrt(self, text, console=False, flush=False):
        self.dbg.write(text.encode())
        if flush:
            self.dbg.flush()
        if console:
            print(text, end='')
            if flush:
                stdout.flush
                
    def initUI(self):
        self.Bind(wx.EVT_LEFT_UP, self.OnMouseEvent)

        sizerV = wx.BoxSizer(wx.VERTICAL)

        sizerG = wx.FlexGridSizer(cols=6, rows=0, vgap=0, hgap=0)

        self.txtFont = txtFont = wx.Font(16, wx.MODERN, wx.NORMAL, \
                                         wx.NORMAL, False, u'Consolas')
        self.posFont = posFont = wx.Font(20, wx.MODERN, wx.NORMAL, \
                                         wx.NORMAL, False, u'Consolas')
        # first row
        # z position

        self.zPos = \
            self.addDialogField(sizerG, "Z", "0.0000", txtFont, \
                                posFont, (130, -1), border=(10, 2), \
                                edit=False, index=cf.jogZPos)
        self.zPos.Bind(wx.EVT_RIGHT_DOWN, self.OnZMenu)

        # x Position

        self.xPos = \
            self.addDialogField(sizerG, "X", "0.0000", txtFont, \
                                posFont, (130, -1), border=(10, 2), \
                                edit=False, index=cf.jogXPos)
        self.xPos.Bind(wx.EVT_RIGHT_DOWN, self.OnXMenu)

        # rpm

        (self.rpm, self.rpmText) = \
            self.addDialogField(sizerG, "RPM", "0", txtFont, \
                                posFont, (80, -1), border=(10, 2), \
                                edit=False, text=True)
        self.rpm.Bind(wx.EVT_RIGHT_DOWN, self.OnRpmMenu)
        self.setSurfaceSpeed()

        # second row
        # pass size
        
        (self.passSize, self.passText) = \
            self.addDialogField(sizerG, "Size", "0.000", txtFont, \
                                posFont, (130, -1), border=(10,2), \
                                edit=False, text=True)
        # x diameter

        self.xPosDiam = \
            self.addDialogField(sizerG, "X D", "0.0000", txtFont, \
                                posFont, (130, -1), border=(10, 2), \
                                edit=False)
        self.xPosDiam.Bind(wx.EVT_RIGHT_DOWN, self.OnXMenu)

        # pass

        self.curPass = \
            self.addDialogField(sizerG, "Pass", "0", txtFont, \
                                posFont, (80, -1), border=(10, 2), \
                                edit=False)

        if DRO:
            # third row
            # z dro position

            self.zDROPos = \
                self.addDialogField(sizerG, "Z", "0.0000", txtFont, \
                                    posFont, (130, -1), border=(10, 2), \
                                    edit=False, index=cf.droZPos)
            self.zDROPos.Bind(wx.EVT_RIGHT_DOWN, self.OnZMenu)

            # x dro Position

            self.xDROPos = \
                self.addDialogField(sizerG, "X", "0.0000", txtFont, \
                                    posFont, (130, -1), border=(10, 2), \
                                    edit=False, index=cf.droXPos)
            self.xDROPos.Bind(wx.EVT_RIGHT_DOWN, self.OnXMenu)

        sizerV.Add(sizerG, flag=wx.ALIGN_CENTER_VERTICAL|wx.CENTER|wx.ALL, \
                   border=2)

        # status line

        sizerH = wx.BoxSizer(wx.HORIZONTAL)

        self.statusText = txt = wx.StaticText(self, -1, "", size=(80, -1), \
                                              style=wx.ST_NO_AUTORESIZE)
        txt.SetFont(txtFont)
        sizerH.Add(txt, flag=wx.ALL|wx.ALIGN_LEFT| \
                   wx.ALIGN_CENTER_VERTICAL, border=2)

        self.statusLine = txt = wx.StaticText(self, -1, "", size=(300, -1))
        txt.SetFont(txtFont)
        sizerH.Add(txt, flag=wx.ALL|wx.ALIGN_LEFT| \
                   wx.ALIGN_CENTER_VERTICAL, border=2)

        txt = wx.StaticText(self, -1, "Limit Override ")
        sizerH.Add(txt, flag=wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, \
                   border=2)

        self.limitOverride = cb = wx.CheckBox(self, -1)
        self.Bind(wx.EVT_CHECKBOX, self.OnOverride, cb)
        sizerH.Add(cb, flag=wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, \
                   border=2)

        sizerV.Add(sizerH)

        # control buttons and jog

        btnSize = wx.DefaultSize

        sizerH = wx.BoxSizer(wx.HORIZONTAL)

        sizerG = wx.FlexGridSizer(cols=3, rows=0, vgap=0, hgap=0)

        # first line

        self.addButton(sizerG, 'E Stop', self.OnEStop, btnSize)

        self.addButton(sizerG, 'Pause', self.OnPause, btnSize)

        if STEP_DRV:
            self.addControlButton(sizerG, 'Jog Spindle +', \
                                  self.OnJogSpindleFwd, self.OnJogUp)
        else:
            sizerG.Add(self.emptyCell)

        # second line

        self.addButton(sizerG, 'Stop', self.OnStop, btnSize)

        self.addButton(sizerG, 'Measure', self.OnMeasure, btnSize)

        if STEP_DRV:
            self.addControlButton(sizerG, 'Jog Spindle -', \
                                  self.OnJogSpindleRev, self.OnJogUp)
        else:
            sizerG.Add(self.emptyCell)

        # third line

        self.addButton(sizerG, 'Done', self.OnDone, btnSize)

        self.addButton(sizerG, 'Resume', self.OnResume, btnSize)

        if STEP_DRV or MOTOR_TEST or SPINDLE_SWITCH or SPINDLE_VAR_SPEED:
            self.addButton(sizerG, 'Start Spindle', \
                           self.OnStartSpindle, btnSize)
        else:
            sizerG.Add(self.emptyCell)

        sizerH.Add(sizerG)

        sizerG = wx.FlexGridSizer(cols=5, rows=0, vgap=0, hgap=0)
        sFlag = wx.ALL|wx.CENTER|wx.ALIGN_CENTER_VERTICAL

        # first row

        sizerG.Add(self.emptyCell)
        sizerG.Add(self.emptyCell)
        sizerG.Add(self.emptyCell)

        self.xNegButton = \
            self.addBitmapButton(sizerG, "north.gif", self.OnXNegDown, \
                                 self.OnXUp, flag=sFlag|wx.EXPAND)
        sizerG.Add(self.emptyCell)

        # second row

        self.zNegButton = \
            self.addBitmapButton(sizerG, "west.gif", self.OnZNegDown, \
                                 self.OnZUp, flag=sFlag)

        self.addButton(sizerG, 'S', self.OnZSafe, style=wx.BU_EXACTFIT, \
                       size=btnSize, flag=sFlag)

        self.zPosButton = \
            self.addBitmapButton(sizerG, "east.gif", self.OnZPosDown, \
                                 self.OnZUp, flag=sFlag)

        self.addButton(sizerG, 'S', self.OnXSafe, style=wx.BU_EXACTFIT, \
                       size=btnSize, flag=sFlag)

        self.step = step = ["Cont", "0.0001", "0.0002", "0.0005", \
                            "0.001", "0.002", "0.005", \
                            "0.010", "0.020", "0.050", \
                            "0.100", "0.200", "0.500", "1.000"]

        self.combo = combo = wx.ComboBox(self, -1, step[1], choices=step, \
                                         style=wx.CB_READONLY)
        cfg.initInfo(cf.jogInc, combo)
        combo.Bind(wx.EVT_COMBOBOX, self.OnCombo)
        combo.Bind(wx.EVT_KEY_DOWN, self.OnKeyDown)
        combo.Bind(wx.EVT_KEY_UP, self.OnKeyUp)
        combo.Bind(wx.EVT_CHAR, self.OnKeyChar)
        combo.Bind(wx.EVT_SET_FOCUS, self.OnSetFocus)
        combo.Bind(wx.EVT_KILL_FOCUS, self.OnKillFocus)
        combo.SetFocus()
        sizerG.Add(combo, flag=sFlag, border=2)

        # third row

        sizerG.Add(self.emptyCell)

        self.addButton(sizerG, 'P', self.OnZPark, style=wx.BU_EXACTFIT, \
                       size=btnSize, flag=sFlag)

        sizerG.Add(self.emptyCell)

        self.xPosButton = \
            self.addBitmapButton(sizerG, "south.gif", self.OnXPosDown,
                                 self.OnXUp, flag=sFlag|wx.EXPAND)

        self.addButton(sizerG, 'P', self.OnXPark, style=wx.BU_EXACTFIT, \
                       size=btnSize, flag=sFlag|wx.ALIGN_CENTER_HORIZONTAL)

        sizerH.Add(sizerG)

        sizerV.Add(sizerH, flag=wx.ALIGN_CENTER_VERTICAL|wx.CENTER|wx.ALL, \
                   border=2)

        self.SetSizer(sizerV)
        sizerV.Fit(self)

    def update(self):
        self.setSurfaceSpeed()

    def setPassText(self, txt):
        self.passText.SetLabel(txt)

    def setSurfaceSpeed(self, val=None):
        if val is not None:
            self.surfaceSpeed.value = val
        if self.surfaceSpeed.value:
            self.rpmText.SetLabel("FPM")
        else:
            self.rpmText.SetLabel("RPM")

    def menuPos(self, e, ctl):
        (xPos, yPos) = ctl.GetPosition()
        if e is not None:
            (x, y) = e.GetPosition()
            xPos += x
            yPos += y
        return(xPos, yPos)

    def OnZMenu(self, e):
        menu = PosMenu(self, AXIS_Z)
        self.PopupMenu(menu, self.menuPos(e, self.zPos))
        menu.Destroy()

    def OnXMenu(self, e):
        menu = PosMenu(self, AXIS_X)
        self.PopupMenu(menu, self.menuPos(e, self.xPos))
        menu.Destroy()
        
    def OnRpmMenu(self, e):
        menu = RpmMenu(self)
        self.PopupMenu(menu, self.menuPos(e, self.xPos))
        menu.Destroy()
        
    def focus(self):
        self.combo.SetFocus()

    def getInc(self):
        val = self.combo.GetValue()
        # print("combo %d" % (self.combo.GetSelection()))
        # stdout.flush()
        return(val)

    def OnZSafe(self, e):
        panel = self.getPanel()
        (z, x) = panel.getSafeLoc()
        comm.queParm(pm.Z_MOVE_POS, z)
        comm.queParm(pm.Z_HOME_OFFSET, round(zHomeOffset * jogPanel.zStepsInch))
        comm.queParm(pm.Z_FLAG, ct.CMD_MAX)
        comm.command(cm.ZMOVEABS)
        self.combo.SetFocus()

    def OnZPark(self, e):
        comm.queParm(pm.Z_MOVE_POS, cfg.getFloatInfoData(cf.zParkLoc))
        comm.queParm(pm.Z_HOME_OFFSET, round(zHomeOffset * jogPanel.zStepsInch))
        comm.queParm(pm.Z_FLAG, ct.CMD_MAX)
        comm.command(cm.ZMOVEABS)
        self.combo.SetFocus()

    def OnXSafe(self, e):
        panel = self.getPanel()
        (z, x) = panel.getSafeLoc()
        comm.queParm(pm.X_MOVE_POS, x)
        comm.queParm(pm.X_HOME_OFFSET, round(xHomeOffset * jogPanel.xStepsInch))
        comm.queParm(pm.X_FLAG, ct.CMD_MAX)
        comm.command(cm.XMOVEABS)
        self.combo.SetFocus()

    def OnXPark(self, e):
        comm.queParm(pm.X_MOVE_POS, cfg.getFloatInfoData(cf.xParkLoc))
        comm.queParm(pm.X_HOME_OFFSET, round(xHomeOffset * jogPanel.xStepsInch))
        comm.queParm(pm.X_FLAG, ct.CMD_MAX)
        comm.command(cm.XMOVEABS)
        self.combo.SetFocus()

    def zJogCmd(self, code, val):
        self.repeat += 1
        sendZData()
        if val == 'Cont':
            if self.jogCode != code: # new jog code
                if self.jogCode is None: # jogging stopped
                    self.jogCode = code
                    self.repeat = 0
                    direction = 1
                    if code == wx.WXK_LEFT:
                        direction = -1
                    print("zJogCmd %d" % (direction))
                    try:
                        comm.queParm(pm.Z_JOG_MAX, cfg.getInfoData(cf.zJogMax))
                        comm.queParm(pm.Z_JOG_DIR, direction)
                        comm.command(cm.ZJMOV)
                    except CommTimeout:
                        commTimeout()
            else:
                try:
                    comm.command(cm.ZJMOV)
                except CommTimeout:
                    commTimeout()
        else:
            if self.jogCode is None:
                self.jogCode = code
                if code == wx.WXK_LEFT:
                    val = '-' + val
                print("zJogCmd %s" % (val))
                stdout.flush()
                try:
                    comm.queParm(pm.Z_FLAG, ct.CMD_JOG)
                    comm.queParm(pm.Z_MOVE_DIST, val)
                    comm.command(cm.ZMOVEREL)
                except CommTimeout:
                    commTimeout()

    def jogDone(self, cmd):
        self.jogCode = None
        val = self.getInc()
        if val == "Cont":
            print("jogDone %d" % (self.repeat))
            stdout.flush()
            try:
                comm.command(cmd)
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
        print("OnZUp")
        stdout.flush()
        val = self.getInc()
        if val == "Cont":
            self.btnRpt.event.clear()
            self.btnRpt.action = None
            self.jogDone(cm.ZSTOP)
        self.jogCode = None
        self.combo.SetFocus()

    def OnZNegDown(self, e):
        self.zNegButton.SetFocus()
        self.zDown(wx.WXK_LEFT)

    def OnZPosDown(self, e):
        print("OnZPosDown")
        stdout.flush()
        self.zPosButton.SetFocus()
        print("OnZPosDown focus")
        stdout.flush()
        self.zDown(wx.WXK_RIGHT)
        print("zDown")
        stdout.flush()

    def xJogCmd(self, code, val):
        self.repeat += 1
        sendXData()
        if val == 'Cont':
            if self.jogCode != code:
                if self.jogCode is None:
                    self.jogCode = code
                    self.repeat = 0
                    direction = 1
                    if code == wx.WXK_UP:
                        direction = -1
                    print("xJogCmd %d" % (direction))
                    stdout.flush()
                    try:
                        comm.queParm(pm.X_JOG_MAX, cfg.getInfoData(cf.xJogMax))
                        comm.queParm(pm.X_JOG_DIR, direction)
                        comm.command(cm.XJMOV)
                    except CommTimeout:
                        commTimeout()
            else:
                try:
                    comm.command(cm.XJMOV)
                except CommTimeout:
                    commTimeout()
        else:
            if self.jogCode is None:
                self.jogCode = code
                if code == wx.WXK_UP:
                    val = '-' + val
                print("xJogCmd %s" % (val))
                stdout.flush()
                try:
                    flag = ct.CMD_JOG | ((ct.DRO_POS | ct.DRO_UPD) \
                                         if X_DRO_POS else 0)
                    comm.queParm(pm.X_FLAG, flag)
                    comm.queParm(pm.X_MOVE_DIST, val)
                    comm.command(cm.XMOVEREL)
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
            self.jogDone(cm.XSTOP)
        self.jogCode = None
        self.combo.SetFocus()

    def OnXPosDown(self, e):
        self.xPosButton.SetFocus()
        self.xDown(wx.WXK_DOWN)

    def OnXNegDown(self, e):
        self.xNegButton.SetFocus()
        self.xDown(wx.WXK_UP)

    def OnCombo(self, e):
        val = self.combo.GetValue()
        print("combo val %s" % (val))
        try:
            val = float(val)
            if val > 0.020:
                val = 0.020
        except ValueError:
            val = 0.0
        comm.queParm(pm.Z_MPG_INC, round(val * self.zStepsInch))
        comm.queParm(pm.X_MPG_INC, round(val * self.xStepsInch))
        comm.sendMulti()

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
        elif code == wx.WXK_NUMPAD_PAGEUP:
            self.spindleJogCmd(code, 1)
            return
        # print("key down %x" % (code))
        # stdout.flush()
        evt.Skip()

    def OnKeyUp(self, evt):
        code = evt.GetKeyCode()
        if code == wx.WXK_LEFT:
            self.jogDone(cm.ZSTOP)
            return
        elif code == wx.WXK_RIGHT:
            self.jogDone(cm.ZSTOP)
            return
        elif code == wx.WXK_UP:
            self.jogDone(cm.XSTOP)
            return
        elif code == wx.WXK_DOWN:
            self.jogDone(cm.XSTOP)
            return
        elif code == wx.WXK_NUMPAD_PAGEDOWN:
            comm.command(cm.SPINDLE_STOP)
            return
        elif code == wx.WXK_NUMPAD_PAGEUP:
            comm.command(cm.SPINDLE_STOP)
            return
        # print("key up %x" % (code))
        # stdout.flush()
        evt.Skip()

    def initKeypadTable(self):
        keypadTable = (\
                       (ord('a'), (self.OnEStop, None)), \
                       (ord('b'), (self.OnStop, None)), \
                       (ord('c'), (self.OnStartSpindle, None)), \
                       (ord('d'), self.noAction), \

                       (ord('e'), self.start), \
                       (ord('f'), (self.OnResume, None)), \
                       (ord('g'), (self.OnPause, None)), \
                       (ord('h'), (self.OnDone, None)), \

                       (ord('i'), self.noAction), \
                       (ord('j'), self.noAction), \
                       (ord('k'), self.noAction), \
                       (ord('l'), self.noAction), \

                       (ord('m'), self.noAction), \
                       (ord('n'), self.noAction), \
                       (ord('o'), self.noAction), \
                       (ord('p'), self.noAction), \
        )
        self.keypadTable = {}
        for (key, action) in keypadTable:
            self.keypadTable[key] = action

    def keypadEvent(self, event):
        code = event.data
        if code in self.keypadTable:
            action = self.keypadTable[code]
            if isinstance(action, tuple):
                (action, arg) = action
                action(arg)
            else:
                action()

    def noAction(self):
        pass

    def initKeyTable(self):
        keyTable = (\
                    (ord('c'), self.comboCont), \
                    (ord('i'), self.comboInc), \
                    (ord('I'), self.comboDec), \
                    (ord('r'), self.start), \
                    (ord('s'), (self.OnResume, None)), \
                    (ord('p'), (self.OnPause, None)), \
                    (ord('d'), (self.OnDone, None)), \

                    (ord('n'), self.nextOperation), \
                    (ord('a'), self.add), \
                    (ord('A'), self.addFocus), \
                    (ord('f'), self.focusPanel), \
                    (ord('P'), self.togglePause), \

                    (wx.WXK_F9, (self.OnStartSpindle, None)), \
                    (wx.WXK_ESCAPE, (self.OnStop, None)), \
                    (ord('z'), (self.OnZMenu, None)), \
                    (ord('x'), (self.OnXMenu, None)), \
                    (ord('R'), (self.OnRpmMenu, None)), \
                    (ord('C'), (self.setStatus, st.STR_CLR)), \
                    (ord('?'), self.help), \
        )
        self.keyTable = {}
        for (key, action) in keyTable:
            self.keyTable[key] = action

    def comboCont(self):
        self.combo.SetSelection(0)
        self.OnCombo(None)

    def comboInc(self):
        combo = self.combo
        val = combo.GetSelection()
        if val == 0:
            combo.SetSelection(1)
        else:
            combo.SetSelection(1) if val >= len(self.step) - 1 else \
                combo.SetSelection(val + 1)
        self.OnCombo(None)

    def comboDec(self):
        combo = self.combo
        val = combo.GetSelection()
        if val > 0:
            if val > 1:
                combo.SetSelection(val - 1)
        self.OnCombo(None)

    def start(self):
        panel = mainFrame.getCurrentPanel()
        panel.OnSend(None)

    def nextOperation(self):
        panel = mainFrame.getCurrentPanel()
        panel.nextOperation()

    def add(self):
        panel = mainFrame.getCurrentPanel()
        panel.OnAdd(None)

    def addFocus(self):
        panel = mainFrame.getCurrentPanel()
        panel.setAddFocus()

    def focusPanel(self):
        panel = mainFrame.getCurrentPanel()
        panel.setFocus()

    def togglePause(self):
        panel = mainFrame.currentPanel
        val = panel.pause.GetValue()
        panel.pause.SetValue(not val)

    def help(self):
        dialog = HelpDialog(mainFrame)
        mainFrame.showDialog(dialog)

    def OnKeyChar(self, evt):
        code = evt.GetKeyCode()
        if code in self.keyTable:
            action = self.keyTable[code]
            if isinstance(action, tuple):
                (action, arg) = action
                action(arg)
            else:
                action()
        else:
            print("key char %x" % (code))
            stdout.flush()
            evt.Skip()

    def testPass(self, passNum, curLoc, retract=None, pause=True, axis=AXIS_X):
        m = moveCommands
        m.nextPass(passNum)
        m.moveX(curLoc) if axis == AXIS_X else m.moveZ(curLoc)
        if DRO:
            m.saveXDro() if axis == AXIS_X else m.saveZDro()
        if pause:
            m.quePause()
        if retract is not None:
            m.moveX(curLoc + retract) if axis == AXIS_X else \
                m.moveZ(curLoc + retract)
            if DRO:
                m.saveXDro() if axis == AXIS_X else m.saveZDro()

    def axisTest(self, inc=0.025, passes=10, retract=None, \
              pause=True, axis=AXIS_X):
        if cfg.getBoolInfoData(cf.cfgDbgSave):
            updateThread.openDebug("dbg_%s.txt" % \
                                   ("x" if axis == AXIS_X else "z"))
        if retract is not None:
            retract = abs(retract) if inc < 0.0 else -abs(retract)
        jogPanel.dPrt("\naxisTest inc %7.4f%s\n" % \
                      (inc, "" if retract is None else \
                       " retract %7.4f" % (retract)), flush=True)
        m = moveCommands
        m.queClear()
        m.quePause(ct.PAUSE_ENA_X_JOG | ct.PAUSE_ENA_Z_JOG)
        m.done(ct.PARM_START)
        if axis == AXIS_X:
            curLoc = float(self.xPosition.value) / self.xStepsInch - xHomeOffset
            m.saveXOffset()
        else:
            curLoc = float(self.zPosition.value) / self.zStepsInch - zHomeOffset
            m.saveZOffset()
        jogPanel.dPrt("curLoc %7.4f\n" % (curLoc), console=True)

        passNum = 0
        self.testPass(99, curLoc + (0.050 if inc < 0 else -0.050), \
                      pause=pause, axis=axis)
        self.testPass(passNum, curLoc, pause=pause, axis=axis)

        for i in range(passes):
            passNum += 1
            curLoc += inc
            print("pass %2d curLoc %7.4f" % (passNum, curLoc))
            self.testPass(passNum, curLoc, retract, pause, axis)
        m.done(ct.PARM_DONE)            

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
        if probeLoc is not None:
            self.probeLoc = probeLoc

    def homeDone(self, status):
        self.xHome = False
        self.probeStatus = 0
        print(status)
        stdout.flush()

    def updateAll(self, val):
        global zHomeOffset, xHomeOffset, xHomed
        if len(val) == 7:
            (z, x, rpm, curPass, zDROPos, xDROPos, mvStatus) = val
            if z != '#':
                self.zPosition.value = z
                zLocation = float(z) / self.zStepsInch
                self.zPos.SetValue("%0.4f" % (zLocation - zHomeOffset))
            if x != '#':
                self.xPosition.value = x
                xLocation = float(x) / self.xStepsInch - xHomeOffset
                self.xPos.SetValue("%0.4f" % (xLocation))
                self.xPosDiam.SetValue("%0.4f" % (abs(xLocation * 2)))
            if not self.surfaceSpeed.value:
                self.rpm.SetValue(str(rpm))
            else:
                fpm = (float(rpm) * abs(xLocation) * 2 * pi) / 12.0
                self.rpm.SetValue("%1.0f" % (fpm))

            val = int(curPass)
            passNum = val & 0xff
            passType = val >> 8
            if passType == 0:
                self.lastPass = passNum
                curPass = str(passNum)
                passSize = self.currentPanel.control.passSize
                if len(passSize) > passNum:
                    self.passSize.SetValue("%0.4f" % \
                        (passSize[passNum]))
                else:
                    self.passSize.SetValue("0.000")
            elif passType == 1:
                curPass = str(passNum) + "S"
            else:
                curPass = "%dS%d" % (self.lastPass, passNum)
            self.curPass.SetValue(curPass)

            if DRO:
                zDROPos = int(zDROPos)
                self.zDROPosition.value = zDROPos
                zDroLoc = float(zDROPos) / self.zDROInch
                if self.lastZOffset != zDROOffset:
                    self.lastZOffset = zDROOffset
                    print("zDROPos %d %0.4f zDROOffset %0.4f" % \
                          (zDROPos, zDroLoc, zDROOffset))
                    stdout.flush()
                zDroLoc = zDroLoc - zDROOffset
                self.zDROPos.SetValue("%0.4f" % (zDroLoc))

                xDROPos = int(xDROPos)
                self.xDROPosition.value = xDROPos
                xDroLoc = float(xDROPos) / self.xDROInch
                if self.lastXOffset != xDROOffset:
                    self.lastXOffset = xDROOffset
                    print("xDROPos %d %0.4f xDROOffset %0.4f" % \
                          (xDROPos, xDroLoc, xDROOffset))
                    stdout.flush()
                xDroLoc = xDroLoc - xDROOffset
                if self.xDroDiam.value:
                    xDroLoc *= 2.0
                self.xDROPos.SetValue("%0.4f" % (xDroLoc))

            text = ''
            if xHomed:
                text = 'H'
            if self.currentPanel.active:
                text += '*'
            mvStatus = int(mvStatus)

            if mvStatus & ct.MV_MEASURE:
                text += 'M'
            if mvStatus & ct.MV_PAUSE:
                text  += 'P'
            if mvStatus & ct.MV_ACTIVE:
                text += 'A'
            if mvStatus & ct.MV_LIMIT:
                text += 'L'
            else:
                if self.overrideSet:
                    self.overrideSet = False
                    self.limitOverride.SetValue(False)
            self.statusText.SetLabel(text)

            if mvStatus != self.mvStatus:
                print("mvStatus %x" % (mvStatus))
                stdout.flush()
            self.mvStatus = mvStatus

            if self.xHome:
                if self.probeAxis == HOME_X:
                    val = comm.getParm(pm.X_HOME_STATUS)
                    if val is not None:
                        if val & ct.HOME_SUCCESS:
                            self.homeDone("home success")
                            xHomed = True
                            if not EXT_DRO:
                                comm.setParm(pm.X_LOC, 0)
                                if DRO:
                                    comm.setParm(pm.X_DRO_POS, 0)
                                    self.updateXDroPos(xLocation)
                            else:
                                self.setXFromExt()
                        elif val & ct.HOME_FAIL:
                            self.homeDone("home success")
                elif self.probeAxis == AXIS_Z:
                    val = comm.getParm(pm.Z_HOME_STATUS)
                    if val & ct.PROBE_SUCCESS:
                        zHomeOffset = zLocation - self.probeLoc
                        self.zHomeOffset.value = zHomeOffset
                        # cfg.setInfo(cf.zSvHomeOffset, "%0.4f" % (zHomeOffset))
                        if DRO:
                            self.updateZDroPos(self.probeLoc, zDROPos)
                        print("z %s zLocation %7.4f probeLoc %7.4f "\
                              "zHomeOffset %7.4f" % \
                              (z, zLocation, self.probeLoc, zHomeOffset))
                        stdout.flush()
                        self.probeLoc = 0.0
                        self.homeDone("z probe success")
                    elif val & ct.PROBE_FAIL:
                        self.homeDone("z probe failure")
                elif self.probeAxis == AXIS_X:
                    val = comm.getParm(pm.X_HOME_STATUS)
                    if val & ct.PROBE_SUCCESS:
                        xHomeOffset = xLocation - self.probeLoc
                        self.xHomeOffset.value = xHomeOffset
                        # cfg.setInfo(cf.xSvHomeOffset, "%0.4f" % (xHomeOffset))
                        if DRO:
                            self.updateXDroPos(self.probeLoc, xDROPos)
                        print("x %s xLocation %7.4f probeLoc %7.4f "\
                              "xHomeOffset %7.4f" % \
                              (x, xLocation, self.probeLoc, xHomeOffset))
                        stdout.flush()
                        self.probeLoc = 0.0
                        self.homeDone("x probe success")
                    elif val & ct.PROBE_FAIL:
                        self.homeDone("x probe failure")

    def updateError(self, text):
        self.setStatus(text)

    def OnEStop(self, e):
        global spindleDataSent, zDataSent, xDataSent
        moveCommands.queClear()
        comm.command(cm.CMD_CLEAR)
        spindleDataSent = False
        zDataSent = False
        xDataSent = False
        mainFrame.initDevice()
        self.clrActive()
        self.combo.SetFocus()

    def OnStop(self, e):
        self.homeDone("stopped")
        moveCommands.queClear()
        comm.command(cm.CMD_STOP)
        mainFrame.initDevice()
        self.clrActive()
        self.combo.SetFocus()

    def OnPause(self, e):
        comm.command(cm.CMD_PAUSE)
        self.combo.SetFocus()

    def OnResume(self, e):
        comm.command(cm.CMD_RESUME)
        self.combo.SetFocus()

    def OnDone(self, e):
        if self.mvStatus == 0:
            self.clrActive()
        else:
            self.setStatus(st.STR_OP_IN_PROGRESS)
        self.combo.SetFocus()

    def OnMeasure(self, e):
        comm.command(cm.CMD_MEASURE)
        self.combo.SetFocus()

    def getPanel(self):
        panel = cfg.getInfoData(cf.mainPanel)
        return(mainFrame.panels[panel])

    def clrActive(self):
        updateThread.closeDbg()
        self.currentPanel.active = False
        self.setStatus(st.STR_CLR)

    def OnStartSpindle(self, e):
        if STEP_DRV or MOTOR_TEST:
            panel = self.getPanel()
            rpm = panel.rpm.GetValue()
            sendSpindleData(True, rpm)
            comm.command(cm.SPINDLE_START)
        self.combo.SetFocus()

    def spindleJogCmd(self, code, val):
        self.repeat += 1
        if self.jogCode != code:
            if self.jogCode is None:
                sendSpindleData()
                direction = 0 if code == wx.WXK_NUMPAD_PAGEDOWN else 1
                comm.setParm(pm.SP_JOG_DIR, direction)
                self.jogCode = code
                self.repeat = 0
        try:
            comm.command(cm.SPINDLE_JOG)
        except CommTimeout:
            commTimeout()
        self.combo.SetFocus()

    def OnJogSpindleFwd(self, e):
        print("jog spingle")
        stdout.flush()
        self.btnRpt.action = self.spindleJogCmd
        self.btnRpt.code = wx.WXK_NUMPAD_PAGEDOWN
        self.btnRpt.val = 0
        self.btnRpt.event.set()

    def OnJogSpindleRev(self, e):
        print("jog spingle")
        stdout.flush()
        self.btnRpt.action = self.spindleJogCmd
        self.btnRpt.code = wx.WXK_NUMPAD_PAGEUP
        self.btnRpt.val = 0
        self.btnRpt.event.set()

    def OnJogUp(self, e):
        self.btnRpt.event.clear()
        self.btnRpt.action = None
        self.jogCode = None
        try:
            comm.command(cm.SPINDLE_STOP)
        except CommTimeout:
            commTimeout()
        self.combo.SetFocus()

    def OnOverride(self, e):
        val = self.limitOverride.GetValue()
        print("override %s" % (val))
        stdout.flush()
        if val and ((self.mvStatus & ct.MV_LIMIT) == 0):
            self.limitOverride.SetValue(False)
            return
        self.overrideSet = val
        comm.setParm(pm.LIMIT_OVERRIDE, (0, 1)[val]);

    def setStatus(self, text):
        if done:
            return
        if isinstance(text, int):
            self.statusLine.SetLabel(st.strTable[text])
        elif isinstance(text, str):
            self.statusLine.SetLabel(text)
        self.Refresh()
        self.Update()

    def updateZPos(self, val):
        global zHomeOffset
        sendZData()
        zLocation = comm.getParm(pm.Z_LOC)
        if zLocation is not None:
            zLocation = float(zLocation) / self.zStepsInch
            zHomeOffset = zLocation - val
            self.zHomeOffset.value = zHomeOffset
            comm.setParm(pm.Z_HOME_OFFSET, \
                         round(zHomeOffset * jogPanel.zStepsInch))
            print("pos %0.4f zLocation %0.4f zHomeOffset %0.4f" % \
                  (val, zLocation, zHomeOffset))
            stdout.flush()
            if DRO:
                self.updateZDroPos(val)
            if EXT_DRO:
                dro.command(eDro.setZ("%0.4f" % (val)))

    def updateZDroPos(self, val, zDROPos=None):
        global zDROOffset
        if zDROPos is None:
            zDROPos = comm.getParm(pm.Z_DRO_POS, True)
        if zDROPos is not None:
            droPos = float(zDROPos) / self.zDROInch
            print("pos %0.4f zDROPos %d %0.4f" % \
                  (val, zDROPos, droPos))
            zDROOffset = droPos - val
            self.zDROOffset.value = zDROOffset
            comm.setParm(pm.Z_DRO_OFFSET, round(zDROOffset * jogPanel.zDROInch))
            print("zDROOffset %d %0.4f" % \
                  (int(zDROOffset * self.zDROInch), zDROOffset))
            stdout.flush()

    def setZFromExt(self):
        val = dro.command(eDro.extReadZ, True)
        val = val.strip()
        try:
            rsp = float(val)
        except ValueError:
            print("setZFromExt ValueError %s" % (val))
            stdout.flush()
            rsp = 0.0
        zPosition = round(rsp * jogPanel.zStepsInch)
        zHomeOffset = 0.0
        self.zHomeOffset.value = zHomeOffset
        comm.queParm(pm.Z_LOC, zPosition)
        comm.queParm(pm.Z_HOME_OFFSET, round(zHomeOffset * jogPanel.zStepsInch))
        if DRO:
            zDROPosition = round(rsp * jogPanel.zDROInch)
            zDROOffset = 0.0
            self.zDROOffset.value = zDROOffset
            comm.queParm(pm.Z_DRO_POS, zDROPosition)
            comm.queParm(pm.Z_DRO_OFFSET, round(zDROOffset * jogPanel.zDROInch))
        comm.sendMulti()

    def updateXPos(self, val):
        global xHomeOffset
        val /= 2.0
        sendXData()
        xLocation = comm.getParm(pm.X_LOC)
        if xLocation is not None:
            xLocation = float(xLocation) / self.xStepsInch
            xHomeOffset = xLocation - val
            self.xHomeOffset.value = xHomeOffset
            comm.setParm(pm.X_HOME_OFFSET, \
                         round(xHomeOffset * jogPanel.xStepsInch))
            print("pos %0.4f xLocation %0.4f xHomeOffset %0.4f" % \
                  (val, xLocation, xHomeOffset))
            stdout.flush()
            if DRO:
                self.updateXDroPos(val)
            if EXT_DRO:
                dro.command(eDro.setX("%0.4f" % (val * 2.0)))

    def updateXDroPos(self, val, xDROPos=None):
        global xDROOffset
        if xDROPos is None:
            xDROPos = comm.getParm(pm.X_DRO_POS)
        if xDROPos is not None:
            droPos = float(xDROPos) / self.xDROInch
            print("pos %0.4f xDROPos %d %0.4f" % \
                  (val, xDROPos, droPos))
            xDROOffset = droPos - val
            self.xDROOffset.value = xDROOffset
            comm.setParm(pm.X_DRO_OFFSET, round(xDROOffset * jogPanel.xDROInch))
            print("xDROOffset %d %0.4f" % \
                  (int(xDROOffset * self.xDROInch), xDROOffset))
            stdout.flush()

    def setXFromExt(self):
        val = dro.command(eDro.extReadX, True)
        val = val.strip()
        try:
            rsp = float(val) / 2.0
        except ValueError:
            print("setXFromExt ValueError %s" % (val))
            stdout.flush()
            rsp = 0.0
        print("val %s rsp %9.6f" % (val, rsp))
        xPosition = round(rsp * jogPanel.xStepsInch)
        xHomeOffset = 0.0
        self.xHomeOffset.value = xHomeOffset
        comm.queParm(pm.X_LOC, xPosition)
        comm.queParm(pm.X_HOME_OFFSET, round(xHomeOffset * jogPanel.xStepsInch))
        if DRO:
            xDROPosition = round(rsp * jogPanel.xDROInch)
            print("xDROPosition %d" % (xDROPosition))
            xDROOffset = 0.0
            self.xDROOffset.value = xDROOffset
            comm.queParm(pm.X_DRO_POS, xDROPosition)
            comm.queParm(pm.X_DRO_OFFSET, round(xDROOffset * jogPanel.xDROInch))
        comm.sendMulti()

    def getPos(self, ctl):
        (xPos, yPos) = mainFrame.GetPosition()
        (x, y) = self.GetPosition()
        xPos += x
        yPos += y
        (x, y) = ctl.GetPosition()
        xPos += x
        yPos += y
        return(xPos, yPos)

class HelpDialog(wx.Dialog):
    def __init__(self, frame):
        pos = (10, 10)
        wx.Dialog.__init__(self, frame, -1, "Help", pos, \
                           wx.DefaultSize, wx.DEFAULT_DIALOG_STYLE)
        helpText = (\
                    ('ESC', "Stop everything"), \
                    ('F9', "Start spindle"), \
                    ('r', "Start"), \
                    ('s', "Resume"), \
                    ('p', "Pause"), \
                    ('d', "Done"), \
                    ('C', "Clear status"), \

                    ('f', "Focus on operation"),
                    ('n', "Next operation"), \
                    ('a', "Add"), \
                    ('A', "Focus on add value"), \
                    ('P', "Toggle operation pause"), \
                    ('z', "Z menu"), \
                    ('x', "X menu"), \

                    ('c', "Jog continuous"), \
                    ('i', "Next jog val"), \
                    ('I', "Prev jog val"), \
                    ('?', "Help"), \
        )
        self.sizerV = sizerV = wx.BoxSizer(wx.VERTICAL)
        sizerG = wx.FlexGridSizer(cols=2, rows=0, vgap=0, hgap=0)
        for (char, text) in helpText:
            char = wx.StaticText(self, -1, char)
            sizerG.Add(char, flag=wx.LEFT|wx.RIGHT|wx.ALIGN_LEFT, border=5)
            text= wx.StaticText(self, -1, text)
            sizerG.Add(text, flag=wx.LEFT|wx.RIGHT|wx.ALIGN_LEFT, border=5)
        sizerV.Add(sizerG, 0, wx.ALIGN_LEFT)

        btn = wx.Button(self, wx.ID_OK)
        btn.SetDefault()
        sizerV.Add(btn, 0, wx.ALL|wx.CENTER, border=5)
        self.SetSizer(sizerV)
        self.sizerV.Fit(self)
        self.Show(True)

class PosMenu(wx.Menu):
    def __init__(self, jP, axis):
        wx.Menu.__init__(self)
        self.jP = jP
        self.axis = axis
 
        active = jogPanel.currentPanel.active
        if not active:
            item = wx.MenuItem(self, wx.Window.NewControlId(), "Set")
            self.Append(item)
            self.Bind(wx.EVT_MENU, self.OnSet, item)

            item = wx.MenuItem(self, wx.Window.NewControlId(), "Zero")
            self.Append(item)
            self.Bind(wx.EVT_MENU, self.OnZero, item)

            if EXT_DRO:
                item = wx.MenuItem(self, wx.Window.NewControlId(), "Ext DRO")
                self.Append(item)
                self.Bind(wx.EVT_MENU, self.OnSetFromExt, item)

            item = wx.MenuItem(self, wx.Window.NewControlId(), "Probe")
            self.Append(item)
            self.Bind(wx.EVT_MENU, self.OnProbe, item)

            if self.axis == AXIS_X:
                item = wx.MenuItem(self, wx.Window.NewControlId(), "Home")
                self.Append(item)
                self.Bind(wx.EVT_MENU, self.OnHomeX, item)

            item = wx.MenuItem(self, wx.Window.NewControlId(), "Go to")
            self.Append(item)
            self.Bind(wx.EVT_MENU, self.OnGoto, item)

        if self.axis == AXIS_X:
            item = wx.MenuItem(self, wx.Window.NewControlId(), "Fix X")
            self.Append(item)
            self.Bind(wx.EVT_MENU, self.OnFixX, item)

            if DRO:
                item = wx.MenuItem(self, wx.Window.NewControlId(), "DRO Diam")
                self.Append(item)
                self.Bind(wx.EVT_MENU, self.OnDroDiam, item)

    def getPosCtl(self):
        ctl = self.jP.zPos if self.axis == AXIS_Z else \
              self.jP.xPos
        return(self.jP.getPos(ctl))

    def OnSet(self, e):
        dialog = SetPosDialog(self.jP, self.axis)
        dialog.SetPosition(self.getPosCtl())
        dialog.Raise()
        dialog.Show(True)

    def OnZero(self, e):
        self.jP.updateZPos(0) if self.axis == AXIS_Z else \
            self.jP.updateXPos(0)
        self.jP.focus()

    def OnProbe(self, e):
        dialog = ProbeDialog(self.jP, self.axis)
        dialog.SetPosition(self.getPosCtl())
        dialog.Raise()
        dialog.Show(True)

    def OnHomeX(self, e):
        global xHomeOffset, xHomed
        if not HOME_IN_PLACE:
            comm.queParm(pm.X_HOME_DIST, cfg.getInfoData(cf.xHomeDist))
            comm.queParm(pm.X_HOME_BACKOFF_DIST, \
                         cfg.getInfoData(cf.xHomeBackoffDist))
            comm.queParm(pm.X_HOME_SPEED, cfg.getInfoData(cf.xHomeSpeed))
            comm.queParm(pm.X_HOME_DIR, 1 if cfg.getBoolInfoData(cf.xHomeDir) \
                         else -1)
            comm.command(cm.XHOMEAXIS)
            self.jP.probe(HOME_X)
        else: 
            xLocation = float(jogPanel.xPos.GetValue())
            xHomeOffset = 0 - xLocation
            jogPanel.xHomeOffset.value = xHomeOffset
            comm.setParm(pm.X_LOC, 0)
            comm.setParm(pm.X_HOME_OFFSET, \
                         round(xHomeOffset * jogPanel.xStepsInch))
            if DRO:
                comm.setParm(pm.X_DRO_POS, 0)
                self.jP.updateXDroPos(xLocation)
            self.jP.homeDone("home success")
            xHomed = True
        self.jP.focus()

    def OnGoto(self, e):
        dialog = GotoDialog(self.jP, self.axis)
        dialog.SetPosition(self.getPosCtl())
        dialog.Raise()
        dialog.Show(True)

    def OnFixX(self, e):
        jP = self.jP
        dialog = jP.fixXPosDialog
        if dialog is None:
            jP.fixXPosDialog = dialog = FixXPosDialog(jP)
        dialog.SetPosition(self.getPosCtl())
        dialog.Raise()
        dialog.Show(True)

    def OnDroDiam(self, e):
        self.jP.xDroDiam.value = not self.jP.xDroDiam.value
        self.jP.focus()

    def OnSetFromExt(self, e):
        if self.axis == AXIS_Z:
            self.jP.setZFromExt()
        else:
            self.jP.setXFromExt()
        self.jP.focus()

class SetPosDialog(wx.Dialog, FormRoutines):
    def __init__(self, jogPnl, axis):
        FormRoutines.__init__(self, False)
        self.jogPanel = jogPnl
        self.axis = axis
        pos = (10, 10)
        title = "Position %s" % ('Z' if axis == AXIS_Z else 'X')
        wx.Dialog.__init__(self, jogPnl, -1, title, pos, \
                            wx.DefaultSize, wx.DEFAULT_DIALOG_STYLE)
        self.Bind(wx.EVT_SHOW, self.OnShow)
        self.sizerV = sizerV = wx.BoxSizer(wx.VERTICAL)

        self.pos = \
            self.addDialogField(sizerV, tcDefault="0.000", \
                tcFont=jogPnl.posFont, size=(120,-1), action=self.OnKeyChar)

        self.addDialogButton(sizerV, wx.ID_OK, self.OnOk, border=10)

        self.SetSizer(sizerV)
        self.sizerV.Fit(self)
        self.Show(False)

    def OnShow(self, e):
        if done:
            return
        if self.IsShown():
            val = self.jogPanel.zPos.GetValue() if self.axis == AXIS_Z else \
               self.jogPanel.xPos.GetValue()
            if self.axis == AXIS_X:
                val = "%0.4f" % (float(val) * 2)
            self.pos.SetValue(val)
            self.pos.SetSelection(-1, -1)

    def OnKeyChar(self, e):
        keyCode = e.GetKeyCode()
        if keyCode == wx.WXK_RETURN:
            self.OnOk(None)
        e.Skip()

    def OnOk(self, e):
        val = self.pos.GetValue()
        try:
            val = float(val)
            self.jogPanel.updateZPos(val) if self.axis == AXIS_Z else \
                self.jogPanel.updateXPos(val)
        except ValueError:
            print("ValueError on %s" % (val))
            stdout.flush()
        self.Show(False)
        self.jogPanel.focus()

class ProbeDialog(wx.Dialog, FormRoutines):
    def __init__(self, jogPnl, axis):
        FormRoutines.__init__(self, False)
        self.jogPanel = jogPnl
        self.axis = axis
        pos = (10, 10)
        title = "Probe %s" % ('Z' if axis == AXIS_Z else 'X Diameter')
        wx.Dialog.__init__(self, jogPnl, -1, title, pos, \
                            wx.DefaultSize, wx.DEFAULT_DIALOG_STYLE)
        self.Bind(wx.EVT_SHOW, self.OnShow)
        self.sizerV = sizerV = wx.BoxSizer(wx.VERTICAL)

        sizerG = wx.FlexGridSizer(cols=2, rows=0, vgap=0, hgap=0)

        self.probeLoc = \
            self.addDialogField(sizerG, \
                'Z Position' if axis == AXIS_Z else 'X Diameter', \
                "0.000", jogPnl.txtFont, jogPnl.posFont, (120, -1))

        self.probeDist = \
            self.addDialogField(sizerG, 'Distance', "0.000", \
                jogPnl.txtFont, jogPnl.posFont, (120, -1), self.OnKeyChar)

        sizerV.Add(sizerG, 0, wx.ALIGN_RIGHT)

        self.addButton(sizerV, 'Ok', self.OnOk, border=10)

        self.SetSizer(sizerV)
        self.sizerV.Fit(self)
        self.Show(False)

    def OnShow(self, e):
        if done:
            return
        if self.IsShown():
            if self.axis == AXIS_Z:
                probeLoc = "0.0000"
                probeDist = cfg.getFloatInfoData(cf.zProbeDist)
            else:
                probeLoc = self.jogPanel.xPos.GetValue()
                probeDist = cfg.getFloatInfoData(cf.xProbeDist)
            self.probeLoc.SetValue(probeLoc)
            self.probeLoc.SetSelection(-1, -1)
            self.probeDist.SetValue("%7.4f" % probeDist)

    def OnKeyChar(self, e):
        keyCode = e.GetKeyCode()
        if keyCode == wx.WXK_RETURN:
            self.OnOk(None)
        e.Skip()

    def OnOk(self, e):
        val = self.probeLoc.GetValue()
        try:
            probeLoc = float(val)
            self.probeZ(probeLoc) if self.axis == AXIS_Z else \
               self.probeX(probeLoc / 2.0)
        except ValueError:
            print("probe ValueError on %s" % (val))
            stdout.flush()
        self.Show(False)
        self.jogPanel.focus()

    def probeZ(self, probeLoc):
        moveCommands.queClear()
        comm.queParm(pm.PROBE_INV, cfg.getBoolInfoData(cf.cfgPrbInv))
        comm.queParm(pm.PROBE_SPEED, cfg.getInfoData(cf.zProbeSpeed))
        comm.queParm(pm.Z_HOME_STATUS, '0')
        comm.sendMulti()
        moveCommands.probeZ(getFloatVal(self.probeDist))
        self.Show(False)
        self.jogPanel.probe(AXIS_Z, probeLoc)
        self.jogPanel.focus()

    def probeX(self, probeLoc):
        moveCommands.queClear()
        comm.queParm(pm.PROBE_INV, cfg.getBoolInfoData(cf.cfgPrbInv))
        comm.queParm(pm.X_HOME_SPEED, cfg.getInfoData(cf.xHomeSpeed))
        comm.queParm(pm.X_HOME_STATUS, '0')
        comm.sendMulti()
        moveCommands.probeX(getFloatVal(self.probeDist))
        self.Show(False)
        self.jogPanel.probe(AXIS_X, probeLoc)
        self.jogPanel.focus()

class GotoDialog(wx.Dialog, FormRoutines):
    def __init__(self, jogPnl, axis):
        FormRoutines.__init__(self, False)
        self.axis = axis
        pos = (10, 10)
        title = "Go to %s" % ('Z Position' if axis == AXIS_Z else 'X Diameter')
        wx.Dialog.__init__(self, jogPnl, -1, title, pos, \
                            wx.DefaultSize, wx.DEFAULT_DIALOG_STYLE)
        self.Bind(wx.EVT_SHOW, self.OnShow)
        self.sizerV = sizerV = wx.BoxSizer(wx.VERTICAL)

        self.pos = \
            self.addDialogField(sizerV, tcDefault="0.000", \
                tcFont=jogPnl.posFont, size=(120,-1), action=self.OnKeyChar)

        self.addButton(sizerV, 'Ok', self.OnOk, border=10)

        self.SetSizer(sizerV)
        self.sizerV.Fit(self)
        self.Show(False)

    def OnShow(self, e):
        if done:
            return
        if self.IsShown():
            val = jogPanel.zPos.GetValue() if self.axis == AXIS_Z else \
               jogPanel.xPos.GetValue()
            try:
                val = float(val)
            except ValueError:
                val = 0.0
            if self.axis == AXIS_X:
                val *= 2.0
            self.pos.SetValue("%0.4f" % (val))
            self.pos.SetSelection(-1, -1)

    def OnKeyChar(self, e):
        keyCode = e.GetKeyCode()
        if keyCode == wx.WXK_RETURN:
            self.OnOk(None)
        e.Skip()

    def OnOk(self, e):
        try:
            loc = float(self.pos.GetValue())
            m = moveCommands
            m.queClear()
            comm.command(cm.CMD_PAUSE)
            comm.command(cm.CLEARQUE)
            if self.axis == AXIS_Z:
                sendZData()
                m.saveZOffset()
                m.moveZ(loc)
            else:
                sendXData()
                m.dbg = True
                m.saveXOffset()
                flag = ct.CMD_JOG | ((ct.DRO_POS | ct.DRO_UPD) \
                                     if X_DRO_POS else 0)
                m.moveX(loc / 2.0, flag)
                m.dbg = False
            comm.command(cm.CMD_RESUME)
            self.Show(False)
            jogPanel.focus()
        except ValueError:
            print("ValueError on goto")
            stdout.flush()

class FixXPosDialog(wx.Dialog, FormRoutines):
    def __init__(self, jogPnl):
        FormRoutines.__init__(self, False)
        pos = (10, 10)
        wx.Dialog.__init__(self, jogPnl, -1, "Fix X Size", pos, \
                            wx.DefaultSize, wx.DEFAULT_DIALOG_STYLE)
        self.Bind(wx.EVT_SHOW, self.OnShow)
        self.sizerV = sizerV = wx.BoxSizer(wx.VERTICAL)

        sizerG = wx.FlexGridSizer(cols=2, rows=0, vgap=0, hgap=0)

        self.curXPos = \
            self.addDialogField(sizerG, 'Current', "0.000", jogPnl.txtFont, \
                                jogPnl.posFont, (120, -1))

        self.actualXPos = \
            self.addDialogField(sizerG, 'Measured', "0.000", jogPnl.txtFont, \
                jogPnl.posFont, (120, -1), self.OnKeyChar)

        sizerV.Add(sizerG, 0, wx.ALIGN_RIGHT)

        self.addButton(sizerV, 'Fix', self.OnFix, border=5)

        self.SetSizer(sizerV)
        self.sizerV.Fit(self)
        self.Show(False)

    def OnShow(self, e):
        if done:
            return
        if self.IsShown():
            xDiameter = jogPanel.passSize.GetValue()
            # try:
            #     xDiameter = float(comm.getParm(pm.X_DIAMETER)) / \
            #                 jogPanel.xStepsInch
            # except (ValueError, TypeError):
            #     xDiameter = 0.0
            # self.curXPos.SetValue("%0.4f" % (xDiameter))
            self.curXPos.SetValue(xDiameter)
            self.actualXPos.SetValue(xDiameter)
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
        
        offset = (actualX - curX)
        curHomeOffset = xHomeOffset
        x = comm.getParm(pm.X_LOC)
        print("x %d xPosition %d" % (x, int(jogPanel.xPosition.value)))
        xLocation = 2 * (float(x) / jogPanel.xStepsInch - xHomeOffset)
        jogPanel.updateXPos(xLocation + offset)

        currentPanel = jogPanel.currentPanel
        if currentPanel.active:
            op = currentPanel.op
            if (op == en.OP_TURN) or \
               (op == en.OP_TAPER) or \
               (op == en.OP_THREAD):
                currentPanel.control.fixCut(offset)
            elif op == en.OP_FACE:
                pass

        dPrt = jogPanel.dPrt
        dPrt("fix x\n")
        dPrt("curX %7.4f actualX %7.4f offset %7.4f\n" \
                  "xHomeOffset cur %7.4f new %7.4f\n" % \
                  (curX, actualX, offset, curHomeOffset, xHomeOffset))
        curLoc = float(jogPanel.xPosition.value) / jogPanel.xStepsInch
        dPrt("xDiam cur %7.4f new %7.4f\n\n" % \
                  ((curLoc - curHomeOffset) * 2, (curLoc - xHomeOffset) * 2), \
             flush=True)

        print("curX %0.4f actualX %0.4f offset %0.4f xHomeOffset %0.4f" % \
              (curX, actualX, offset, xHomeOffset))
        stdout.flush()

        self.Show(False)
        jogPanel.focus()

class RpmMenu(wx.Menu):
    def __init__(self, jP):
        wx.Menu.__init__(self)
        self.jP = jP
        item = wx.MenuItem(self, wx.Window.NewControlId(), "RPM")
        self.Append(item)
        self.Bind(wx.EVT_MENU, self.OnRPM, item)

        item = wx.MenuItem(self, wx.Window.NewControlId(), "Surface Speed")
        self.Append(item)
        self.Bind(wx.EVT_MENU, self.OnSurfaceSpeed, item)

    def OnRPM(self, e):
        self.jP.setSurfaceSpeed(False)

    def OnSurfaceSpeed(self, e):
        self.jP.setSurfaceSpeed(True)

EVT_UPDATE_ID = wx.Window.NewControlId()

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
        self.threadDone = False
        self.parmList = (self.readAll, )
        self.encoderCount = None
        self.xLoc = None
        self.zLoc = None
        self.xIntLoc = None
        self.zIntLoc = None
        self.zDro = None
        self.xDro = None
        self.xEncoderStart = None
        self.zEncoderStart = None
        self.xEncoderCount = None
        self.zEncoderCount = None
        self.passVal = None
        self.dbg = None
        self.baseTime = None
        self.mIdle = False
        dbgSetup = (\
                    (en.D_PASS, self.dbgPass), \
                    (en.D_DONE, self.dbgDone), \
                    (en.D_TEST, self.dbgTest), \

                    (en.D_XMOV, self.dbgXMov), \
                    (en.D_XLOC, self.dbgXLoc), \
                    (en.D_XDST, self.dbgXDst), \
                    (en.D_XSTP, self.dbgXStp),
                    (en.D_XST,  self.dbgXState), \
                    (en.D_XBSTP, self.dbgXBSteps), \
                    (en.D_XDRO, self.dbgXDro), \
                    (en.D_XPDRO, self.dbgXPDro), \
                    (en.D_XEXP, self.dbgXExp), \
                    (en.D_XWT,  self.dbgXWait), \
                    (en.D_XDN,  self.dbgXDone), \
                    (en.D_XEST, self.dbgXEncStart), \
                    (en.D_XEDN, self.dbgXEncDone), \
                    (en.D_XX, self.dbgXX), \
                    (en.D_XY, self.dbgXY), \

                    (en.D_ZMOV, self.dbgZMov), \
                    (en.D_ZLOC, self.dbgZLoc), \
                    (en.D_ZDST, self.dbgZDst), \
                    (en.D_ZSTP, self.dbgZStp),
                    (en.D_ZST, self.dbgZState), \
                    (en.D_ZBSTP, self.dbgZBSteps), \
                    (en.D_ZDRO, self.dbgZDro), \
                    (en.D_ZPDRO, self.dbgZPDro), \
                    (en.D_ZEXP, self.dbgZExp), \
                    (en.D_ZWT, self.dbgZWait), \
                    (en.D_ZDN, self.dbgZDone), \
                    (en.D_ZEST, self.dbgZEncStart), \
                    (en.D_ZEDN, self.dbgZEncDone), \
                    (en.D_ZX, self.dbgZX), \
                    (en.D_ZY, self.dbgZY), \

                    (en.D_HST, self.dbgHome), \

                    (en.D_MSTA, self.dbgMoveState), \
                    (en.D_MCMD, self.dbgMoveCmd), \
        )
        self.dbgTbl = dbgTbl = [None for i in range(len(dbgSetup))]
        for (index, action) in dbgSetup:
            dbgTbl[index] = action
        for i, val in enumerate(dbgTbl):
            if val is None:
                print("dbgTbl action for %s missing" % (en.dMessageList[i]))
                stdout.flush()

    def openDebug(self, file="dbg.txt"):
        self.dbg = open(os.path.join(DBG_DIR, file), "wb")
        t = strftime("%a %b %d %Y %H:%M:%S\n", localtime())
        self.dbg.write(t.encode())
        self.dbg.flush()

    def closeDbg(self):
        if self.dbg is not None:
            self.dbg.close()
            self.dbg = None
            self.baseTime = None

    # def zLoc(self):
    #     val = comm.getParm(pm.Z_LOC)
    #     if val is not None:
    #         result = (en.EV_ZLOC, val)
    #         wx.PostEvent(self.notifyWindow, UpdateEvent(result))

    # def xLoc(self):
    #     val = comm.getParm(pm.X_LOC)
    #     if val is not None:
    #         result = (en.EV_XLOC, val)
    #         wx.PostEvent(self.notifyWindow, UpdateEvent(result))

    # def rpm(self):
    #     period = comm.getParm(pm.INDEX_PERIOD)
    #     if period is not None:
    #         preScaler = comm.getParm(pm.INDEX_PRE_SCALER)
    #         result = (en.EV_RPM, period * preScaler)
    #         wx.PostEvent(self.notifyWindow, UpdateEvent(result))

    def readAll(self):
        if done:
            return
        comm.xDbgPrint = False
        try:
            result = comm.command(cm.READALL)
            if result is None:
                return

        except CommTimeout:
            if done:
                return
            self.readAllError = True
            wx.PostEvent(self.notifyWindow, \
                         UpdateEvent((en.EV_ERROR, st.STR_READALL_ERROR)))
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
                         UpdateEvent((en.EV_ERROR, st.STR_CLR)))
        try:
            (z, x, rpm, curPass, droZ, droX, flag) = \
                result.rstrip().split(' ')[1:]
            result = (en.EV_READ_ALL, z, x, rpm, curPass, droZ, droX, flag)
            wx.PostEvent(self.notifyWindow, UpdateEvent(result))
        except ValueError:
            print("readAll ValueError %s" % (result))
            stdout.flush()

    def run(self):
        i = 0
        op = None
        scanMax = len(self.parmList)
        while True:
            stdout.flush()
            sleep(0.1)
            if not self.threadRun:
                break

            # read update variables

            if i < len(self.parmList):
                func = self.parmList[i]
                try:
                    pass
                    func()
                except CommTimeout:
                    print("CommTimeout on func")
                    stdout.flush()
                except serial.SerialException:
                    print("SerialException on func")
                    stdout.flush()
                    break
                except RuntimeError:
                    if done:
                        break
            i += 1
            if i >= scanMax:
                i = 0

            # process move queue

            moveQue = moveCommands.moveQue
            if not moveQue.empty() or (op is not None):
                if not self.threadRun:
                    break
                try:
                    num = comm.getQueueStatus()
                    if not self.threadRun:
                        break
                    while num > 0:
                        num -= 1
                        if op is None:
                            try:
                                (opString, op, val) = moveQue.get(False)
                            except Empty:
                                break
                        comm.sendMove(opString, op, val)
                        op = None
                except CommTimeout:
                    print("CommTimeout on queue")
                    stdout.flush()
                except serial.SerialException:
                    print("SerialException on queue")
                    stdout.flush()
                    break

            # get debug data

            if self.procDebug():
                break
            
        print("UpdateThread done")
        stdout.flush()
        self.threadDone = True

    def close(self):
        self.closeDbg()
        self.threadRun = False
        
    def procDebug(self):
        try:
            result = comm.getString(cm.READDBG, 10)
            if not self.threadRun:
                return(True)
            if result is None:
                return(False)
            if not REM_DBG:
                return(False)
            tmp = result.split()
            rLen = len(tmp)
            # if rLen > 0:
            #     print("%2d (%s)" % (rLen, result))
            index = 2
            t = (("%8.3f " % (time() - self.baseTime))
                 if self.baseTime is not None else "   0.000 ")
            while index <= rLen:
                (cmd, val) = tmp[index-2:index]
                index += 2
                try:
                    cmd = int(cmd, 16)
                    val = int(val, 16)
                    try:
                        action = self.dbgTbl[cmd]
                        output = action(val)
                        if output is not None:
                            if self.dbg is None:
                                print(t + output)
                                stdout.flush()
                            else:
                                self.dbg.write((t + output + "\n").encode())
                                self.dbg.flush()
                        # if cmd == en.D_DONE:
                        #     if val == 0:
                        #         if not jogPanel.currentPanel.control.add:
                        #             self.baseTime = time()
                        #     if val == 1:
                        #         self.baseTime = None
                        #         if self.dbg is not None:
                        #             self.dbg.close()
                        #             self.dbg = None
                    except IndexError:
                        print("index error %s" % result)
                        stdout.flush()
                    except TypeError:
                        print("type error %s %s" % \
                              (en.dMessageList[cmd], result))
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
            return(True)

    def dbgDispatch(self, t0, cmd, val):
        try:
            action = self.dbgTbl[cmd]
            output = action(val)
            if output is not None:
                t = (("%8.3f " % (t0 - self.baseTime))
                     if self.baseTime is not None else "   0.000 ")
                if self.dbg is None:
                    print(t + output)
                    stdout.flush()
                else:
                    self.dbg.write((t + output + "\n").encode())
                    self.dbg.flush()
        except IndexError:
            print("index error %d" % cmd)
            stdout.flush()
        except TypeError:
            print("type error %s %s" % \
                  (en.dMessageList[cmd], str(val)))
            stdout.flush()

    def dbgPass(self, val):
        # tmp = val >> 8
        # if tmp == 0:
        #     return("pass %d\n")
        # elif tmp == 1:
        #     return("spring\n")
        # elif tmp == 2:
        #     return("spring %d\n" % (val & 0xff))
        self.passVal = val
        result = "spring\n" if val & 0x100 else \
                 "spring %d\n" % (val & 0xff) if val & 0x200 else \
                 "pass %d\n" % (val)
        return(result)

    def dbgDone(self, val):
        if val == ct.PARM_START:
            if not jogPanel.currentPanel.control.add:
                self.baseTime = time()
            return("strt\n")
        elif val == ct.PARM_DONE:
            return("done\n")

    def dbgTest(self, val):
        return("test %d" % (val))

    def dbgXMov(self, val):
        tmp = float(val) / jogPanel.xStepsInch - xHomeOffset
        return("xmov %7.4f %7.4f" % (tmp, tmp * 2.0))

    def dbgXLoc(self, val):
        iTmp = int(val)
        self.xIntLoc = iTmp
        tmp = float(val) / jogPanel.xStepsInch - xHomeOffset
        self.xLoc = tmp
        if self.xDro is not None:
            diff = " diff %7.4f" % (self.xDro - tmp)
            self.xDro = None
        else:
            diff = ""
        return("xloc %7d %7.4f %7.4f%s" % (iTmp, tmp, tmp * 2.0, diff))

    def dbgXDst(self, val):
        tmp = float(val) / jogPanel.xStepsInch
        return("xdst %7.4f %7d" % (tmp, val))

    def dbgXStp(self, val):
        dist = float(val) / jogPanel.xStepsInch
        if self.xEncoderCount is None or self.xEncoderCount == 0:
            return("xstp %7.4f %7d" % (dist, val))
        else:
            pitch = dist / (float(self.xEncoderCount) / self.encoderCount)
            self.xEncoderCount = None
            return("xstp %7.4f %7d pitch %7.4f" % (dist, val, pitch))

    def dbgXState(self, val):
        return(("x_st %s" % (en.xStatesList[val])) + \
                ("\n" if self.mIdle and val == en.XIDLE else ""))

    def dbgXBSteps(self, val):
        tmp = float(val) / jogPanel.xStepsInch
        return("xbst %7.4f %7d" % (tmp, val))

    def dbgXDro(self, val):
        tmp = float(val) / jogPanel.xDROInch - xDROOffset
        self.xDro = tmp
        return("xdro %7.4f %7.4f %7d" % (tmp, tmp * 2.0, val))

    def dbgXPDro(self, val):
        tmp = float(val) / jogPanel.xDROInch - xDROOffset
        s = "pass %2d xdro %7.4f xloc %7.4f diff %7.4f" % \
            (self.passVal, tmp * 2.0, self.xLoc * 2.0, self.xLoc - tmp)
        jogPanel.dPrt(s + "\n", flush=True)
        return("xpdro " + s)

    def dbgXExp(self, val):
        tmp = float(val) / jogPanel.xStepsInch - xHomeOffset
        return("xexp %7.4f" % (tmp))

    def dbgXWait(self, val):
        return("xwt  %2x" % (val))

    def dbgXDone(self, val):
        return("xdn  %2x" % (val))

    def dbgXEncStart(self, val):
        self.xEncoderStart = val
        return(None)

    def dbgXX(self, val):
        return("x_x  %7d" % (val))

    def dbgXY(self, val):
        return("x_y  %7d" % (val))

    def dbgXEncDone(self, val):
        if self.xEncoderStart is None:
            return(None)
        count = c_uint32(val - self.xEncoderStart).value
        self.xEncoderCount = count
        return("xedn %7.2f %7d" % (float(count) / self.encoderCount, count))

    def dbgZMov(self, val):
        tmp = float(val) / jogPanel.zStepsInch - zHomeOffset
        return("zmov %7.4f" % (tmp))

    def dbgZLoc(self, val):
        iTmp = int(val)
        self.zIntLoc = iTmp
        tmp = float(val) / jogPanel.zStepsInch - zHomeOffset
        self.zLoc = tmp
        if self.zDro is not None:
            diff = " diff %7.4f" % (self.zDro - tmp)
            self.zDro = None
        else:
            diff = ""
        return("zloc %7d %7.4f%s" % (iTmp, tmp, diff))

    def dbgZDst(self, val):
        tmp = float(val) / jogPanel.zStepsInch
        return("zdst %7.4f %7d" % (tmp, val))

    def dbgZStp(self, val):
        dist = float(val) / jogPanel.zStepsInch
        if self.zEncoderCount is None or self.zEncoderCount == 0:
            return("zstp %7.4f %7d" % (dist, val))
        else:
            pitch = dist / (float(self.zEncoderCount) / self.encoderCount)
            self.zEncoderCount = None
            return("zstp %7.4f %7d pitch %7.4f" % (dist, val, pitch))

    def dbgZState(self, val):
        return(("z_st %s" % (en.zStatesList[val])) + \
                ("\n" if self.mIdle and val == en.ZIDLE else ""))

    def dbgZBSteps(self, val):
        tmp = float(val) / jogPanel.zStepsInch
        return("zbst %7.4f %7d" % (tmp, val))

    def dbgZDro(self, val):
        tmp = float(val) / jogPanel.zDROInch - zDROOffset
        self.zDro = tmp
        return("zdro %7.4f" % (tmp))

    def dbgZPDro(self, val):
        tmp = float(val) / jogPanel.zDROInch - zDROOffset
        s = "pass %2d zdro %7.4f zloc %7.4f diff %7.4f" % \
            (self.passVal, tmp, self.zLoc, self.zLoc - tmp)
        jogPanel.dPrt(s + "\n", flush=True)
        return("zpdro " + s)

    def dbgZExp(self, val):
        tmp = float(val) / jogPanel.zStepsInch - zHomeOffset
        return("zexp %7.4f" % (tmp))

    def dbgZWait(self, val):
        return("zwt  %2x" % (val))

    def dbgZDone(self, val):
        return("zdn  %2x" % (val))

    def dbgZEncStart(self, val):
        self.zEncoderStart = val
        return(None)

    def dbgZEncDone(self, val):
        if self.zEncoderStart is None:
            return(None)
        count = c_uint32(val - self.zEncoderStart).value
        self.zEncoderCount = count
        return("zedn %7.2f %7d" % (float(count) / self.encoderCount, count))

    def dbgZX(self, val):
        return("z_x  %7d" % (val))

    def dbgZY(self, val):
        return("z_y  %7d" % (val))

    def dbgHome(self, val):
        return("hsta %s" % (en.hStatesList[val]))

    def dbgMoveState(self, val):
        self.mIdle = val == en.M_IDLE
        return("msta %s" % (en.mStatesList[val]
                            + ("\n" if self.mIdle else "")))

    def dbgMoveCmd(self, val):
        if (val & 0xff00) == 0:
            return("mcmd %s" % (en.mCommandsList[val]))
        else:
            return("mcmd %s %02x" % (en.mCommandsList[val & 0xff], val >> 8))

    def abort(self):
        self.threadRun = False

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

EVT_RESIZE_ID = wx.Window.NewControlId()

class ResizeEvent(wx.PyEvent):
    def __init__(self):
        wx.PyEvent.__init__(self)
        self.SetEventType(EVT_RESIZE_ID)

class Delay(Thread):
    def __init__(self, frame):
        Thread.__init__(self)
        print("Delay start")
        stdout.flush()
        self.frame = frame
        self.start()

    def run(self):
        sleep(1)
        print("SendSizeEvent")
        wx.PostEvent(self.frame, ResizeEvent())
        print("Delay done")
        stdout.flush()

class MainFrame(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, -1, title)
        self.Bind(wx.EVT_CLOSE, self.onClose)
        self.Connect(-1, -1, EVT_RESIZE_ID, self.OnResize)
        self.dirName = os.getcwd()
        self.parseCmdLine()
        self.initialConfig()
        
        self.hdrFont = wx.Font(20, wx.MODERN, wx.NORMAL, \
                               wx.NORMAL, False, u'Consolas')
        self.defaultFont = defaultFont = \
            wx.Font(10, wx.MODERN, wx.NORMAL,
                    wx.NORMAL, False, u'Consolas')
        self.SetFont(defaultFont)

        global moveCommands
        moveCommands = MoveCommands()

        self.currentPanel = None
        
        self.zDialog = ZDialog(self, defaultFont)
        self.xDialog = XDialog(self, defaultFont)
        self.spindleDialog = SpindleDialog(self, defaultFont)
        self.portDialog = PortDialog(self, defaultFont)
        self.configDialog = ConfigDialog(self, defaultFont)

        self.testSpindleDialog = None
        self.testSyncDialog = None
        self.testTaperDialog = None
        self.testMoveDialog = None

        self.menuSetup()
        self.initUI()

        global updateThread
        self.updateThread = updateThread = UpdateThread(self.jogPanel)

        global jogShuttle
        self.jogShuttle = jogShuttle = JogShuttle()

        comm.openSerial(cfg.getInfoData(cf.commPort), \
                        cfg.getInfoData(cf.commRate))

        if SPINDLE_SYNC_BOARD:
            syncComm.openSerial(cfg.getInfoData(cf.syncPort), \
                                cfg.getInfoData(cf.syncRate))
            syncComm.setupCmds(sc.SYNC_LOADMULTI, sc.SYNC_LOADVAL,
                               sc.SYNC_READVAL)

            syncComm.setupTables(sc.cmdTable, sp.parmTable)
        
        global keypad
        port = cfg.getInfoData(cf.keypadPort)
        if len(port) != 0:
            self.keypad = keypad = Keypad(cfg.getInfoData(cf.keypadPort), \
                                          cfg.getInfoData(cf.keypadRate))
        else:
            self.keypad = keypad = None
        
        self.initDRO()
                                                                              
        if FPGA:
            comm.xRegs = xr.xRegTable

        self.initDevice()

        if not R_PI:
            updateThread.start()
        else:
            comm.rpi.setPostUpdate(self.jogPanel.postUpdate)
            comm.rpi.setDbgDispatch(updateThread.dbgDispatch)
        self.delay = Delay(self)

    def onClose(self, e):
        global done
        posList = (cf.zSvPosition, cf.zSvHomeOffset, \
                   cf.xSvPosition, cf.xSvHomeOffset)
        if DRO:
            posList += (cf.zSvDROPosition, cf.zSvDROOffset, \
                        cf.xSvDROPosition, cf.xSvDROOffset)
        cfg.saveList(self.posFile, posList)
        done = True
        jogPanel.close()
        self.updateThread.close()
        buttonRepeat.close()
        jogShuttle.close()
        if R_PI:
            comm.rpi.close()
        if keypad is not None:
            keypad.close()
        self.Destroy()

    def menuSetup(self):
        # file menu
        fileMenu = wx.Menu()

        ID_FILE_SAVE = wx.Window.NewControlId()
        menu = fileMenu.Append(ID_FILE_SAVE, 'Save')
        self.Bind(wx.EVT_MENU, self.OnSave, menu)

        ID_FILE_INIT_DEVICE = wx.Window.NewControlId()
        menu = fileMenu.Append(ID_FILE_INIT_DEVICE, 'Init Device')
        self.Bind(wx.EVT_MENU, self.OnInit, menu)

        ID_FILE_SAVE_RESTART = wx.Window.NewControlId()
        menu = fileMenu.Append(ID_FILE_SAVE_RESTART, 'Save and Restart')
        self.Bind(wx.EVT_MENU, self.OnRestat, menu)

        ID_FILE_SAVE_PANEL = wx.Window.NewControlId()
        menu = fileMenu.Append(ID_FILE_SAVE_PANEL, 'Save Panel')
        self.Bind(wx.EVT_MENU, self.OnSavePanel, menu)

        ID_FILE_LOAD_PANEL = wx.Window.NewControlId()
        menu = fileMenu.Append(ID_FILE_LOAD_PANEL, 'Load Panel')
        self.Bind(wx.EVT_MENU, self.OnLoadPanel, menu)

        ID_FILE_EXIT = wx.Window.NewControlId()
        menu = fileMenu.Append(ID_FILE_EXIT, 'Exit')
        self.Bind(wx.EVT_MENU, self.OnExit, menu)

        # setup menu
        setupMenu = wx.Menu()

        ID_Z_SETUP = wx.Window.NewControlId()
        menu = setupMenu.Append(ID_Z_SETUP, 'Z')
        self.Bind(wx.EVT_MENU, self.OnZSetup, menu)

        ID_X_SETUP = wx.Window.NewControlId()
        menu = setupMenu.Append(ID_X_SETUP, 'X')
        self.Bind(wx.EVT_MENU, self.OnXSetup, menu)

        ID_SPINDLE_SETUP = wx.Window.NewControlId()
        menu = setupMenu.Append(ID_SPINDLE_SETUP, 'Spindle')
        self.Bind(wx.EVT_MENU, self.OnSpindleSetup, menu)

        ID_PORT_SETUP = wx.Window.NewControlId()
        menu = setupMenu.Append(ID_PORT_SETUP, 'Port')
        self.Bind(wx.EVT_MENU, self.OnPortSetup, menu)

        ID_PORT_SETUP = wx.Window.NewControlId()
        menu = setupMenu.Append(ID_PORT_SETUP, 'Config')
        self.Bind(wx.EVT_MENU, self.OnConfigSetup, menu)

        # operation menu
        operationMenu = wx.Menu()

        ID_TURN = wx.Window.NewControlId()
        menu = operationMenu.Append(ID_TURN, 'Turn')
        self.Bind(wx.EVT_MENU, self.OnTurn, menu)

        ID_FACE = wx.Window.NewControlId()
        menu = operationMenu.Append(ID_FACE, 'Face')
        self.Bind(wx.EVT_MENU, self.OnFace, menu)

        ID_CUTOFF = wx.Window.NewControlId()
        menu = operationMenu.Append(ID_CUTOFF, 'Cutoff')
        self.Bind(wx.EVT_MENU, self.OnCutoff, menu)

        ID_TAPER = wx.Window.NewControlId()
        menu = operationMenu.Append(ID_TAPER, 'Taper')
        self.Bind(wx.EVT_MENU, self.OnTaper, menu)

        if STEP_DRV or SPINDLE_ENCODER:
            ID_THREAD = wx.Window.NewControlId()
            menu = operationMenu.Append(ID_THREAD, 'Thread')
            self.Bind(wx.EVT_MENU, self.OnThread, menu)

        # test menu
        testMenu = wx.Menu()

        ID_TEST_SPINDLE = wx.Window.NewControlId()
        menu = testMenu.Append(ID_TEST_SPINDLE, 'Spindle')
        self.Bind(wx.EVT_MENU, self.OnTestSpindle, menu)

        ID_TEST_SYNC = wx.Window.NewControlId()
        menu = testMenu.Append(ID_TEST_SYNC, 'Sync')
        self.Bind(wx.EVT_MENU, self.OnTestSync, menu)

        ID_TEST_TAPER = wx.Window.NewControlId()
        menu = testMenu.Append(ID_TEST_TAPER, 'Taper')
        self.Bind(wx.EVT_MENU, self.OnTestTaper, menu)

        ID_TEST_MOVE = wx.Window.NewControlId()
        menu = testMenu.Append(ID_TEST_MOVE, 'Move')
        self.Bind(wx.EVT_MENU, self.OnTestMove, menu)

        menuBar = wx.MenuBar()
        menuBar.Append(fileMenu, 'File')
        menuBar.Append(setupMenu, 'Setup')
        menuBar.Append(operationMenu, 'Operation')
        menuBar.Append(testMenu, 'Test')

        self.SetMenuBar(menuBar)

    def initUI(self):
        # filter = KeyEventFilter()
        # self.Bind(wx.EVT_KEY_DOWN, self.OnKeyDown)
        # self.Bind(wx.EVT_KEY_UP, self.OnKeyUp)
        # self.Bind(wx.EVT_CHAR_HOOK, self.OnKeyChar)

        self.sizerV = sizerV = wx.BoxSizer(wx.VERTICAL)

        self.panels = {}
        self.turnPanel = panel = TurnPanel(self, self.hdrFont)
        self.panels['turnPanel'] = panel
        sizerV.Add(panel, 0, wx.EXPAND|wx.ALL, border=2)
        panel.Hide()

        self.facePanel = panel = FacePanel(self, self.hdrFont)
        self.panels['facePanel'] = panel
        sizerV.Add(panel, 0, wx.EXPAND|wx.ALL, border=2)
        panel.Hide()

        self.cutoffPanel = panel = CutoffPanel(self, self.hdrFont)
        self.panels['cutoffPanel'] = panel
        sizerV.Add(panel, 0, wx.EXPAND|wx.ALL, border=2)
        panel.Hide()

        self.taperPanel = panel = TaperPanel(self, self.hdrFont)
        self.panels['taperPanel'] = panel
        sizerV.Add(panel, 0, wx.EXPAND|wx.ALL, border=2)
        panel.Hide()

        if STEP_DRV or SPINDLE_ENCODER:
            self.threadPanel = panel = ThreadPanel(self, self.hdrFont)
            self.panels['threadPanel'] = panel
            sizerV.Add(panel, 0, wx.EXPAND|wx.ALL, border=2)
            panel.Hide()

        print("MainFrame JogPanel")
        global jogPanel
        self.jogPanel = jogPanel = JogPanel(self, style=wx.WANTS_CHARS)
        sizerV.Add(jogPanel, 0, wx.EXPAND|wx.ALL, border=2)

        self.SetSizer(sizerV)
        self.SetSizerAndFit(sizerV)

        cfg.readInfo(self.cfgFile, cf.config)
        cfg.readInfo(self.posFile, cf.config)

        jogPanel.update()

        varList = (('jogPanel.zPosition', cf.zSvPosition), \
                ('jogPanel.zHomeOffset', cf.zSvHomeOffset), \
                ('jogPanel.xPosition', cf.xSvPosition), \
                ('jogPanel.xHomeOffset', cf.xSvHomeOffset))
        if DRO:
            varList += (('jogPanel.zDROPosition', cf.zSvDROPosition), \
                     ('jogPanel.zDROOffset', cf.zSvDROOffset), \
                     ('jogPanel.xDROPosition', cf.xSvDROPosition), \
                     ('jogPanel.xDROOffset', cf.xSvDROOffset))

        for (v, key) in varList:
            if cfg.info[key] is None:
                cfg.newInfo(key, 0)
            exp = v + ' = cfg.getInfoInstance(' + str(key) + ')'
            exec(exp)

        dw, dh = wx.DisplaySize()
        w, h = self.GetSize()
        self.SetPosition((int((3 * dw) / 4 - w), 0))

        self.turnPanel.update()
        self.facePanel.update()
        self.cutoffPanel.update()
        self.taperPanel.update()
        if STEP_DRV:
            self.threadPanel.update()

        self.showPanel()
        self.Fit()

    def initDRO(self):
        if EXT_DRO:
            port = cfg.getInfoData(cf.extDroPort)
            print("port %s" % (port))
            stdout.flush()
            if port is not None:
                dro.openSerial(cfg.getInfoData(cf.extDroPort), \
                               cfg.getInfoData(cf.extDroRate))
                # rsp = dro.command("system.reset()\n", True)
                # print(rsp)
                # dro.flush()

                # automate = False
                # try:
                #     dro.flush()
                #     dro.command("\n", True, eDro.delim)
                #     print("automation off")
                # except DroTimeout:
                #     print("automation on")
                #     automate = True

                # if automate:
                #     try:
                #         rsp = dro.command("luash.automate(nil)\n", \
                #                           True, eDro.delim)
                #         print("automation turned on")
                #     except DroTimeout:
                #         print("DroTimeont exception")

                try:
                    dro.command(eDro.automateOff, True, eDro.delim)
                    print("automation turned on")
                    rsp = dro.command(eDro.showFunc, True, eDro.delim)
                    rsp = re.sub(eDro.matchPrompt, "", rsp)
                    # print(rsp)
                    rsp = rsp.split("\n")
                    for option in rsp:
                        tmp = option.strip().lower().split(":")
                        if len(tmp) == 2:
                            if tmp[0].strip() == "diameter":
                                if tmp[1].strip() != "on":
                                    dro.command(eDro.diamFunc, \
                                                True, eDro.delim)
                                    break
                    dro.command(eDro.inchMode, True, eDro.delim)
                    dro.command(eDro.absMode, True, eDro.delim)
                    for line in eDro.axisFunc:
                        dro.command(line, True, eDro.delim)
                    rsp = dro.command(eDro.automateOn, True)
                    # rsp = dro.command(eDro.extReadX, True)
                    # print(rsp, end="")
                    # rsp = dro.command(eDro.extReadZ, True)
                    # print(rsp, end="")
                    # dro.command(eDro.setZ(str(3.555)), True)
                    # dro.command("axis.zeroa(1,-2+axis.read(1))")
                    # dro.command("axis.zeroa(2,-4+axis.read(2));"\
                    #             "io.write('ok\\n')", True)
                except DroTimeout:
                    print("DroTimeont excpetion")

    def initDevice(self):
        global zPosition, zHomeOffset, xPosition, xHomeOffset
        if DRO:
            global zDROPosition, zDROOffset, xDROPosition, xDROOffset
        sendClear()
        stdout.flush()

        if comm.ser is not None:
            try:
                comm.queParm(pm.CFG_FPGA, cfg.getBoolInfoData(cf.cfgFpga))
                # comm.queParm(pm.CFG_FCY, cfg.getInfoData(cf.cfgFcy))
                comm.queParm(pm.CFG_MPG, cfg.getBoolInfoData(cf.cfgMPG))
                comm.queParm(pm.CFG_DRO, cfg.getBoolInfoData(cf.cfgDRO))
                comm.queParm(pm.CFG_LCD, cfg.getBoolInfoData(cf.cfgLCD))
                comm.queParm(pm.CFG_SWITCH, cfg.getBoolInfoData(cf.spSwitch))
                comm.queParm(pm.CFG_VAR_SPEED, \
                             cfg.getBoolInfoData(cf.spVarSpeed))
                comm.command(cm.CMD_SETUP)
                
                sendSpindleData()

                sendZData()
                if EXT_DRO:
                    self.jogPanel.setZFromExt()
                else:
                    zPosition = cfg.getIntInfo(cf.zSvPosition)
                    comm.queParm(pm.Z_LOC, zPosition)
                    zHomeOffset = cfg.getFloatInfo(cf.zSvHomeOffset)
                    comm.queParm(pm.Z_HOME_OFFSET, \
                                 round(zHomeOffset * jogPanel.zStepsInch))
                    print("zLoc %d %x %7.4f zHomeOffset %7.4f" % \
                          (zPosition, zPosition, \
                           float(zPosition) / jogPanel.zStepsInch, zHomeOffset))
                    stdout.flush()
                    if DRO:
                        zDROPosition = cfg.getIntInfo(cf.zSvDROPosition)
                        comm.queParm(pm.Z_DRO_POS, zDROPosition)
                        zDROOffset = cfg.getFloatInfo(cf.zSvDROOffset)
                        comm.queParm(pm.Z_DRO_OFFSET, \
                                     round(zDROOffset, jogPanel.zDROInch))
                        print("zDROPosition %d %x %7.4f zDROOffset %7.4f" % \
                              (zDROPosition, zDROPosition, \
                               float(zDROPosition) / jogPanel.zDROInch, \
                               zDROOffset))
                        stdout.flush()
                comm.sendMulti()

                sendXData()
                if EXT_DRO:
                    self.jogPanel.setXFromExt()
                else:
                    xPosition = cfg.getIntInfo(cf.xSvPosition)
                    comm.queParm(pm.X_LOC, xPosition)
                    xHomeOffset = cfg.getFloatInfo(cf.xSvHomeOffset)
                    comm.queParm(pm.X_HOME_OFFSET, \
                                 round(xHomeOffset * jogPanel.xStepsInch))
                    print("xLoc %d %x %7.4f xHomeOffset %7.4f" % \
                          (xPosition, xPosition, \
                           float(xPosition) / jogPanel.xStepsInch, xHomeOffset))
                    stdout.flush()
                    if DRO:
                        xDROPosition = cfg.getIntInfo(cf.xSvDROPosition)
                        comm.queParm(pm.X_DRO_POS, xDROPosition)
                        xDROOffset = cfg.getFloatInfo(cf.xSvDROOffset)
                        comm.queParm(pm.X_DRO_OFFSET, \
                                     round(xDROOffset * jogPanel.xDROInch))
                        print("xDROPosition %d %x %7.4f xDROOffset %7.4f" % \
                              (xDROPosition, xDROPosition, \
                               float(xDROPosition) / jogPanel.xDROInch, \
                               xDROOffset))
                        stdout.flush()

                if HOME_TEST:
                    val = str(int(cfg.getFloatInfoData(cf.xHomeLoc) * \
                                  jogPanel.xStepsInch))
                    comm.queParm(pm.X_HOME_LOC, val)
                    comm.queParm(pm.X_HOME_STATUS, \
                                 ct.HOME_SUCCESS if xHomed else ct.HOME_ACTIVE)
                comm.sendMulti()

            except CommTimeout:
                commTimeout()
        else:
            sendZData()
            sendXData()

    def parseCmdLine(self):
        global xHomed
        n = 1
        self.cfgFile = None
        self.posFile = None
        while True:
            if n >= len(sys.argv):
                break
            val = sys.argv[n]
            if val.startswith('--'):
                if len(val) >= 3:
                    tmp = val[2:]
                    if tmp == 'xhomed':
                        xHomed = True
                    elif tmp == 'help':
                        self.help()
            elif val.startswith('-'):
                if len(val) >= 2:
                    tmp = val[1]
                    if tmp == 'h':
                        self.help()
                    elif tmp == 'p':
                        n += 1
                        if n < len(sys.argv):
                            self.posFile = sys.argv[n]
                            if not re.search('\.[a-zA-Z0-9]*$', self.posFile):
                                self.posFile += ".txt"
            elif val.startswith('?'):
                self.help();
            else:
                if self.cfgFile is None:
                    self.cfgFile = val
                    if not re.search('\.[a-zA-Z0-9]*$', self.cfgFile):
                        self.cfgFile += ".txt"
            n += 1
        if self.cfgFile is None:
            self.cfgFile = "config.txt"
        if self.posFile is None:
            self.posFile = "posInfo.txt"

    def initialConfig(self):
        global cfg, comm, FPGA, DRO, EXT_DRO, REM_DBG, STEP_DRV, \
            MOTOR_TEST, SPINDLE_ENCODER, SPINDLE_SYNC_BOARD, \
            TURN_SYNC, THREAD_SYNC, SPINDLE_SWITCH, SPINDLE_VAR_SPEED, \
            HOME_IN_PLACE, X_DRO_POS

        cfg = ConfigInfo(cf.configTable)
        cfg.clrInfo(len(cf.config))
        cfg.readInfo(self.cfgFile, cf.config)

        FPGA = cfg.getInitialBoolInfo(cf.cfgFpga)
        DRO = cfg.getInitialBoolInfo(cf.cfgDRO)
        REM_DBG = cfg.getInitialBoolInfo(cf.cfgRemDbg)
        STEP_DRV = cfg.getInitialBoolInfo(cf.spStepDrive)
        MOTOR_TEST = cfg.getInitialBoolInfo(cf.spMotorTest)
        SPINDLE_ENCODER = cfg.getInitialBoolInfo(cf.cfgSpEncoder)

        if DRO:
            X_DRO_POS = cfg.getInitialBoolInfo(cf.xDROPos)
            EXT_DRO = cfg.getInitialBoolInfo(cf.cfgExtDro)
        else:
            X_DRO_POS = False
            EXT_DRO = False

        if not STEP_DRV and not MOTOR_TEST:
            SPINDLE_SWITCH = cfg.getInitialBoolInfo(cf.spSwitch)
            SPINDLE_VAR_SPEED = cfg.getInitialBoolInfo(cf.spVarSpeed)

        if SPINDLE_ENCODER:
            SPINDLE_SYNC_BOARD = cfg.getInitialBoolInfo(cf.cfgSpSyncBoard)
        else:
            SPINDLE_SYNC_BOARD = False

        TURN_SYNC = cfg.getIntInfoData(cf.cfgTurnSync)
        THREAD_SYNC =  cfg.getIntInfoData(cf.cfgThreadSync)
        
        if True:
            print("STEP_DRV %s SPINDLE_ENCODER %s "\
                  "SPINDLE_SYNC_BOARD %s" % \
                  (STEP_DRV, SPINDLE_ENCODER, SPINDLE_SYNC_BOARD))
            print("TURN_SYNC %d %s THREAD_SYNC %d %s" % \
                  (TURN_SYNC, en.selTurnText[TURN_SYNC], \
                   THREAD_SYNC, en.selThreadText[THREAD_SYNC]))
            
        HOME_IN_PLACE = cfg.getInitialBoolInfo(cf.cfgHomeInPlace)

        cfg.clrInfo(len(cf.config))

        if FPGA:
            global xb, xr
            if not R_PI:
                import xBitDef as xb
                import xRegDef as xr
            else:
                import fpgaLathe as xb
                import lRegDef as xr

        if EXT_DRO:
            global dro, eDro
            import extDro as eDro
            from extDro import DroTimeout
            dro = eDro.ExtDro()

        if DRO:
            global zDROOffset, xDROOffset, zDROPosition, xDROPosition
            zDROOffset = 0.0
            xDROOffset = 0.0
            zDROPosition = 0.0
            xDROPosition = 0.0

        if SPINDLE_SYNC_BOARD:
            global syncComm
            syncComm = Comm()

        syncDbg = True

        global zSyncInt, zSyncExt, xSyncInt, xSyncExt
        if not FPGA:
            if (TURN_SYNC == en.SEL_TU_ISYN or \
                TURN_SYNC == en.SEL_TU_ESYN or \
                THREAD_SYNC == en.SEL_TH_ISYN_RENC or \
                THREAD_SYNC == en.SEL_TH_ESYN_RENC or \
                THREAD_SYNC == en.SEL_TH_ESYN_RSYN):
                zSyncInt = Sync(dbg=syncDbg)
                zSyncExt = Sync(dbg=syncDbg)

            if (TURN_SYNC == en.SEL_TU_ISYN or \
                TURN_SYNC == en.SEL_TU_ESYN or \
                THREAD_SYNC == en.SEL_TH_ISYN_RENC or \
                THREAD_SYNC == en.SEL_TH_ESYN_RSYN):
                xSyncExt = Sync(dbg=syncDbg)
                xSyncInt = Sync(dbg=syncDbg)
        else:
            zSyncInt = Sync(dbg=syncDbg, fpga=True)
            xSyncInt = Sync(dbg=syncDbg, fpga=True)

        comm = Comm()
        comm.SWIG = SWIG

        if FPGA:
            comm.enableXilinx()

    def OnResize(self, e):
        print("OnResize")
        stdout.flush()
        self.Layout()
        self.Fit()

    def OnSave(self, e):
        cfg.saveInfo(self.cfgFile)

    def OnInit(self, e):
        if False:
            self.zDialog = None
            self.xDialog = None
            self.SpindleDialog = None
            self.portDialog = None
            self.configDialog = None
            self.initialConfig()
        self.initDevice()

    def OnRestat(self, e):
        cfg.saveInfo(self.cfgFile)
        os.execl(sys.executable, sys.executable, *sys.argv)

    def OnSavePanel(self, e):
        panel = cfg.getInfoData(cf.mainPanel)
        p = panel.replace('Panel', '')
        p = p[:1].upper() + p[1:].lower()
        dlg = wx.FileDialog(self, "Save " + p + " Config", self.dirName,
                            p + ".txt", "", wx.FD_SAVE)
        if dlg.ShowModal() == wx.ID_OK:
            self.dirName = dlg.GetDirectory()
            path = dlg.GetPath()
            cfg.saveList(path, self.panels[panel].getConfigList())

    def OnLoadPanel(self, e):
        panel = cfg.getInfoData(cf.mainPanel)
        p = panel.replace('Panel', '')
        p = p[:1].upper() + p[1:].lower()
        dlg = wx.FileDialog(self, "Load " + p + " Config", self.dirName,
                            p + ".txt", "", wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            self.dirName = dlg.GetDirectory()
            path = dlg.GetPath()
            cfg.readInfo(path, cf.config, self.panels[panel].getConfigList())

    def OnExit(self, e):
        self.Close(True)

    def showDialog(self, dialog):
        (xPos, yPos) = mainFrame.GetPosition()
        dialog.Raise()
        dialog.Show(True)
        (w, h) = dialog.GetSize()
        xPos -= w
        if xPos < 1:
            xPos = 1
        dialog.SetPosition((xPos, yPos))

    def OnZSetup(self, e):
        if self.zDialog is None:
            self.zDialog = ZDialog(self, self.defaultFont)
        self.showDialog(self.zDialog)

    def OnXSetup(self, e):
        if self.xDialog is None:
            self.xDialog = XDialog(self, self.defaultFont)
        self.showDialog(self.xDialog)

    def OnSpindleSetup(self, e):
        if self.spindleDialog is None:
            self.spindleDialog = SpindleDialog(self, self.defaultFont)
        self.showDialog(self.spindleDialog)

    def OnPortSetup(self, e):
        if self.portDialog is None:
            self.portDialog = PortDialog(self, self.defaultFont)
        self.showDialog(self.portDialog)
        
    def OnConfigSetup(self, e):
        if self.configDialog is None:
            self.configDialog = ConfigDialog(self, self.defaultFont)
        self.showDialog(self.configDialog)

    def getCurrentPanel(self):
        return(self.currentPanel)
    
    def showPanel(self):
        key = cf.mainPanel
        if cfg.info[key] is None:
            cfg.initInfo(key, InfoValue('turnPanel'))

        if jogPanel.mvStatus != 0:
            jogPanel.updateError(st.STR_OP_IN_PROGRESS)
            return
        
        showPanel = cfg.getInfoData(key)
        for key in self.panels:
            panel = self.panels[key]
            if key == showPanel:
                panel.Show()
                self.currentPanel = panel
            else:
                panel.Hide()
        if self.currentPanel == None:
            panel = self.turnPanel
            panel.Show()
            self.currentPanel = panel
        self.Layout()
        self.Fit()

    def OnTurn(self, e):
        cfg.setInfo(cf.mainPanel, 'turnPanel')
        self.showPanel()

    def OnFace(self, e):
        cfg.setInfo(cf.mainPanel, 'facePanel')
        self.showPanel()

    def OnCutoff(self, e):
        cfg.setInfo(cf.mainPanel, 'cutoffPanel')
        self.showPanel()

    def OnTaper(self, e):
        cfg.setInfo(cf.mainPanel, 'taperPanel')
        self.showPanel()

    def OnThread(self, e):
        cfg.setInfo(cf.mainPanel, 'threadPanel')
        self.showPanel()

    def OnTestSpindle(self, e):
        if self.testSpindleDialog is None:
            self.testSpindleDialog = TestSpindleDialog(self, self.defaultFont)
        else:
            self.testSpindleDialog.Raise()
        self.testSpindleDialog.spindleTest.test()
        self.testSpindleDialog.Show()

    def OnTestSync(self, e):
        if self.testSyncDialog is None:
            self.testSyncDialog = TestSyncDialog(self, self.defaultFont)
        else:
            self.testSyncDialog.Raise()
        self.testSyncDialog.syncTest.test()
        self.testSyncDialog.Show()

    def OnTestTaper(self, e):
        if self.testTaperDialog is None:
            self.testTaperDialog = TestTaperDialog(self, self.defaultFont)
        else:
            self.testTaperDialog.Raise()
        self.testTaperDialog.taperTest.test()
        self.testTaperDialog.Show()

    def OnTestMove(self, e):
        if self.testMoveDialog is None:
            self.testMoveDialog = TestMoveDialog(self, self.defaultFont)
        else:
            self.testMoveDialog.Raise()
        self.testMoveDialog.moveTest.test()
        self.testMoveDialog.Show()

class ZDialog(wx.Dialog, FormRoutines, DialogActions):
    def __init__(self, frame, defaultFont):
        pos = (10, 10)
        wx.Dialog.__init__(self, frame, -1, "Z Setup", pos, \
                            wx.DefaultSize, wx.DEFAULT_DIALOG_STYLE)
        self.SetFont(defaultFont)
        FormRoutines.__init__(self, False)
        DialogActions.__init__(self)
        self.sizerV = sizerV = wx.BoxSizer(wx.VERTICAL)

        sizerG = wx.FlexGridSizer(cols=2, rows=0, vgap=0, hgap=0)

        self.fields = (
            ("Pitch", cf.zPitch, 'f'), \
            ("Motor Steps", cf.zMotorSteps, 'd'), \
            ("Micro Steps", cf.zMicroSteps, 'd'), \
            ("Motor Ratio", cf.zMotorRatio, 'fs'), \
            ("Backlash", cf.zBacklash, 'f'), \
            ("Backlash Incrment", cf.zBackInc, 'f'), \
            ("Accel Unit/Sec2", cf.zAccel, 'fs'), \
            ("Min Speed U/Min", cf.zMinSpeed, 'fs'), \
            ("Max Speed U/Min", cf.zMaxSpeed, 'fs'), \
            ("Jog Min U/Min", cf.zJogMin, 'fs'), \
            ("Jog Max U/Min", cf.zJogMax, 'fs'), \
            ("MPG Jog Increment", cf.zMpgInc, 'fs'), \
            ("MPG Jog Max Dist", cf.zMpgMax, 'fs'), \
            ("Park Loc", cf.zParkLoc, 'f'), \
            ("Probe Dist", cf.zProbeDist, 'f'), \
            ("Probe Speed", cf.zProbeSpeed, 'fs'), \
            ("bInvert Dir", cf.zInvDir, None), \
            ("bInvert MPG", cf.zInvMpg, None), \
            ("DRO Inch", cf.zDROInch, 'd'), \
            ("bInv DRO", cf.zInvDRO, None), \
        )
        self.fieldList(sizerG, self.fields)

        sizerV.Add(sizerG, flag=wx.LEFT|wx.ALL, border=2)

        self.addButton(sizerV, 'Setup Z', self.OnSetup, border=5)

        sizerH = wx.BoxSizer(wx.HORIZONTAL)
        sizerH.Add((0, 0), 0, wx.EXPAND)

        self.addDialogButton(sizerH, wx.ID_OK)

        self.addDialogButton(sizerH, wx.ID_CANCEL, self.OnCancel)

        sizerV.Add(sizerH, 0, wx.ALIGN_RIGHT)

        self.SetSizer(sizerV)
        self.sizerV.Fit(self)
        self.Show(False)

    def setupAction(self):
        sendZData(True)

    def showAction(self, changed):
        global zDataSent
        if changed:
            zDataSent = False

class XDialog(wx.Dialog, FormRoutines, DialogActions):
    def __init__(self, frame, defaultFont):
        pos = (10, 10)
        wx.Dialog.__init__(self, frame, -1, "X Setup", pos, \
                            wx.DefaultSize, wx.DEFAULT_DIALOG_STYLE)
        self.SetFont(defaultFont)
        FormRoutines.__init__(self, False)
        DialogActions.__init__(self)
        self.sizerV = sizerV = wx.BoxSizer(wx.VERTICAL)

        sizerG = wx.FlexGridSizer(cols=2, rows=0, vgap=0, hgap=0)

        self.fields = (
            ("Pitch", cf.xPitch, 'f'), \
            ("Motor Steps", cf.xMotorSteps, 'd'), \
            ("Micro Steps", cf.xMicroSteps, 'd'), \
            ("Motor Ratio", cf.xMotorRatio, 'fs'), \
            ("Backlash", cf.xBacklash, 'f'), \
            ("Accel Unit/Sec2", cf.xAccel, 'fs'), \
            ("Min Speed U/Min", cf.xMinSpeed, 'fs'), \
            ("Max Speed U/Min", cf.xMaxSpeed, 'fs'), \
            ("Jog Min U/Min", cf.xJogMin, 'fs'), \
            ("Jog Max U/Min", cf.xJogMax, 'fs'), \
            ("MPG Jog Increment", cf.xMpgInc, 'fs'), \
            ("MPG Jog Max Dist", cf.xMpgMax, 'fs'), \
            ("Park Loc", cf.xParkLoc, 'f'), \
            ("bInvert Dir", cf.xInvDir, None), \
            ("bInvert MPG", cf.xInvMpg, None), \
            ("Probe Dist", cf.xProbeDist, 'f'), \
            ("Home Dist", cf.xHomeDist, 'f'), \
            ("Home/Probe Speed", cf.xHomeSpeed, 'fs'), \
            ("Backoff Dist", cf.xHomeBackoffDist, 'f'), \
            ("bHome Dir", cf.xHomeDir, None), \
        )
        if DRO:
            self.fields += (
                ("DRO Inch", cf.xDROInch, 'd'), \
                ("bInv DRO", cf.xInvDRO, None), \
                ("bDRO Position", cf.xDROPos, None), \
                ("DRO Final Dist", cf.xDroFinalDist, 'f'), \
                ("DRO Read Delay ms", cf.xDoneDelay, None), \
            )
        if HOME_TEST:
            self.fields += (
                ("Home Start", cf.xHomeStart, 'f'), \
                ("Home End", cf.xHomeEnd, 'f'), \
                ("Home Loc", cf.xHomeLoc, 'f'), \
            )
        self.fieldList(sizerG, self.fields)

        sizerV.Add(sizerG, flag=wx.LEFT|wx.ALL, border=2)

        if HOME_TEST:
            self.addButton(sizerV, 'Set Home Loc', self.OnSetHomeLoc, border=5)

        self.addButton(sizerV, 'Setup X', self.OnSetup, border=5)

        sizerH = wx.BoxSizer(wx.HORIZONTAL)

        sizerH.Add((0, 0), 0, wx.EXPAND)

        self.addDialogButton(sizerH, wx.ID_OK, self.OnOk)

        self.addDialogButton(sizerH, wx.ID_CANCEL, self.OnCancel)

        sizerV.Add(sizerH, 0, wx.ALIGN_RIGHT)

        self.SetSizer(sizerV)
        self.sizerV.Fit(self)
        self.Show(False)

    def OnSetHomeLoc(self, e):
        loc = str(int(cfg.getFloatInfoData(cf.xHomeLoc) * jogPanel.xStepsInch))
        comm.setParm(pm.X_HOME_LOC, loc)

    def setupAction(self):
        sendXData(True)

    def showAction(self, changed):
        global xDataSent
        if changed:
            xDataSent = False

class SpindleDialog(wx.Dialog, FormRoutines, DialogActions):
    def __init__(self, frame, defaultFont):
        pos = (10, 10)
        wx.Dialog.__init__(self, frame, -1, "Spindle Setup", pos, \
                            wx.DefaultSize, wx.DEFAULT_DIALOG_STYLE)
        self.SetFont(defaultFont)
        FormRoutines.__init__(self, False)
        DialogActions.__init__(self)
        self.sizerV = sizerV = wx.BoxSizer(wx.VERTICAL)
        sizerG = wx.FlexGridSizer(cols=2, rows=0, vgap=0, hgap=0)

        self.fields = ( \
            ("bStepper Drive", cf.spStepDrive, None), \
            ("bMotor Test", cf.spMotorTest, None), \
            ("bSpindle Encoder", cf.cfgSpEncoder, None), \
        )
        if SPINDLE_ENCODER:
            self.fields += (("Encoder", cf.cfgEncoder, 'd'),)
            if not FPGA:
                self.fields += (("bSync Board", cf.cfgSpSyncBoard, None),)
        self.fields += ( \
            ("cTurn Sync", cf.cfgTurnSync, 'c', self.turnSync), \
            ("cThread Sync", cf.cfgThreadSync, 'c', self.threadSync), \
        )
        if STEP_DRV or MOTOR_TEST:
            self.fields += ( \
                ("Motor Steps", cf.spMotorSteps, 'd'), \
                ("Micro Steps", cf.spMicroSteps, 'd'), \
                ("Min RPM", cf.spMinRPM, 'd'), \
                ("Max RPM", cf.spMaxRPM, 'd'), \
                ("Accel RPM/Sec2", cf.spAccel, 'fs'), \
                ("Jog Min", cf.spJogMin, 'd'), \
                ("Jog Max", cf.spJogMax, 'd'), \
                ("Jog Time Initial", cf.spJTimeInitial, 'f2'), \
                ("Jog Time Incrmemnt", cf.spJTimeInc, 'f2'), \
                ("Jog Time Maximum", cf.spJTimeMax, 'f2'), \
                # ("Jog Accel Time", cf.spJogAccelTime, 'f'), \
                ("bInvert Dir", cf.spInvDir, None), \
                ("bTest Index", cf.spTestIndex, None), \
                ("bTest Encoder", cf.spTestEncoder, None), \
            )
        else:
            self.fields += ( \
                ("bSwitch", cf.spSwitch, None), \
                ("bVar Speed", cf.spVarSpeed, None), \
            )
        if SPINDLE_VAR_SPEED:
            self.fields += ( \
                ("PWM Frequency", cf.spPWMFreq, None), \
                ("Current Range", cf.spCurRange, None), \
                ("Speed Ranges", cf.spRanges, None), \
            )
            for i in range(6):
                index = str(i + 1)
                tmp = (\
                    ("Min " + index, cf.spRangeMin1 + i , None), \
                    ("Max " + index, cf.spRangeMax1 + i , None), \
                )
                self.fields += tmp
        self.fieldList(sizerG, self.fields)

        sizerV.Add(sizerG, flag=wx.LEFT|wx.ALL, border=2)

        # spindle start and stop

        if STEP_DRV:
            sizerH = wx.BoxSizer(wx.HORIZONTAL)

            self.addButton(sizerH, 'Start', self.OnStart, border=5)

            self.addButton(sizerH, 'Stop', self.OnStop, border=5)

            sizerV.Add(sizerH, 0, wx.CENTER)

        # ok and cancel buttons

        sizerH = wx.BoxSizer(wx.HORIZONTAL)

        self.addDialogButton(sizerH, wx.ID_OK, self.OnOk)

        self.addDialogButton(sizerH, wx.ID_CANCEL, self.OnCancel)

        sizerV.Add(sizerH, 0, wx.ALIGN_RIGHT)

        self.SetSizer(sizerV)
        self.sizerV.Fit(self)

    def turnSync(self):
        if STEP_DRV:
            indexList = (en.SEL_TU_STEP,)
        elif SPINDLE_ENCODER:
            indexList = (en.SEL_TU_ENC,)
            if not FPGA:
                if SPINDLE_SYNC_BOARD:
                    indexList += (en.SEL_TU_ISYN, en.SEL_TU_ESYN)
            else:
                indexList += (en.SEL_TU_SYN,)
        else:
            indexList = (en.SEL_TU_SPEED,)

        choiceList = []
        for i in indexList:
            choiceList.append(en.selTurnText[i])
        return(indexList, choiceList, en.selTurnText)

    def threadSync(self):
        if STEP_DRV:
            indexList = (en.SEL_TH_STEP,)
        elif SPINDLE_ENCODER:
            indexList = (en.SEL_TH_ENC, en.SEL_TH_ISYN_RENC)
            if not FPGA:
                indexList += (en.SEL_TH_ISYN_RENC,)
                if SPINDLE_SYNC_BOARD:
                    indexList += (en.SEL_TH_ESYN_RENC, en.SEL_TH_ESYN_RSYN)
            else:
                indexList = (en.SEL_TH_ENC, en.SEL_TH_SYN)
        else:
            indexList += (en.SEL_TH_NO_ENC,)
            
        choiceList = []
        for i in indexList:
            choiceList.append(en.selThreadText[i])
        return(indexList, choiceList, en.selThreadText)

    def OnStart(self, e):
        global spindleDataSent
        if not self.formatData(self.fields):
            return
        for (label, index, fmt) in self.fields:
            tmp = cfg.getInfoData(index)
            if self.fieldInfo[index] != tmp:
                self.fieldInfo[index] = tmp
                spindleDataSent = False
        if not spindleDataSent:
            sendSpindleData()
        else:
            comm.command(cm.CMD_SPSETUP)
        comm.command(cm.SPINDLE_START)

    def OnStop(self, e):
        comm.command(cm.SPINDLE_STOP)

    def showAction(self, changed):
        global spindleDataSent
        if changed:
            spindleDataSent = False

class PortDialog(wx.Dialog, FormRoutines, DialogActions):
    def __init__(self, frame, defaultFont):
        pos = (10, 10)
        wx.Dialog.__init__(self, frame, -1, "Port Setup", pos, \
                            wx.DefaultSize, wx.DEFAULT_DIALOG_STYLE)
        self.SetFont(defaultFont)
        FormRoutines.__init__(self, False)
        DialogActions.__init__(self)
        self.sizerV = sizerV = wx.BoxSizer(wx.VERTICAL)
        sizerG = wx.FlexGridSizer(cols=2, rows=0, vgap=0, hgap=0)

        self.fields = ( \
            ("Comm Port", cf.commPort, None), \
            ("Comm Rate", cf.commRate, 'd'), \
            ("Keypad Port", cf.keypadPort, None), \
            ("Keypad Rate", cf.keypadRate, 'd'), \
        )
        if SPINDLE_SYNC_BOARD:
            self.fields += ( \
                ("Sync Port", cf.syncPort, None), \
                ("Sync Rate", cf.syncRate, 'd'), \
            )
        if EXT_DRO:
            self.fields += ( \
                ("Ext DRO Port", cf.extDroPort, None), \
                ("Ext DRO Baud Rate", cf.extDroRate, 'd'), \
            )
        self.fieldList(sizerG, self.fields)

        sizerV.Add(sizerG, flag=wx.LEFT|wx.ALL, border=2)
        sizerH = wx.BoxSizer(wx.HORIZONTAL)
        sizerH.Add((0, 0), 0, wx.EXPAND)

        self.addDialogButton(sizerH, wx.ID_OK, self.OnOk)

        self.addDialogButton(sizerH, wx.ID_CANCEL, self.OnCancel)

        sizerV.Add(sizerH, 0, wx.ALIGN_RIGHT)

        self.SetSizer(sizerV)
        self.sizerV.Fit(self)
        self.Show(False)

    def showAction(self, changed):
        pass

class ConfigDialog(wx.Dialog, FormRoutines, DialogActions):
    def __init__(self, frame, defaultFont):
        pos = (10, 10)
        wx.Dialog.__init__(self, frame, -1, "Config Setup", pos, \
                           wx.DefaultSize, wx.DEFAULT_DIALOG_STYLE)
        self.SetFont(defaultFont)
        FormRoutines.__init__(self, False)
        DialogActions.__init__(self)
        self.sizerV = sizerV = wx.BoxSizer(wx.VERTICAL)
        sizerG = wx.FlexGridSizer(cols=2, rows=0, vgap=0, hgap=0)

        self.fields = (
            ("bFPGA Control", cf.cfgFpga, None), \
            ("bMPG", cf.cfgMPG, None), \
            ("bDRO", cf.cfgDRO, None), \
            ("bExternal DRO", cf.cfgExtDro, None), \
            ("bLCD", cf.cfgLCD, None), \
            ("bProbe Inv", cf.cfgPrbInv, None), \
            ("wfcy", cf.cfgFcy, 'd'), \
            ("bDisable Commands", cf.cfgCmdDis, None), \
            ("bDraw Moves", cf.cfgDraw, None), \
            ("bSave Debug", cf.cfgDbgSave, None), \
            ("bRemote Debug", cf.cfgRemDbg, None), \
            ("bHome in Place", cf.cfgHomeInPlace, None), \
            ("Taper Cycle Dist", cf.cfgTaperCycleDist, 'f'), \
            ("Jog Time Initial", cf.jogTimeInitial, 'f2'), \
            ("Jog Time Incrmemnt", cf.jogTimeInc, 'f2'), \
            ("Jog Time Maximum", cf.jogTimeMax, 'f2'), \
            ("bMpg Jog Debug", cf.cfgJogDebug, None), \
        )
        if FPGA:
                # ("Encoder", cf.cfgEncoder, 'd'), \
            self.fields += (
                ("wFPGA Freq", cf.cfgFpgaFreq, 'd'), \
                ("Freq Mult", cf.cfgFreqMult, 'd'), \
                ("bTest Mode", cf.cfgTestMode, None), \
                ("Test RPM", cf.cfgTestRPM, 'd'), \
                ("bInvert Enc Dir", cf.cfgInvEncDir, None), \
            )
        self.fieldList(sizerG, self.fields)

        sizerV.Add(sizerG, flag=wx.CENTER|wx.ALL, border=2)

        sizerH = wx.BoxSizer(wx.HORIZONTAL)
        sizerH.Add((0, 0), 0, wx.EXPAND)

        self.addDialogButton(sizerH, wx.ID_OK, self.OnOk)

        self.addDialogButton(sizerH, wx.ID_CANCEL, self.OnCancel)

        sizerV.Add(sizerH, 0, wx.ALIGN_RIGHT)

        self.SetSizer(sizerV)
        self.sizerV.Fit(self)
        self.Show(False)

    def showAction(self, changed):
        pass

def testText(dialog, defaultFont):
    dialog.sizerV = sizerV = wx.BoxSizer(wx.VERTICAL)

    txt = wx.TextCtrl(dialog, style=wx.TE_MULTILINE, size=(650,350))
    txt.SetFont(defaultFont)
    # w, h = txt.GetTextExtent("0123456789")
    # w *= 8
    # h *= 24
    # txt.SetSize((w, h))
    sizerV.Add(txt)

    dialog.SetSizer(sizerV)
    dialog.sizerV.Fit(dialog)
    return(txt)

class TestSpindleDialog(wx.Dialog):
    def __init__(self, frame, defaultFont):
        pos = (10, 10)
        wx.Dialog.__init__(self, frame, -1, "Test Spindle", pos, \
                            wx.DefaultSize, wx.DEFAULT_DIALOG_STYLE)

        txt = testText(self, defaultFont)
        self.spindleTest = SpindleTest(txt)

class TestSyncDialog(wx.Dialog):
    def __init__(self, frame, defaultFont):
        pos = (10, 10)
        wx.Dialog.__init__(self, frame, -1, "Test Sync", pos, \
                            wx.DefaultSize, wx.DEFAULT_DIALOG_STYLE)

        txt = testText(self, defaultFont)
        self.syncTest = SyncTest(txt)

class TestTaperDialog(wx.Dialog):
    def __init__(self, frame, defaultFont):
        pos = (10, 10)
        wx.Dialog.__init__(self, frame, -1, "Test Taper", pos, \
                            wx.DefaultSize, wx.DEFAULT_DIALOG_STYLE)

        txt = testText(self, defaultFont)
        self.taperTest = TaperTest(txt)

class TestMoveDialog(wx.Dialog):
    def __init__(self, frame, defaultFont):
        pos = (10, 10)
        wx.Dialog.__init__(self, frame, -1, "Test Move", pos, \
                            wx.DefaultSize, wx.DEFAULT_DIALOG_STYLE)

        txt = testText(self, defaultFont)
        self.moveTest = MoveTest(txt)

def dbgPrt(txt, fmt, values):
    txt.AppendText((fmt + "\n") % values)
    f.write((fmt + "\n") % values)

fcy = 90000000

class SpindleTest():
    def __init__(self, txt):
        self.txt = txt

    def test(self):
        global f
        txt = self.txt
        txt.SetValue("")
        minRPM = cfg.getFloatInfoData(cf.spMinRPM) # minimum rpm
        maxRPM = cfg.getFloatInfoData(cf.spMaxRPM) # maximum rpm
        accel = cfg.getFloatInfoData(cf.spAccel)   # accel rpm per sec

        f = open(os.path_join(DBG_DIR, 'spindle.txt'), 'w')

        dbgPrt(txt, "minRPM %d maxRPM %d", (minRPM, maxRPM))

        spindleMicroSteps = cfg.getIntInfoData(cf.spMicroSteps)
        spindleMotorSteps = cfg.getIntInfoData(cf.spMotorSteps)
        spindleStepsRev = spindleMotorSteps * spindleMicroSteps
        dbgPrt(txt, "spindleStepsRev %d", (spindleStepsRev))

        spindleStepsSec = (maxRPM * spindleStepsRev) / 60.0
        spindleClocksStep = int(fcy / spindleStepsSec + .5)
        spindleClockPeriod = (float(spindleClocksStep) / fcy) * 1000000
        spindleClocksRev = spindleStepsRev * spindleClocksStep
        dbgPrt(txt, "spindleClocksStep %d spindleClockPeriod %6.3f us " +
               "spindleClocksRev %d",
               (spindleClocksStep, spindleClockPeriod, spindleClocksRev))

        # accelStepsSec2 = (accel * spindleStepsRev) / 60

        sStepsSecMin = float(minRPM * spindleStepsRev) / 60
        sStepsSecMax = float(maxRPM * spindleStepsRev) / 60
        deltaV = sStepsSecMax - sStepsSecMin
        dbgPrt(txt, "deltaV %4.1f sStepsSecMin %4.1f sStepsSecMax %4.1f", \
               (deltaV, sStepsSecMin, sStepsSecMax))
        if False:
            pass
            # accelStepsSec2 = deltaV / aTime
            # accel = (accelStepsSec2 / spindleStepsRev) * 60
        else:
            accelStepsSec2 = (accel / 60) * spindleStepsRev
            # aTime = deltaV / accelStepsSec2

        dbgPrt(txt, "accel %0.1f rpm per sec", (accel))

        accelMinTime = sStepsSecMin / accelStepsSec2
        accelMaxTime = sStepsSecMax / accelStepsSec2
        dbgPrt(txt, "accelMinTime %5.5f accelMaxTime %5.2f", \
               (accelMinTime, accelMaxTime))

        accelMinSteps = round((sStepsSecMin * accelMinTime) / 2.0)
        accelMaxSteps = round((sStepsSecMax * accelMaxTime) / 2.0)
        dbgPrt(txt, "accelMinSteps %d accelMaxSteps %d ", \
               (accelMinSteps, accelMaxSteps))

        accelTime = deltaV / accelStepsSec2
        accelSteps = accelMaxSteps - accelMinSteps
        accelClocks = accelTime * fcy
        dbgPrt(txt, "accelStepsSec2 %0.1f accelTime %5.3f accelSteps %d "\
               "accelClocks %d", \
               (accelStepsSec2, accelTime, accelSteps, accelClocks))

        accelRev = float(accelSteps) / spindleStepsRev
        dbgPrt(txt, "accelRev %5.3f", (accelRev))

        cFactorA = (fcy * sqrt(2)) / sqrt(accelStepsSec2)
        cFactorB = spindleClocksStep / (sqrt(accelMaxSteps) -
                                        sqrt(accelMaxSteps - 1))
        dbgPrt(txt, "cFactorA %0.2f cFactorB %0.2f", (cFactorA, cFactorB))
        cFactor = cFactorB

        lastCount = int(cFactor * sqrt(accelMinSteps))
        lastTime = float(lastCount) / fcy

        dbgPrt(txt, "accelMinSteps %d lastCount %d lastTime %0.6f", \
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
            time0 = float(actCount) / fcy
            delta = time0 - lastTime
            freq = 1.0 / delta
            rpm = (freq / spindleStepsRev) * 60
            f.write("step %4d count %9d %9d pre %d %5d %6d t %8.6f %8.6f "\
                    "f %8.2f rpm %4.1f\n" % \
                    (step, count, actCount, pre, ctr, ctr * pre - lastCtr, \
                     time0, delta, freq, rpm))
            lastCount = actCount
            lastCtr = ctr * pre
            lastTime = time0

        f.write("\n")

        finalCount = int(cFactor * sqrt(accelMaxSteps))
        finalCount -= int(cFactor * sqrt(accelMaxSteps - 1))
        dbgPrt(txt, "finalCount %d lastCtr %d spindleClocksStep %d", \
               (finalCount, ctr, spindleClocksStep))

        f.write("\n***\n\n")

        while step > accelMinSteps:
            step -= 1
            count = int(cFactor * sqrt(step))
            ctr = lastCount - count
            time0 = float(count) / fcy
            delta = lastTime - time0
            freq = 1.0 / delta
            rpm = (freq / spindleStepsRev) * 60
            f.write("step %4d count %9d %7d %5d t %8.6f %8.6f "\
                    "f %8.2f rpm %4.1f\n" % \
                    (step, count, ctr, ctr - lastCtr, time0, delta, freq, rpm))
            lastCount = count
            lastCtr = ctr
            lastTime = time0

        lastCount = int(cFactor * sqrt(accelMinSteps))
        f.write("\naccelMinSteps %d lastCount %d\n" % \
                (accelMinSteps, lastCount))

        f.close()

class SyncTest(object):
    def __init__(self, txt):
        self.txt = txt

    def test(self):
        global f
        txt = self.txt
        txt.SetValue("")
        print("")
        f = open(os.path_join(DBG_DIR, 'zsync.txt'), 'w')

        zAxis = True
        panel = cfg.getInfoData(cf.mainPanel)
        if panel == 'threadPanel':
            arg1 = cfg.getFloatInfoData(cf.thThread)
        elif panel == 'turnPanel':
            arg1 = cfg.getFloatInfoData(cf.tuZFeed)
        elif panel == 'facePanel':
            arg1 = cfg.getFloatInfoData(cf.faXFeed)
            zAxis = False
        elif panel == 'CutoffPanel':
            arg1 = cfg.getFloatInfoData(cf.cuXFeed)
            zAxis = False
        elif panel == 'taperPanel':
            arg1 = cfg.getFloatInfoData(cf.tpZFeed)

        maxRPM = cfg.getFloatInfoData(cf.spMaxRPM) # maximum rpm

        spindleMicroSteps = cfg.getIntInfoData(cf.spMicroSteps)
        spindleMotorSteps = cfg.getIntInfoData(cf.spMotorSteps)
        spindleStepsRev = spindleMotorSteps * spindleMicroSteps
        dbgPrt(txt, "spindleStepsRev %d", (spindleStepsRev))

        spindleStepsSec = (maxRPM * spindleStepsRev) / 60.0
        spindleClocksStep = int(fcy / spindleStepsSec + .5)
        spindleClockPeriod = (float(spindleClocksStep) / fcy) * 1000000
        spindleClocksRev = spindleStepsRev * spindleClocksStep
        dbgPrt(txt, "spindleClocksStep %d spindleClockPeriod %6.3f us "\
               "spindleClocksRev %d", \
               (spindleClocksStep, spindleClockPeriod, spindleClocksRev))
        dbgPrt(txt, "", ())

        if zAxis:
            pitch = cfg.getDistInfoData(cf.zPitch)
            microSteps = cfg.getFloatInfoData(cf.zMicroSteps)
            motorSteps = cfg.getFloatInfoData(cf.zMotorSteps)
            motorRatio = cfg.getFloatInfoData(cf.zMotorRatio)
        else:
            pitch = cfg.getDistInfoData(cf.xPitch)
            microSteps = cfg.getFloatInfoData(cf.xMicroSteps)
            motorSteps = cfg.getFloatInfoData(cf.xMotorSteps)
            motorRatio = cfg.getFloatInfoData(cf.xMotorRatio)

        zStepsInch = ((microSteps * motorSteps * motorRatio) / pitch)
        dbgPrt(txt, "zStepsInch %d", (zStepsInch))

        if arg1 >= 8:
            inch = True
            inchPitch = False
            tpi = arg1
        else:
            inch = False
            pitch = arg1
            if pitch < .3:
                inchPitch = True

        if inchPitch:
            revCycle = round(1.0 / pitch)
            if revCycle > 20:
                revCycle = 20
            cycleDist = revCycle * pitch
            dbgPrt(txt, "pitch %5.3f revCycle %d cycleDist %5.3f", \
                   (pitch, revCycle, cycleDist))
            clocksCycle = spindleClocksRev * revCycle
            spindleStepsCycle = spindleStepsRev * revCycle
            zStepsCycle = zStepsInch * revCycle * pitch
        elif inch:
            clocksCycle = spindleClocksRev * tpi
            spindleStepsCycle = spindleStepsRev * tpi
            zStepsCycle = zStepsInch
            pitch = 1.0 / tpi
            dbgPrt(txt, "tpi %d pitch %5.3f", (tpi, pitch))
        else:
            revolutions = 127
            inches = (pitch * revolutions) / 25.4
            dbgPrt(txt, "pitch %4.2f mm inches %5.3f", (pitch, inches))

            clocksCycle = spindleClocksRev * revolutions
            spindleStepsCycle = spindleStepsRev * revolutions
            zStepsCycle = zStepsInch * inches

        cycleTime = float(clocksCycle) / fcy
        dbgPrt(txt, "clocksCycle %d cycleTime %4.2f\nspindleStepsCycle %d "\
               "zStepsCycle %d", \
               (clocksCycle, cycleTime, spindleStepsCycle, zStepsCycle))

        zClocksStep = round(clocksCycle / zStepsCycle)
        zRemainder = (clocksCycle - zClocksStep * zStepsCycle)
        dbgPrt(txt, "zClocksStep %d remainder %d", \
               (zClocksStep, zRemainder))

        dx = zStepsCycle
        dy = zRemainder
        incr1 = 2 * dy
        incr2 = incr1 - 2 * dx
        d = incr1 - dx
        dbgPrt(txt, "incr1 %d incr2 %d d %d", (incr1, incr2, d))

        rSum = d
        x = 0
        y = 0
        clocks = 0
        while x < zStepsCycle:
            x += 1
            clocks += zClocksStep
            if rSum < 0:
                rSum += incr1
            else:
                y += 1
                rSum += incr2
                clocks += 1
        dbgPrt(txt, "clocks %d x %d y %d", (clocks, x, y))

        dbgPrt(txt, "", ())

        zSpeedIPM = pitch * maxRPM
        zStepsPerSec = int((zSpeedIPM * zStepsInch) / 60)
        dbgPrt(txt, "zSpeedIPM %4.2f in/min zStepsSec %d steps/sec", \
               (zSpeedIPM, zStepsPerSec))

        zAccel = .5                      # acceleration in per sec^2
        zAccelTime = ((zSpeedIPM / 60.0) / zAccel) # acceleration time
        dbgPrt(txt, "zAccel %5.3f in/sec^2 zAccelTime %8.6f sec", \
               (zAccel, zAccelTime))

        zAccelStepsSec2 = zAccel * zStepsInch
        dbgPrt(txt, "zAccelStepsSec2 %3.0f steps/sec^2", (zAccelStepsSec2))

        zAccelSteps = int((zAccelTime * zStepsPerSec) / 2.0)
        if zAccelSteps != 0:
            cFactorA = (fcy * sqrt(2)) / sqrt(zAccelStepsSec2)
            cFactorB = zClocksStep / (sqrt(zAccelSteps) -
                                      sqrt(zAccelSteps - 1))
            dbgPrt(txt, "cFactorA %0.2f cFactorB %0.2f", (cFactorA, cFactorB))
            cFactor1 = cFactorB

            zAccelClocks = int(cFactor1 * sqrt(zAccelSteps))
            zAccelTime = float(zAccelClocks) / fcy
            zAccelDist = float(zAccelSteps) / zStepsInch
            dbgPrt(txt, "zAccelTime %8.6f zAccelSteps %d zAccelClocks %d "\
                   "zAccelDist %5.3f", \
                   (zAccelTime, zAccelSteps, zAccelClocks, zAccelDist))

            initialCount = int(cFactor1 * sqrt(1))
            initialCount -= int(cFactor1 * sqrt(0))
            finalCount = int(cFactor1 * sqrt(zAccelSteps))

            isrCount = finalCount + initialCount

            dbgPrt(txt, "initialCount %d initialTime %8.6f accelTime %8.6f "\
                   "hwTime %8.6f", \
                   (initialCount, float(initialCount) / fcy, \
                    float(finalCount) / fcy, float(isrCount) / fcy))

            zAccelSpindleSteps = int(isrCount / spindleClocksStep)
            remainder = isrCount - zAccelSpindleSteps * spindleClocksStep
            dbgPrt(txt, "zAccelSpindleSteps %d remainder %d", \
                   (zAccelSpindleSteps, remainder))

            f.write("\n")

            lastCount = 0
            lastTime = 0
            lastCtr = 0
            # dbgPrt(txt, "lastCount %d lastTime %0.6f" % (lastCount, lastTime)
            for step in range(1, zAccelSteps + 1):
                count = int(cFactor1 * sqrt(step))
                ctr = count - lastCount
                time0 = float(count) / fcy
                delta = time0 - lastTime
                freq = 1.0 / delta
                ipm = (freq / zStepsInch) * 60
                f.write("step %4d count %9d %9d %9d t %8.6f %8.6f "\
                        "f %7.2f ipm %4.1f\n" % \
                        (step, count, ctr, ctr - lastCtr, time0, delta, \
                         freq, ipm))
                lastCount = count
                lastCtr = ctr
                lastTime = time0

            f.write("\n")

            # countRemainder = zAccelClocks - lastCount
            # div = int(countRemainder / zAccelSteps)
            # rem = countRemainder - zAccelSteps * div
            # dbgPrt(txt, "lastCount %d countRemainder %d div %d rem %d" % \
            #        (lastCount, countRemainder, div, rem))

            lastCount1 = int(cFactor1 * sqrt(zAccelSteps))
            lastTime1 = float(count) / fcy
            dbgPrt(txt, "lastCount1 %d lastTime1 %0.6f", \
                   (lastCount1, lastTime1))

            # spindleSteps = lastCount1 / spindleClocksStep
            # spindleCount = spindleSteps * spindleClocksStep
            # countRemainder = lastCount1 - (spindleSteps * spindleClocksStep)

            # div = int(countRemainder / zAccelSteps)
            # rem = countRemainder - zAccelSteps * div
            # dbgPrt(txt, "spindleSteps %d lastCount %d "\
            #       "countRemainder %d div "%d rem %d", \
            #        (spindleSteps, lastCount, countRemainder, div, rem))

            finalCount -= int(cFactor1 * sqrt(zAccelSteps - 1))
            dbgPrt(txt, "finalCount %d lastCtr %d zClocksStep %d", \
                   (finalCount, lastCtr, zClocksStep))

        f.close()

class TaperTest(object):
    def __init__(self, txt):
        self.txt = txt

    def test(self):
        global f
        txt = self.txt
        txt.SetValue("")
        f = open(os.path_join(DBG_DIR, 'taper.txt'), 'w')

        maxRPM = cfg.getFloatInfoData(cf.spMaxRPM) # maximum rpm
        spindleMicroSteps = cfg.getIntInfoData(cf.spMicroSteps)
        spindleMotorSteps = cfg.getIntInfoData(cf.spMotorSteps)
        spindleStepsRev = spindleMotorSteps * spindleMicroSteps
        dbgPrt(txt, "spindleStepsRev %d", (spindleStepsRev))

        spindleStepsSec = (maxRPM * spindleStepsRev) / 60.0
        spindleClocksStep = int(fcy / spindleStepsSec + .5)
        spindleClockPeriod = (float(spindleClocksStep) / fcy) * 1000000
        spindleClocksRev = spindleStepsRev * spindleClocksStep
        dbgPrt(txt, "spindleClocksStep %d spindleClockPeriod %6.3f us "\
               "spindleClocksRev %d", \
               (spindleClocksStep, spindleClockPeriod, spindleClocksRev))
        dbgPrt(txt, "", ())

        pitch = cfg.getDistInfoData(cf.zPitch)
        microSteps = cfg.getFloatInfoData(cf.zMicroSteps)
        motorSteps = cfg.getFloatInfoData(cf.zMotorSteps)
        motorRatio = cfg.getFloatInfoData(cf.zMotorRatio)

        zStepsInch = ((microSteps * motorSteps * motorRatio) / pitch)
        dbgPrt(txt, "zStepsInch %d", (zStepsInch))

        pitch = cfg.getDistInfoData(cf.xPitch)
        microSteps = cfg.getFloatInfoData(cf.xMicroSteps)
        motorSteps = cfg.getFloatInfoData(cf.xMotorSteps)
        motorRatio = cfg.getFloatInfoData(cf.xMotorRatio)
        xStepsInch = ((microSteps * motorSteps * motorRatio) / pitch)
        dbgPrt(txt, "xStepsInch %d", (xStepsInch))

        pitch = cfg.getFloatInfoData(cf.tpZFeed)
        revCycle = round(1.0 / pitch)
        if revCycle > 20:
            revCycle = 20
        cycleDist = revCycle * pitch
        dbgPrt(txt, "pitch %5.3f revCycle %d cycleDist %5.3f", \
               (pitch, revCycle, cycleDist))
        clocksCycle = spindleClocksRev * revCycle
        spindleStepsCycle = spindleStepsRev * revCycle
        zStepsCycle = zStepsInch * revCycle * pitch

        zClocksStep = round(clocksCycle / zStepsCycle)
        zRemainder = (clocksCycle - zClocksStep * zStepsCycle)
        dbgPrt(txt, "spindleStepsCycle %d zStepsCycle %d " \
               "zClocksStep %d remainder %d", \
               (spindleStepsCycle, zStepsCycle, zClocksStep, zRemainder))

        arg2 = cfg.getFloatInfoData(cf.tpZDelta)
        arg3 = cfg.getFloatInfoData(cf.tpXDelta)

        d0 = arg2
        d1 = arg3

        zCycleDist = float(zStepsCycle) / zStepsInch
        xCycleDist = (d1 / d0) * zCycleDist
        dbgPrt(txt, "zCycleDist %5.3f xCycleDist %5.3f", \
               (zCycleDist, xCycleDist))

        d0Steps = int(zCycleDist * zStepsInch)
        d1Steps = int(xCycleDist * xStepsInch)
        d0Clocks = d0Steps * zClocksStep
        dbgPrt(txt, "d0Steps %d d1Steps %d d0Clocks %d", \
               (d0Steps, d1Steps, d0Clocks))

        # d1ClocksStep = int(d0Clocks / d1Steps)
        # d1Remainder = d0Clocks - d1Steps * d1ClocksStep
        # dbgPrt(txt, "d1ClocksStep %d d1Remainder %d", \
        #        (d1ClocksStep, d1Remainder))

        d1ClocksStep = int(clocksCycle / d1Steps)
        d1Remainder = clocksCycle - d1Steps * d1ClocksStep
        dbgPrt(txt, "d1ClocksStep %d d1Remainder %d", \
               (d1ClocksStep, d1Remainder))

        dx = d1Steps
        dy = d1Remainder
        incr1 = 2 * dy
        incr2 = incr1 - 2 * dx
        d = incr1 - dx
        dbgPrt(txt, "incr1 %d incr2 %d d %d", \
               (incr1, incr2, d))

        f.close()

class MoveTest(object):
    def __init__(self, txt):
        self.txt = txt

    def test(self):
        global f
        txt = self.txt
        txt.SetValue("")

        f = open(os.path_join(DBG_DIR, 'move.txt'), 'w')

        pitch = cfg.getFloatInfoData(cf.zPitch)
        microSteps = cfg.getFloatInfoData(cf.zMicroSteps)
        motorSteps = cfg.getFloatInfoData(cf.zMotorSteps)
        motorRatio = cfg.getFloatInfoData(cf.zMotorRatio)

        zStepsInch = ((microSteps * motorSteps * motorRatio) / pitch)
        dbgPrt(txt, "zStepsInch %d", (zStepsInch))

        minSpeed = cfg.getFloatInfoData(cf.zMinSpeed) # minimum speed ipm
        maxSpeed = cfg.getFloatInfoData(cf.zMaxSpeed) # maximum speed ipm
        zMoveAccelTime = cfg.getFloatInfoData(cf.zAccel) # accel time seconds
        dbgPrt(txt, "zMinSpeed %d zMaxSpeed %d zMoveAccelTime %4.2f", \
               (minSpeed, maxSpeed, zMoveAccelTime))

        zMStepsSec = int((maxSpeed * zStepsInch) / 60.0)
        zMClocksStep = int(fcy / zMStepsSec)
        dbgPrt(txt, "zMStepsSec %d zMClocksStep %d", \
               (zMStepsSec, zMClocksStep))

        zMinStepsSec = int((zStepsInch * minSpeed) / 60.0)
        zMaxStepsSec = int((zStepsInch * maxSpeed) / 60.0)
        dbgPrt(txt, "zMinStepsSec %d zMaxStepsSec %d", \
               (zMinStepsSec, zMaxStepsSec))

        zMDeltaV = zMaxStepsSec - zMinStepsSec
        zMAccelStepsSec2 = zMDeltaV / zMoveAccelTime
        dbgPrt(txt, "zMDeltaV %d zMAccelStepsSec2 %6.3f", \
               (zMDeltaV, zMAccelStepsSec2))

        if zMAccelStepsSec2 != 0:
            zMAccelMinTime = zMinStepsSec / zMAccelStepsSec2
            zMAccelMaxTime = zMaxStepsSec / zMAccelStepsSec2
            dbgPrt(txt, "zMAccelMinTime %d zMAccelMaxTime %d", \
                   (zMAccelMinTime, zMAccelMaxTime))

            zMAccelMinSteps = round((zMinStepsSec * zMAccelMinTime) / 2.0)
            zMAccelMaxSteps = round((zMaxStepsSec * zMAccelMaxTime) / 2.0)
            dbgPrt(txt, "zMAccelMinSteps %d zMAccelMaxSteps %d", \
                   (zMAccelMinSteps, zMAccelMaxSteps))

            zMAccelTime = zMDeltaV / zMAccelStepsSec2
            zMAccelSteps = zMAccelMaxSteps - zMAccelMinSteps
            zMAccelClocks = int(zMAccelTime * fcy)
            dbgPrt(txt, "zMAccelTime %5.3f zMAccelSteps %d zMAccelClocks %d", \
                   (zMAccelTime, zMAccelSteps, zMAccelClocks))

            zMAccelDist = float(zMAccelSteps) / zStepsInch
            dbgPrt(txt, "zMAccelDist %5.3f", (zMAccelDist))

            cFactorA = (fcy * sqrt(2)) / sqrt(zMAccelStepsSec2)
            cFactorB = zMClocksStep / (sqrt(zMAccelSteps) -
                                       sqrt(zMAccelSteps - 1))
            dbgPrt(txt, "cFactorA %0.2f cFactorB %0.2f", (cFactorA, cFactorB))
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
                time0 = float(count) / fcy
                delta = time0 - lastTime
                freq = 1.0 / delta
                ipm = (freq / zStepsInch) * 60
                f.write("step %4d count %9d %7d %7d t %8.6f %8.6f "\
                        "f %7.2f rpm %3.1f\n" % \
                        (step, count, ctr, abs(ctr - lastCtr), time0, \
                         delta, freq, ipm))
                lastCount = count
                lastCtr = ctr
                lastTime = time0

            f.write("\n")

            finalCount = int(zMCFactor * (sqrt(zMAccelSteps) -
                                          sqrt(zMAccelSteps - 1)))
            dbgPrt(txt, "finalCount %d lastCtr %d zMClocksStep %d", \
                   (finalCount, ctr, zMClocksStep))

            f.write("\n***\n\n")

            while step > zMAccelMinSteps:
                step -= 1
                count = int(zMCFactor * sqrt(step))
                ctr = lastCount - count
                time0 = float(count) / fcy
                delta = lastTime - time0
                freq = 1.0 / delta
                ipm = (freq / zStepsInch) * 60
                f.write("step %4d count %9d %7d %7d t %8.6f %8.6f "\
                        "f %7.2f ipm %3.1f\n" % \
                        (step, count, ctr, abs(ctr - lastCtr), time0, \
                         delta, freq, ipm))
                lastCount = count
                lastCtr = ctr
                lastTime = time0

            lastCount = int(zMCFactor * sqrt(zMAccelMinSteps))
            f.write("\nzMAccelMinSteps %d lastCount %d\n" % \
                    (zMAccelMinSteps, lastCount))

            f.close()

# n = 1
# while True:
#     if n >= len(sys.argv):
#         break
#     tmpArg = sys.argv[n]
#     # if len(tmpArg) != 0 and tmpArg[0].isdigit():
#     #     break
#     tmpArg = tmpArg.lower()
#     if tmpArg == 'xhomed':
#         xHomed = True
#     else:
#         print("invalid argument: %s" % (tmpArg))
#         stdout.flush()
#         break
#     n += 1

class MainApp(wx.App):
    def OnInit(self):
        """Init Main App."""
        print("mainapp")
        global mainFrame
        mainFrame = frame = MainFrame(None, "Lathe Control")
        frame.Show(True)
        self.SetTopWindow(frame)
        return True

    def FilterEvent(self, evt):
        if evt.EventType == wx.EVT_KEY_DOWN:
            print(evt)
        return(-1)

factor = Factor(MAX_PRIME)

app = MainApp(redirect=False)
# app.SetCallFilterEvent(True)
# wx.lib.inspection.InspectionTool().Show()
app.MainLoop()

if comm.ser is not None:
    comm.ser.close()
