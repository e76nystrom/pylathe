# config table

# system config

cfgCmdDis        =   0          # config disable sending commands
cfgCommonLimits  =   1          # config all limit switches on one pin
cfgLimitsEnabled =   2          # config limits enabled
cfgCommonHome    =   3          # config all switches on one pin
cfgDbgSave       =   4          # config save debug info
cfgDRO           =   5          # config dro present
cfgDraw          =   6          # config draw paths
cfgEncoder       =   7          # config encoder counts per revolution
cfgEStop         =   8          # config estop enable
cfgEStopInv      =   9          # config estop invert
cfgExtDro        =  10          # config external digital readout
cfgFcy           =  11          # config microprocesssor clock frequency
cfgFreqMult      =  12          # config fpga frequency multiplier
cfgHomeInPlace   =  13          # config home in place
cfgInvEncDir     =  14          # config fpga invert encoder direction
cfgLCD           =  15          # config enable lcd
cfgMPG           =  16          # config enable manual pulse generator
cfgPrbInv        =  17          # config invert probe signal
cfgRemDbg        =  18          # config print remote debug info
cfgSpEncCap      =  19          # config encoder on capture interrupt
cfgSpEncoder     =  20          # config spindle encoder
cfgSpSync        =  21          # config spindle using timer
cfgSpSyncBoard   =  22          # config spindle sync board
cfgSpUseEncoder  =  23          # config use spindle encoder for threading
cfgTaperCycleDist =  24         # config taper cycle distance
cfgTestMode      =  25          # conifg test mode
cfgTestRPM       =  26          # config fpga test rpm value
cfgTurnSync      =  27          # config for turning synchronization
cfgThreadSync    =  28          # config for threading synchronization
cfgFpgaFreq      =  29          # config fpga frequency
cfgFpga          =  30          # config fpga interface present

# communications config

commPort         =  31          # comm port
commRate         =  32          # comm baud rate

# cutoff config

cuPause          =  33          # cutoff pause before cutting
cuRPM            =  34          # cutoff rpm
cuToolWidth      =  35          # cutoff tool width
cuXEnd           =  36          # cutoff x end
cuXFeed          =  37          # cutoff x feed
cuXRetract       =  38          # cutoff x retract
cuXStart         =  39          # cutoff x start
cuZCutoff        =  40          # cutoff offset to z cutoff
cuZRetract       =  41          # cutoff offset to z retract
cuZStart         =  42          # cutoff z location

# dro position

droXPos          =  43          # dro x position
droZPos          =  44          # dro z position

# external dro

extDroPort       =  45          # external dro port
extDroRate       =  46          # external dro baud Rate

# face config

faAddFeed        =  47          # face 
faPasses         =  48          # face 
faPause          =  49          # face pause before cutting
faRPM            =  50          # face 
faSPInt          =  51          # face 
faSpring         =  52          # face 
faXEnd           =  53          # face 
faXFeed          =  54          # face 
faXRetract       =  55          # face 
faXStart         =  56          # face 
faZEnd           =  57          # face 
faZFeed          =  58          # face 
faZRetract       =  59          # face 
faZStart         =  60          # face 

# jog config

jogInc           =  61          # jog 
jogXPos          =  62          # jog 
jogXPosDiam      =  63          # jog 
jogZPos          =  64          # jog 

# jog panel config

jpSurfaceSpeed   =  65          # jogpanle fpm or rpm
jpXDroDiam       =  66          # jogpanel x dro diameter

# jog time parameters

jogTimeInitial   =  67          # jog time initial
jogTimeInc       =  68          # jog time increment
jogTimeMax       =  69          # jog time max

# keypad

keypadPort       =  70          # external dro port
keypadRate       =  71          # external dro baud Rate

# main panel

mainPanel        =  72          # name of main panel

# spindle config

spAccel          =  73          # spindle acceleration
spAccelTime      =  74          # spindle accelerationtime
spCurRange       =  75          # spindle current range
spInvDir         =  76          # spindle invert direction
spJogAccelTime   =  77          # spindle jog acceleration time
spJogMax         =  78          # spindle jog max speed
spJogMin         =  79          # spindle jog min speed
spJTimeInc       =  80          # spindle jog increment
spJTimeInitial   =  81          # spindle jog initial time 
spJTimeMax       =  82          # spindle jog max
spMaxRPM         =  83          # spindle jog max rpm
spMicroSteps     =  84          # spindle micro steps
spMinRPM         =  85          # spindle minimum rpm
spMotorSteps     =  86          # spindle motor stpes per revolution
spMotorTest      =  87          # use stepper drive to test motor
spPWMFreq        =  88          # spindle pwm frequency
spRangeMin1      =  89          # spindle speed range 1 minimum
spRangeMin2      =  90          # spindle speed range 2 minimum
spRangeMin3      =  91          # spindle speed range 3 minimum
spRangeMin4      =  92          # spindle speed range 4 minimum
spRangeMin5      =  93          # spindle speed range 5 minimum
spRangeMin6      =  94          # spindle speed range 6 minimum
spRangeMax1      =  95          # spindle speed range 1 maximum
spRangeMax2      =  96          # spindle speed range 2 maximum
spRangeMax3      =  97          # spindle speed range 3 maximum
spRangeMax4      =  98          # spindle speed range 4 maximum
spRangeMax5      =  99          # spindle speed range 5 maximum
spRangeMax6      = 100          # spindle speed range 6 maximum
spRanges         = 101          # spindle number of speed ranges
spStepDrive      = 102          # spindle stepper drive
spSwitch         = 103          # spindle off on switch
spTestEncoder    = 104          # spindle test generate encoder test pulse
spTestIndex      = 105          # spindle test generate internal index pulse
spVarSpeed       = 106          # spindle variable speed

# sync communications config

syncPort         = 107          # sync comm port
syncRate         = 108          # sync comm baud rate

# threading config

thAddFeed        = 109          # thread feed to add after done
thAlternate      = 110          # thread althernate thread flanks
thAngle          = 111          # thread hanlf angle of thread
thFirstFeed      = 112          # thread first feed for thread area calc
thFirstFeedBtn   = 113          # thread button to select first feed
thInternal       = 114          # thread internal threads
thLastFeed       = 115          # thread last feed for thread area calculation
thLastFeedBtn    = 116          # thread button to select last feed
thLeftHand       = 117          # thread left hand 
thMM             = 118          # thread button for mm
thPasses         = 119          # thread number of passes
thPause          = 120          # thread pause between passes
thRPM            = 121          # thread speed for threading operation
thRunout         = 122          # thread runout for rh exit or lh entrance
thSPInt          = 123          # thread spring pass interval
thSpring         = 124          # thread number of spring passes at end
thTPI            = 125          # thread select thread in threads per inch
thThread         = 126          # thread field containing tpi or pitch
thXDepth         = 127          # thread x depth of thread
thXRetract       = 128          # thread x retract
thXStart         = 129          # thread x diameter
thXTaper         = 130          # thread x taper
thZ0             = 131          # thread z right end of thread left start
thZ1             = 132          # thread z right start left end
thZRetract       = 133          # thread z retract

# taper config

tpAddFeed        = 134          # tp 
tpAngle          = 135          # tp 
tpAngleBtn       = 136          # tp 
tpDeltaBtn       = 137          # tp 
tpInternal       = 138          # tp 
tpLargeDiam      = 139          # tp 
tpPasses         = 140          # tp 
tpPause          = 141          # tp 
tpRPM            = 142          # tp 
tpSPInt          = 143          # tp 
tpSmallDiam      = 144          # tp 
tpSpring         = 145          # tp 
tpTaperSel       = 146          # tp 
tpXDelta         = 147          # tp 
tpXFeed          = 148          # tp 
tpXFinish        = 149          # tp 
tpXInFeed        = 150          # tp 
tpXRetract       = 151          # tp 
tpZDelta         = 152          # tp 
tpZFeed          = 153          # tp 
tpZLength        = 154          # tp 
tpZRetract       = 155          # tp 
tpZStart         = 156          # tp 

# turn config

tuAddFeed        = 157          # turn 
tuInternal       = 158          # turn internal
tuPasses         = 159          # turn 
tuPause          = 160          # turn 
tuRPM            = 161          # turn 
tuSPInt          = 162          # turn 
tuSpring         = 163          # turn 
tuXDiam0         = 164          # turn 
tuXDiam1         = 165          # turn 
tuXFeed          = 166          # turn 
tuXRetract       = 167          # turn 
tuZEnd           = 168          # turn 
tuZFeed          = 169          # turn 
tuZRetract       = 170          # turn 
tuZStart         = 171          # turn 

# x axis config

xAccel           = 172          # x axis 
xBackInc         = 173          # z axis distance to go past for taking out backlash
xBacklash        = 174          # x axis 
xDoneDelay       = 175          # x axis done to read dro delay
xDroFinalDist    = 176          # x dro final approach dist
xDROInch         = 177          # x axis 
xDROPos          = 178          # x axis use dro to go to correct position
xHomeDir         = 179          # x axis 
xHomeDist        = 180          # x axis 
xHomeDistBackoff = 181          # x axis 
xHomeDistRev     = 182          # x axis 
xHomeEna         = 183          # x axis 
xHomeEnd         = 184          # x axis 
xHomeInv         = 185          # x axis 
xHomeLoc         = 186          # x axis 
xHomeSpeed       = 187          # x axis 
xHomeStart       = 188          # x axis 
xInvDRO          = 189          # x axis invert dro
xInvDir          = 190          # x axis invert stepper direction
xInvEnc          = 191          # x axis 
xInvMpg          = 192          # x axis invert mpg direction
xJogMax          = 193          # x axis 
xJogMin          = 194          # x axis 
xLimEna          = 195          # x axis limits enable
xLimNegInv       = 196          # x axis negative limit invert
xLimPosInv       = 197          # x axis positive limit invert
xMpgInc          = 198          # x axis jog increment
xMpgMax          = 199          # x axis jog maximum
xJogSpeed        = 200          # x axis 
xMaxSpeed        = 201          # x axis 
xMicroSteps      = 202          # x axis 
xMinSpeed        = 203          # x axis 
xMotorRatio      = 204          # x axis 
xMotorSteps      = 205          # x axis 
xParkLoc         = 206          # x axis 
xPitch           = 207          # x axis 
xProbeDist       = 208          # x axis 

# x axis position config

xSvPosition      = 209          # x axis 
xSvHomeOffset    = 210          # x axis 
xSvDROPosition   = 211          # x axis 
xSvDROOffset     = 212          # x axis 

# z axis config

zAccel           = 213          # z axis 
zBackInc         = 214          # z axis distance to go past for taking out backlash
zBacklash        = 215          # z axis 
zDoneDelay       = 216          # z axis done to read dro delay
zDroFinalDist    = 217          # z dro final approach dist
zDROPos          = 218          # z axis use dro to go to correct position
zDROInch         = 219          # z axis 
zHomeDir         = 220          # z axis 
zHomeDist        = 221          # z axis 
zHomeDistRev     = 222          # z axis 
zHomeDistBackoff = 223          # z axis 
zHomeEna         = 224          # z axis 
zHomeEnd         = 225          # z axis 
zHomeInv         = 226          # z axis 
zHomeLoc         = 227          # z axis 
zHomeSpeed       = 228          # z axis 
zHomeStart       = 229          # z axis 
zInvDRO          = 230          # z axis 
zInvDir          = 231          # z axis 
zInvEnc          = 232          # z axis 
zInvMpg          = 233          # z axis 
zJogMax          = 234          # z axis 
zJogMin          = 235          # z axis 
zMpgInc          = 236          # z axis jog increment
zMpgMax          = 237          # z axis jog maximum
zJogSpeed        = 238          # z axis 
zLimEna          = 239          # z axis limits enable
zLimNegInv       = 240          # z axis negative limit invert
zLimPosInv       = 241          # z axis positive limit invert
zMaxSpeed        = 242          # z axis 
zMicroSteps      = 243          # z axis 
zMinSpeed        = 244          # z axis 
zMotorRatio      = 245          # z axis 
zMotorSteps      = 246          # z axis 
zParkLoc         = 247          # z axis 
zPitch           = 248          # z axis 
zProbeDist       = 249          # z axis 
zProbeSpeed      = 250          # z axis 

# z axis position config

zSvPosition      = 251          # z axis 
zSvHomeOffset    = 252          # z axis 
zSvDROPosition   = 253          # z axis 
zSvDROOffset     = 254          # z axis 
cfgJogDebug      = 255          # debug jogging

config = { \
    'cfgCmdDis' : 0,
    'cfgCommonLimits' : 1,
    'cfgLimitsEnabled' : 2,
    'cfgCommonHome' : 3,
    'cfgDbgSave' : 4,
    'cfgDRO' : 5,
    'cfgDraw' : 6,
    'cfgEncoder' : 7,
    'cfgEStop' : 8,
    'cfgEStopInv' : 9,
    'cfgExtDro' : 10,
    'cfgFcy' : 11,
    'cfgFreqMult' : 12,
    'cfgHomeInPlace' : 13,
    'cfgInvEncDir' : 14,
    'cfgLCD' : 15,
    'cfgMPG' : 16,
    'cfgPrbInv' : 17,
    'cfgRemDbg' : 18,
    'cfgSpEncCap' : 19,
    'cfgSpEncoder' : 20,
    'cfgSpSync' : 21,
    'cfgSpSyncBoard' : 22,
    'cfgSpUseEncoder' : 23,
    'cfgTaperCycleDist' : 24,
    'cfgTestMode' : 25,
    'cfgTestRPM' : 26,
    'cfgTurnSync' : 27,
    'cfgThreadSync' : 28,
    'cfgFpgaFreq' : 29,
    'cfgFpga' : 30,
    'commPort' : 31,
    'commRate' : 32,
    'cuPause' : 33,
    'cuRPM' : 34,
    'cuToolWidth' : 35,
    'cuXEnd' : 36,
    'cuXFeed' : 37,
    'cuXRetract' : 38,
    'cuXStart' : 39,
    'cuZCutoff' : 40,
    'cuZRetract' : 41,
    'cuZStart' : 42,
    'droXPos' : 43,
    'droZPos' : 44,
    'extDroPort' : 45,
    'extDroRate' : 46,
    'faAddFeed' : 47,
    'faPasses' : 48,
    'faPause' : 49,
    'faRPM' : 50,
    'faSPInt' : 51,
    'faSpring' : 52,
    'faXEnd' : 53,
    'faXFeed' : 54,
    'faXRetract' : 55,
    'faXStart' : 56,
    'faZEnd' : 57,
    'faZFeed' : 58,
    'faZRetract' : 59,
    'faZStart' : 60,
    'jogInc' : 61,
    'jogXPos' : 62,
    'jogXPosDiam' : 63,
    'jogZPos' : 64,
    'jpSurfaceSpeed' : 65,
    'jpXDroDiam' : 66,
    'jogTimeInitial' : 67,
    'jogTimeInc' : 68,
    'jogTimeMax' : 69,
    'keypadPort' : 70,
    'keypadRate' : 71,
    'mainPanel' : 72,
    'spAccel' : 73,
    'spAccelTime' : 74,
    'spCurRange' : 75,
    'spInvDir' : 76,
    'spJogAccelTime' : 77,
    'spJogMax' : 78,
    'spJogMin' : 79,
    'spJTimeInc' : 80,
    'spJTimeInitial' : 81,
    'spJTimeMax' : 82,
    'spMaxRPM' : 83,
    'spMicroSteps' : 84,
    'spMinRPM' : 85,
    'spMotorSteps' : 86,
    'spMotorTest' : 87,
    'spPWMFreq' : 88,
    'spRangeMin1' : 89,
    'spRangeMin2' : 90,
    'spRangeMin3' : 91,
    'spRangeMin4' : 92,
    'spRangeMin5' : 93,
    'spRangeMin6' : 94,
    'spRangeMax1' : 95,
    'spRangeMax2' : 96,
    'spRangeMax3' : 97,
    'spRangeMax4' : 98,
    'spRangeMax5' : 99,
    'spRangeMax6' : 100,
    'spRanges' : 101,
    'spStepDrive' : 102,
    'spSwitch' : 103,
    'spTestEncoder' : 104,
    'spTestIndex' : 105,
    'spVarSpeed' : 106,
    'syncPort' : 107,
    'syncRate' : 108,
    'thAddFeed' : 109,
    'thAlternate' : 110,
    'thAngle' : 111,
    'thFirstFeed' : 112,
    'thFirstFeedBtn' : 113,
    'thInternal' : 114,
    'thLastFeed' : 115,
    'thLastFeedBtn' : 116,
    'thLeftHand' : 117,
    'thMM' : 118,
    'thPasses' : 119,
    'thPause' : 120,
    'thRPM' : 121,
    'thRunout' : 122,
    'thSPInt' : 123,
    'thSpring' : 124,
    'thTPI' : 125,
    'thThread' : 126,
    'thXDepth' : 127,
    'thXRetract' : 128,
    'thXStart' : 129,
    'thXTaper' : 130,
    'thZ0' : 131,
    'thZ1' : 132,
    'thZRetract' : 133,
    'tpAddFeed' : 134,
    'tpAngle' : 135,
    'tpAngleBtn' : 136,
    'tpDeltaBtn' : 137,
    'tpInternal' : 138,
    'tpLargeDiam' : 139,
    'tpPasses' : 140,
    'tpPause' : 141,
    'tpRPM' : 142,
    'tpSPInt' : 143,
    'tpSmallDiam' : 144,
    'tpSpring' : 145,
    'tpTaperSel' : 146,
    'tpXDelta' : 147,
    'tpXFeed' : 148,
    'tpXFinish' : 149,
    'tpXInFeed' : 150,
    'tpXRetract' : 151,
    'tpZDelta' : 152,
    'tpZFeed' : 153,
    'tpZLength' : 154,
    'tpZRetract' : 155,
    'tpZStart' : 156,
    'tuAddFeed' : 157,
    'tuInternal' : 158,
    'tuPasses' : 159,
    'tuPause' : 160,
    'tuRPM' : 161,
    'tuSPInt' : 162,
    'tuSpring' : 163,
    'tuXDiam0' : 164,
    'tuXDiam1' : 165,
    'tuXFeed' : 166,
    'tuXRetract' : 167,
    'tuZEnd' : 168,
    'tuZFeed' : 169,
    'tuZRetract' : 170,
    'tuZStart' : 171,
    'xAccel' : 172,
    'xBackInc' : 173,
    'xBacklash' : 174,
    'xDoneDelay' : 175,
    'xDroFinalDist' : 176,
    'xDROInch' : 177,
    'xDROPos' : 178,
    'xHomeDir' : 179,
    'xHomeDist' : 180,
    'xHomeDistBackoff' : 181,
    'xHomeDistRev' : 182,
    'xHomeEna' : 183,
    'xHomeEnd' : 184,
    'xHomeInv' : 185,
    'xHomeLoc' : 186,
    'xHomeSpeed' : 187,
    'xHomeStart' : 188,
    'xInvDRO' : 189,
    'xInvDir' : 190,
    'xInvEnc' : 191,
    'xInvMpg' : 192,
    'xJogMax' : 193,
    'xJogMin' : 194,
    'xLimEna' : 195,
    'xLimNegInv' : 196,
    'xLimPosInv' : 197,
    'xMpgInc' : 198,
    'xMpgMax' : 199,
    'xJogSpeed' : 200,
    'xMaxSpeed' : 201,
    'xMicroSteps' : 202,
    'xMinSpeed' : 203,
    'xMotorRatio' : 204,
    'xMotorSteps' : 205,
    'xParkLoc' : 206,
    'xPitch' : 207,
    'xProbeDist' : 208,
    'xSvPosition' : 209,
    'xSvHomeOffset' : 210,
    'xSvDROPosition' : 211,
    'xSvDROOffset' : 212,
    'zAccel' : 213,
    'zBackInc' : 214,
    'zBacklash' : 215,
    'zDoneDelay' : 216,
    'zDroFinalDist' : 217,
    'zDROPos' : 218,
    'zDROInch' : 219,
    'zHomeDir' : 220,
    'zHomeDist' : 221,
    'zHomeDistRev' : 222,
    'zHomeDistBackoff' : 223,
    'zHomeEna' : 224,
    'zHomeEnd' : 225,
    'zHomeInv' : 226,
    'zHomeLoc' : 227,
    'zHomeSpeed' : 228,
    'zHomeStart' : 229,
    'zInvDRO' : 230,
    'zInvDir' : 231,
    'zInvEnc' : 232,
    'zInvMpg' : 233,
    'zJogMax' : 234,
    'zJogMin' : 235,
    'zMpgInc' : 236,
    'zMpgMax' : 237,
    'zJogSpeed' : 238,
    'zLimEna' : 239,
    'zLimNegInv' : 240,
    'zLimPosInv' : 241,
    'zMaxSpeed' : 242,
    'zMicroSteps' : 243,
    'zMinSpeed' : 244,
    'zMotorRatio' : 245,
    'zMotorSteps' : 246,
    'zParkLoc' : 247,
    'zPitch' : 248,
    'zProbeDist' : 249,
    'zProbeSpeed' : 250,
    'zSvPosition' : 251,
    'zSvHomeOffset' : 252,
    'zSvDROPosition' : 253,
    'zSvDROOffset' : 254,
    'cfgJogDebug' : 255,
    }

configTable = ( \
    'cfgCmdDis',
    'cfgCommonLimits',
    'cfgLimitsEnabled',
    'cfgCommonHome',
    'cfgDbgSave',
    'cfgDRO',
    'cfgDraw',
    'cfgEncoder',
    'cfgEStop',
    'cfgEStopInv',
    'cfgExtDro',
    'cfgFcy',
    'cfgFreqMult',
    'cfgHomeInPlace',
    'cfgInvEncDir',
    'cfgLCD',
    'cfgMPG',
    'cfgPrbInv',
    'cfgRemDbg',
    'cfgSpEncCap',
    'cfgSpEncoder',
    'cfgSpSync',
    'cfgSpSyncBoard',
    'cfgSpUseEncoder',
    'cfgTaperCycleDist',
    'cfgTestMode',
    'cfgTestRPM',
    'cfgTurnSync',
    'cfgThreadSync',
    'cfgFpgaFreq',
    'cfgFpga',
    'commPort',
    'commRate',
    'cuPause',
    'cuRPM',
    'cuToolWidth',
    'cuXEnd',
    'cuXFeed',
    'cuXRetract',
    'cuXStart',
    'cuZCutoff',
    'cuZRetract',
    'cuZStart',
    'droXPos',
    'droZPos',
    'extDroPort',
    'extDroRate',
    'faAddFeed',
    'faPasses',
    'faPause',
    'faRPM',
    'faSPInt',
    'faSpring',
    'faXEnd',
    'faXFeed',
    'faXRetract',
    'faXStart',
    'faZEnd',
    'faZFeed',
    'faZRetract',
    'faZStart',
    'jogInc',
    'jogXPos',
    'jogXPosDiam',
    'jogZPos',
    'jpSurfaceSpeed',
    'jpXDroDiam',
    'jogTimeInitial',
    'jogTimeInc',
    'jogTimeMax',
    'keypadPort',
    'keypadRate',
    'mainPanel',
    'spAccel',
    'spAccelTime',
    'spCurRange',
    'spInvDir',
    'spJogAccelTime',
    'spJogMax',
    'spJogMin',
    'spJTimeInc',
    'spJTimeInitial',
    'spJTimeMax',
    'spMaxRPM',
    'spMicroSteps',
    'spMinRPM',
    'spMotorSteps',
    'spMotorTest',
    'spPWMFreq',
    'spRangeMin1',
    'spRangeMin2',
    'spRangeMin3',
    'spRangeMin4',
    'spRangeMin5',
    'spRangeMin6',
    'spRangeMax1',
    'spRangeMax2',
    'spRangeMax3',
    'spRangeMax4',
    'spRangeMax5',
    'spRangeMax6',
    'spRanges',
    'spStepDrive',
    'spSwitch',
    'spTestEncoder',
    'spTestIndex',
    'spVarSpeed',
    'syncPort',
    'syncRate',
    'thAddFeed',
    'thAlternate',
    'thAngle',
    'thFirstFeed',
    'thFirstFeedBtn',
    'thInternal',
    'thLastFeed',
    'thLastFeedBtn',
    'thLeftHand',
    'thMM',
    'thPasses',
    'thPause',
    'thRPM',
    'thRunout',
    'thSPInt',
    'thSpring',
    'thTPI',
    'thThread',
    'thXDepth',
    'thXRetract',
    'thXStart',
    'thXTaper',
    'thZ0',
    'thZ1',
    'thZRetract',
    'tpAddFeed',
    'tpAngle',
    'tpAngleBtn',
    'tpDeltaBtn',
    'tpInternal',
    'tpLargeDiam',
    'tpPasses',
    'tpPause',
    'tpRPM',
    'tpSPInt',
    'tpSmallDiam',
    'tpSpring',
    'tpTaperSel',
    'tpXDelta',
    'tpXFeed',
    'tpXFinish',
    'tpXInFeed',
    'tpXRetract',
    'tpZDelta',
    'tpZFeed',
    'tpZLength',
    'tpZRetract',
    'tpZStart',
    'tuAddFeed',
    'tuInternal',
    'tuPasses',
    'tuPause',
    'tuRPM',
    'tuSPInt',
    'tuSpring',
    'tuXDiam0',
    'tuXDiam1',
    'tuXFeed',
    'tuXRetract',
    'tuZEnd',
    'tuZFeed',
    'tuZRetract',
    'tuZStart',
    'xAccel',
    'xBackInc',
    'xBacklash',
    'xDoneDelay',
    'xDroFinalDist',
    'xDROInch',
    'xDROPos',
    'xHomeDir',
    'xHomeDist',
    'xHomeDistBackoff',
    'xHomeDistRev',
    'xHomeEna',
    'xHomeEnd',
    'xHomeInv',
    'xHomeLoc',
    'xHomeSpeed',
    'xHomeStart',
    'xInvDRO',
    'xInvDir',
    'xInvEnc',
    'xInvMpg',
    'xJogMax',
    'xJogMin',
    'xLimEna',
    'xLimNegInv',
    'xLimPosInv',
    'xMpgInc',
    'xMpgMax',
    'xJogSpeed',
    'xMaxSpeed',
    'xMicroSteps',
    'xMinSpeed',
    'xMotorRatio',
    'xMotorSteps',
    'xParkLoc',
    'xPitch',
    'xProbeDist',
    'xSvPosition',
    'xSvHomeOffset',
    'xSvDROPosition',
    'xSvDROOffset',
    'zAccel',
    'zBackInc',
    'zBacklash',
    'zDoneDelay',
    'zDroFinalDist',
    'zDROPos',
    'zDROInch',
    'zHomeDir',
    'zHomeDist',
    'zHomeDistRev',
    'zHomeDistBackoff',
    'zHomeEna',
    'zHomeEnd',
    'zHomeInv',
    'zHomeLoc',
    'zHomeSpeed',
    'zHomeStart',
    'zInvDRO',
    'zInvDir',
    'zInvEnc',
    'zInvMpg',
    'zJogMax',
    'zJogMin',
    'zMpgInc',
    'zMpgMax',
    'zJogSpeed',
    'zLimEna',
    'zLimNegInv',
    'zLimPosInv',
    'zMaxSpeed',
    'zMicroSteps',
    'zMinSpeed',
    'zMotorRatio',
    'zMotorSteps',
    'zParkLoc',
    'zPitch',
    'zProbeDist',
    'zProbeSpeed',
    'zSvPosition',
    'zSvHomeOffset',
    'zSvDROPosition',
    'zSvDROOffset',
    'cfgJogDebug',
    )
