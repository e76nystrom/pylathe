# fpga bits

# RiscV control register

riscvData    = 0x01             # riscv data active
riscvSPI     = 0x02             # riscv spi active
riscvInTest  = 0x04             # riscv input test

# status register

zAxisEna     = 0x01             # 'ZE' z axis enable flag
zAxisDone    = 0x02             # 'ZD' z axis done
zAxisCurDir  = 0x04             # 'Zd' z axis current dir
xAxisEna     = 0x08             # 'XE' x axis enable flag
xAxisDone    = 0x10             # 'XD' x axis done
xAxisCurDir  = 0x20             # 'Xd' x axis current dir
stEStop      = 0x40             # 'ES' emergency stop
spindleActive = 0x80            # 'S+' spindle active
syncActive   = 0x100            # 'SA' sync active

# input register

inPin10      = 0x01             # '10' pin 10
inPin11      = 0x02             # '11' pin 11
inPin12      = 0x04             # '12' pin 12
inPin13      = 0x08             # '13' pin 13
inPin15      = 0x10             # '15' pin 15
inZHome      = 0x20             # 'ZH' z home switch
inZMinus     = 0x40             # 'Z-' z limit minus
inZPlus      = 0x80             # 'Z+' z Limit Plus
inXHome      = 0x100            # 'XH' x home switch
inXMinus     = 0x200            # 'X-' x limit minus
inXPlus      = 0x400            # 'X+' x Limit Plus
inProbe      = 0x800            # 'PR' probe input
inSpare      = 0x1000           # 'SP' spare input

# axis inputs

axHome       = 0x01             # axis home
axMinus      = 0x02             # axis minus limit
axPlus       = 0x04             # axis plus limit
axProbe      = 0x08             # axis probe

# output register

outPin1      = 0x01             # pin 1
outPin14     = 0x02             # pin 14
outPin17     = 0x04             # pin 17

# pin out signals

pinOut2      = 0x01             # z dir
pinOut3      = 0x02             # z step
pinOut4      = 0x04             # x dir
pinOut5      = 0x08             # x step
pinOut6      = 0x10             # 
pinOut7      = 0x20             # 
pinOut8      = 0x40             # 
pinOut9      = 0x80             # 
pinOut1      = 0x100            # 
pinOut14     = 0x200            # 
pinOut16     = 0x400            # 
pinOut17     = 0x800            # 

# jog control register

jogContinuous = 0x01            # jog continuous mode
jogBacklash  = 0x02             # jog backlash present

# axis control register

ctlInit      = 0x01             # 'IN' reset flag
ctlStart     = 0x02             # 'ST' start
ctlBacklash  = 0x04             # 'BK' backlash move no pos upd
ctlWaitSync  = 0x08             # 'WS' wait for sync to start
ctlDir       = 0x10             # '+-' direction
ctlSetLoc    = 0x20             # 'SL' set location
ctlChDirect  = 0x40             # 'CH' ch input direct
ctlSlave     = 0x80             # 'SL' slave ctl by other axis
ctlDroEnd    = 0x100            # 'DE' use dro to end move
ctlDistMode  = 0x200            # 'DM' distance udpdate mode
ctlJogCmd    = 0x400            # 'JC' jog with commands
ctlJogMpg    = 0x800            # 'JM' jog with mpg
ctlHome      = 0x1000           # 'HO' homing axis
ctlHomePol   = 0x2000           # 'HP' home signal polarity
ctlProbe     = 0x4000           # 'PR' probe enable
ctlUseLimits = 0x8000           # 'UL' use limits

# axis status register

axDone       = 0x01             # 'DN' axis done
axDistZero   = 0x02             # 'ZE' axis distance zero
axDoneDro    = 0x04             # 'DR' axis done dro
axDoneHome   = 0x08             # 'HO' axis done home
axDoneLimit  = 0x10             # 'LI' axis done limit
axDoneProbe  = 0x20             # 'PR' axis done probe
axInHome     = 0x40             # 'IH' axis home
axInMinus    = 0x80             # 'IM' axis minus limit
axInPlus     = 0x100            # 'IP' axis plus limit
axInProbe    = 0x200            # 'IR' axis probe

# configuration control register

cfgZDirInv   = 0x01             # z dir inverted
cfgXDirInv   = 0x02             # x dir inverted
cfgZDroInv   = 0x04             # z dro dir inverted
cfgXDroInv   = 0x08             # x dro dir inverted
cfgZMpgInv   = 0x10             # z mpg dir inverted
cfgXMpgInv   = 0x20             # x mpg dir inverted
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
clkMask      = 0x07             # clock mask
clkNone      = 0x00             # 
clkFreq      = 0x04             # 
clkCh        = 0x08             # 
clkIntClk    = 0x0c             # 
clkSlvFreq   = 0x10             # 
clkSlvCh     = 0x14             # 
clkSpindle   = 0x18             # 
clkDbgFreq   = 0x1c             # 
zClkNone     = 0x00             # 
zClkZFreq    = 0x04             # 
zClkCh       = 0x08             # 
zClkIntClk   = 0x0c             # 
zClkXFreq    = 0x10             # 
zClkXCh      = 0x14             # 
zClkSpindle  = 0x18             # 
zClkDbgFreq  = 0x1c             # 
xClkNone     = 0x00             # 
xClkXFreq    = 0x20             # 
xClkCh       = 0x40             # 
xClkIntClk   = 0x60             # 
xClkZFreq    = 0x80             # 
xClkZCh      = 0xa0             # 
xClkSpindle  = 0xc0             # 
xClkDbgFreq  = 0xe0             # 
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
