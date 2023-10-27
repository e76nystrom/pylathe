# fpga bits

# RiscV control register

riscvData    = 0x01             # riscv data active
riscvSPI     = 0x02             # riscv spi active

# status register

zAxisEna     = 0x01             # 'ZE' z axis enable flag
zAxisDone    = 0x02             # 'ZD' z axis done
zAxisCurDir  = 0x04             # 'Zd' z axis current dir
xAxisEna     = 0x08             # 'XE' x axis enable flag
xAxisDone    = 0x10             # 'XD' x axis done
xAxisCurDir  = 0x20             # 'Xd' x axis current dir
stEStop      = 0x40             # 'ES' emergency stop
spindleActive = 0x80            # 'S+' spindle active
queNotEmpty  = 0x100            # 'Q+' ctl queue not empty
ctlBusy      = 0x200            # 'CB' controller busy
syncActive   = 0x400            # 'SA' sync active

# inputs register

inZHome      = 0x01             # z home switch
inZMinus     = 0x02             # z limit minus
inZPlus      = 0x04             # z Limit Plus
inXHome      = 0x08             # x home switch
inXMinus     = 0x10             # x limit minus
inXPlus      = 0x20             # x Limit Plus
inSpare      = 0x40             # spare input
inProbe      = 0x80             # probe input
inPin10      = 0x100            # pin 10
inPin11      = 0x200            # pin 11
inPin12      = 0x400            # pin 12
inPin13      = 0x800            # pin 13
inPin15      = 0x1000           # pin 15

# run control register

runEna       = 0x01             # run from controller data
runInit      = 0x02             # initialize controller
readerInit   = 0x04             # initialize reader

# jog control register

jogContinuous = 0x01            # jog continuous mode
jogBacklash  = 0x02             # jog backlash present

# axis control register

ctlInit      = 0x01             # reset flag
ctlStart     = 0x02             # start
ctlBacklash  = 0x04             # backlash move no pos upd
ctlWaitSync  = 0x08             # wait for sync to start
ctlDir       = 0x10             # direction
ctlSetLoc    = 0x20             # set location
ctlChDirect  = 0x40             # ch input direct
ctlSlave     = 0x80             # slave ctl by other axis
ctlDroEnd    = 0x100            # use dro to end move
ctlJogCmd    = 0x200            # jog with commands
ctlJogMpg    = 0x400            # jog with mpg
ctlHome      = 0x800            # homing axis
ctlUseLimits = 0x1000           # use limits

# axis status register

axDoneDist   = 0x01             # axis done distance
axDoneDro    = 0x02             # axis done dro
axDoneHome   = 0x04             # axis done home
axDoneLimit  = 0x08             # axis done limit

# configuration control register

cfgZDirInv   = 0x01             # z dir inverted
cfgXDirInv   = 0x02             # x dir inverted
cfgZDroInv   = 0x04             # z dro dir inverted
cfgXDroInv   = 0x08             # x dro dir inverted
cfgZJogInv   = 0x10             # z jog dir inverted
cfgXJogInv   = 0x20             # x jog dir inverted
cfgSpDirInv  = 0x40             # spindle dir inverted
cfgZHomeInv  = 0x80             # z home inverted
cfgZMinusInv = 0x100            # z minus inverted
cfgZPlusInv  = 0x200            # z plus inverted
cfgXHomeInv  = 0x400            # x home inverted
cfgXMinusInv = 0x800            # x minus inverted
cfgXPlusInv  = 0x1000           # x plus inverted
cfgProbeInv  = 0x2000           # probe inverted
cfgEncDirInv = 0x4000           # invert encoder dir
cfgEStopEna  = 0x8000           # estop enable
cfgEStopInv  = 0x10000          # estop invert
cfgEnaEncDir = 0x20000          # enable encoder dir
cfgGenSync   = 0x40000          # generate sync pulse
cfgPwmEna    = 0x80000          # pwm enable
cfgDroStep   = 0x100000         # step pulse to dro

# clock control register

zFreqShift   = 0x00             # z Frequency shift
xFreqShift   = 0x03             # x Frequency shift
clkNone      = 0x00             # 
clkFreq      = 0x01             # 
clkCh        = 0x02             # 
clkIntClk    = 0x03             # 
clkSlvFreq   = 0x04             # 
clkSlvCh     = 0x05             # 
clkSpindle   = 0x06             # 
clkDbgFreq   = 0x07             # 
zClkNone     = 0x00             # 
zClkZFreq    = 0x01             # 
zClkCh       = 0x02             # 
zClkIntClk   = 0x03             # 
zClkXFreq    = 0x04             # 
zClkXCh      = 0x05             # 
zClkSpindle  = 0x06             # 
zClkDbgFreq  = 0x07             # 
xClkNone     = 0x00             # 
xClkXFreq    = 0x08             # 
xClkCh       = 0x10             # 
xClkIntClk   = 0x18             # 
xClkZFreq    = 0x20             # 
xClkZCh      = 0x28             # 
xClkSpindle  = 0x30             # 
xClkDbgFreq  = 0x38             # 
clkDbgFreqEna = 0x40            # enable debug frequency

# sync control register

synPhaseInit = 0x01             # init phase counter
synEncInit   = 0x02             # init encoder
synEncEna    = 0x04             # enable encoder

# spindle control register

spInit       = 0x01             # spindle init
spEna        = 0x02             # spindle enable
spDir        = 0x04             # spindle direction
spJogEnable  = 0x08             # spindle jog enable

importList = ( \
 riscvData, \
 riscvSPI, \
 zAxisEna, \
 zAxisDone, \
 zAxisCurDir, \
 xAxisEna, \
 xAxisDone, \
 xAxisCurDir, \
 stEStop, \
 spindleActive, \
 queNotEmpty, \
 ctlBusy, \
 syncActive, \
 inZHome, \
 inZMinus, \
 inZPlus, \
 inXHome, \
 inXMinus, \
 inXPlus, \
 inSpare, \
 inProbe, \
 inPin10, \
 inPin11, \
 inPin12, \
 inPin13, \
 inPin15, \
 runEna, \
 runInit, \
 readerInit, \
 jogContinuous, \
 jogBacklash, \
 ctlInit, \
 ctlStart, \
 ctlBacklash, \
 ctlWaitSync, \
 ctlDir, \
 ctlSetLoc, \
 ctlChDirect, \
 ctlSlave, \
 ctlDroEnd, \
 ctlJogCmd, \
 ctlJogMpg, \
 ctlHome, \
 ctlUseLimits, \
 axDoneDist, \
 axDoneDro, \
 axDoneHome, \
 axDoneLimit, \
 cfgZDirInv, \
 cfgXDirInv, \
 cfgZDroInv, \
 cfgXDroInv, \
 cfgZJogInv, \
 cfgXJogInv, \
 cfgSpDirInv, \
 cfgZHomeInv, \
 cfgZMinusInv, \
 cfgZPlusInv, \
 cfgXHomeInv, \
 cfgXMinusInv, \
 cfgXPlusInv, \
 cfgProbeInv, \
 cfgEncDirInv, \
 cfgEStopEna, \
 cfgEStopInv, \
 cfgEnaEncDir, \
 cfgGenSync, \
 cfgPwmEna, \
 cfgDroStep, \
 zFreqShift, \
 xFreqShift, \
 clkNone, \
 clkFreq, \
 clkCh, \
 clkIntClk, \
 clkSlvFreq, \
 clkSlvCh, \
 clkSpindle, \
 clkDbgFreq, \
 zClkNone, \
 zClkZFreq, \
 zClkCh, \
 zClkIntClk, \
 zClkXFreq, \
 zClkXCh, \
 zClkSpindle, \
 zClkDbgFreq, \
 xClkNone, \
 xClkXFreq, \
 xClkCh, \
 xClkIntClk, \
 xClkZFreq, \
 xClkZCh, \
 xClkSpindle, \
 xClkDbgFreq, \
 clkDbgFreqEna, \
 synPhaseInit, \
 synEncInit, \
 synEncEna, \
 spInit, \
 spEna, \
 spDir, \
 spJogEnable, \
)
