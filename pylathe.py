#!/cygdrive/c/Python310/Python.exe
#!/usr/bin/python
#!/cygdrive/c/DevSoftware/Python/Python36-32/Python
################################################################################

#--xhomed ../TPyLathe/config.txt -p ../TPyLathe/posInfo.txt

import math
import os
import re
import subprocess
import sys
import traceback
from ctypes import c_uint32
from math import atan2, ceil, cos, degrees, hypot, pi, \
    radians, sin, sqrt, tan
from platform import system
#from Queue import Empty, Queue
from queue import Empty, Queue
from sys import stderr, stdout
from threading import Event, Thread
from time import sleep, time
from datetime import datetime
from pytz import timezone
from collections import namedtuple
from extDro import DroTimeout
# from contextlib import redirect_stderr
#     with open(os.path.join(DBG_DIR, "err.log")) as stderr, \
#          redirect_stderr(stderr):

import serial
import wx
import wx.lib.inspection
from dxfwrite import DXFEngine as dxf

import remCmdDef as cm
import configDef as cf
import ctlBitDef as ct
import enumDef as en
import megaEnumDef as em
import remParmDef as pm
import megaParmDef as mp
import stringDef as st
import syncCmdDef as sc
import syncParmDef as sp
from configInfo import ConfigInfo, InfoValue
from sync import Sync

import cairo
import wx.lib.wxcairo as wxcairo

DBG_DIR = os.path.join(os.getcwd(), "dbg")
DXF_DIR = os.path.join(os.getcwd(), "dxf")
DBG_LOG = os.path.join(DBG_DIR, "dbgLog.txt")

stdError = stderr
stderr = open(os.path.join(DBG_DIR, "err.log"), 'w')
stderr.write("testing\n")

R_PI = False
RISCV = False
xArgs = sys.argv
for xArg in xArgs:
    if "--rpi" == xArg:
        R_PI = True
    if "--riscv" == xArg:
        RISCV = True

print("R_PI %s RISCV %s" % (str(R_PI), str(RISCV)))

from comm import CommTimeout
WINDOWS = system() == 'Windows'
if WINDOWS:
    from pywinusb.hid import find_all_hid_devices, HIDError
    if R_PI:
        if not RISCV:
            from commPi import CommPi
        else:
            from commRiscv import CommRiscv
    else:
        from comm import Comm
    pncDir = ("Python", "Pnc")
    dirStrip = -2
else:
    print(os.uname())
    if not os.uname().machine.startswith('arm'):
        from comm import Comm
    else:
        from commPi import CommPi
        R_PI = True
    pncDir = ("pnc",)
    dirStrip = -1

fileDir = os.path.dirname(os.path.abspath(__file__))
filePath = ""
for f in tuple(fileDir.split(os.sep)[:dirStrip]) + pncDir:
    if len(f) != 0 and not (":" in f):
        filePath += os.sep
    filePath += f
sys.path.append(filePath)
print(sys.path)

from geometry import Line
from geometry import ARC, CW, LINE
from geometry import Arc as GeoArc
import dbgprt as dp
dp.DBG = True

SWIG = False
HOME_TEST = False
SETUP = False

MEGA = False
FPGA = False
DRO = False
EXT_DRO = False
X_DRO_POS = False
Z_DRO_POS = False
REM_DBG = False
STEP_DRV = False
MOTOR_TEST = False
SPINDLE_ENCODER = False
SPINDLE_SYNC_BOARD = False
SPINDLE_INTERNAL_SYNC = False
SPINDLE_SWITCH = False
SPINDLE_VAR_SPEED = False
HOME_IN_PLACE = False
SYNC_SPI = False

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
        setup.createFpgaReg(xilinxList, cLoc, xLoc, fData)
        setup.createFpgaBits(xilinxBitList, cLoc, xLoc, fData)

    importList = setup.importList
    setupCmd = "from setup import "
    for var in importList:
        setupCmd += var + ","
    exec(setupCmd[:-1])

# if SWIG:
#     import lathe
#     from lathe import taperCalc, T_ACCEL, zTaperInit, xTaperInit

print(sys.version)
print(wx.version())
stdout.flush()

REF = 'REF'
TEXT = 'TEXT'

EVT_STATUS_UPDATE_ID = wx.Window.NewControlId()

class StatusEvent(wx.PyEvent):
    def __init__(self, data):
        wx.PyEvent.__init__(self)
        self.SetEventType(EVT_STATUS_UPDATE_ID)
        self.data = data

MAX_PRIME = 127

AL_LEFT   = 0x001
AL_RIGHT  = 0x002
AL_CENTER = 0x004
ABOVE     = 0x008
BELOW     = 0x010
MIDDLE    = 0x020
LEFT      = 0x040
RIGHT     = 0x080
CENTER    = 0x100

HOME_Z = -2
HOME_X = -1
AXIS_Z = 0
AXIS_X = 1

LathePt = namedtuple('LathePt', ['x', 'z'])

tz = timezone("America/New_York")

def intRound(val):
    return int(round(val))

def timeStr():
    now = datetime.now(tz=tz)
    return now.strftime("%a %b %d %Y %H:%M:%S\n")

def commTimeout(jogPanel):
    # wx.PostEvent(jogPanel, StatusEvent(st.STR_TIMEOUT_ERROR))
    jogPanel.setStatus(st.STR_TIMEOUT_ERROR)

def getFloatVal(tc):
    try:
        return float(tc.GetValue())
    except ValueError:
        return 0.0

def getIntVal(tc):
    try:
        return int(tc.GetValue())
    except ValueError:
        return 0

def buttonDisable(btn):
    btn.Disable()
    btn.SetBackgroundColour(None)

def buttonEnable(btn):
    # print("buttonEnable %s" % (btn.GetLabel()))
    # stdout.flush()
    btn.Enable()
    btn.SetBackgroundColour('Green')

class Factor:
    def __init__(self, maxPrime):
        self.primes = self.calcPrimes(maxPrime)

    @staticmethod
    def remFactors(nFactors, dFactors):
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
        return nFactors, dResult

    @staticmethod
    def combineFactors(factors):
        result = 1
        for val in factors:
            result *= val
        return result

    @staticmethod
    def calcPrimes(maxPrime):
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
            if sieve[i]:
                primes.append(i)
        return primes

    def factor(self, n):
        factors = []
        for i in self.primes:
            while n % i == 0:
                factors.append(i)
                n /= i
        return factors

factor = Factor(MAX_PRIME)

class Offset:
    def __init__(self, scale):
        self.scale = scale
        self.val = None

    def intVal(self):
        return self.val * self.scale

class ComboBox(wx.ComboBox):
    def __init__(self, parent, label, indexList,  choiceList, \
                 *args, **kwargs):
        self.label = label
        self.indexList = indexList
        self.choiceList = choiceList
        self.text = None
        super(ComboBox, self).__init__(parent, *args, **kwargs)

    def GetValue(self):
        val = self.GetCurrentSelection()
        rtnVal = self.indexList[val]
        # if self.text is not None:
        #     print("label \"%s\" GetValue %d text \"%s\" index %d" % \
        #           (self.label, rtnVal, self.text[val], val))
        #     print("indexList", self.indexList)
        return str(rtnVal)

    def SetValue(self, val):
        if isinstance(val, str):
            val = int(val)
        for (n, index) in enumerate(self.indexList):
            if val == index:
                self.SetSelection(n)
                # if self.text is not None:
                #     print("label \"%s\" SetValue %d text \"%s\" index %d" % \
                #           (self.label, val, self.text[index], n))
                #     print("indexList", self.indexList)

def fieldList(panel, sizer, fields, col=1):
    total = len(fields)
    offset = (total + 1) // 2
    for i in range(total):
        if col == 1:
            field = fields[i]
        else:
            j = i // 2
            if (i & 1) != 0:
                j += offset
            field = fields[j]
        (label, index) = field[:2]
        if label.startswith('b'):
            addCheckBox(panel, sizer, label[1:], index)
        elif label.startswith('c'):
            action = field[3]
            addComboBox(panel, sizer, label[1:], index, action)
        elif label.startswith('w'):
            addField(panel, sizer, label[1:], index, (80, -1))
        else:
            addField(panel, sizer, label, index)

def OnEnter(panel):
    if panel.formatList is None:
        return
    jp = panel.mf.jogPanel
    if formatData(panel.mf.cfg, panel.formatList):
        jp.setStatus(st.STR_CLR)
        jp.focus()
    else:
        jp.setStatus(st.STR_FIELD_ERROR)

def addFieldText(panel, sizer, label, key, fmt=None, keyText=None):
    if fmt is not None:
        panel.formatList.append((key, fmt))

    cfg = panel.mf.cfg
    txt = None
    if len(label) != 0:
        txt = wx.StaticText(panel, -1, label)
        sizer.Add(txt, flag=wx.ALL|wx.ALIGN_RIGHT|\
                  wx.ALIGN_CENTER_VERTICAL, border=2)
        if keyText is not None:
            cfg.initInfo(keyText, txt)

    tc = wx.TextCtrl(panel, -1, "", size=(panel.width, -1), \
                     style=wx.TE_PROCESS_ENTER)
    tc.Bind(wx.EVT_TEXT_ENTER, panel.OnEnter)
    sizer.Add(tc, flag=wx.ALL, border=2)
    cfg.initInfo(key, tc)
    return tc, txt

def addField(panel, sizer, label, index, fmt=None, size=None):
    if size is None:
        size = (panel.width, -1)
    if fmt is not None:
        panel.formatList.append((index, fmt))
    if label is not None:
        txt = wx.StaticText(panel, -1, label)
        sizer.Add(txt, flag=wx.ALL|wx.ALIGN_RIGHT|\
                  wx.ALIGN_CENTER_VERTICAL, border=2)

    tc = wx.TextCtrl(panel, -1, "", size=size, \
                     style=wx.TE_PROCESS_ENTER)
    tc.Bind(wx.EVT_TEXT_ENTER, panel.OnEnter)
    sizer.Add(tc, flag=wx.ALL, border=2)

    cfg = panel.mf.cfg
    if cfg.info[index] is not None:
        val = cfg.getInfo(index)
        tc.SetValue(val)
    cfg.initInfo(index, tc)
    return tc

def addCheckBox(panel, sizer, label, index, action=None, box=False):
    txt = wx.StaticText(panel, -1, label)
    if box:
        sizerH = wx.BoxSizer(wx.HORIZONTAL)
        sizerH.Add(txt, flag=wx.ALL|\
                   wx.ALIGN_CENTER_VERTICAL, border=2)
    else:
        sizerH = sizer
        sizerH.Add(txt, flag=wx.ALL|wx.ALIGN_RIGHT|\
                   wx.ALIGN_CENTER_VERTICAL, border=2)
    cb = wx.CheckBox(panel, -1, style=wx.ALIGN_LEFT)
    if action is not None:
        panel.Bind(wx.EVT_CHECKBOX, action, cb)
    sizerH.Add(cb, flag=wx.ALL|wx.ALIGN_CENTER_VERTICAL, border=2)

    cfg = panel.mf.cfg
    if cfg.info[index] is not None:
        val = cfg.getInfo(index)
        cb.SetValue(val == 'True')
    cfg.initInfo(index, cb)
    if box:
        sizer.Add(sizerH, flag=wx.ALIGN_RIGHT)
    return cb

def addComboBox(panel, sizer, label, index, action, border=2,
                flag=wx.CENTER|wx.ALL):
    txt = wx.StaticText(panel, -1, label)
    sizer.Add(txt, flag=wx.ALL|wx.ALIGN_RIGHT|\
              wx.ALIGN_CENTER_VERTICAL, border=2)

    (indexList, choiceList, text) = action()
    combo = ComboBox(panel, label, indexList, choiceList, \
                     id=-1, value=choiceList[0], choices=choiceList, \
                     style=wx.CB_READONLY)
    combo.text = text
    cfg = panel.mf.cfg
    if cfg.info[index] is not None:
        val = cfg.getInfo(index)
        combo.SetValue(val)
    sizer.Add(combo, flag=flag, border=border)
    cfg.initInfo(index, combo)
    return combo

class PanelButton(wx.Button):
    def __init__(self, panel, *args, **kwargs):
        wx.Button.__init__(self, *args, **kwargs)
        self.panel = panel

def addButton(panel, sizer, label, action, size=(60, -1), border=2, \
              style=0, flag=wx.CENTER|wx.ALL):
    btn = PanelButton(panel, panel, label=label, style=style, size=size)
    btn.Bind(wx.EVT_BUTTON, action)
    sizer.Add(btn, flag=flag, border=border)
    return btn

def addToggleButton(panel, sizer, label, action, size=(60, -1), border=2, \
                    style=0, flag=wx.CENTER|wx.ALL):
    btn = wx.ToggleButton(panel, label=label, style=style, size=size)
    btn.Bind(wx.EVT_TOGGLEBUTTON, action)
    sizer.Add(btn, flag=flag, border=border)
    return btn

def addControlButton(panel, sizer, label, downAction, upAction, \
                     flag=wx.CENTER|wx.ALL):
    btn = wx.Button(panel, label=label)
    btn.Bind(wx.EVT_LEFT_DOWN, downAction)
    btn.Bind(wx.EVT_LEFT_UP, upAction)
    sizer.Add(btn, flag=flag, border=2)
    return btn

def addBitmapButton(panel, sizer, bitmap, downAction, upAction, flag=0):
    bmp = wx.Bitmap(bitmap, wx.BITMAP_TYPE_ANY)
    btn = wx.BitmapButton(panel, id=wx.ID_ANY, bitmap=bmp, \
                          size=(bmp.GetWidth()+10, bmp.GetHeight()+10))
    btn.Bind(wx.EVT_LEFT_DOWN, downAction)
    btn.Bind(wx.EVT_LEFT_UP, upAction)
    sizer.Add(btn, flag=flag, border=2)
    return btn

class DialogButton(wx.Button):
    def __init__(self, dialog, *args, **kwargs):
        wx.Button.__init__(self, *args, **kwargs)
        self.dialog = dialog

def addSetupButton(dialog, sizer, label, action, size=(60, -1), border=2, \
                   style=0, flag=wx.CENTER|wx.ALL):
    btn = DialogButton(dialog, dialog, label=label, style=style, size=size)
    btn.Bind(wx.EVT_BUTTON, action)
    sizer.Add(btn, flag=flag, border=border)
    return btn

def addDialogButton(panel, sizer, idx, action=None, border=5):
    btn = DialogButton(panel, panel, idx)
    if action is None:
        btn.SetDefault()
    else:
        btn.Bind(wx.EVT_BUTTON, action)
    sizer.Add(btn, 0, wx.ALL|wx.CENTER, border=border)
    return btn

def addRadioButton(panel, sizer, label, key, style=0, action=None):
    btn = wx.RadioButton(panel, label=label, style=style)
    if action is not None:
        btn.Bind(wx.EVT_RADIOBUTTON, action)
    sizer.Add(btn, flag=wx.ALIGN_CENTER_VERTICAL|wx.ALL, border=2)
    panel.mf.cfg.initInfo(key, btn)
    return btn

EMPTY_CELL = (0, 0)

def placeHolder(sizerG, count=2):
    for _ in range(count):
        sizerG.Add(EMPTY_CELL)

def addDialogField(panel, sizer, label=None, tcDefault="", textFont=None, \
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

    txt = None
    if label is not None:
        txt = wx.StaticText(panel, -1, label)
        if textFont is not None:
            txt.SetFont(textFont)
        sizer.Add(txt, flag=wx.LEFT|wx.RIGHT|wx.ALIGN_RIGHT|\
                  wx.ALIGN_CENTER_VERTICAL, border=b0)

    tc = wx.TextCtrl(panel, -1, tcDefault, size=size, \
                     style=wx.TE_RIGHT|wx.TE_PROCESS_ENTER)
    if tcFont is not None:
        tc.SetFont(tcFont)
    if action is not None:
        tc.Bind(wx.EVT_CHAR, action)
    if not edit:
        tc.SetEditable(False)
    if index is not None:
        panel.mf.cfg.initInfo(index, tc)
    sizer.Add(tc, flag=wx.CENTER|wx.ALL, border=b1)
    return tc if not text else (tc, txt)

def formatData(cfg, formatList):
    if formatList is None:
        return True
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
                    val = fmt % val
                    if strip:
                        if re.search(r"\.0*$", val):
                            val = re.sub(r"\.0*$", "", val)
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
                    ctl.SetValue("%d" % val)
            except ValueError:
                success = False
                strVal = ''
                ctl.SetValue('')
        elif fieldType == 'c':
            pass
        cfg.setInfoData(index, strVal)
    return success

def getConfigList(panel):
    if panel.configList is None:
        panel.configList = []
        for i, name in enumerate(cf.configTable):
            if name.startswith(panel.prefix):
                panel.configList.append(i)
    return panel.configList

class FormRoutines:
    def __init__(self):
        self.configList = None
        self.prefix = ""
        self.focusField = None
        self.formatList = []
        self.width = 60 if WINDOWS else 75

class PanelVars:
    def __init__(self):
        self.zRetract = None
        self.zFeed = None
        self.zStart = None
        self.zEnd = None
        self.xRetract = None
        self.xFeed = None
        self.sizerV = None
        self.passes = None
        self.sPInt = None
        self.spring = None
        self.internal = None

def addButtons(panel, sizerG, add, rpm, pause, combine=False):
    panel.sendButton = addButton(panel, sizerG, 'Send', OnPanelSend)
    # panel.sendButton.SetBackgroundColour('Green')

    panel.startButton = addButton(panel, sizerG, 'Start', OnPanelStart)
    panel.startButton.Disable()

    if add is not None:
        panel.addButton = addButton(panel, sizerG, 'Add', OnPanelAddPass)
        panel.addButton.Disable()
        panel.addPass = addField(panel, sizerG, None, add, 'f')
    else:
        panel.addButton = None
        placeHolder(sizerG)

    panel.rpm = addField(panel, sizerG, "RPM", rpm, 'd')
    panel.rpm.Bind(wx.EVT_KILL_FOCUS, OnRPMKillFocus)

    panel.pause = addCheckBox(panel, sizerG, "Pause", pause, box=combine)

def OnPanelShow(evt):
    panel = evt.EventObject
    try:
        if panel.mf.done:
            return
    except AttributeError:
        return
    if panel.IsShown():
        jp = panel.mf.jogPanel
        jp.currentPanel = panel
        jp.currentControl = panel.control
        try:
            jp.setRPMSlider(int(panel.rpm.GetValue()))
        except ValueError:
            panel.rpm.SetValue('0')
            jp.setRPMSlider(0)
        panel.update()
    else:
        panel.active = False

def OnPanelSend(evt):
    panel = evt.EventObject.panel
    jp = panel.mf.jogPanel
    if formatData(panel.mf.cfg, panel.formatList):
        if not jp.xHomed:
            jp.setStatus(st.STR_NOT_HOMED)
        elif panel.active or \
             jp.mvStatus & (ct.MV_ACTIVE | ct.MV_PAUSE):
            jp.setStatus(st.STR_OP_IN_PROGRESS)
        else:
            jp.setStatus(st.STR_CLR)
            try:
                if callable(panel.sendAction):
                    if panel.sendAction():
                        panel.active = True
                        panel.sendButton.Disable()
                        buttonEnable(panel.startButton)
                        buttonDisable(jp.spindleButton)
            except CommTimeout:
                commTimeout(jp)
            # except:
            #     traceback.print_exc()
    else:
        jp.setStatus(st.STR_FIELD_ERROR)
    jp.focus()

def OnPanelStart(evt):
    panel = evt.EventObject.panel
    jp = panel.mf.jogPanel
    if not panel.active:
        jp.setStatus(st.STR_NOT_SENT)
    elif (jp.mvStatus & ct.MV_PAUSE) == 0:
        jp.setStatus(st.STR_NOT_PAUSED)
    else:
        jp.setStatus(st.STR_CLR)
        try:
            if callable(panel.startAction):
                panel.startAction()
                buttonDisable(panel.startButton)
        except CommTimeout:
            commTimeout(jp)
        except AttributeError:
            print("ActionRoutines OnStart AttributeError")
            stdout.flush()
    jp.focus()

def OnPanelAddPass(evt):
    panel = evt.EventObject.panel
    jp = panel.mf.jogPanel
    if not panel.active:
        jp.setStatus(st.STR_OP_NOT_ACTIVE)
    elif jp.mvStatus & (ct.MV_ACTIVE | ct.MV_PAUSE):
        jp.setStatus(st.STR_OP_IN_PROGRESS)
    else:
        jp.setStatus(st.STR_CLR)
        jp.clrRetract()
        try:
            # curPass = panel.mf.comm.getParm(pm.CURRENT_PASS)
            curPass = jp.lastPass
            if curPass >= panel.control.passes:
                if callable(panel.addAction):
                    panel.addAction()
            else:
                jp.setStatus(st.STR_PASS_ERROR)
        except CommTimeout:
            commTimeout(jp)
        except AttributeError:
            print("ActionRoutines OnAddPass AttributeError")
            stdout.flush()
    jp.focus()

def OnRPMKillFocus(evt):
    panel = evt.EventObject.Parent
    panel.mf.jogPanel.setRPMSlider(int(panel.rpm.GetValue()))
    evt.Skip()

def getSafeLoc(panel):
    control = panel.control
    control.getParameters()
    panel.safeX = control.xStart + control.xRetract
    panel.safeZ = control.zStart + control.zRetract
    return panel.safeZ, panel.safeX

class ActionRoutines():
    def __init__(self, control, op):
        self.control = control
        self.op = op
        self.rpm = None
        self.addPass = None
        self.sendButton = None
        self.startButton = None
        self.pause = None
        self.active = False
        self.safeX = None
        self.safeZ = None
        self.formatList = []
        self.manualMode = False

    # def formatData(self, formatList):
    #     print("ActionRoutines formatData stub called")
    #     stdout.flush()
    #     return True

    def sendAction(self):
        print("ActionRoutines sendAction stub called")
        stdout.flush()
        return False

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

    # def getSafeLoc(self):
    #     control = self.control
    #     control.getParameters()
    #     self.safeX = control.xStart + control.xRetract
    #     self.safeZ = control.zStart + control.zRetract
    #     return self.safeZ, self.safeX

    # def OnSend(self, evt):
    #     panel = evt.EventObject.panel
    #     jp = panel.mf.jogPanel
    #     if formatData(panel.mf.cfg, panel.formatList):
    #         if not jp.xHomed:
    #             jp.setStatus(st.STR_NOT_HOMED)
    #         elif panel.active or \
    #              jp.mvStatus & (ct.MV_ACTIVE | ct.MV_PAUSE):
    #             jp.setStatus(st.STR_OP_IN_PROGRESS)
    #         else:
    #             jp.setStatus(st.STR_CLR)
    #             try:
    #                 if callable(panel.sendAction):
    #                     if panel.sendAction():
    #                         panel.active = True
    #                         panel.sendButton.Disable()
    #                         buttonEnable(panel.startButton)
    #                         buttonDisable(jp.spindleButton)
    #             except CommTimeout:
    #                 commTimeout(jp)
    #             except:
    #                 traceback.print_exc()
    #     else:
    #         jp.setStatus(st.STR_FIELD_ERROR)
    #     jp.focus()

    # def OnStart(self, _):
    #     jp = self.armf.jogPanel
    #     if not self.active:
    #         jp.setStatus(st.STR_NOT_SENT)
    #     elif (jp.mvStatus & ct.MV_PAUSE) == 0:
    #         jp.setStatus(st.STR_NOT_PAUSED)
    #     else:
    #         jp.setStatus(st.STR_CLR)
    #         try:
    #             if callable(self.startAction):
    #                 self.startAction()
    #                 buttonDisable(self.startButton)
    #         except CommTimeout:
    #             commTimeout(jp)
    #         except AttributeError:
    #             print("ActionRoutines OnStart AttributeError")
    #             stdout.flush()
    #     jp.focus()

    # def OnAddPass(self, _):
    #     jp = self.armf.jogPanel
    #     if not self.active:
    #         jp.setStatus(st.STR_OP_NOT_ACTIVE)
    #     elif jp.mvStatus & (ct.MV_ACTIVE | ct.MV_PAUSE):
    #         jp.setStatus(st.STR_OP_IN_PROGRESS)
    #     else:
    #         jp.setStatus(st.STR_CLR)
    #         jp.clrRetract()
    #         try:
    #             curPass = self.armf.comm.getParm(pm.CURRENT_PASS)
    #             if curPass >= self.control.passes:
    #                 if callable(self.addAction):
    #                     self.addAction()
    #             else:
    #                 jp.setStatus(st.STR_PASS_ERROR)
    #         except CommTimeout:
    #             commTimeout(jp)
    #         except AttributeError:
    #             print("ActionRoutines OnAddPass AttributeError")
    #             stdout.flush()
    #     jp.focus()

    # def OnRPMKillFocus(self, e):
    #     self.armf.jogPanel.setRPMSlider(int(self.rpm.GetValue()))
    #     e.Skip()

def saveData(dialog):
    changed = False
    cfg = dialog.mf.cfg
    for fmt in dialog.fields:
        (label, index) = fmt[:2]
        val = cfg.getInfo(index)
        if dialog.fieldInfo[index] != val:
            dialog.fieldInfo[index] = val
            cfg.setInfoData(index, val)
            dialog.sendData = True
            changed = True
    return changed

def OnDialogShow(evt):
    dialog = evt.EventObject
    try:
        if dialog.mf.done:
            return
    except AttributeError:
        return

    changed = False
    if dialog.IsShown():
        formatData(dialog.mf.cfg, dialog.fields)
        dialog.fieldInfo = {}
        for fmt in dialog.fields:
            (label, index) = fmt[:2]
            dialog.fieldInfo[index] = dialog.mf.cfg.getInfo(index)
    else:
        changed = saveData(dialog)

    if hasattr(dialog, 'showAction') and \
       callable(dialog.showAction):
        dialog.showAction(changed)

def OnDialogOk(evt):
    dialog = evt.EventObject.dialog
    if formatData(dialog.mf.cfg, dialog.fields):
        dialog.Show(False)
        if hasattr(dialog, 'okAction') and \
           callable(dialog.okAction):
            dialog.okAction()

def OnDialogCancel(evt):
    dialog = evt.EventObject.dialog
    for field in dialog.fields:
        index = field[1]
        dialog.mf.cfg.setInfo(index, dialog.fieldInfo[index])
    dialog.Show(False)

def OnDialogSetup(evt):
    dialog = evt.EventObject.dialog
    if not formatData(dialog.mf.cfg, dialog.fields):
        return
    dialog.mf.move.queClear()
    if hasattr(dialog, 'setupAction') and \
       callable(dialog.setupAction):
        dialog.setupAction()

class DialogActions():
    def __init__(self):
        self.fields = None
        self.fieldInfo = None
        self.sendData = False
        self.changed = False

    def setupAction(self):
        print("DialogAction setupAction stub called")
        stdout.flush()

    def showAction(self, changed):
        print("DialogAction showAction stub called")
        stdout.flush()

class MoveCommands():
    def __init__(self, mainFrame):
        self.jp = mainFrame.jogPanel
        self.cfg = mainFrame.cfg
        self.comm = mainFrame.comm
        if not R_PI:
            self.moveQue = Queue()
        else:
            self.moveQue = self.comm.moveQue
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
        d.add_layer('0', color=0, lineweight=0)
        d.add_layer(TEXT, color=0, lineweight=0)
        d.add_layer(REF, color=1, lineweight=0)
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
            flip = self.flip
            self.d.add(dxf.line((p0X, flip * p0Y), \
                                (p1X, flip * p1Y), layer=layer))

    def drawLineX(self, x, layer=0):
        if self.d is not None:
            flip = self.flip
            self.d.add(dxf.line((self.lastZ, flip * self.lastX), \
                                (self.lastZ, flip * x), layer=layer))
            self.lastX = x

    def drawLineZ(self, z, layer=0):
        if self.d is not None:
            flip = self.flip
            self.d.add(dxf.line((self.lastZ, flip * self.lastX), \
                                (z, flip * self.lastX), layer=layer))
            self.lastZ = z

    def drawLine(self, z, x, layer=0):
        if self.d is not None:
            flip = self.flip
            self.d.add(dxf.line((self.lastZ, flip * self.lastX), \
                                (z, flip * x), layer=layer))
            self.lastX = x
            self.lastZ = z

    def drawCenter(self, center, layer=0):
        if self.d is not None:
            l = 0.005
            (yc, xc) = center
            yc *= self.flip
            self.d.add(dxf.line((xc, yc + l), (xc, yc - l), layer=layer))
            self.d.add(dxf.line((xc + l, yc), (xc - l, yc), layer=layer))

    def drawArc(self, center, p0, p1, layer=0):
        if self.d is not None:
            (yc, xc) = center
            (x0, y0) = p0
            (x1, y1) = p1
            self.lastX = x1
            self.lastY = y1
            flip = self.flip
            yc *= flip
            y0 *= flip
            y1 *= flip
            dx = x0 - xc
            dy = y0 - yc
            a0 = degrees(atan2(dy, dx))
            if a0 < 0:
                a0 += 360
            a1 = degrees(atan2(y1 - yc, x1 - xc))
            if a1 < 0:
                a1 += 360
            if a1 < a0:
                a1 += 360
            # print("drawArc a0 %7.3f a1 %7.3f" % (a0, a1))
            radius = hypot(dy, dx)
            if a0 > a1:
                (a0, a1) = (a1, a0)
            self.d.add(dxf.arc(radius, (xc, yc), a0, a1, layer=layer))

    def drawDXFArc(self, center, radius, a0, a1, layer=0):
        if self.d is not None:
            (yc, xc) = center
            yc *= self.flip
            self.d.add(dxf.arc(radius, (xc, yc), a0, a1, layer=layer))

    def drawL(self, l, layer=0):
        if l.type == LINE:
            self.setLoc(l.p0.x, l.p0.y)
            self.drawLine(l.p1.x, l.p1.y, layer=layer)
        elif l.type == ARC:
            (yc, xc) = l.c
            self.drawArc((xc, yc), l.p0, l.p1, layer=layer)

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

    def text(self, text, p0, align=None, layer='TEXT', textAngle=None):
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

            if textAngle is None:
                textAngle = self.textAngle
            if textAngle != 0.0:
                (vOffset, hOffset) = (hOffset, -vOffset)
            self.d.add(dxf.text(text, \
                                (x + hOffset, self.flip * y + vOffset), \
                                height=self.textH, rotation=textAngle, \
                                layer=layer, style=self.style, thickness=0.0))

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
        self.comm.sendMulti()   # send parameters first
        self.zOffset = None
        self.xOffset = None

    def queMove(self, op, val=0):
        if self.send:
            opString = en.mCommandsList[op]
            print("moveQue put op %6x %-18s %s" % (op, opString, str(val)))
            self.moveQue.put((opString, op, val))

    def queMoveF(self, op, flag, val):
        if self.send:
            opString = en.mCommandsList[op]
            op |= (flag << 16)
            print("moveQue put op %6x %-18s %-1s" % (op, opString, str(val)))
            self.moveQue.put((opString, op, val))

    def queClear(self):
        self.send = not self.cfg.getBoolInfoData(cf.cfgCmdDis)
        while not self.moveQue.empty():
            self.moveQue.get()
        self.queInit()

    def queZSetup(self, feed):
        self.queMove(en.Q_Z_FEED_SETUP, feed)
        self.saveZOffset()
        self.saveXOffset()

    def queXSetup(self, feed):
        self.queMove(en.Q_X_FEED_SETUP, feed)
        self.saveZOffset()
        self.saveXOffset()

    def startSpindle(self, rpm):
        self.queMove(en.Q_START_SPINDLE, rpm)
        self.saveZOffset()
        self.saveXOffset()

    def stopSpindle(self):
        self.queMove(en.Q_STOP_SPINDLE)

    def queFeedType(self, feedType):
        self.queMove(en.Q_SAVE_FEED_TYPE, feedType)

    def zSynSetup(self, feed):
        self.queMove(en.Q_Z_SYN_SETUP, feed)

    def xSynSetup(self, feed):
        self.queMove(en.Q_X_SYN_SETUP, feed)

    def syncParms(self):
        self.queMove(en.Q_SEND_SYNC_PARMS)

    def syncCommand(self, cmd):
        self.queMove(en.Q_SYNC_COMMAND, cmd)

    def nextPass(self, passNum):
        self.passNum = passNum
        self.queMove(en.Q_PASS_NUM, passNum)
        if self.dbg:
            if passNum & 0x100:
                print("spring\n")
            elif passNum & 0x200:
                print("spring %d" % (passNum & 0xff))
            else:
                print("pass %d" % (passNum))

    def quePause(self, val=0):
        self.queMove(en.Q_QUE_PAUSE, val)

    # def moveZOffset(self):
    #     self.queMove(en.Q_MOVE_Z_OFFSET)

    def moveZ(self, zLocation, flag=ct.CMD_MAX, backlash=0.0):
        if (flag & ct.DRO_POS) == 0:
            val = round((zLocation + backlash) * self.jp.zStepsInch)
        else:
            val = round((zLocation + backlash) * self.jp.zDROInch)
        self.queMoveF(en.Q_MOVE_Z, flag, val)
        self.drawLineZ(zLocation)
        if self.dbg:
            print("moveZ   %7.4f" % (zLocation))
            stdout.flush()

    def moveX(self, xLocation, flag=ct.CMD_MAX, backlash=0.0):
        if (flag & ct.DRO_POS) == 0:
            val = round((xLocation + backlash) * self.jp.xStepsInch)
        else:
            val = round((xLocation + backlash) * self.jp.xDROInch)
        self.queMoveF(en.Q_MOVE_X, flag, val)
        self.drawLineX(xLocation)
        if self.dbg:
            print("moveX   %7.4f" % (xLocation))
            stdout.flush()

    def saveZOffset(self):
        jp = self.jp
        if self.zOffset != jp.zHomeOffset:
            self.zOffset = jp.zHomeOffset
            # zHomeOffset floating, zHomeOffset sent as integer
            self.queMove(en.Q_SAVE_Z_OFFSET,
                         round(jp.zHomeOffset * jp.zStepsInch))
            if self.dbg:
                print("saveZOffset %7.4f" % (jp.zHomeOffset))
                stdout.flush()

    def saveXOffset(self):
        jp = self.jp
        if self.xOffset != jp.xHomeOffset:
            self.xOffset = jp.xHomeOffset
            # xHomeOffset floating, xHomeOffset sent as integer
            self.queMove(en.Q_SAVE_X_OFFSET,
                         round(jp.xHomeOffset * jp.xStepsInch))
            if self.dbg:
                print("saveXOffset  %7.4f" % (jp.xHomeOffset))
                stdout.flush()

    # def moveXZ(self, zLocation, xLocation):
    #     self.queMove(en.Q_SAVE_Z, zLocation)
    #     self.queMove(en.Q_MOVE_X_Z, xLocation)
    #     if self.dbg:
    #         print("moveZX %7.4f %7.4f" % (zLocation, xLocation))
    #
    # def moveZX(self, zLocation, xLocation):
    #     self.queMove(en.Q_SAVE_X, xLocation)
    #     self.queMove(en.Q_MOVE_Z_X, zLocation)
    #     if self.dbg:
    #         print("moveXZ %7.4f %7.4f" % (zLocation, xLocation))

    def saveTaper(self, taper):
        if not R_PI:
            taper = "%0.6f" % (taper)
        self.queMove(en.Q_SAVE_TAPER, taper)
        if self.dbg:
            print("saveTaper %s" % (taper))

    def saveThreadFlags(self, flags):
        self.queMove(en.Q_SAVE_FLAGS, flags)
        if self.dbg:
            print("saveThreadFlags %02x" % (flags))

    def taperZX(self, zLocation, xLocation):
        self.queMove(en.Q_SAVE_X, xLocation)
        self.queMoveF(en.Q_TAPER_Z_X, 1, zLocation)
        if self.dbg:
            print("taperZX %7.4f" % (zLocation))

    def taperXZ(self, xLocation, zLocation):
        self.queMove(en.Q_SAVE_Z, zLocation)
        self.queMoveF(en.Q_TAPER_X_Z, 1, xLocation)
        if self.dbg:
            print("taperXZ %7.4f" % (xLocation))

    def probeZ(self, zDist):
        self.queMove(en.Q_PROBE_Z, zDist)
        if self.dbg:
            print("probeZ %7.4f" % (zDist))

    def probeX(self, xDist):
        self.queMove(en.Q_PROBE_X, xDist)
        if self.dbg:
            print("probeX %7.4f" % (xDist))

    def saveZDro(self):
        self.queMove(en.Q_SAVE_Z_DRO)

    def saveXDro(self):
        self.queMove(en.Q_SAVE_X_DRO)

    def queParm(self, parm, val):
        op = en.Q_QUE_PARM
        opString = en.mCommandsList[op]
        op |= parm << 16
        print("moveQue put op %6x %-18s %s" % (op, opString, str(val)))
        self.moveQue.put((opString, op, val))

    def moveArc(self):
        self.queMove(en.Q_MOVE_ARC)

    def done(self, parm):
        self.queMove(en.Q_OP_DONE, parm)
        if parm == ct.PARM_START:
            self.saveZOffset()
            self.saveXOffset()

class SendData:
    def __init__(self, mainFrame):
        self.mf = mainFrame
        self.jp = mainFrame.jogPanel
        self.cfg = mainFrame.cfg
        self.comm = mainFrame.comm
        self.spindleDataSent = False
        self.zDataSent = False
        self.xDataSent = False
        self.megaDataSent = False

    def sendClear(self):
        try:
            self.comm.command(cm.C_CLRDBG)
            self.comm.command(cm.C_CMD_CLEAR)
        except CommTimeout:
            commTimeout(self.jp)
        self.spindleDataSent = False
        self.zDataSent = False
        self.xDataSent = False

    def xilinxTestMode(self):
        cfg = self.cfg
        comm = self.comm
        #testMode = False
        try:
            testMode = cfg.getBoolInfoData(cf.cfgTestMode)
        except KeyError:
            testMode = False
        if testMode:
            try:
                encoder = cfg.getIntInfoData(cf.cfgEncoder)
            except KeyError:
                encoder = 0
            try:
                rpm = int(cfg.getFloatInfoData(cf.cfgTestRPM))
            except KeyError:
                rpm = 0
            if encoder != 0:
                preScaler = 1
                if rpm == 0:
                    rpm = 1
                rps = rpm / 60.0
                fcy = cfg.getIntInfoData(cf.cfgFpgaFreq)
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

    def sendSpindleData(self, send=False, rpm=None):
        cfg = self.cfg
        comm = self.comm
        queParm = self.comm.queParm
        try:
            if send or (not self.spindleDataSent):
                queParm(pm.STEPPER_DRIVE, cfg.getBoolInfoData(cf.spStepDrive))
                queParm(pm.MOTOR_TEST, cfg.getBoolInfoData(cf.spMotorTest))
                queParm(pm.SPINDLE_ENCODER, \
                        cfg.getBoolInfoData(cf.cfgSpEncoder))
                queParm(pm.SPINDLE_SYNC_BOARD, \
                        cfg.getBoolInfoData(cf.cfgSpSyncBoard))
                queParm(pm.SPINDLE_INTERNAL_SYNC, \
                        cfg.getBoolInfoData(cf.cfgIntSync))
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
                    self.mf.updateThread.encoderCount = count
                    if MOTOR_TEST and SPINDLE_ENCODER:
                        queParm(pm.SP_TEST_ENCODER, \
                                cfg.getBoolInfoData(cf.spTestEncoder))
                elif FPGA:
                    queParm(pm.ENC_PER_REV, cfg.getInfoData(cf.cfgEncoder))
                    queParm(pm.FPGA_FREQUENCY, cfg.getInfoData(cf.cfgFpgaFreq))
                    # queParm(pm.FREQ_MULT, cfg.getInfoData(cf.cfgFreqMult))
                    queParm(pm.FREQ_MULT, 8)
                    self.xilinxTestMode()
                    queParm(pm.RPM, cfg.getInfoData(cf.cfgTestRPM))
                    print(R_PI)
                    if not R_PI:
                        cfgReg = 0
                        if bool(cfg.getBoolInfoData(cf.cfgInvEncDir)):
                            cfgReg |= xb.ENC_POL
                        if bool(cfg.getBoolInfoData(cf.zInvDir)):
                            cfgReg |= xb.ZDIR_POL
                        if bool(cfg.getBoolInfoData(cf.xInvDir)):
                            cfgReg |= xb.XDIR_POL
                        queParm(pm.X_CFG_REG, cfgReg)
                    else:
                        pass
                    comm.sendMulti()
                elif SPINDLE_ENCODER:
                    mf = self.mf
                    count = cfg.getIntInfoData(cf.cfgEncoder)
                    if mf.zSyncExt is not None:
                        mf.zSyncExt.setEncoder(count)
                    if mf.xSyncExt is not None:
                        mf.xSyncExt.setEncoder(count)
                    if mf.zSyncInt is not None:
                        mf.zSyncInt.setEncoder(count)
                    if mf.xSyncInt is not None:
                        mf.xSyncInt.setEncoder(count)
                    queParm(pm.ENC_PER_REV, count)
                    mf.updateThread.encoderCount = count

                if SPINDLE_VAR_SPEED:
                    queParm(pm.PWM_FREQ, cfg.getIntInfoData(cf.spPWMFreq))
                    curRange = cfg.getIntInfoData(cf.spCurRange)
                    if 1 <= curRange <= cfg.getIntInfoData(cf.spRanges):
                        curRange -= 1
                        queParm(pm.MIN_SPEED, \
                                cfg.getIntInfoData(cf.spRangeMin1 + curRange))
                        queParm(pm.MAX_SPEED, \
                                cfg.getIntInfoData(cf.spRangeMax1 + curRange))
                    else:
                        queParm(pm.MIN_SPEED, 0)
                        queParm(pm.MAX_SPEED, 0)
                        
                if STEP_DRV or MOTOR_TEST or SPINDLE_VAR_SPEED:
                    if rpm is not None:
                        queParm(pm.SP_MAX_RPM, rpm)
                    else:
                        queParm(pm.SP_MAX_RPM, cfg.getInfoData(cf.spMaxRPM))

                comm.command(cm.C_CMD_SPSETUP)
                self.spindleDataSent = True
        except CommTimeout:
            commTimeout(self.jp)

    def sendZData(self, send=False):
        cfg = self.cfg
        comm = self.comm
        queParm = self.comm.queParm
        try:
            # pitch = cfg.getDistInfoData(cf.zPitch)
            motorSteps = cfg.getIntInfoData(cf.zMotorSteps)
            microSteps = cfg.getIntInfoData(cf.zMicroSteps)
            # motorRatio = cfg.getFloatInfoData(cf.zMotorRatio)
            # self.jp.zStepsInch = stepsInch = (microSteps * motorSteps * \
            #                                   motorRatio) / pitch
            self.jp.zStepsInch = stepsInch = self.mf.zStepsInch

            zSyncInt = self.mf.zSyncInt
            if zSyncInt is not None:
                zSyncInt.setLeadscrew(cfg.getInfoData(cf.zPitch))
                zSyncInt.setMotorSteps(motorSteps)
                zSyncInt.setMicroSteps(microSteps)
                if not FPGA:
                    zSyncInt.setClockFreq(cfg.getIntInfoData(cf.cfgFcy))
                else:
                    zSyncInt.setClockFreq(cfg.getIntInfoData(cf.cfgFpgaFreq))

            zSyncExt = self.mf.zSyncExt
            if zSyncExt is not None:
                zSyncExt.setLeadscrew(cfg.getInfoData(cf.zPitch))
                zSyncExt.setMotorSteps(motorSteps)
                zSyncExt.setMicroSteps(microSteps)

            # droInch = 0
            # if DRO:
                # self.jp.zDROInch = droInch = cfg.getIntInfoData(cf.zDROInch)

            # print("zStepsInch %0.2f" % (self.jp.zStepsInch))
            # stdout.flush()

            if send or (not self.zDataSent):
                if DRO:
                    droInch = self.mf.zDROInch
                    queParm(pm.Z_DRO_COUNT_INCH, droInch)
                    queParm(pm.Z_DRO_INVERT, cfg.getBoolInfoData(cf.zInvDRO))
                    queParm(pm.Z_USE_DRO, cfg.getBoolInfoData(cf.zDROPos))
                    queParm(pm.Z_DONE_DELAY, cfg.getIntInfoData(cf.zDoneDelay))
                    queParm(pm.Z_DRO_FINAL_DIST,
                            round(cfg.getFloatInfoData(cf.zDroFinalDist) * \
                                  droInch))
                    stepF = factor.factor(stepsInch)
                    droF = factor.factor(droInch)
                    (stepF, droF) = factor.remFactors(stepF, droF)
                    stepFactor = factor.combineFactors(stepF)
                    droFactor = factor.combineFactors(droF)
                    queParm(pm.Z_STEP_FACTOR, stepFactor)
                    queParm(pm.Z_DRO_FACTOR, droFactor)
                else:
                    queParm(pm.Z_DONE_DELAY, 0)

                val = self.jp.combo.GetValue()
                try:
                    val = float(val)

                    if val > 0.020:
                        val = 0.020
                except ValueError:
                    # val = cfg.getFloatInfoData(cf.zMpgInc)
                    val = 0
                if FPGA:
                    queParm(pm.FREQ_MULT, 8)

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

                queParm(pm.Z_HOME_DIST, cfg.getInfoData(cf.zHomeDist))
                queParm(pm.Z_HOME_DIST_REV, cfg.getInfoData(cf.zHomeDistRev))
                queParm(pm.Z_HOME_DIST_BACKOFF, \
                        cfg.getInfoData(cf.zHomeDistBackoff))
                queParm(pm.Z_HOME_SPEED, cfg.getInfoData(cf.zHomeSpeed))
                queParm(pm.Z_HOME_DIR, \
                        1 if bool(cfg.getBoolInfoData(cf.zHomeDir)) else -1)

                comm.command(cm.C_CMD_ZSETUP)

                self.zDataSent = True
        except CommTimeout:
            commTimeout(self.jp)
        # except:
        #     print("setZData exception")
        #     stdout.flush()
        #     traceback.print_exc()

    def sendXData(self, send=False):
        cfg = self.cfg
        comm = self.comm
        queParm = comm.queParm
        try:
            # pitch = cfg.getDistInfoData(cf.xPitch)
            motorSteps = cfg.getIntInfoData(cf.xMotorSteps)
            microSteps = cfg.getIntInfoData(cf.xMicroSteps)
            # motorRatio = cfg.getFloatInfoData(cf.xMotorRatio)
            # if motorRatio == 0:
            #     motorRatio = 1
            # self.jp.xStepsInch = stepsInch = (microSteps * motorSteps * \
            #                                   motorRatio) / pitch
            self.jp.xStepsInch = stepsInch = self.mf.xStepsInch

            xSyncInt = self.mf.xSyncInt
            if xSyncInt is not None:
                xSyncInt.setLeadscrew(cfg.getInfoData(cf.xPitch))
                xSyncInt.setMotorSteps(motorSteps)
                xSyncInt.setMicroSteps(microSteps)
                if not FPGA:
                    xSyncInt.setClockFreq(cfg.getIntInfoData(cf.cfgFcy))
                else:
                    xSyncInt.setClockFreq(cfg.getIntInfoData(cf.cfgFpgaFreq))

            xSyncExt = self.mf.xSyncExt
            if xSyncExt is not None:
                xSyncExt.setLeadscrew(cfg.getInfoData(cf.xPitch))
                xSyncExt.setMotorSteps(motorSteps)
                xSyncExt.setMicroSteps(microSteps)

            # droInch = 0
            # if DRO:
            #     self.jp.xDROInch = droInch = cfg.getIntInfoData(cf.xDROInch)

            # print("xStepsInch %0.2f" % (self.jp.xStepsInch))
            # stdout.flush()

            if send or (not self.xDataSent):
                if DRO:
                    droInch = self.mf.xDROInch
                    queParm(pm.X_DRO_COUNT_INCH, droInch)
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

                val = self.jp.combo.GetValue()
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

                comm.queParm(pm.X_HOME_DIST, cfg.getInfoData(cf.xHomeDist))
                comm.queParm(pm.X_HOME_DIST_REV, \
                             cfg.getInfoData(cf.xHomeDistRev))
                comm.queParm(pm.X_HOME_DIST_BACKOFF, \
                             cfg.getInfoData(cf.xHomeDistBackoff))
                comm.queParm(pm.X_HOME_SPEED, cfg.getInfoData(cf.xHomeSpeed))
                comm.queParm(pm.X_HOME_DIR,
                             1 if bool(cfg.getBoolInfoData(cf.xHomeDir)) else -1)

                if HOME_TEST:
                    stepsInch = self.jp.xStepsInch
                    start = str(int(cfg.getFloatInfoData(cf.xHomeStart) * \
                                    stepsInch))
                    end = str(int(cfg.getFloatInfoData(cf.xHomeEnd) * \
                                  stepsInch))
                    if end > start:
                        (start, end) = (end, start)
                    queParm(pm.X_HOME_START, start)
                    queParm(pm.X_HOME_END, end)

                comm.command(cm.C_CMD_XSETUP)
                self.xDataSent = True
        except CommTimeout:
            commTimeout(self.jp)

    def sendMegaData(self, send=False):
        if send or (not self.megaDataSent):
            self.megaDataSent = True
            cfg = self.cfg
            setMega = self.comm.setMegaParm
            try:
                setMega(mp.M_PARM_PWM_CFG, cfg.getIntInfoData(cf.cfgMegaVFD))
                setMega(mp.M_PARM_ENC_TEST, cfg.getBoolInfoData(cf.cfgMegaEncTest))
                setMega(mp.M_PARM_ENC_LINES, cfg.getIntInfoData(cf.cfgMegaEncLines))
            except CommTimeout:
                pass

class LatheOp():
    def __init__(self, mainFrame, panel):
        self.panel = panel
        self.m = mainFrame.move
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
    def __init__(self, mainFrame):
        self.upmf = mainFrame
        self.calcPassN = None    # calculate values for a pass
        self.runPassN = None     # run a pass with current values

        self.addEnabled = False
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
        self.lastPass = None

    def calcFeed(self, feed, cutAmount, finish=0.0):
        self.addEnabled = False
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
        self.passSize = [0.0 for _ in range(self.passes + 1)]
        self.passCount = 0
        self.sPassCtr = 0
        self.spring = 0
        self.feed = 0.0
        self.springFlag = False
        self.lastPass = False

    def updatePass(self):
        if (self.passCount < self.passes) or self.springFlag:
            if self.springFlag:
                self.springFlag = False
                self.upmf.move.nextPass(0x100 | self.passCount)
                self.runpassN()
            else:
                self.passCount += 1
                self.upmf.move.nextPass(self.passCount)
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
                            return True
        else:
            if self.spring < self.sPasses:
                self.spring += 1
                self.upmf.move.nextPass(0x200 | self.spring)
                self.lastPass = self.spring == self.sPasses
                # print("spring %d lastPass %s" % \
                #       (self.spring, self.lastPass))
                self.runpassN()
            else:
                return False
        # print("updatePass %d %s" % (self.passCount, self.springFlag))
        return True

    def passDone(self):
        m = self.upmf.move
        m.drawClose()
        if STEP_DRV or MOTOR_TEST or SPINDLE_SWITCH:
            m.stopSpindle()
        m.done(ct.PARM_DONE)
        stdout.flush()

    def addInit(self, label, panel):
        self.upmf.dPrt("\n%s addPass\n" % (label))
        self.upmf.dPrt(timeStr() + "\n")
        self.pause = panel.pause.GetValue()
        self.addEnabled = True
        add = getFloatVal(panel.addPass)
        if add != 0.0:
            panel.addPass.SetValue("0.0000")
        else:
            self.pause = True
        return add

    def addDone(self):
        m = self.upmf.move
        if STEP_DRV or MOTOR_TEST or SPINDLE_SWITCH:
            m.stopSpindle()
        m.done(ct.PARM_DONE)
        self.upmf.comm.command(cm.C_CMD_RESUME)

    def fixCut(self, offset=0.0):
        pass

def getSyncParm(control, feed, rpm, axis):
    val = getFloatVal(feed)
    rpm = getIntVal(rpm)
    mf = control.mf
    turnSync = mf.turnSync
    if turnSync == en.SEL_TU_ISYN or turnSync == en.SEL_TU_SYN:
        syn = mf.zSyncInt if axis == AXIS_Z else mf.xSyncInt
        (control.cycle, control.output,
         control.inPreScaler, control.outPreScaler) = \
            syn.calcSync(val, metric=False, rpm=rpm, turn=True)
    elif turnSync == en.SEL_TU_ESYN:
        syn = mf.zSyncExt if axis == AXIS_Z else mf.xSyncExt
        (control.cycle, control.output,
         control.inPreScaler, control.outPreScaler) = \
            syn.calcSync(val, metric=False, rpm=rpm, turn=True)

def sendSyncParm(control):
    mf = control.mf
    turnSync = mf.turnSync
    queParm = mf.comm.queParm
    if turnSync == en.SEL_TU_ISYN or \
       turnSync == en.SEL_TU_SYN or \
       ((turnSync == en.SEL_TU_ESYN) and SYNC_SPI):
        queParm(pm.L_SYNC_CYCLE, control.cycle)
        queParm(pm.L_SYNC_OUTPUT, control.output)
        queParm(pm.L_SYNC_IN_PRESCALER, control.inPreScaler)
        queParm(pm.L_SYNC_OUT_PRESCALER, control.outPreScaler)
        if SYNC_SPI:
            m = control.m
            m.syncParms()
            m.syncCommand(sc.SYNC_SETUP)
    elif turnSync == en.SEL_TU_ESYN:
        syncComm = mf.syncComm
        syncComm.setParm(sp.SYNC_ENCODER, \
                         control.cfg.getIntInfoData(cf.cfgEncoder))
        syncComm.setParm(sp.SYNC_CYCLE, control.cycle)
        syncComm.setParm(sp.SYNC_OUTPUT, control.output)
        syncComm.setParm(sp.SYNC_PRESCALER, control.outPreScaler)
        syncComm.command(sc.SYNC_SETUP)

class Turn(LatheOp, UpdatePass):
    def __init__(self, mainFrame, turnPanel):
        LatheOp.__init__(self, mainFrame, turnPanel)
        UpdatePass.__init__(self, mainFrame)
        self.mf = mainFrame
        self.cfg = mainFrame.cfg
        self.xCut = 0.0
        self.curX = 0.0
        self.internal = False
        self.neg = False

    def getParameters(self):
        tu = self.panel
        self.manual = tu.manual.GetValue()
        self.internal = tu.internal.GetValue()

        if not self.manual:
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

        getSyncParm(self, tu.zFeed, tu.rpm, AXIS_Z)

    def runOperation(self):
        self.getParameters()

        if self.xStart < 0:
            if self.xEnd <= 0:
                self.neg = True
            else:
                self.mf.jogPanel.setStatus(st.STR_SIGN_ERROR)
                return False
        else:
            if self.xEnd >= 0:
                self.neg = False
            else:
                self.mf.jogPanel.setStatus(st.STR_SIGN_ERROR)
                return False

        self.xCut = abs(self.xStart) - abs(self.xEnd)
        if self.internal:
            if self.xCut > 0:
                self.mf.jogPanel.setStatus(st.STR_INTERNAL_ERROR)
                return False
        else:
            if self.xCut < 0:
                self.mf.jogPanel.setStatus(st.STR_EXTERNAL_ERROR)
                return False
        self.xCut = abs(self.xCut)

        self.calcFeed(self.xFeed, self.xCut)
        self.mf.comm.setParm(pm.TOTAL_PASSES, self.passes)
        self.pause = self.panel.pause.GetValue()
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

        if self.mf.cfgDraw:
            self.m.draw("turn", self.zStart, self.zEnd)

        self.mf.dPrt("\nturn runOperation\n")
        self.mf.dPrt(timeStr() + "\n")
        self.setup()

        while self.updatePass():
            pass

        self.m.moveX(self.safeX)

        self.passDone()
        return(True)

    def setup(self, add=False): # turn
        comm = self.mf.comm
        comm.queParm(pm.CURRENT_OP, en.OP_TURN)
        m = self.m
        if not add:
            m.setLoc(self.zEnd, self.xStart)
            m.drawLineZ(self.zStart, REF)
            m.drawLineX(self.xEnd, REF)
            m.setLoc(self.safeZ, self.safeX)

            sendSyncParm(self)

        m.queInit()
        if (not add) or (add and not self.pause):
            m.quePause()
        m.done(ct.PARM_START)

        comm.command(cm.C_CMD_SYNCSETUP)

        m.startSpindle(self.cfg.getIntInfoData(cf.tuRPM))

        m.queFeedType(ct.FEED_PITCH)
        m.zSynSetup(self.cfg.getFloatInfoData(cf.tuZFeed))

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
        self.mf.dPrt("pass %2d feed %5.3f x %5.3f "\
                     "diameter %5.3f %s\n" % \
                     (self.passCount, feed, self.curX, \
                      self.curX * 2.0, ("", "final")[final]), \
                     True, True)

    def runPass(self, addPass=False): # turn
        m = self.m
        flag = (ct.CMD_JOG | ct.DRO_POS | ct.DRO_UPD) if X_DRO_POS else \
            ct.CMD_MOV
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
        add = self.addInit("turn", self.panel) / 2.0
        self.cutAmount += add
        self.setup(True)
        self.calcPass(True)
        self.m.nextPass(self.passCount)
        self.runPass(True)
        self.m.moveX(self.xStart + self.xRetract)
        self.addDone()

    def fixCut(self, offset=0.0): # turn
        passNum = self.mf.jogPanel.lastPass
        if offset == 0.0:
            actual = float(self.mf.jogPanel.xPos.GetValue())
            self.passSize[passNum] = 2 * actual
            if self.internal:
                self.cutAmount = actual - self.xStart
            else:
                self.cutAmount = self.xStart - actual
        else:
            self.passSize[passNum] += offset

    def manualOperation(self):
        self.getParameters()

        jp = self.mf.jogPanel
        startSpindle = not jp.spindleButton.GetValue()

        comm = self.mf.comm
        xLocation = (float(comm.getParm(pm.X_LOC)) / jp.xStepsInch - \
                     jp.xHomeOffset)

        if self.internal:
            self.xRetract = -self.xRetract

        self.safeX = xLocation + self.xRetract
        self.safeZ = self.zStart + self.zRetract

        self.passSize = [0.0, 2 * xLocation]
        self.passNum = 1

        self.mf.dPrt("\nturn manualOperation\n")
        self.mf.dPrt(timeStr() + "\n")

        comm.queParm(pm.CURRENT_OP, en.OP_TURN)

        self.mf.setupSync()
        m = self.mf.move
        m.queInit()
        m.done(ct.PARM_START)

        comm.command(cm.C_CMD_SYNCSETUP)

        if startSpindle:
            m.startSpindle(self.cfg.getIntInfoData(cf.tuRPM))

        m.queFeedType(ct.FEED_PITCH)
        m.zSynSetup(self.cfg.getFloatInfoData(cf.tuZFeed))

        self.passCount = 1
        m.nextPass(self.passCount)

        m.moveZ(self.zStart)
        m.moveZ(self.zEnd, ct.CMD_SYN)

        m.moveX(self.safeX)
        m.moveZ(self.safeZ)

        flag = (ct.CMD_JOG | ct.DRO_POS | ct.DRO_UPD) if X_DRO_POS else \
            ct.CMD_MOV
        m.moveX(xLocation, flag)

        if startSpindle:
            if STEP_DRV or MOTOR_TEST or SPINDLE_SWITCH:
                m.stopSpindle()
        m.done(ct.PARM_DONE)
        stdout.flush()

class TurnPanel(wx.Panel, PanelVars, FormRoutines, ActionRoutines):
    def __init__(self, mainFrame, hdrFont, *args, **kwargs):
        PanelVars.__init__(self)
        FormRoutines.__init__(self)
        super(TurnPanel, self).__init__(mainFrame, *args, **kwargs)
        ActionRoutines.__init__(self, Turn(mainFrame, self), en.OP_TURN)
        self.Bind(wx.EVT_SHOW, OnPanelShow)
        self.mf = mainFrame
        self.fields0 = []
        self.hdrFont = hdrFont
        self.InitUI()
        self.prefix = 'tu'
        # self.formatList = ((cf.tuAddFeed, 'f'), \
        #                    (cf.tuInternal, None), \
        #                    (cf.tuPasses, 'd'), \
        #                    (cf.tuPause, None), \
        #                    (cf.tuRPM, 'd'), \
        #                    (cf.tuSPInt, 'd'), \
        #                    (cf.tuSpring, 'd'), \
        #                    (cf.tuXDiam0, 'f'), \
        #                    (cf.tuXDiam1, 'f'), \
        #                    (cf.tuXFeed, 'f'), \
        #                    (cf.tuXRetract, 'f'), \
        #                    (cf.tuZEnd, 'f'), \
        #                    (cf.tuZFeed, 'f'), \
        #                    (cf.tuZRetract, 'f'), \
        #                    (cf.tuZStart, 'f'))

    def InitUI(self):
        fields0 = self.fields0
        self.sizerV = sizerV = wx.BoxSizer(wx.VERTICAL)

        txt = wx.StaticText(self, -1, "Turn", size=(120, 30))
        txt.SetFont(self.hdrFont)

        sizerV.Add(txt, flag=wx.CENTER|wx.ALL, border=2)

        sizerG = wx.FlexGridSizer(cols=8, rows=0, vgap=0, hgap=0)

        # x parameters

        (self.xDiam0, self.diam0Txt) = \
            addFieldText(self, sizerG, "X Start D", cf.tuXDiam0, 'f')
        self.focusField = self.xDiam0
        fields0.append(self.xDiam0)

        (self.xDiam1, self.diam1Txt) = \
            addFieldText(self, sizerG, "X End D", cf.tuXDiam1, 'f')
        fields0.append(self.xDiam1)

        self.xFeed = addField(self, sizerG, "X Feed D", cf.tuXFeed, 'f')
        fields0.append(self.xFeed)

        self.xRetract = addField(self, sizerG, "X Retract", cf.tuXRetract, 'f')

        # z parameters

        self.zEnd = addField(self, sizerG, "Z End", cf.tuZEnd, 'f')

        self.zStart = addField(self, sizerG, "Z Start", cf.tuZStart, 'f')

        self.zFeed = addField(self, sizerG, "Z Feed", cf.tuZFeed, 'f')

        self.zRetract = addField(self, sizerG, "Z Retract", cf.tuZRetract, 'f')

        # pass info

        self.passes = addField(self, sizerG, "Passes", cf.tuPasses, 'd')
        self.passes.SetEditable(False)

        self.sPInt = addField(self, sizerG, "SP Int", cf.tuSPInt, 'd')
        fields0.append(self.sPInt)

        self.spring = addField(self, sizerG, "Spring", cf.tuSpring, 'd')
        fields0.append(self.spring)

        self.manual = addCheckBox(self, sizerG, "Manual", cf.tuManual, \
                                  self.OnManual)

        # buttons

        addButtons(self, sizerG, cf.tuAddFeed, cf.tuRPM, cf.tuPause, True)
        fields0.append(self.sendButton)
        fields0.append(self.addPass)
        fields0.append(self.pause)

        self.internal = addCheckBox(self, sizerG, "Internal", cf.tuInternal, \
                                    self.OnInternal, box=True)

        sizerV.Add(sizerG, flag=wx.CENTER|wx.ALL, border=2)

        self.SetSizer(sizerV)
        sizerV.Fit(self)

    def OnEnter(self, _):
        OnEnter(self)

    def OnManual(self, _):
        self.updateUI()

    def OnInternal(self, _):
        self.updateUI()

    def updateUI(self):
        if not self.active:
            if self.internal.GetValue():
                self.diam0Txt.SetLabel("X End D")
                self.diam1Txt.SetLabel("X Start D")
            else:
                self.diam0Txt.SetLabel("X Start D")
                self.diam1Txt.SetLabel("X End D")
            btn = self.startButton
            self.manualMode = self.manual.GetValue()
            if self.manualMode:
                for f0 in self.fields0:
                    f0.Disable()
                btn.Enable()
                btn.Bind(wx.EVT_BUTTON, self.OnManualStart)
            else:
                for f0 in self.fields0:
                    f0.Enable()
                    btn.Disable()
                btn.Bind(wx.EVT_BUTTON, OnPanelStart)
            self.sizerV.Layout()

    def update(self):
        self.updateUI()
        formatData(self.mf.cfg, self.formatList)
        self.mf.jogPanel.setPassText("Diam")

    def sendData(self):
        try:
            self.mf.move.queClear()
            sd = self.mf.sendData
            sd.sendClear()
            sd.sendSpindleData()
            sd.sendZData()
            sd.sendXData()
        except CommTimeout:
            commTimeout(self.mf.jogPanel)

    def sendAction(self):
        self.sendData()
        return(self.control.runOperation())

    def startAction(self):
        self.mf.comm.command(cm.C_CMD_RESUME)
        control = self.control
        if control.addEnabled:
            if self.mf.jogPanel.mvStatus & ct.MV_READ_X:
                control.fixCut()
        else:
            if self.mf.dbgSave:
                self.mf.updateThread.openDebug(action=en.OP_TURN)

    def OnManualStart(self, _):
        self.sendData()
        if self.mf.dbgSave:
            self.mf.updateThread.openDebug(action=en.OP_TURN)
        self.control.manualOperation()

    def addAction(self):
        self.control.addPass()

    def nextOperation(self):
        if not self.active:
            self.mf.jogPanel.setStatus(st.STR_OP_NOT_ACTIVE)
            return

        if self.internal.GetValue():
            dCur = self.xDiam1
            dNxt = self.xDiam0
        else:
            dCur = self.xDiam0
            dNxt = self.xDiam1
        dCur.SetValue(self.mf.jogPanel.passSize.GetValue())
        dNxt.SetFocus()
        dNxt.SetSelection(-1, -1)
        self.active = False
        self.mf.jogPanel.setStatus(st.STR_CLR)

class Arc(LatheOp, UpdatePass):
    def __init__(self, mainFrame, arcPanel):
        LatheOp.__init__(self, mainFrame, arcPanel)
        UpdatePass.__init__(self, mainFrame)
        self.mf = mainFrame
        self.dPrt = mainFrame.dPrt
        self.cut = 0.0
        self.curX = 0.0
        self.neg = False
        self.internal = False
        self.arcRadius = None
        self.materialRadius = None
        self.retract = None
        self.startZ = None
        self.toolRadius = None
        self.largeRadius = None
        self.largeStem = None
        self.smallRadius = None
        self.smallStem = None
        self.endDist = None
        self.toolAngle = None
        self.finishAllowance = None
        self.arcCW = None
        self.arcType = None
        self.ball = None
        self.cutRadius = None
        self.center = None
        self.radiusStart = None
        self.toolRadiusStart = None
        self.toolArcRadius = None
        self.moveInitial = None
        self.movePreCut = None
        self.moveCut = None
        self.movePostCut = None
        self.toolEnd = None
        self.ballStem = None

    def getParameters(self, draw=False):
        panel = self.panel

        self.arcRadius = getFloatVal(panel.arcRadius)
        self.materialRadius = getFloatVal(panel.diameter) / 2
        self.feed = abs(getFloatVal(panel.feed) / 2.0)
        self.retract = abs(getFloatVal(panel.retract))

        self.startZ = getFloatVal(panel.zStart)

        self.toolRadius = getFloatVal(panel.toolRadius) # ***

        self.largeRadius = getFloatVal(panel.largeEnd) / 2
        self.largeStem = getFloatVal(panel.largeStem) / 2
        self.smallStem = getFloatVal(panel.smallStem) / 2
        self.smallRadius = getFloatVal(panel.smallEnd) / 2
        self.endDist = getFloatVal(panel.endDist)

        self.toolAngle = getFloatVal(panel.toolAngle)
        self.xFeed = abs(getFloatVal(panel.xFeed) / 2.0)
        self.finishAllowance = getFloatVal(panel.finishAllowance)

        self.arcCW = not panel.arcCCW.GetValue()
        self.arcType = panel.arcType.GetSelection()

        self.ball = False
        arcType = self.arcType
        if arcType == en.SEL_ARC_END:
            self.cutRadius = self.materialRadius
            self.center = LathePt(0, self.startZ - self.arcRadius)
            self.setupActions()
        elif arcType == en.SEL_ARC_CORNER:
            self.cutRadius = self.arcRadius
            self.center = LathePt(self.materialRadius - self.arcRadius, \
                                  self.startZ - self.arcRadius)
            self.setupActions()
        elif arcType == en.SEL_ARC_SMALL:
            self.cutRadius = self.materialRadius
            self.center = LathePt(0, self.startZ - self.smallRadius)
            self.setupActions()
            self.ball = True
            self.stem(self.smallRadius, self.smallStem, \
                      self.largeStem, self.largeRadius, stem=False, draw=draw)
        elif arcType == en.SEL_ARC_LARGE:
            self.cutRadius = self.materialRadius
            self.arcRadius = self.largeRadius
            self.center = LathePt(0, self.startZ - self.largeRadius)
            self.setupActions()
            self.ball = True
            self.stem(self.largeRadius, self.largeStem, \
                      self.smallStem, self.smallRadius, stem=False, draw=draw)
        elif arcType == en.SEL_ARC_SMALL_STEM:
            self.cutRadius = self.materialRadius
            self.center = LathePt(0, self.startZ - self.smallRadius)
            self.stem(self.smallRadius, self.smallStem, \
                      self.largeStem, self.largeRadius)
        elif arcType == en.SEL_ARC_LARGE_STEM:
            self.cutRadius = self.materialRadius
            self.arcRadius = self.largeRadius
            self.center = LathePt(0, self.startZ - self.largeRadius)
            self.stem(self.largeRadius, self.largeStem, \
                      self.smallStem, self.smallRadius)

        self.radiusStart = \
            hypot(self.materialRadius - self.center.x, self.arcRadius)

        self.toolRadiusStart = self.radiusStart + self.toolRadius # ***
        self.toolArcRadius = self.arcRadius + self.toolRadius     # ***
        self.cut = self.toolRadiusStart - self.toolArcRadius

        print("toolRadiusStart %5.3f toolArcRadius %5.3f cut %5.3f" % \
              (self.toolRadiusStart, self.toolArcRadius, self.cut))
        stdout.flush()

        getSyncParm(self, panel.zFeed, panel.rpm, AXIS_Z)

    def setupActions(self):
        if self.arcCW:
            self.moveInitial = self.moveInitCW
            self.movePreCut = self.movePreCW
            self.moveCut = self.moveCutCW
            self.movePostCut = self.movePostCW
        else:
            self.moveInitial = self.moveInitCCW
            self.movePreCut = self.movePreCCW
            self.moveCut = self.moveCutCCW
            self.movePostCut = self.movePostCCW

    def stem(self, rad0, stem0, stem1, rad1, stem=True, draw=False):
        m = self.m
        x0 = stem0
        z0 = self.center.z - sqrt(rad0 * rad0 - x0 * x0)
        x1 = stem1
        z1 = self.center.z - self.endDist + sqrt(rad1 * rad1 - x1 * x1)

        if stem:
            rad0F = rad0 + self.finishAllowance
            # rad1F = rad1 + self.finishAllowance
            self.moveInitial = self.moveInitStem
            self.movePreCut = self.movePreStem
            self.moveCut = self.moveCutStem
            self.movePostCut = self.movePostStem
        else:
            rad0F = rad0
            # rad1F = rad1

        if draw:
            m.drawArc(self.center, (z0, x0), (self.center.z, 0))
            m.setLoc(z0, x0)
            m.drawLine(z1, x1)
            m.drawArc((self.center.x, self.center.z - self.endDist), \
                      (self.center.z - self.endDist - rad1, 0), (z1, x1))

        toolAngle = radians(self.toolAngle / 2)
        tanToolAngle = tan(toolAngle)
        self.taper = tanToolAngle
        offset = tanToolAngle * (self.materialRadius - rad0F)
        matIntersect = self.center.z + offset
        axisIntersect = self.center.z + offset + (self.materialRadius / \
                                                  tanToolAngle)

        if draw:
            m.setLoc(self.center.z, rad0)
            m.drawLine(matIntersect, self.materialRadius)

        trim1 = Line((self.center.z, self.arcRadius),
                     (matIntersect, self.materialRadius))
        if draw:
            m.drawL(trim1)

        trim2 = GeoArc((self.center.z, self.center.x), rad0F, 180, 270)
        if draw:
            m.drawL(trim2)

        trim3 = Line((z1, x1 + self.finishAllowance), \
                     (z0, x0 + self.finishAllowance))

        if draw:
            m.drawL(trim3)

        toolCentArc = GeoArc((self.center.z, self.center.x), \
                             rad0F + self.toolRadius, 180, 270) # ***
        toolCentLine = trim3.parallel(self.toolRadius, CW)      # ***
        toolCentLine.intersect(toolCentArc, end=1, trim=False)
        toolEndCenter = toolCentLine.p1
        self.toolEnd = LathePt(toolEndCenter.y, \
                               toolEndCenter.x) # x <- y, z <- x

        # if draw:
        #     toolCentArc.prt()
        #     toolCentLine.prt()
        #     toolEnd = GeoArc(p, self.toolRadius, 0, 360)
        #     toolEnd.prt()
        #     m.drawL(toolCentArc)
        #     m.drawL(toolCentLine)
        #     m.drawL(toolEnd)

        if not stem:
            return

        pMat = (matIntersect, self.materialRadius)
        pAxis = (axisIntersect, 0)

        lStart = Line(pMat, pAxis)
        zFeedOffset = self.xFeed / sin(toolAngle)
        # print("zFeedOffset %7.4f" % (zFeedOffset))
        trimType = 0
        dbg = False
        self.ballStem = []
        wDone = False
        i = 1
        while not wDone:
            passFeed = i * zFeedOffset
            l = Line((matIntersect - passFeed, self.materialRadius), \
                     (axisIntersect - passFeed, 0))
            if dbg:
                print("%2d " % (i), end="")
                l.prt()
            if trimType == 0:
                p = l.intersect(trim1, False, dbg=dbg)
                if p[1] < rad0F:
                    trimType = 1

            if trimType == 1:
                p = l.intersect(trim2, end=0, trim=False, dbg=dbg)
                if p[1] < x0:
                    trimType = 2

            if trimType == 2:
                p = l.intersect(trim3, False)
                distance = l.pointDistance(toolEndCenter)
                if distance is not None and distance > self.toolRadius: # ***
                    wDone = True

            if draw:
                m.drawL(l)
            self.ballStem.append((l.p0, l.p1))
            i += 1

        m.drawClose()

    # noinspection PyMethodMayBeStatic
    def moveNone(self, val=None):
        if val is not None:
            print("moveNone called with", val)

    def runOperation(self):
        # if self.mf.cfgDraw:
        #     self.m.draw("arc", self.startZ, self.zEnd)

        self.getParameters(draw=False)

        mf = self.mf
        mf.comm.queParm(pm.ARC_X_CENTER, \
                     intRound(self.center.x * mf.jogPanel.xStepsInch))

        mf.comm.queParm(pm.ARC_Z_CENTER, \
                     intRound(self.center.z * mf.jogPanel.zStepsInch))
        mf.comm.sendMulti()

        arcType = self.arcType
        if (arcType == en.SEL_ARC_SMALL_STEM or \
            arcType == en.SEL_ARC_LARGE_STEM):
            self.passes = len(self.ballStem)
            self.initPass()
            toolRadius = 0.0    # ***
            self.arc = False
        else:
            self.calcFeed(self.feed, self.cut)
            toolRadius = self.toolRadius # ***
            self.arc = True

        self.mf.comm.setParm(pm.TOTAL_PASSES, self.passes)
        self.pause = self.panel.pause.GetValue()

        print("cut %5.3f passes %d" % (self.cut, self.passes))
        stdout.flush()

        self.setupSpringPasses(self.panel)
        self.setupAction(self.calcPass, self.runPass)

        self.panel.passes.SetValue("%d" % (self.passes))

        self.safeX = self.materialRadius + toolRadius + self.retract # ***
        self.safeZ = self.startZ + toolRadius + self.zRetract # ***

        if self.mf.cfgDraw:
            self.m.draw("arc", self.zStart, self.zEnd)

        if self.arc and True:
            m = self.m
            m.drawArc(self.center, \
                      (self.center.z, self.center.x + self.arcRadius), \
                      (self.center.z + self.arcRadius, self.center.x))

            m.drawArc(self.center, \
                      (self.center.z, self.center.x + self.toolArcRadius), \
                      (self.center.z + self.toolArcRadius, self.center.x))

            m.drawArc(self.center, \
                      (self.center.z, self.center.x + self.toolRadiusStart), \
                      (self.center.z + self.toolRadiusStart, self.center.x))

            m.drawArc((self.center.x, \
                       self.center.z + self.arcRadius + toolRadius), \
                      (self.center.z + self.arcRadius + 2*toolRadius, \
                       self.center.x),\
                      (self.center.z + self.arcRadius + 2*toolRadius, \
                       self.center.x))

            m.drawArc((self.center.x + self.arcRadius + toolRadius, \
                       self.center.z), \
                      (self.center.z + toolRadius, \
                       self.center.x + self.arcRadius + toolRadius),
                      (self.center.z + toolRadius, \
                       self.center.x + self.arcRadius + toolRadius))

            m.setLoc(self.center.z, self.materialRadius)
            m.drawLine(self.startZ, self.materialRadius)
            m.drawLine(self.startZ, self.center.x)

            m.setLoc(self.center.z, self.materialRadius + toolRadius)
            m.drawLine(self.startZ + toolRadius, \
                       self.materialRadius + toolRadius)
            m.drawLine(self.startZ + toolRadius, self.center.x)

            tick = 0.010
            m.setLoc(self.center.z-tick, self.center.x)
            m.drawLine(self.center.z+tick, self.center.x)

            m.setLoc(self.center.z , self.center.x-tick)
            m.drawLine(self.center.z, self.center.x+tick)

        self.dPrt("\narc runOperation %s %s\n" % \
                  (("CCW", "CW")[self.arcCW], en.selArcTypeText[self.arcType]))
        self.dPrt(timeStr() + "\n")
        self.setup()

        while self.updatePass():
            pass

        self.m.moveX(self.safeX)
        self.passDone()
        return(True)

    def setup(self, add=False): # arc
        comm = self.mf.comm
        comm.queParm(pm.CURRENT_OP, en.OP_ARC)
        m = self.m
        if not add:
            m.setLoc(self.zEnd, self.xStart)
            m.drawLineZ(self.zStart, REF)
            m.drawLineX(self.xEnd, REF)
            m.setLoc(self.safeZ, self.safeX)

            sendSyncParm(self)

        m.queInit()
        if (not add) or (add and not self.pause):
            m.quePause()
        m.done(ct.PARM_START)

        comm.command(cm.C_CMD_SYNCSETUP)

        cfg = self.mf.cfg
        if not self.arc:
            comm.setParm(pm.TAPER_CYCLE_DIST, \
                         cfg.getInfoData(cf.cfgTaperCycleDist))
            m.saveTaper(self.taper)

        m.startSpindle(cfg.getIntInfoData(cf.tuRPM))

        m.queFeedType(ct.FEED_PITCH)
        m.zSynSetup(cfg.getFloatInfoData(cf.arcZFeed))
        if not self.arcCW:
            m.xSynSetup(cfg.getFloatInfoData(cf.arcZFeed))

        self.movePostCut()

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
        if self.arc:
            feed = self.cutAmount if final else \
                self.passCount * self.actualFeed
            self.feed = feed
            self.curRadius = self.radiusStart - feed
            self.calcArcEndPass(final)
        else:
            feed = self.xFeed
            self.curRadius = self.ballStem[self.passCount-1][1][1]
            self.calcStemPass(final)

        (xc, zc) = self.center
        x0Delta = self.xStart - xc
        z0Delta = self.zStart - zc
        x1Delta = self.xEnd - xc
        z1Delta = self.zEnd - zc
        rad0 = hypot(x0Delta, z0Delta)
        rad1 = hypot(x1Delta, z1Delta)

        self.dPrt("pass %2d feed %5.3f s (x %5.3f z %6.3f) " \
                  "e (x %5.3f z %6.3f) r %5.3f %5.3f %5.3f %s\n" % \
                  (self.passCount, feed, self.xStart, self.zStart, \
                   self.xEnd, self.zEnd, self.curRadius, rad0, rad1,\
                   ("", "final")[final]), True, True)

    def calcArcEndPass(self, final):
        toolRadius = self.toolRadius
        c = self.curRadius + toolRadius # ***
        a = self.toolArcRadius          # ***

        print("curToolRadius %7.4f toolArcRadius %7.4f" % (c, a))
        stdout.flush()
        x0 = sqrt(c * c - a * a) + self.center.x
        z0 = self.startZ + toolRadius # ***
        self.passSize[self.passCount] = x0 * 2

        if self.curRadius < self.cutRadius:
            self.xLabel = True
            if self.ball and final:
                (x1, z1) = self.toolEnd
            else:
                x1 = self.center.x + self.curRadius + toolRadius # ***
                z1 = self.center.z
        else:
            self.xLabel = False
            x1 = self.materialRadius - self.center.x + toolRadius # ***
            z1 = sqrt(c * c - x1 * x1) + self.center.z
            x1 += self.center.x

        self.passSize[self.passCount] = (x1 - toolRadius) * 2.0 # ***

        if self.arcCW:
            self.xStart = x0
            self.zStart = z0
            self.xEnd = x1
            self.zEnd = z1
        else:
            self.xStart = x1
            self.zStart = z1
            self.xEnd = x0
            self.zEnd = z0

        self.curX = self.xStart

    def calcStemPass(self, final):
        self.xLabel = False
        ((self.zStart, self.xStart), (self.zEnd, self.xEnd)) = \
            self.ballStem[self.passCount - 1]
        # print("taper %7.4f" % \
        #       ((self.xStart - self.xEnd) / (self.zStart - self.zEnd)))
        self.passSize[self.passCount] = self.xEnd * 2

    def runPass(self, addPass=False): # arc
        m = self.m
        if addPass:
            m.passNum |= 0x8000

        flag = (ct.CMD_JOG | ct.DRO_POS | ct.DRO_UPD) if X_DRO_POS else \
            ct.CMD_MOV

        self.moveInitial(flag)

        if DRO:
            m.saveXDro()
        if self.pause:
            flag = (ct.PAUSE_ENA_X_JOG | ct.PAUSE_READ_X) if addPass else 0
            m.quePause(flag)

        self.movePreCut()

        if DRO:
            m.saveXDro()
            m.saveZDro()

        self.moveCut()

        if DRO:
            m.saveZDro()
            m.saveXDro()

        self.movePostCut()

        m.passNum &= ~0x8000

    def passMove(self):
        m = self.m
        jp = self.mf.jogPanel
        m.queParm(pm.ARC_RADIUS, self.curRadius + self.toolRadius)
        m.queParm(pm.ARC_X_START, intRound(self.xStart * jp.xStepsInch))
        m.queParm(pm.ARC_Z_START, intRound(self.zStart * jp.zStepsInch))
        m.queParm(pm.ARC_X_END, intRound(self.xEnd * jp.xStepsInch))
        m.queParm(pm.ARC_Z_END, intRound(self.zEnd * jp.zStepsInch))
        m.moveArc()

    # clockwise arc, corner, and ball

    def moveInitCW(self, flag):
        m = self.m
        m.moveX(self.curX, flag)
        if (m.passNum & 0xff00) == 0:
            m.text("%2d %7.3f" % (m.passNum, self.xStart * 2), \
                   (self.safeZ, self.curX))

    def movePreCW(self):
        self.m.moveZ(self.zStart)

    def moveCutCW(self):
        self.passMove()
        m = self.m
        if (m.passNum & 0xff00) == 0:
            if self.xLabel:
                m.text("%2d %7.3f" % (m.passNum, self.xEnd), \
                       (self.zEnd, self.xEnd), RIGHT)
                # if self.zEnd == self.center.z:
                #     self.endLabel = False
            else:
                m.text("%2d %7.3f" % (m.passNum, self.zEnd), \
                       (self.zEnd, self.safeX), RIGHT, textAngle=90)

            m.drawArc(self.center, (self.zEnd, self.xEnd), \
                      (self.zStart, self.xStart))

            if m.passNum == 1:
                m.drawCenter(self.center)

    def movePostCW(self):
        self.m.moveX(self.safeX)
        self.m.moveZ(self.safeZ)

    # counterclockwise arc, corner, and ball

    def moveInitCCW(self, flag):
        m = self.m
        m.moveZ(self.zStart)
        # self.dPrt("moveInitCCW moveZ zStart   %7.4f\n" % (self.zStart))
        if (m.passNum & 0xff00) == 0:
            if self.xLabel:
                m.text("%2d %7.3f" % (m.passNum, self.xStart * 2), \
                       (self.zStart, self.xStart), RIGHT)
            else:
                m.text("%2d %7.3f" % (m.passNum, self.zStart), \
                       (self.zStart, self.safeX), RIGHT, textAngle=90)

    def movePreCCW(self):
        m = self.m
        m.moveX(self.xStart + self.retract)
        m.moveX(self.xStart) #, ct.CMD_SYN)
        # self.dPrt("moveInitCCW moveX xRetract %7.4f\n" % (self.xStart))
        # self.dPrt("moveInitCCW moveX xStart   %7.4f\n" % (self.xStart))

    def moveCutCCW(self):
        m = self.m
        self.passMove()
        # self.dPrt("moveCutCCW  moveX zEnd     %7.4f xEnd %7.4f\n" % \
        #               (self.zEnd, self.xEnd))
        if (m.passNum & 0xff00) == 0:
            m.text("%2d %7.3f" % (m.passNum, self.xEnd), \
                   (self.safeZ+.060, self.xEnd), RIGHT)
            m.drawArc(self.center, (self.zStart, self.xStart), \
                      (self.zEnd, self.xEnd))
            if m.passNum == 1:
                m.drawCenter(self.center)

    def movePostCCW(self):
        m = self.m
        m.moveZ(self.safeZ)
        m.moveX(self.safeX)
        # self.dPrt("movePostCCW moveZ safeZ    %7.4f\n" % (self.safeZ))
        # self.dPrt("movePostCCW moveX safeX    %7.4f\n" % (self.safeX))

    # stem

    def moveInitStem(self, final):
        m = self.m
        m.moveZ(self.zStart)
        if (m.passNum & 0xff00) == 0:
            m.text("%2d %7.3f" % (m.passNum, self.xStart * 2), \
                   (self.safeZ, self.curX))

    def movePreStem(self):
        self.m.moveX(self.xStart)

    def moveCutStem(self):
        self.m.taperZX(self.zEnd, self.xEnd)

    def movePostStem(self):
        self.m.moveX(self.safeX)

    # def addPass(self):
    #     add = self.addInit("turn") / 2.0
    #     self.cutAmount += add
    #     self.setup(True)
    #     self.calcPass(True)
    #     moveCommands.nextPass(self.passCount)
    #     self.runPass(True)
    #     self.m.moveX(self.xStart + self.xRetract)
    #     self.addDone()

    def fixCut(self, offset=0.0): # arc
        jp = self.mf.jogPanel
        passNum = jp.lastPass
        if offset == 0.0:
            actual = float(jp.xPos.GetValue())
            self.passSize[passNum] = 2 * actual
            if self.internal:
                self.cutAmount = actual - self.xStart
            else:
                self.cutAmount = self.xStart - actual
        else:
            self.passSize[passNum] += offset

class ArcPanel(wx.Panel, FormRoutines, ActionRoutines):
    def __init__(self, mainFrame, hdrFont, *args, **kwargs):
        super(ArcPanel, self).__init__(mainFrame, *args, **kwargs)
        FormRoutines.__init__(self)
        ActionRoutines.__init__(self, Arc(mainFrame, self), en.OP_ARC)
        self.Bind(wx.EVT_SHOW, OnPanelShow)
        self.mf = mainFrame
        self.hdrFont = hdrFont
        self.InitUI()
        self.prefix = 'arc'

    def InitUI(self):
        fields0 = self.fields0 = []
        self.sizerV = sizerV = wx.BoxSizer(wx.VERTICAL)

        txt = wx.StaticText(self, -1, "Arc", size=(120, 30))
        txt.SetFont(self.hdrFont)

        sizerV.Add(txt, flag=wx.CENTER|wx.ALL, border=2)

        sizerG = wx.FlexGridSizer(cols=8, rows=0, vgap=0, hgap=0)

        # line 1 radius parameters

        self.arcRadius = addField(self, sizerG, "Radius", cf.arcRadius, 'f')

        self.diameter = addField(self, sizerG, "Diam", cf.arcDiam, 'f')

        self.feed = addField(self, sizerG, "Radius Feed", cf.arcFeed, 'f')

        self.zFeed = addField(self, sizerG, "Z Feed", cf.arcZFeed, 'f')


        # line 2 diameter and angle

        self.zStart = addField(self, sizerG, "Z Start", cf.arcZStart, 'f')

        self.retract = addField(self, sizerG, "Retract", cf.arcRetract, 'f')

        self.toolRadius = addField(self, sizerG, "Tool Radius", \
                                   cf.arcToolRad, 'f')

        self.arcType = addComboBox(self, sizerG, "Arc Type", cf.arcType, \
                                   self.arcTypeSetup)
        self.arcType.Bind(wx.EVT_COMBOBOX, self.OnArcType)


        # line 3 z parameters

        self.ballList = []
        self.largeEnd = f0 = addField(self, sizerG, "Large End", \
                                      cf.arcLargeEnd, 'f')
        self.ballList.append(f0)

        self.largeStem = f0 = addField(self, sizerG, "Large Stem", \
                                       cf.arcLargeStem, 'f')
        self.ballList.append(f0)

        self.smallStem = f0 = addField(self, sizerG, "Small Stem", \
                                       cf.arcSmallStem, 'f')
        self.ballList.append(f0)

        self.smallEnd = f0 = addField(self, sizerG, "Small End", \
                                      cf.arcSmallEnd, 'f')
        self.ballList.append(f0)

        # line 4

        self.toolAngle = f0 = addField(self, sizerG, "Tool Angle", \
                                       cf.arcToolAngle, 'f0')
        self.ballList.append(f0)

        self.xFeed = f0 = addField(self, sizerG, "x Feed", cf.arcXFeed, 'f')
        self.ballList.append(f0)

        self.finishAllowance = f0 = addField(self, sizerG, "Finish", \
                                             cf.arcFinish, 'f')
        self.ballList.append(f0)

        self.endDist = f0 =addField(self, sizerG, "Ball Dist", \
                                    cf.arcBallDist, 'f')
        self.ballList.append(f0)

        # line 5 pass info

        self.passes = addField(self, sizerG, "Passes", cf.arcPasses, 'd')
        self.passes.SetEditable(False)

        self.sPInt = addField(self, sizerG, "SP Int", cf.arcSPInt, 'd')
        fields0.append(self.sPInt)

        self.spring = addField(self, sizerG, "Spring", cf.arcSpring, 'd')
        fields0.append(self.spring)

        placeHolder(sizerG)

        # line 6 buttons

        addButtons(self, sizerG, cf.arcAddFeed, cf.arcRPM, cf.arcPause, True)
        fields0.append(self.sendButton)
        fields0.append(self.addPass)
        fields0.append(self.pause)

        self.arcCCW = addCheckBox(self, sizerG, "Dir CCW", cf.arcCCW, box=True)

        # self.internal = addCheckBox(self, sizerG, "Internal", cf.arcInternal, \
        #                                  self.OnInternal, box=True)

        sizerV.Add(sizerG, flag=wx.CENTER|wx.ALL, border=2)

        self.SetSizer(sizerV)
        sizerV.Fit(self)

    def OnEnter(self, _):
        OnEnter(self)

    # noinspection PyMethodMayBeStatic
    def arcTypeSetup(self):
        indexList = (en.SEL_ARC_END, en.SEL_ARC_CORNER, \
                     en.SEL_ARC_SMALL, en.SEL_ARC_LARGE, \
                     en.SEL_ARC_SMALL_STEM, en.SEL_ARC_LARGE_STEM)
        choiceList = []
        for i in indexList:
            choiceList.append(en.selArcTypeText[i])
        return (indexList, choiceList, en.selArcTypeText)

    # def OnInternal(self, _):
    #     self.updateUI()

    def updateUI(self):
        if not self.active:
            arcType = self.arcType.GetSelection()
            if (arcType == en.SEL_ARC_END or \
                arcType == en.SEL_ARC_CORNER):
                self.arcRadius.Enable()
                for f0 in self.ballList:
                    f0.Disable()
            else:
                self.arcRadius.Disable()
                for f0 in self.ballList:
                    f0.Enable()
            self.sizerV.Layout()

    def update(self):
        self.updateUI()
        formatData(self.mf.cfg, self.formatList)
        self.mf.jogPanel.setPassText("Radius")

    def sendData(self):
        try:
            self.mf.move.queClear()
            sd = self.mf.sendData
            sd.sendClear()
            sd.sendSpindleData()
            sd.sendZData()
            sd.sendXData()
        except CommTimeout:
            commTimeout(self.mf.jogPanel)

    def sendAction(self):
        self.sendData()
        return(self.control.runOperation())

    def startAction(self):
        self.mf.comm.command(cm.C_CMD_RESUME)
        control = self.control
        if control.addEnabled:
            if self.mf.jogPanel.mvStatus & ct.MV_READ_X:
                control.fixCut()
        else:
            if self.mf.dbgSave:
                self.mf.updateThread.openDebug(action=en.OP_ARC)

    def addAction(self):
        self.control.addPass()

    def nextOperation(self):
        if not self.active:
            self.mf.jogPanel.setStatus(st.STR_OP_NOT_ACTIVE)
            return

    def OnArcType(self, _):
        self.updateUI()

class Face(LatheOp, UpdatePass):
    def __init__(self, mainFrame, facePanel):
        LatheOp.__init__(self, mainFrame, facePanel)
        UpdatePass.__init__(self, mainFrame)
        self.mf = mainFrame
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

        getSyncParm(self, fa.xFeed, fa.rpm, AXIS_X)

    def runOperation(self):
        self.getParameters()

        self.internal = self.xStart < self.xEnd
        self.zCut = abs(self.zStart - self.zEnd)

        self.calcFeed(self.zFeed, self.zCut)
        self.mf.comm.setParm(pm.TOTAL_PASSES, self.passes)
        self.pause = self.panel.pause.GetValue()
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
        if self.mf.cfgDraw:
            m.draw("face", self.xStart, self.xEnd)
            m.setTextAngle(90)

        self.mf.dPrt("\nface runOperation\n")
        self.mf.dPrt(timeStr() + "\n")
        self.setup()

        while self.updatePass():
            pass

        m.moveX(self.safeX)
        m.moveZ(self.zStart + self.zRetract)

        self.passDone()
        return(True)

    def setup(self, add=False): # face
        comm = self.mf.comm
        comm.queParm(pm.CURRENT_OP, en.OP_FACE)
        m = self.m
        if not add:
            m.setLoc(self.zEnd, self.xStart)
            m.drawLineZ(self.zStart, REF)
            m.drawLineX(self.xEnd, REF)
            m.setLoc(self.zStart, self.safeX)

            sendSyncParm(self)

        m.queInit()
        if (not add) or (add and not self.pause):
            m.quePause()
        m.done(ct.PARM_START)

        comm.command(cm.C_CMD_SYNCSETUP)

        m.startSpindle(self.mf.cfg.getIntInfoData(cf.faRPM))

        m.queFeedType(ct.FEED_PITCH)
        m.xSynSetup(self.mf.cfg.getFloatInfoData(cf.faXFeed))

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
        self.mf.dPrt("pass %2d feed %5.3f z %5.3f\n" % \
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
        add = self.addInit("face", self.panel)
        self.cutAmount += add
        self.setup(True)
        self.calcPass(True)
        m = self.m
        m.nextPass(self.passCount)
        self.runPass(True)
        m.moveX(self.safeX)
        m.moveZ(self.zStart + self.zRetract)
        self.addDone()

    def fixCut(self, offset=0.0): # turn
        jp = self.mf.jogPanel
        passNum = jp.lastPass
        if offset == 0.0:
            actual = float(jp.zPos.GetValue())
            self.passSize[passNum] = actual
            self.cutAmount = self.zStart - actual
        else:
            self.passSize[passNum] += offset

class FacePanel(wx.Panel, PanelVars, FormRoutines, ActionRoutines):
    def __init__(self, mainFrame, hdrFont, *args, **kwargs):
        PanelVars.__init__(self)
        FormRoutines.__init__(self)
        super(FacePanel, self).__init__(mainFrame, *args, **kwargs)
        ActionRoutines.__init__(self, Face(mainFrame, self), en.OP_FACE)
        self.Bind(wx.EVT_SHOW, OnPanelShow)
        self.mf = mainFrame
        self.hdrFont = hdrFont
        self.InitUI()
        self.prefix = 'fa'
        # self.formatList = ((cf.faAddFeed, 'f'), \
        #                    (cf.faPasses, 'd'), \
        #                    (cf.faPause, None), \
        #                    (cf.faRPM, 'd'), \
        #                    (cf.faSPInt, 'd'), \
        #                    (cf.faSpring, 'd'), \
        #                    (cf.faXEnd, 'f'), \
        #                    (cf.faXFeed, 'f'), \
        #                    (cf.faXRetract, 'f'), \
        #                    (cf.faXStart, 'f'), \
        #                    (cf.faZEnd, 'f'), \
        #                    (cf.faZFeed, 'f'), \
        #                    (cf.faZRetract, 'f'), \
        #                    (cf.faZStart, 'f'))

    def InitUI(self):
        self.sizerV = sizerV = wx.BoxSizer(wx.VERTICAL)

        txt = wx.StaticText(self, -1, "Face", size=(120, 30))
        txt.SetFont(self.hdrFont)

        sizerV.Add(txt, flag=wx.CENTER|wx.ALL, border=2)

        sizerG = wx.FlexGridSizer(cols=8, rows=0, vgap=0, hgap=0)

        # z parameters

        self.zEnd = addField(self, sizerG, "Z End", cf.faZEnd, 'f')

        self.zStart = addField(self, sizerG, "Z Start", cf.faZStart, 'f')

        self.zFeed = addField(self, sizerG, "Z Feed", cf.faZFeed, 'f')

        self.zRetract = addField(self, sizerG, "Z Retract", cf.faZRetract, 'f')

        # x parameters

        self.xStart = addField(self, sizerG, "X Start D", cf.faXStart, 'f')

        self.xEnd = addField(self, sizerG, "X End D", cf.faXEnd, 'f')

        self.xFeed = addField(self, sizerG, "X Feed", cf.faXFeed, 'f')

        self.xRetract = addField(self, sizerG, "X Retract", cf.faXRetract, 'f')

        # pass info

        self.passes = addField(self, sizerG, "Passes", cf.faPasses, 'd')
        self.passes.SetEditable(False)

        self.sPInt = addField(self, sizerG, "SP Int", cf.faSPInt, 'd')

        self.spring = addField(self, sizerG, "Spring", cf.faSpring, 'd')

        placeHolder(sizerG)

        # buttons

        addButtons(self, sizerG, cf.faAddFeed, cf.faRPM, cf.faPause)

        sizerV.Add(sizerG, flag=wx.CENTER|wx.ALL, border=2)

        self.SetSizer(sizerV)
        self.sizerV.Fit(self)

    def OnEnter(self, _):
        OnEnter(self)

    def update(self):
        formatData(self.mf.cfg, self.formatList)
        self.mf.jogPanel.setPassText("Len")

    def sendData(self):
        try:
            self.mf.move.queClear()
            sd = self.mf.sendData
            sd.sendClear()
            sd.sendSpindleData()
            sd.sendZData()
            sd.sendXData()

        except CommTimeout:
            commTimeout(self.mf.jogPanel)

    def sendAction(self):
        self.mf.jogPanel.setStatus(st.STR_CLR)
        self.sendData()
        return(self.control.runOperation())

    def startAction(self):
        self.mf.comm.command(cm.C_CMD_RESUME)
        control = self.control
        if control.addEnabled:
            if self.mf.jogPanel.mvStatus & ct.MV_READ_Z:
                control.fixCut()
        else:
            if self.mf.dbgSave:
                self.mf.updateThread.openDebug(action=en.OP_FACE)

    def addAction(self):
        self.control.addPass()

class Cutoff(LatheOp):
    def __init__(self, mainFrame, cutoffPanel):
        LatheOp.__init__(self, mainFrame, cutoffPanel)
        self.mf = mainFrame
        self.addEnabled = False
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

        getSyncParm(self, cu.xFeed, cu.rpm, AXIS_Z)

    def runOperation(self):
        self.getParameters()

        self.safeX = self.xStart + self.xRetract
        self.cutoffZ = self.zCutoff - self.toolWidth

        self.passSize[0] = self.cutoffZ
        m = self.m
        if self.mf.cfgDraw:
            m.draw("cutoff", self.xStart, self.zStart)

        dPrt = self.mf.dPrt
        dPrt("\ncutoff runOperation\n")
        dPrt(timeStr() + "\n")
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
        m = self.m
        mf = self.mf
        comm = mf.comm
        comm.queParm(pm.CURRENT_OP, en.OP_CUTOFF)

        sendSyncParm(self)

        m.queInit()
        m.quePause()
        m.done(ct.PARM_START)

        comm.command(cm.C_CMD_SYNCSETUP)

        cfg = mf.cfg
        m.startSpindle(cfg.getIntInfoData(cf.cuRPM))

        m.queFeedType(ct.FEED_PITCH)
        m.xSynSetup(cfg.getFloatInfoData(cf.cuXFeed))

        m.moveX(self.safeX)
        m.moveZ(self.cutoffZ)
        m.moveX(self.xStart)

class CutoffPanel(wx.Panel, FormRoutines, ActionRoutines):
    def __init__(self, mainFrame, hdrFont, *args, **kwargs):
        super(CutoffPanel, self).__init__(mainFrame, *args, **kwargs)
        FormRoutines.__init__(self)
        ActionRoutines.__init__(self, Cutoff(mainFrame, self), en.OP_CUTOFF)
        self.Bind(wx.EVT_SHOW, OnPanelShow)
        self.mf = mainFrame
        self.hdrFont = hdrFont
        self.InitUI()
        self.prefix = 'cf'
        # self.formatList = ((cf.cuPause, None), \
        #                    (cf.cuRPM, 'd'), \
        #                    (cf.cuToolWidth, 'f'), \
        #                    (cf.cuXEnd, 'f'), \
        #                    (cf.cuXFeed, 'f'), \
        #                    (cf.cuXRetract, 'f'), \
        #                    (cf.cuXStart, 'f'), \
        #                    (cf.cuZCutoff, 'f'), \
        #                    (cf.cuZStart, 'f'), \
        #                    (cf.cuZRetract, 'f'), \
        # )

    def InitUI(self):
        self.sizerV = sizerV = wx.BoxSizer(wx.VERTICAL)

        txt = wx.StaticText(self, -1, "Cutoff", size=(120, 30))
        txt.SetFont(self.hdrFont)

        sizerV.Add(txt, flag=wx.CENTER|wx.ALL, border=2)

        sizerG = wx.FlexGridSizer(cols=8, rows=0, vgap=0, hgap=0)

        # z parameters

        self.zCutoff = addField(self, sizerG, "Z Cutoff", cf.cuZCutoff, 'f')

        self.zStart = addField(self, sizerG, "Z Start", cf.cuZStart, 'f')

        self.zRetract = addField(self, sizerG, "Z Retract", cf.cuZRetract, 'f')

        self.toolWidth = addField(self, sizerG, "Tool Width", \
                                  cf.cuToolWidth, 'f')

        # x parameters

        self.xStart = addField(self, sizerG, "X Start D", cf.cuXStart, 'f')

        self.xEnd = addField(self, sizerG, "X End D", cf.cuXEnd, 'f')

        self.xFeed = addField(self, sizerG, "X Feed", cf.cuXFeed, 'f')

        self.xRetract = addField(self, sizerG, "X Retract", cf.cuXRetract, 'f')

        # buttons

        addButtons(self, sizerG, None, cf.cuRPM, cf.cuPause)

        sizerV.Add(sizerG, flag=wx.CENTER|wx.ALL, border=2)

        self.SetSizer(sizerV)
        self.sizerV.Fit(self)

    def OnEnter(self, _):
        OnEnter(self)

    def update(self):
        formatData(self.mf.cfg, self.formatList)
        self.mf.jogPanel.setPassText("Len")

    def sendData(self):
        try:
            self.mf.move.queClear()
            sd = self.mf.sendData
            sd.sendClear()
            sd.sendSpindleData()
            sd.sendZData()
            sd.sendXData()
        except CommTimeout:
            commTimeout(self.mf.jogPanel)

    def sendAction(self):
        self.sendData()
        return(self.control.runOperation())

    def startAction(self):
        self.mf.comm.command(cm.C_CMD_RESUME)
        if self.mf.dbgSave:
            self.mf.updateThread.openDebug(action=en.OP_CUTOFF)

class Taper(LatheOp, UpdatePass):
    def __init__(self, mainFrame, taperPanel):
        LatheOp.__init__(self, mainFrame, taperPanel)
        UpdatePass.__init__(self, mainFrame)
        self.mf = mainFrame
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

        self.zBackInc = abs(self.mf.cfg.getFloatInfoData(cf.zBackInc))
        self.finish = abs(getFloatVal(tp.finish))

        getSyncParm(self, tp.zFeed, tp.rpm, AXIS_Z)

        totalTaper = taperInch * self.zLength
        print("taperX %s totalTaper %5.3f taperInch %6.4f" % \
              (self.taperX, totalTaper, taperInch))

    def setup(self, add=False): # taper
        comm = self.mf.comm
        cfg = self.mf.cfg
        m = self.m
        comm.queParm(pm.CURRENT_OP, en.OP_TAPER)
        if not add:
            m.setLoc(self.zEnd, self.xStart)
            m.drawLineZ(self.zStart, REF)
            m.drawLineX(self.xEnd, REF)
            m.setLoc(self.safeZ, self.safeX)

            sendSyncParm(self)

        m.queInit()
        if (not add) or (add and not self.pause):
            m.quePause(ct.PAUSE_ENA_X_JOG | ct.PAUSE_ENA_Z_JOG)
        m.done(ct.PARM_START)

        comm.command(cm.C_CMD_SYNCSETUP)

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
        self.mf.comm.setParm(pm.TOTAL_PASSES, self.passes)
        self.pause = self.panel.pause.GetValue()
        self.setupSpringPasses(self.panel)
        self.setupAction(self.externalCalcPass, self.externalRunPass)

        self.panel.passes.SetValue("%d" % (self.passes,))
        print("passes %d cutAmount %5.3f feed %6.3f" % \
              (self.passes, self.cutAmount, self.actualFeed))

        m = self.m
        if self.mf.cfgDraw:
            m.draw("taper", self.zStart, self.taper)

        self.mf.dPrt("\ntaper external RunOperation\n")
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
        self.mf.dPrt("%2d start (%6.3f %6.3f) end (%6.3f %6.3f) "\
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
        add = self.addInit("external taper", self.panel) / 2.0
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
            jp = self.mf.jogPanel
            actual = float(jp.xPos.GetValue())
            passNum = jp.lastPass
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
        self.mf.comm.setParm(pm.TOTAL_PASSES, self.passes)
        self.pause = self.panel.pause.GetValue()
        self.setupSpringPasses(self.panel)
        self.setupAction(self.internalCalcPass, self.internalRunPass)

        self.panel.passes.SetValue("%d" % (self.passes))
        print("passes %d cutAmount %5.3f feed %6.3f" % \
              (self.passes, self.cutAmount, self.actualFeed))

        self.endZ = self.zStart

        self.safeX = self.boreRadius - self.xRetract
        self.safeZ = self.zStart + self.zRetract

        m = self.m
        if self.mf.cfgDraw:
            m.draw("taper", self.zStart, self.taper)

        self.mf.dPrt("\ntaper internalRunOperation\n")
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
        self.mf.dPrt("%2d feed %6.3f start (%6.3f,%6.3f) end (%6.3f %6.3f) "\
                     "%6.3f %6.3f\n" % \
                     (self.passCount, self.feed, self.startX,
                      self.startZ, self.endX, self.endZ, \
                      self.startX * 2.0, self.endX * 2.0), True, True)

    def internalRunPass(self, addPass=False):
        m = self.m
        if self.zBackInc != 0.0:
            m.moveZ(self.startZ, backlash=-self.zBackInc) # past the start
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
        add = self.addInit("internal taper", self.panel) / 2.0
        self.cutAmount += add
        self.setup(True)
        self.internalCalcPass(True)
        m = self.m
        m.nextPass(self.passCount)
        self.internalRunPass(True)
        m.moveX(self.safeX)
        m.moveZ(self.safeZ)
        self.addDone()

class TaperPanel(wx.Panel, PanelVars, FormRoutines, ActionRoutines):
    def __init__(self, mainFrame, hdrFont, *args, **kwargs):
        super(TaperPanel, self).__init__(mainFrame, *args, **kwargs)
        PanelVars.__init__(self)
        FormRoutines.__init__(self)
        ActionRoutines.__init__(self, Taper(mainFrame, self), en.OP_TAPER)
        self.Bind(wx.EVT_SHOW, OnPanelShow)
        self.mf = mainFrame
        self.hdrFont = hdrFont
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
        self.taperSel = None
        self.zLength = None
        self.xInFeed = None
        self.deltaBtn = None
        self.zDelta = None
        self.xDelta = None
        self.angleButton = None
        self.angle = None
        self.finish = None
        self.taperList = []
        for t in self.taperDef:
            self.taperList.append(t[0])
        self.InitUI()
        self.prefix = 'tp'
        # self.formatList = ((cf.tpAddFeed, 'f'), \
        #                    (cf.tpAngle, 'fs'), \
        #                    (cf.tpAngleBtn, None), \
        #                    (cf.tpDeltaBtn, None), \
        #                    (cf.tpInternal, None), \
        #                    (cf.tpLargeDiam, 'f'), \
        #                    (cf.tpPasses, 'd'), \
        #                    (cf.tpPause, None), \
        #                    (cf.tpRPM, 'd'), \
        #                    (cf.tpSPInt, 'd'), \
        #                    (cf.tpSmallDiam, 'f'), \
        #                    (cf.tpSpring, 'd'), \
        #                    (cf.tpTaperSel, None), \
        #                    (cf.tpXDelta, 'f5'), \
        #                    (cf.tpXFeed, 'f'), \
        #                    (cf.tpXFinish, 'f'), \
        #                    (cf.tpXInFeed, 'f'), \
        #                    (cf.tpXRetract, 'f'), \
        #                    (cf.tpZDelta, 'f'), \
        #                    (cf.tpZFeed, 'f'), \
        #                    (cf.tpZLength, 'f'), \
        #                    (cf.tpZRetract, 'f'), \
        #                    (cf.tpZStart, 'f'))

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
        self.mf.cfg.initInfo(cf.tpTaperSel, combo)
        combo.Bind(wx.EVT_COMBOBOX, self.OnCombo)
        sizerH.Add(combo, flag=wx.ALL, border=2)

        sizerV.Add(sizerH, flag=wx.CENTER|wx.ALL, border=2)

        sizerG = wx.FlexGridSizer(cols=8, rows=0, vgap=0, hgap=0)

        # z parameters

        self.zLength = addField(self, sizerG, "Z Length", cf.tpZLength, 'f')

        self.zStart = addField(self, sizerG, "Z Start", cf.tpZStart, 'f')

        self.zFeed = addField(self, sizerG, "Z Feed", cf.tpZFeed, 'f')

        self.zRetract = addField(self, sizerG, "Z Retract", cf.tpZRetract, 'f')

        # x parameters

        (self.largeDiam, self.largeDiamTxt) = \
            addFieldText(self, sizerG, "Large Diam", cf.tpLargeDiam, 'f')

        (self.smallDiam, self.smallDiamTxt) = \
            addFieldText(self, sizerG, "Small Diam", cf.tpSmallDiam, 'f')

        self.xInFeed = addField(self, sizerG, "X In Feed R", cf.tpXInFeed, 'f')

        self.xFeed = addField(self, sizerG, "X Pass D", cf.tpXFeed, 'f')

        # taper parameters

        self.deltaBtn = addRadioButton(self, sizerG, "Delta Z", cf.tpDeltaBtn, \
                                       style=wx.RB_GROUP, action=self.OnDelta)

        self.zDelta = addField(self, sizerG, None, cf.tpZDelta, 'f')
        self.zDelta.Bind(wx.EVT_KILL_FOCUS, self.OnDeltaFocus)

        self.xDelta = addField(self, sizerG, "Delta X", cf.tpXDelta, 'f5')
        self.xDelta.Bind(wx.EVT_KILL_FOCUS, self.OnDeltaFocus)

        self.angleBtn = addRadioButton(self, sizerG, "Angle", cf.tpAngleBtn, \
                                       action=self.OnAngle)

        self.angle = addField(self, sizerG, None, cf.tpAngle, 'fs')
        self.angle.Bind(wx.EVT_KILL_FOCUS, self.OnAngleFocus)

        self.xRetract = addField(self, sizerG, "X Retract", cf.tpXRetract, 'f')

        # pass info

        self.passes = addField(self, sizerG, "Passes", cf.tpPasses, 'd')
        self.passes.SetEditable(False)

        self.sPInt = addField(self, sizerG, "SP Int", cf.tpSPInt, 'd')

        self.spring = addField(self, sizerG, "Spring", cf.tpSpring, 'd')

        self.finish = addField(self, sizerG, "Finish", cf.tpXFinish, 'f')

        # control buttons

        addButtons(self, sizerG, cf.tpAddFeed, cf.tpRPM, cf.tpPause, True)

        self.internal = addCheckBox(self, sizerG, "Internal", cf.tpInternal, \
                                    self.OnInternal, box=True)

        sizerV.Add(sizerG, flag=wx.CENTER|wx.ALL, border=2)

        self.SetSizer(sizerV)
        sizerV.Fit(self)

    def OnEnter(self, _):
        OnEnter(self)

    def update(self):
        self.updateUI()
        self.updateDelta()
        self.updateAngle()
        formatData(self.mf.cfg, self.formatList)

    def updateUI(self):
        val = self.deltaBtn.GetValue()
        self.zDelta.SetEditable(val)
        self.xDelta.SetEditable(val)
        self.angle.SetEditable(not val)
        taper = getFloatVal(self.xDelta) / getFloatVal(self.zDelta)
        if self.internal.GetValue():
            self.largeDiamTxt.SetLabel("Bore Diam")
            self.smallDiamTxt.SetLabel("Large Diam")
            self.mf.jogPanel.setPassText("L Diam")

        else:
            self.largeDiamTxt.SetLabel("Large Diam")
            self.smallDiamTxt.SetLabel("Small Diam")
            self.mf.jogPanel.setPassText("S Diam" if taper < 1.0 else \
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
            except ValueError:
                traceback.print_exc()

    def OnCombo(self, _):
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

    def OnInternal(self, _):
        self.updateUI()

    def OnDelta(self, _):
        self.updateUI()

    def OnAngle(self, _):
        self.updateUI()

    def sendData(self):
        try:
            mf = self.mf
            mf.move.queClear()
            sd = mf.sendData
            sd.sendClear()
            sd.sendSpindleData()
            sd.sendZData()
            sd.sendXData()
            mf.comm.setParm(pm.TAPER_CYCLE_DIST, \
                            mf.cfg.getInfoData(cf.cfgTaperCycleDist))
        except CommTimeout:
            commTimeout(self.mf.jogPanel)

    def sendAction(self):
        self.sendData()
        taper = getFloatVal(self.xDelta) / getFloatVal(self.zDelta)
        if self.internal.GetValue():
            return self.control.internalRunOperation(taper)
        else:
            return self.control.externalRunOperation(taper)

    def startAction(self):      # taper
        mf = self.mf
        mf.comm.command(cm.C_CMD_RESUME)
        control = self.control
        if control.addEnabled:
            if mf.jogPanel.mvStatus & ct.MV_READ_X:
                control.fixCut()
        else:
            if mf.dbgSave:
                mf.updateThread.openDebug(action=en.OP_TAPER)

    def addAction(self):
        self.control.internalAddPass() if self.internal.GetValue() else \
            self.control.externalAddPass()

    # def OnDebug(self, _):
    #     self.sendData()
    #     moveX(1.000)
    #     moveZ(0.010)
    #     taperZX(-0.25, 0.0251)

class ScrewThread(LatheOp, UpdatePass):
    def __init__(self, mainFrame, threadPanel):
        LatheOp.__init__(self, mainFrame, threadPanel)
        UpdatePass.__init__(self, mainFrame)
        self.mf = mainFrame
        self.tpiBtn = None
        self.alternate = None
        self.firstFeedBtn = None
        self.runout = None
        self.endZ = 0.0

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
        self.zBackInc = abs(self.mf.cfg.getFloatInfoData(cf.zBackInc))

        self.tpiBtn = th.tpi.GetValue()
        self.alternate = th.alternate.GetValue()
        self.firstFeedBtn = th.firstFeedBtn.GetValue()

        thVal =  getFloatVal(th.thread)
        rpm = getIntVal(th.rpm)
        if self.tpiBtn:
            self.tpi = thVal
            self.pitch = 1.0 / thVal
            metric = False
        else:
            self.pitch = thVal / 25.4
            self.tpi = 1.0 / self.pitch
            metric = True

        threadSync = self.mf.threadSync
        if threadSync == en.SEL_TH_ISYN_RENC or threadSync == en.SEL_TH_SYN:
            (self.cycle, self.output, self.inPreScaler, self.outPreScaler) = \
                self.mf.zSyncInt.calcSync(thVal, dbg=True,
                                          metric=metric, rpm=rpm)
        elif (threadSync == en.SEL_TH_ESYN_RENC or \
              threadSync == en.SEL_TH_ESYN_RSYN):
            (self.cycle, self.output, self.inPreScaler, self.outPreScaler) = \
                self.mf.zSyncExt.calcSync(thVal, dbg=True,
                                          metric=metric, rpm=rpm)

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
            if threadSync == en.SEL_TH_ESYN_RSYN:
                xSync = self.mf.xSyncExt
                xSync.setExitRevs(self.runout)
                (self.xCycle, self.xOutput, self.xInPreScaler,
                 self.xOutPreScaler) = \
                    xSync.calcSync(self.depth, rpm=rpm, dist=True)

        self.endZ = self.zEnd

    def setup(self, add=False): # thread
        comm = self.mf.comm
        queParm = comm.queParm
        queParm(pm.CURRENT_OP, en.OP_THREAD)
        m = self.m
        if not add:
            m.setLoc(self.endZ, self.xStart)
            m.drawLineZ(self.zStart, REF)
            m.drawLineX(self.xEnd, REF)
            m.setLoc(self.safeZ, self.safeX)

        threadSync = self.mf.threadSync
        if threadSync == en.SEL_TH_ISYN_RENC or \
           threadSync == en.SEL_TH_SYN or \
           ((threadSync == en.SEL_TH_ESYN_RENC) and SYNC_SPI):
            queParm(pm.L_SYNC_CYCLE, self.cycle)
            queParm(pm.L_SYNC_OUTPUT, self.output)
            queParm(pm.L_SYNC_IN_PRESCALER, self.inPreScaler)
            queParm(pm.L_SYNC_IN_PRESCALER, self.outPreScaler)
            if SYNC_SPI:
                m.syncParms()
                m.syncCommand(sc.SYNC_SETUP)
        elif threadSync == en.SEL_TH_ESYN_RENC:
            syncComm = self.mf.syncComm
            syncComm.setParm(sp.SYNC_ENCODER, \
                             self.mf.cfg.getIntInfoData(cf.cfgEncoder))
            syncComm.setParm(sp.SYNC_CYCLE, self.cycle)
            syncComm.setParm(sp.SYNC_OUTPUT, self.output)
            syncComm.setParm(sp.SYNC_PRESCALER, self.outPreScaler)
            syncComm.command(sc.SYNC_SETUP)

        if ((self.runout != 0) and \
            (threadSync == en.SEL_TH_ESYN_RSYN)):
            queParm(pm.L_X_SYNC_CYCLE, self.xCycle)
            queParm(pm.L_X_SYNC_OUTPUT, self.xOutput)
            queParm(pm.L_X_SYNC_IN_PRESCALER, self.xInPreScaler)
            queParm(pm.L_X_SYNC_OUT_PRESCALER, self.xOutPreScaler)

        queParm(pm.RUNOUT_DEPTH, self.runoutDepth)
        queParm(pm.RUNOUT_DISTANCE, self.runoutDist)

        m.queInit()
        if (not add) or (add and not self.pause):
            m.quePause()
        m.done(ct.PARM_START)

        comm.command(cm.C_CMD_SYNCSETUP)

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

        m.zSynSetup(self.mf.cfg.getFloatInfoData(cf.thThread))

        if not self.rightHand:  # left hand threads
            if self.runoutDist == 0.0: # without runout
                m.queFeedType(ct.FEED_PITCH)
                m.xSynSetup(getFloatVal(th.lastFeed))

        m.startSpindle(self.mf.cfg.getIntInfoData(cf.thRPM))

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
        self.mf.comm.setParm(pm.TOTAL_PASSES, self.passes)
        self.pause = self.panel.pause.GetValue()

        if self.internal:
            self.xRetract = -self.xRetract

        self.safeX = self.xStart + self.xRetract
        # self.startZ = self.zStart + self.zAccelDist

        # if self.mf.cfgDraw:
        #     self.draw(self.xStart * 2.0, self.tpi)
        #     self.p0 = (0, 0)

        if self.mf.cfgDraw:
            self.m.draw("thread", self.xStart * 2.0, self.tpi)

        dPrt = self.mf.dPrt
        dPrt("\nthread runOperation\n")
        dPrt(timeStr() + "\n")
        self.setup()

        self.curArea = 0.0
        self.prevFeed = 0.0
        self.zOffset = 0.0
        if not self.alternate:
            dPrt("pass     area   xfeed  xdelta zoffset  " \
                 "xsize startz\n", True, True)
        else:
            dPrt("pass     area   xfeed  xdelta  offset " \
                 "zoffset  xsize startz\n", True, True)

        while self.updatePass():
            pass

        self.m.printXText("%2d Z %6.4f Zofs %6.4f D %6.4f F %6.4f", \
                          LEFT if self.rightHand else RIGHT, \
                          self.internal)

        self.passDone()
        return(True)

    def calcPass(self, final=False, add=False):
        dPrt = self.mf.dPrt
        if not add:
            if final:
                self.curArea = self.area
            else:
                self.curArea += self.areaPass
            self.feed = sqrt(self.curArea / self.tanAngle)

        feed = self.feed
        passFeed = feed - self.prevFeed
        self.prevFeed = feed

        offset = 0
        if not self.alternate:
            self.zOffset = -feed * self.tanAngle
            dPrt("startZ %7.4f zOffset %7.4f\n" % \
                          (self.startZ, self.zOffset))
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
            dPrt("%4d %8.6f %7.4f %7.4f %7.4f %6.4f %6.4f\n" % \
                          (self.passCount, self.curArea, feed, \
                           passFeed, self.zOffset, \
                           self.curX * 2.0, startZPass), \
                          True, True)
        else:
            dPrt("%4d %8.6f %7.4f %7.4f %7.4f %7.4f %6.4f %6.4f\n" % \
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
            # if addPass:
            #     m.moveZOffset()

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
        add = self.addInit("thread", self.panel) / 2.0
        self.feed += add
        self.setup(True)

        jp = self.mf.jogPanel
        queParm = self.mf.comm.queParm
        queParm(pm.TH_Z_START, \
                round((self.startZ + jp.zHomeOffset) * jp.zStepsInch))
        queParm(pm.TH_X_START, \
                round((self.xStart + jp.xHomeOffset) * jp.xStepsInch))
        queParm(pm.TAN_THREAD_ANGLE, self.tanAngle)

        self.calcPass(add=True)
        self.m.nextPass(self.passCount)
        self.runPass(True)
        self.addDone()

    def fixCut(self, offset=0.0): # thread
        if offset == 0.0:
            jp = self.mf.jogPanel
            actual = float(jp.xPos.GetValue())
            passNum = jp.lastPass
            if self.internal:
                self.feed = actual - self.xStart
            else:
                self.feed = self.xStart - actual
            self.passSize[passNum] = self.feed
        else:
            pass

class ThreadPanel(wx.Panel, PanelVars, FormRoutines, ActionRoutines):
    def __init__(self, mainFrame, hdrFont, *args, **kwargs):
        super(ThreadPanel, self).__init__(mainFrame, *args, **kwargs)
        PanelVars.__init__(self)
        FormRoutines.__init__(self)
        ActionRoutines.__init__(self, ScrewThread(mainFrame, self), en.OP_THREAD)
        self.Bind(wx.EVT_SHOW, OnPanelShow)
        self.mf = mainFrame
        self.hdrFont = hdrFont
        self.leftHand = None
        self.xStart = None
        self.depth = None
        self.alternate = None
        self.thread = None
        self.tpi = None
        self.mm = None
        self.angle = None
        self.firstFeedBtn = None
        self.firstFeed = None
        self.xTaper = None
        self.runout = None
        self.lastFeedBtn = None
        self.lastFeed = None
        self.InitUI()
        self.prefix = 'th'
        # self.formatList = ((cf.thAddFeed, 'f'), \
        #                    (cf.thAlternate, None), \
        #                    (cf.thAngle, 'fs'), \
        #                    (cf.thFirstFeed, 'f'), \
        #                    (cf.thFirstFeedBtn, None), \
        #                    (cf.thInternal, None), \
        #                    (cf.thLastFeed, 'f'), \
        #                    (cf.thLastFeedBtn, None), \
        #                    (cf.thLeftHand, None), \
        #                    (cf.thMM, None), \
        #                    (cf.thPasses, 'd'), \
        #                    (cf.thPause, None), \
        #                    (cf.thRPM, 'd'), \
        #                    (cf.thSPInt, 'n'), \
        #                    (cf.thSpring, 'n'), \
        #                    (cf.thTPI, None), \
        #                    (cf.thThread, 'fs'), \
        #                    (cf.thXDepth, 'f'), \
        #                    (cf.thXRetract, 'f'), \
        #                    (cf.thRunout, 'fs'), \
        #                    (cf.thXStart, 'f'), \
        #                    (cf.thXTaper, 'f'), \
        #                    (cf.thZ0, 'f'), \
        #                    (cf.thZ1, 'f'), \
        #                    (cf.thZRetract, 'f'))

    def InitUI(self):
        self.sizerV = sizerV = wx.BoxSizer(wx.VERTICAL)

        txt = wx.StaticText(self, -1, "Thread", size=(120, 30))
        txt.SetFont(self.hdrFont)

        sizerV.Add(txt, flag=wx.CENTER|wx.ALL, border=2)

        sizerG = wx.FlexGridSizer(cols=8, rows=0, vgap=0, hgap=0)

        # z parameters

        (self.z0, self.z0Txt) = \
            addFieldText(self, sizerG, "Z End", cf.thZ0, 'f')

        (self.z1, self.z1Txt) = \
            addFieldText(self, sizerG, "Z Start", cf.thZ1, 'f')

        self.zRetract = addField(self, sizerG, "Z Retract", cf.thZRetract, 'f')

        self.leftHand = addCheckBox(self, sizerG, "Left Hand", cf.thLeftHand, \
                                    action=self.OnLeftHand)

        # x parameters

        self.xStart = addField(self, sizerG, "X Start D", cf.thXStart, 'f')

        self.xRetract = addField(self, sizerG, "X Retract", cf.thXRetract, 'f')

        self.depth = addField(self, sizerG, "Depth", cf.thXDepth, 'f')

        self.alternate = addCheckBox(self, sizerG, "Alternate", cf.thAlternate)


        # self.final = btn = wx.RadioButton(self, label="Final", \
        #                                   style = wx.RB_GROUP)
        # sizerH.Add(btn, flag=wx.CENTER|wx.ALL, border=2)
        # self.mf.cfg.initInfo(thFinal, btn)

        # self.depth = btn = wx.RadioButton(self, label="Depth")
        # sizerH.Add(btn, flag=wx.CENTER|wx.ALL, border=2)
        # self.mf.cfg.initInfo(thDepth, btn)

        # thread parameters

        self.thread = addField(self, sizerG, "Thread", cf.thThread, 'fs')

        self.tpi = addRadioButton(self, sizerG, "TPI", cf.thTPI, \
                                  style=wx.RB_GROUP)

        self.mm = addRadioButton(self, sizerG, "mm", cf.thMM)

        self.angle = addField(self, sizerG, "Angle", cf.thAngle, 'fs')


        self.firstFeedBtn = addRadioButton(self, sizerG, "First Feed", \
                                           cf.thFirstFeedBtn, \
                                           style=wx.RB_GROUP, \
                                           action=self.OnFirstFeed)

        self.firstFeed = addField(self, sizerG, None, cf.thFirstFeed, 'f')

        # special thread parameters

        self.xTaper = addField(self, sizerG, "Taper", cf.thXTaper, 'f')

        self.runout = addField(self, sizerG, "Exit Rev", cf.thRunout, 'fs')

        placeHolder(sizerG)

        self.lastFeedBtn = addRadioButton(self, sizerG, "Last Feed", \
                                          cf.thLastFeedBtn, \
                                          action=self.OnLastFeed)

        self.lastFeed = addField(self, sizerG, None, cf.thLastFeed, 'f')

        # pass info

        self.passes = addField(self, sizerG, "Passes", cf.thPasses, 'd')
        self.passes.SetEditable(False)

        self.sPInt = addField(self, sizerG, "SP Int", cf.thSPInt, 'd')

        self.spring = addField(self, sizerG, "Spring", cf.thSpring, 'd')

        placeHolder(sizerG)

        # buttons

        addButtons(self, sizerG, cf.thAddFeed, cf.thRPM, cf.thPause, True)

        self.internal = addCheckBox(self, sizerG, "Internal", cf.thInternal, \
                                    action=self.OnInternal, box=True)

        sizerV.Add(sizerG, flag=wx.CENTER|wx.ALL, border=2)

        self.SetSizer(sizerV)
        self.sizerV.Fit(self)

    def OnEnter(self, _):
        OnEnter(self)

    def update(self):
        formatData(self.mf.cfg, self.formatList)
        self.updateLeftHand()
        self.updateFirstFeed()
        self.updateLastFeed()
        self.sizerV.Layout()
        self.mf.jogPanel.setPassText("Feed")

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

    def OnLeftHand(self, _):
        self.updateLeftHand()
        self.sizerV.Layout()

    def OnInternal(self, _):
        pass

    def OnFirstFeed(self, _):
        self.updateFirstFeed()

    def OnLastFeed(self, _):
        self.updateLastFeed()

    def sendData(self):
        self.mf.move.queClear()
        sd = self.mf.sendData
        sd.sendClear()
        sd.sendSpindleData()
        sd.sendZData()
        sd.sendXData()

    def sendAction(self):
        self.sendData()
        return(self.control.runOperation())

    def startAction(self):      # thread
        self.mf.comm.command(cm.C_CMD_RESUME)
        control = self.control
        if control.addEnabled:
            if self.mf.jogPanel.mvStatus & ct.MV_READ_X:
                control.fixCut()
        else:
            if self.mf.dbgSave:
                print("openDebug")
                stdout.flush()
                self.mf.updateThread.openDebug(action=en.OP_THREAD)

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
            while self.event.is_set():
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
    def __init__(self, mainFrame, port, rate):
        self.mf = mainFrame
        self.threadRun = False
        self.threadDone = False
        if port is None:
            return
        if len(port) == 0:
            return
        Thread.__init__(self)
        self.port = port
        self.rate = rate
        try:
            self.ser = serial.Serial(port, rate, timeout=1)
        except IOError:
            print("keypad unable to open port %s exit" % (port))
            stdout.flush()
            self.ser = None
            self.threadDone = True
            return

        self.start()

    def run(self):
        self.threadRun = True
        prtErr = True
        while self.threadRun:
            if self.ser is not None:
                try:
                    tmp = str(self.ser.read(1).decode('utf8'))
                    if len(tmp) != 0:
                        wx.PostEvent(self.mf.jogPanel, KeypadEvent(ord(tmp[0])))
                except serial.SerialException:
                    self.ser.close()
                    self.ser = None
                    print("keypad SerialException")
                except UnicodeDecodeError:
                    print("keypad UnicodeDecodeError")
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
        if self.ser is not None:
            self.ser.close()
        print("Keypad done")
        stdout.flush()
        self.threadDone = True

    def close(self):
        self.threadRun = False

class JogShuttle(Thread):
    def __init__(self, mainFrame):
        Thread.__init__(self)
        self.mf = mainFrame
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
                        self.run()
                    except HIDError:
                        traceback.print_exc()
                    break
        if self.device is not None:
            self.threadDone = True
            return

        self.lastOuterRing = 0
        self.lastKnob = None
        self.lastButton = 0
        self.buttonAction = ((16, self.setZ), (32, self.setX))
        if STEP_DRV:
            self.buttonAction += ((64, self.setSpindle),)
        else:
            self.buttonAction += ((64, None),)
        self.buttonAction += ((128, None), (1, None))
        self.axisAction = None
        self.factor = (0.00, 0.01, 0.02, 0.05, 0.10, 0.20, 0.50, 1.00)

        factorLen = len(self.factor)

        self.zSpeed = [0.0 for _ in range(factorLen)]
        self.zCurSpeed = 0.0

        self.xSpeed = [0.0 for _ in range(factorLen)]
        self.xCurSpeed = 0.0

        self.spindleSpeed = [0.0 for _ in range(factorLen)]
        self.spindleCurSpeed = 0.0

        self.start()

    def run(self):
        t = 1
        while True:
            if not self.threadRun:
                break

            if self.device is not None:
                if not self.device.is_plugged():
                    print("shuttle unplugged")
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
                                print("open shuttle")
                                stdout.flush()
                                t = 1
                            except HIDError:
                                traceback.print_exc()
            sleep(t)
        print("JogShuttle done")
        stdout.flush()
        self.threadDone = True

    def close(self):
        self.threadRun = False

    def KeypadInput(self):
        pass

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
                buttonRepeat = self.mf.jogPanel.btnRpt
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
            maxSpeed = self.mf.cfg.getFloatInfoData(cf.zMaxSpeed)
            for val in range(len(self.factor)):
                self.zSpeed[val] = maxSpeed * self.factor[val]
            # print("set z")
            # stdout.flush()

    def setX(self, button, val):
        if button & val:
            self.axisAction = self.jogX
            maxSpeed = self.mf.cfg.getFloatInfoData(cf.xMaxSpeed)
            for val in range(len(self.factor)):
                self.xSpeed[val] = maxSpeed * self.factor[val]
            # print("set x")
            # stdout.flush()

    def setSpindle(self, button, val):
        if button & val:
            self.axisAction = self.jogSpindle
            maxSpeed = self.mf.cfg.getFloatInfoData(cf.spMaxRPM)
            for val in range(len(self.factor)):
                self.spindleSpeed[val] = \
                    maxSpeed * self.factor[val]
            # print("set spindle")
            # stdout.flush()

    def jogDone(self, cmd):
        buttonRepeat = self.mf.jogPanel.btnRpt
        buttonRepeat.action = None
        buttonRepeat.event.clear()
        self.xCurIndex = -1
        try:
            self.mf.comm.command(cmd)
        except CommTimeout:
            commTimeout(self.mf.jogPanel)

    def jogZ(self, code, val):
        if val == 0:
            self.jogDone(cm.C_ZSTOP)

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
                    self.mf.comm.setParm(pm.Z_JOG_SPEED, speed)
                self.mf.comm.command(cm.C_ZJSPEED)
            except CommTimeout:
                commTimeout(self.mf.jogPanel)

    def jogX(self, code, val):
        if val == 0:
            self.jogDone(cm.C_XSTOP)
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
                    self.mf.comm.setParm(pm.X_JOG_SPEED, speed)
                self.mf.comm.command(cm.C_XJSPEED)
            except CommTimeout:
                commTimeout(self.mf.jogPanel)

    def jogSpindle(self, code, val):
        if val == 0:
            self.jogDone(cm.C_SPINDLE_STOP)
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
                    self.mf.comm.setParm(pm.SP_JOG_RPM, speed)
                self.mf.comm.command(cm.C_SPINDLE_JOG_SPEED)
            except CommTimeout:
                commTimeout(self.mf.jogPanel)

class JogPanel(wx.Panel, FormRoutines):
    def __init__(self, mainFrame, *args, **kwargs):
        super(JogPanel, self).__init__(mainFrame, *args, **kwargs)
        FormRoutines.__init__(self)
        self.Connect(-1, -1, EVT_UPDATE_ID, self.OnUpdate)
        self.Connect(-1, -1, EVT_KEYPAD_ID, self.OnKeypadEvent)
        # self.Connect(-1, -1, EVT_STATUS_UPDATE_ID, self.OnStatusUpdate)
        # self.Bind(wx.EVT_CHAR_HOOK, self.OnCharHook)
        self.mf = mainFrame
        self.comm = mainFrame.comm
        self.cfg = mainFrame.cfg
        self.jogCode = None
        self.repeat = 0
        self.btnRpt = ButtonRepeat()
        self.surfaceSpeed = mainFrame.cfg.newInfo(cf.jpSurfaceSpeed, False)
        self.fixXPosDialog = None
        self.retractXDialog = None
        self.retractZDialog = None
        self.xReturnLoc = None
        self.zReturnLoc = None
        self.probeLoc = 0.0
        self.probeStatus = 0
        self.mvStatus = 0
        self.lastPass = 0
        self.currentPanel = None
        self.currentControl = None
        self.spindleActive = False

        self.homeOrProbe = None

        self.zStepsInch = 0
        self.lastZOffset = 0.0
        self.zPosition = 0.0
        self.zHomeOffset = 0.0
        self.zIPosition = None
        self.zIHomeOffset = None
        self.zLocation = 0.0

        self.xStepsInch = 0
        self.xPosition = 0.0
        self.xHomeOffset = 0.0
        self.xIPosition = None
        self.xIHomeOffset = None
        self.lastXOffset = 0.0
        self.xLocation = 0.0
        if DRO:
            self.zDROInch = 0
            self.zDROPosition = 0.0
            self.zDROOffset = 0.0
            self.zIDROPosition = None
            self.zIDROOffset = None

            self.xDROInch = 0
            self.xDROPosition = 0.0
            self.xDROOffset = 0.0
            self.xIDROPosition = None
            self.xIDROOffset = None
            self.xDroDiam = mainFrame.cfg.newInfo(cf.jpXDroDiam, False)
        self.overrideSet = False
        self.addEna = False
        self.xHomed = False

        eventTable = (\
                      (en.EV_ZLOC, self.updateZ), \
                      (en.EV_XLOC, self.updateX), \
                      (en.EV_RPM, self.updateRPM), \
                      (en.EV_READ_ALL, self.updateAll), \
                      (en.EV_ERROR, self.updateError), \
                      )

        self.procUpdate = [None for _ in range(en.EV_MAX)]
        for (event, action) in eventTable:
            self.procUpdate[event] = action

        self.initKeyTable()
        self.initKeypadTable()
        self.initUI()

    # noinspection PyMethodMayBeStatic
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
                assert (callable(update))
                update(val)

    def initUI(self):
        self.Bind(wx.EVT_LEFT_UP, self.OnMouseEvent)

        sizerV = wx.BoxSizer(wx.VERTICAL)

        sizerG = wx.FlexGridSizer(cols=6, rows=0, vgap=0, hgap=0)

        self.txtFont = txtFont = \
            wx.Font(16, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, \
                    wx.FONTWEIGHT_NORMAL, False, u'Consolas')
        self.posFont = posFont = \
            wx.Font(20, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, \
                    wx.FONTWEIGHT_NORMAL, False, u'Consolas')
        # first row
        # z position

        self.zPos = \
            addDialogField(self, sizerG, "Z", "0.0000", txtFont, \
                           posFont, (130, -1), border=(10, 2), \
                           edit=False, index=cf.jogZPos)
        self.zPos.Bind(wx.EVT_RIGHT_DOWN, self.OnZMenu)

        # x Position

        self.xPos = \
            addDialogField(self, sizerG, "X", "0.0000", txtFont, \
                           posFont, (130, -1), border=(10, 2), \
                           edit=False, index=cf.jogXPos)
        self.xPos.Bind(wx.EVT_RIGHT_DOWN, self.OnXMenu)

        # rpm

        (self.rpm, self.rpmText) = \
            addDialogField(self, sizerG, "RPM", "0", txtFont, \
                           posFont, (80, -1), border=(10, 2), \
                           edit=False, text=True)
        self.rpm.Bind(wx.EVT_RIGHT_DOWN, self.OnRpmMenu)
        self.setSurfaceSpeed()

        # second row
        # pass size

        (self.passSize, self.passText) = \
            addDialogField(self, sizerG, "Size", "0.000", txtFont, \
                           posFont, (130, -1), border=(10,2), \
                           edit=False, text=True)
        # x diameter

        self.xPosDiam = \
            addDialogField(self, sizerG, "X D", "0.0000", txtFont, \
                           posFont, (130, -1), border=(10, 2), \
                           edit=False)
        self.xPosDiam.Bind(wx.EVT_RIGHT_DOWN, self.OnXMenu)

        # pass

        self.curPass = \
            addDialogField(self, sizerG, "Pass", "0", txtFont, \
                           posFont, (80, -1), border=(10, 2), \
                           edit=False)

        if DRO:
            # third row
            # z dro position

            self.zDROPos = \
                addDialogField(self, sizerG, "Z", "0.0000", txtFont, \
                               posFont, (130, -1), border=(10, 2), \
                               edit=False, index=cf.droZPos)
            self.zDROPos.Bind(wx.EVT_RIGHT_DOWN, self.OnZMenu)

            # x dro Position

            self.xDROPos = \
                addDialogField(self, sizerG, "X", "0.0000", txtFont, \
                               posFont, (130, -1), border=(10, 2), \
                               edit=False, index=cf.droXPos)
            self.xDROPos.Bind(wx.EVT_RIGHT_DOWN, self.OnXMenu)

        # sizerV.Add(sizerG, flag=wx.ALIGN_CENTER_VERTICAL|wx.CENTER|wx.ALL, \
        #            border=2)
        sizerV.Add(sizerG, flag=wx.CENTER|wx.ALL, \
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
        # sizerH.Add(txt, flag=wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, \
        #            border=2)
        sizerH.Add(txt, flag=wx.ALIGN_CENTER_VERTICAL, \
                   border=2)

        self.limitOverride = cb = wx.CheckBox(self, -1)
        self.Bind(wx.EVT_CHECKBOX, self.OnOverride, cb)
        sizerH.Add(cb, flag=wx.ALIGN_CENTER_VERTICAL, \
                   border=2)

        sizerV.Add(sizerH)

        # control buttons and jog

        btnSize = wx.DefaultSize

        sizerH = wx.BoxSizer(wx.HORIZONTAL)

        sizerG = wx.FlexGridSizer(cols=3, rows=0, vgap=0, hgap=0)

        # first line

        btn = addButton(self, sizerG, 'E Stop', self.OnEStop, btnSize)
        btn.SetBackgroundColour('Red')

        self.pauseButton = \
            addButton(self, sizerG, 'Pause', self.OnPause, btnSize)
        self.pauseButton.Disable()

        if STEP_DRV:
            addControlButton(self, sizerG, 'Jog Spindle +', \
                                  self.OnJogSpindleFwd, self.OnJogUp)
        else:
            placeHolder(sizerG, 1)

        # second line

        btn = addButton(self, sizerG, 'Stop', self.OnStop, btnSize)
        btn.SetBackgroundColour(wx.Colour(255, 160, 0))

        self.measureButton = \
            addButton(self, sizerG, 'Measure', self.OnMeasure, btnSize)
        self.measureButton.Disable()

        if STEP_DRV:
            addControlButton(self, sizerG, 'Jog Spindle -', \
                                  self.OnJogSpindleRev, self.OnJogUp)
        else:
            placeHolder(sizerG, 1)

        # third line

        self.doneButton = addButton(self, sizerG, 'Done', self.OnDone, btnSize)
        self.doneButton.Disable()

        self.resumeButton = \
            addButton(self, sizerG, 'Resume', self.OnResume, btnSize)
        self.resumeButton.Disable()


        if STEP_DRV or MOTOR_TEST or SPINDLE_SWITCH or SPINDLE_VAR_SPEED:
            self.spindleButton = \
                addToggleButton(self, sizerG, 'Start Spindle', \
                                self.OnStartSpindle, btnSize)
            self.spindleButton.SetBackgroundColour('Green')
        else:
            placeHolder(sizerG, 1)

        sizerH.Add(sizerG)

        sizerG = wx.FlexGridSizer(cols=5, rows=0, vgap=0, hgap=0)
        sFlag = wx.ALL|wx.CENTER|wx.ALIGN_CENTER_VERTICAL

        # first row

        placeHolder(sizerG, 3)

        self.xNegButton = \
            addBitmapButton(self, sizerG, "north.png", self.OnXNegDown, \
                                 self.OnXUp, flag=sFlag|wx.EXPAND)

        placeHolder(sizerG, 1)

        # second row

        self.zNegButton = \
            addBitmapButton(self, sizerG, "west.png", self.OnZNegDown, \
                                 self.OnZUp, flag=sFlag)

        addButton(self, sizerG, 'S', self.OnZSafe, style=wx.BU_EXACTFIT, \
                       size=btnSize, flag=sFlag)

        self.zPosButton = \
            addBitmapButton(self, sizerG, "east.png", self.OnZPosDown, \
                                 self.OnZUp, flag=sFlag)

        addButton(self, sizerG, 'S', self.OnXSafe, style=wx.BU_EXACTFIT, \
                       size=btnSize, flag=sFlag)

        self.step = step = ["Cont", "0.0001", "0.0002", "0.0005", \
                            "0.001", "0.002", "0.005", \
                            "0.010", "0.020", "0.050", \
                            "0.100", "0.200", "0.500", "1.000"]

        self.combo = combo = wx.ComboBox(self, -1, step[1], choices=step, \
                                         style=wx.CB_READONLY)
        self.cfg.initInfo(cf.jogInc, combo)
        combo.Bind(wx.EVT_COMBOBOX, self.OnCombo)
        combo.Bind(wx.EVT_KEY_DOWN, self.OnKeyDown)
        combo.Bind(wx.EVT_KEY_UP, self.OnKeyUp)
        combo.Bind(wx.EVT_CHAR, self.OnKeyChar)
        combo.Bind(wx.EVT_SET_FOCUS, self.OnSetFocus)
        combo.Bind(wx.EVT_KILL_FOCUS, self.OnKillFocus)
        combo.SetFocus()
        sizerG.Add(combo, flag=sFlag, border=2)

        # third row

        placeHolder(sizerG, 1)

        self.zButton = \
            addBitmapButton(self, sizerG, "eastG.png", self.OnZRetract, \
                                 None,  flag=sFlag|wx.EXPAND)

        placeHolder(sizerG, 1)

        self.xPosButton = \
            addBitmapButton(self, sizerG, "south.png", self.OnXPosDown,
                                 self.OnXUp, flag=sFlag|wx.EXPAND)

        self.xButton = \
            addBitmapButton(self, sizerG, "southG.png", self.OnXRetract, \
                                 None,  flag=sFlag|wx.EXPAND)

        sizerH.Add(sizerG)

        # sizerV.Add(sizerH, flag=wx.ALIGN_CENTER_VERTICAL|wx.CENTER|wx.ALL, \
        #            border=2)
        sizerV.Add(sizerH, flag=wx.CENTER|wx.ALL, \
                   border=2)


        self.sliderMax = 1000
        self.spindleSlider = slider = wx.Slider(self, size=(500, -1),
                                                maxValue=self.sliderMax)
        slider.Bind(wx.EVT_SCROLL_THUMBTRACK, self.OnSliderThumbtrack)
        slider.Bind(wx.EVT_SCROLL_THUMBRELEASE, self.OnSliderRelease)

        sizerV.Add(slider)

        self.SetSizer(sizerV)
        sizerV.Fit(self)

    def OnEnter(self, _):
        OnEnter(self)

    def spindleRangeSetup(self):
        print("spindleRangeSetup")
        cfg = self.cfg
        spRange = cfg.getIntInfoData(cf.spCurRange)
        if 1 <= spRange <= cfg.getIntInfoData(cf.spRanges):
            spRange -= 1
            self.minSpeed = cfg.getIntInfoData(cf.spRangeMin1 + spRange)
            self.maxSpeed = cfg.getIntInfoData(cf.spRangeMax1 + spRange)
            self.speedRange = self.maxSpeed - self.minSpeed

    def setRPMSlider(self, rpm):
        if rpm > self.minSpeed:
            pos = int((float(rpm - self.minSpeed) / self.speedRange) * \
                      self.sliderMax)
            self.spindleSlider.SetValue(pos)
        else:
            self.spindleSlider.SetValue(0)

    def OnSliderThumbtrack(self, e):
        pos = e.GetPosition()
        rpm = int(self.minSpeed + \
                  (float(pos) / self.sliderMax) * self.speedRange)
        self.currentPanel.rpm.SetValue(str(rpm))
        # print(pos, rpm)
        # stdout.flush()

    def OnSliderRelease(self, _):
        if self.spindleActive:
            rpm = int(self.currentPanel.rpm.GetValue())
            self.comm.setParm(pm.SP_RPM, rpm)
            self.comm.command(cm.C_SPINDLE_UPDATE)
        self.focus()

    def update(self):
        self.setSurfaceSpeed()
        self.spindleRangeSetup()

    def setPassText(self, txt):
        self.passText.SetLabel(txt)

    def setSurfaceSpeed(self, val=None):
        if val is not None:
            self.surfaceSpeed.value = val
        if self.surfaceSpeed.value:
            self.rpmText.SetLabel("FPM")
        else:
            self.rpmText.SetLabel("RPM")

    # noinspection PyMethodMayBeStatic
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

    def OnZSafe(self, _):
        if self.addEna:
            panel = self.getPanel()
            (z, x) = getSafeLoc(panel)
            self.comm.queParm(pm.Z_MOVE_POS, z)
            self.comm.queParm(pm.Z_HOME_OFFSET, \
                         round(self.zHomeOffset * self.zStepsInch))
            self.comm.queParm(pm.Z_FLAG, ct.CMD_MAX)
            self.comm.command(cm.C_ZMOVEABS)
        self.combo.SetFocus()

    def OnZRetract(self, _):
        if self.addEna:
            if self.zReturnLoc is None:
                loc = self.cfg.getFloatInfoData(cf.zRetractLoc)
                bitmap = "westR.png"
                self.zReturnLoc = self.zPos.GetValue()
            else:
                loc = self.zReturnLoc
                bitmap = "eastG.png"
                self.zReturnLoc = None
            self.zButton.SetBitmap(wx.Bitmap(bitmap))
            self.comm.queParm(pm.Z_MOVE_POS, loc)
            self.comm.queParm(pm.Z_HOME_OFFSET, \
                         round(self.zHomeOffset * self.zStepsInch))
            self.comm.queParm(pm.Z_FLAG, ct.CMD_MAX)
            self.comm.command(cm.C_ZMOVEABS)
        self.combo.SetFocus()

    def OnXSafe(self, _):
        if self.addEna:
            panel = self.getPanel()
            (z, x) = getSafeLoc(panel)
            self.comm.queParm(pm.X_MOVE_POS, x)
            self.comm.queParm(pm.X_HOME_OFFSET, \
                         round(self.xHomeOffset * self.xStepsInch))
            self.comm.queParm(pm.X_FLAG, ct.CMD_MAX)
            self.comm.command(cm.C_XMOVEABS)
        self.combo.SetFocus()

    def OnXRetract(self, _):
        if self.addEna:
            if self.xReturnLoc is None:
                loc = self.cfg.getFloatInfoData(cf.xRetractLoc)
                bitmap = "northR.png"
                self.xReturnLoc = self.xPos.GetValue()
            else:
                loc = self.xReturnLoc
                bitmap = "southG.png"
                self.xReturnLoc = None
            self.xButton.SetBitmap(wx.Bitmap(bitmap))
            self.comm.queParm(pm.X_MOVE_POS, loc)
            self.comm.queParm(pm.X_HOME_OFFSET, \
                         round(self.xHomeOffset * self.xStepsInch))
            self.comm.queParm(pm.X_FLAG, ct.CMD_MAX)
            self.comm.command(cm.C_XMOVEABS)
        self.combo.SetFocus()

    def zJogCmd(self, code, val):
        self.repeat += 1
        self.mf.sendData.sendZData()
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
                        self.comm.queParm(pm.Z_JOG_MAX, \
                                          self.cfg.getInfoData(cf.zJogMax))
                        self.comm.queParm(pm.Z_JOG_DIR, direction)
                        self.comm.command(cm.C_ZJMOV)
                    except CommTimeout:
                        commTimeout(self)
            else:
                try:
                    self.comm.command(cm.C_ZJMOV)
                except CommTimeout:
                    commTimeout(self)
        else:
            if self.jogCode is None:
                self.jogCode = code
                if code == wx.WXK_LEFT:
                    val = '-' + val
                print("zJogCmd %s" % (val))
                stdout.flush()
                try:
                    self.comm.queParm(pm.Z_FLAG, ct.CMD_JOG)
                    self.comm.queParm(pm.Z_MOVE_DIST, val)
                    self.comm.command(cm.C_ZMOVEREL)
                except CommTimeout:
                    commTimeout(self)

    def jogDone(self, cmd):
        self.jogCode = None
        val = self.getInc()
        if val == "Cont":
            print("jogDone %d" % (self.repeat))
            stdout.flush()
            try:
                self.comm.command(cmd)
            except CommTimeout:
                commTimeout(self)

    def zDown(self, code):
        val = self.getInc()
        if val != "Cont":
            self.zJogCmd(code, val)
        else:
            self.btnRpt.action = self.zJogCmd
            self.btnRpt.code = code
            self.btnRpt.val = val
            self.btnRpt.event.set()

    def OnZUp(self, _):
        print("OnZUp")
        stdout.flush()
        val = self.getInc()
        if val == "Cont":
            self.btnRpt.event.clear()
            self.btnRpt.action = None
            self.jogDone(cm.C_ZSTOP)
        self.jogCode = None
        self.combo.SetFocus()

    def OnZNegDown(self, _):
        self.zNegButton.SetFocus()
        self.zDown(wx.WXK_LEFT)

    def OnZPosDown(self, _):
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
        self.mf.sendData.sendXData()
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
                        self.comm.queParm(pm.X_JOG_MAX, \
                                          self.cfg.getInfoData(cf.xJogMax))
                        self.comm.queParm(pm.X_JOG_DIR, direction)
                        self.comm.command(cm.C_XJMOV)
                    except CommTimeout:
                        commTimeout(self)
            else:
                try:
                    self.comm.command(cm.C_XJMOV)
                except CommTimeout:
                    commTimeout(self)
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
                    self.comm.queParm(pm.X_FLAG, flag)
                    self.comm.queParm(pm.X_MOVE_DIST, val)
                    self.comm.command(cm.C_XMOVEREL)
                except CommTimeout:
                    commTimeout(self)

    def xDown(self, code):
        val = self.getInc()
        if val != "Cont":
            self.xJogCmd(code, val)
        else:
            self.btnRpt.action = self.xJogCmd
            self.btnRpt.code = code
            self.btnRpt.val = val
            self.btnRpt.event.set()

    def OnXUp(self, _):
        val = self.getInc()
        if val == "Cont":
            self.btnRpt.event.clear()
            self.btnRpt.action = None
            self.jogDone(cm.C_XSTOP)
        self.jogCode = None
        self.combo.SetFocus()

    def OnXPosDown(self, _):
        self.xPosButton.SetFocus()
        self.xDown(wx.WXK_DOWN)

    def OnXNegDown(self, _):
        self.xNegButton.SetFocus()
        self.xDown(wx.WXK_UP)

    def OnCombo(self, _):
        val = self.combo.GetValue()
        print("combo val %s" % (val))
        try:
            val = float(val)
            if val > 0.020:
                val = 0.020
        except ValueError:
            val = 0.0
        self.comm.queParm(pm.Z_MPG_INC, round(val * self.zStepsInch))
        self.comm.queParm(pm.X_MPG_INC, round(val * self.xStepsInch))
        self.comm.sendMulti()

    def OnMouseEvent(self, evt):
        self.combo.SetFocus()
        evt.Skip()

    # noinspection PyMethodMayBeStatic
    def OnSetFocus(self, evt):
        # print("focus set")
        # stdout.flush()
        evt.Skip()

    # noinspection PyMethodMayBeStatic
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
            self.jogDone(cm.C_ZSTOP)
            return
        elif code == wx.WXK_RIGHT:
            self.jogDone(cm.C_ZSTOP)
            return
        elif code == wx.WXK_UP:
            self.jogDone(cm.C_XSTOP)
            return
        elif code == wx.WXK_DOWN:
            self.jogDone(cm.C_XSTOP)
            return
        elif code == wx.WXK_NUMPAD_PAGEDOWN:
            self.comm.command(cm.C_SPINDLE_STOP)
            return
        elif code == wx.WXK_NUMPAD_PAGEUP:
            self.comm.command(cm.C_SPINDLE_STOP)
            return
        # print("key up %x" % (code))
        # stdout.flush()
        evt.Skip()

                       # (ord('a'), (self.OnEStop, None)), \
                       # (ord('b'), (self.OnStop, None)), \
                       # (ord('c'), (self.OnStartSpindle, None)), \
                       # (ord('d'), self.noAction), \

                       # (ord('e'), self.start), \
                       # (ord('f'), (self.OnResume, None)), \
                       # (ord('g'), (self.OnPause, None)), \
                       # (ord('h'), (self.OnDone, None)), \

    def initKeypadTable(self):
        keypadTable = (\
                       (ord('1'), (self.OnEStop, None)), \
                       (ord('2'), (self.OnStop, None)), \
                       (ord('3'), (self.OnStartSpindle, None)), \
                       (ord('a'), self.noAction), \

                       (ord('*'), self.start), \
                       (ord('0'), (self.OnPause, None)), \
                       (ord('#'), (self.OnDone, None)), \
                       (ord('d'), (self.OnResume, None)), \

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

    def OnKeypadEvent(self, event):
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
        panel = self.mf.getCurrentPanel()
        panel.OnSend(None)

    def nextOperation(self):
        panel = self.mf.getCurrentPanel()
        panel.nextOperation()

    def add(self):
        panel = self.mf.getCurrentPanel()
        panel.OnAddPass(None)

    def addFocus(self):
        panel = self.mf.getCurrentPanel()
        # panel.setAddFocus()
        field = panel.addPass
        if field is not None:
            field.SetFocus()
            field.SetSelection(-1, -1)

    def focusPanel(self):
        panel = self.mf.getCurrentPanel()
        # panel.setFocus()
        field = panel.focusField
        if field is not None:
            field.SetFocus()
            field.SetSelection(-1, -1)

    def togglePause(self):
        panel = self.mf.currentPanel
        val = panel.pause.GetValue()
        panel.pause.SetValue(not val)

    def help(self):
        dialog = HelpDialog(self.mf)
        self.mf.showDialog(dialog)

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

    def OnStatusUpdate(self, evt):
        self.setStatus(evt.data)
        self.focus()

    def testPass(self, passNum, curLoc, retract=None, pause=True, axis=AXIS_X):
        m = self.mf.move
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
        if self.mf.dbgSave:
            self.mf.updateThread.openDebug("dbg_%s.txt" % \
                                   ("x" if axis == AXIS_X else "z"))
        if retract is not None:
            retract = abs(retract) if inc < 0.0 else -abs(retract)
        self.mf.dPrt("\naxisTest inc %7.4f%s\n" % \
                     (inc, "" if retract is None else \
                      " retract %7.4f" % (retract)), flush=True)
        m = self.mf.move
        m.queClear()
        m.quePause(ct.PAUSE_ENA_X_JOG | ct.PAUSE_ENA_Z_JOG)
        m.done(ct.PARM_START)
        if axis == AXIS_X:
            curLoc = (float(self.xIPosition.value) / self.xStepsInch - \
                      self.xHomeOffset)
            m.saveXOffset()
        else:
            curLoc = (float(self.zIPosition.value) / self.zStepsInch - \
                      self.zHomeOffset)
            m.saveZOffset()
        self.mf.dPrt("curLoc %7.4f\n" % (curLoc), console=True)

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
        xPos = (float(val) / self.xStepsInch) \
            if self.xStepsInch != 0.0 else 0.0
        txt = "%7.3f" % xPos
        self.xPos.SetValue(txt)
        dialPanel = self.mf.dialPanel
        if dialPanel is not None:
            dialPanel.updatePointer(xPos)

    # noinspection PyMethodMayBeStatic
    def updateRPM(self, val):
        print(val)
        stdout.flush()

    def probe(self, axis, probeLoc=None):
        self.homeOrProbe = axis
        if probeLoc is not None:
            self.probeLoc = probeLoc

    def homeDone(self, axis, status, msg):
        if axis == AXIS_X:
            axisStr = 'X'
        elif axis == AXIS_Z:
            axisStr = 'Z'
        else:
            axisStr = ''
        self.homeOrProbe = None
        self.probeStatus = 0
        self.setStatus(msg)
        print(axisStr + st.strTable[msg])
        stdout.flush()

    def updateAll(self, val):
        if len(val) != 7:
            return

        (z, x, rpm, curPass, zDROPos, xDROPos, mvStatus) = val
        if z != '#':
            self.zIPosition.value = z
            zLocation = float(z) / self.zStepsInch
            self.zLocation = zLocation
            self.zPos.SetValue("%0.4f" % (zLocation - self.zHomeOffset))
        else:
            zLocation = self.zLocation

        if x != '#':
            self.xIPosition.value = x
            xLocation = float(x) / self.xStepsInch - self.xHomeOffset
            self.xLocation = xLocation
            self.xPos.SetValue("%0.4f" % (xLocation))
            dialPanel = self.mf.dialPanel
            if dialPanel is not None:
                dialPanel.updatePointer(xLocation)
            self.xPosDiam.SetValue("%0.4f" % (abs(xLocation * 2)))
            if self.surfaceSpeed.value:
                fpm = (float(rpm) * abs(xLocation) * 2 * pi) / 12.0
                self.rpm.SetValue("%1.0f" % (fpm))
        else:
            xLocation = self.xLocation

        if not self.surfaceSpeed.value:
            self.rpm.SetValue(str(rpm))

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
            self.zIDROPosition.value = zDROPos
            zDroLoc = float(zDROPos) / self.zDROInch
            if self.lastZOffset != self.zDROOffset:
                self.lastZOffset = self.zDROOffset
                print("zDROPos %d %0.4f zDROOffset %0.4f" % \
                      (zDROPos, zDroLoc, self.zDROOffset))
                stdout.flush()
            zDroLoc = zDroLoc - self.zDROOffset
            self.zDROPos.SetValue("%0.4f" % (zDroLoc))

            xDROPos = int(xDROPos)
            self.xIDROPosition.value = xDROPos
            xDroLoc = float(xDROPos) / self.xDROInch
            if self.lastXOffset != self.xDROOffset:
                self.lastXOffset = self.xDROOffset
                print("xDROPos %d %0.4f xDROOffset %0.4f" % \
                      (xDROPos, xDroLoc, self.xDROOffset))
                stdout.flush()
            xDroLoc = xDroLoc - self.xDROOffset
            self.xDROPos.SetValue("%0.4f" % (xDroLoc))

            if self.xDroDiam.value:
                xDroLoc *= 2.0

            dialPanel = self.mf.dialPanel
            if dialPanel is not None:
                dialPanel.updatePointer(xDroLoc)

        text = ''
        if self.xHomed:
            text = 'H'
        if self.currentPanel.active:
            text += '*'
        mvStatus = int(mvStatus)

        if mvStatus & ct.MV_MEASURE:
            text += 'M'
        if mvStatus & ct.MV_PAUSE:
            text += 'P'
        if mvStatus & ct.MV_ACTIVE:
            text += 'A'
        if mvStatus & (ct.MV_XLIMIT | ct.MV_ZLIMIT):
            text += 'L'
        else:
            if self.overrideSet:
                self.overrideSet = False
                self.limitOverride.SetValue(False)
        self.statusText.SetLabel(text)

        addEna = (mvStatus & ct.MV_DONE) != 0

        if addEna != self.addEna:
            panel = self.currentPanel
            if addEna:
                if not panel.manualMode:
                    if panel.addButton is not None:
                        buttonEnable(panel.addButton)
                    buttonEnable(self.doneButton)
                buttonDisable(self.measureButton)
                buttonDisable(self.pauseButton)
            else:
                if panel.addButton is not None:
                    buttonDisable(panel.addButton)
                buttonDisable(self.doneButton)
            self.addEna = addEna

        if mvStatus != self.mvStatus:
            changed = mvStatus ^ self.mvStatus
            if (changed & ct.MV_PAUSE) != 0:
                if (mvStatus & ct.MV_PAUSE) != 0:
                    buttonEnable(self.resumeButton)
                    buttonDisable(self.pauseButton)
                    buttonDisable(self.measureButton)
                else:
                    buttonDisable(self.resumeButton)
                    if self.currentPanel.active:
                        buttonEnable(self.pauseButton)
                        if not self.currentPanel.manualMode:
                            buttonEnable(self.measureButton)

            self.mvStatus = mvStatus
            print("mvStatus %x" % (mvStatus))
            stdout.flush()

        if self.homeOrProbe is not None:
            if self.homeOrProbe == HOME_X:
                val = self.comm.getParm(pm.X_HOME_STATUS)
                if val is not None:
                    if val & ct.HOME_SUCCESS:
                        self.homeDone(AXIS_X, True, st.STR_HOME_SUCCESS)
                        self.xHomed = True
                        if not EXT_DRO:
                            self.comm.setParm(pm.X_LOC, 0)
                            if DRO:
                                self.comm.setParm(pm.X_DRO_LOC, 0)
                                self.updateXDroPos(xLocation)
                        else:
                            self.setXFromExt()
                    elif val & ct.HOME_FAIL:
                        self.homeDone(AXIS_X, False, st.STR_HOME_FAIL)
            elif self.homeOrProbe == HOME_Z:
                val = self.comm.getParm(pm.Z_HOME_STATUS)
                if val is not None:
                    if val & ct.HOME_SUCCESS:
                        self.homeDone(AXIS_Z, True, st.STR_HOME_SUCCESS)
                        self.zHomed = True
                        if not EXT_DRO:
                            self.comm.setParm(pm.Z_LOC, 0)
                            if DRO:
                                self.comm.setParm(pm.Z_DRO_LOC, 0)
                                self.updateZDroPos(zLocation)
                        else:
                            self.setZFromExt()
                    elif val & ct.HOME_FAIL:
                        self.homeDone(AXIS_Z, False, st.STR_HOME_FAIL)
            elif self.homeOrProbe == AXIS_X:
                val = self.comm.getParm(pm.X_HOME_STATUS)
                if val & ct.PROBE_SUCCESS:
                    self.xHomeOffset = xLocation - self.probeLoc
                    self.xIHomeOffset.value = self.xHomeOffset
                    # cfg.setInfo(cf.xSvHomeOffset, "%0.4f" % (xHomeOffset))
                    if DRO:
                        self.updateXDroPos(self.probeLoc, xDROPos)
                    print("x %s xLocation %7.4f probeLoc %7.4f "\
                          "xHomeOffset %7.4f" % \
                          (x, xLocation, self.probeLoc, self.xHomeOffset))
                    stdout.flush()
                    self.probeLoc = 0.0
                    self.homeDone(AXIS_X, True, st.STR_PROBE_SUCCESS)
                elif val & ct.PROBE_FAIL:
                    self.homeDone(AXIS_X, False, st.STR_PROBE_FAIL)
            elif self.homeOrProbe == AXIS_Z:
                val = self.comm.getParm(pm.Z_HOME_STATUS)
                if val & ct.PROBE_SUCCESS:
                    self.zHomeOffset = zLocation - self.probeLoc
                    self.zIHomeOffset.value = self.zHomeOffset
                    # cfg.setInfo(cf.zSvHomeOffset, "%0.4f" % \
                    #             (self.zHomeOffset))
                    if DRO:
                        self.updateZDroPos(self.probeLoc, zDROPos)
                    print("z %s zLocation %7.4f probeLoc %7.4f "\
                          "zHomeOffset %7.4f" % \
                          (z, zLocation, self.probeLoc, self.zHomeOffset))
                    stdout.flush()
                    self.probeLoc = 0.0
                    self.homeDone(AXIS_Z, True, st.STR_PROBE_SUCCESS)
                elif val & ct.PROBE_FAIL:
                    self.homeDone(AXIS_Z, False, st.STR_PROBE_FAIL)

    def updateError(self, text):
        self.setStatus(text)

    def OnEStop(self, _):
        self.homeOrProbe = None
        self.mf.move.queClear()
        self.comm.command(cm.C_CMD_CLEAR)
        sd = self.mf.sendData
        sd.spindleDataSent = False
        sd.zDataSent = False
        sd.xDataSent = False
        self.mf.initDevice()
        self.clrActive()
        self.combo.SetFocus()

    def OnStop(self, _):
        self.homeOrProbe = None
        self.mf.move.queClear()
        self.comm.command(cm.C_CMD_STOP)
        self.mf.initDevice()
        self.setStatus(st.STR_STOPPED)
        self.clrActive()
        self.combo.SetFocus()

    def OnPause(self, _):
        self.comm.command(cm.C_CMD_PAUSE)
        self.combo.SetFocus()

    def OnResume(self, _):
        self.comm.command(cm.C_CMD_RESUME)
        self.combo.SetFocus()

    def OnDone(self, _):
        if (self.mvStatus & (ct.MV_PAUSE | ct.MV_ACTIVE | ct.MV_MEASURE)) == 0:
            self.clrActive()
            self.comm.command(cm.C_CMD_DONE)
        else:
            self.setStatus(st.STR_OP_IN_PROGRESS)
        self.combo.SetFocus()

    def OnMeasure(self, _):
        self.comm.command(cm.C_CMD_MEASURE)
        self.combo.SetFocus()

    def getPanel(self):
        panel = self.cfg.getInfoData(cf.mainPanel)
        return(self.mf.panels[panel])

    def clrRetract(self):
        self.xReturnLoc = None
        self.zReturnLoc = None
        self.xButton.SetBitmap(wx.Bitmap("southG.png"))
        self.zButton.SetBitmap(wx.Bitmap("eastG.png"))

    def clrActive(self):
        # updateThread.closeDbg()
        self.mf.updateThread.baseTime = None
        print("***clear baseTime***")
        panel = self.currentPanel
        panel.active = False
        if not panel.manualMode:
            panel.sendButton.Enable()
            buttonDisable(panel.startButton)
        else:
            panel.sendButton.Disable()
            buttonEnable(panel.startButton)
        btn = self.spindleButton
        if self.spindleActive:
            self.spindleActive = False
            btn.SetLabel('Start Spindle')
            btn.SetValue(False)
        buttonEnable(btn)
        buttonDisable(self.pauseButton)
        buttonDisable(self.measureButton)
        self.clrRetract()
        self.setStatus(st.STR_CLR)

    def OnStartSpindle(self, _):
        if STEP_DRV or MOTOR_TEST or SPINDLE_SWITCH or SPINDLE_VAR_SPEED:
            if not self.currentPanel.active:
                btn = self.spindleButton
                # self.spindleActive = state = btn.GetValue()
                if self.spindleActive:
                    self.spindleActive = False
                    btn.SetLabel('Start Spindle')
                    btn.SetBackgroundColour('Green')
                    self.currentPanel.sendButton.Enable()
                    self.comm.command(cm.C_SPINDLE_STOP)
                else:
                    self.spindleActive = True
                    btn.SetLabel('Stop Spindle')
                    btn.SetBackgroundColour('Red')
                    panel = self.currentPanel
                    panel.sendButton.Disable()
                    rpm = panel.rpm.GetValue()
                    self.mf.sendData.sendSpindleData(True, rpm)
                    self.comm.command(cm.C_SPINDLE_START)
        self.combo.SetFocus()

    def spindleJogCmd(self, code, val):
        self.repeat += 1
        if self.jogCode != code:
            if self.jogCode is None:
                self.mf.sendData.sendSpindleData()
                direction = 0 if code == wx.WXK_NUMPAD_PAGEDOWN else 1
                self.comm.setParm(pm.SP_JOG_DIR, direction)
                self.jogCode = code
                self.repeat = 0
        try:
            self.comm.command(cm.C_SPINDLE_JOG)
        except CommTimeout:
            commTimeout(self)
        self.combo.SetFocus()

    def OnJogSpindleFwd(self, _):
        print("jog spingle")
        stdout.flush()
        self.btnRpt.action = self.spindleJogCmd
        self.btnRpt.code = wx.WXK_NUMPAD_PAGEDOWN
        self.btnRpt.val = 0
        self.btnRpt.event.set()

    def OnJogSpindleRev(self, _):
        print("jog spingle")
        stdout.flush()
        self.btnRpt.action = self.spindleJogCmd
        self.btnRpt.code = wx.WXK_NUMPAD_PAGEUP
        self.btnRpt.val = 0
        self.btnRpt.event.set()

    def OnJogUp(self, _):
        self.btnRpt.event.clear()
        self.btnRpt.action = None
        self.jogCode = None
        try:
            self.comm.command(cm.C_SPINDLE_STOP)
        except CommTimeout:
            commTimeout(self)
        self.combo.SetFocus()

    def OnOverride(self, _):
        val = self.limitOverride.GetValue()
        print("override %s" % (val))
        stdout.flush()
        if val and ((self.mvStatus & (ct.MV_XLIMIT | ct.MV_ZLIMIT)) == 0):
            self.limitOverride.SetValue(False)
            return
        self.overrideSet = val
        self.comm.setParm(pm.LIMIT_OVERRIDE, (0, 1)[val])

    def setStatus(self, text):
        if self.mf.done:
            return
        if isinstance(text, int):
            self.statusLine.SetLabel(st.strTable[text])
        elif isinstance(text, str):
            self.statusLine.SetLabel(text)
        self.Refresh()
        self.Update()

    def updateZPos(self, val):
        self.mf.sendData.sendZData()
        zLocation = self.comm.getParm(pm.Z_LOC)
        if zLocation is not None:
            zLocation = float(zLocation) / self.zStepsInch
            self.zHomeOffset = zLocation - val
            self.zIHomeOffset.value = self.zHomeOffset
            self.comm.setParm(pm.Z_HOME_OFFSET, \
                         round(self.zHomeOffset * self.zStepsInch))
            print("pos %0.4f zLocation %0.4f zHomeOffset %0.4f" % \
                  (val, zLocation, self.zHomeOffset))
            stdout.flush()
            if DRO:
                self.updateZDroPos(val)
            if EXT_DRO:
                dro = self.mf.dro
                dro.command(dro.setZ("%0.4f" % (val)))

    def updateZDroPos(self, val, zDROPos=None):
        if zDROPos is None:
            zDROPos = self.comm.getParm(pm.Z_DRO_LOC)
        if zDROPos is not None:
            droPos = float(zDROPos) / self.zDROInch
            print("pos %0.4f zDROPos %d %0.4f" % \
                  (val, zDROPos, droPos))
            self.zDROOffset = droPos - val
            self.zIDROOffset.value = self.zDROOffset
            self.comm.setParm(pm.Z_DRO_OFFSET, \
                         round(self.zDROOffset * self.zDROInch))
            print("zDROOffset %d %0.4f" % \
                  (int(self.zDROOffset * self.zDROInch), self.zDROOffset))
            stdout.flush()

    def setZFromExt(self):
        dro = self.mf.dro
        val = dro.command(dro.extReadZ, True)
        val = val.strip()
        try:
            rsp = float(val)
        except ValueError:
            print("setZFromExt ValueError %s" % (val))
            stdout.flush()
            rsp = 0.0
        self.zPosition = round(rsp * self.zStepsInch)
        self.zHomeOffset = 0.0
        self.zIHomeOffset.value = self.zHomeOffset
        self.comm.queParm(pm.Z_LOC, self.zPosition)
        self.comm.queParm(pm.Z_HOME_OFFSET, \
                     round(self.zHomeOffset * self.zStepsInch))
        if DRO:
            self.zDROPosition = round(rsp * self.zDROInch)
            self.zDROOffset = 0.0
            self.zIDROOffset.value = self.zDROOffset
            self.comm.queParm(pm.Z_DRO_LOC, self.zDROPosition)
            self.comm.queParm(pm.Z_DRO_OFFSET, \
                         round(self.zDROOffset * self.zDROInch))
        self.comm.sendMulti()

    def updateXPos(self, val):
        val /= 2.0
        self.mf.sendData.sendXData()
        xLocation = self.comm.getParm(pm.X_LOC)
        print("xLocation %d" % (xLocation))
        if xLocation is not None:
            xLocation = float(xLocation) / self.xStepsInch
            self.xHomeOffset = xLocation - val
            self.xIHomeOffset.value = self.xHomeOffset
            self.comm.setParm(pm.X_HOME_OFFSET, \
                         round(self.xHomeOffset * self.xStepsInch))
            print("pos %0.4f xLocation %0.4f xHomeOffset %0.4f" % \
                  (val, xLocation, self.xHomeOffset))
            stdout.flush()
            if DRO:
                self.updateXDroPos(val)
            if EXT_DRO:
                dro = self.mf.dro
                dro.command(dro.setX("%0.4f" % (val * 2.0)))

    def updateXDroPos(self, val, xDROPos=None):
        if xDROPos is None:
            xDROPos = self.comm.getParm(pm.X_DRO_LOC)
        if xDROPos is not None:
            droPos = float(xDROPos) / self.xDROInch
            print("pos %0.4f xDROPos %d %0.4f" % \
                  (val, xDROPos, droPos))
            self.xDROOffset = droPos - val
            self.xIDROOffset.value = self.xDROOffset
            self.comm.setParm(pm.X_DRO_OFFSET, \
                         round(self.xDROOffset * self.xDROInch))
            print("xDROOffset %d %0.4f" % \
                  (int(self.xDROOffset * self.xDROInch), self.xDROOffset))
            stdout.flush()

    def setXFromExt(self):
        dro = self.mf.dro
        val = dro.command(dro.extReadX, True)
        val = val.strip()
        try:
            rsp = float(val) / 2.0
        except ValueError:
            print("setXFromExt ValueError %s" % (val))
            stdout.flush()
            rsp = 0.0
        print("val %s rsp %9.6f" % (val, rsp))
        self.xPosition = round(rsp * self.xStepsInch)
        self.xHomeOffset = 0.0
        self.xIHomeOffset.value = self.xHomeOffset
        self.comm.queParm(pm.X_LOC, self.xPosition)
        self.comm.queParm(pm.X_HOME_OFFSET, \
                     round(self.xHomeOffset * self.xStepsInch))
        if DRO:
            self.xDROPosition = round(rsp * self.xDROInch)
            print("xDROPosition %d" % (self.xDROPosition))
            self.xDROOffset = 0.0
            self.xIDROOffset.value = self.xDROOffset
            self.comm.queParm(pm.X_DRO_LOC, self.xDROPosition)
            self.comm.queParm(pm.X_DRO_OFFSET, \
                         round(self.xDROOffset * self.xDROInch))
        self.comm.sendMulti()

    def getPos(self, ctl):
        (xPos, yPos) = self.mf.GetPosition()
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
        self.comm = jP.mf.comm
        self.axis = axis

        active = jP.currentPanel.active
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

            item = wx.MenuItem(self, wx.Window.NewControlId(), "Home")
            self.Append(item)
            if self.axis == AXIS_X:
                self.Bind(wx.EVT_MENU, self.OnHomeXFwd, item)
            elif self.axis == AXIS_Z:
                self.Bind(wx.EVT_MENU, self.OnHomeZFwd, item)

            item = wx.MenuItem(self, wx.Window.NewControlId(), "Rev Home")
            self.Append(item)
            if self.axis == AXIS_X:
                self.Bind(wx.EVT_MENU, self.OnHomeXRev, item)
            elif self.axis == AXIS_Z:
                self.Bind(wx.EVT_MENU, self.OnHomeZRev, item)

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

        if jP.addEna:
            retract = jP.zReturnLoc is None if self.axis == AXIS_Z \
                else jP.xReturnLoc is None
            tmp = "Retract" if retract else "Return"
            item = wx.MenuItem(self, wx.Window.NewControlId(), tmp)
            self.Append(item)
            self.Bind(wx.EVT_MENU, self.OnRetract, item)

    def getPosCtl(self):
        jP = self.jP
        ctl = jP.zPos if self.axis == AXIS_Z else \
              jP.xPos
        return(jP.getPos(ctl))

    def OnSet(self, _):
        dialog = SetPosDialog(self.jP, self.axis)
        dialog.SetPosition(self.getPosCtl())
        dialog.Raise()
        dialog.Show(True)

    def OnZero(self, _):
        self.jP.updateZPos(0) if self.axis == AXIS_Z else \
            self.jP.updateXPos(0)
        self.jP.focus()

    def OnProbe(self, _):
        dialog = ProbeDialog(self.jP, self.axis)
        dialog.SetPosition(self.getPosCtl())
        dialog.Raise()
        dialog.Show(True)

    def OnHomeXFwd(self, _):
        jp = self.jP
        if not HOME_IN_PLACE:
            self.comm.command(cm.C_XHOMEFWD)
            self.jP.probe(HOME_X)
        else:
            xLocation = float(jp.xPos.GetValue())
            jp.xHomeOffset = 0 - xLocation
            jp.xIHomeOffset.value = jp.xHomeOffset
            self.comm.setParm(pm.X_LOC, 0)
            self.comm.setParm(pm.X_HOME_OFFSET, \
                         round(jp.xHomeOffset * jp.xStepsInch))
            if DRO:
                self.comm.setParm(pm.X_DRO_LOC, 0)
                self.jP.updateXDroPos(xLocation)
            self.jP.homeDone(AXIS_X, True, st.STR_HOME_SUCCESS)
            jp.xHomed = True
        self.jP.focus()

    def OnHomeZFwd(self, _):
        jp = self.jP
        if not HOME_IN_PLACE:
            self.comm.command(cm.C_ZHOMEFWD)
            jp.probe(HOME_Z)
        else:
            zLocation = float(jp.zPos.GetValue())
            jp.zHomeOffset = 0 - zLocation
            jp.zIHomeOffset.value = jp.zHomeOffset
            self.comm.setParm(pm.Z_LOC, 0)
            self.comm.setParm(pm.Z_HOME_OFFSET, \
                         round(jp.zHomeOffset * jp.zStepsInch))
            if DRO:
                self.comm.setParm(pm.Z_DRO_LOC, 0)
                jp.updateZDroPos(zLocation)
            jp.homeDone(AXIS_Z, True, st.STR_HOME_SUCCESS)
            jp.zHomed = True
        jp.focus()

    def OnHomeXRev(self, _):
        jp = self.jP
        if not HOME_IN_PLACE:
            self.comm.command(cm.C_XHOMEREV)
            jp.probe(HOME_X)
        else:
            xLocation = float(jp.xPos.GetValue())
            jp.xHomeOffset = 0 - xLocation
            jp.xIHomeOffset.value = jp.xHomeOffset
            self.comm.setParm(pm.X_LOC, 0)
            self.comm.setParm(pm.X_HOME_OFFSET, \
                         round(jp.xHomeOffset * jp.xStepsInch))
            if DRO:
                self.comm.setParm(pm.X_DRO_LOC, 0)
                jp.updateXDroPos(xLocation)
            jp.homeDone(AXIS_X, True, st.STR_HOME_SUCCESS)
            jp.xHomed = True
        jp.focus()

    def OnHomeZRev(self, _):
        jp = self.jP
        if not HOME_IN_PLACE:
            self.comm.command(cm.C_ZHOMEREV)
            jp.probe(HOME_Z)
        else:
            zLocation = float(jp.zPos.GetValue())
            jp.zHomeOffset = 0 - zLocation
            jp.zIHomeOffset.value = jp.zHomeOffset
            self.comm.setParm(pm.Z_LOC, 0)
            self.comm.setParm(pm.Z_HOME_OFFSET, \
                         round(jp.zHomeOffset * jp.zStepsInch))
            if DRO:
                self.comm.setParm(pm.Z_DRO_LOC, 0)
                jp.updateZDroPos(zLocation)
            jp.homeDone(AXIS_Z, True, st.STR_HOME_SUCCESS)
            jp.zHomed = True
        jp.focus()

    def OnGoto(self, _):
        dialog = GotoDialog(self.jP, self.axis)
        dialog.SetPosition(self.getPosCtl())
        dialog.Raise()
        dialog.Show(True)

    def OnFixX(self, _):
        jP = self.jP
        dialog = jP.fixXPosDialog
        if dialog is None:
            jP.fixXPosDialog = dialog = FixXPosDialog(jP)
        dialog.SetPosition(self.getPosCtl())
        dialog.Raise()
        dialog.Show(True)

    def OnDroDiam(self, _):
        jp = self.jP
        jp.xDroDiam.value = not jp.xDroDiam.value
        jp.focus()

    def OnSetFromExt(self, _):
        jp = self.jP
        if self.axis == AXIS_Z:
            jp.setZFromExt()
        else:
            jp.setXFromExt()
        jp.focus()

    def OnRetract(self, _):
        jp = self.jP
        if self.axis == AXIS_Z:
            dialog = jp.retractZDialog
            if dialog is None:
                jp.retractZDialog = dialog = RetractDialog(jp, self.axis)
        else:
            dialog = jp.retractXDialog
            if dialog is None:
                jp.retractXDialog = dialog = RetractDialog(jp, self.axis)
        dialog.SetPosition(self.getPosCtl())
        dialog.Raise()
        dialog.Show(True)

class SetPosDialog(wx.Dialog, FormRoutines):
    def __init__(self, jp, axis):
        FormRoutines.__init__(self)
        self.jp = jp
        self.axis = axis
        pos = (10, 10)
        title = "Position %s" % ('Z' if axis == AXIS_Z else 'X')
        wx.Dialog.__init__(self, jp, -1, title, pos, \
                            wx.DefaultSize, wx.DEFAULT_DIALOG_STYLE)
        self.Bind(wx.EVT_SHOW, self.OnShow)
        self.sizerV = sizerV = wx.BoxSizer(wx.VERTICAL)

        self.pos = \
            addDialogField(self, sizerV, tcDefault="0.000", \
                tcFont=jp.posFont, size=(120,-1), action=self.OnKeyChar)

        addDialogButton(self, sizerV, wx.ID_OK, self.OnOk, border=10)

        self.SetSizer(sizerV)
        self.sizerV.Fit(self)
        self.Show(False)

    def OnShow(self, _):
        if self.jp.mf.done:
            return
        if self.IsShown():
            val = self.jp.zPos.GetValue() if self.axis == AXIS_Z else \
               self.jp.xPos.GetValue()
            if self.axis == AXIS_X:
                val = "%0.4f" % (float(val) * 2)
            self.pos.SetValue(val)
            self.pos.SetSelection(-1, -1)

    def OnKeyChar(self, e):
        keyCode = e.GetKeyCode()
        if keyCode == wx.WXK_RETURN:
            self.OnOk(None)
        e.Skip()

    def OnOk(self, _):
        val = self.pos.GetValue()
        try:
            val = float(val)
            self.jp.updateZPos(val) if self.axis == AXIS_Z else \
                self.jp.updateXPos(val)
        except ValueError:
            print("ValueError on %s" % (val))
            stdout.flush()
        self.Show(False)
        self.jp.focus()

class ProbeDialog(wx.Dialog, FormRoutines):
    def __init__(self, jogPanel, axis):
        FormRoutines.__init__(self)
        self.jp = jogPanel
        self.axis = axis
        pos = (10, 10)
        title = "Probe %s" % ('Z' if axis == AXIS_Z else 'X Diameter')
        wx.Dialog.__init__(self, jogPanel, -1, title, pos, \
                            wx.DefaultSize, wx.DEFAULT_DIALOG_STYLE)
        self.Bind(wx.EVT_SHOW, self.OnShow)
        self.sizerV = sizerV = wx.BoxSizer(wx.VERTICAL)

        sizerG = wx.FlexGridSizer(cols=2, rows=0, vgap=0, hgap=0)

        self.probeLoc = \
            addDialogField(self, sizerG, \
                'Z Position' if axis == AXIS_Z else 'X Diameter', \
                "0.000", jogPanel.txtFont, jogPanel.posFont, (120, -1))

        self.probeDist = \
            addDialogField(self, sizerG, 'Distance', "0.000", \
                jogPanel.txtFont, jogPanel.posFont, (120, -1), self.OnKeyChar)

        sizerV.Add(sizerG, 0, wx.ALIGN_RIGHT)

        addButton(self, sizerV, 'Ok', self.OnOk, border=10)

        self.SetSizer(sizerV)
        self.sizerV.Fit(self)
        self.Show(False)

    def OnShow(self, _):
        if self.jp.mf.done:
            return
        if self.IsShown():
            if self.axis == AXIS_Z:
                probeLoc = "0.0000"
                probeDist = self.jp.cfg.getFloatInfoData(cf.zProbeDist)
            else:
                probeLoc = self.jp.xPos.GetValue()
                probeDist = self.jp.cfg.getFloatInfoData(cf.xProbeDist)
            self.probeLoc.SetValue(probeLoc)
            self.probeLoc.SetSelection(-1, -1)
            self.probeDist.SetValue("%7.4f" % probeDist)

    def OnKeyChar(self, e):
        keyCode = e.GetKeyCode()
        if keyCode == wx.WXK_RETURN:
            self.OnOk(None)
        e.Skip()

    def OnOk(self, _):
        val = self.probeLoc.GetValue()
        try:
            probeLoc = float(val)
            self.probeZ(probeLoc) if self.axis == AXIS_Z else \
               self.probeX(probeLoc / 2.0)
        except ValueError:
            print("probe ValueError on %s" % (val))
            stdout.flush()
        self.Show(False)
        self.jp.focus()

    def probeZ(self, probeLoc):
        jp = self.jp
        mf = jp.mf
        cfg = jp.cfg
        mf.move.queClear()
        comm = mf.comm
        comm.queParm(pm.PROBE_INV, cfg.getBoolInfoData(cf.cfgPrbInv))
        comm.queParm(pm.PROBE_SPEED, cfg.getInfoData(cf.zProbeSpeed))
        comm.queParm(pm.Z_HOME_STATUS, '0')
        comm.sendMulti()
        mf.move.probeZ(getFloatVal(self.probeDist))
        self.Show(False)
        self.jp.probe(AXIS_Z, probeLoc)
        self.jp.focus()

    def probeX(self, probeLoc):
        jp = self.jp
        mf = jp.mf
        cfg = jp.cfg
        mf.move.queClear()
        comm = mf.comm
        comm.queParm(pm.PROBE_INV, cfg.getBoolInfoData(cf.cfgPrbInv))
        comm.queParm(pm.X_HOME_SPEED, cfg.getInfoData(cf.xHomeSpeed))
        comm.queParm(pm.X_HOME_STATUS, '0')
        comm.sendMulti()
        mf.move.probeX(getFloatVal(self.probeDist))
        self.Show(False)
        jp.probe(AXIS_X, probeLoc)
        jp.focus()

class GotoDialog(wx.Dialog, FormRoutines):
    def __init__(self, jp, axis):
        FormRoutines.__init__(self)
        self.jp = jp
        self.comm = jp.mf.comm
        self.axis = axis
        pos = (10, 10)
        title = "Go to %s" % ('Z Position' if axis == AXIS_Z else 'X Diameter')
        wx.Dialog.__init__(self, jp, -1, title, pos, \
                            wx.DefaultSize, wx.DEFAULT_DIALOG_STYLE)
        self.Bind(wx.EVT_SHOW, self.OnShow)
        self.sizerV = sizerV = wx.BoxSizer(wx.VERTICAL)

        self.pos = \
            addDialogField(self, sizerV, tcDefault="0.000", \
                tcFont=jp.posFont, size=(120,-1), action=self.OnKeyChar)

        addButton(self, sizerV, 'Ok', self.OnOk, border=10)

        self.SetSizer(sizerV)
        self.sizerV.Fit(self)
        self.Show(False)

    def OnShow(self, _):
        jp = self.jp
        if jp.mf.done:
            return
        if self.IsShown():
            val = jp.zPos.GetValue() if self.axis == AXIS_Z else \
               jp.xPos.GetValue()
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

    def OnOk(self, _):
        try:
            loc = float(self.pos.GetValue())
            m = self.jp.mf.move
            m.queClear()
            self.comm.command(cm.C_CMD_PAUSE)
            self.comm.command(cm.C_CLEARQUE)
            if self.axis == AXIS_Z:
                self.jp.mf.sendData.sendZData()
                m.saveZOffset()
                flag = ct.CMD_JOG | ((ct.DRO_POS | ct.DRO_UPD) \
                                     if X_DRO_POS else 0)
                m.moveZ(loc, flag)
            else:
                self.jp.mf.sendData.sendXData()
                m.dbg = True
                m.saveXOffset()
                flag = ct.CMD_JOG | ((ct.DRO_POS | ct.DRO_UPD) \
                                     if X_DRO_POS else 0)
                m.moveX(loc / 2.0, flag)
                m.dbg = False
            self.comm.command(cm.C_CMD_RESUME)
            self.Show(False)
            self.jp.focus()
        except ValueError:
            print("ValueError on goto")
            stdout.flush()

class FixXPosDialog(wx.Dialog, FormRoutines):
    def __init__(self, jp):
        FormRoutines.__init__(self)
        self.jp = jp
        self.comm = jp.mf.comm
        pos = (10, 10)
        wx.Dialog.__init__(self, jp, -1, "Fix X Size", pos, \
                            wx.DefaultSize, wx.DEFAULT_DIALOG_STYLE)
        self.Bind(wx.EVT_SHOW, self.OnShow)
        self.sizerV = sizerV = wx.BoxSizer(wx.VERTICAL)

        sizerG = wx.FlexGridSizer(cols=2, rows=0, vgap=0, hgap=0)

        self.curXPos = \
            addDialogField(self, sizerG, 'Current', "0.000", jp.txtFont, \
                                jp.posFont, (120, -1))

        self.actualXPos = \
            addDialogField(self, sizerG, 'Measured', "0.000", jp.txtFont, \
                jp.posFont, (120, -1), self.OnKeyChar)

        sizerV.Add(sizerG, 0, wx.ALIGN_RIGHT)

        addButton(self, sizerV, 'Fix', self.OnFix, border=5)

        self.SetSizer(sizerV)
        self.sizerV.Fit(self)
        self.Show(False)

    def OnShow(self, _):
        if self.jp.mf.done:
            return
        if self.IsShown():
            xDiameter = self.jp.passSize.GetValue()
            # try:
            #     xDiameter = float(self.comm.getParm(pm.X_DIAMETER)) / \
            #                 self.jp.xStepsInch
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

    def OnFix(self, _):
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

        jp = self.jp
        offset = (actualX - curX)
        curHomeOffset = jp.xHomeOffset
        x = self.comm.getParm(pm.X_LOC)
        print("x %d xPosition %d" % (x, int(jp.xIPosition.value)))
        xLocation = 2 * (float(x) / jp.xStepsInch - jp.xHomeOffset)
        jp.updateXPos(xLocation + offset)

        currentPanel = jp.currentPanel
        if currentPanel.active:
            op = currentPanel.op
            if (op == en.OP_TURN) or \
               (op == en.OP_TAPER) or \
               (op == en.OP_THREAD):
                currentPanel.control.fixCut(offset)
            elif op == en.OP_FACE:
                pass

        dPrt = jp.mf.dPrt
        dPrt("fix x\n")
        dPrt("curX %7.4f actualX %7.4f offset %7.4f\n" \
                  "xHomeOffset cur %7.4f new %7.4f\n" % \
                  (curX, actualX, offset, curHomeOffset, jp.xHomeOffset))
        curLoc = float(jp.xIPosition.value) / jp.xStepsInch
        dPrt("xDiam cur %7.4f new %7.4f\n\n" % \
                  ((curLoc - curHomeOffset) * 2,
                   (curLoc - jp.xHomeOffset) * 2), flush=True)

        print("curX %0.4f actualX %0.4f offset %0.4f xHomeOffset %0.4f" % \
              (curX, actualX, offset, jp.xHomeOffset))
        stdout.flush()

        self.Show(False)
        jp.focus()

class RetractDialog(wx.Dialog, FormRoutines):
    def __init__(self, jp, axis):
        FormRoutines.__init__(self)
        self.jp = jp
        self.axis = axis
        self.axisVal = 'Z' if axis == AXIS_Z else 'X'
        pos = (10, 10)
        title = "Return %s" % self.axisVal
        wx.Dialog.__init__(self, jp -1, title, pos, \
                            wx.DefaultSize, wx.DEFAULT_DIALOG_STYLE)
        self.Bind(wx.EVT_SHOW, self.OnShow)
        self.sizerV = sizerV = wx.BoxSizer(wx.VERTICAL)

        self.pos = \
            addDialogField(self, sizerV, tcDefault="0.000", \
                tcFont=jp.posFont, size=(120,-1), action=self.OnKeyChar)

        addButton(self, sizerV, 'Ok', self.OnOk, border=10)

        self.SetSizer(sizerV)
        self.sizerV.Fit(self)
        self.Show(False)

    def OnShow(self, _):
        jp = self.jp
        if jp.mf.done:
            return
        if self.IsShown():
            if self.axis == AXIS_Z:
                self.retract = jp.zReturnLoc is None
                if self.retract:
                    val = self.jp.cfg.getFloatInfoData(cf.zRetractLoc)
                else:
                    val = jp.zReturnLoc
            else:
                self.retract = jp.xReturnLoc is None
                if self.retract:
                    val = self.jp.cfg.getFloatInfoData(cf.xRetractLoc)
                else:
                    val = jp.xReturnLoc

            title = "%s %s" % ("Retract" if self.retract \
                               else "Return", self.axisVal)
            self.SetTitle(title)
            self.pos.SetEditable(self.retract)

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

    def OnOk(self, _):
        jp = self.jp
        try:
            loc = float(self.pos.GetValue())
            m = self.jp.mf.move
            m.queClear()
            comm = self.jp.mf.comm
            comm.command(cm.C_CMD_PAUSE)
            comm.command(cm.C_CLEARQUE)
            if self.axis == AXIS_Z:
                self.jp.mf.sendData.sendZData()
                m.saveZOffset()
                m.moveZ(loc, ct.CMD_JOG)
                jp.zReturnLoc = \
                    jp.zPos.GetValue() if self.retract else None
                bitmap = "westR.png" if self.retract else "eastG.png"
                jp.zButton.SetBitmap(wx.Bitmap(bitmap))
            else:
                self.jp.mf.sendData.sendXData()
                m.saveXOffset()
                m.moveX(loc, ct.CMD_JOG)
                jp.xReturnLoc = \
                    jp.xPos.GetValue() if self.retract else None
                bitmap = "northR.png" if self.retract else "southG.png"
                jp.xButton.SetBitmap(wx.Bitmap(bitmap))
            comm.command(cm.C_CMD_RESUME)
            self.Show(False)
            jp.focus()
        except ValueError:
            print("ValueError on retract")
            stdout.flush()

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

    def OnRPM(self, _):
        self.jP.setSurfaceSpeed(False)

    def OnSurfaceSpeed(self, _):
        self.jP.setSurfaceSpeed(True)

EVT_UPDATE_ID = wx.Window.NewControlId()

class UpdateEvent(wx.PyEvent):
    def __init__(self, data):
        wx.PyEvent.__init__(self)
        self.SetEventType(EVT_UPDATE_ID)
        self.data = data

class UpdateThread(Thread):
    def __init__(self, mainFrame, notifyWindow):
        Thread.__init__(self)
        self.mf = mainFrame
        self.jp = mainFrame.jogPanel
        self.comm = mainFrame.comm
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
        self.lastXIdxD = None
        self.lastXIdxP = None
        self.lastZIdxD = None
        self.lastZIdxP = None
        self.queCount = 0
        self.dbgCount = 0
        dbgSetup = ( \
            (en.D_PASS, self.dbgPass), \
            (en.D_DONE, self.dbgDone), \
            (en.D_TEST, self.dbgTest), \
            (en.D_XMOV, self.dbgXMov), \
            (en.D_XLOC, self.dbgXLoc), \
            (en.D_XDST, self.dbgXDst), \
            (en.D_XSTP, self.dbgXStp),
            (en.D_XST, self.dbgXState), \
            (en.D_XBSTP, self.dbgXBSteps), \
            (en.D_XDRO, self.dbgXDro), \
            (en.D_XPDRO, self.dbgXPDro), \
            (en.D_XEXP, self.dbgXExp), \
            (en.D_XERR, self.dbgXErr), \
            (en.D_XWT, self.dbgXWait), \
            (en.D_XDN, self.dbgXDone), \
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
            (en.D_ZERR, self.dbgZErr), \
            (en.D_ZWT, self.dbgZWait), \
            (en.D_ZDN, self.dbgZDone), \
            (en.D_ZEST, self.dbgZEncStart), \
            (en.D_ZEDN, self.dbgZEncDone), \
            (en.D_ZX, self.dbgZX), \
            (en.D_ZY, self.dbgZY), \
            (en.D_XIDXD, self.dbgXIdxD), \
            (en.D_XIDXP, self.dbgXIdxP), \
            (en.D_ZIDXD, self.dbgZIdxD), \
            (en.D_ZIDXP, self.dbgZIdxP), \
            (en.D_HST, self.dbgHome), \
            (en.D_MSTA, self.dbgMoveState), \
            (en.D_MCMD, self.dbgMoveCmd), \
            )
        self.dbgTbl = dbgTbl = [self.dbgNone for _ in range(en.D_MAX)]
        for (index, action) in dbgSetup:
            dbgTbl[index] = action
        # for i, val in enumerate(dbgTbl):
        #     if val is None:
        #         print("dbgTbl action for %s missing" % (en.dMessageList[i]))
        #         stdout.flush()

    def openDebug(self, fName="dbg.txt", action=None):
        self.dbg = open(os.path.join(DBG_DIR, fName), "ab")
        t = "\n" + timeStr()
        if action is not None:
            t = t[:-1] + " " + en.operationsList[action] + "\n"
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
        if self.mf.done:
            return
        #comm.xDbgPrint = False
        try:
            result = self.comm.command(cm.C_READALL, True)
            if result is None:
                return

        except CommTimeout:
            if self.mf.done:
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

        #comm.xDbgPrint = True
        if self.readAllError:
            self.readAllError = False
            wx.PostEvent(self.notifyWindow,
                         UpdateEvent((en.EV_ERROR, st.STR_CLR)))
        try:
            tmp = result[3:].split(' ')
            (z, x, rpm, curPass, droZ, droX, flag, \
             queCount, dbgCount) = tmp[1:10]
            self.queCount = int(queCount)
            self.dbgCount = int(dbgCount)
            result = (en.EV_READ_ALL, z, x, rpm, curPass, droZ, droX, flag)
            wx.PostEvent(self.notifyWindow, UpdateEvent(result))
        except ValueError:
            print("readAll ValueError ", result)
            stdout.flush()

    def run(self):
        print("Update started")
        i = 0
        scanMax = len(self.parmList)
        moveQue = self.mf.move.moveQue
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
                    if self.mf.done:
                        break
            i += 1
            if i >= scanMax:
                i = 0

            # process move queue

            if not moveQue.empty() and self.queCount > 10:
                if not self.threadRun:
                    break
                try:
                    # num = self.comm.getQueueStatus()
                    # if not self.threadRun:
                    #     break
                    num = self.queCount
                    while num > 0:
                        num -= 1
                        try:
                            (opString, op, val) = moveQue.get(False)
                            self.comm.queMove(opString, op, val)
                            # self.comm.sendMove(opString, op, val)
                        except Empty:
                            break
                except CommTimeout:
                    print("CommTimeout on queue")
                    stdout.flush()
                except serial.SerialException:
                    print("SerialException on queue")
                    stdout.flush()
                    break
                except TypeError:
                    print("TypeError on queue")
                    stdout.flush()
                self.comm.sendMultiMove()

            # get debug data

            if self.dbgCount != 0:
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
            result = self.comm.getString(cm.C_READDBG, 10)
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
                    # print("c %2x val %4x" % (cmd, val))
                    try:
                        action = self.dbgTbl[cmd]
                        assert (callable(action))
                        # noinspection PyArgumentList
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
                        #         if not self.jp.currentPanel.control.addEnabled:
                        #             self.baseTime = time()
                        #     if val == 1:
                        #         self.baseTime = None
                        #         if self.dbg is not None:
                        #             self.dbg.close()
                        #             self.dbg = None
                    except IndexError:
                        print("procDebug IndexError %s" % result)
                        stdout.flush()
                    except TypeError:
                        print("procDebug TypeError %s %s" % \
                              (en.dMessageList[cmd], result))
                        stdout.flush()
                except ValueError:
                    print("procDebug ValueError cmd %s val %s" % (cmd, val))
                    stdout.flush()
        except CommTimeout:
            print("procDebug getString CommTimeout")
            stdout.flush()
        except serial.SerialException:
            print("procDebug getString SerialException")
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
            print("dbgDispatch IndexError %d" % cmd)
            stdout.flush()
        except TypeError:
            print("dbgDispatch TypeError %s %s" % \
                  (en.dMessageList[cmd], str(val)))
            stdout.flush()

    # noinspection PyMethodMayBeStatic,PyUnusedLocal
    def dbgNone(self, val):
        return "none"

    def dbgPass(self, val):
        # tmp = val >> 8
        # if tmp == 0:
        #     return("pass %d\n")
        # elif tmp == 1:
        #     return("spring\n")
        # elif tmp == 2:
        #     return("spring %d\n" % (val & 0xff))
        self.passVal = val
        self.lastXIdxD = None
        self.lastXIdxP = None
        self.lastZIdxD = None
        self.lastZIdxP = None
        result = "spring\n" if val & 0x100 else \
                 "spring %d\n" % (val & 0xff) if val & 0x200 else \
                 "pass %d\n" % (val)
        return(result)

    def dbgDone(self, val):
        if val == ct.PARM_START:
            if not self.jp.currentPanel.control.addEnabled:
                self.baseTime = time()
            return("strt " + timeStr())
        elif val == ct.PARM_DONE:
            return("done " + timeStr())

    # noinspection PyMethodMayBeStatic
    def dbgTest(self, val):
        return("test %d" % (val))

    def dbgXMov(self, val):
        tmp = float(val) / self.mf.xStepsInch - self.jp.xHomeOffset
        return("xmov %7.4f %7.4f" % (tmp, tmp * 2.0))

    def dbgXLoc(self, val):
        iTmp = int(val)
        self.xIntLoc = iTmp
        tmp = float(val) / self.mf.xStepsInch - self.jp.xHomeOffset
        self.xLoc = tmp
        if self.xDro is not None:
            diff = " diff %7.4f" % (self.xDro - tmp)
            self.xDro = None
        else:
            diff = ""
        return("xloc %7.4f %7.4f %7d%s" % (tmp, tmp * 2.0, iTmp, diff))

    def dbgXDst(self, val):
        tmp = float(val) / self.mf.xStepsInch
        return("xdst %7.4f %7d" % (tmp, val))

    def dbgXStp(self, val):
        dist = float(val) / self.mf.xStepsInch
        if self.xEncoderCount is None or self.xEncoderCount == 0:
            return("xstp %7.4f %7d" % (dist, val))
        else:
            pitch = dist / (float(self.xEncoderCount) / self.encoderCount)
            self.xEncoderCount = None
            return("xstp %7.4f %7d pitch %7.4f" % (dist, val, pitch))

    def dbgXState(self, val):
        return(("x_st %s" % (en.axisStatesList[val])) + \
                ("\n" if self.mIdle and val == en.AXIS_IDLE else ""))

    def dbgXBSteps(self, val):
        tmp = float(val) / self.mf.xStepsInch
        return("xbst %7.4f %7d" % (tmp, val))

    def dbgXDro(self, val):
        tmp = float(val) / self.jp.xDROInch - self.jp.xDROOffset
        self.xDro = tmp
        return("xdro %7.4f %7.4f %7d" % (tmp, tmp * 2.0, val))

    def dbgXPDro(self, val):
        tmp = float(val) / self.jp.xDROInch - self.jp.xDROOffset
        passVal = self.passVal
        spring = (passVal & 0xf00) >> 8
        passVal &= 0xff
        if spring == 0:
            spring = "  "
        else:
            spring = "s" + str(spring)
        s = "pass %s %2d xdro %7.4f xloc %7.4f diff %7.4f" % \
            (spring, passVal, tmp * 2.0, self.xLoc * 2.0, self.xLoc - tmp)
        self.jp.mf.dPrt(s + "\n", flush=True)
        return("xpdro " + s)

    def dbgXExp(self, val):
        tmp = float(val) / self.mf.xStepsInch - self.jp.xHomeOffset
        return("xexp %7.4f" % (tmp))

    def dbgXErr(self, val):
        tmp = float(val) / self.mf.xStepsInch
        return("xerr %7.4f" % (tmp))

    # noinspection PyMethodMayBeStatic
    def dbgXWait(self, val):
        return("xwt  %2x" % (val))

    # noinspection PyMethodMayBeStatic
    def dbgXDone(self, val):
        return("xdn  %2x" % (val))

    def dbgXEncStart(self, val):
        self.xEncoderStart = val
        return(None)

    # noinspection PyMethodMayBeStatic
    def dbgXX(self, val):
        return("x_x  %7d" % (val))

    # noinspection PyMethodMayBeStatic
    def dbgXY(self, val):
        return("x_y  %7d" % (val))

    def dbgXEncDone(self, val):
        if self.xEncoderStart is None:
            return(None)
        count = c_uint32(val - self.xEncoderStart).value
        self.xEncoderCount = count
        return("xedn %7.2f %7d" % (float(count) / self.encoderCount, count))

    def dbgZMov(self, val):
        tmp = float(val) / self.mf.zStepsInch - self.jp.zHomeOffset
        return("zmov %7.4f" % (tmp))

    def dbgZLoc(self, val):
        iTmp = int(val)
        self.zIntLoc = iTmp
        tmp = float(val) / self.mf.zStepsInch - self.jp.zHomeOffset
        self.zLoc = tmp
        if self.zDro is not None:
            diff = " diff %7.4f" % (self.zDro - tmp)
            self.zDro = None
        else:
            diff = ""
        return("zloc %7.4f %7d %s" % (tmp, iTmp, diff))

    def dbgZDst(self, val):
        tmp = float(val) / self.mf.zStepsInch
        return("zdst %7.4f %7d" % (tmp, val))

    def dbgZStp(self, val):
        dist = float(val) / self.mf.zStepsInch
        if self.zEncoderCount is None or self.zEncoderCount == 0:
            return("zstp %7.4f %7d" % (dist, val))
        else:
            pitch = dist / (float(self.zEncoderCount) / self.encoderCount)
            self.zEncoderCount = None
            return("zstp %7.4f %7d pitch %7.4f" % (dist, val, pitch))

    def dbgZState(self, val):
        if self.jp.currentPanel.active:
            return(("z_st %s" % (en.axisStatesList[val])) + \
                   ("\n" if self.mIdle and val == en.AXIS_IDLE else ""))
        else:
            rtnVal = "z_st %s" % (en.axisStatesList[val])
            if val == en.AXIS_IDLE:
                self.baseTime = None
                rtnVal += "\n"
            elif self.baseTime is None:
                self.baseTime = time()
            return(rtnVal)

    def dbgZBSteps(self, val):
        tmp = float(val) / self.mf.zStepsInch
        return("zbst %7.4f %7d" % (tmp, val))

    def dbgZDro(self, val):
        tmp = float(val) / self.jp.zDROInch - self.jp.zDROOffset
        self.zDro = tmp
        return("zdro %7.4f" % (tmp))

    def dbgZPDro(self, val):
        tmp = float(val) / self.jp.zDROInch - self.jp.zDROOffset
        passVal = self.passVal
        spring = (passVal & 0xf00) >> 8
        passVal &= 0xff
        if spring == 0:
            spring = "  "
        else:
            spring = "s" + str(spring)
        s = "pass %s %2d zdro %7.4f zloc %7.4f diff %7.4f" % \
            (spring, passVal, tmp, self.zLoc, self.zLoc - tmp)
        self.jp.mf.dPrt(s + "\n", flush=True)
        return("zpdro " + s)

    def dbgZExp(self, val):
        tmp = float(val) / self.mf.zStepsInch - self.jp.zHomeOffset
        return("zexp %7.4f" % (tmp))

    def dbgZErr(self, val):
        tmp = float(val) / self.mf.zStepsInch
        return("zerr %7.4f" % (tmp))

    # noinspection PyMethodMayBeStatic
    def dbgZWait(self, val):
        return("zwt  %2x" % (val))

    # noinspection PyMethodMayBeStatic
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

    # noinspection PyMethodMayBeStatic
    def dbgZX(self, val):
        return("z_x  %7d" % (val))

    # noinspection PyMethodMayBeStatic
    def dbgZY(self, val):
        return("z_y  %7d" % (val))

    def dbgXIdxD(self, val):
        result = "xixd %7.4f" % (float(val) / self.jp.xDROInch - \
                                 self.jp.xDROOffset)

        if self.lastXIdxD is not None:
            delta = abs(self.lastXIdxD - val)
            result += " %7.4f %6d %5d" % (delta / self.jp.xDROInch, val, delta)
        self.lastXIdxD = val
        return(result)

    def dbgXIdxP(self, val):
        result = "xixp %7.4f" % (float(val) / self.jp.xStepsInch - \
                                 self.jp.xHomeOffset)

        if self.lastXIdxP is not None:
            delta = abs(self.lastXIdxP - val)
            result += " %7.4f %6d %5d" % \
                (delta / self.jp.xStepsInch, val, delta)
        self.lastXIdxP = val
        return(result)

    def dbgZIdxD(self, val):
        result = "zixd %7.4f" % (float(val) / self.jp.zDROInch - \
                                 self.jp.zDROOffset)

        if self.lastZIdxD is not None:
            delta = abs(self.lastZIdxD - val)
            result += " %7.4f %6d %5d" % (delta / self.jp.zDROInch, val, delta)
        self.lastZIdxD = val
        return(result)

    def dbgZIdxP(self, val):
        result = "zixp %7.4f" % (float(val) / self.jp.zStepsInch - \
                                 self.jp.zHomeOffset)

        if self.lastZIdxP is not None:
            delta = abs(self.lastZIdxP - val)
            result += " %7.4f %6d %5d" % \
                (delta / self.jp.zStepsInch, val, delta)
        self.lastZIdxP = val
        return(result)

    # noinspection PyMethodMayBeStatic
    def dbgHome(self, val):
        return("hsta %s" % (en.hStatesList[val]))

    def dbgMoveState(self, val):
        self.mIdle = val == en.M_IDLE
        return("msta %s" % (en.mStatesList[val]
                            + ("\n" if self.mIdle else "")))

    # noinspection PyMethodMayBeStatic
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

class DialFrame(wx.Frame):
    def __init__(self, title, parent=None):
        wx.Frame.__init__(self, parent=parent, title=title)

        self.pointerVal = 0

        self.SetSize(wx.Size(512, 512))

        self.sizerV = sizerV = wx.BoxSizer(wx.VERTICAL)
        self.dialPanel = panel = DialPanel(self)
        panel.SetAutoLayout(True)
        panel.SetSizer(sizerV)
        sizerV.Fit(panel)
        self.Show()

class DialPanel(wx.Panel):
    def __init__(self, parent, *args, **kwargs):
        super(DialPanel, self).__init__(parent, *args, **kwargs)

        self.pointerVal = 0
        self.Bind(wx.EVT_SIZE, self.OnResize)
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.bmp = None

    def updatePointer(self, val):
        pointerVal = (int(val * 10000) % 1000) / 10
        if self.pointerVal != pointerVal:
            self.pointerVal = pointerVal
            self.Refresh()
            # self.Update()

    # noinspection PyUnusedLocal
    def OnResize(self, event):
        self.bmp = None
        self.Refresh()
        self.Layout()

    def OnPaint(self, _):
        dc = wx.PaintDC(self)
        dc.SetMapMode(wx.MM_TEXT)
        brush = wx.Brush("white")
        dc.SetBackground(brush)
        dc.Clear()
        self.render(dc)

    def render(self, dc):
        size = self.GetSize()
        # print("width %3d height %3d" % (size.x, size.y))
        # stdout.flush()

        WIDTH, HEIGHT = size.x, size.y

        r = 0.5
        self.r = r
        if self.bmp is None:
            surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
            ctx = cairo.Context(surface)

            s = min(size.x, size.y)
            self.scale = s
            ctx.scale(s, s)         # Normalizing the canvas

            ctx.set_font_size(0.05)
            ctx.select_font_face("Arial", cairo.FONT_SLANT_NORMAL, \
                                 cairo.FONT_WEIGHT_NORMAL)

            # r0 = 0.9 * r
            rc = 0.99 * r
            ctx.translate(r, r)  # Changing the current transformation matrix

            ctx.move_to(rc, 0)

            ctx.arc(0.0, 0.0, rc, 0.0, 2*pi)

            for i in range(100):
                a = radians((i / 100) * 360) - pi/2
                label = False
                if i % 10 == 0:
                    r0 = 0.8 * r
                    label = True
                else:
                    rem = i % 5
                    if rem == 0:
                        r0 = 0.85 * r
                    # elif (rem == 2) or (rem == 3):
                    #     r0 = 0.85 * r
                    else:
                        r0 = 0.9 * r
                x0 = r0 * cos(a)
                y0 = r0 * sin(a)
                x1 = rc * cos(a)
                y1 = rc * sin(a)
                # print(i, x0, y0, x1, y1)
                ctx.move_to(x0, y0)
                ctx.line_to(x1, y1)
                if label:
                    txt = str(i)
                    extents = ctx.text_extents(txt)
                    r1 = r0 - 0.01
                    x0 = r1 * cos(a)
                    y0 = r1 * sin(a)
                    xOffset = 0
                    yOffset = 0
                    if i == 0:
                        xOffset = -extents.x_advance / 2
                        yOffset = extents.height
                    elif i == 10:
                        xOffset = -extents.x_advance
                        yOffset = extents.height *.75
                    elif i == 20:
                        xOffset = -extents.x_advance
                        yOffset = extents.height / 2
                    elif i == 30:
                        xOffset = -extents.x_advance
                        yOffset = extents.height / 2
                    elif i == 40:
                        xOffset = -extents.x_advance
                        yOffset = extents.height *.25
                    elif i == 50:
                        xOffset = -extents.x_advance / 2
                    elif i == 60:
                        yOffset = extents.height * .25
                    elif i == 70:
                        yOffset = extents.height / 2
                    elif i == 80:
                        yOffset = extents.height / 2
                    elif i == 90:
                        yOffset = extents.height *.75
                    ctx.move_to(x0 + xOffset, y0 + yOffset)
                    ctx.show_text(txt)
                    # label = False

            ctx.set_source_rgb(0.3, 0.2, 0.5)  # Solid color
            ctx.set_line_width(0.002)
            ctx.stroke()

            ctx.arc(0, 0, 0.05 * r, 0, 2 * pi)
            ctx.fill()

            self.bmp = wxcairo.BitmapFromImageSurface(surface)

        dc.DrawBitmap(self.bmp, 0, 0)

        # # Arc(cx, cy, radius, start_angle, stop_angle)
        # ctx.arc(0.2, 0.1, 0.1, -math.pi / 2, 0)
        # ctx.line_to(0.5, 0.1)  # Line to (x,y)
        # # Curve(x1, y1, x2, y2, x3, y3)
        # ctx.curve_to(0.5, 0.2, 0.5, 0.4, 0.2, 0.8)
        # ctx.close_path()

        # if False:
        #     ctx = wxcairo.ContextFromDC(dc)
        #
        #     s = min(size.x, size.y)
        #     ctx.scale(s, s)         # Normalizing the canvas
        #     ctx.translate(r, r)	# Changing the current transformation matrix
        #
        #     # ctx.arc(0, 0, 0.05 * r, 0, 2 * pi)
        #     # ctx.fill()
        #
        #     ctx.move_to(0, 0)
        #     ctx.line_to(0.75 * r, 0)
        #
        #     ctx.set_source_rgb(1.0, 0.0, 0.0)
        #     ctx.set_line_width(0.01)
        #     ctx.stroke()
        #
        #     ctx.move_to(0.75 * r, 0)
        #     ctx.line_to(0.95 * r, 0)
        #
        #     ctx.set_source_rgb(1.0, 0.0, 0.0)
        #     ctx.set_line_width(0.002)
        #     ctx.stroke()

        self.drawPointer(dc)

    def drawPointer(self, dc):
        ctx = wxcairo.ContextFromDC(dc)

        s = self.scale
        r = self.r

        ctx.scale(s, s)         # Normalizing the canvas
        ctx.translate(r, r)	# Changing the current transformation matrix

        r0 = 0.70 * r
        r1 = 0.95 * r
        a = radians((self.pointerVal / 100) * 360) - pi/2

        x0 = r0 * cos(a)
        y0 = r0 * sin(a)
        ctx.move_to(0, 0)
        ctx.line_to(x0, y0)

        ctx.set_source_rgb(1.0, 0.0, 0.0)
        ctx.set_line_width(0.01)
        ctx.stroke()

        x1 = r1 * cos(a)
        y1 = r1 * sin(a)
        ctx.move_to(x0, y0)
        ctx.line_to(x1, y1)

        ctx.set_source_rgb(1.0, 0.0, 0.0)
        ctx.set_line_width(0.002)
        ctx.stroke()

class MainFrame(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, -1, title)
        self.done = False
        self.xHomed = False
        self.Bind(wx.EVT_CLOSE, self.onClose)
        self.Connect(-1, -1, EVT_RESIZE_ID, self.OnResize)
        self.dirName = os.getcwd()
        self.parseCmdLine()

        if not os.path.exists(DBG_DIR):
            os.makedirs(DBG_DIR)
        self.dbg = open(DBG_LOG, "ab")
        t = "\n" + timeStr() + "\n"
        self.dbg.write(t.encode())
        self.dbg.flush()

        self.turnSync = en.SEL_TU_SPEED
        self.threadSync = en.SEL_TH_NO_ENC

        self.xSyncInt = None
        self.zSyncInt = None
        self.xSyncExt = None
        self.zSyncExt = None

        self.cfg = cfg = ConfigInfo(cf.configTable)
        self.initialConfig(cfg)

        self.zStepsInch = None
        self.xStepsInch = None

        self.zDROInch = None
        self.xDROInch = None

        if EXT_DRO:
            # global eDro
            import extDro as eDro
            from extDro import DroTimeout
            self.dro = eDro.ExtDro()

        if not R_PI and SPINDLE_SYNC_BOARD and not SYNC_SPI:
            self.syncComm = Comm()

        if R_PI:
            if RISCV:
                comm = CommRiscv(self)
            else:
                comm = CommPi()
        else:
            comm = Comm()
        self.comm = comm
        comm.SWIG = SWIG

        self.hdrFont = \
            wx.Font(20, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, \
                    wx.FONTWEIGHT_NORMAL, False, u'Consolas')
        self.defaultFont = defaultFont = \
            wx.Font(10, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, \
                    wx.FONTWEIGHT_NORMAL, False, u'Consolas')
        self.SetFont(defaultFont)

        self.currentPanel = None

        self.zDialog = ZDialog(self, defaultFont)
        self.xDialog = XDialog(self, defaultFont)
        self.spindleDialog = SpindleDialog(self, defaultFont)
        self.portDialog = PortDialog(self, defaultFont)
        self.configDialog = ConfigDialog(self, defaultFont)
        if not R_PI:
            self.megaDialog = MegaDialog(self, defaultFont)

        self.testSpindleDialog = None
        self.testSyncDialog = None
        self.testTaperDialog = None
        self.testMoveDialog = None

        self.menuSetup()
        self.initUI()

        self.zDialog.setupVars()
        self.xDialog.setupVars()

        self.dbgSave = bool(cfg.getBoolInfoData(cf.cfgDbgSave))
        self.cfgDraw = bool(cfg.getBoolInfoData(cf.cfgDraw))

        self.sendData = SendData(self)

        self.dialFrame = None
        self.dialPanel = None
        # self.dialFrame = DialFrame("Dial Frame")
        # self.dialPanel = self.dialFrame.dialPanel

        if not R_PI and not RISCV:
            self.updateThread = \
                updateThread = UpdateThread(self, self.jogPanel)
            if self.dbgSave:
                print("***start saving debug***")
                updateThread.openDebug()

        if WINDOWS:
            self.jogShuttle = JogShuttle(self)
        else:
            self.jogShuttle = None

        comm.openSerial(cfg.getInfoData(cf.commPort), \
                        cfg.getInfoData(cf.commRate))

        if not R_PI and SPINDLE_SYNC_BOARD and not SYNC_SPI:
            self.syncComm.openSerial(cfg.getInfoData(cf.syncPort), \
                                cfg.getInfoData(cf.syncRate))
            self.syncComm.setupCmds(sc.SYNC_LOADMULTI, sc.SYNC_LOADVAL,
                               sc.SYNC_READVAL)

            self.syncComm.setupTables(sc.cmdTable, sp.parmTable)

        port = cfg.getInfoData(cf.keypadPort)
        if len(port) != 0:
            self.keypad = Keypad(self, cfg.getInfoData(cf.keypadPort), \
                                 cfg.getInfoData(cf.keypadRate))
        else:
            self.keypad = None

        if EXT_DRO:
            self.initDRO()

        if FPGA:
            global xb, xr
            if not R_PI:
                # import xBitDef as xb
                import xRegDef as xr

                comm.enableXilinx()
                comm.xRegs = xr.xRegTable
            else:
                # import fpgaLathe as xb
                import lRegDef as xr

        self.initDevice()

        if not R_PI:
            updateThread.start()
        else:
            comm.setPostUpdate(self.jogPanel.postUpdate)
            # comm.setDbgDispatch(updateThread.dbgDispatch)
        self.delay = Delay(self)

        if (not R_PI) and MEGA:
            self.sendData.sendMegaData()

        self.fTest = None

    def dbgOpen(self, fName):
        self.fTest = open(os.path.join(DBG_DIR, fName), 'w')

    def dbgPrt(self, txt, fmt, values):
        txt.AppendText((fmt + "\n") % values)
        self.fTest.write((fmt + "\n") % values)

    def dbgClose(self):
        self.fTest.close()

    def dPrt(self, text, console=False, flush=False):
        self.dbg.write(text.encode())
        if flush:
            self.dbg.flush()
        if console:
            print(text, end='')
            if flush:
                stdout.flush()

    def onClose(self, _):
        posList = (cf.zSvPosition, cf.zSvHomeOffset, \
                   cf.xSvPosition, cf.xSvHomeOffset)
        if DRO:
            posList += (cf.zSvDROPosition, cf.zSvDROOffset, \
                        cf.xSvDROPosition, cf.xSvDROOffset)
        self.cfg.saveList(self.posFile, posList)
        self.done = True
        if not R_PI and not RISCV:
            self.updateThread.close()
        self.jogPanel.btnRpt.close()
        if self.jogShuttle is not None:
            self.jogShuttle.close()
        if R_PI:
            self.comm.close()
        if self.keypad is not None:
            self.keypad.close()
        # self.dialFrame.Destroy()
        if self.comm.ser is not None:
            self.comm.ser.close()
        if self.dbg is not None:
            self.dbg.close()
            self.dbg = None
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
        self.Bind(wx.EVT_MENU, self.OnRestart, menu)

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

        ID_CONFIG_SETUP = wx.Window.NewControlId()
        menu = setupMenu.Append(ID_CONFIG_SETUP, 'Config')
        self.Bind(wx.EVT_MENU, self.OnConfigSetup, menu)

        if not R_PI:
            ID_MEGA_SETUP = wx.Window.NewControlId()
            menu = setupMenu.Append(ID_MEGA_SETUP, 'Mega')
            self.Bind(wx.EVT_MENU, self.OnMegaSetup, menu)

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

        ID_ARC = wx.Window.NewControlId()
        menu = operationMenu.Append(ID_ARC, 'Arc')
        self.Bind(wx.EVT_MENU, self.OnArc, menu)

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

        print("MainFrame JogPanel")
        self.jogPanel = jogPanel = JogPanel(self, style=wx.WANTS_CHARS)
        if RISCV:
            self.comm.jp = jogPanel

        self.move = MoveCommands(self)

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

        self.arcPanel = panel = ArcPanel(self, self.hdrFont)
        self.panels['arcPanel'] = panel
        sizerV.Add(panel, 0, wx.EXPAND|wx.ALL, border=2)
        panel.Hide()

        sizerV.Add(jogPanel, 0, wx.EXPAND|wx.ALL, border=2)

        self.SetSizer(sizerV)
        self.SetSizerAndFit(sizerV)
        jogPanel.xHomed = self.xHomed

        varList = (('jogPanel.zIPosition', cf.zSvPosition), \
                ('jogPanel.zIHomeOffset', cf.zSvHomeOffset), \
                ('jogPanel.xIPosition', cf.xSvPosition), \
                ('jogPanel.xIHomeOffset', cf.xSvHomeOffset))
        if DRO:
            varList += (('jogPanel.zIDROPosition', cf.zSvDROPosition), \
                     ('jogPanel.zIDROOffset', cf.zSvDROOffset), \
                     ('jogPanel.xIDROPosition', cf.xSvDROPosition), \
                     ('jogPanel.xIDROOffset', cf.xSvDROOffset))

        cfg = self.cfg
        for (v, key) in varList:
            if cfg.info[key] is None:
                cfg.newInfo(key, 0)
            exp = v + ' = cfg.getInfoInstance(' + str(key) + ')'
            exec(exp)

        dw, dh = wx.DisplaySize()
        w, h = self.GetSize()
        self.SetPosition((int((3 * dw) / 4 - w), 0))

        # read data here so updates below have data

        cfg.readInfo(self.cfgFile, cf.config)
        cfg.readInfo(self.posFile, cf.config)

        jogPanel.update()

        self.turnPanel.update()
        self.facePanel.update()
        self.cutoffPanel.update()
        self.taperPanel.update()
        if STEP_DRV:
            self.threadPanel.update()
        self.arcPanel.update()

        self.showPanel()
        self.Fit()

    def initDRO(self):
        cfg = self.cfg
        port = cfg.getInfoData(cf.extDroPort)
        print("port %s" % (port))
        stdout.flush()
        if port is not None:
            self.dro.openSerial(cfg.getInfoData(cf.extDroPort), \
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
                dro = self.dro
                dro.command(dro.automateOff, True, dro.delim)
                print("automation turned on")
                rsp = dro.command(dro.showFunc, True, dro.delim)
                rsp = re.sub(dro.matchPrompt, "", rsp)
                # print(rsp)
                rsp = rsp.split("\n")
                for option in rsp:
                    tmp = option.strip().lower().split(":")
                    if len(tmp) == 2:
                        if tmp[0].strip() == "diameter":
                            if tmp[1].strip() != "on":
                                dro.command(dro.diamFunc, \
                                            True, dro.delim)
                                break
                dro.command(dro.inchMode, True, dro.delim)
                dro.command(dro.absMode, True, dro.delim)
                for line in dro.axisFunc:
                    dro.command(line, True, dro.delim)
                rsp = dro.command(dro.automateOn, True)
                # rsp = dro.command(dro.extReadX, True)
                # print(rsp, end="")
                # rsp = dro.command(dro.extReadZ, True)
                # print(rsp, end="")
                # dro.command(dro.setZ(str(3.555)), True)
                # dro.command("axis.zeroa(1,-2+axis.read(1))")
                # dro.command("axis.zeroa(2,-4+axis.read(2))"\
                #             "io.write('ok\\n')", True)
            except DroTimeout:
                print("DroTimeout exception")

    def initDevice(self):
        self.sendData.sendClear()
        stdout.flush()

        jp = self.jogPanel
        comm = self.comm
        cfg = self.cfg
        if comm.ser is not None:
            try:
                comm.queParm(pm.CFG_FPGA, cfg.getBoolInfoData(cf.cfgFpga))
                # comm.queParm(pm.CFG_FCY, cfg.getInfoData(cf.cfgFcy))
                comm.queParm(pm.CFG_MPG, cfg.getBoolInfoData(cf.cfgMPG))
                comm.queParm(pm.CFG_DRO, cfg.getBoolInfoData(cf.cfgDRO))
                comm.queParm(pm.CFG_LCD, cfg.getBoolInfoData(cf.cfgLCD))
                if not R_PI:
                    comm.queParm(pm.CFG_MEGA, cfg.getBoolInfoData(cf.cfgMega))
                comm.queParm(pm.CFG_SWITCH, cfg.getBoolInfoData(cf.spSwitch))
                comm.queParm(pm.CFG_VAR_SPEED, \
                             cfg.getBoolInfoData(cf.spVarSpeed))
                comm.queParm(pm.FPGA_FREQUENCY, \
                             cfg.getIntInfoData(cf.cfgFpgaFreq))
                comm.queParm(pm.COMMON_LIMITS, \
                             cfg.getBoolInfoData(cf.cfgCommonLimits))
                comm.queParm(pm.LIMITS_ENABLED, \
                             cfg.getBoolInfoData(cf.cfgLimitsEnabled))
                comm.queParm(pm.COMMON_HOME, \
                             cfg.getBoolInfoData(cf.cfgCommonHome))
                comm.command(cm.C_CMD_SETUP)

                self.sendData.sendSpindleData()

                self.sendData.sendZData()
                if EXT_DRO:
                    jp.setZFromExt()
                else:
                    jp.zPosition = cfg.getIntInfo(cf.zSvPosition)
                    comm.queParm(pm.Z_LOC, jp.zPosition)
                    jp.zHomeOffset = cfg.getFloatInfo(cf.zSvHomeOffset)
                    comm.queParm(pm.Z_HOME_OFFSET, \
                                 round(jp.zHomeOffset * self.zStepsInch))
                    print("zLoc %d %x %7.4f zHomeOffset %7.4f" % \
                          (jp.zPosition, jp.zPosition, \
                           float(jp.zPosition) / self.zStepsInch, \
                           jp.zHomeOffset))
                    stdout.flush()
                    if DRO:
                        jp.zDROPosition = cfg.getIntInfo(cf.zSvDROPosition)
                        comm.queParm(pm.Z_DRO_LOC, jp.zDROPosition)
                        jp.zDROOffset = cfg.getFloatInfo(cf.zSvDROOffset)
                        comm.queParm(pm.Z_DRO_OFFSET, \
                                     round(jp.zDROOffset * jp.zDROInch))
                        print("zDROPosition %d %x %7.4f zDROOffset %7.4f" % \
                              (jp.zDROPosition, jp.zDROPosition, \
                               float(jp.zDROPosition) / jp.zDROInch, \
                               jp.zDROOffset))
                        stdout.flush()
                comm.sendMulti()
                comm.command(cm.C_CMD_ZSETLOC)

                self.sendData.sendXData()
                if EXT_DRO:
                    jp.setXFromExt()
                else:
                    jp.xPosition = cfg.getIntInfo(cf.xSvPosition)
                    comm.queParm(pm.X_LOC, jp.xPosition)
                    jp.xHomeOffset = cfg.getFloatInfo(cf.xSvHomeOffset)
                    comm.queParm(pm.X_HOME_OFFSET, \
                                 round(jp.xHomeOffset * self.xStepsInch))
                    print("xLoc %d %x %7.4f xHomeOffset %7.4f" % \
                          (jp.xPosition, jp.xPosition, \
                           float(jp.xPosition) / self.xStepsInch, \
                           jp.xHomeOffset))
                    stdout.flush()
                    if DRO:
                        jp.xDROPosition = cfg.getIntInfo(cf.xSvDROPosition)
                        comm.queParm(pm.X_DRO_LOC, jp.xDROPosition)
                        jp.xDROOffset = cfg.getFloatInfo(cf.xSvDROOffset)
                        comm.queParm(pm.X_DRO_OFFSET, \
                                     round(jp.xDROOffset * jp.xDROInch))
                        print("xDROPosition %d %x %7.4f xDROOffset %7.4f" % \
                              (jp.xDROPosition, jp.xDROPosition, \
                               float(jp.xDROPosition) / jp.xDROInch, \
                               jp.xDROOffset))
                        stdout.flush()

                if HOME_TEST:
                    val = str(int(cfg.getFloatInfoData(cf.xHomeLoc) * \
                                  self.xStepsInch))
                    comm.queParm(pm.X_HOME_LOC, val)
                    comm.queParm(pm.X_HOME_STATUS, \
                                 ct.HOME_SUCCESS if jp.xHomed else \
                                 ct.HOME_ACTIVE)
                comm.command(cm.C_CMD_XSETLOC)

                if not R_PI:
                    comm.queParm(pm.MEGA_SIM, cfg.getBoolInfo(cf.spMegaSim))
                comm.sendMulti()

            except CommTimeout:
                commTimeout(jp)
        else:
            self.sendData.sendZData()
            self.sendData.sendXData()

    def parseCmdLine(self):
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
                        self.xHomed = True
                    elif tmp == 'help':
                        self.jogPanel.help()
            elif val.startswith('-'):
                if len(val) >= 2:
                    tmp = val[1]
                    if tmp == 'h':
                        self.jogPanel.help()
                    elif tmp == 'p':
                        n += 1
                        if n < len(sys.argv):
                            self.posFile = sys.argv[n]
                            if not re.search(r'\.[a-zA-Z0-9]*$', self.posFile):
                                self.posFile += ".txt"
            elif val.startswith('?'):
                self.jogPanel.help()
            else:
                if self.cfgFile is None:
                    self.cfgFile = val
                    if not re.search(r'\.[a-zA-Z0-9]*$', self.cfgFile):
                        self.cfgFile += ".txt"
            n += 1
        if self.cfgFile is None:
            self.cfgFile = "config.txt"
        if self.posFile is None:
            self.posFile = "posInfo.txt"

    def initialConfig(self, cfg):
        global FPGA, DRO, EXT_DRO, REM_DBG, STEP_DRV, \
            MEGA, MOTOR_TEST, SPINDLE_ENCODER, SPINDLE_SYNC_BOARD, \
            SPINDLE_INTERNAL_SYNC, SPINDLE_SWITCH, SPINDLE_VAR_SPEED, \
            HOME_IN_PLACE, X_DRO_POS, SYNC_SPI

        cfg.clrInfo(len(cf.config))
        cfg.readInfo(self.cfgFile, cf.config)

        FPGA = cfg.getInitialBoolInfo(cf.cfgFpga)
        DRO = cfg.getInitialBoolInfo(cf.cfgDRO)
        REM_DBG = cfg.getInitialBoolInfo(cf.cfgRemDbg)
        STEP_DRV = cfg.getInitialBoolInfo(cf.spStepDrive)
        MOTOR_TEST = cfg.getInitialBoolInfo(cf.spMotorTest)
        SPINDLE_ENCODER = cfg.getInitialBoolInfo(cf.cfgSpEncoder)
        SYNC_SPI = cfg.getInitialBoolInfo(cf.cfgSyncSPI)
        if R_PI:
            MEGA = False
        else:
            MEGA = cfg.getBoolInfoData(cf.cfgMega)

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
            SPINDLE_INTERNAL_SYNC = cfg.getInitialBoolInfo(cf.cfgIntSync)
        else:
            SPINDLE_SYNC_BOARD = False
            SPINDLE_INTERNAL_SYNC = False

        self.syncFuncSetup()

        HOME_IN_PLACE = cfg.getInitialBoolInfo(cf.cfgHomeInPlace)

        cfg.clrInfo(len(cf.config))

    def syncFuncSetup(self):
        cfg = self.cfg
        self.turnSync = turnSync = cfg.getIntInfoData(cf.cfgTurnSync)
        self.threadSync = threadSync = cfg.getIntInfoData(cf.cfgThreadSync)

        syncDbg = True

        if not FPGA:
            if (turnSync == en.SEL_TU_ESYN or \
                threadSync == en.SEL_TH_ESYN_RENC or \
                threadSync == en.SEL_TH_ESYN_RSYN):
                if self.zSyncExt is None:
                    self.zSyncExt = Sync(dbg=syncDbg)

            if (turnSync == en.SEL_TU_ESYN or \
                threadSync == en.SEL_TH_ISYN_RENC or \
                threadSync == en.SEL_TH_ESYN_RSYN):
                if self.xSyncExt is None:
                    self.xSyncExt = Sync(dbg=syncDbg)

            if (turnSync == en.SEL_TU_ISYN or \
                threadSync == en.SEL_TH_ISYN_RENC):
                if self.zSyncInt is None:
                    self.zSyncInt = Sync(dbg=syncDbg)

            if turnSync == en.SEL_TU_ISYN:
                if self.xSyncInt is None:
                    self.xSyncInt = Sync(dbg=syncDbg)
        else:
            self.zSyncInt = Sync(dbg=syncDbg, fpga=True)
            self.xSyncInt = Sync(dbg=syncDbg, fpga=True)

        if True:
            print("FPGA %s" % (FPGA))
            print("STEP_DRV %s SPINDLE_ENCODER %s "\
                  "SPINDLE_SYNC_BOARD %s" % \
                  (STEP_DRV, SPINDLE_ENCODER, SPINDLE_SYNC_BOARD))
            print("turnSync %d %s threadSync %d %s" % \
                  (turnSync, en.selTurnText[turnSync], \
                   threadSync, en.selThreadText[threadSync]))

    def OnResize(self, _):
        print("OnResize")
        stdout.flush()
        self.Layout()
        self.Fit()

    def OnSave(self, _):
        self.cfg.saveInfo(self.cfgFile)

    def OnInit(self, _):
        # if False:
        #     self.zDialog = None
        #     self.xDialog = None
        #     self.SpindleDialog = None
        #     self.portDialog = None
        #     self.configDialog = None
        #     self.megaDialog = None
        #     self.initialConfig()
        self.initDevice()

    def OnRestart(self, _):
        self.cfg.saveInfo(self.cfgFile)
        os.execl(sys.executable, sys.executable, *sys.argv)

    def OnSavePanel(self, _):
        panel = self.cfg.getInfoData(cf.mainPanel)
        p = panel.replace('Panel', '')
        p = p[:1].upper() + p[1:].lower()
        dlg = wx.FileDialog(self, "Save " + p + " Config", self.dirName,
                            p + ".txt", "", wx.FD_SAVE)
        if dlg.ShowModal() == wx.ID_OK:
            self.dirName = dlg.GetDirectory()
            path = dlg.GetPath()
            self.cfg.saveList(path, getConfigList(self.panels[panel]))

    def OnLoadPanel(self, _):
        cfg = self.cfg
        panel = cfg.getInfoData(cf.mainPanel)
        p = panel.replace('Panel', '')
        p = p[:1].upper() + p[1:].lower()
        dlg = wx.FileDialog(self, "Load " + p + " Config", self.dirName,
                            p + ".txt", "", wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            self.dirName = dlg.GetDirectory()
            path = dlg.GetPath()
            cfg.readInfo(path, cf.config, getConfigList(self.panels[panel]))

    def OnExit(self, _):
        self.Close(True)

    def showDialog(self, dialog):
        (xPos, yPos) = self.GetPosition()
        dialog.Raise()
        dialog.Show(True)
        (w, h) = dialog.GetSize()
        xPos -= w
        if xPos < 1:
            xPos = 1
        dialog.SetPosition((xPos, yPos))

    def OnZSetup(self, _):
        if self.zDialog is None:
            self.zDialog = ZDialog(self, self.defaultFont)
        self.showDialog(self.zDialog)

    def OnXSetup(self, _):
        if self.xDialog is None:
            self.xDialog = XDialog(self, self.defaultFont)
        self.showDialog(self.xDialog)

    def OnSpindleSetup(self, _):
        if self.spindleDialog is None:
            self.spindleDialog = SpindleDialog(self, self.defaultFont)
        self.showDialog(self.spindleDialog)

    def OnPortSetup(self, _):
        if self.portDialog is None:
            self.portDialog = PortDialog(self, self.defaultFont)
        self.showDialog(self.portDialog)

    def OnConfigSetup(self, _):
        if self.configDialog is None:
            self.configDialog = ConfigDialog(self, self.defaultFont)
        self.showDialog(self.configDialog)

    def OnMegaSetup(self, _):
        if self.megaDialog is None:
            self.megaDialog = MegaDialog(self, self.defaultFont)
        self.showDialog(self.megaDialog)

    def getCurrentPanel(self):
        return(self.currentPanel)

    def showPanel(self):
        key = cf.mainPanel
        cfg = self.cfg
        if cfg.info[key] is None:
            cfg.initInfo(key, InfoValue('turnPanel'))

        if self.jogPanel.mvStatus != 0:
            self.jogPanel.updateError(st.STR_OP_IN_PROGRESS)
            return

        showPanel = cfg.getInfoData(key)
        for key in self.panels:
            panel = self.panels[key]
            if key == showPanel:
                panel.Show()
                self.currentPanel = panel
            else:
                panel.Hide()
        if self.currentPanel is None:
            panel = self.turnPanel
            panel.Show()
            self.currentPanel = panel
        self.Layout()
        self.Fit()

    def OnTurn(self, _):
        self.cfg.setInfo(cf.mainPanel, 'turnPanel')
        self.showPanel()

    def OnFace(self, _):
        self.cfg.setInfo(cf.mainPanel, 'facePanel')
        self.showPanel()

    def OnCutoff(self, _):
        self.cfg.setInfo(cf.mainPanel, 'cutoffPanel')
        self.showPanel()

    def OnTaper(self, _):
        self.cfg.setInfo(cf.mainPanel, 'taperPanel')
        self.showPanel()

    def OnThread(self, _):
        self.cfg.setInfo(cf.mainPanel, 'threadPanel')
        self.showPanel()

    def OnArc(self, _):
        self.cfg.setInfo(cf.mainPanel, 'arcPanel')
        self.showPanel()

    def OnTestSpindle(self, _):
        if self.testSpindleDialog is None:
            self.testSpindleDialog = TestSpindleDialog(self, self.defaultFont)
        else:
            self.testSpindleDialog.Raise()
        self.testSpindleDialog.spindleTest.test()
        self.testSpindleDialog.Show()

    def OnTestSync(self, _):
        if self.testSyncDialog is None:
            self.testSyncDialog = TestSyncDialog(self, self.defaultFont)
        else:
            self.testSyncDialog.Raise()
        self.testSyncDialog.syncTest.test()
        self.testSyncDialog.Show()

    def OnTestTaper(self, _):
        if self.testTaperDialog is None:
            self.testTaperDialog = TestTaperDialog(self, self.defaultFont)
        else:
            self.testTaperDialog.Raise()
        self.testTaperDialog.taperTest.test()
        self.testTaperDialog.Show()

    def OnTestMove(self, _):
        if self.testMoveDialog is None:
            self.testMoveDialog = TestMoveDialog(self, self.defaultFont)
        else:
            self.testMoveDialog.Raise()
        self.testMoveDialog.moveTest.test()
        self.testMoveDialog.Show()

class ZDialog(wx.Dialog, FormRoutines, DialogActions):
    def __init__(self, mainFrame, defaultFont):
        self.mf = mainFrame
        pos = (10, 10)
        wx.Dialog.__init__(self, mainFrame, -1, "Z Setup", pos, \
                            wx.DefaultSize, wx.DEFAULT_DIALOG_STYLE)
        self.SetFont(defaultFont)
        FormRoutines.__init__(self)
        DialogActions.__init__(self)
        self.Bind(wx.EVT_SHOW, OnDialogShow)
        self.sizerV = sizerV = wx.BoxSizer(wx.VERTICAL)

        self.fields = (
            ("Pitch", cf.zPitch, 'f'), \
            ("Motor Steps", cf.zMotorSteps, 'd'), \
            ("Micro Steps", cf.zMicroSteps, 'd'), \
            ("Motor Ratio", cf.zMotorRatio, 'fs'), \

            ("Backlash", cf.zBacklash, 'f'), \
            ("Backlash Increment", cf.zBackInc, 'f'), \

            ("Accel Unit/Sec2", cf.zAccel, 'fs'), \
            ("Min Speed U/Min", cf.zMinSpeed, 'fs'), \
            ("Max Speed U/Min", cf.zMaxSpeed, 'fs'), \
            ("Jog Min U/Min", cf.zJogMin, 'fs'), \
            ("Jog Max U/Min", cf.zJogMax, 'fs'), \
            ("MPG Jog Increment", cf.zMpgInc, 'fs'), \
            ("MPG Jog Max Dist", cf.zMpgMax, 'fs'), \

            ("bInvert Dir", cf.zInvDir, None), \
            ("bInvert MPG", cf.zInvMpg, None), \

            ("Retract Loc", cf.zRetractLoc, 'f'), \
            ("Probe Dist", cf.zProbeDist, 'f'), \
            ("Home/Probe Speed", cf.zHomeSpeed, 'fs'), \

            ("bHome Enable", cf.zHomeEna, None), \
            ("bHome Invert", cf.zHomeInv, None), \
            ("Home Dist", cf.zHomeDist, 'f'), \
            ("Home Rev Dist", cf.zHomeDistRev, 'f'), \
            ("Backoff Dist", cf.zHomeDistBackoff, 'f'), \
            ("bHome Dir", cf.zHomeDir, None), \

            ("bLimits Enable", cf.zLimEna, None), \
            ("bNeg Limit Invert", cf.zLimNegInv, None), \
            ("bPos Limit Invert", cf.zLimPosInv, None), \
        )

        if DRO:
            self.fields += (
                ("DRO Inch", cf.zDROInch, 'd'), \
                ("bInv DRO", cf.zInvDRO, None), \
                ("bDRO Position", cf.zDROPos, None), \
                ("DRO Final Dist", cf.zDroFinalDist, 'f'), \
                ("DRO Read Delay ms", cf.zDoneDelay, None), \
        )

        sizerG = wx.FlexGridSizer(cols=4, rows=0, vgap=0, hgap=0)

        fieldList(self, sizerG, self.fields, 2)

        sizerV.Add(sizerG, flag=wx.LEFT|wx.ALL, border=2)

        addSetupButton(self, sizerV, 'Setup Z', OnDialogSetup, border=5)

        sizerH = wx.BoxSizer(wx.HORIZONTAL)
        sizerH.Add((0, 0), 0, wx.EXPAND)

        addDialogButton(self, sizerH, wx.ID_OK, OnDialogOk)

        addDialogButton(self, sizerH, wx.ID_CANCEL, OnDialogCancel)

        sizerV.Add(sizerH, 0, wx.ALIGN_RIGHT)

        self.SetSizer(sizerV)
        self.sizerV.Fit(self)
        self.Show(False)

    def OnEnter(self, _):
        OnEnter(self)

    def setupVars(self):
        cfg = self.mf.cfg
        pitch = cfg.getDistInfoData(cf.zPitch)
        motorSteps = cfg.getIntInfoData(cf.zMotorSteps)
        microSteps = cfg.getIntInfoData(cf.zMicroSteps)
        motorRatio = cfg.getFloatInfoData(cf.zMotorRatio)
        stepsInch = (microSteps * motorSteps * motorRatio) / pitch
        self.mf.zStepsInch = stepsInch
        self.mf.jogPanel.zStepsInch = stepsInch
        print("zStepsInch %d" % (stepsInch,))
        if DRO:
            droInch = cfg.getIntInfoData(cf.zDROInch)
            self.mf.zDROInch = droInch
            self.mf.jogPanel.zDROInch = droInch

    def setupAction(self):
        self.setupVars()
        self.mf.sendData.sendZData(True)

    def showAction(self, changed):
        if changed:
            self.mf.sendData.zDataSent = False

    def okAction(self):
        self.setupVars()

class XDialog(wx.Dialog, FormRoutines, DialogActions):
    def __init__(self, mainFrame, defaultFont):
        self.mf = mainFrame
        pos = (10, 10)
        wx.Dialog.__init__(self, mainFrame, -1, "X Setup", pos, \
                            wx.DefaultSize, wx.DEFAULT_DIALOG_STYLE)
        self.SetFont(defaultFont)
        FormRoutines.__init__(self)
        DialogActions.__init__(self)
        self.Bind(wx.EVT_SHOW, OnDialogShow)
        self.sizerV = sizerV = wx.BoxSizer(wx.VERTICAL)

        self.fields = (
            ("Pitch", cf.xPitch, 'f'), \
            ("Motor Steps", cf.xMotorSteps, 'd'), \
            ("Micro Steps", cf.xMicroSteps, 'd'), \
            ("Motor Ratio", cf.xMotorRatio, 'fs'), \

            ("Backlash", cf.xBacklash, 'f'), \
            ("Backlash Increment", cf.xBackInc, 'f'), \

            ("Accel Unit/Sec2", cf.xAccel, 'fs'), \
            ("Min Speed U/Min", cf.xMinSpeed, 'fs'), \
            ("Max Speed U/Min", cf.xMaxSpeed, 'fs'), \
            ("Jog Min U/Min", cf.xJogMin, 'fs'), \
            ("Jog Max U/Min", cf.xJogMax, 'fs'), \
            ("MPG Jog Increment", cf.xMpgInc, 'fs'), \
            ("MPG Jog Max Dist", cf.xMpgMax, 'fs'), \

            ("bInvert Dir", cf.xInvDir, None), \
            ("bInvert MPG", cf.xInvMpg, None), \

            ("Retract Loc", cf.xRetractLoc, 'f'), \
            ("Probe Dist", cf.xProbeDist, 'f'), \
            ("Home/Probe Speed", cf.xHomeSpeed, 'fs'), \

            ("bHome Enable", cf.xHomeEna, None), \
            ("bHome Invert", cf.xHomeInv, None), \
            ("Home Dist", cf.xHomeDist, 'f'), \
            ("Home Rev Dist", cf.xHomeDistRev, 'f'), \
            ("Backoff Dist", cf.xHomeDistBackoff, 'f'), \
            ("bHome Dir", cf.xHomeDir, None), \

            ("bLimits Enable", cf.xLimEna, None), \
            ("bNeg Limit Invert", cf.xLimNegInv, None), \
            ("bPos Limit Invert", cf.xLimPosInv, None), \
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

        sizerG = wx.FlexGridSizer(cols=4, rows=0, vgap=0, hgap=0)

        fieldList(self, sizerG, self.fields, 2)

        sizerV.Add(sizerG, flag=wx.LEFT|wx.ALL, border=2)

        if HOME_TEST:
            addButton(self, sizerV, 'Set Home Loc', self.OnSetHomeLoc, border=5)

        addSetupButton(self, sizerV, 'Setup X', OnDialogSetup, border=5)

        sizerH = wx.BoxSizer(wx.HORIZONTAL)

        sizerH.Add((0, 0), 0, wx.EXPAND)

        addDialogButton(self, sizerH, wx.ID_OK, OnDialogOk)

        addDialogButton(self, sizerH, wx.ID_CANCEL, OnDialogCancel)

        sizerV.Add(sizerH, 0, wx.ALIGN_RIGHT)

        self.SetSizer(sizerV)
        self.sizerV.Fit(self)
        self.Show(False)

    def OnEnter(self, _):
        OnEnter(self)

    def OnSetHomeLoc(self, _):
        loc = str(int(self.mf.cfg.getFloatInfoData(cf.xHomeLoc) * \
                      self.mf.jogPanel.xStepsInch))
        self.mf.comm.setParm(pm.X_HOME_LOC, loc)

    def setupVars(self):
        cfg = self.mf.cfg
        pitch = cfg.getDistInfoData(cf.xPitch)
        motorSteps = cfg.getIntInfoData(cf.xMotorSteps)
        microSteps = cfg.getIntInfoData(cf.xMicroSteps)
        motorRatio = cfg.getFloatInfoData(cf.xMotorRatio)
        stepsInch = (microSteps * motorSteps * motorRatio) / pitch
        self.mf.xStepsInch = stepsInch
        self.mf.jogPanel.xStepsInch = stepsInch
        if DRO:
            droInch = cfg.getIntInfoData(cf.xDROInch)
            self.mf.xDROInch = droInch
            self.mf.jogPanel.xDROInch = droInch

    def setupAction(self):
        self.setupVars()
        self.mf.sendData.sendXData(True)

    def showAction(self, changed):
        if changed:
            self.mf.sendData.xDataSent = False

    def okAction(self):
        self.setupVars()

class SpindleDialog(wx.Dialog, FormRoutines, DialogActions):
    def __init__(self, mainFrame, defaultFont):
        self.mf = mainFrame
        pos = (10, 10)
        wx.Dialog.__init__(self, mainFrame, -1, "Spindle Setup", pos, \
                            wx.DefaultSize, wx.DEFAULT_DIALOG_STYLE)
        self.SetFont(defaultFont)
        FormRoutines.__init__(self)
        DialogActions.__init__(self)
        self.Bind(wx.EVT_SHOW, OnDialogShow)
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
                self.fields += (("bSync Board", cf.cfgSpSyncBoard, None), \
                                ("bInternal Sync", cf.cfgIntSync, None), \
                                )
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
                ("Jog Time Increment", cf.spJTimeInc, 'f2'), \
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
            if MEGA:
                self.fields += ( \
                    ("bMega Encoder", cf.spMegaSim, None), \
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
        fieldList(self, sizerG, self.fields)

        sizerV.Add(sizerG, flag=wx.LEFT|wx.ALL, border=2)

        # spindle start and stop

        if STEP_DRV:
            sizerH = wx.BoxSizer(wx.HORIZONTAL)

            addButton(self, sizerH, 'Start', self.OnStart, border=5)

            addButton(self, sizerH, 'Stop', self.OnStop, border=5)

            sizerV.Add(sizerH, 0, wx.CENTER)

        # ok and cancel buttons

        sizerH = wx.BoxSizer(wx.HORIZONTAL)

        addDialogButton(self, sizerH, wx.ID_OK, OnDialogOk)

        addDialogButton(self, sizerH, wx.ID_CANCEL, OnDialogCancel)

        sizerV.Add(sizerH, 0, wx.ALIGN_RIGHT)

        self.SetSizer(sizerV)
        self.sizerV.Fit(self)

    def OnEnter(self, _):
        OnEnter(self)

    def OnStart(self, _):
        mf = self.mf
        if not formatData(self.mf.cfg, self.fields):
            return
        for (label, index, fmt) in self.fields:
            tmp = mf.cfg.getInfoData(index)
            if self.fieldInfo[index] != tmp:
                self.fieldInfo[index] = tmp
                mf.sendData.spindleDataSent = False
        if not self.mf.senData.spindleDataSent:
            mf.sendData.sendSpindleData()
        else:
            mf.comm.command(cm.C_CMD_SPSETUP)
        mf.comm.command(cm.C_SPINDLE_START)

    def OnStop(self, _):
        self.mf.comm.command(cm.C_SPINDLE_STOP)

    def showAction(self, changed):
        if changed:
            self.mf.syncFuncSetup()
            self.mf.jogPanel.spindleRangeSetup()
            self.mf.sendData.spindleDataSent = False

    def okAction(self):
        self.mf.syncFuncSetup()

    @staticmethod
    def turnSync():
        if STEP_DRV:
            indexList = (en.SEL_TU_STEP,)
        elif SPINDLE_ENCODER:
            indexList = (en.SEL_TU_ENC,)
            if not FPGA:
                if SPINDLE_INTERNAL_SYNC:
                    indexList += (en.SEL_TU_ISYN,)
                if SPINDLE_SYNC_BOARD:
                    indexList += (en.SEL_TU_ESYN,)
            else:
                indexList += (en.SEL_TU_SYN,)
        else:
            indexList = (en.SEL_TU_SPEED,)

        choiceList = []
        for i in indexList:
            choiceList.append(en.selTurnText[i])
        return( indexList, choiceList, en.selTurnText)

    @staticmethod
    def threadSync():
        if STEP_DRV:
            indexList = (en.SEL_TH_STEP,)
        elif SPINDLE_ENCODER:
            indexList = (en.SEL_TH_ENC,)
            if not FPGA:
                if SPINDLE_INTERNAL_SYNC:
                    indexList += (en.SEL_TH_ISYN_RENC,)
                if SPINDLE_SYNC_BOARD:
                    indexList += (en.SEL_TH_ESYN_RENC, en.SEL_TH_ESYN_RSYN)
            else:
                indexList = (en.SEL_TH_ENC, en.SEL_TH_SYN)
        else:
            indexList = (en.SEL_TH_NO_ENC,)

        choiceList = []
        for i in indexList:
            choiceList.append(en.selThreadText[i])
        return (indexList, choiceList, en.selThreadText)

class PortDialog(wx.Dialog, FormRoutines, DialogActions):
    def __init__(self, mainFrame, defaultFont):
        self.mf = mainFrame
        pos = (10, 10)
        wx.Dialog.__init__(self, mainFrame, -1, "Port Setup", pos, \
                            wx.DefaultSize, wx.DEFAULT_DIALOG_STYLE)
        self.SetFont(defaultFont)
        FormRoutines.__init__(self)
        DialogActions.__init__(self)
        self.Bind(wx.EVT_SHOW, OnDialogShow)
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
        fieldList(self, sizerG, self.fields)

        sizerV.Add(sizerG, flag=wx.LEFT|wx.ALL, border=2)
        sizerH = wx.BoxSizer(wx.HORIZONTAL)
        sizerH.Add((0, 0), 0, wx.EXPAND)

        addDialogButton(self, sizerH, wx.ID_OK, OnDialogOk)

        addDialogButton(self, sizerH, wx.ID_CANCEL, OnDialogCancel)

        sizerV.Add(sizerH, 0, wx.ALIGN_RIGHT)

        self.SetSizer(sizerV)
        self.sizerV.Fit(self)
        self.Show(False)

    def OnEnter(self, _):
        OnEnter(self)

    def showAction(self, changed):
        pass

class ConfigDialog(wx.Dialog, FormRoutines, DialogActions):
    def __init__(self, mainFrame, defaultFont):
        self.mf = mainFrame
        pos = (10, 10)
        wx.Dialog.__init__(self, mainFrame, -1, "Config Setup", pos, \
                           wx.DefaultSize, wx.DEFAULT_DIALOG_STYLE)
        self.SetFont(defaultFont)
        FormRoutines.__init__(self)
        DialogActions.__init__(self)
        self.Bind(wx.EVT_SHOW, OnDialogShow)
        self.sizerV = sizerV = wx.BoxSizer(wx.VERTICAL)
        sizerG = wx.FlexGridSizer(cols=2, rows=0, vgap=0, hgap=0)

        self.fields = (
            ("bFPGA Control", cf.cfgFpga, None), \
            ("bMPG", cf.cfgMPG, None), \
            ("bDRO", cf.cfgDRO, None), \
            ("bExternal DRO", cf.cfgExtDro, None), \
            ("bLCD", cf.cfgLCD, None), \
            ("bControl MEGA", cf.cfgMega, None), \
            ("bSync SPI", cf.cfgSyncSPI, None), \
            ("bProbe Inv", cf.cfgPrbInv, None), \
            ("wFcy", cf.cfgFcy, 'd'), \
            ("bDisable Commands", cf.cfgCmdDis, None), \
            ("bDraw Moves", cf.cfgDraw, None), \
            ("bSave Debug", cf.cfgDbgSave, None), \
            ("bRemote Debug", cf.cfgRemDbg, None), \
            ("bHome in Place", cf.cfgHomeInPlace, None), \
            ("Taper Cycle Dist", cf.cfgTaperCycleDist, 'f'), \
            ("Jog Time Initial", cf.jogTimeInitial, 'f2'), \
            ("Jog Time Increment", cf.jogTimeInc, 'f2'), \
            ("Jog Time Maximum", cf.jogTimeMax, 'f2'), \
            ("bMpg Jog Debug", cf.cfgJogDebug, None), \

            ("bCommon Limits", cf.cfgCommonLimits, None), \
            ("bLimits Enabled", cf.cfgLimitsEnabled, None), \
            ("bCommon Home", cf.cfgCommonHome, None), \

            ("bEnable EStop", cf.cfgEStop, None), \
            ("bInvert EStop", cf.cfgEStopInv, None), \
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
        fieldList(self, sizerG, self.fields)

        sizerV.Add(sizerG, flag=wx.CENTER|wx.ALL, border=2)

        sizerH = wx.BoxSizer(wx.HORIZONTAL)
        sizerH.Add((0, 0), 0, wx.EXPAND)

        addDialogButton(self, sizerH, wx.ID_OK, OnDialogOk)

        addDialogButton(self, sizerH, wx.ID_CANCEL, OnDialogCancel)

        sizerV.Add(sizerH, 0, wx.ALIGN_RIGHT)

        self.SetSizer(sizerV)
        self.sizerV.Fit(self)
        self.Show(False)

    def OnEnter(self, _):
        OnEnter(self)

    def showAction(self, changed):
        pass

    def okAction(self):
        mf = self.mf
        mf.dbgSave = bool(mf.cfg.getBoolInfoData(cf.cfgDbgSave))
        mf.cfgDraw = bool(mf.cfg.getBoolInfoData(cf.cfgDraw))

class MegaDialog(wx.Dialog, FormRoutines, DialogActions):
    def __init__(self, mainFrame, defaultFont):
        self.mf = mainFrame
        pos = (10, 10)
        wx.Dialog.__init__(self, mainFrame, -1, "Mega Setup", pos, \
                           wx.DefaultSize, wx.DEFAULT_DIALOG_STYLE)
        self.SetFont(defaultFont)
        FormRoutines.__init__(self)
        DialogActions.__init__(self)
        self.Bind(wx.EVT_SHOW, OnDialogShow)
        self.sizerV = sizerV = wx.BoxSizer(wx.VERTICAL)
        sizerG = wx.FlexGridSizer(cols=2, rows=0, vgap=0, hgap=0)

        self.fields = ( \
            ("cVFD Speed", cf.cfgMegaVFD, 'c', self.vfdSpeed), \
            ("bMega Encoder Test", cf.cfgMegaEncTest, None), \
            ("Mega Encoder Lines", cf.cfgMegaEncLines, 'd'), \
       )
        fieldList(self, sizerG, self.fields)

        sizerV.Add(sizerG, flag=wx.CENTER|wx.ALL, border=2)

        addSetupButton(self, sizerV, 'Setup Mega', OnDialogSetup, \
                       size=(80, -1), border=5)

        sizerH = wx.BoxSizer(wx.HORIZONTAL)
        sizerH.Add((0, 0), 0, wx.EXPAND)

        addDialogButton(self, sizerH, wx.ID_OK, OnDialogOk)

        addDialogButton(self, sizerH, wx.ID_CANCEL, OnDialogCancel)

        sizerV.Add(sizerH, 0, wx.ALIGN_RIGHT)

        self.SetSizer(sizerV)
        self.sizerV.Fit(self)
        self.Show(False)

    def OnEnter(self, _):
        OnEnter(self)

    def setupAction(self):
        if formatData(self.mf.cfg, self.fields):
            changed = saveData(self)
            print("MegaDialog setupAction changed %s" % (changed))
            self.mf.sendData.sendMegaData(True)

    def showAction(self, changed):
        pass

    @staticmethod
    def vfdSpeed():
        indexList = (em.MEGA_SLOW_PWM, em.MEGA_FAST_PWM, em.MEGA_DIRECT_RPM)
        choiceList = []
        for i in indexList:
            choiceList.append(em.vfdSpeedText[i])
        return (indexList, choiceList, em.vfdSpeedText)

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
    def __init__(self, mainFrame, defaultFont):
        pos = (10, 10)
        wx.Dialog.__init__(self, mainFrame, -1, "Test Spindle", pos, \
                            wx.DefaultSize, wx.DEFAULT_DIALOG_STYLE)

        self.sizerV = None
        txt = testText(self, defaultFont)
        self.spindleTest = SpindleTest(mainFrame, txt)

class TestSyncDialog(wx.Dialog):
    def __init__(self, mainFrame, defaultFont):
        pos = (10, 10)
        wx.Dialog.__init__(self, mainFrame, -1, "Test Sync", pos, \
                            wx.DefaultSize, wx.DEFAULT_DIALOG_STYLE)

        self.sizerV = None
        txt = testText(self, defaultFont)
        self.syncTest = SyncTest(mainFrame, txt)

class TestTaperDialog(wx.Dialog):
    def __init__(self, mainFrame, defaultFont):
        pos = (10, 10)
        wx.Dialog.__init__(self, mainFrame, -1, "Test Taper", pos, \
                            wx.DefaultSize, wx.DEFAULT_DIALOG_STYLE)

        self.sizerV = None
        txt = testText(self, defaultFont)
        self.taperTest = TaperTest(mainFrame, txt)

class TestMoveDialog(wx.Dialog):
    def __init__(self, mainFrame, defaultFont):
        pos = (10, 10)
        wx.Dialog.__init__(self, mainFrame, -1, "Test Move", pos, \
                            wx.DefaultSize, wx.DEFAULT_DIALOG_STYLE)

        self.sizerV = None
        txt = testText(self, defaultFont)
        self.moveTest = MoveTest(mainFrame, txt)

class SpindleTest():
    def __init__(self, mainFrame, txt):
        self.mf = mainFrame
        self.txt = txt

    def test(self):
        txt = self.txt
        txt.SetValue("")

        self.mf.dbgOpen('spindle.txt')
        fTest = self.mf.fTest
        dbgPrt = self.mf.dbgPrt

        cfg = self.mf.cfg
        minRPM = cfg.getFloatInfoData(cf.spMinRPM) # minimum rpm
        maxRPM = cfg.getFloatInfoData(cf.spMaxRPM) # maximum rpm
        accel = cfg.getFloatInfoData(cf.spAccel)   # accel rpm per sec

        dbgPrt(txt, "minRPM %d maxRPM %d", (minRPM, maxRPM))

        spindleMicroSteps = cfg.getIntInfoData(cf.spMicroSteps)
        spindleMotorSteps = cfg.getIntInfoData(cf.spMotorSteps)
        spindleStepsRev = spindleMotorSteps * spindleMicroSteps
        dbgPrt(txt, "spindleStepsRev %d", (spindleStepsRev))

        fcy = cfg.getIntInfoData(cf.cfgFcy)
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
        # noinspection PyUnreachableCode
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

        fTest.write("\n")

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
            fTest.write("step %4d count %9d %9d pre %d %5d %6d t %8.6f %8.6f "\
                        "f %8.2f rpm %4.1f\n" % \
                        (step, count, actCount, pre, ctr, ctr * pre - lastCtr, \
                         time0, delta, freq, rpm))
            lastCount = actCount
            lastCtr = ctr * pre
            lastTime = time0

        fTest.write("\n")

        finalCount = int(cFactor * sqrt(accelMaxSteps))
        finalCount -= int(cFactor * sqrt(accelMaxSteps - 1))
        dbgPrt(txt, "finalCount %d lastCtr %d spindleClocksStep %d", \
               (finalCount, ctr, spindleClocksStep))

        fTest.write("\n***\n\n")

        while step > accelMinSteps:
            step -= 1
            count = int(cFactor * sqrt(step))
            ctr = lastCount - count
            time0 = float(count) / fcy
            delta = lastTime - time0
            freq = 1.0 / delta
            rpm = (freq / spindleStepsRev) * 60
            fTest.write("step %4d count %9d %7d %5d t %8.6f %8.6f "\
                        "f %8.2f rpm %4.1f\n" % \
                        (step, count, ctr, ctr - lastCtr, time0, delta, \
                         freq, rpm))
            lastCount = count
            lastCtr = ctr
            lastTime = time0

        lastCount = int(cFactor * sqrt(accelMinSteps))
        fTest.write("\naccelMinSteps %d lastCount %d\n" % \
                    (accelMinSteps, lastCount))

        self.mf.dbgClose()

class SyncTest(object):
    def __init__(self, mainFrame, txt):
        self.mf = mainFrame
        self.txt = txt

    def test(self):
        txt = self.txt
        txt.SetValue("")

        self.mf.dbgOpen('zsync.txt')
        fTest = self.mf.fTest
        dbgPrt = self.mf.dbgPrt

        zAxis = True
        cfg = self.mf.cfg
        arg1 = 20
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

        fcy = cfg.getIntInfoData(cf.cfgFcy)
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

        inchPitch = True
        tpi = 20
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

            fTest.write("\n")

            lastCount = 0
            lastTime = 0
            lastCtr = 0
            # dbgPrt(txt, "lastCount %d lastTime %0.6f" % (lastCount, lastTime)
            count = 0
            for step in range(1, zAccelSteps + 1):
                count = int(cFactor1 * sqrt(step))
                ctr = count - lastCount
                time0 = float(count) / fcy
                delta = time0 - lastTime
                freq = 1.0 / delta
                ipm = (freq / zStepsInch) * 60
                fTest.write("step %4d count %9d %9d %9d t %8.6f %8.6f "\
                            "f %7.2f ipm %4.1f\n" % \
                            (step, count, ctr, ctr - lastCtr, time0, delta, \
                             freq, ipm))
                lastCount = count
                lastCtr = ctr
                lastTime = time0

            fTest.write("\n")

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

        self.mf.dbgClose()

class TaperTest(object):
    def __init__(self, mainFrame, txt):
        self.mf = mainFrame
        self.txt = txt

    def test(self):
        txt = self.txt
        txt.SetValue("")

        self.mf.dbgOpen('taper.txt')
        # fTest = self.mf.fTest
        dbgPrt = self.mf.dbgPrt

        cfg = self.mf.cfg
        maxRPM = cfg.getFloatInfoData(cf.spMaxRPM) # maximum rpm
        spindleMicroSteps = cfg.getIntInfoData(cf.spMicroSteps)
        spindleMotorSteps = cfg.getIntInfoData(cf.spMotorSteps)
        spindleStepsRev = spindleMotorSteps * spindleMicroSteps
        dbgPrt(txt, "spindleStepsRev %d", (spindleStepsRev))

        fcy = cfg.getIntInfoData(cf.cfgFcy)
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

        self.mf.dbgClose()

class MoveTest(object):
    def __init__(self, mainFrame, txt):
        self.mf = mainFrame
        self.txt = txt

    def test(self):
        txt = self.txt
        txt.SetValue("")

        self.mf.dbgOpen('move.txt')
        fTest = self.mf.fTest
        dbgPrt = self.mf.dbgPrt

        cfg = self.mf.cfg
        pitch = cfg.getDistInfoData(cf.zPitch)
        microSteps = cfg.getFloatInfoData(cf.zMicroSteps)
        motorSteps = cfg.getFloatInfoData(cf.zMotorSteps)
        motorRatio = cfg.getFloatInfoData(cf.zMotorRatio)
        fcy = cfg.getIntInfoData(cf.cfgFcy)

        zStepsInch = ((microSteps * motorSteps * motorRatio) / pitch)
        dbgPrt(txt, "fcy %d zStepsInch %d", (fcy, zStepsInch))

        minSpeed = cfg.getFloatInfoData(cf.zMinSpeed) # minimum speed ipm
        maxSpeed = cfg.getFloatInfoData(cf.zMaxSpeed) # maximum speed ipm
        # (in / min) / ((sec / min) * (in / sec^2))
        # (in / min) * ((min / sec) * ((sec * sec) / in)))
        #  22   111      111   333            333    22
        zAccel = cfg.getFloatInfoData(cf.zAccel) # accel time seconds
        zMoveAccelTime = (maxSpeed - minSpeed) / (60 * zAccel)
        dbgPrt(txt, "zMinSpeed %d zMaxSpeed %d zMoveAccel %3.0f zMoveAccelTime %4.3f", \
               (minSpeed, maxSpeed, zAccel, zMoveAccelTime))

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
        dbgPrt(txt, "zMDeltaV %d zMAccelStepsSec2 %6.0f", \
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

            fTest.write("\n")

            lastCtr = 0
            ctr = 0
            step = zMAccelMinSteps
            while step < zMAccelMaxSteps:
                step += 1
                count = int(zMCFactor * sqrt(step))
                ctr = count - lastCount
                time0 = float(count) / fcy
                delta = time0 - lastTime
                freq = 1.0 / delta
                ipm = (freq / zStepsInch) * 60
                fTest.write("step %4d count %9d %8d %8d t %8.6f %8.6f "\
                            "f %7.2f ipm %3.1f\n" % \
                            (step, count, ctr, abs(ctr - lastCtr), time0, \
                             delta, freq, ipm))
                lastCount = count
                lastCtr = ctr
                lastTime = time0

            fTest.write("\n")

            finalCount = int(zMCFactor * (sqrt(zMAccelSteps) -
                                          sqrt(zMAccelSteps - 1)))
            dbgPrt(txt, "finalCount %d lastCtr %d zMClocksStep %d", \
                   (finalCount, ctr, zMClocksStep))

            fTest.write("\n***\n\n")

            while step > zMAccelMinSteps:
                step -= 1
                count = int(zMCFactor * sqrt(step))
                ctr = lastCount - count
                time0 = float(count) / fcy
                delta = lastTime - time0
                freq = 1.0 / delta
                ipm = (freq / zStepsInch) * 60
                fTest.write("step %4d count %9d %7d %7d t %8.6f %8.6f "\
                            "f %7.2f ipm %3.1f\n" % \
                            (step, count, ctr, abs(ctr - lastCtr), time0, \
                             delta, freq, ipm))
                lastCount = count
                lastCtr = ctr
                lastTime = time0

            lastCount = int(zMCFactor * sqrt(zMAccelMinSteps))
            fTest.write("\nzMAccelMinSteps %d lastCount %d\n" % \
                        (zMAccelMinSteps, lastCount))

            self.mf.dbgClose()

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
        frame = MainFrame(None, "Lathe Control")
        frame.Show(True)
        self.SetTopWindow(frame)
        return True

    def FilterEvent(self, evt):
        if evt.EventType == wx.EVT_KEY_DOWN:
            print(evt)
        return(-1)

app = MainApp(redirect=False)
# app.SetCallFilterEvent(True)
# wx.lib.inspection.InspectionTool().Show()
app.MainLoop()
