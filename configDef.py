# config table

# arc panel

arcAddFeed       =   0          # arc 
arcBallDist      =   1          # arc 
arcCCW           =   2          # arc 
arcDiam          =   3          # arc 
arcFeed          =   4          # arc 
arcLargeEnd      =   5          # arc 
arcLargeStem     =   6          # arc 
arcPasses        =   7          # arc 
arcPause         =   8          # arc 
arcRetract       =   9          # arc 
arcRadius        =  10          # arc 
arcRPM           =  11          # arc 
arcSmallEnd      =  12          # arc 
arcSmallStem     =  13          # arc 
arcSPInt         =  14          # arc 
arcSpring        =  15          # arc 
arcToolRad       =  16          # arc 
arcType          =  17          # arc 
arcZFeed         =  18          # arc 
arcZStart        =  19          # arc 

# system config

cfgCmdDis        =  20          # config disable sending commands
cfgCommonLimits  =  21          # config all limit switches on one pin
cfgLimitsEnabled =  22          # config limits enabled
cfgCommonHome    =  23          # config all switches on one pin
cfgDbgSave       =  24          # config save debug info
cfgDRO           =  25          # config dro present
cfgDraw          =  26          # config draw paths
cfgEncoder       =  27          # config encoder counts per revolution
cfgEStop         =  28          # config estop enable
cfgEStopInv      =  29          # config estop invert
cfgExtDro        =  30          # config external digital readout
cfgFcy           =  31          # config microprocesssor clock frequency
cfgFreqMult      =  32          # config fpga frequency multiplier
cfgHomeInPlace   =  33          # config home in place
cfgInvEncDir     =  34          # config fpga invert encoder direction
cfgLCD           =  35          # config enable lcd
cfgMPG           =  36          # config enable manual pulse generator
cfgPrbInv        =  37          # config invert probe signal
cfgRemDbg        =  38          # config print remote debug info
cfgSpEncCap      =  39          # config encoder on capture interrupt
cfgSpEncoder     =  40          # config spindle encoder
cfgSpSync        =  41          # config spindle using timer
cfgSpSyncBoard   =  42          # config spindle sync board
cfgSpUseEncoder  =  43          # config use spindle encoder for threading
cfgTaperCycleDist =  44         # config taper cycle distance
cfgTestMode      =  45          # conifg test mode
cfgTestRPM       =  46          # config fpga test rpm value
cfgTurnSync      =  47          # config for turning synchronization
cfgThreadSync    =  48          # config for threading synchronization
cfgFpgaFreq      =  49          # config fpga frequency
cfgFpga          =  50          # config fpga interface present

# communications cxonfig

commPort         =  51          # comm port
commRate         =  52          # comm baud rate

# cutoff config

cuPause          =  53          # cutoff pause before cutting
cuRPM            =  54          # cutoff rpm
cuToolWidth      =  55          # cutoff tool width
cuXEnd           =  56          # cutoff x end
cuXFeed          =  57          # cutoff x feed
cuXRetract       =  58          # cutoff x retract
cuXStart         =  59          # cutoff x start
cuZCutoff        =  60          # cutoff offset to z cutoff
cuZRetract       =  61          # cutoff offset to z retract
cuZStart         =  62          # cutoff z location

# dro position

droXPos          =  63          # dro x position
droZPos          =  64          # dro z position

# external dro

extDroPort       =  65          # external dro port
extDroRate       =  66          # external dro baud Rate

# face config

faAddFeed        =  67          # face 
faPasses         =  68          # face 
faPause          =  69          # face pause before cutting
faRPM            =  70          # face 
faSPInt          =  71          # face 
faSpring         =  72          # face 
faXEnd           =  73          # face 
faXFeed          =  74          # face 
faXRetract       =  75          # face 
faXStart         =  76          # face 
faZEnd           =  77          # face 
faZFeed          =  78          # face 
faZRetract       =  79          # face 
faZStart         =  80          # face 

# jog config

jogInc           =  81          # jog 
jogXPos          =  82          # jog 
jogXPosDiam      =  83          # jog 
jogZPos          =  84          # jog 

# jog panel config

jpSurfaceSpeed   =  85          # jogpanle fpm or rpm
jpXDroDiam       =  86          # jogpanel x dro diameter

# jog time parameters

jogTimeInitial   =  87          # jog time initial
jogTimeInc       =  88          # jog time increment
jogTimeMax       =  89          # jog time max

# keypad

keypadPort       =  90          # external dro port
keypadRate       =  91          # external dro baud Rate

# main panel

mainPanel        =  92          # name of main panel

# spindle config

spAccel          =  93          # spindle acceleration
spAccelTime      =  94          # spindle accelerationtime
spCurRange       =  95          # spindle current range
spInvDir         =  96          # spindle invert direction
spJogAccelTime   =  97          # spindle jog acceleration time
spJogMax         =  98          # spindle jog max speed
spJogMin         =  99          # spindle jog min speed
spJTimeInc       = 100          # spindle jog increment
spJTimeInitial   = 101          # spindle jog initial time 
spJTimeMax       = 102          # spindle jog max
spMaxRPM         = 103          # spindle jog max rpm
spMicroSteps     = 104          # spindle micro steps
spMinRPM         = 105          # spindle minimum rpm
spMotorSteps     = 106          # spindle motor stpes per revolution
spMotorTest      = 107          # use stepper drive to test motor
spPWMFreq        = 108          # spindle pwm frequency
spRangeMin1      = 109          # spindle speed range 1 minimum
spRangeMin2      = 110          # spindle speed range 2 minimum
spRangeMin3      = 111          # spindle speed range 3 minimum
spRangeMin4      = 112          # spindle speed range 4 minimum
spRangeMin5      = 113          # spindle speed range 5 minimum
spRangeMin6      = 114          # spindle speed range 6 minimum
spRangeMax1      = 115          # spindle speed range 1 maximum
spRangeMax2      = 116          # spindle speed range 2 maximum
spRangeMax3      = 117          # spindle speed range 3 maximum
spRangeMax4      = 118          # spindle speed range 4 maximum
spRangeMax5      = 119          # spindle speed range 5 maximum
spRangeMax6      = 120          # spindle speed range 6 maximum
spRanges         = 121          # spindle number of speed ranges
spStepDrive      = 122          # spindle stepper drive
spSwitch         = 123          # spindle off on switch
spTestEncoder    = 124          # spindle test generate encoder test pulse
spTestIndex      = 125          # spindle test generate internal index pulse
spVarSpeed       = 126          # spindle variable speed

# sync communications config

syncPort         = 127          # sync comm port
syncRate         = 128          # sync comm baud rate

# threading config

thAddFeed        = 129          # thread feed to add after done
thAlternate      = 130          # thread althernate thread flanks
thAngle          = 131          # thread hanlf angle of thread
thFirstFeed      = 132          # thread first feed for thread area calc
thFirstFeedBtn   = 133          # thread button to select first feed
thInternal       = 134          # thread internal threads
thLastFeed       = 135          # thread last feed for thread area calculation
thLastFeedBtn    = 136          # thread button to select last feed
thLeftHand       = 137          # thread left hand 
thMM             = 138          # thread button for mm
thPasses         = 139          # thread number of passes
thPause          = 140          # thread pause between passes
thRPM            = 141          # thread speed for threading operation
thRunout         = 142          # thread runout for rh exit or lh entrance
thSPInt          = 143          # thread spring pass interval
thSpring         = 144          # thread number of spring passes at end
thTPI            = 145          # thread select thread in threads per inch
thThread         = 146          # thread field containing tpi or pitch
thXDepth         = 147          # thread x depth of thread
thXRetract       = 148          # thread x retract
thXStart         = 149          # thread x diameter
thXTaper         = 150          # thread x taper
thZ0             = 151          # thread z right end of thread left start
thZ1             = 152          # thread z right start left end
thZRetract       = 153          # thread z retract

# taper config

tpAddFeed        = 154          # tp 
tpAngle          = 155          # tp 
tpAngleBtn       = 156          # tp 
tpDeltaBtn       = 157          # tp 
tpInternal       = 158          # tp 
tpLargeDiam      = 159          # tp 
tpPasses         = 160          # tp 
tpPause          = 161          # tp 
tpRPM            = 162          # tp 
tpSPInt          = 163          # tp 
tpSmallDiam      = 164          # tp 
tpSpring         = 165          # tp 
tpTaperSel       = 166          # tp 
tpXDelta         = 167          # tp 
tpXFeed          = 168          # tp 
tpXFinish        = 169          # tp 
tpXInFeed        = 170          # tp 
tpXRetract       = 171          # tp 
tpZDelta         = 172          # tp 
tpZFeed          = 173          # tp 
tpZLength        = 174          # tp 
tpZRetract       = 175          # tp 
tpZStart         = 176          # tp 

# turn config

tuAddFeed        = 177          # turn 
tuInternal       = 178          # turn internal
tuManual         = 179          # turn manual mode
tuPasses         = 180          # turn 
tuPause          = 181          # turn 
tuRPM            = 182          # turn 
tuSPInt          = 183          # turn 
tuSpring         = 184          # turn 
tuXDiam0         = 185          # turn 
tuXDiam1         = 186          # turn 
tuXFeed          = 187          # turn 
tuXRetract       = 188          # turn 
tuZEnd           = 189          # turn 
tuZFeed          = 190          # turn 
tuZRetract       = 191          # turn 
tuZStart         = 192          # turn 

# x axis config

xAccel           = 193          # x axis 
xBackInc         = 194          # z axis distance to go past for taking out backlash
xBacklash        = 195          # x axis 
xDoneDelay       = 196          # x axis done to read dro delay
xDroFinalDist    = 197          # x dro final approach dist
xDROInch         = 198          # x axis 
xDROPos          = 199          # x axis use dro to go to correct position
xHomeDir         = 200          # x axis 
xHomeDist        = 201          # x axis 
xHomeDistBackoff = 202          # x axis 
xHomeDistRev     = 203          # x axis 
xHomeEna         = 204          # x axis 
xHomeEnd         = 205          # x axis 
xHomeInv         = 206          # x axis 
xHomeLoc         = 207          # x axis 
xHomeSpeed       = 208          # x axis 
xHomeStart       = 209          # x axis 
xInvDRO          = 210          # x axis invert dro
xInvDir          = 211          # x axis invert stepper direction
xInvEnc          = 212          # x axis 
xInvMpg          = 213          # x axis invert mpg direction
xJogMax          = 214          # x axis 
xJogMin          = 215          # x axis 
xLimEna          = 216          # x axis limits enable
xLimNegInv       = 217          # x axis negative limit invert
xLimPosInv       = 218          # x axis positive limit invert
xMpgInc          = 219          # x axis jog increment
xMpgMax          = 220          # x axis jog maximum
xJogSpeed        = 221          # x axis 
xMaxSpeed        = 222          # x axis 
xMicroSteps      = 223          # x axis 
xMinSpeed        = 224          # x axis 
xMotorRatio      = 225          # x axis 
xMotorSteps      = 226          # x axis 
xParkLoc         = 227          # x axis 
xPitch           = 228          # x axis 
xProbeDist       = 229          # x axis 

# x axis position config

xSvPosition      = 230          # x axis 
xSvHomeOffset    = 231          # x axis 
xSvDROPosition   = 232          # x axis 
xSvDROOffset     = 233          # x axis 

# z axis config

zAccel           = 234          # z axis 
zBackInc         = 235          # z axis distance to go past for taking out backlash
zBacklash        = 236          # z axis 
zDoneDelay       = 237          # z axis done to read dro delay
zDroFinalDist    = 238          # z dro final approach dist
zDROPos          = 239          # z axis use dro to go to correct position
zDROInch         = 240          # z axis 
zHomeDir         = 241          # z axis 
zHomeDist        = 242          # z axis 
zHomeDistRev     = 243          # z axis 
zHomeDistBackoff = 244          # z axis 
zHomeEna         = 245          # z axis 
zHomeEnd         = 246          # z axis 
zHomeInv         = 247          # z axis 
zHomeLoc         = 248          # z axis 
zHomeSpeed       = 249          # z axis 
zHomeStart       = 250          # z axis 
zInvDRO          = 251          # z axis 
zInvDir          = 252          # z axis 
zInvEnc          = 253          # z axis 
zInvMpg          = 254          # z axis 
zJogMax          = 255          # z axis 
zJogMin          = 256          # z axis 
zMpgInc          = 257          # z axis jog increment
zMpgMax          = 258          # z axis jog maximum
zJogSpeed        = 259          # z axis 
zLimEna          = 260          # z axis limits enable
zLimNegInv       = 261          # z axis negative limit invert
zLimPosInv       = 262          # z axis positive limit invert
zMaxSpeed        = 263          # z axis 
zMicroSteps      = 264          # z axis 
zMinSpeed        = 265          # z axis 
zMotorRatio      = 266          # z axis 
zMotorSteps      = 267          # z axis 
zParkLoc         = 268          # z axis 
zPitch           = 269          # z axis 
zProbeDist       = 270          # z axis 
zProbeSpeed      = 271          # z axis 

# z axis position config

zSvPosition      = 272          # z axis 
zSvHomeOffset    = 273          # z axis 
zSvDROPosition   = 274          # z axis 
zSvDROOffset     = 275          # z axis 
cfgJogDebug      = 276          # debug jogging

config = { \
    'arcAddFeed' : 0,
    'arcBallDist' : 1,
    'arcCCW' : 2,
    'arcDiam' : 3,
    'arcFeed' : 4,
    'arcLargeEnd' : 5,
    'arcLargeStem' : 6,
    'arcPasses' : 7,
    'arcPause' : 8,
    'arcRetract' : 9,
    'arcRadius' : 10,
    'arcRPM' : 11,
    'arcSmallEnd' : 12,
    'arcSmallStem' : 13,
    'arcSPInt' : 14,
    'arcSpring' : 15,
    'arcToolRad' : 16,
    'arcType' : 17,
    'arcZFeed' : 18,
    'arcZStart' : 19,
    'cfgCmdDis' : 20,
    'cfgCommonLimits' : 21,
    'cfgLimitsEnabled' : 22,
    'cfgCommonHome' : 23,
    'cfgDbgSave' : 24,
    'cfgDRO' : 25,
    'cfgDraw' : 26,
    'cfgEncoder' : 27,
    'cfgEStop' : 28,
    'cfgEStopInv' : 29,
    'cfgExtDro' : 30,
    'cfgFcy' : 31,
    'cfgFreqMult' : 32,
    'cfgHomeInPlace' : 33,
    'cfgInvEncDir' : 34,
    'cfgLCD' : 35,
    'cfgMPG' : 36,
    'cfgPrbInv' : 37,
    'cfgRemDbg' : 38,
    'cfgSpEncCap' : 39,
    'cfgSpEncoder' : 40,
    'cfgSpSync' : 41,
    'cfgSpSyncBoard' : 42,
    'cfgSpUseEncoder' : 43,
    'cfgTaperCycleDist' : 44,
    'cfgTestMode' : 45,
    'cfgTestRPM' : 46,
    'cfgTurnSync' : 47,
    'cfgThreadSync' : 48,
    'cfgFpgaFreq' : 49,
    'cfgFpga' : 50,
    'commPort' : 51,
    'commRate' : 52,
    'cuPause' : 53,
    'cuRPM' : 54,
    'cuToolWidth' : 55,
    'cuXEnd' : 56,
    'cuXFeed' : 57,
    'cuXRetract' : 58,
    'cuXStart' : 59,
    'cuZCutoff' : 60,
    'cuZRetract' : 61,
    'cuZStart' : 62,
    'droXPos' : 63,
    'droZPos' : 64,
    'extDroPort' : 65,
    'extDroRate' : 66,
    'faAddFeed' : 67,
    'faPasses' : 68,
    'faPause' : 69,
    'faRPM' : 70,
    'faSPInt' : 71,
    'faSpring' : 72,
    'faXEnd' : 73,
    'faXFeed' : 74,
    'faXRetract' : 75,
    'faXStart' : 76,
    'faZEnd' : 77,
    'faZFeed' : 78,
    'faZRetract' : 79,
    'faZStart' : 80,
    'jogInc' : 81,
    'jogXPos' : 82,
    'jogXPosDiam' : 83,
    'jogZPos' : 84,
    'jpSurfaceSpeed' : 85,
    'jpXDroDiam' : 86,
    'jogTimeInitial' : 87,
    'jogTimeInc' : 88,
    'jogTimeMax' : 89,
    'keypadPort' : 90,
    'keypadRate' : 91,
    'mainPanel' : 92,
    'spAccel' : 93,
    'spAccelTime' : 94,
    'spCurRange' : 95,
    'spInvDir' : 96,
    'spJogAccelTime' : 97,
    'spJogMax' : 98,
    'spJogMin' : 99,
    'spJTimeInc' : 100,
    'spJTimeInitial' : 101,
    'spJTimeMax' : 102,
    'spMaxRPM' : 103,
    'spMicroSteps' : 104,
    'spMinRPM' : 105,
    'spMotorSteps' : 106,
    'spMotorTest' : 107,
    'spPWMFreq' : 108,
    'spRangeMin1' : 109,
    'spRangeMin2' : 110,
    'spRangeMin3' : 111,
    'spRangeMin4' : 112,
    'spRangeMin5' : 113,
    'spRangeMin6' : 114,
    'spRangeMax1' : 115,
    'spRangeMax2' : 116,
    'spRangeMax3' : 117,
    'spRangeMax4' : 118,
    'spRangeMax5' : 119,
    'spRangeMax6' : 120,
    'spRanges' : 121,
    'spStepDrive' : 122,
    'spSwitch' : 123,
    'spTestEncoder' : 124,
    'spTestIndex' : 125,
    'spVarSpeed' : 126,
    'syncPort' : 127,
    'syncRate' : 128,
    'thAddFeed' : 129,
    'thAlternate' : 130,
    'thAngle' : 131,
    'thFirstFeed' : 132,
    'thFirstFeedBtn' : 133,
    'thInternal' : 134,
    'thLastFeed' : 135,
    'thLastFeedBtn' : 136,
    'thLeftHand' : 137,
    'thMM' : 138,
    'thPasses' : 139,
    'thPause' : 140,
    'thRPM' : 141,
    'thRunout' : 142,
    'thSPInt' : 143,
    'thSpring' : 144,
    'thTPI' : 145,
    'thThread' : 146,
    'thXDepth' : 147,
    'thXRetract' : 148,
    'thXStart' : 149,
    'thXTaper' : 150,
    'thZ0' : 151,
    'thZ1' : 152,
    'thZRetract' : 153,
    'tpAddFeed' : 154,
    'tpAngle' : 155,
    'tpAngleBtn' : 156,
    'tpDeltaBtn' : 157,
    'tpInternal' : 158,
    'tpLargeDiam' : 159,
    'tpPasses' : 160,
    'tpPause' : 161,
    'tpRPM' : 162,
    'tpSPInt' : 163,
    'tpSmallDiam' : 164,
    'tpSpring' : 165,
    'tpTaperSel' : 166,
    'tpXDelta' : 167,
    'tpXFeed' : 168,
    'tpXFinish' : 169,
    'tpXInFeed' : 170,
    'tpXRetract' : 171,
    'tpZDelta' : 172,
    'tpZFeed' : 173,
    'tpZLength' : 174,
    'tpZRetract' : 175,
    'tpZStart' : 176,
    'tuAddFeed' : 177,
    'tuInternal' : 178,
    'tuManual' : 179,
    'tuPasses' : 180,
    'tuPause' : 181,
    'tuRPM' : 182,
    'tuSPInt' : 183,
    'tuSpring' : 184,
    'tuXDiam0' : 185,
    'tuXDiam1' : 186,
    'tuXFeed' : 187,
    'tuXRetract' : 188,
    'tuZEnd' : 189,
    'tuZFeed' : 190,
    'tuZRetract' : 191,
    'tuZStart' : 192,
    'xAccel' : 193,
    'xBackInc' : 194,
    'xBacklash' : 195,
    'xDoneDelay' : 196,
    'xDroFinalDist' : 197,
    'xDROInch' : 198,
    'xDROPos' : 199,
    'xHomeDir' : 200,
    'xHomeDist' : 201,
    'xHomeDistBackoff' : 202,
    'xHomeDistRev' : 203,
    'xHomeEna' : 204,
    'xHomeEnd' : 205,
    'xHomeInv' : 206,
    'xHomeLoc' : 207,
    'xHomeSpeed' : 208,
    'xHomeStart' : 209,
    'xInvDRO' : 210,
    'xInvDir' : 211,
    'xInvEnc' : 212,
    'xInvMpg' : 213,
    'xJogMax' : 214,
    'xJogMin' : 215,
    'xLimEna' : 216,
    'xLimNegInv' : 217,
    'xLimPosInv' : 218,
    'xMpgInc' : 219,
    'xMpgMax' : 220,
    'xJogSpeed' : 221,
    'xMaxSpeed' : 222,
    'xMicroSteps' : 223,
    'xMinSpeed' : 224,
    'xMotorRatio' : 225,
    'xMotorSteps' : 226,
    'xParkLoc' : 227,
    'xPitch' : 228,
    'xProbeDist' : 229,
    'xSvPosition' : 230,
    'xSvHomeOffset' : 231,
    'xSvDROPosition' : 232,
    'xSvDROOffset' : 233,
    'zAccel' : 234,
    'zBackInc' : 235,
    'zBacklash' : 236,
    'zDoneDelay' : 237,
    'zDroFinalDist' : 238,
    'zDROPos' : 239,
    'zDROInch' : 240,
    'zHomeDir' : 241,
    'zHomeDist' : 242,
    'zHomeDistRev' : 243,
    'zHomeDistBackoff' : 244,
    'zHomeEna' : 245,
    'zHomeEnd' : 246,
    'zHomeInv' : 247,
    'zHomeLoc' : 248,
    'zHomeSpeed' : 249,
    'zHomeStart' : 250,
    'zInvDRO' : 251,
    'zInvDir' : 252,
    'zInvEnc' : 253,
    'zInvMpg' : 254,
    'zJogMax' : 255,
    'zJogMin' : 256,
    'zMpgInc' : 257,
    'zMpgMax' : 258,
    'zJogSpeed' : 259,
    'zLimEna' : 260,
    'zLimNegInv' : 261,
    'zLimPosInv' : 262,
    'zMaxSpeed' : 263,
    'zMicroSteps' : 264,
    'zMinSpeed' : 265,
    'zMotorRatio' : 266,
    'zMotorSteps' : 267,
    'zParkLoc' : 268,
    'zPitch' : 269,
    'zProbeDist' : 270,
    'zProbeSpeed' : 271,
    'zSvPosition' : 272,
    'zSvHomeOffset' : 273,
    'zSvDROPosition' : 274,
    'zSvDROOffset' : 275,
    'cfgJogDebug' : 276,
    }

configTable = ( \
    'arcAddFeed',
    'arcBallDist',
    'arcCCW',
    'arcDiam',
    'arcFeed',
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
    'arcToolRad',
    'arcType',
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
