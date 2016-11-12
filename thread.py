#!/cygdrive/c/Python27/Python.exe
#!/usr/bin/python
################################################################################

import wx
import wx.lib.colourdb
import sys
from sys import stdout, argv
from math import cos, radians, sqrt

#from draw import

from dxfwrite import DXFEngine as dxf
#from svgwrite import Drawing
#from svgwrite.path import Path

AL_LEFT   = 0x001
AL_RIGHT  = 0x002
AL_CENTER = 0x004
ABOVE     = 0x008
BELOW     = 0x010
MIDDLE    = 0x020
LEFT      = 0x040
RIGHT     = 0x080
CENTER    = 0x100

REF   = 'REF'
TEXT  = 'TEXT'
MAJOR = 'MAJOR'
PITCH = 'PITCH'
MINOR = 'MINOR'
TIP   = 'TIP'
WIRE  = 'WIRE'

threadWires = (0.018, 0.024, 0.029, 0.032, 0.040, 0.045, 0.055, 0.063,
               0.072, 0.081, 0.092, 0.108, 0.120, 0.127, 0.143, 0.285) 

class ThreadCalc():
    def __init__(self, frame=None):
        self.frame = frame
        self.zoom = False
        self.offset = None

    def calc(self, diam, tpi, series='un'):
        print "diam %0.3f tpi %0.1f series %s" % (diam, tpi, series)
        self.diam = diam
        self.tpi = tpi
        self.pitch = 1.0 / tpi
        cos30 = cos(radians(30))
        self.height = self.pitch * cos30
        print "pitch %0.4f height %0.4f" % (self.pitch, self.height)

        oneThird = 1.0 / 3.0
        pitchSqrd = self.pitch * self.pitch
        self.tolMajDiam = 0.06 * pitchSqrd ** oneThird
        print "tolMajDiam %0.6f" % (self.tolMajDiam)

        # TD2 external pitch diameter tolerance
        if series == "unef" or (series == "un") and (tpi >= 10.0):
            lenEngagement = 9.0 * self.pitch
        else:
            lenEngagement = diam
        self.extPitchDiamTol = (0.0015 * (diam ** oneThird) +
                           0.0015 * sqrt(lenEngagement) +
                           0.015 * pitchSqrd ** oneThird)
        print ("extPitchDiamTol %0.6f lenEngagement %0.6f" %
               (self.extPitchDiamTol, lenEngagement))
        # es allowance
        self.allowance = 0.3 * self.extPitchDiamTol
        print "allowance %0.6f" % (self.allowance)

        # Has external thread addendum
        self.extDblAddendum = 2.0 * 3.0 / 8.0 * self.height # has
        print "extDblAddendum %0.6f" % (self.extDblAddendum)

        # hs un double height of external un thread
        self.extDblHUN = 2.0 * 5.0 / 8.0 * self.height
        print "extDblHUN %0.6f" % (self.extDblHUN)

        # hs unr double height of external unr thread
        self.extDblHUNR = 2.0 * 11.0 / 16.0 * self.height
        print "extDblHUNR %0.6f" % (self.extDblHUNR)
    
        # external major diameter
        self.extMaxMajDiam = diam - self.allowance
        self.extMinMajDiam = self.extMaxMajDiam - self.tolMajDiam
        print ("extMaxMajDiam %0.4f extMinMajDiam %0.4f" % 
               (self.extMaxMajDiam, self.extMinMajDiam))

        # external pitch diameter
        self.extMaxPitchDiam = self.extMaxMajDiam - self.extDblAddendum
        self.extPitchDiam = self.diam - 2.0 * 3.0 / 8.0 * self.height
        self.extMinPitchDiam = self.extMaxPitchDiam - self.extPitchDiamTol
        print "extPitchDiam %0.4f" % (self.extPitchDiam)
        print ("extMaxPitchDiam %0.4f extMinPitchDiam %0.4f" % 
               (self.extMaxPitchDiam, self.extMinPitchDiam))

        # external minor diameter
        self.extMaxUNMinorDiam = self.extMaxMajDiam - self.extDblHUN
        self.extMaxUNRMinorDiam = self.extMaxMajDiam - self.extDblHUNR
        self.extMaxMinorDiam = self.extMaxUNMinorDiam
        self.extMinMinorDiam = diam - 2.0 * 7.0 / 8.0 * self.height
        print ("extMaxMinorDiam %0.4f extMinMinorDiam %0.4f" % 
               (self.extMaxMinorDiam, self.extMinMinorDiam))

        a = (self.extMaxMajDiam - self.extMaxPitchDiam) / 2
        b = (self.extMaxPitchDiam - self.extMinMinorDiam) / 2
        print "a %0.4f b %0.4f" % (a, b)

        # TD1 internal minor diameter tolerance
        self.intMinorDiamTol = 0.25 * self.pitch - 0.4 * pitchSqrd
        print "intMinorDiamTol %0.6f" % (self.intMinorDiamTol)

        # TD2 internal pitch diameter tolerance
        self.intPitchDiamTol = 1.3 * self.extPitchDiamTol
        print "intPitchDiamTol %0.6f" % (self.intPitchDiamTol)

        # hn double heigth of internal thread
        self.intDblHeight = 2.0 * 5.0 / 8.0 * self.height
        print "intDblHeight %0.6f" % (self.intDblHeight)

        # hb double external thread addendum
        self.intDblAddendum = 3.0 / 4.0 * self.height
        print "intDblAddendum %0.6f" % (self.intDblAddendum)

        # internal major diameter
        self.intMinMajDiam = diam
        print "intMinMajDiam %0.4f" % (self.intMinMajDiam)

        # internal pitch diameter
        self.intMinPitchDiam = diam - self.intDblAddendum
        self.intMaxPitchDiam = self.intMinPitchDiam + self.intPitchDiamTol
        print ("intMaxPitchDiam %0.4f intMinPitchDiam %0.4f" % 
               (self.intMaxPitchDiam, self.intMinPitchDiam))

        # internal minor diameter
        self.intMinMinorDiam = diam - self.intDblHeight
        self.intMaxMinorDiam = self.intMinMinorDiam + self.intMinorDiamTol
        print ("intMaxMinorDiam %0.4f intMinMinorDiam %0.4f" % 
               (self.intMaxMinorDiam, self.intMinMinorDiam))

        bestWire = 0.5 * self.pitch / cos30
        min = 1.0
        for size in threadWires:
            if size > bestWire:
                actualWire = size
                break
        self.actualWire = actualWire
        print "bestWire %0.4f actialWire %0.3f" % (bestWire, actualWire)
        c = 3 * actualWire - self.height
        self.wireMeasurement = self.extPitchDiam + c
        self.minWire = self.extMinPitchDiam + c
        self.maxWire = self.extMaxPitchDiam + c
        print "wireMeasurement %0.4f" % (self.wireMeasurement)
        print "minWire %0.4f maxWire %0.4f" % (self.minWire, self.maxWire)

    def calcScale(self):
        self.size = size = self.frame.GetSize()
        print "w %d h %d" % (size.width, size.height)
        stdout.flush()
        actualWidth = 5 * self.pitch
        self.xOffset = 0
        self.yOffset = self.extPitchDiam / 2
        self.yBase = size.height / 2
        if self.zoom:
            self.scale = (size.width / actualWidth) * 2
            if self.offset:
                self.xBase = 0
            else:
                self.xBase = size.width - 20
        else:
            self.scale = size.width / actualWidth
            self.xBase = size.width / 2

    def setZoomOffset(self, zoom, offset):
        size = self.size
        self.zoom = zoom
        self.offset = offset

    def fixPoint(self, p0):
        (x, y) = p0
        x0 = self.xBase + (x + self.x0 + self.xOffset) * self.scale
        y0 = self.yBase - (y + self.yOffset) * self.scale
        return (x0, y0)

    def dxfPoint(self, p0):
        (x, y) = p0
        x += self.x0
        return (x, y)

    def drawLine(self, p0, p1, layer=0):
        if self.d != None:
            self.d.add(dxf.line(self.dxfPoint(p0), self.dxfPoint(p1),
                                layer=layer))

        if self.dc != None:
            (x0, y0) = self.fixPoint(p0)
            (x1, y1) = self.fixPoint(p1)
            pen = self.pen[layer]
            if pen != None:
                self.dc.SetPen(pen)
            self.dc.DrawLine(x0, y0, x1, y1)

    def addText(self, text, p0, align=None, layer='TEXT'):
        if self.d != None:
            (x, y) = self.dxfPoint
            hOffset = self.hS
            vOffset = -self.textH / 2
            if align != None:
                textW = len(text) * self.textH * .75
                if align & RIGHT:
                    hOffset = -textW
                elif align & CENTER:
                    hOffset = -textW / 2
                elif align & LEFT:
                    hOffset = self.hS

                if align & ABOVE:
                    vOffset = self.vS
                elif align & BELOW:
                    vOffset = -self.textH - self.vS
                elif align & MIDDLE:
                    vOffset = -self.textH / 2

            self.d.add(dxf.text(text, (x + hOffset, y + vOffset),
                                height=self.textH, layer=layer))

        if self.dc != None:
            size = self.dc.GetMultiLineTextExtent(text)
            if align != None:
                if align & RIGHT:
                    hOffset = -size.width
                elif align & CENTER:
                    hOffset = -size.width / 2
                elif align & LEFT:
                    hOffset = self.hS1

                if align & ABOVE:
                    vOffset = -size.height - self.vS1
                elif align & BELOW:
                    vOffset = self.vS1
                elif align & MIDDLE:
                    vOffset = -size.height / 2

            color = self.color[layer]
            if color != None:
                self.dc.SetTextForeground(color)
            (x, y) = self.fixPoint(p0)
            self.dc.DrawText(text, x + hOffset, y + vOffset)

    def drawCircle(self, radius, center, layer):
        if self.d != None:
            self.d.add(dxf.circle(radius, self.dxfPoint(center), layer=layer))

        if self.dc != None:
            pen = self.pen[layer]
            if pen != None:
                self.dc.SetPen(pen)
            (x, y) = self.fixPoint(center)
            radius *= self.scale
            size = 2 * radius
            self.dc.SetBrush(wx.Brush('white', wx.TRANSPARENT))
            self.dc.DrawEllipse(x - radius, y - radius, size, size)

    def drawShape(self, path, color, colorName):
        if self.d != None:
            points = []
            for p in path:
                points.append(self.dxfPoint(p))
            self.d.add(dxf.solid(points, color=color))

        if self.dc != None:
            points = []
            for p in path:
                points.append(self.fixPoint(p))

            self.dc.SetBrush(wx.Brush(colorName))
            self.dc.SetPen(wx.Pen(colorName))
            self.dc.DrawPolygon(points)

    def drawRefLine(self, y, label, layer, align=AL_RIGHT):
        yPos = -y / 2
        txt = "%0.4f" % (y)
        self.drawLine((0 - self.pitch, yPos),
                      (0 + self.pitch, yPos), layer=layer)
        if align != None:
            hOffset = 0
            if align & AL_LEFT:
                hOffset = -self.pitch
                txt = txt + ' ' + label
            elif align & AL_RIGHT:
                hOffset = self.pitch
                txt = label + ' ' + txt
            elif align & AL_CENTER:
                hOffset = 0
            self.addText(txt, (0 + hOffset, yPos), align | MIDDLE)

    def draw(self, dc=None):
        self.dc = dc
        d = None
        if dc == None:
            tmp = "thread%0.3f-%0.1f" % (self.diam, self.tpi)
            tmp = tmp.replace("0.", "-")
            tmp = tmp.replace(".0", "")
            tmp = tmp.replace(".", "-") + ".dxf"
            d = dxf.drawing(tmp)
            d.add_layer(REF, color=0)
            d.add_layer(TEXT, color=0)
            d.add_layer(MAJOR, color=1)
            d.add_layer(PITCH, color=2)
            d.add_layer(MINOR, color=3)
            d.add_layer(TIP, color=5)
            d.add_layer(WIRE, color=6)
            self.textH = self.height / 40
            self.vS = self.textH / 2
            self.hS = self.textH
        self.d = d

        if self.dc != None:
            if self.zoom:
                fontSize = 12
            else:
                fontSize = 6
            self.font = wx.Font(fontSize, wx.MODERN, wx.NORMAL,
                                wx.NORMAL, False, u'Consolas')
            self.dc.SetFont(self.font)
            wx.lib.colourdb.updateColourDB()

            self.pen = {}
            self.pen[TEXT] = self.pen[REF] = blackPen = wx.Pen("black")
            self.pen[MAJOR] = redPen = wx.Pen("red")
            self.pen[MINOR] = greenPen = wx.Pen("green")
            self.pen[PITCH] = yellowPen = wx.Pen("yellow")
            self.pen[TIP] = bluePen = wx.Pen("blue")
            self.pen[WIRE] = magentaPen = wx.Pen("magenta")

            self.color = {}
            self.color[TEXT] = self.color[REF] = wx.Colour("black")
            self.color[MAJOR] = wx.Colour("red")
            self.color[MINOR] = wx.Colour("green")
            self.color[PITCH] = wx.Colour("yellow")
            self.color[TIP] = wx.Colour("blue")
            self.color[WIRE] = wx.Colour("magenta")
            
            self.vS1 = 3
            self.hS1 = 3

        pitch = self.pitch
        halfP = pitch / 2
        cos295 = cos(radians(29.5))
        sqrt3 = sqrt(3)

        # external threads

        self.x0 = -1.275 * pitch

        self.drawRefLine(self.diam, '', REF, AL_CENTER|CENTER|BELOW)
        # txt = "Diameter %0.4f" % (self.diam)
        # self.addText(txt, (0, -self.diam / 2), CENTER|BELOW)

        txt = "Pitch %0.4f" % (pitch)
        self.addText(txt, (0 + halfP, -self.diam / 2),
                     CENTER|BELOW)

        txt = "Height %0.4f" % (self.height)
        self.addText(txt, (0, -self.diam / 2 + self.height),
                     CENTER|ABOVE)

        radius = self.diam / 2
        p0 = (0 - halfP, -radius)
        p1 = (0 + halfP , -radius)
        p2 = (0, -radius + self.height)
        self.drawLine(p0, p1, layer=REF)
        self.drawLine(p1, p2, layer=REF)
        self.drawLine(p2, p0, layer=REF)
        p2 = (0 - pitch , -radius + self.height)
        self.drawLine(p0, p2, layer=REF)
        p2 = (0 + pitch , -radius + self.height)
        self.drawLine(p1, p2, layer=REF)

        extAvgMajDiam = (self.extMinMajDiam +
                         (self.extMaxMajDiam - self.extMinMajDiam) / 2)

        extMeasuredDiam = self.extMinMajDiam

        x0 = 0 - halfP
        for x0 in (0 - halfP, 0 + halfP):
            y = -extMeasuredDiam / 2
            ofs =  (self.diam / 2 + y) / sqrt3
            p0 = (x0 - ofs, y)
            p1 = (x0 + ofs, y)
            y = -self.extMinMinorDiam / 2
            ofs = (self.diam / 2 + y) / sqrt3
            p2 = (x0 + ofs, y)
            p3 = (x0 - ofs, y)
            self.drawShape([p0, p1, p2, p3], color=0, colorName="lightblue")

        self.drawRefLine(self.extMaxMajDiam, 'Max Major', MAJOR,
                         AL_RIGHT|LEFT|MIDDLE)
        self.drawRefLine(extAvgMajDiam, 'Avg Major', MAJOR,
                         AL_RIGHT|LEFT|MIDDLE)
        self.drawRefLine(self.extMinMajDiam, 'Min Major', MAJOR,
                         AL_RIGHT|LEFT|MIDDLE)

        self.drawRefLine(self.extMaxPitchDiam, 'Max Pitch', PITCH,
                         AL_RIGHT|LEFT|MIDDLE)
        self.drawRefLine(self.extPitchDiam, 'Pitch', PITCH,
                         AL_RIGHT|RIGHT|BELOW)
        self.drawRefLine(self.extMinPitchDiam, 'Min Pitch', PITCH,
                         AL_RIGHT|LEFT|MIDDLE)

        self.drawRefLine(self.extMaxMinorDiam, 'Max Minor', MINOR,
                         AL_RIGHT|LEFT|MIDDLE)
        self.drawRefLine(self.extMinMinorDiam, 'Min Minor', MINOR,
                         AL_RIGHT|LEFT|MIDDLE)

        tipRadius = 0.06 / 25.4
        tipDepth = (self.height - tipRadius)
        p0 = (0, -self.diam / 2 + tipDepth - tipRadius)
        self.drawCircle(tipRadius, p0, layer="TIP")

        tipDepth -= (self.diam - extMeasuredDiam) / 2
        txt = "Tip depth %0.4f" % (tipDepth)
        p0 = (0 + halfP, -self.extMinMinorDiam / 2)
        self.addText(txt, p0, CENTER|ABOVE)

        txt = "29.5 feed %0.4f" % (tipDepth / cos295)
        self.addText(txt, p0, CENTER|BELOW)

        flatWidth = .125 * pitch
        txt = "Flat width %0.4f" % (flatWidth)
        p0 = (0 - flatWidth / 2, -self.extMinMinorDiam / 2)
        self.addText(txt, p0, RIGHT|ABOVE)

        txt = "Tip Radius %0.4f" % (tipRadius)
        p0 = (0 + flatWidth / 2, -self.extMinMinorDiam / 2)
        self.addText(txt, p0, LEFT|ABOVE)

        flatDepth = self.height - sqrt3 / 2 * flatWidth
        y = -self.diam / 2 + flatDepth
        p0 = (0 - flatWidth / 2, y)
        p1 = (0 + flatWidth / 2, y)
        self.drawLine(p0, p1, layer=REF)

        flatDepth = self.height - (self.diam - extMeasuredDiam) / 2
        txt = "Flat depth %0.4f" % (flatDepth)
        p0 = (0 - halfP, -self.extMinMinorDiam / 2)
        self.addText(txt, p0, CENTER|ABOVE)

        txt = "29.5 feed %0.4f" % (flatDepth / cos295)
        self.addText(txt, p0, CENTER|BELOW)

        # print "tipDepth %0.5f flatDepth %0.5f" % (tipDepth, flatDepth)

        y =  -self.extMaxMinorDiam / 2
        minDepth = extMeasuredDiam / 2 + y
        txt = "Min depth %0.4f" % (minDepth)
        self.addText(txt, (0 - halfP, y), CENTER|ABOVE)

        wireRadius = self.actualWire / 2
        wireDepth = self.height - self.actualWire
        yWire = -self.diam / 2 + wireDepth
        p0 = (0, yWire)
        self.drawCircle(wireRadius, p0, layer="WIRE")

        yWire -= wireRadius
        if d != None:
            txt = "Wire Size %0.4f" % (self.actualWire)
            self.addText(txt, (0, yWire), CENTER | BELOW, WIRE)

            textH = -(self.textH + self.vS)
            txt = "Min Wire %0.4f" % (self.minWire)
            self.addText(txt, (0, yWire + textH), CENTER | BELOW, WIRE)

            textH = -2 * (self.textH + self.vS)
            txt = "Max Wire %0.4f" % (self.maxWire)
            self.addText(txt, (0, yWire + textH), CENTER | BELOW, WIRE)

        if dc != None:
            txt = ("Wire Size %0.4f\nMin Wire %0.4f\nMax Wire %0.4f" % 
                   (self.actualWire, self.minWire, self.maxWire))
            self.addText(txt, (0, yWire), CENTER | BELOW, WIRE)

        # internal threads

        self.x0 = 1.275 * pitch

        intFlatWidth = 0.041667 * pitch
        intFlatDiam = self.intMinMajDiam - intFlatWidth * sqrt3
        print ("intFlatWidth %0.4f intFlatDiam %0.4f" %
               (intFlatWidth, intFlatDiam))

        p0 = (0 - halfP, -radius)
        p1 = (0 + halfP , -radius)
        p2 = (0, -radius + self.height)
        self.drawLine(p0, p1, layer=REF)
        self.drawLine(p1, p2, layer=REF)
        self.drawLine(p2, p0, layer=REF)

        p2 = (0 - pitch , -radius + self.height)
        self.drawLine(p0, p2, layer=REF)
        p2 = (0 + pitch , -radius + self.height)
        self.drawLine(p1, p2, layer=REF)

        y = -self.intMinMinorDiam / 2
        ofs = (self.height -self.intMinMajDiam / 2 - y) / sqrt3
        p2 = (0 + ofs, y)
        p3 = (0 - ofs, y)
        self.drawShape([p0, p1, p2, p3], color=0, colorName="lightblue")

        px = (0 - pitch + ofs, y)
        p2 = (0 - pitch, y)
        p3 = (0 - pitch, -radius)
        self.drawShape([p0, px, p2, p3], color=0, colorName="lightblue")

        px = (0 + pitch - ofs, y)
        p2 = (0 + pitch, y)
        p3 = (0 + pitch , -radius)
        self.drawShape([p1, px, p2, p3], color=0, colorName="lightblue")

        self.drawRefLine(self.intMinMajDiam, 'Min Major', MAJOR,
                         AL_LEFT|RIGHT|MIDDLE)

        self.drawRefLine(intFlatDiam, 'Flat Diam', MAJOR,
                         AL_LEFT|RIGHT|MIDDLE)

        self.drawRefLine(extMeasuredDiam, 'Actual Ext', MAJOR,
                         AL_LEFT|RIGHT|MIDDLE)

        self.drawRefLine(self.intMinPitchDiam, 'Min Pitch', PITCH,
                         AL_LEFT|RIGHT|MIDDLE)
        self.drawRefLine(self.intMaxPitchDiam, 'Max Pitch', PITCH,
                         AL_LEFT|RIGHT|MIDDLE)

        self.drawRefLine(self.intMinMinorDiam, 'Min Minor', MINOR,
                         AL_LEFT|RIGHT|MIDDLE)
        self.drawRefLine(self.intMaxMinorDiam, 'Max Minor', MINOR,
                         AL_LEFT|RIGHT|MIDDLE)

        for x in (-halfP, halfP):
            p0 = (0 + x, -self.intMinMajDiam / 2 + 2 * tipRadius)
            self.drawCircle(tipRadius, p0, layer="TIP")

        intTipDepth = self.intDblHeight / 2 - tipRadius
        txt = "Tip depth %0.4f" % (intTipDepth)
        p0 = (0 + halfP, -self.intMinMinorDiam / 2)
        self.addText(txt, p0, CENTER|ABOVE)

        txt = "Tip feed %0.4f" % (intTipDepth / cos295)
        self.addText(txt, p0, CENTER|BELOW)

        intFlatDepth = (intFlatDiam - self.intMinMinorDiam) / 2
        txt = "Flat depth %0.4f" % (intFlatDepth)
        p0 = (0 - halfP, -self.intMinMinorDiam / 2)
        self.addText(txt, p0, CENTER|ABOVE)

        txt = "Flat feed %0.4f" % (intFlatDepth / cos295)
        self.addText(txt, p0, CENTER|BELOW)

        try:
            if d != None:
                d.save()
        except:
            print "dxf file save error"

class MainFrame(wx.Frame): 
    def __init__(self, parent, title): 
        super(MainFrame, self).__init__(parent, title = title)
        self.Maximize(True)
        self.InitUI() 
        # colors = wx.lib.colourdb.getColourList()
        # for line in colors:
        #     print line
        # stdout.flush()
         
    def InitUI(self): 
        global arg1, arg2
        self.zoom = False
        self.left = None
        self.Bind(wx.EVT_PAINT, self.OnPaint) 
        self.Centre() 
        self.tc = ThreadCalc(self)
        self.tc.calc(arg1, arg2)
        self.Bind(wx.EVT_LEFT_UP, self.OnMouseEvent)
        self.Show(True)

    def OnMouseEvent(self, e):
        x = e.GetX()
        if not self.zoom:
            self.zoom = True
            self.offset = x > self.tc.xBase
        else:
            self.zoom = False
            self.offset = False
        self.tc.setZoomOffset(self.zoom, self.offset)
        self.Refresh()
		
    def OnPaint(self, e): 
        dc = wx.PaintDC(self) 
        dc.SetMapMode(wx.MM_TEXT)
        brush = wx.Brush("white")
        dc.SetBackground(brush)  
        dc.Clear() 
        self.tc.calcScale()
        self.tc.draw(dc)
        
        # color = wx.Colour(255,0,0)
        # dc.SetTextForeground(color) 
        # dc.DrawText("Hello wxPython",10,10)
        # dc.DrawLine(10,10, 100,10)
		
arg1 = None
arg2 = None
if __name__ == '__main__':
    print "starting"
    stdout.flush()
    if len(argv) >= 3:
        try:
            arg1 = float(argv[1])
            arg2 = float(argv[2])
        except ValueError:
            print "invalid argument"
            sys.exit()
    else:
            arg1 = 0.5
            arg2 = 28
    if len(argv) >= 4:
        tc = ThreadCalc()
        tc.calc(arg1, arg2)
        tc.draw()
    else:
        ex = wx.App() 
        MainFrame(None,'Drawing demo') 
        ex.MainLoop()
