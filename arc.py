class Arc(LatheOp, UpdatePass):
    def __init__(self, arcPanel):
        LatheOp.__init__(self, arcPanel)
        UpdatePass.__init__(self)
        self.xCut = 0.0
        self.curX = 0.0
        self.neg = False
        self.internal = False

    def getParameters(self):
        tu = self.panel
        self.manual = tu.manual.GetValue()
        self.internal = tu.internal.GetValue()

        rpm = getIntVal(tu.rpm)

    def runOperation(self):
        self.getParameters()

        self.calcFeed(self.xFeed, self.xCut)
        self.setupSpringPasses(self.panel)
        self.setupAction(self.calcPass, self.runPass)

        self.panel.passes.SetValue("%d" % (self.passes))
        print("xCut %5.3f passes %d" % \
              (self.xCut, self.passes))

        self.safeX = self.xStart + self.xRetract
        self.safeZ = self.zStart + self.zRetract

        if cfg.getBoolInfoData(cf.cfgDraw):
            self.m.draw("arc", self.zStart, self.zEnd)

        jogPanel.dPrt("\narc runOperation\n")
        jogPanel.dPrt(timeStr() + "\n")
        self.setup()

        while self.updatePass():
            pass

        self.m.moveX(self.safeX)

        self.passDone()
        return(True)

    def setup(self, add=False): # turn
        comm.queParm(pm.CURRENT_OP, en.OP_ARC)
        m = self.m
        if not add:
            m.setLoc(self.zEnd, self.xStart)
            m.drawLineZ(self.zStart, REF)
            m.drawLineX(self.xEnd, REF)
            m.setLoc(self.safeZ, self.safeX)

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
        jogPanel.dPrt("pass %2d feed %5.3f x %5.3f diameter %5.3f %s\n" % \
                      (self.passCount, feed, self.curX, self.curX * 2.0, \
                       ("", "final")[final]), \
                      True, True)

    def runPass(self, addPass=False): # arc
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
        add = self.addInit("turn") / 2.0
        self.cutAmount += add
        self.setup(True)
        self.calcPass(True)
        moveCommands.nextPass(self.passCount)
        self.runPass(True)
        self.m.moveX(self.xStart + self.xRetract)
        self.addDone()

    def fixCut(self, offset=0.0): # arc
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

class ArcPanel(wx.Panel, FormRoutines, ActionRoutines):
    def __init__(self, parent, hdrFont, *args, **kwargs):
        super(ArcPanel, self).__init__(parent, *args, **kwargs)
        self.hdrFont = hdrFont
        FormRoutines.__init__(self)
        ActionRoutines.__init__(self, Arc(self), en.OP_ARC)
        self.InitUI()
        self.configList = None
        self.prefix = 'arc'
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
        fields0 = self.fields0 = []
        self.sizerV = sizerV = wx.BoxSizer(wx.VERTICAL)

        txt = wx.StaticText(self, -1, "Arc", size=(120, 30))
        txt.SetFont(self.hdrFont)

        sizerV.Add(txt, flag=wx.CENTER|wx.ALL, border=2)

        sizerG = wx.FlexGridSizer(cols=8, rows=0, vgap=0, hgap=0)

        # line 1 radius parameters

        self.radiusStart = self.addField(sizerG, "R Start", cf.arcRStart, 'f')

        self.RadiusEnd = self.addField(sizerG, "R End", cf.arcREnd, 'f')

        self.Feed = self.addField(sizerG, "Feed", cf.arcFeed, 'f')

        self.Retract = self.addField(sizerG, "Retract", cf.arcRetract, 'f')

        # line 2 diameter and angle

        self.diameter = self.addField(sizerG, "Diam", cf.arcCX, 'f')

        self.endDiam = self.addField(sizerG, "End Diam", cf.arcCX, 'f')

        self.angStart = self.addField(sizerG, "Ang Start", cf.arcZFeed, 'f')

        self.angEnd = self.addField(sizerG, "Ang End", cf.arcZRetract, 'f')

        # line 3 z parameters

        self.centerX = self.addField(sizerG, "x Center", cf.arcCX, 'f')

        self.centerZ = self.addField(sizerG, "Z Center", cf.arcCZ, 'f')

        self.toolRadius = self.addField(sizerG, "Z Center", cf.arcToolRad, 'f')

        self.placeHolder(sizerG)

        # line 4 pass info

        self.passes = self.addField(sizerG, "Passes", cf.arcPasses, 'd')
        self.passes.SetEditable(False)

        self.sPInt = self.addField(sizerG, "SP Int", cf.arcSPInt, 'd')
        fields0.append(self.sPInt)

        self.spring = self.addField(sizerG, "Spring", cf.arcSpring, 'd')
        fields0.append(self.spring)

        self.placeHolder(sizerG)
        
        # line 5 buttons

        self.addButtons(sizerG, cf.arcAddFeed, cf.arcRPM, cf.arcPause, True)
        fields0.append(self.sendButton)
        fields0.append(self.add)
        fields0.append(self.pause)

        # self.internal = self.addCheckBox(sizerG, "Internal", cf.arcInternal, \
        #                                  self.OnInternal, box=True)

        sizerV.Add(sizerG, flag=wx.CENTER|wx.ALL, border=2)

        self.SetSizer(sizerV)
        sizerV.Fit(self)

    # def OnInternal(self, e):
    #     self.updateUI()
            
    def updateUI(self):
        if not self.active:
            self.sizerV.Layout()

    def update(self):
        self.updateUI()
        self.formatData(self.formatList)
        jogPanel.setPassText("Radius")

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
        
        # self.active = False
        # jogPanel.setStatus(st.STR_CLR)

