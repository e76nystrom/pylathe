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
cfgMega          =  39          # config control link to mega
cfgMPG           =  40          # config enable manual pulse generator
cfgPrbInv        =  41          # config invert probe signal
cfgRemDbg        =  42          # config print remote debug info
cfgSpEncCap      =  43          # config encoder on capture interrupt
cfgSpEncoder     =  44          # config spindle encoder
cfgSpSync        =  45          # config spindle using timer
cfgSpSyncBoard   =  46          # config spindle sync board
cfgSpUseEncoder  =  47          # config use spindle encoder for threading
cfgTaperCycleDist =  48         # config taper cycle distance
cfgTestMode      =  49          # conifg test mode
cfgTestRPM       =  50          # config fpga test rpm value
cfgTurnSync      =  51          # config for turning synchronization
cfgThreadSync    =  52          # config for threading synchronization
cfgFpgaFreq      =  53          # config fpga frequency
cfgFpga          =  54          # config fpga interface present

# communications cxonfig

commPort         =  55          # comm port
commRate         =  56          # comm baud rate

# cutoff config

cuPause          =  57          # cutoff pause before cutting
cuRPM            =  58          # cutoff rpm
cuToolWidth      =  59          # cutoff tool width
cuXEnd           =  60          # cutoff x end
cuXFeed          =  61          # cutoff x feed
cuXRetract       =  62          # cutoff x retract
cuXStart         =  63          # cutoff x start
cuZCutoff        =  64          # cutoff offset to z cutoff
cuZRetract       =  65          # cutoff offset to z retract
cuZStart         =  66          # cutoff z location

# dro position

droXPos          =  67          # dro x position
droZPos          =  68          # dro z position

# external dro

extDroPort       =  69          # external dro port
extDroRate       =  70          # external dro baud Rate

# face config

faAddFeed        =  71          # face 
faPasses         =  72          # face 
faPause          =  73          # face pause before cutting
faRPM            =  74          # face 
faSPInt          =  75          # face 
faSpring         =  76          # face 
faXEnd           =  77          # face 
faXFeed          =  78          # face 
faXRetract       =  79          # face 
faXStart         =  80          # face 
faZEnd           =  81          # face 
faZFeed          =  82          # face 
faZRetract       =  83          # face 
faZStart         =  84          # face 

# jog config

jogInc           =  85          # jog 
jogXPos          =  86          # jog 
jogXPosDiam      =  87          # jog 
jogZPos          =  88          # jog 

# jog panel config

jpSurfaceSpeed   =  89          # jogpanle fpm or rpm
jpXDroDiam       =  90          # jogpanel x dro diameter

# jog time parameters

jogTimeInitial   =  91          # jog time initial
jogTimeInc       =  92          # jog time increment
jogTimeMax       =  93          # jog time max

# keypad

keypadPort       =  94          # external dro port
keypadRate       =  95          # external dro baud Rate

# main panel

mainPanel        =  96          # name of main panel

# spindle config

spAccel          =  97          # spindle acceleration
spAccelTime      =  98          # spindle accelerationtime
spCurRange       =  99          # spindle current range
spInvDir         = 100          # spindle invert direction
spJogAccelTime   = 101          # spindle jog acceleration time
spJogMax         = 102          # spindle jog max speed
spJogMin         = 103          # spindle jog min speed
spJTimeInc       = 104          # spindle jog increment
spJTimeInitial   = 105          # spindle jog initial time 
spJTimeMax       = 106          # spindle jog max
spMaxRPM         = 107          # spindle jog max rpm
spMicroSteps     = 108          # spindle micro steps
spMinRPM         = 109          # spindle minimum rpm
spMotorSteps     = 110          # spindle motor stpes per revolution
spMotorTest      = 111          # use stepper drive to test motor
spPWMFreq        = 112          # spindle pwm frequency
spRangeMin1      = 113          # spindle speed range 1 minimum
spRangeMin2      = 114          # spindle speed range 2 minimum
spRangeMin3      = 115          # spindle speed range 3 minimum
spRangeMin4      = 116          # spindle speed range 4 minimum
spRangeMin5      = 117          # spindle speed range 5 minimum
spRangeMin6      = 118          # spindle speed range 6 minimum
spRangeMax1      = 119          # spindle speed range 1 maximum
spRangeMax2      = 120          # spindle speed range 2 maximum
spRangeMax3      = 121          # spindle speed range 3 maximum
spRangeMax4      = 122          # spindle speed range 4 maximum
spRangeMax5      = 123          # spindle speed range 5 maximum
spRangeMax6      = 124          # spindle speed range 6 maximum
spRanges         = 125          # spindle number of speed ranges
spStepDrive      = 126          # spindle stepper drive
spSwitch         = 127          # spindle off on switch
spTestEncoder    = 128          # spindle test generate encoder test pulse
spTestIndex      = 129          # spindle test generate internal index pulse
spVarSpeed       = 130          # spindle variable speed

# sync communications config

syncPort         = 131          # sync comm port
syncRate         = 132          # sync comm baud rate

# threading config

thAddFeed        = 133          # thread feed to add after done
thAlternate      = 134          # thread althernate thread flanks
thAngle          = 135          # thread hanlf angle of thread
thFirstFeed      = 136          # thread first feed for thread area calc
thFirstFeedBtn   = 137          # thread button to select first feed
thInternal       = 138          # thread internal threads
thLastFeed       = 139          # thread last feed for thread area calculation
thLastFeedBtn    = 140          # thread button to select last feed
thLeftHand       = 141          # thread left hand 
thMM             = 142          # thread button for mm
thPasses         = 143          # thread number of passes
thPause          = 144          # thread pause between passes
thRPM            = 145          # thread speed for threading operation
thRunout         = 146          # thread runout for rh exit or lh entrance
thSPInt          = 147          # thread spring pass interval
thSpring         = 148          # thread number of spring passes at end
thTPI            = 149          # thread select thread in threads per inch
thThread         = 150          # thread field containing tpi or pitch
thXDepth         = 151          # thread x depth of thread
thXRetract       = 152          # thread x retract
thXStart         = 153          # thread x diameter
thXTaper         = 154          # thread x taper
thZ0             = 155          # thread z right end of thread left start
thZ1             = 156          # thread z right start left end
thZRetract       = 157          # thread z retract

# taper config

tpAddFeed        = 158          # tp 
tpAngle          = 159          # tp 
tpAngleBtn       = 160          # tp 
tpDeltaBtn       = 161          # tp 
tpInternal       = 162          # tp 
tpLargeDiam      = 163          # tp 
tpPasses         = 164          # tp 
tpPause          = 165          # tp 
tpRPM            = 166          # tp 
tpSPInt          = 167          # tp 
tpSmallDiam      = 168          # tp 
tpSpring         = 169          # tp 
tpTaperSel       = 170          # tp 
tpXDelta         = 171          # tp 
tpXFeed          = 172          # tp 
tpXFinish        = 173          # tp 
tpXInFeed        = 174          # tp 
tpXRetract       = 175          # tp 
tpZDelta         = 176          # tp 
tpZFeed          = 177          # tp 
tpZLength        = 178          # tp 
tpZRetract       = 179          # tp 
tpZStart         = 180          # tp 

# turn config

tuAddFeed        = 181          # turn 
tuInternal       = 182          # turn internal
tuManual         = 183          # turn manual mode
tuPasses         = 184          # turn 
tuPause          = 185          # turn 
tuRPM            = 186          # turn 
tuSPInt          = 187          # turn 
tuSpring         = 188          # turn 
tuXDiam0         = 189          # turn 
tuXDiam1         = 190          # turn 
tuXFeed          = 191          # turn 
tuXRetract       = 192          # turn 
tuZEnd           = 193          # turn 
tuZFeed          = 194          # turn 
tuZRetract       = 195          # turn 
tuZStart         = 196          # turn 

# x axis config

xAccel           = 197          # x axis 
xBackInc         = 198          # z axis distance to go past for taking out backlash
xBacklash        = 199          # x axis 
xDoneDelay       = 200          # x axis done to read dro delay
xDroFinalDist    = 201          # x dro final approach dist
xDROInch         = 202          # x axis 
xDROPos          = 203          # x axis use dro to go to correct position
xHomeDir         = 204          # x axis 
xHomeDist        = 205          # x axis 
xHomeDistBackoff = 206          # x axis 
xHomeDistRev     = 207          # x axis 
xHomeEna         = 208          # x axis 
xHomeEnd         = 209          # x axis 
xHomeInv         = 210          # x axis 
xHomeLoc         = 211          # x axis 
xHomeSpeed       = 212          # x axis 
xHomeStart       = 213          # x axis 
xInvDRO          = 214          # x axis invert dro
xInvDir          = 215          # x axis invert stepper direction
xInvEnc          = 216          # x axis 
xInvMpg          = 217          # x axis invert mpg direction
xJogMax          = 218          # x axis 
xJogMin          = 219          # x axis 
xLimEna          = 220          # x axis limits enable
xLimNegInv       = 221          # x axis negative limit invert
xLimPosInv       = 222          # x axis positive limit invert
xMpgInc          = 223          # x axis jog increment
xMpgMax          = 224          # x axis jog maximum
xJogSpeed        = 225          # x axis 
xMaxSpeed        = 226          # x axis 
xMicroSteps      = 227          # x axis 
xMinSpeed        = 228          # x axis 
xMotorRatio      = 229          # x axis 
xMotorSteps      = 230          # x axis 
xRetractLoc      = 231          # x axis 
xPitch           = 232          # x axis 
xProbeDist       = 233          # x axis 

# x axis position config

xSvPosition      = 234          # x axis 
xSvHomeOffset    = 235          # x axis 
xSvDROPosition   = 236          # x axis 
xSvDROOffset     = 237          # x axis 

# z axis config

zAccel           = 238          # z axis 
zBackInc         = 239          # z axis distance to go past for taking out backlash
zBacklash        = 240          # z axis 
zDoneDelay       = 241          # z axis done to read dro delay
zDroFinalDist    = 242          # z dro final approach dist
zDROPos          = 243          # z axis use dro to go to correct position
zDROInch         = 244          # z axis 
zHomeDir         = 245          # z axis 
zHomeDist        = 246          # z axis 
zHomeDistRev     = 247          # z axis 
zHomeDistBackoff = 248          # z axis 
zHomeEna         = 249          # z axis 
zHomeEnd         = 250          # z axis 
zHomeInv         = 251          # z axis 
zHomeLoc         = 252          # z axis 
zHomeSpeed       = 253          # z axis 
zHomeStart       = 254          # z axis 
zInvDRO          = 255          # z axis 
zInvDir          = 256          # z axis 
zInvEnc          = 257          # z axis 
zInvMpg          = 258          # z axis 
zJogMax          = 259          # z axis 
zJogMin          = 260          # z axis 
zMpgInc          = 261          # z axis jog increment
zMpgMax          = 262          # z axis jog maximum
zJogSpeed        = 263          # z axis 
zLimEna          = 264          # z axis limits enable
zLimNegInv       = 265          # z axis negative limit invert
zLimPosInv       = 266          # z axis positive limit invert
zMaxSpeed        = 267          # z axis 
zMicroSteps      = 268          # z axis 
zMinSpeed        = 269          # z axis 
zMotorRatio      = 270          # z axis 
zMotorSteps      = 271          # z axis 
zRetractLoc      = 272          # z axis 
zPitch           = 273          # z axis 
zProbeDist       = 274          # z axis 
zProbeSpeed      = 275          # z axis 

# z axis position config

zSvPosition      = 276          # z axis 
zSvHomeOffset    = 277          # z axis 
zSvDROPosition   = 278          # z axis 
zSvDROOffset     = 279          # z axis 
cfgJogDebug      = 280          # debug jogging

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
    'cfgMega' : 39,
    'cfgMPG' : 40,
    'cfgPrbInv' : 41,
    'cfgRemDbg' : 42,
    'cfgSpEncCap' : 43,
    'cfgSpEncoder' : 44,
    'cfgSpSync' : 45,
    'cfgSpSyncBoard' : 46,
    'cfgSpUseEncoder' : 47,
    'cfgTaperCycleDist' : 48,
    'cfgTestMode' : 49,
    'cfgTestRPM' : 50,
    'cfgTurnSync' : 51,
    'cfgThreadSync' : 52,
    'cfgFpgaFreq' : 53,
    'cfgFpga' : 54,
    'commPort' : 55,
    'commRate' : 56,
    'cuPause' : 57,
    'cuRPM' : 58,
    'cuToolWidth' : 59,
    'cuXEnd' : 60,
    'cuXFeed' : 61,
    'cuXRetract' : 62,
    'cuXStart' : 63,
    'cuZCutoff' : 64,
    'cuZRetract' : 65,
    'cuZStart' : 66,
    'droXPos' : 67,
    'droZPos' : 68,
    'extDroPort' : 69,
    'extDroRate' : 70,
    'faAddFeed' : 71,
    'faPasses' : 72,
    'faPause' : 73,
    'faRPM' : 74,
    'faSPInt' : 75,
    'faSpring' : 76,
    'faXEnd' : 77,
    'faXFeed' : 78,
    'faXRetract' : 79,
    'faXStart' : 80,
    'faZEnd' : 81,
    'faZFeed' : 82,
    'faZRetract' : 83,
    'faZStart' : 84,
    'jogInc' : 85,
    'jogXPos' : 86,
    'jogXPosDiam' : 87,
    'jogZPos' : 88,
    'jpSurfaceSpeed' : 89,
    'jpXDroDiam' : 90,
    'jogTimeInitial' : 91,
    'jogTimeInc' : 92,
    'jogTimeMax' : 93,
    'keypadPort' : 94,
    'keypadRate' : 95,
    'mainPanel' : 96,
    'spAccel' : 97,
    'spAccelTime' : 98,
    'spCurRange' : 99,
    'spInvDir' : 100,
    'spJogAccelTime' : 101,
    'spJogMax' : 102,
    'spJogMin' : 103,
    'spJTimeInc' : 104,
    'spJTimeInitial' : 105,
    'spJTimeMax' : 106,
    'spMaxRPM' : 107,
    'spMicroSteps' : 108,
    'spMinRPM' : 109,
    'spMotorSteps' : 110,
    'spMotorTest' : 111,
    'spPWMFreq' : 112,
    'spRangeMin1' : 113,
    'spRangeMin2' : 114,
    'spRangeMin3' : 115,
    'spRangeMin4' : 116,
    'spRangeMin5' : 117,
    'spRangeMin6' : 118,
    'spRangeMax1' : 119,
    'spRangeMax2' : 120,
    'spRangeMax3' : 121,
    'spRangeMax4' : 122,
    'spRangeMax5' : 123,
    'spRangeMax6' : 124,
    'spRanges' : 125,
    'spStepDrive' : 126,
    'spSwitch' : 127,
    'spTestEncoder' : 128,
    'spTestIndex' : 129,
    'spVarSpeed' : 130,
    'syncPort' : 131,
    'syncRate' : 132,
    'thAddFeed' : 133,
    'thAlternate' : 134,
    'thAngle' : 135,
    'thFirstFeed' : 136,
    'thFirstFeedBtn' : 137,
    'thInternal' : 138,
    'thLastFeed' : 139,
    'thLastFeedBtn' : 140,
    'thLeftHand' : 141,
    'thMM' : 142,
    'thPasses' : 143,
    'thPause' : 144,
    'thRPM' : 145,
    'thRunout' : 146,
    'thSPInt' : 147,
    'thSpring' : 148,
    'thTPI' : 149,
    'thThread' : 150,
    'thXDepth' : 151,
    'thXRetract' : 152,
    'thXStart' : 153,
    'thXTaper' : 154,
    'thZ0' : 155,
    'thZ1' : 156,
    'thZRetract' : 157,
    'tpAddFeed' : 158,
    'tpAngle' : 159,
    'tpAngleBtn' : 160,
    'tpDeltaBtn' : 161,
    'tpInternal' : 162,
    'tpLargeDiam' : 163,
    'tpPasses' : 164,
    'tpPause' : 165,
    'tpRPM' : 166,
    'tpSPInt' : 167,
    'tpSmallDiam' : 168,
    'tpSpring' : 169,
    'tpTaperSel' : 170,
    'tpXDelta' : 171,
    'tpXFeed' : 172,
    'tpXFinish' : 173,
    'tpXInFeed' : 174,
    'tpXRetract' : 175,
    'tpZDelta' : 176,
    'tpZFeed' : 177,
    'tpZLength' : 178,
    'tpZRetract' : 179,
    'tpZStart' : 180,
    'tuAddFeed' : 181,
    'tuInternal' : 182,
    'tuManual' : 183,
    'tuPasses' : 184,
    'tuPause' : 185,
    'tuRPM' : 186,
    'tuSPInt' : 187,
    'tuSpring' : 188,
    'tuXDiam0' : 189,
    'tuXDiam1' : 190,
    'tuXFeed' : 191,
    'tuXRetract' : 192,
    'tuZEnd' : 193,
    'tuZFeed' : 194,
    'tuZRetract' : 195,
    'tuZStart' : 196,
    'xAccel' : 197,
    'xBackInc' : 198,
    'xBacklash' : 199,
    'xDoneDelay' : 200,
    'xDroFinalDist' : 201,
    'xDROInch' : 202,
    'xDROPos' : 203,
    'xHomeDir' : 204,
    'xHomeDist' : 205,
    'xHomeDistBackoff' : 206,
    'xHomeDistRev' : 207,
    'xHomeEna' : 208,
    'xHomeEnd' : 209,
    'xHomeInv' : 210,
    'xHomeLoc' : 211,
    'xHomeSpeed' : 212,
    'xHomeStart' : 213,
    'xInvDRO' : 214,
    'xInvDir' : 215,
    'xInvEnc' : 216,
    'xInvMpg' : 217,
    'xJogMax' : 218,
    'xJogMin' : 219,
    'xLimEna' : 220,
    'xLimNegInv' : 221,
    'xLimPosInv' : 222,
    'xMpgInc' : 223,
    'xMpgMax' : 224,
    'xJogSpeed' : 225,
    'xMaxSpeed' : 226,
    'xMicroSteps' : 227,
    'xMinSpeed' : 228,
    'xMotorRatio' : 229,
    'xMotorSteps' : 230,
    'xRetractLoc' : 231,
    'xPitch' : 232,
    'xProbeDist' : 233,
    'xSvPosition' : 234,
    'xSvHomeOffset' : 235,
    'xSvDROPosition' : 236,
    'xSvDROOffset' : 237,
    'zAccel' : 238,
    'zBackInc' : 239,
    'zBacklash' : 240,
    'zDoneDelay' : 241,
    'zDroFinalDist' : 242,
    'zDROPos' : 243,
    'zDROInch' : 244,
    'zHomeDir' : 245,
    'zHomeDist' : 246,
    'zHomeDistRev' : 247,
    'zHomeDistBackoff' : 248,
    'zHomeEna' : 249,
    'zHomeEnd' : 250,
    'zHomeInv' : 251,
    'zHomeLoc' : 252,
    'zHomeSpeed' : 253,
    'zHomeStart' : 254,
    'zInvDRO' : 255,
    'zInvDir' : 256,
    'zInvEnc' : 257,
    'zInvMpg' : 258,
    'zJogMax' : 259,
    'zJogMin' : 260,
    'zMpgInc' : 261,
    'zMpgMax' : 262,
    'zJogSpeed' : 263,
    'zLimEna' : 264,
    'zLimNegInv' : 265,
    'zLimPosInv' : 266,
    'zMaxSpeed' : 267,
    'zMicroSteps' : 268,
    'zMinSpeed' : 269,
    'zMotorRatio' : 270,
    'zMotorSteps' : 271,
    'zRetractLoc' : 272,
    'zPitch' : 273,
    'zProbeDist' : 274,
    'zProbeSpeed' : 275,
    'zSvPosition' : 276,
    'zSvHomeOffset' : 277,
    'zSvDROPosition' : 278,
    'zSvDROOffset' : 279,
    'cfgJogDebug' : 280,
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
    'cfgMega',
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
