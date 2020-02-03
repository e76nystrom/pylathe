
# xilinx bits

# status register

zAxisEna     = 0x01             # z axis enable flag
zAxisDone    = 0x02             # z axis done
xAxisEna     = 0x04             # x axis enable flag
xAxisDone    = 0x08             # x axis done
queEmpty     = 0x10             # controller queue empty
ctlIdle      = 0x20             # controller idle

# run control register

runEna       = 0x01             # run from controller data
runInit      = 0x02             # initialize controller

# axis control register

ctlInit      = 0x01             # reset flag
ctlStart     = 0x02             # start
ctlBacklash  = 0x04             # backlash move no pos upd
ctlWaitSync  = 0x08             # wait for sync to start
ctlDir       = 0x10             # direction
ctlDirPos    = 0x10             # move in positive dir
ctlDirNeg    = 0x00             # move in negative dir
ctlSetLoc    = 0x20             # set location
ctlChDirect  = 0x40             # ch input direct
ctlSlave     = 0x80             # slave controlled by other axis

# configuration control register

cfgZDir      = 0x01             # z direction inverted
cfgXDir      = 0x02             # x direction inverted
cfgSpDir     = 0x04             # spindle directiion inverted
cfgEncDir    = 0x08             # invert encoder direction
cfgEnaEncDir = 0x10             # enable encoder direction
cfgGenSync   = 0x20             # no encoder generate sync pulse

# clock control register

clkNone      = 0x00             # 
clkFreq      = 0x01             # 
clkCh        = 0x02             # 
clkIntClk    = 0x03             # 
clkSlvStep   = 0x04             # 
clkslvFreq   = 0x05             # 
clkSpare     = 0x06             # 
clkDbgFreq   = 0x07             # 
zFreqSel     = 0x07             # z Frequency select
zClkNone     = 0x00             # 
zClkZFreq    = 0x01             # 
zClkCh       = 0x02             # 
zClkIntClk   = 0x03             # 
zClkXStep    = 0x04             # 
zClkXFreq    = 0x05             # 
zClkSpare    = 0x06             # 
zClkDbgFreq  = 0x07             # 
xFreqSel     = 0x38             # x Frequency select
xClkNone     = 0x00             # 
xClkXFreq    = 0x08             # 
xClkCh       = 0x10             # 
xClkIntClk   = 0x18             # 
xClkZStep    = 0x20             # 
xClkZFreq    = 0x28             # 
xClkSpare    = 0x06             # 
xClkDbgFreq  = 0x38             # 
clkDbgFreqEna = 0x40            # enable debug frequency

# sync control register

synPhaseInit = 0x01             # init phase counter
synEncInit   = 0x02             # init encoder
synEncEna    = 0x04             # enable encoder

importList = ( \
 zAxisEna, \
 zAxisDone, \
 xAxisEna, \
 xAxisDone, \
 queEmpty, \
 ctlIdle, \
 runEna, \
 runInit, \
 ctlInit, \
 ctlStart, \
 ctlBacklash, \
 ctlWaitSync, \
 ctlDir, \
 ctlDirPos, \
 ctlDirNeg, \
 ctlSetLoc, \
 ctlChDirect, \
 ctlSlave, \
 cfgZDir, \
 cfgXDir, \
 cfgSpDir, \
 cfgEncDir, \
 cfgEnaEncDir, \
 cfgGenSync, \
 clkNone, \
 clkFreq, \
 clkCh, \
 clkIntClk, \
 clkSlvStep, \
 clkslvFreq, \
 clkSpare, \
 clkDbgFreq, \
 zFreqSel, \
 zClkNone, \
 zClkZFreq, \
 zClkCh, \
 zClkIntClk, \
 zClkXStep, \
 zClkXFreq, \
 zClkSpare, \
 zClkDbgFreq, \
 xFreqSel, \
 xClkNone, \
 xClkXFreq, \
 xClkCh, \
 xClkIntClk, \
 xClkZStep, \
 xClkZFreq, \
 xClkSpare, \
 xClkDbgFreq, \
 clkDbgFreqEna, \
 synPhaseInit, \
 synEncInit, \
 synEncEna, \
)
