# config table

# arc panel

arcAddFeed       =   0          # arc 
arcBallDist      =   1          # arc 
arcCCW           =   2          # arc 
arcDiam          =   3          # arc 
arcFeed          =   4          # arc 
arcFinish        =   5          # arc 
arcLargeEnd      =   6          # arc 
arcLargeStem     =   7          # arc 
arcPasses        =   8          # arc 
arcPause         =   9          # arc 
arcRetract       =  10          # arc 
arcRadius        =  11          # arc 
arcRPM           =  12          # arc 
arcSmallEnd      =  13          # arc 
arcSmallStem     =  14          # arc 
arcSPInt         =  15          # arc 
arcSpring        =  16          # arc 
arcToolAngle     =  17          # arc 
arcToolRad       =  18          # arc 
arcType          =  19          # arc 
arcXFeed         =  20          # arc 
arcZFeed         =  21          # arc 
arcZStart        =  22          # arc 

# system config

cfgCmdDis        =  23          # config disable sending commands
cfgCommonLimits  =  24          # config all limit switches on one pin
cfgLimitsEnabled =  25          # config limits enabled
cfgCommonHome    =  26          # config all switches on one pin
cfgDbgSave       =  27          # config save debug info
cfgDRO           =  28          # config dro present
cfgDraw          =  29          # config draw paths
cfgEncoder       =  30          # config encoder counts per revolution
cfgEStop         =  31          # config estop enable
cfgEStopInv      =  32          # config estop invert
cfgExtDro        =  33          # config external digital readout
cfgFcy           =  34          # config microprocesssor clock frequency
cfgFreqMult      =  35          # config fpga frequency multiplier
cfgHomeInPlace   =  36          # config home in place
cfgInvEncDir     =  37          # config fpga invert encoder direction
cfgLCD           =  38          # config enable lcd
cfgMPG           =  39          # config enable manual pulse generator
cfgPrbInv        =  40          # config invert probe signal
cfgRemDbg        =  41          # config print remote debug info
cfgSpEncCap      =  42          # config encoder on capture interrupt
cfgSpEncoder     =  43          # config spindle encoder
cfgSpSync        =  44          # config spindle using timer
cfgSpSyncBoard   =  45          # config spindle sync board
cfgSpUseEncoder  =  46          # config use spindle encoder for threading
cfgTaperCycleDist =  47         # config taper cycle distance
cfgTestMode      =  48          # conifg test mode
cfgTestRPM       =  49          # config fpga test rpm value
cfgTurnSync      =  50          # config for turning synchronization
cfgThreadSync    =  51          # config for threading synchronization
cfgFpgaFreq      =  52          # config fpga frequency
cfgFpga          =  53          # config fpga interface present

# communications cxonfig

commPort         =  54          # comm port
commRate         =  55          # comm baud rate

# cutoff config

cuPause          =  56          # cutoff pause before cutting
cuRPM            =  57          # cutoff rpm
cuToolWidth      =  58          # cutoff tool width
cuXEnd           =  59          # cutoff x end
cuXFeed          =  60          # cutoff x feed
cuXRetract       =  61          # cutoff x retract
cuXStart         =  62          # cutoff x start
cuZCutoff        =  63          # cutoff offset to z cutoff
cuZRetract       =  64          # cutoff offset to z retract
cuZStart         =  65          # cutoff z location

# dro position

droXPos          =  66          # dro x position
droZPos          =  67          # dro z position

# external dro

extDroPort       =  68          # external dro port
extDroRate       =  69          # external dro baud Rate

# face config

faAddFeed        =  70          # face 
faPasses         =  71          # face 
faPause          =  72          # face pause before cutting
faRPM            =  73          # face 
faSPInt          =  74          # face 
faSpring         =  75          # face 
faXEnd           =  76          # face 
faXFeed          =  77          # face 
faXRetract       =  78          # face 
faXStart         =  79          # face 
faZEnd           =  80          # face 
faZFeed          =  81          # face 
faZRetract       =  82          # face 
faZStart         =  83          # face 

# jog config

jogInc           =  84          # jog 
jogXPos          =  85          # jog 
jogXPosDiam      =  86          # jog 
jogZPos          =  87          # jog 

# jog panel config

jpSurfaceSpeed   =  88          # jogpanle fpm or rpm
jpXDroDiam       =  89          # jogpanel x dro diameter

# jog time parameters

jogTimeInitial   =  90          # jog time initial
jogTimeInc       =  91          # jog time increment
jogTimeMax       =  92          # jog time max

# keypad

keypadPort       =  93          # external dro port
keypadRate       =  94          # external dro baud Rate

# main panel

mainPanel        =  95          # name of main panel

# spindle config

spAccel          =  96          # spindle acceleration
spAccelTime      =  97          # spindle accelerationtime
spCurRange       =  98          # spindle current range
spInvDir         =  99          # spindle invert direction
spJogAccelTime   = 100          # spindle jog acceleration time
spJogMax         = 101          # spindle jog max speed
spJogMin         = 102          # spindle jog min speed
spJTimeInc       = 103          # spindle jog increment
spJTimeInitial   = 104          # spindle jog initial time 
spJTimeMax       = 105          # spindle jog max
spMaxRPM         = 106          # spindle jog max rpm
spMicroSteps     = 107          # spindle micro steps
spMinRPM         = 108          # spindle minimum rpm
spMotorSteps     = 109          # spindle motor stpes per revolution
spMotorTest      = 110          # use stepper drive to test motor
spPWMFreq        = 111          # spindle pwm frequency
spRangeMin1      = 112          # spindle speed range 1 minimum
spRangeMin2      = 113          # spindle speed range 2 minimum
spRangeMin3      = 114          # spindle speed range 3 minimum
spRangeMin4      = 115          # spindle speed range 4 minimum
spRangeMin5      = 116          # spindle speed range 5 minimum
spRangeMin6      = 117          # spindle speed range 6 minimum
spRangeMax1      = 118          # spindle speed range 1 maximum
spRangeMax2      = 119          # spindle speed range 2 maximum
spRangeMax3      = 120          # spindle speed range 3 maximum
spRangeMax4      = 121          # spindle speed range 4 maximum
spRangeMax5      = 122          # spindle speed range 5 maximum
spRangeMax6      = 123          # spindle speed range 6 maximum
spRanges         = 124          # spindle number of speed ranges
spStepDrive      = 125          # spindle stepper drive
spSwitch         = 126          # spindle off on switch
spTestEncoder    = 127          # spindle test generate encoder test pulse
spTestIndex      = 128          # spindle test generate internal index pulse
spVarSpeed       = 129          # spindle variable speed

# sync communications config

syncPort         = 130          # sync comm port
syncRate         = 131          # sync comm baud rate

# threading config

thAddFeed        = 132          # thread feed to add after done
thAlternate      = 133          # thread althernate thread flanks
thAngle          = 134          # thread hanlf angle of thread
thFirstFeed      = 135          # thread first feed for thread area calc
thFirstFeedBtn   = 136          # thread button to select first feed
thInternal       = 137          # thread internal threads
thLastFeed       = 138          # thread last feed for thread area calculation
thLastFeedBtn    = 139          # thread button to select last feed
thLeftHand       = 140          # thread left hand 
thMM             = 141          # thread button for mm
thPasses         = 142          # thread number of passes
thPause          = 143          # thread pause between passes
thRPM            = 144          # thread speed for threading operation
thRunout         = 145          # thread runout for rh exit or lh entrance
thSPInt          = 146          # thread spring pass interval
thSpring         = 147          # thread number of spring passes at end
thTPI            = 148          # thread select thread in threads per inch
thThread         = 149          # thread field containing tpi or pitch
thXDepth         = 150          # thread x depth of thread
thXRetract       = 151          # thread x retract
thXStart         = 152          # thread x diameter
thXTaper         = 153          # thread x taper
thZ0             = 154          # thread z right end of thread left start
thZ1             = 155          # thread z right start left end
thZRetract       = 156          # thread z retract

# taper config

tpAddFeed        = 157          # tp 
tpAngle          = 158          # tp 
tpAngleBtn       = 159          # tp 
tpDeltaBtn       = 160          # tp 
tpInternal       = 161          # tp 
tpLargeDiam      = 162          # tp 
tpPasses         = 163          # tp 
tpPause          = 164          # tp 
tpRPM            = 165          # tp 
tpSPInt          = 166          # tp 
tpSmallDiam      = 167          # tp 
tpSpring         = 168          # tp 
tpTaperSel       = 169          # tp 
tpXDelta         = 170          # tp 
tpXFeed          = 171          # tp 
tpXFinish        = 172          # tp 
tpXInFeed        = 173          # tp 
tpXRetract       = 174          # tp 
tpZDelta         = 175          # tp 
tpZFeed          = 176          # tp 
tpZLength        = 177          # tp 
tpZRetract       = 178          # tp 
tpZStart         = 179          # tp 

# turn config

tuAddFeed        = 180          # turn 
tuInternal       = 181          # turn internal
tuManual         = 182          # turn manual mode
tuPasses         = 183          # turn 
tuPause          = 184          # turn 
tuRPM            = 185          # turn 
tuSPInt          = 186          # turn 
tuSpring         = 187          # turn 
tuXDiam0         = 188          # turn 
tuXDiam1         = 189          # turn 
tuXFeed          = 190          # turn 
tuXRetract       = 191          # turn 
tuZEnd           = 192          # turn 
tuZFeed          = 193          # turn 
tuZRetract       = 194          # turn 
tuZStart         = 195          # turn 

# x axis config

xAccel           = 196          # x axis 
xBackInc         = 197          # z axis distance to go past for taking out backlash
xBacklash        = 198          # x axis 
xDoneDelay       = 199          # x axis done to read dro delay
xDroFinalDist    = 200          # x dro final approach dist
xDROInch         = 201          # x axis 
xDROPos          = 202          # x axis use dro to go to correct position
xHomeDir         = 203          # x axis 
xHomeDist        = 204          # x axis 
xHomeDistBackoff = 205          # x axis 
xHomeDistRev     = 206          # x axis 
xHomeEna         = 207          # x axis 
xHomeEnd         = 208          # x axis 
xHomeInv         = 209          # x axis 
xHomeLoc         = 210          # x axis 
xHomeSpeed       = 211          # x axis 
xHomeStart       = 212          # x axis 
xInvDRO          = 213          # x axis invert dro
xInvDir          = 214          # x axis invert stepper direction
xInvEnc          = 215          # x axis 
xInvMpg          = 216          # x axis invert mpg direction
xJogMax          = 217          # x axis 
xJogMin          = 218          # x axis 
xLimEna          = 219          # x axis limits enable
xLimNegInv       = 220          # x axis negative limit invert
xLimPosInv       = 221          # x axis positive limit invert
xMpgInc          = 222          # x axis jog increment
xMpgMax          = 223          # x axis jog maximum
xJogSpeed        = 224          # x axis 
xMaxSpeed        = 225          # x axis 
xMicroSteps      = 226          # x axis 
xMinSpeed        = 227          # x axis 
xMotorRatio      = 228          # x axis 
xMotorSteps      = 229          # x axis 
xRetractLoc      = 230          # x axis 
xPitch           = 231          # x axis 
xProbeDist       = 232          # x axis 

# x axis position config

xSvPosition      = 233          # x axis 
xSvHomeOffset    = 234          # x axis 
xSvDROPosition   = 235          # x axis 
xSvDROOffset     = 236          # x axis 

# z axis config

zAccel           = 237          # z axis 
zBackInc         = 238          # z axis distance to go past for taking out backlash
zBacklash        = 239          # z axis 
zDoneDelay       = 240          # z axis done to read dro delay
zDroFinalDist    = 241          # z dro final approach dist
zDROPos          = 242          # z axis use dro to go to correct position
zDROInch         = 243          # z axis 
zHomeDir         = 244          # z axis 
zHomeDist        = 245          # z axis 
zHomeDistRev     = 246          # z axis 
zHomeDistBackoff = 247          # z axis 
zHomeEna         = 248          # z axis 
zHomeEnd         = 249          # z axis 
zHomeInv         = 250          # z axis 
zHomeLoc         = 251          # z axis 
zHomeSpeed       = 252          # z axis 
zHomeStart       = 253          # z axis 
zInvDRO          = 254          # z axis 
zInvDir          = 255          # z axis 
zInvEnc          = 256          # z axis 
zInvMpg          = 257          # z axis 
zJogMax          = 258          # z axis 
zJogMin          = 259          # z axis 
zMpgInc          = 260          # z axis jog increment
zMpgMax          = 261          # z axis jog maximum
zJogSpeed        = 262          # z axis 
zLimEna          = 263          # z axis limits enable
zLimNegInv       = 264          # z axis negative limit invert
zLimPosInv       = 265          # z axis positive limit invert
zMaxSpeed        = 266          # z axis 
zMicroSteps      = 267          # z axis 
zMinSpeed        = 268          # z axis 
zMotorRatio      = 269          # z axis 
zMotorSteps      = 270          # z axis 
zRetractLoc      = 271          # z axis 
zPitch           = 272          # z axis 
zProbeDist       = 273          # z axis 
zProbeSpeed      = 274          # z axis 

# z axis position config

zSvPosition      = 275          # z axis 
zSvHomeOffset    = 276          # z axis 
zSvDROPosition   = 277          # z axis 
zSvDROOffset     = 278          # z axis 
cfgJogDebug      = 279          # debug jogging

config = { \
    'arcAddFeed' : 0,
    'arcBallDist' : 1,
    'arcCCW' : 2,
    'arcDiam' : 3,
    'arcFeed' : 4,
    'arcFinish' : 5,
    'arcLargeEnd' : 6,
    'arcLargeStem' : 7,
    'arcPasses' : 8,
    'arcPause' : 9,
    'arcRetract' : 10,
    'arcRadius' : 11,
    'arcRPM' : 12,
    'arcSmallEnd' : 13,
    'arcSmallStem' : 14,
    'arcSPInt' : 15,
    'arcSpring' : 16,
    'arcToolAngle' : 17,
    'arcToolRad' : 18,
    'arcType' : 19,
    'arcXFeed' : 20,
    'arcZFeed' : 21,
    'arcZStart' : 22,
    'cfgCmdDis' : 23,
    'cfgCommonLimits' : 24,
    'cfgLimitsEnabled' : 25,
    'cfgCommonHome' : 26,
    'cfgDbgSave' : 27,
    'cfgDRO' : 28,
    'cfgDraw' : 29,
    'cfgEncoder' : 30,
    'cfgEStop' : 31,
    'cfgEStopInv' : 32,
    'cfgExtDro' : 33,
    'cfgFcy' : 34,
    'cfgFreqMult' : 35,
    'cfgHomeInPlace' : 36,
    'cfgInvEncDir' : 37,
    'cfgLCD' : 38,
    'cfgMPG' : 39,
    'cfgPrbInv' : 40,
    'cfgRemDbg' : 41,
    'cfgSpEncCap' : 42,
    'cfgSpEncoder' : 43,
    'cfgSpSync' : 44,
    'cfgSpSyncBoard' : 45,
    'cfgSpUseEncoder' : 46,
    'cfgTaperCycleDist' : 47,
    'cfgTestMode' : 48,
    'cfgTestRPM' : 49,
    'cfgTurnSync' : 50,
    'cfgThreadSync' : 51,
    'cfgFpgaFreq' : 52,
    'cfgFpga' : 53,
    'commPort' : 54,
    'commRate' : 55,
    'cuPause' : 56,
    'cuRPM' : 57,
    'cuToolWidth' : 58,
    'cuXEnd' : 59,
    'cuXFeed' : 60,
    'cuXRetract' : 61,
    'cuXStart' : 62,
    'cuZCutoff' : 63,
    'cuZRetract' : 64,
    'cuZStart' : 65,
    'droXPos' : 66,
    'droZPos' : 67,
    'extDroPort' : 68,
    'extDroRate' : 69,
    'faAddFeed' : 70,
    'faPasses' : 71,
    'faPause' : 72,
    'faRPM' : 73,
    'faSPInt' : 74,
    'faSpring' : 75,
    'faXEnd' : 76,
    'faXFeed' : 77,
    'faXRetract' : 78,
    'faXStart' : 79,
    'faZEnd' : 80,
    'faZFeed' : 81,
    'faZRetract' : 82,
    'faZStart' : 83,
    'jogInc' : 84,
    'jogXPos' : 85,
    'jogXPosDiam' : 86,
    'jogZPos' : 87,
    'jpSurfaceSpeed' : 88,
    'jpXDroDiam' : 89,
    'jogTimeInitial' : 90,
    'jogTimeInc' : 91,
    'jogTimeMax' : 92,
    'keypadPort' : 93,
    'keypadRate' : 94,
    'mainPanel' : 95,
    'spAccel' : 96,
    'spAccelTime' : 97,
    'spCurRange' : 98,
    'spInvDir' : 99,
    'spJogAccelTime' : 100,
    'spJogMax' : 101,
    'spJogMin' : 102,
    'spJTimeInc' : 103,
    'spJTimeInitial' : 104,
    'spJTimeMax' : 105,
    'spMaxRPM' : 106,
    'spMicroSteps' : 107,
    'spMinRPM' : 108,
    'spMotorSteps' : 109,
    'spMotorTest' : 110,
    'spPWMFreq' : 111,
    'spRangeMin1' : 112,
    'spRangeMin2' : 113,
    'spRangeMin3' : 114,
    'spRangeMin4' : 115,
    'spRangeMin5' : 116,
    'spRangeMin6' : 117,
    'spRangeMax1' : 118,
    'spRangeMax2' : 119,
    'spRangeMax3' : 120,
    'spRangeMax4' : 121,
    'spRangeMax5' : 122,
    'spRangeMax6' : 123,
    'spRanges' : 124,
    'spStepDrive' : 125,
    'spSwitch' : 126,
    'spTestEncoder' : 127,
    'spTestIndex' : 128,
    'spVarSpeed' : 129,
    'syncPort' : 130,
    'syncRate' : 131,
    'thAddFeed' : 132,
    'thAlternate' : 133,
    'thAngle' : 134,
    'thFirstFeed' : 135,
    'thFirstFeedBtn' : 136,
    'thInternal' : 137,
    'thLastFeed' : 138,
    'thLastFeedBtn' : 139,
    'thLeftHand' : 140,
    'thMM' : 141,
    'thPasses' : 142,
    'thPause' : 143,
    'thRPM' : 144,
    'thRunout' : 145,
    'thSPInt' : 146,
    'thSpring' : 147,
    'thTPI' : 148,
    'thThread' : 149,
    'thXDepth' : 150,
    'thXRetract' : 151,
    'thXStart' : 152,
    'thXTaper' : 153,
    'thZ0' : 154,
    'thZ1' : 155,
    'thZRetract' : 156,
    'tpAddFeed' : 157,
    'tpAngle' : 158,
    'tpAngleBtn' : 159,
    'tpDeltaBtn' : 160,
    'tpInternal' : 161,
    'tpLargeDiam' : 162,
    'tpPasses' : 163,
    'tpPause' : 164,
    'tpRPM' : 165,
    'tpSPInt' : 166,
    'tpSmallDiam' : 167,
    'tpSpring' : 168,
    'tpTaperSel' : 169,
    'tpXDelta' : 170,
    'tpXFeed' : 171,
    'tpXFinish' : 172,
    'tpXInFeed' : 173,
    'tpXRetract' : 174,
    'tpZDelta' : 175,
    'tpZFeed' : 176,
    'tpZLength' : 177,
    'tpZRetract' : 178,
    'tpZStart' : 179,
    'tuAddFeed' : 180,
    'tuInternal' : 181,
    'tuManual' : 182,
    'tuPasses' : 183,
    'tuPause' : 184,
    'tuRPM' : 185,
    'tuSPInt' : 186,
    'tuSpring' : 187,
    'tuXDiam0' : 188,
    'tuXDiam1' : 189,
    'tuXFeed' : 190,
    'tuXRetract' : 191,
    'tuZEnd' : 192,
    'tuZFeed' : 193,
    'tuZRetract' : 194,
    'tuZStart' : 195,
    'xAccel' : 196,
    'xBackInc' : 197,
    'xBacklash' : 198,
    'xDoneDelay' : 199,
    'xDroFinalDist' : 200,
    'xDROInch' : 201,
    'xDROPos' : 202,
    'xHomeDir' : 203,
    'xHomeDist' : 204,
    'xHomeDistBackoff' : 205,
    'xHomeDistRev' : 206,
    'xHomeEna' : 207,
    'xHomeEnd' : 208,
    'xHomeInv' : 209,
    'xHomeLoc' : 210,
    'xHomeSpeed' : 211,
    'xHomeStart' : 212,
    'xInvDRO' : 213,
    'xInvDir' : 214,
    'xInvEnc' : 215,
    'xInvMpg' : 216,
    'xJogMax' : 217,
    'xJogMin' : 218,
    'xLimEna' : 219,
    'xLimNegInv' : 220,
    'xLimPosInv' : 221,
    'xMpgInc' : 222,
    'xMpgMax' : 223,
    'xJogSpeed' : 224,
    'xMaxSpeed' : 225,
    'xMicroSteps' : 226,
    'xMinSpeed' : 227,
    'xMotorRatio' : 228,
    'xMotorSteps' : 229,
    'xRetractLoc' : 230,
    'xPitch' : 231,
    'xProbeDist' : 232,
    'xSvPosition' : 233,
    'xSvHomeOffset' : 234,
    'xSvDROPosition' : 235,
    'xSvDROOffset' : 236,
    'zAccel' : 237,
    'zBackInc' : 238,
    'zBacklash' : 239,
    'zDoneDelay' : 240,
    'zDroFinalDist' : 241,
    'zDROPos' : 242,
    'zDROInch' : 243,
    'zHomeDir' : 244,
    'zHomeDist' : 245,
    'zHomeDistRev' : 246,
    'zHomeDistBackoff' : 247,
    'zHomeEna' : 248,
    'zHomeEnd' : 249,
    'zHomeInv' : 250,
    'zHomeLoc' : 251,
    'zHomeSpeed' : 252,
    'zHomeStart' : 253,
    'zInvDRO' : 254,
    'zInvDir' : 255,
    'zInvEnc' : 256,
    'zInvMpg' : 257,
    'zJogMax' : 258,
    'zJogMin' : 259,
    'zMpgInc' : 260,
    'zMpgMax' : 261,
    'zJogSpeed' : 262,
    'zLimEna' : 263,
    'zLimNegInv' : 264,
    'zLimPosInv' : 265,
    'zMaxSpeed' : 266,
    'zMicroSteps' : 267,
    'zMinSpeed' : 268,
    'zMotorRatio' : 269,
    'zMotorSteps' : 270,
    'zRetractLoc' : 271,
    'zPitch' : 272,
    'zProbeDist' : 273,
    'zProbeSpeed' : 274,
    'zSvPosition' : 275,
    'zSvHomeOffset' : 276,
    'zSvDROPosition' : 277,
    'zSvDROOffset' : 278,
    'cfgJogDebug' : 279,
    }

configTable = ( \
    'arcAddFeed',
    'arcBallDist',
    'arcCCW',
    'arcDiam',
    'arcFeed',
    'arcFinish',
    'arcLargeEnd',
    'arcLargeStem',
    'arcPasses',
    'arcPause',
    'arcRetract',
    'arcRadius',
    'arcRPM',
    'arcSmallEnd',
    'arcSmallStem',
    'arcSPInt',
    'arcSpring',
    'arcToolAngle',
    'arcToolRad',
    'arcType',
    'arcXFeed',
    'arcZFeed',
    'arcZStart',
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
    'tuManual',
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
    'xRetractLoc',
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
    'zRetractLoc',
    'zPitch',
    'zProbeDist',
    'zProbeSpeed',
    'zSvPosition',
    'zSvHomeOffset',
    'zSvDROPosition',
    'zSvDROOffset',
    'cfgJogDebug',
    )
