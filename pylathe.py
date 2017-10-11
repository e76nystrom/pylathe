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
import traceback
from sys import stdout, stderr
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

from configInfo import ConfigInfo, InfoValue
from comm import Comm, CommTimeout

SWIG = False
HOME_TEST = False
SETUP = False
configFile = "config.txt"
posFile = "posInfo.txt"

if SETUP:
    from interface import configList, strList, cmdList, parmList, \
        enumList, regList
else:
    import configDef as cf
    import stringDef as st
    import cmdDef as cm
    import parmDef as pm
    import enumDef as en
    import ctlBitDef as ct

if SETUP:
    from setup import Setup
    setup = Setup()
    (config, configTable) = setup.createConfig(configList)

cfg = ConfigInfo(cf.configTable)
cfg.clrInfo(len(cf.config))
cfg.readInfo(configFile, cf.config)

if SETUP:
    setupCmd = "from setup import "
    for var in setup.configImports:
        setupCmd += var + ","
    exec(setupCmd[:-1])

XILINX = cfg.getInitialBoolInfo(cf.cfgXilinx)
DRO = cfg.getInitialBoolInfo(cf.cfgDRO)
REM_DBG = cfg.getInitialBoolInfo(cf.cfgRemDbg)
STEP_DRV = cfg.getInitialBoolInfo(cf.spStepDrive)
MOTOR_TEST = cfg.getInitialBoolInfo(cf.spMotorTest)

cfg.clrInfo(len(cf.config))

cLoc = "../Lathe/include/"
fData = False

if SETUP:
    setup.createCommands(cmdList, cLoc, fData)
    setup.createStrings(strList)
    setup.createParameters(parmList, cLoc, fData)
    setup.createCtlBits(regList, cLoc, fData)
    setup.createEnums(enumList, cLoc, fData)
    if XILINX:
        xLoc = '../../Xilinx/LatheCtl/'
        from interface import xilinxList, xilinxBitList
        setup.createXilinxReg(xilinxList, cLoc, xLoc, fData)
        setup.createXilinxBits(xilinxBitList, cLoc, xLoc, fData)

    importList = setup.importList
    setupCmd = "from setup import "
    for var in importList:
        setupCmd += var + ","
    exec(setupCmd[:-1])
else:
    if XILINX:
        import xBitDef.py as xb
        import xRegDef.py as xr

comm = Comm()
comm.SWIG = SWIG

if XILINX:
    comm.enableXilinx()

if SWIG:
    import lathe
    from lathe import taperCalc, T_ACCEL, zTaperInit, xTaperInit

print(sys.version)
print(wx.version())
stdout.flush()

f = None
mainFrame = None
updateThread = None
jogPanel = None
spindleDataSent = False
zDataSent = False
xDataSent = False
zPosition = 0.0
zHomeOffset = 0.0
xPosition = 0.0
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

JOG_Z = 0
JOG_X = 1
JOG_SPINDLE = 2

def commTimeout():
    jogPanel.setStatus(st.STR_TIMEOUT_ERROR)

class FormRoutines():
    def __init__(self, panel=True):
        self.emptyCell = (0, 0)
        self.configList = None
        self.prefix = ""
        self.focusField = None

    def formatData(self, formatList):
        success = True
        for fmt in formatList:
            if len(fmt) == 2:
                (index, fieldType) = fmt
            else:
                (name, index, fieldType) = fmt
            if fieldType is None:
                continue
            ctl = cfg.info[index]
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
                fmt = "%%0.%df" % digits

                try:
                    val = float(strVal)
                    val = fmt % (val)
                    if strip:
                        if re.search("\.0*$", val):
                            val = re.sub("\.0*$", "", val)
                        else:
                            val = val.rstrip('0')
                    ctl.SetValue(val)
                except ValueError:
                    success = False
                    strVal = ''
                    ctl.SetValue('')
            elif fieldType == 'd':
                try:
                    val = int(strVal)
                    ctl.SetValue("%d" % (val))
                except ValueError:
                    success = False
                    strVal = ''
                    ctl.SetValue('')
            cfg.setInfoData(index, strVal)
        return(success)

    def fieldList(self, sizer, fields):
        for (label, index, fmt) in fields:
            if label.startswith('b'):
                self.addCheckBox(sizer, label[1:], index)
            else:
                if label.startswith('w'):
                    self.addField(sizer, label[1:], index, (80, -1))
                else:
                    self.addField(sizer, label, index)

    def getConfigList(self):
        if self.configList is None:
            self.configList = []
            for i, (name) in enumerate(cf.configTable):
                if name.startswith(self.prefix):
                    self.configList.append(i)
        return(self.configList)

    def addFieldText(self, sizer, label, key, keyText):
        if len(label) != 0:
            txt = wx.StaticText(self, -1, label)
            sizer.Add(txt, flag=wx.ALL|wx.ALIGN_RIGHT|\
                      wx.ALIGN_CENTER_VERTICAL, border=2)
            cfg.initInfo(keyText, txt)

        tc = wx.TextCtrl(self, -1, "", size=(60, -1), \
                         style=wx.TE_PROCESS_ENTER)
        tc.Bind(wx.EVT_TEXT_ENTER, self.OnEnter)
        sizer.Add(tc, flag=wx.ALL, border=2)
        cfg.initInfo(key, tc)
        return(tc)

    def addField(self, sizer, label, index, size=(60, -1)):
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
        if self.formatData(self.formatList):
            jogPanel.setStatus(st.STR_CLR)
            jogPanel.focus()
        else:
            jogPanel.setStatus(st.STR_FIELD_ERROR)
            
class ActionRoutines():
    def __init__(self, control):
        self.control = control
        self.active = False
        self.Bind(wx.EVT_SHOW, self.OnShow)
        self.safeX = None
        self.safeZ = None
        self.formatList = None

    def formatData(self, formatList):
        pass

    def sendAction(self):
        return(False)

    def startAction(self):
        pass

    def addAction(self):
        pass

    def update(self):
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
                # except AttributeError:
                #     pass
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
                pass
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
                pass
        jogPanel.focus()

class DialogActions():
    def __init__(self):
        self.fields = None
        self.fieldInfo = None
        self.sendData = False
        self.changed = False
        self.Bind(wx.EVT_SHOW, self.OnShow)

    def setupAction(self):
        pass

    def showAction(self, changed):
        pass

    def formatData(self, fields):
        pass

    def OnSetup(self, e):
        if not self.formatData(self.fields):
            return
        moveCommands.queClear()
        try:
            if callable(self.setupAction):
                self.setupAction()
        except AttributeError:
            pass

    def OnShow(self, e):
        if done:
            return
        changed = False
        if self.IsShown():
            self.changed = not self.formatData(self.fields)
            self.fieldInfo = {}
            for (label, index, fmt) in self.fields:
                self.fieldInfo[index] = cfg.getInfo(index)
        else:
            for (label, index, fmt) in self.fields:
                val = cfg.getInfo(index)
                if self.fieldInfo[index] != val:
                    cfg.setInfoData(index, val)
                    self.sendData = True
        if changed:
            try:
                if callable(self.showAction):
                    self.showAction(changed)
            except AttributeError:
                pass

    def OnCancel(self, e):
        for (label, index, fmt) in self.fields:
            cfg.setInfo(index, self.fieldInfo[index])
        self.Show(False)

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

class MoveCommands():
    def __init__(self):
        self.moveQue = Queue()
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
        self.style = None
        self.zOffset = 0.0
        self.xOffset = 0.0

    def draw(self, cmd, diam, parm):
        tmp = "%s%0.3f-%0.3f" % (cmd, diam, parm)
        tmp = tmp.replace(".", "-")
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
        if self.d is not None:
            self.lastX = x
            self.lastZ = z

    def drawLineX(self, x, layer=0):
        if self.d is not None:
            self.d.add(dxf.line((self.lastZ, self.lastX), \
                                (self.lastZ, x), layer=layer))
            self.lastX = x

    def drawLineZ(self, z, layer=0):
        if self.d is not None:
            self.d.add(dxf.line((self.lastZ, self.lastX), \
                                (z, self.lastX), layer=layer))
            self.lastZ = z

    def drawLine(self, z, x, layer=0):
        if self.d is not None:
            self.d.add(dxf.line((self.lastZ, self.lastX), \
                                (z, x), layer=layer))
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
        if self.d is not None:
            try:
                if self.d is not None:
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
                traceback.print_exc()

    def queMove(self, op, val):
        if self.send:
            opString = en.mCommandsList[op]
            self.moveQue.put((opString, op, val))

    def queMoveF(self, op, flag, val):
        if self.send:
            opString = en.mCommandsList[op]
            op |= (flag << 8)
            self.moveQue.put((opString, op, val))

    def queClear(self):
        self.send = not cfg.getBoolInfoData(cf.cfgCmdDis)
        while not self.moveQue.empty():
            self.moveQue.get()

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
                print("pass %d]" % (passNum))

    def quePause(self):
        self.queMove(en.QUE_PAUSE, 0)

    def saveDiameter(self, val):
        self.queMove(en.SAVE_DIAMETER, val)

    def moveZ(self, zLocation, flag=ct.CMD_MAX):
        self.queMoveF(en.MOVE_Z, flag, zLocation)
        self.drawLineZ(zLocation)
        if self.dbg:
            print("moveZ  %7.4f" % (zLocation))

    def moveX(self, xLocation, flag=ct.CMD_MAX):
        self.queMoveF(en.MOVE_X, flag, xLocation)
        self.drawLineX(xLocation)
        if self.dbg:
            print("moveX  %7.4f" % (xLocation))

    def saveZOffset(self):
        if self.zOffset != zHomeOffset:
            self.zOffset = zHomeOffset
            self.queMove(en.SAVE_Z_OFFSET, zHomeOffset)
            if self.dbg:
                print("saveZOffset  %7.4f" % (zHomeOffset))

    def saveXOffset(self):
        if self.xOffset != xHomeOffset:
            self.xOffset = xHomeOffset
            self.queMove(en.SAVE_X_OFFSET, xHomeOffset)
            if self.dbg:
                print("savexOffset  %7.4f" % (xHomeOffset))

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
        taper = "%0.6f" % (taper)
        self.queMove(en.SAVE_TAPER, taper)
        if self.dbg:
            print("saveTaper %s" % (taper))

    def saveRunout(self, runout):
        self.queMove(en.SAVE_RUNOUT, runout)
        if self.dbg:
            print("saveRunout %7.4f" % (runout))

    def saveDepth(self, depth):
        self.queMove(en.SAVE_DEPTH, depth)
        if self.dbg:
            print("saveDepth %7.4f" % (depth))

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
    try:
        if send or (not spindleDataSent):
            comm.queParm(pm.STEPPER_DRIVE, cfg.getBoolInfoData(cf.spStepDrive))
            comm.queParm(pm.MOTOR_TEST, cfg.getBoolInfoData(cf.spMotorTest))
            if STEP_DRV or MOTOR_TEST:
                comm.queParm(pm.SP_STEPS, cfg.getInfoData(cf.spMotorSteps))
                comm.queParm(pm.SP_MICRO, cfg.getInfoData(cf.spMicroSteps))
                comm.queParm(pm.SP_MIN_RPM, cfg.getInfoData(cf.spMinRPM))
                if rpm is not None:
                    comm.queParm(pm.SP_MAX_RPM, rpm)
                else:
                    comm.queParm(pm.SP_MAX_RPM, cfg.getInfoData(cf.spMaxRPM))

                comm.queParm(pm.SP_ACCEL, cfg.getInfoData(cf.spAccel))
                comm.queParm(pm.SP_JOG_MIN_RPM, cfg.getInfoData(cf.spJogMin))
                comm.queParm(pm.SP_JOG_MAX_RPM, cfg.getInfoData(cf.spJogMax))

                comm.queParm(pm.SP_DIR_FLAG, cfg.getBoolInfoData(cf.spInvDir))
                comm.queParm(pm.SP_TEST_INDEX, \
                             cfg.getBoolInfoData(cf.spTestIndex))
                comm.command(cm.CMD_SPSETUP)
            elif XILINX:
                comm.queParm(pm.ENC_MAX, cfg.getInfoData(cf.cfgEncoder))
                comm.queParm(pm.X_FREQUENCY, cfg.getInfoData(cf.cfgXFreq))
                comm.queParm(pm.FREQ_MULT, cfg.getInfoData(cf.cfgFreqMult))
                xilinxTestMode()
                comm.queParm(pm.RPM, cfg.getInfoData(cf.cfgTestRPM))
                cfgReg = 0
                if cfg.getBoolInfoData(cf.cfgInvEncDir):
                    cfgReg |= xb.ENC_POL
                if cfg.getBoolInfoData(cf.zInvDir):
                    cfgReg |= xb.ZDIR_POL
                if cfg.getBoolInfoData(cf.xInvDir):
                    cfgReg |= xb.XDIR_POL
                comm.queParm(pm.X_CFG_REG, cfgReg)
                comm.sendMulti()
            spindleDataSent = True
    except CommTimeout:
        commTimeout()

def sendZData(send=False):
    global zDataSent
    try:
        pitch = cfg.getFloatInfoData(cf.zPitch)
        motorSteps = cfg.getIntInfoData(cf.zMotorSteps)
        microSteps = cfg.getIntInfoData(cf.zMicroSteps)
        motorRatio = cfg.getFloatInfoData(cf.zMotorRatio)
        jogPanel.zStepsInch = (microSteps * motorSteps * \
                               motorRatio) / pitch
        # print("zStepsInch %0.2f" % (jogPanel.zStepsInch))

        if DRO:
            jogPanel.zDROInch = cfg.getIntInfoData(cf.zDROInch)
            jogPanel.zDROInvert = -1 if cfg.getBoolInfoData(cf.zInvDRO) else 1
        # stdout.flush()

        if send or (not zDataSent):
            if DRO:
                comm.queParm(pm.Z_DRO_INCH, jogPanel.zDROInch)
                comm.queParm(pm.X_DRO_DIR, jogPanel.zDROInvert)

            val = jogPanel.combo.GetValue()
            try:
                val = float(val)
                if val > 0.020:
                    val = 0.020
            except ValueError:
                val = 0.001
            comm.queParm(pm.Z_MPG_INC, val * jogPanel.zStepsInch)

            comm.queParm(pm.Z_PITCH, cfg.getInfoData(cf.zPitch))
            comm.queParm(pm.Z_RATIO, cfg.getInfoData(cf.zMotorRatio))
            comm.queParm(pm.Z_MICRO, cfg.getInfoData(cf.zMicroSteps))
            comm.queParm(pm.Z_MOTOR, cfg.getInfoData(cf.zMotorSteps))
            comm.queParm(pm.Z_ACCEL, cfg.getInfoData(cf.zAccel))
            comm.queParm(pm.Z_BACKLASH, cfg.getInfoData(cf.zBacklash))

            comm.queParm(pm.Z_MOVE_MIN, cfg.getInfoData(cf.zMinSpeed))
            comm.queParm(pm.Z_MOVE_MAX, cfg.getInfoData(cf.zMaxSpeed))

            comm.queParm(pm.Z_JOG_MIN, cfg.getInfoData(cf.zJogMin))
            comm.queParm(pm.Z_JOG_MAX, cfg.getInfoData(cf.zJogMax))

            comm.queParm(pm.Z_DIR_FLAG, cfg.getBoolInfoData(cf.zInvDir))
            comm.queParm(pm.Z_MPG_FLAG, cfg.getBoolInfoData(cf.zInvMpg))

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
    try:
        pitch = cfg.getFloatInfoData(cf.xPitch)
        motorSteps = cfg.getIntInfoData(cf.xMotorSteps)
        microSteps = cfg.getIntInfoData(cf.xMicroSteps)
        motorRatio = cfg.getFloatInfoData(cf.xMotorRatio)
        jogPanel.xStepsInch = (microSteps * motorSteps * \
                               motorRatio) / pitch
        # print("xStepsInch %0.2f" % (jogPanel.xStepsInch))
        if DRO:
            jogPanel.xDROInch = cfg.getIntInfoData(cf.xDROInch)
            jogPanel.xDROInvert = -1 if cfg.getBoolInfoData(cf.xInvDRO) else 1
        # stdout.flush()

        if send or (not xDataSent):
            if DRO:
                comm.queParm(pm.X_DRO_INCH, jogPanel.xDROInch)
                comm.queParm(pm.Z_DRO_DIR, jogPanel.xDROInvert)

            val = jogPanel.combo.GetValue()
            try:
                val = float(val)
                if val > 0.020:
                    val = 0.020
            except ValueError:
                val = 0.001
            comm.queParm(pm.X_MPG_INC, val * jogPanel.xStepsInch)

            comm.queParm(pm.X_PITCH, cfg.getInfoData(cf.xPitch))
            comm.queParm(pm.X_RATIO, cfg.getInfoData(cf.xMotorRatio))
            comm.queParm(pm.X_MICRO, cfg.getInfoData(cf.xMicroSteps))
            comm.queParm(pm.X_MOTOR, cfg.getInfoData(cf.xMotorSteps))
            comm.queParm(pm.X_ACCEL, cfg.getInfoData(cf.xAccel))
            comm.queParm(pm.X_BACKLASH, cfg.getInfoData(cf.xBacklash))

            comm.queParm(pm.X_MOVE_MIN, cfg.getInfoData(cf.xMinSpeed))
            comm.queParm(pm.X_MOVE_MAX, cfg.getInfoData(cf.xMaxSpeed))

            comm.queParm(pm.X_JOG_MIN, cfg.getInfoData(cf.xJogMin))
            comm.queParm(pm.X_JOG_MAX, cfg.getInfoData(cf.xJogMax))

            comm.queParm(pm.X_DIR_FLAG, cfg.getBoolInfoData(cf.xInvDir))
            comm.queParm(pm.X_MPG_FLAG, cfg.getBoolInfoData(cf.xInvMpg))

            if HOME_TEST:
                stepsInch = jogPanel.xStepsInch
                start = str(int(cfg.getFloatInfoData(cf.xHomeStart) * \
                                stepsInch))
                end = str(int(cfg.getFloatInfoData(cf.xHomeEnd) * stepsInch))
                if end > start:
                    (start, end) = (end, start)
                comm.queParm(pm.X_HOME_START, start)
                comm.queParm(pm.X_HOME_END, end)

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
        self.calcPass = None    # pass calculation routine
        self.genPass = None     # pass generation routine

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
        comm.setParm(pm.TOTAL_PASSES, self.passes)
        self.passSize = [None for i in range(self.passes + 1)]
        self.passSize[0] = 0.0
        self.passCount = 0
        self.sPassCtr = 0
        self.spring = 0
        self.feed = 0.0
        self.springFlag = False

    def updatePass(self):
        if (self.passCount < self.passes) or self.springFlag:
            if self.springFlag:
                self.springFlag = False
                moveCommands.nextPass(0x100 | self.passCount)
                self.genPass()
            else:
                self.passCount += 1
                moveCommands.nextPass(self.passCount)
                self.calcPass(self.passCount == self.passes)
                self.genPass()
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
                self.genPass()
            else:
                return(False)
        # print("updatePass %d %s" % (self.passCount, self.springFlag))
        return(True)

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

        self.zStart = getFloatVal(tu.zStart) / 2.0
        self.zEnd = getFloatVal(tu.zEnd) / 2.0
        self.zRetract = getFloatVal(tu.zRetract)

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
        self.setupAction(self.calculatePass, self.runPass)

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

        self.setup()

        while self.updatePass():
            pass

        self.m.moveX(self.xStart + self.xRetract)
        if STEP_DRV or MOTOR_TEST:
            self.m.stopSpindle()
        self.m.done(1)
        self.m.drawClose()
        stdout.flush()
        return(True)

    def setup(self):
        m = self.m
        m.setLoc(self.zEnd, self.xStart)
        m.drawLineZ(self.zStart, REF)
        m.drawLineX(self.xEnd, REF)
        m.setLoc(self.safeZ, self.safeX)
        m.quePause()
        self.m.done(0)
        if STEP_DRV:
            m.startSpindle(cfg.getIntInfoData(cf.tuRPM))
            m.queFeedType(ct.FEED_PITCH)
            m.zSynSetup(cfg.getFloatInfoData(cf.tuZFeed))
        else:
            m. queZSetup(cfg.getFloatInfoData(cf.tuZFeed))
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

    def calculatePass(self, final=False):
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
        print("pass %2d feed %5.3f x %5.3f diameter %5.3f" % \
              (self.passCount, feed, self.curX, self.curX * 2.0))
        stdout.flush()

    def runPass(self):
        m = self.m
        m.moveX(self.curX, ct.CMD_JOG)
        m.saveDiameter(self.curX * 2.0)
        if self.panel.pause.GetValue():
            print("pause")
            self.m.quePause()
        if m.passNum & 0x300 == 0:
            m.text("%2d %7.3f" % (m.passNum, self.curX * 2.0), \
                   (self.safeZ, self.curX))
        m.moveZ(self.zStart)
        m.moveZ(self.zEnd, ct.CMD_SYN)
        m.moveX(self.safeX)
        if m.passNum & 0x300 == 0:
            m.text("%2d %7.3f" % (m.passNum, self.safeX * 2.0), \
                   (self.zEnd, self.safeX), RIGHT)
        m.moveZ(self.safeZ)

    def addPass(self):
        if self.feed >= self.xCut:
            add = getFloatVal(self.panel.add)
            self.cutAmount += add
            self.calculatePass(True)
            self.setup()
            moveCommands.nextPass(self.passCount)
            self.runPass()
            self.m.moveX(self.xStart + self.xRetract)
            if STEP_DRV or MOTOR_TEST:
                self.m.stopSpindle()
            self.m.done(1)
            comm.command(cm.CMD_RESUME)

class TurnPanel(wx.Panel, FormRoutines, ActionRoutines):
    def __init__(self, parent, hdrFont, *args, **kwargs):
        super(TurnPanel, self).__init__(parent, *args, **kwargs)
        self.hdrFont = hdrFont
        FormRoutines.__init__(self)
        self.control = Turn(self)
        ActionRoutines.__init__(self, self.control)
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

        txt = wx.StaticText(self, -1, "Turn")
        txt.SetFont(self.hdrFont)

        sizerV.Add(txt, flag=wx.CENTER|wx.ALL, border=2)

        sizerG = wx.FlexGridSizer(8, 0, 0)

        # x parameters

        self.xDiam0 = self.addFieldText(sizerG, "X Start D", cf.tuXDiam0, \
                                        cf.tuXDiam0Text)
        self.focusField = self.xDiam0

        self.xDiam1 = self.addFieldText(sizerG, "X End D", cf.tuXDiam1, \
                                        cf.tuXDiam1Text)

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
            cfg.infoSetLabel(cf.tuXDiam0Text, "  X End D")
            cfg.infoSetLabel(cf.tuXDiam1Text, "X Start D")
        else:
            cfg.infoSetLabel(cf.tuXDiam0Text, "X Start D")
            cfg.infoSetLabel(cf.tuXDiam1Text, "  X End D")

    def update(self):
        self.updateUI()
        self.formatData(self.formatList)
        jogPanel.passText.SetLabel("Diam")

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

    def addAction(self):
        self.control.addPass()

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

    def runOperation(self):
        self.getParameters()

        self.internal = self.xStart < self.xEnd
        self.zCut = abs(self.zStart - self.zEnd)

        self.calcFeed(self.zFeed, self.zCut)
        self.setupSpringPasses(self.panel)
        self.setupAction(self.calculatePass, self.runPass)

        self.panel.passes.SetValue("%d" % (self.passes))
        print("zCut %5.3f passes %d internal %s" % \
              (self.zCut, self.passes, self.internal))

        if self.internal:
            self.xRetract = -self.xRetract
        self.safeX = self.xStart + self.xRetract
        self.safeZ = self.zStart + self.zRetract

        if cfg.getBoolInfoData(cf.cfgDraw):
            self.m.draw("face", self.xStart, self.xEnd)
            self.m.setTextAngle(90)

        self.setup()

        while self.updatePass():
            pass

        self.m.moveX(self.safeX)
        self.m.moveZ(self.zStart + self.zRetract)

        if STEP_DRV or MOTOR_TEST:
            self.m.stopSpindle()
        self.m.done(1)
        self.m.drawClose()
        stdout.flush()
        return(True)

    def setup(self):
        m = self.m
        m.setLoc(self.zEnd, self.xStart)
        m.drawLineZ(self.zStart, REF)
        m.drawLineX(self.xEnd, REF)
        m.setLoc(self.zStart, self.safeX)
        m.quePause()
        self.m.done(0)
        if STEP_DRV:
            m.startSpindle(cfg.getIntInfoData(cf.faRPM))
            m.queFeedType(ct.FEED_PITCH)
            m.xSynSetup(cfg.getFloatInfoData(cf.faXFeed))
        else:
            m.queXSetup(cfg.getFloatInfoData(cf.faXFeed))
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

    def calculatePass(self, final=False):
        feed = self.cutAmount if final else self.passCount * self.actualFeed
        self.feed = feed
        self.curZ = self.zStart - feed
        self.safeZ = self.curZ + self.zRetract
        self.passSize[self.passCount] = self.curZ
        print("pass %2d feed %5.3f z %5.3f" % \
              (self.passCount, feed, self.curZ))
        stdout.flush()

    def runPass(self):
        m = self.m
        m.moveZ(self.curZ, ct.CMD_JOG)
        if self.panel.pause.GetValue():
            print("pause")
            m.quePause()
        if m.passNum & 0x300 == 0:
            m.text("%2d %7.3f" % (m.passNum, self.curZ), \
                   (self.curZ, self.safeX), RIGHT if self.internal else None)
        m.moveX(self.xStart)
        m.moveX(self.xEnd, ct.CMD_SYN)
        m.moveZ(self.safeZ)
        if m.passNum & 0x300 == 0:
            m.text("%2d %7.3f" % (m.passNum, self.safeZ), \
                   (self.safeZ, self.xEnd), None if self.internal else RIGHT)
        m.moveX(self.safeX)

    def addPass(self):
        if self.feed >= self.zCut:
            add = getFloatVal(self.panel.add)
            self.cutAmount += add
            self.setup()
            self.calculatePass(True)
            moveCommands.nextPass(self.passCount)
            self.runPass()
            self.m.moveX(self.safeX)
            self.m.moveZ(self.zStart + self.zRetract)
            if STEP_DRV or MOTOR_TEST:
                self.m.stopSpindle()
            self.m.done(1)
            comm.command(cm.CMD_RESUME)

class FacePanel(wx.Panel, FormRoutines, ActionRoutines):
    def __init__(self, parent, hdrFont, *args, **kwargs):
        super(FacePanel, self).__init__(parent, *args, **kwargs)
        self.hdrFont = hdrFont
        FormRoutines.__init__(self)
        self.control = Face(self)
        ActionRoutines.__init__(self, self.control)
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

        txt = wx.StaticText(self, -1, "Face")
        txt.SetFont(self.hdrFont)

        sizerV.Add(txt, flag=wx.CENTER|wx.ALL, border=2)

        sizerG = wx.FlexGridSizer(8, 0, 0)

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
        jogPanel.passText.SetLabel("Len")

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
        if cfg.getBoolInfoData(cf.cfgDbgSave):
            updateThread.openDebug()

    def addAction(self):
        self.control.addPass()

class Cutoff(LatheOp):
    def __init__(self, cutoffPanel):
        LatheOp.__init__(self, cutoffPanel)
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

    def runOperation(self):
        self.getParameters()

        self.safeX = self.xStart + self.xRetract
        self.cutoffZ = self.zCutoff - self.toolWidth

        self.passSize[0] = self.cutoffZ
        if cfg.getBoolInfoData(cf.cfgDraw):
            self.m.draw("cutoff", self.xStart, self.zStart)

        self.setup()

        if self.panel.pause.GetValue():
            print("pause")
            self.m.quePause()
        self.m.moveX(self.xEnd, ct.CMD_SYN)
        self.m.moveX(self.safeX)
        self.m.moveZ(self.zStart)

        if STEP_DRV or MOTOR_TEST:
            self.m.stopSpindle()
        self.m.done(1)
        self.m.drawClose()
        stdout.flush()
        return(True)

    def setup(self):
        m = self.m
        m.quePause()
        self.m.done(0)
        if STEP_DRV:
            m.startSpindle(cfg.getIntInfoData(cf.cuRPM))
            m.queFeedType(ct.FEED_PITCH)
            m.xSynSetup(cfg.getFloatInfoData(cf.cuXFeed))
        else:
            m.queXSetup(cfg.getFloatInfoData(cf.cuXFeed))
        m.moveX(self.safeX)
        m.moveZ(self.cutoffZ)
        m.moveX(self.xStart)

class CutoffPanel(wx.Panel, FormRoutines, ActionRoutines):
    def __init__(self, parent, hdrFont, *args, **kwargs):
        super(CutoffPanel, self).__init__(parent, *args, **kwargs)
        self.hdrFont = hdrFont
        FormRoutines.__init__(self)
        self.control = Cutoff(self)
        ActionRoutines.__init__(self, self.control)
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

        txt = wx.StaticText(self, -1, "Cutoff")
        txt.SetFont(self.hdrFont)

        sizerV.Add(txt, flag=wx.CENTER|wx.ALL, border=2)

        sizerG = wx.FlexGridSizer(8, 0, 0)

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
        jogPanel.passText.SetLabel("Len")

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
        self.pause = False

        self.taperX = False
        self.taper = 0.0
        self.backInc = 0.002

        self.cut = 0.0
        self.internal = False
        self.boreRadius = 0.0

        self.startZ = 0.0
        self.startX = 0.0
        self.taperLength = 0.0
        self.endZ = 0.0
        self.endX = 0.0

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

        self.finish = abs(getFloatVal(tp.finish))
        self.pause = self.panel.pause.GetValue()

        totalTaper = taperInch * self.zLength
        print("taperX %s totalTaper %5.3f taperInch %6.4f" % \
              (self.taperX, totalTaper, taperInch))

    def setup(self):
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
            
        if STEP_DRV:
            m.startSpindle(cfg.getIntInfoData(cf.tpRPM))
            m.queFeedType(ct.FEED_PITCH)
            m.zSynSetup(cfg.getFloatInfoData(cf.tpZFeed))
            m.xSynSetup(cfg.getFloatInfoData(cf.tpXInFeed))
        else:
            m.queZSetup(cfg.getFloatInfoData(cf.tpZFeed))
            m.queXSetup(cfg.getFloatInfoData(cf.tpXInFeed))

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
        self.setupAction(self.calcExternalPass, self.externalPass)

        self.panel.passes.SetValue("%d" % (self.passes))
        print("passes %d cutAmount %5.3f feed %6.3f" % \
              (self.passes, self.cutAmount, self.actualFeed))

        if cfg.getBoolInfoData(cf.cfgDraw):
            self.m.draw("taper", self.zStart, self.taper)

        self.setup()

        while self.updatePass():
            pass

        self.m.printXText("%2d %7.4f %7.4f", LEFT, False)
        self.m.printZText("%2d %7.4f", LEFT|MIDDLE)
        self.m.moveZ(self.safeZ)
        if STEP_DRV or MOTOR_TEST:
            self.m.stopSpindle()
        self.m.done(1)
        self.m.drawClose()
        stdout.flush()
        return(True)

    def calcExternalPass(self, final=False):
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
        print("%2d start (%6.3f,%6.3f) end (%6.3f %6.3f) "\
              "%6.3f %6.3f" % \
              (self.passCount, self.startZ, self.startX, \
               self.endZ, self.endX, 2.0 * self.startX, 2.0 * self.endX))
        stdout.flush()

    def externalPass(self):
        m = self.m
        m.moveZ(self.startZ - self.backInc) # move past start
        m.moveZ(self.startZ, ct.CMD_JOG) # move to takeout backlash
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
            m.moveX(self.startX, ct.CMD_SYN)
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
            add = getFloatVal(self.panel.add) / 2
            self.cutAmount += add
            self.setup()
            self.calcExternalPass(True)
            moveCommands.nextPass(self.passCount)
            self.externalPass()
            if self.taperX:
                self.m.moveX(self.safeX)
                self.m.moveZ(self.startZ)
            else:
                pass
            if STEP_DRV or MOTOR_TEST:
                self.m.stopSpindle()
            self.m.done(1)
            comm.command(cm.CMD_RESUME)

    def internalTaper(self, taperInch):
        print("internalTaper")
        self.internal = True
        self.getParameters(taperInch)

        self.boreRadius = self.xStart = self.largeDiameter / 2.0
        self.xEnd = self.smallDiameter / 2.0
        self.cut = self.xEnd - self.boreRadius

        self.calcFeed(self.xFeed, self.cut, self.finish)
        self.setupSpringPasses(self.panel)
        self.setupAction(self.calcInternalPass, self.internalPass)

        self.panel.passes.SetValue("%d" % (self.passes))
        print("passes %d cutAmount %5.3f feed %6.3f" % \
              (self.passes, self.cutAmount, self.actualFeed))

        self.endZ = self.zStart

        self.safeX = self.boreRadius - self.xRetract
        self.safeZ = self.zStart + self.zRetract

        if cfg.getBoolInfoData(cf.cfgDraw):
            self.m.draw("taper", self.zStart, self.taper)

        self.setup()

        while self.updatePass():
            pass

        self.m.printXText("%2d %7.4f %7.4f", LEFT, True)
        self.m.printZText("%2d %7.4f %7.4f %7.4f", RIGHT|MIDDLE)
        self.m.moveX(self.safeX)
        self.m.moveZ(self.safeZ)
        if STEP_DRV or MOTOR_TEST:
            self.m.stopSpindle()
        self.m.done(1)
        self.m.drawClose()
        stdout.flush()
        return(True)

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
        self.passSize[self.passCount] = self.endX * 2.0
        print("%2d feed %6.3f start (%6.3f,%6.3f) end (%6.3f %6.3f) "\
              "%6.3f %6.3f" % \
              (self.passCount, self.feed, self.startX, self.startZ, \
               self.endX, self.endZ, \
               2.0 * self.startX, 2.0 * self.endX))

    def internalPass(self):
        m = self.m
        m.moveZ(self.startZ - self.backInc) # past the start point
        m.moveZ(self.startZ, ct.CMD_JOG) # back to start to remove backlash
        m.moveX(self.startX, ct.CMD_SYN)
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
            add = getFloatVal(self.panel.add) / 2
            self.feed += add
            self.passCount += 1
            self.taper()
            self.m.moveZ(self.safeZ)
            self.calcInternalPass()
            moveCommands.nextPass(self.passCount)
            self.internalPass()
            self.m.moveX(self.safeX)
            self.m.moveZ(self.safeZ)
            if STEP_DRV or MOTOR_TEST:
                self.m.stopSpindle()
            self.m.done(1)
            comm.command(cm.CMD_RESUME)

class TaperPanel(wx.Panel, FormRoutines, ActionRoutines):
    def __init__(self, parent, hdrFont, *args, **kwargs):
        super(TaperPanel, self).__init__(parent, *args, **kwargs)
        self.hdrFont = hdrFont
        FormRoutines.__init__(self)
        self.control = Taper(self)
        ActionRoutines.__init__(self, self.control)
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
                           (cf.tpLargeDiamText, None), \
                           (cf.tpPasses, 'd'), \
                           (cf.tpPause, None), \
                           (cf.tpRPM, 'd'), \
                           (cf.tpSPInt, 'd'), \
                           (cf.tpSmallDiam, 'f'), \
                           (cf.tpSmallDiamText, None), \
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

        txt = wx.StaticText(self, -1, "Taper")
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

        sizerG = wx.FlexGridSizer(8, 0, 0)

        # z parameters

        self.zLength = self.addField(sizerG, "Z Length", cf.tpZLength)

        self.zStart = self.addField(sizerG, "Z Start", cf.tpZStart)

        self.zFeed = self.addField(sizerG, "Z Feed", cf.tpZFeed)

        self.zRetract = self.addField(sizerG, "Z Retract", cf.tpZRetract)

        # x parameters

        self.largeDiam = self.addFieldText(sizerG, "Large Diam", \
                                           cf.tpLargeDiam, cf.tpLargeDiamText)

        self.smallDiam = self.addFieldText(sizerG, "Small Diam", \
                                           cf.tpSmallDiam, cf.tpSmallDiamText)

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
            cfg.infoSetLabel(cf.tpLargeDiamText, "Bore Diam")
            cfg.infoSetLabel(cf.tpSmallDiamText, "Large Diam")
            jogPanel.passText.SetLabel("L Diam")

        else:
            cfg.infoSetLabel(cf.tpLargeDiamText, "Large Diam")
            cfg.infoSetLabel(cf.tpSmallDiamText, "Small Diam")
            jogPanel.passText.SetLabel("S Diam" if taper < 1.0 else \
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
        except CommTimeout:
            commTimeout()

    def sendAction(self):
        self.sendData()
        taper = getFloatVal(self.xDelta) / getFloatVal(self.zDelta)
        rtn = self.control.internalTaper(taper) if self.internal.GetValue() \
              else self.control.externalTaper(taper)
        return(rtn)

    def startAction(self):
        comm.command(cm.CMD_RESUME)
        if cfg.getBoolInfoData(cf.cfgDbgSave):
            updateThread.openDebug()

    def addAction(self):
        self.control.internalAdd() if self.internal.GetValue() else \
            self.control.externalAdd()

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
        self.d = None
        self.internal = False
        self.tpi = 0.0
        self.pitch = 0.0

        self.zBackInc = 0.003
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
        self.zAccel = 0.0
        self.zOffset = 0.0
        self.p0 = 0.0

    def draw(self, diam, tpi):
        tmp = "tfeed%0.3f-%0.1f" % (diam, tpi)
        tmp = tmp.replace(".", "-")
        tmp = re.sub("-0$", "", tmp) + ".dxf"
        d = dxf.drawing(tmp)
        d.add_layer(REF, color=0)
        d.add_layer(TEXT, color=0)
        self.d = d

    def drawLine(self, p0, p1, layer=0):
        if self.d is not None:
            self.d.add(dxf.line(p0, p1, layer=layer))

    def drawClose(self):
        try:
            if self.d is not None:
                self.d.save()
                self.d = None
        except:
            print("dxf file save error")
            traceback.print_exc()

    def getParameters(self):
        th = self.panel
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

    def runOperation(self):
        self.getParameters()

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

        firstFeed = self.panel.firstFeedBtn.GetValue()
        if firstFeed:
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

        if firstFeed:
            lastA = self.area - self.areaPass
            lastD = self.depth - sqrt(lastA / self.tanAngle)
            self.panel.lastFeed.SetValue("%0.4f" % (lastD))
        else:
            firstF = sqrt(self.areaPass / self.tanAngle)
            self.panel.firstFeed.SetValue("%0.4f" % (firstF))

        self.setupSpringPasses(self.panel)
        self.setupAction(self.calculatePass, self.runPass)
        self.initPass()

        if self.internal:
            self.xRetract = -self.xRetract

        self.safeX = self.xStart + self.xRetract
        self.startZ = self.zStart + self.zAccel

        if cfg.getBoolInfoData(cf.cfgDraw):
            self.draw(self.xStart * 2.0, self.tpi)
            self.p0 = (0, 0)

        if cfg.getBoolInfoData(cf.cfgDraw):
            self.m.draw("threada", self.xStart * 2.0, self.tpi)

        self.setup()

        self.curArea = 0.0
        self.prevFeed = 0.0
        print("pass     area   xfeed  zfeed   delta  xsize")

        while self.updatePass():
            pass

        self.m.printXText("%2d Z %6.4f Zofs %6.4f D %6.4f F %6.4f", \
                          LEFT, self.internal)

        self.drawClose()
        self.m.drawClose()
        self.m.stopSpindle()
        self.m.done(1)
        stdout.flush()
        return(True)

    def setup(self, add=False):
        m = self.m
        if not add:
            m.setLoc(self.zEnd, self.xStart)
            m.drawLineZ(self.zStart, REF)
            m.drawLineX(self.xEnd, REF)
            m.setLoc(self.safeZ, self.safeX)
        m.quePause()
        self.m.done(0)
        m.startSpindle(cfg.getIntInfoData(cf.thRPM))
        feedType = ct.FEED_TPI if self.panel.tpi.GetValue() else ct.FEED_METRIC
        m.queFeedType(feedType)
        m.saveTaper(cfg.getFloatInfoData(cf.thXTaper))
        m.saveRunout(cfg.getFloatInfoData(cf.thExitRev))
        m.saveDepth(self.depth)
        m.zSynSetup(cfg.getFloatInfoData(cf.thPitch))
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

    def calculatePass(self, final=False, add=False):
        if not add:
            if final:
                self.curArea = self.area
            else:
                self.curArea += self.areaPass
            feed = sqrt(self.curArea / self.tanAngle)
            self.feed = feed
        else:
            feed = self.feed

        if not self.panel.alternate.GetValue():
            self.zOffset = feed * self.tanAngle
        else:
            offset = (feed - self.prevFeed) * self.tanAngle
            if self.passCount & 1:
                offset = -offset
            self.zOffset += offset

        if self.internal:
            feed = -feed
        self.curX = self.xStart - feed
        self.passSize[self.passCount] = self.curX * 2.0
        print("%4d %8.6f %7.4f %6.4f %7.4f %6.4f" % \
              (self.passCount, self.curArea, feed, self.zOffset, \
               feed - self.prevFeed, self.curX * 2.0))
        stdout.flush()
        self.prevFeed = feed

        if self.d is not None:
            p1 = (self.zOffset, feed)
            pa = (self.zOffset - feed * self.tanAngle, 0)
            pb = (self.zOffset + feed * self.tanAngle, 0)
            self.drawLine(self.p0, p1)
            self.drawLine(p1, pa)
            self.drawLine(p1, pb)
            self.p0 = p1

    def runPass(self):
        m = self.m
        startZ = self.safeZ - self.zOffset
        self.m.moveZ(startZ + self.zBackInc)
        self.m.moveZ(startZ)
        self.m.moveX(self.curX, ct.CMD_JOG)
        if self.panel.pause.GetValue():
            print("pause")
            self.m.quePause()
        if m.passNum & 0x300 == 0:
            m.saveXText((m.passNum, startZ, self.zOffset, \
                        self.curX * 2.0, self.feed), (self.safeZ, self.curX))
        self.m.moveZ(self.zEnd, ct.CMD_SYN | ct.Z_SYN_START)
        self.m.moveX(self.safeX)

    def addPass(self):
        add = getFloatVal(self.panel.add)
        self.feed += add
        self.setup(True)
        self.calculatePass(add=True)
        moveCommands.nextPass(self.passCount)
        self.runPass()
        self.m.stopSpindle()
        self.m.done(1)
        comm.command(cm.CMD_RESUME)
        jogPanel.setStatus(st.STR_NO_ADD)

class ThreadPanel(wx.Panel, FormRoutines, ActionRoutines):
    def __init__(self, parent, hdrFont, *args, **kwargs):
        super(ThreadPanel, self).__init__(parent, *args, **kwargs)
        self.hdrFont = hdrFont
        FormRoutines.__init__(self)
        self.control = ScrewThread(self)
        ActionRoutines.__init__(self, self.control)
        self.InitUI()
        self.configList = None
        self.prefix = 'th'
        self.formatList = ((cf.thAddFeed, 'f'), \
                           (cf.thAlternate, None), \
                           (cf.thAngle, 'fs'), \
                           (cf.thExitRev, 'fs'), \
                           (cf.thFirstFeed, 'f'), \
                           (cf.thFirstFeedBtn, None), \
                           (cf.thHFactor, 'f'), \
                           (cf.thInternal, None), \
                           (cf.thLastFeed, 'f'), \
                           (cf.thLastFeedBtn, None), \
                           (cf.thMM, None), \
                           (cf.thPasses, 'd'), \
                           (cf.thPause, None), \
                           (cf.thPitch, 'fs'), \
                           (cf.thRPM, 'd'), \
                           (cf.thSPInt, 'n'), \
                           (cf.thSpring, 'n'), \
                           (cf.thTPI, None), \
                           (cf.thXDepth, 'f'), \
                           (cf.thXRetract, 'f'), \
                           (cf.thXStart, 'f'), \
                           (cf.thXTaper, 'f'), \
                           (cf.thZEnd, 'f'), \
                           (cf.thZRetract, 'f'), \
                           (cf.thZStart, 'f'))

    def InitUI(self):
        self.sizerV = sizerV = wx.BoxSizer(wx.VERTICAL)

        txt = wx.StaticText(self, -1, "Thread")
        txt.SetFont(self.hdrFont)

        sizerV.Add(txt, flag=wx.CENTER|wx.ALL, border=2)

        sizerG = wx.FlexGridSizer(8, 0, 0)

        # z parameters

        self.zEnd = self.addField(sizerG, "Z End", cf.thZEnd)

        self.zStart = self.addField(sizerG, "Z Start", cf.thZStart)

        self.zRetract = self.addField(sizerG, "Z Retract", cf.thZRetract)

        sizerG.Add(self.emptyCell)
        sizerG.Add(self.emptyCell)

        # x parameters

        self.xStart = self.addField(sizerG, "X Start D", cf.thXStart)

        self.xRetract = self.addField(sizerG, "X Retract", cf.thXRetract)

        self.depth = self.addField(sizerG, "Depth", cf.thXDepth)

        sizerG.Add(self.emptyCell)
        sizerG.Add(self.emptyCell)

        # self.final = btn = wx.RadioButton(self, label="Final", \
        #                                   style = wx.RB_GROUP)
        # sizerH.Add(btn, flag=wx.CENTER|wx.ALL, border=2)
        # cfg.initInfo(thFinal, btn)

        # self.depth = btn = wx.RadioButton(self, label="Depth")
        # sizerH.Add(btn, flag=wx.CENTER|wx.ALL, border=2)
        # cfg.initInfo(thDepth, btn)

        # thread parameters

        self.thread = self.addField(sizerG, "Thread", cf.thPitch)

        self.tpi = self.addRadioButton(sizerG, "TPI", cf.thTPI, \
                                       style=wx.RB_GROUP)

        self.mm = self.addRadioButton(sizerG, "mm", cf.thMM)

        self.angle = self.addField(sizerG, "Angle", cf.thAngle)

        self.alternate = self.addCheckBox(sizerG, "Alternate", cf.thAlternate)

        # special thread parameters

        self.xTaper = self.addField(sizerG, "Taper", cf.thXTaper)

        self.xExitRev = self.addField(sizerG, "Exit Rev", cf.thExitRev)

        self.firstFeedBtn = self.addRadioButton(sizerG, "First Feed", \
                                                cf.thFirstFeedBtn, \
                                                style=wx.RB_GROUP, \
                                                action=self.OnFirstFeed)

        self.firstFeed = self.addField(sizerG, None, cf.thFirstFeed)

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
        self.updateFirstFeed()
        self.updateLastFeed()
        jogPanel.passText.SetLabel("M Diam")

    def updateFirstFeed(self):
        if self.firstFeedBtn.GetValue():
            self.firstFeed.SetEditable(True)
            self.lastFeed.SetEditable(False)

    def updateLastFeed(self):
        if self.lastFeedBtn.GetValue():
            self.lastFeed.SetEditable(True)
            self.firstFeed.SetEditable(False)

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

    def startAction(self):
        comm.command(cm.CMD_RESUME)
        if cfg.getBoolInfoData(cf.cfgDbgSave):
            updateThread.openDebug()

    def addAction(self):
        self.control.addPass()

class ButtonRepeat(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.threadRun = True
        self.event = Event()
        self.action = None
        self.code = None
        self.val = None
        # self.jogCode = None
        # self.repeat = 0
        self.start()

    def run(self):
        while True:
            timeout = .5
            self.event.wait(.2)
            if not self.threadRun:
                break
            while self.event.isSet():
                # if self.action is not None:
                #     self.action(self.code, self.val)
                if self.action == JOG_Z:
                    jogPanel.zJogCmd(self.code, self.val)
                elif self.action == JOG_X:
                    jogPanel.xJogCmd(self.code, self.val)
                elif self.action == JOG_SPINDLE:
                    jogPanel.spindleJogCmd(self.code, self.val)
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
                        traceback.print_exc()
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
        print(data)
        stdout.flush()
        outerRing = data[1]
        if outerRing != jogShuttle.lastOuterRing:
            if jogShuttle.axisAction is not None:
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
            if jogShuttle.lastKnob is not None:
                pass
            jogShuttle.lastKnob = knob
        button = data[4] | data[5]
        if button | jogShuttle.lastButton:
            changed = button ^ jogShuttle.lastButton
            for action in jogShuttle.buttonAction:
                (val, function) = action
                if changed & val:
                    if function is not None:
                        function(button, val)
            jogShuttle.lastButton = button

    def setZ(self, button, val):
        if button & val:
            jogShuttle.axisAction = jogShuttle.jogZ
            maxSpeed = cfg.getFloatInfoData(cf.zMaxSpeed)
            for val in range(len(jogShuttle.factor)):
                jogShuttle.zSpeed[val] = maxSpeed * jogShuttle.factor[val]
            # print("set z")
            # stdout.flush()

    def setX(self, button, val):
        if button & val:
            jogShuttle.axisAction = jogShuttle.jogX
            maxSpeed = cfg.getFloatInfoData(cf.xMaxSpeed)
            for val in range(len(jogShuttle.factor)):
                jogShuttle.xSpeed[val] = maxSpeed * jogShuttle.factor[val]
            # print("set x")
            # stdout.flush()

    def setSpindle(self, button, val):
        if button & val:
            jogShuttle.axisAction = jogShuttle.jogSpindle
            maxSpeed = cfg.getFloatInfoData(cf.spMaxRPM)
            for val in range(len(jogShuttle.factor)):
                jogShuttle.spindleSpeed[val] = \
                    maxSpeed * jogShuttle.factor[val]
            # print("set spindle")
            # stdout.flush()

    def jogZ(self, code, val):
        # print("jog z %d %d" % (val, jogShuttle.zCurIndex))
        # stdout.flush()
        index = abs(val)
        speed = jogShuttle.zSpeed[index]
        if val < 0:
            speed = -speed
        if ((jogShuttle.zCurSpeed >= 0 and speed >= 0) or \
            (jogShuttle.zCurSpeed <= 0 and speed <= 0)):
            jogShuttle.zCurSpeed = speed
            try:
                if index != jogShuttle.zCurIndex:
                    jogShuttle.zCurIndex = index
                    comm.setParm(pm.Z_JOG_SPEED, speed)
                comm.command(cm.ZJSPEED)
            except CommTimeout:
                commTimeout()
            if index == 0:
                buttonRepeat.action = None
                buttonRepeat.event.clear()
                jogShuttle.zCurIndex = -1
                # print("jogZ done")
                # stdout.flush()

    def jogX(self, code, val):
        # print("jog x %d" % (val))
        # stdout.flush()
        index = abs(val)
        speed = jogShuttle.xSpeed[index]
        if val > 0:
            speed = -speed
        if ((jogShuttle.xCurSpeed >= 0 and speed >= 0) or \
            (jogShuttle.xCurSpeed <= 0 and speed <= 0)):
            jogShuttle.xCurSpeed = speed
            try:
                if index != jogShuttle.xCurIndex:
                    jogShuttle.xCurIndex = index
                    comm.setParm(pm.X_JOG_SPEED, speed)
                comm.command(cm.XJSPEED)
            except CommTimeout:
                commTimeout()
            if index == 0:
                buttonRepeat.action = None
                buttonRepeat.event.clear()
                jogShuttle.xCurIndex = -1
                # print("jogX done")
                # stdout.flush()

    def jogSpindle(self, code, val):
        # print("jog spindle %d %d" % (val, jogShuttle.spindleCurIndex))
        # stdout.flush()
        index = abs(val)
        speed = jogShuttle.spindleSpeed[index]
        if val < 0:
            speed = -speed
        if ((jogShuttle.spindleCurSpeed >= 0 and speed >= 0) or \
            (jogShuttle.spindleCurSpeed <= 0 and speed <= 0)):
            jogShuttle.spindleCurSpeed = speed
            try:
                if index != jogShuttle.spindleCurIndex:
                    jogShuttle.spindleCurIndex = index
                    comm.setParm(pm.SP_JOG_RPM, speed)
                comm.command(cm.SPINDLE_JOG_SPEED)
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
        FormRoutines.__init__(self, False)
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
        self.zMenu = None
        self.xMenu = None
        self.mvStatus = 0
        self.lastPass = 0
        self.currentPanel = None
        self.currentControl = None
        self.lastZOffset = 0.0
        self.lastXOffset = 0.0
        self.zPosition = None
        self.zHomeOffset = None
        self.xPosition = None
        self.xHomeOffset = None
        self.probeStatus = 0
        if DRO:
            self.zDROInch = 0
            self.xDROInch = 0
            self.zDROInvert = 1
            self.xDROInvert = 1
            self.zDROPostition = None
            self.zDROOffset = None
            self.xDROPostition = None
            self.xDROOffset = None

    def initUI(self):
        self.Bind(wx.EVT_LEFT_UP, self.OnMouseEvent)

        sizerV = wx.BoxSizer(wx.VERTICAL)

        sizerG = wx.FlexGridSizer(6, 0, 0)

        self.txtFont = txtFont = wx.Font(16, wx.MODERN, wx.NORMAL, \
                                         wx.NORMAL, False, u'Consolas')
        self.posFont = posFont = wx.Font(20, wx.MODERN, wx.NORMAL, \
                                         wx.NORMAL, False, u'Consolas')
        # first row
        # z position

        self.zPos = \
            self.addDialogField(sizerG, "Z", "0.0000", txtFont, \
                                posFont, (120, -1), border=(10, 2), \
                                edit=False, index=cf.jogZPos)
        self.zPos.Bind(wx.EVT_RIGHT_DOWN, self.OnZMenu)

        # x Position

        self.xPos = \
            self.addDialogField(sizerG, "X", "0.0000", txtFont, \
                                posFont, (120, -1), border=(10, 2), \
                                edit=False, index=cf.jogXPos)
        self.xPos.Bind(wx.EVT_RIGHT_DOWN, self.OnXMenu)

        # rpm

        self.rpm = \
            self.addDialogField(sizerG, "RPM", "0", txtFont, \
                                posFont, (80, -1), border=(10, 2), \
                                edit=False)

        # second row

        (self.passSize, self.passText) = \
            self.addDialogField(sizerG, "Size", "0.000", txtFont, \
                                posFont, (120, -1), border=(10,2), \
                                edit=False, text=True)
        # sizerG.Add(self.emptyCell)

        # self.statusText = txt = wx.StaticText(self, -1, "")
        # txt.SetFont(txtFont)
        # sizerG.Add(txt, flag=wx.ALL|wx.ALIGN_LEFT| \
        #            wx.ALIGN_CENTER_VERTICAL, border=10)

        # x diameter

        self.xPosDiam = \
            self.addDialogField(sizerG, "X D", "0.0000", txtFont, \
                                posFont, (120, -1), border=(10, 2), \
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
                                    posFont, (120, -1), border=(10, 2), \
                                    edit=False, index=cf.droZPos)

            # x dro Position

            self.xDROPos = \
                self.addDialogField(sizerG, "X", "0.0000", txtFont, \
                                    posFont, (120, -1), border=(10, 2), \
                                    edit=False, index=cf.droXPos)

        sizerV.Add(sizerG, flag=wx.ALIGN_CENTER_VERTICAL|wx.CENTER|wx.ALL, \
                   border=2)

        # status line

        sizerH = wx.BoxSizer(wx.HORIZONTAL)

        self.statusText = txt = wx.StaticText(self, -1, "", size=(80, -1), \
                                              style=wx.ST_NO_AUTORESIZE)
        txt.SetFont(txtFont)
        sizerH.Add(txt, flag=wx.ALL|wx.ALIGN_LEFT| \
                   wx.ALIGN_CENTER_VERTICAL, border=2)

        self.statusLine = txt = wx.StaticText(self, -1, "")
        txt.SetFont(txtFont)
        sizerH.Add(txt, flag=wx.ALL|wx.ALIGN_LEFT| \
                   wx.ALIGN_CENTER_VERTICAL, border=2)

        sizerV.Add(sizerH)

        # control buttons and jog

        btnSize = wx.DefaultSize

        sizerH = wx.BoxSizer(wx.HORIZONTAL)

        sizerG = wx.FlexGridSizer(3, 0, 0)

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

        if STEP_DRV or MOTOR_TEST:
            self.addButton(sizerG, 'Start Spindle', \
                           self.OnStartSpindle, btnSize)
        else:
            sizerG.Add(self.emptyCell)

        sizerH.Add(sizerG)

        sizerG = wx.FlexGridSizer(5, 0, 0)
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
        comm.queParm(pm.Z_HOME_OFFSET, zHomeOffset)
        comm.queParm(pm.Z_FLAG, ct.CMD_MAX)
        comm.command(cm.ZMOVEABS)
        self.combo.SetFocus()

    def OnZPark(self, e):
        comm.queParm(pm.Z_MOVE_POS, cfg.getFloatInfoData(cf.zParkLoc))
        comm.queParm(pm.Z_HOME_OFFSET, zHomeOffset)
        comm.queParm(pm.Z_FLAG, ct.CMD_MAX)
        comm.command(cm.ZMOVEABS)
        self.combo.SetFocus()

    def OnXSafe(self, e):
        panel = self.getPanel()
        (z, x) = panel.getSafeLoc()
        comm.queParm(pm.X_MOVE_POS, x)
        comm.queParm(pm.X_HOME_OFFSET, xHomeOffset)
        comm.queParm(pm.X_FLAG, ct.CMD_MAX)
        comm.command(cm.XMOVEABS)
        self.combo.SetFocus()

    def OnXPark(self, e):
        comm.queParm(pm.X_MOVE_POS, cfg.getFloatInfoData(cf.xParkLoc))
        comm.queParm(pm.X_HOME_OFFSET, xHomeOffset)
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
            # self.btnRpt.action = self.zJogCmd
            self.btnRpt.action = JOG_Z
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
                    comm.queParm(pm.X_FLAG, ct.CMD_JOG)
                    comm.queParm(pm.X_MOVE_DIST, val)
                    comm.command(cm.XMOVEREL)
                except CommTimeout:
                    commTimeout()

    def xDown(self, code):
        val = self.getInc()
        if val != "Cont":
            self.xJogCmd(code, val)
        else:
            # self.btnRpt.action = self.xJogCmd
            self.btnRpt.action = JOG_X
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
            val = 0.001
        comm.queParm(pm.Z_MPG_INC, val * self.zStepsInch)
        comm.queParm(pm.X_MPG_INC, val * self.xStepsInch)
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

    def OnKeyChar(self, evt):
        code = evt.GetKeyCode()
        if code == ord('c'):
            self.combo.SetSelection(0)
        elif code == ord('i'):
            combo = self.combo
            val = combo.GetSelection()
            if val == 0:
                combo.SetSelection(1)
            else:
                combo.SetSelection(1) if val >= len(self.step) - 1 else \
                    combo.SetSelection(val + 1)
        elif code == ord('I'):
            combo = self.combo
            val = combo.GetSelection()
            if val > 0:
                if val > 1:
                    combo.SetSelection(val - 1)
        elif code == ord('r'):
            panel = mainFrame.getCurrentPanel()
            panel.OnSend(None)
        elif code == ord('s'):
            self.OnResume(None)
        elif code == ord('p'):
            self.OnPause(None)
        elif code == ord('a'):
            panel = mainFrame.getCurrentPanel()
            panel.OnAdd(None)
        elif code == ord('A'):
            panel = mainFrame.getCurrentPanel()
            panel.setAddFocus()
        elif code == wx.WXK_F9:
            self.OnStartSpindle(None)
        elif code == wx.WXK_ESCAPE:
            self.OnStop(None)
        elif code == ord('f'):
            panel = mainFrame.getCurrentPanel()
            panel.setFocus()
        elif code == ord('z'):
            self.OnZMenu(None)
        elif code == ord('x'):
            self.OnXMenu(None)
        elif code == ord('d'):
            self.OnDone(None)
        elif code == ord('C'):
            self.setStatus(st.STR_CLR)
        else:
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
            self.rpm.SetValue(rpm)

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
                zDroLoc = self.zDROInvert * zDroLoc - zDROOffset
                self.zDROPos.SetValue("%0.4f" % (zDroLoc))

                xDROPos = int(xDROPos)
                self.xDROPosition.value = xDROPos
                xDroLoc = float(xDROPos) / self.xDROInch
                if self.lastXOffset != xDROOffset:
                    self.lastXOffset = xDROOffset
                    print("xDROPos %d %0.4f xDROOffset %0.4f" % \
                          (xDROPos, xDroLoc, xDROOffset))
                    stdout.flush()
                xDroLoc = self.xDROInvert * xDroLoc - xDROOffset
                self.xDROPos.SetValue("%0.4f" % (xDroLoc))

            text = ''
            if xHomed:
                text = 'H'
            if self.currentPanel.active:
                text += '*'
            mvStatus = int(mvStatus)
            self.mvStatus = mvStatus
            if mvStatus & ct.MV_MEASURE:
                text += 'M'
            if mvStatus & ct.MV_PAUSE:
                text  += 'P'
            if mvStatus & ct.MV_ACTIVE:
                text += 'A'
            self.statusText.SetLabel(text)

            if self.xHome:
                if self.probeAxis == HOME_X:
                    val = comm.getParm(pm.X_HOME_STATUS)
                    if val is not None:
                        if val & ct.HOME_SUCCESS:
                            self.homeDone("home success")
                            xHomed = True
                            comm.setParm(pm.X_LOC, 0)
                            if DRO:
                                comm.setParm(pm.X_DRO_POS, 0)
                                self.updateXDroPos(xLocation)
                        elif val & ct.HOME_FAIL:
                            self.homeDone("home success")
                elif self.probeAxis == AXIS_Z:
                    val = comm.getParm(pm.Z_HOME_STATUS)
                    if val & ct.PROBE_SUCCESS:
                        zHomeOffset = zLocation - self.probeLoc
                        self.zHomeOffset.value = zHomeOffset
                        cfg.setInfo(cf.zSvHomeOffset, "%0.4f" % (zHomeOffset))
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
                        cfg.setInfo(cf.xSvHomeOffset, "%0.4f" % (xHomeOffset))
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
        self.clrActive()
        self.combo.SetFocus()

    def OnStop(self, e):
        moveCommands.queClear()
        comm.command(cm.CMD_STOP)
        self.clrActive()
        self.combo.SetFocus()

    def OnPause(self, e):
        comm.command(cm.CMD_PAUSE)
        self.combo.SetFocus()

    def OnResume(self, e):
        comm.command(cm.CMD_RESUME)
        self.combo.SetFocus()

    def OnDone(self, e):
        self.clrActive()
        self.setStatus(st.STR_CLR)
        self.combo.SetFocus()

    def OnMeasure(self, e):
        comm.command(cm.CMD_MEASURE)
        self.combo.SetFocus()

    def getPanel(self):
        panel = cfg.getInfoData(cf.mainPanel)
        return(mainFrame.panels[panel])

    def clrActive(self):
        self.currentPanel.active = False

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
        # self.btnRpt.action = self.spindleJogCmd
        self.btnRpt.action = JOG_SPINDLE
        self.btnRpt.code = wx.WXK_NUMPAD_PAGEDOWN
        self.btnRpt.val = 0
        self.btnRpt.event.set()

    def OnJogSpindleRev(self, e):
        print("jog spingle")
        stdout.flush()
        # self.btnRpt.action = self.spindleJogCmd
        self.btnRpt.action = JOG_SPINDLE
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
            comm.setParm(pm.Z_HOME_OFFSET, zHomeOffset)
            print("pos %0.4f zLocation %0.4f zHomeOffset %0.4f" % \
                  (val, zLocation, zHomeOffset))
            stdout.flush()
        if DRO:
            self.updateZDroPos(val)

    def updateZDroPos(self, val, zDROPos=None):
        global zDROOffset
        if zDROPos is None:
            zDROPos = comm.getParm(pm.Z_DRO_POS, True)
        if zDROPos is not None:
            droPos = float(zDROPos) / self.zDROInch
            print("pos %0.4f zDROPos %d %0.4f invert %d" % \
                  (val, zDROPos, droPos, self.zDROInvert))
            zDROOffset = self.zDROInvert * droPos - val
            self.zDROOffset.value = zDROOffset
            comm.setParm(pm.Z_DRO_OFFSET, zDROOffset)
            print("zDROOffset %d %0.4f" % \
                  (int(zDROOffset * self.zDROInch), zDROOffset))
            stdout.flush()

    def updateXPos(self, val):
        global xHomeOffset
        val /= 2.0
        sendXData()
        xLocation = comm.getParm(pm.X_LOC)
        if xLocation is not None:
            xLocation = float(xLocation) / self.xStepsInch
            xHomeOffset = xLocation - val
            self.xHomeOffset.value = xHomeOffset
            comm.setParm(pm.X_HOME_OFFSET, xHomeOffset)
            print("pos %0.4f xLocation %0.4f xHomeOffset %0.4f" % \
                  (val, xLocation, xHomeOffset))
            stdout.flush()
        if DRO:
            self.updateXDroPos(val)

    def updateXDroPos(self, val, xDROPos=None):
        global xDROOffset
        if xDROPos is None:
            xDROPos = comm.getParm(pm.X_DRO_POS)
        if xDROPos is not None:
            droPos = float(xDROPos) / self.xDROInch
            print("pos %0.4f xDROPos %d %0.4f invert %d" % \
                  (val, xDROPos, droPos, self.xDROInvert))
            xDROOffset = self.xDROInvert * droPos - val
            self.xDROOffset.value = xDROOffset
            comm.setParm(pm.X_DRO_OFFSET, xDROOffset)
            print("xDROOffset %d %0.4f" % \
                  (int(xDROOffset * self.xDROInch), xDROOffset))
            stdout.flush()

    def getPos(self, ctl):
        (xPos, yPos) = mainFrame.GetPosition()
        (x, y) = self.GetPosition()
        xPos += x
        yPos += y
        (x, y) = ctl.GetPosition()
        xPos += x
        yPos += y
        return(xPos, yPos)

class PosMenu(wx.Menu):
    def __init__(self, jogPnl, axis):
        wx.Menu.__init__(self)
        self.jogPanel = jogPnl
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
        ctl = self.jogPanel.zPos if self.axis == AXIS_Z else \
              self.jogPanel.xPos
        return(self.jogPanel.getPos(ctl))

    def OnSet(self, e):
        dialog = SetPosDialog(self.jogPanel, self.axis)
        dialog.SetPosition(self.getPosCtl())
        dialog.Raise()
        dialog.Show(True)

    def OnZero(self, e):
        self.jogPanel.updateZPos(0) if self.axis == AXIS_Z else \
            self.jogPanel.updateXPos(0)
        self.jogPanel.focus()

    def OnProbe(self, e):
        dialog = ProbeDialog(self.jogPanel, self.axis)
        dialog.SetPosition(self.getPosCtl())
        dialog.Raise()
        dialog.Show(True)

    def OnHomeX(self, e):
        comm.queParm(pm.X_HOME_DIST, cfg.getInfoData(cf.xHomeDist))
        comm.queParm(pm.X_HOME_BACKOFF_DIST, \
                     cfg.getInfoData(cf.xHomeBackoffDist))
        comm.queParm(pm.X_HOME_SPEED, cfg.getInfoData(cf.xHomeSpeed))
        comm.queParm(pm.X_HOME_DIR, 1 if cfg.getBoolInfoData(cf.xHomeDir) \
                     else -1)
        comm.command(cm.XHOMEAXIS)
        self.jogPanel.probe(HOME_X)
        self.jogPanel.focus()

    def OnGoto(self, e):
        dialog = GotoDialog(self.jogPanel, self.axis)
        dialog.SetPosition(self.getPosCtl())
        dialog.Raise()
        dialog.Show(True)

    def OnFixX(self, e):
        jogPnl = self.jogPanel
        dialog = jogPnl.fixXPosDialog
        if dialog is None:
            jogPnl.fixXPosDialog = dialog = FixXPosDialog(self.jogPanel)
        dialog.SetPosition(self.getPosCtl())
        dialog.Raise()
        dialog.Show(True)

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

        sizerG = wx.FlexGridSizer(2, 0, 0)

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
                m.saveXOffset()
                m.moveX(loc / 2.0)
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

        sizerG = wx.FlexGridSizer(2, 0, 0)

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
            try:
                xDiameter = float(comm.getParm(pm.X_DIAMETER)) / \
                            jogPanel.xStepsInch
            except (ValueError, TypeError):
                xDiameter = 0.0
            self.curXPos.SetValue("%0.4f" % (xDiameter))
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

        cfg.setInfo(cf.xSvHomeOffset, "%0.4f" % (xHomeOffset))
        print("curX %0.4f actualX %0.4f offset %0.4f xHomeOffset %0.4f" % \
              (curX, actualX, offset, xHomeOffset))
        stdout.flush()

        self.Show(False)
        jogPanel.focus()

EVT_UPDATE_ID = wx.NewId()

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
        self.dbg = None
        self.start()

    def openDebug(self, file="dbg.txt"):
        self.dbg = open(file, "wb")

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
        dbgSetup = (\
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
                    (en.D_XEXP, self.dbgXExp), \
                    (en.D_XWT, self.dbgXWait), \
                    (en.D_XDN, self.dbgXDone), \

                    (en.D_ZMOV, self.dbgZMov), \
                    (en.D_ZLOC, self.dbgZLoc), \
                    (en.D_ZDST, self.dbgZDst), \
                    (en.D_ZSTP, self.dbgZStp),
                    (en.D_ZST, self.dbgZState), \
                    (en.D_ZBSTP, self.dbgZBSteps), \
                    (en.D_ZDRO, self.dbgZDro), \
                    (en.D_ZEXP, self.dbgZExp), \
                    (en.D_ZWT, self.dbgZWait), \
                    (en.D_ZDN, self.dbgZDone), \

                    (en.D_HST, self.dbgHome), \

                    (en.D_MSTA, self.dbgMoveState), \
                    (en.D_MCMD, self.dbgMoveCmd), \
        )
        dbgTbl = [None for i in range(len(dbgSetup))]
        for (index, action) in dbgSetup:
            dbgTbl[index] = action
        for i, (val) in enumerate(dbgTbl):
            if val is None:
                print("dbgTbl action for %s missing" % (en.dMessageList[i]))
                stdout.flush()
        i = 0
        op = None
        scanMax = len(self.parmList)
        baseTime = None
        while True:
            stdout.flush()
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

            try:
                result = comm.getString(cm.READDBG, 10)
                if not self.threadRun:
                    break
                if result is None:
                    continue
                if not REM_DBG:
                    continue
                tmp = result.split()
                rLen = len(tmp)
                # if rLen > 0:
                #     print("%2d (%s)" % (rLen, result))
                index = 2
                t = (("%8.3f " % (time() - baseTime))
                     if baseTime is not None else "   0.000 ")
                while index <= rLen:
                    (cmd, val) = tmp[index-2:index]
                    index += 2
                    try:
                        cmd = int(cmd, 16)
                        val = int(val, 16)
                        try:
                            action = dbgTbl[cmd]
                            output = action(val)
                            if self.dbg is None:
                                print(t + output)
                                stdout.flush()
                            else:
                                self.dbg.write(t + output + "\n")
                                self.dbg.flush()
                            if cmd == en.D_DONE:
                                if val == 0:
                                    baseTime = time()
                                if val == 1:
                                    baseTime = None
                                    if self.dbg is not None:
                                        self.dbg.close()
                                    self.dbg = None
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
        if self.xDro is not None:
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
        tmp = en.xStatesList[val]
        return("x_st %s" % (tmp + ("\n" if val == en.XIDLE else "")))

    def dbgXBSteps(self, val):
        tmp = float(val) / jogPanel.xStepsInch
        return("xbst %7.4f %6d" % (tmp, val))

    def dbgXDro(self, val):
        tmp = (jogPanel.xDROInvert * float(val)) / jogPanel.xDROInch - \
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
        if self.zDro is not None:
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
        tmp = en.zStatesList[val]
        return("z_st %s" % (tmp + ("\n" if val == en.ZIDLE else "")))

    def dbgZBSteps(self, val):
        tmp = float(val) / jogPanel.zStepsInch
        return("zbst %7.4f %6d" % (tmp, val))

    def dbgZDro(self, val):
        tmp = (jogPanel.zDROInvert * float(val)) / jogPanel.zDROInch - \
              zDROOffset
        self.zDro = tmp
        return("zdro %7.4f" % (tmp))

    def dbgZExp(self, val):
        tmp = float(val) / jogPanel.zStepsInch - zHomeOffset
        return("zexp %7.4f" % (tmp))

    def dbgZWait(self, val):
        return("zwt  %2x" % (val))

    def dbgZDone(self, val):
        return("zdn  %2x" % (val))

    def dbgHome(self, val):
        return("hsta %s" % (en.hStatesList[val]))

    def dbgMoveState(self, val):
        return("msta %s" % (en.mStatesList[val]))

    def dbgMoveCmd(self, val):
        return("mcmd %s" % (en.mCommandsList[val]))

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

class MainFrame(wx.Frame):
    def __init__(self, parent, title):
        global moveCommands, jogShuttle
        wx.Frame.__init__(self, parent, -1, title)
        self.Bind(wx.EVT_CLOSE, self.onClose)
        self.Connect(-1, -1, EVT_UPDATE_ID, self.OnUpdate)

        self.hdrFont = wx.Font(20, wx.MODERN, wx.NORMAL, \
                               wx.NORMAL, False, u'Consolas')
        self.defaultFont = defaultFont = \
            wx.Font(10, wx.MODERN, wx.NORMAL,
                    wx.NORMAL, False, u'Consolas')
        self.SetFont(defaultFont)

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

        self.dirName = os.getcwd()

        self.initUI()

        self.jogShuttle = jogShuttle = JogShuttle()
        comm.openSerial(cfg.getInfoData(cf.commPort), \
                        cfg.getInfoData(cf.commRate))
        if XILINX:
            comm.xRegs = xr.xRegTable

        self.initDevice()

        eventTable = (\
                      (en.EV_ZLOC, self.jogPanel.updateZ), \
                      (en.EV_XLOC, self.jogPanel.updateX), \
                      (en.EV_RPM, self.jogPanel.updateRPM), \
                      (en.EV_READ_ALL, self.jogPanel.updateAll), \
                      (en.EV_ERROR, self.jogPanel.updateError), \
                      )

        self.procUpdate = [None for i in range(en.EV_MAX)]
        for (event, action) in eventTable:
            self.procUpdate[event] = action

        global updateThread
        self.update = updateThread = UpdateThread(self)

    def onClose(self, e):
        global done
        posList = (cf.zSvPosition, cf.zSvHomeOffset, \
                   cf.xSvPosition, cf.xSvHomeOffset)
        if DRO:
            posList += (cf.zSvDROPosition, cf.zSvDROOffset, \
                        cf.xSvDROPosition, cf.xSvDROOffset)
        cfg.saveList(posFile, posList)
        done = True
        self.update.threadRun = False
        buttonRepeat.threadRun = False
        self.Destroy()

    def OnUpdate(self, e):
        index = e.data[0]
        if index < len(self.procUpdate):
            update = self.procUpdate[index]
            if update is not None:
                val = e.data[1:]
                if len(val) == 1:
                    val = val[0]
                update(val)

    def initUI(self):
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

        if STEP_DRV:
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

        if STEP_DRV:
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

        cfg.readInfo(configFile, cf.config)
        cfg.readInfo(posFile, cf.config)

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
        self.SetPosition(((3 * dw) / 4 - w, 0))

        self.showPanel()

        self.turnPanel.update()
        self.facePanel.update()
        self.cutoffPanel.update()
        self.taperPanel.update()
        if STEP_DRV:
            self.threadPanel.update()

        self.taperPanel.updateUI()
        self.Fit()

    def initDevice(self):
        sendClear()
        stdout.flush()

        if comm.ser is not None:
            try:
                comm.queParm(pm.CFG_XILINX, cfg.getBoolInfoData(cf.cfgXilinx))
                comm.queParm(pm.CFG_FCY, cfg.getInfoData(cf.cfgFcy))
                comm.queParm(pm.CFG_MPG, cfg.getBoolInfoData(cf.cfgMPG))
                comm.queParm(pm.CFG_DRO, cfg.getBoolInfoData(cf.cfgDRO))
                comm.queParm(pm.CFG_LCD, cfg.getBoolInfoData(cf.cfgLCD))
                comm.command(cm.CMD_SETUP)

                global zHomeOffset
                sendZData()
                zPosition = cfg.getIntInfo(cf.zSvPosition)
                comm.queParm(pm.Z_LOC, zPosition)
                zHomeOffset = cfg.getFloatInfo(cf.zSvHomeOffset)
                comm.queParm(pm.Z_HOME_OFFSET, zHomeOffset)
                print("zLoc %d %x %7.4f zHomeOffset %7.4f" % \
                      (zPosition, zPosition, \
                       float(zPosition) / jogPanel.zStepsInch, zHomeOffset))
                stdout.flush()
                if DRO:
                    global zDROOffset
                    zPosition = cfg.getIntInfo(cf.zSvDROPosition)
                    comm.queParm(pm.Z_DRO_POS, zPosition)
                    zDROOffset = cfg.getFloatInfo(cf.zSvDROOffset)
                    comm.queParm(pm.Z_DRO_OFFSET, zDROOffset)
                    print("zDROPosition %d %x %7.4f zDROOffset %7.4f" % \
                          (zPosition, zPosition, \
                           float(zPosition) / jogPanel.zDROInch, zDROOffset))
                    stdout.flush()
                comm.sendMulti()

                global xHomeOffset
                sendXData()
                xPosition = cfg.getIntInfo(cf.xSvPosition)
                comm.queParm(pm.X_LOC, xPosition)
                xHomeOffset = cfg.getFloatInfo(cf.xSvHomeOffset)
                comm.queParm(pm.X_HOME_OFFSET, xHomeOffset)
                print("xLoc %d %x %7.4f xHomeOffset %7.4f" % \
                      (xPosition, xPosition, \
                       float(xPosition) / jogPanel.xStepsInch, xHomeOffset))
                stdout.flush()
                if DRO:
                    global xDROOffset
                    xPosition = cfg.getIntInfo(cf.xSvDROPosition)
                    comm.queParm(pm.X_DRO_POS, xPosition)
                    xDROOffset = cfg.getFloatInfo(cf.xSvDROOffset)
                    comm.queParm(pm.X_DRO_OFFSET, xDROOffset)
                    print("xDROPosition %d %x %7.4f xDROOffset %7.4f" % \
                          (xPosition, xPosition, \
                           float(xPosition) / jogPanel.xDROInch, xDROOffset))
                    stdout.flush()

                if HOME_TEST:
                    val = str(int(cfg.getFloatInfoData(cf.xHomeLoc) * \
                                  jogPanel.xStepsInch))
                    comm.queParm(pm.X_HOME_LOC, val)
                    comm.queParm(pm.X_HOME_STATUS, \
                                 ct.HOME_SUCCESS if xHomed else ct.HOME_ACTIVE)
                comm.sendMulti()

                sendSpindleData()

            except CommTimeout:
                commTimeout()
        else:
            sendZData()
            sendXData()

    def OnSave(self, e):
        cfg.saveInfo(configFile)

    def OnRestat(self, e):
        cfg.saveInfo(configFile)
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
        self.showDialog(self.zDialog)

    def OnXSetup(self, e):
        self.showDialog(self.xDialog)

    def OnSpindleSetup(self, e):
        self.showDialog(self.spindleDialog)

    def OnPortSetup(self, e):
        self.showDialog(self.portDialog)

    def OnConfigSetup(self, e):
        self.showDialog(self.configDialog)

    def getCurrentPanel(self):
        return(self.currentPanel)
    
    def showPanel(self):
        key = cf.mainPanel
        if cfg.info[key] is None:
            cfg.initInfo(key, InfoValue('turnPanel'))
        showPanel = cfg.getInfoData(key)

        for key in self.panels:
            panel = self.panels[key]
            if key == showPanel:
                panel.Show()
                self.currentPanel = panel
            else:
                panel.Hide()
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

        sizerG = wx.FlexGridSizer(2, 0, 0)

        self.fields = (
            ("Pitch", cf.zPitch, 'f'), \
            ("Motor Steps", cf.zMotorSteps, 'd'), \
            ("Micro Steps", cf.zMicroSteps, 'd'), \
            ("Motor Ratio", cf.zMotorRatio, 'fs'), \
            ("Backlash", cf.zBacklash, 'f'), \
            ("Accel Unit/Sec2", cf.zAccel, 'fs'), \
            ("Min Speed U/Min", cf.zMinSpeed, 'fs'), \
            ("Max Speed U/Min", cf.zMaxSpeed, 'fs'), \
            ("Jog Min U/Min", cf.zJogMin, 'fs'), \
            ("Jog Max U/Min", cf.zJogMax, 'fs'), \
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

        sizerG = wx.FlexGridSizer(2, 0, 0)

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
            ("Park Loc", cf.xParkLoc, 'f'), \
            ("bInvert Dir", cf.xInvDir, None), \
            ("bInvert MPG", cf.xInvMpg, None), \
            ("Probe Dist", cf.xProbeDist, 'f'), \
            ("Home Dist", cf.xHomeDist, 'f'), \
            ("Home/Probe Speed", cf.xHomeSpeed, 'fs'), \
            ("Backoff Dist", cf.xHomeBackoffDist, 'f'), \
            ("bHome Dir", cf.xHomeDir, None), \
            ("DRO Inch", cf.xDROInch, 'd'), \
            ("bInv DRO", cf.xInvDRO, None), \
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

        self.addDialogButton(sizerH, wx.ID_OK)

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
        sizerG = wx.FlexGridSizer(2, 0, 0)

        self.fields = (
            ("bStepper Drive", cf.spStepDrive, None), \
            ("bMotor Test", cf.spMotorTest, None), \
        )
        if STEP_DRV or MOTOR_TEST:
            self.fields += (
                ("Motor Steps", cf.spMotorSteps, 'd'), \
                ("Micro Steps", cf.spMicroSteps, 'd'), \
                ("Min RPM", cf.spMinRPM, 'd'), \
                ("Max RPM", cf.spMaxRPM, 'd'), \
                ("Accel RPM/Sec2", cf.spAccel, 'fs'), \
                ("Jog Min", cf.spJogMin, 'd'), \
                ("Jog Max", cf.spJogMax, 'd'), \
                # ("Jog Accel Time", cf.spJogAccelTime, 'f'), \
                ("bInvert Dir", cf.spInvDir, None), \
                ("bTest Index", cf.spTestIndex, None), \
            )
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

        self.addDialogButton(sizerH, wx.ID_OK)

        self.addDialogButton(sizerH, wx.ID_CANCEL, self.OnCancel)

        sizerV.Add(sizerH, 0, wx.ALIGN_RIGHT)

        self.SetSizer(sizerV)
        self.sizerV.Fit(self)

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
        sizerG = wx.FlexGridSizer(2, 0, 0)

        self.fields = (
            ("Comm Port", cf.commPort, None), \
            ("Baud Rate", cf.commRate, 'd'), \
        )
        self.fieldList(sizerG, self.fields)

        sizerV.Add(sizerG, flag=wx.LEFT|wx.ALL, border=2)
        sizerH = wx.BoxSizer(wx.HORIZONTAL)
        sizerH.Add((0, 0), 0, wx.EXPAND)

        self.addDialogButton(sizerH, wx.ID_OK)

        self.addDialogButton(sizerH, wx.ID_CANCEL, self.OnCancel)

        sizerV.Add(sizerH, 0, wx.ALIGN_RIGHT)

        self.SetSizer(sizerV)
        self.sizerV.Fit(self)
        self.Show(False)

class ConfigDialog(wx.Dialog, FormRoutines, DialogActions):
    def __init__(self, frame, defaultFont):
        pos = (10, 10)
        wx.Dialog.__init__(self, frame, -1, "Config Setup", pos, \
                           wx.DefaultSize, wx.DEFAULT_DIALOG_STYLE)
        self.SetFont(defaultFont)
        FormRoutines.__init__(self, False)
        DialogActions.__init__(self)
        self.sizerV = sizerV = wx.BoxSizer(wx.VERTICAL)
        sizerG = wx.FlexGridSizer(2, 0, 0)

        self.fields = (
            ("bHW Control", cf.cfgXilinx, None), \
            ("bMPG", cf.cfgMPG, None), \
            ("bDRO", cf.cfgDRO, None), \
            ("bLCD", cf.cfgLCD, None), \
            ("bProbe Inv", cf.cfgPrbInv, None), \
            ("wfcy", cf.cfgFcy, 'd'), \
            ("bDisable Commands", cf.cfgCmdDis, None), \
            ("bDraw Moves", cf.cfgDraw, None), \
            ("bSave Debug", cf.cfgDbgSave, None), \
            ("bRemote Debug", cf.cfgRemDbg, None), \
        )
        if XILINX:
            self.fields += (
                ("Encoder", cf.cfgEncoder, 'd'), \
                ("Xilinx Freq", cf.cfgXFreq, 'd'), \
                ("Freq Mult", cf.cfgFreqMult, 'd'), \
                ("bTest Mode", cf.cfgTestMode, None), \
                ("Test RPM", cf.cfgTestRPM, 'd'), \
                ("bInvert Enc Dir", cf.cfgInvEncDir, None), \
            )
        self.fieldList(sizerG, self.fields)

        sizerV.Add(sizerG, flag=wx.CENTER|wx.ALL, border=2)

        sizerH = wx.BoxSizer(wx.HORIZONTAL)
        sizerH.Add((0, 0), 0, wx.EXPAND)

        self.addDialogButton(sizerH, wx.ID_OK)

        self.addDialogButton(sizerH, wx.ID_CANCEL, self.OnCancel)

        sizerV.Add(sizerH, 0, wx.ALIGN_RIGHT)

        self.SetSizer(sizerV)
        self.sizerV.Fit(self)
        self.Show(False)

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

        f = open('spindle.txt', 'w')

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

        accelMinSteps = int((sStepsSecMin * accelMinTime) / 2.0 + 0.5)
        accelMaxSteps = int((sStepsSecMax * accelMaxTime) / 2.0 + 0.5)
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
        f = open('zsync.txt', 'w')

        zAxis = True
        panel = cfg.getInfoData(cf.mainPanel)
        if panel == 'threadPanel':
            arg1 = cfg.getFloatInfoData(cf.thPitch)
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
            pitch = cfg.getFloatInfoData(cf.zPitch)
            microSteps = cfg.getFloatInfoData(cf.zMicroSteps)
            motorSteps = cfg.getFloatInfoData(cf.zMotorSteps)
            motorRatio = cfg.getFloatInfoData(cf.zMotorRatio)
        else:
            pitch = cfg.getFloatInfoData(cf.xPitch)
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
            revCycle = int(1.0 / pitch + 0.5)
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

        zClocksStep = int(clocksCycle / zStepsCycle + 0.5)
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
        f = open('taper.txt', 'w')

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

        pitch = cfg.getFloatInfoData(cf.zPitch)
        microSteps = cfg.getFloatInfoData(cf.zMicroSteps)
        motorSteps = cfg.getFloatInfoData(cf.zMotorSteps)
        motorRatio = cfg.getFloatInfoData(cf.zMotorRatio)

        zStepsInch = ((microSteps * motorSteps * motorRatio) / pitch)
        dbgPrt(txt, "zStepsInch %d", (zStepsInch))

        pitch = cfg.getFloatInfoData(cf.xPitch)
        microSteps = cfg.getFloatInfoData(cf.xMicroSteps)
        motorSteps = cfg.getFloatInfoData(cf.xMotorSteps)
        motorRatio = cfg.getFloatInfoData(cf.xMotorRatio)
        xStepsInch = ((microSteps * motorSteps * motorRatio) / pitch)
        dbgPrt(txt, "xStepsInch %d", (xStepsInch))

        pitch = cfg.getFloatInfoData(cf.tpZFeed)
        revCycle = int(1.0 / pitch + 0.5)
        if revCycle > 20:
            revCycle = 20
        cycleDist = revCycle * pitch
        dbgPrt(txt, "pitch %5.3f revCycle %d cycleDist %5.3f", \
               (pitch, revCycle, cycleDist))
        clocksCycle = spindleClocksRev * revCycle
        spindleStepsCycle = spindleStepsRev * revCycle
        zStepsCycle = zStepsInch * revCycle * pitch

        zClocksStep = int(clocksCycle / zStepsCycle + 0.5)
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

        f = open('move.txt', 'w')

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

            zMAccelMinSteps = int((zMinStepsSec * zMAccelMinTime) / 2.0 + 0.5)
            zMAccelMaxSteps = int((zMaxStepsSec * zMAccelMaxTime) / 2.0 + 0.5)
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

n = 1
while True:
    if n >= len(sys.argv):
        break
    tmpArg = sys.argv[n]
    # if len(tmpArg) != 0 and tmpArg[0].isdigit():
    #     break
    tmpArg = tmpArg.lower()
    if tmpArg == 'xhomed':
        xHomed = True
    else:
        print("invalid argument: %s" % (tmpArg))
        stdout.flush()
        break
    n += 1

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

app = MainApp(redirect=False)
# app.SetCallFilterEvent(True)
# wx.lib.inspection.InspectionTool().Show()
app.MainLoop()

if comm.ser is not None:
    comm.ser.close()
