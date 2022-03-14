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
cfgFpga          =  35          # config fpga interface present
cfgFpgaFreq      =  36          # config fpga frequency
cfgFreqMult      =  37          # config fpga frequency multiplier
cfgHomeInPlace   =  38          # config home in place
cfgInvEncDir     =  39          # config fpga invert encoder direction
cfgLCD           =  40          # config enable lcd
cfgMega          =  41          # config control link to mega
cfgMPG           =  42          # config enable manual pulse generator
cfgPrbInv        =  43          # config invert probe signal
cfgRemDbg        =  44          # config print remote debug info
cfgSpEncCap      =  45          # config encoder on capture interrupt
cfgSpEncoder     =  46          # config spindle encoder
cfgSpSync        =  47          # config spindle using timer
cfgSpSyncBoard   =  48          # config spindle sync board
cfgSpUseEncoder  =  49          # config use spindle encoder for threading
cfgSyncSPI       =  50          # config sync comm through spi
cfgTaperCycleDist =  51         # config taper cycle distance
cfgTestMode      =  52          # conifg test mode
cfgTestRPM       =  53          # config fpga test rpm value
cfgTurnSync      =  54          # config for turning synchronization
cfgThreadSync    =  55          # config for threading synchronization

# communications cxonfig

commPort         =  56          # comm port
commRate         =  57          # comm baud rate

# cutoff config

cuPause          =  58          # cutoff pause before cutting
cuRPM            =  59          # cutoff rpm
cuToolWidth      =  60          # cutoff tool width
cuXEnd           =  61          # cutoff x end
cuXFeed          =  62          # cutoff x feed
cuXRetract       =  63          # cutoff x retract
cuXStart         =  64          # cutoff x start
cuZCutoff        =  65          # cutoff offset to z cutoff
cuZRetract       =  66          # cutoff offset to z retract
cuZStart         =  67          # cutoff z location

# dro position

droXPos          =  68          # dro x position
droZPos          =  69          # dro z position

# external dro

extDroPort       =  70          # external dro port
extDroRate       =  71          # external dro baud Rate

# face config

faAddFeed        =  72          # face 
faPasses         =  73          # face 
faPause          =  74          # face pause before cutting
faRPM            =  75          # face 
faSPInt          =  76          # face 
faSpring         =  77          # face 
faXEnd           =  78          # face 
faXFeed          =  79          # face 
faXRetract       =  80          # face 
faXStart         =  81          # face 
faZEnd           =  82          # face 
faZFeed          =  83          # face 
faZRetract       =  84          # face 
faZStart         =  85          # face 

# jog config

jogInc           =  86          # jog 
jogXPos          =  87          # jog 
jogXPosDiam      =  88          # jog 
jogZPos          =  89          # jog 

# jog panel config

jpSurfaceSpeed   =  90          # jogpanle fpm or rpm
jpXDroDiam       =  91          # jogpanel x dro diameter

# jog time parameters

jogTimeInitial   =  92          # jog time initial
jogTimeInc       =  93          # jog time increment
jogTimeMax       =  94          # jog time max

# keypad

keypadPort       =  95          # external dro port
keypadRate       =  96          # external dro baud Rate

# main panel

mainPanel        =  97          # name of main panel

# spindle config

spAccel          =  98          # spindle acceleration
spAccelTime      =  99          # spindle accelerationtime
spCurRange       = 100          # spindle current range
spInvDir         = 101          # spindle invert direction
spJogAccelTime   = 102          # spindle jog acceleration time
spJogMax         = 103          # spindle jog max speed
spJogMin         = 104          # spindle jog min speed
spJTimeInc       = 105          # spindle jog increment
spJTimeInitial   = 106          # spindle jog initial time 
spJTimeMax       = 107          # spindle jog max
spMaxRPM         = 108          # spindle jog max rpm
spMicroSteps     = 109          # spindle micro steps
spMinRPM         = 110          # spindle minimum rpm
spMotorSteps     = 111          # spindle motor stpes per revolution
spMotorTest      = 112          # use stepper drive to test motor
spPWMFreq        = 113          # spindle pwm frequency
spRangeMin1      = 114          # spindle speed range 1 minimum
spRangeMin2      = 115          # spindle speed range 2 minimum
spRangeMin3      = 116          # spindle speed range 3 minimum
spRangeMin4      = 117          # spindle speed range 4 minimum
spRangeMin5      = 118          # spindle speed range 5 minimum
spRangeMin6      = 119          # spindle speed range 6 minimum
spRangeMax1      = 120          # spindle speed range 1 maximum
spRangeMax2      = 121          # spindle speed range 2 maximum
spRangeMax3      = 122          # spindle speed range 3 maximum
spRangeMax4      = 123          # spindle speed range 4 maximum
spRangeMax5      = 124          # spindle speed range 5 maximum
spRangeMax6      = 125          # spindle speed range 6 maximum
spRanges         = 126          # spindle number of speed ranges
spStepDrive      = 127          # spindle stepper drive
spSwitch         = 128          # spindle off on switch
spTestEncoder    = 129          # spindle test generate encoder test pulse
spTestIndex      = 130          # spindle test generate internal index pulse
spVarSpeed       = 131          # spindle variable speed

# sync communications config

syncPort         = 132          # sync comm port
syncRate         = 133          # sync comm baud rate

# threading config

thAddFeed        = 134          # thread feed to add after done
thAlternate      = 135          # thread althernate thread flanks
thAngle          = 136          # thread hanlf angle of thread
thFirstFeed      = 137          # thread first feed for thread area calc
thFirstFeedBtn   = 138          # thread button to select first feed
thInternal       = 139          # thread internal threads
thLastFeed       = 140          # thread last feed for thread area calculation
thLastFeedBtn    = 141          # thread button to select last feed
thLeftHand       = 142          # thread left hand 
thMM             = 143          # thread button for mm
thPasses         = 144          # thread number of passes
thPause          = 145          # thread pause between passes
thRPM            = 146          # thread speed for threading operation
thRunout         = 147          # thread runout for rh exit or lh entrance
thSPInt          = 148          # thread spring pass interval
thSpring         = 149          # thread number of spring passes at end
thTPI            = 150          # thread select thread in threads per inch
thThread         = 151          # thread field containing tpi or pitch
thXDepth         = 152          # thread x depth of thread
thXRetract       = 153          # thread x retract
thXStart         = 154          # thread x diameter
thXTaper         = 155          # thread x taper
thZ0             = 156          # thread z right end of thread left start
thZ1             = 157          # thread z right start left end
thZRetract       = 158          # thread z retract

# taper config

tpAddFeed        = 159          # tp 
tpAngle          = 160          # tp 
tpAngleBtn       = 161          # tp 
tpDeltaBtn       = 162          # tp 
tpInternal       = 163          # tp 
tpLargeDiam      = 164          # tp 
tpPasses         = 165          # tp 
tpPause          = 166          # tp 
tpRPM            = 167          # tp 
tpSPInt          = 168          # tp 
tpSmallDiam      = 169          # tp 
tpSpring         = 170          # tp 
tpTaperSel       = 171          # tp 
tpXDelta         = 172          # tp 
tpXFeed          = 173          # tp 
tpXFinish        = 174          # tp 
tpXInFeed        = 175          # tp 
tpXRetract       = 176          # tp 
tpZDelta         = 177          # tp 
tpZFeed          = 178          # tp 
tpZLength        = 179          # tp 
tpZRetract       = 180          # tp 
tpZStart         = 181          # tp 

# turn config

tuAddFeed        = 182          # turn 
tuInternal       = 183          # turn internal
tuManual         = 184          # turn manual mode
tuPasses         = 185          # turn 
tuPause          = 186          # turn 
tuRPM            = 187          # turn 
tuSPInt          = 188          # turn 
tuSpring         = 189          # turn 
tuXDiam0         = 190          # turn 
tuXDiam1         = 191          # turn 
tuXFeed          = 192          # turn 
tuXRetract       = 193          # turn 
tuZEnd           = 194          # turn 
tuZFeed          = 195          # turn 
tuZRetract       = 196          # turn 
tuZStart         = 197          # turn 

# x axis config

xAccel           = 198          # x axis 
xBackInc         = 199          # z axis distance to go past for taking out backlash
xBacklash        = 200          # x axis 
xDoneDelay       = 201          # x axis done to read dro delay
xDroFinalDist    = 202          # x dro final approach dist
xDROInch         = 203          # x axis 
xDROPos          = 204          # x axis use dro to go to correct position
xHomeDir         = 205          # x axis 
xHomeDist        = 206          # x axis 
xHomeDistBackoff = 207          # x axis 
xHomeDistRev     = 208          # x axis 
xHomeEna         = 209          # x axis 
xHomeEnd         = 210          # x axis 
xHomeInv         = 211          # x axis 
xHomeLoc         = 212          # x axis 
xHomeSpeed       = 213          # x axis 
xHomeStart       = 214          # x axis 
xInvDRO          = 215          # x axis invert dro
xInvDir          = 216          # x axis invert stepper direction
xInvEnc          = 217          # x axis 
xInvMpg          = 218          # x axis invert mpg direction
xJogMax          = 219          # x axis 
xJogMin          = 220          # x axis 
xLimEna          = 221          # x axis limits enable
xLimNegInv       = 222          # x axis negative limit invert
xLimPosInv       = 223          # x axis positive limit invert
xMpgInc          = 224          # x axis jog increment
xMpgMax          = 225          # x axis jog maximum
xJogSpeed        = 226          # x axis 
xMaxSpeed        = 227          # x axis 
xMicroSteps      = 228          # x axis 
xMinSpeed        = 229          # x axis 
xMotorRatio      = 230          # x axis 
xMotorSteps      = 231          # x axis 
xRetractLoc      = 232          # x axis 
xPitch           = 233          # x axis 
xProbeDist       = 234          # x axis 

# x axis position config

xSvPosition      = 235          # x axis 
xSvHomeOffset    = 236          # x axis 
xSvDROPosition   = 237          # x axis 
xSvDROOffset     = 238          # x axis 

# z axis config

zAccel           = 239          # z axis 
zBackInc         = 240          # z axis distance to go past for taking out backlash
zBacklash        = 241          # z axis 
zDoneDelay       = 242          # z axis done to read dro delay
zDroFinalDist    = 243          # z dro final approach dist
zDROPos          = 244          # z axis use dro to go to correct position
zDROInch         = 245          # z axis 
zHomeDir         = 246          # z axis 
zHomeDist        = 247          # z axis 
zHomeDistRev     = 248          # z axis 
zHomeDistBackoff = 249          # z axis 
zHomeEna         = 250          # z axis 
zHomeEnd         = 251          # z axis 
zHomeInv         = 252          # z axis 
zHomeLoc         = 253          # z axis 
zHomeSpeed       = 254          # z axis 
zHomeStart       = 255          # z axis 
zInvDRO          = 256          # z axis 
zInvDir          = 257          # z axis 
zInvEnc          = 258          # z axis 
zInvMpg          = 259          # z axis 
zJogMax          = 260          # z axis 
zJogMin          = 261          # z axis 
zMpgInc          = 262          # z axis jog increment
zMpgMax          = 263          # z axis jog maximum
zJogSpeed        = 264          # z axis 
zLimEna          = 265          # z axis limits enable
zLimNegInv       = 266          # z axis negative limit invert
zLimPosInv       = 267          # z axis positive limit invert
zMaxSpeed        = 268          # z axis 
zMicroSteps      = 269          # z axis 
zMinSpeed        = 270          # z axis 
zMotorRatio      = 271          # z axis 
zMotorSteps      = 272          # z axis 
zRetractLoc      = 273          # z axis 
zPitch           = 274          # z axis 
zProbeDist       = 275          # z axis 
zProbeSpeed      = 276          # z axis 

# z axis position config

zSvPosition      = 277          # z axis 
zSvHomeOffset    = 278          # z axis 
zSvDROPosition   = 279          # z axis 
zSvDROOffset     = 280          # z axis 
cfgJogDebug      = 281          # debug jogging

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
    'cfgFpga' : 35,
    'cfgFpgaFreq' : 36,
    'cfgFreqMult' : 37,
    'cfgHomeInPlace' : 38,
    'cfgInvEncDir' : 39,
    'cfgLCD' : 40,
    'cfgMega' : 41,
    'cfgMPG' : 42,
    'cfgPrbInv' : 43,
    'cfgRemDbg' : 44,
    'cfgSpEncCap' : 45,
    'cfgSpEncoder' : 46,
    'cfgSpSync' : 47,
    'cfgSpSyncBoard' : 48,
    'cfgSpUseEncoder' : 49,
    'cfgSyncSPI' : 50,
    'cfgTaperCycleDist' : 51,
    'cfgTestMode' : 52,
    'cfgTestRPM' : 53,
    'cfgTurnSync' : 54,
    'cfgThreadSync' : 55,
    'commPort' : 56,
    'commRate' : 57,
    'cuPause' : 58,
    'cuRPM' : 59,
    'cuToolWidth' : 60,
    'cuXEnd' : 61,
    'cuXFeed' : 62,
    'cuXRetract' : 63,
    'cuXStart' : 64,
    'cuZCutoff' : 65,
    'cuZRetract' : 66,
    'cuZStart' : 67,
    'droXPos' : 68,
    'droZPos' : 69,
    'extDroPort' : 70,
    'extDroRate' : 71,
    'faAddFeed' : 72,
    'faPasses' : 73,
    'faPause' : 74,
    'faRPM' : 75,
    'faSPInt' : 76,
    'faSpring' : 77,
    'faXEnd' : 78,
    'faXFeed' : 79,
    'faXRetract' : 80,
    'faXStart' : 81,
    'faZEnd' : 82,
    'faZFeed' : 83,
    'faZRetract' : 84,
    'faZStart' : 85,
    'jogInc' : 86,
    'jogXPos' : 87,
    'jogXPosDiam' : 88,
    'jogZPos' : 89,
    'jpSurfaceSpeed' : 90,
    'jpXDroDiam' : 91,
    'jogTimeInitial' : 92,
    'jogTimeInc' : 93,
    'jogTimeMax' : 94,
    'keypadPort' : 95,
    'keypadRate' : 96,
    'mainPanel' : 97,
    'spAccel' : 98,
    'spAccelTime' : 99,
    'spCurRange' : 100,
    'spInvDir' : 101,
    'spJogAccelTime' : 102,
    'spJogMax' : 103,
    'spJogMin' : 104,
    'spJTimeInc' : 105,
    'spJTimeInitial' : 106,
    'spJTimeMax' : 107,
    'spMaxRPM' : 108,
    'spMicroSteps' : 109,
    'spMinRPM' : 110,
    'spMotorSteps' : 111,
    'spMotorTest' : 112,
    'spPWMFreq' : 113,
    'spRangeMin1' : 114,
    'spRangeMin2' : 115,
    'spRangeMin3' : 116,
    'spRangeMin4' : 117,
    'spRangeMin5' : 118,
    'spRangeMin6' : 119,
    'spRangeMax1' : 120,
    'spRangeMax2' : 121,
    'spRangeMax3' : 122,
    'spRangeMax4' : 123,
    'spRangeMax5' : 124,
    'spRangeMax6' : 125,
    'spRanges' : 126,
    'spStepDrive' : 127,
    'spSwitch' : 128,
    'spTestEncoder' : 129,
    'spTestIndex' : 130,
    'spVarSpeed' : 131,
    'syncPort' : 132,
    'syncRate' : 133,
    'thAddFeed' : 134,
    'thAlternate' : 135,
    'thAngle' : 136,
    'thFirstFeed' : 137,
    'thFirstFeedBtn' : 138,
    'thInternal' : 139,
    'thLastFeed' : 140,
    'thLastFeedBtn' : 141,
    'thLeftHand' : 142,
    'thMM' : 143,
    'thPasses' : 144,
    'thPause' : 145,
    'thRPM' : 146,
    'thRunout' : 147,
    'thSPInt' : 148,
    'thSpring' : 149,
    'thTPI' : 150,
    'thThread' : 151,
    'thXDepth' : 152,
    'thXRetract' : 153,
    'thXStart' : 154,
    'thXTaper' : 155,
    'thZ0' : 156,
    'thZ1' : 157,
    'thZRetract' : 158,
    'tpAddFeed' : 159,
    'tpAngle' : 160,
    'tpAngleBtn' : 161,
    'tpDeltaBtn' : 162,
    'tpInternal' : 163,
    'tpLargeDiam' : 164,
    'tpPasses' : 165,
    'tpPause' : 166,
    'tpRPM' : 167,
    'tpSPInt' : 168,
    'tpSmallDiam' : 169,
    'tpSpring' : 170,
    'tpTaperSel' : 171,
    'tpXDelta' : 172,
    'tpXFeed' : 173,
    'tpXFinish' : 174,
    'tpXInFeed' : 175,
    'tpXRetract' : 176,
    'tpZDelta' : 177,
    'tpZFeed' : 178,
    'tpZLength' : 179,
    'tpZRetract' : 180,
    'tpZStart' : 181,
    'tuAddFeed' : 182,
    'tuInternal' : 183,
    'tuManual' : 184,
    'tuPasses' : 185,
    'tuPause' : 186,
    'tuRPM' : 187,
    'tuSPInt' : 188,
    'tuSpring' : 189,
    'tuXDiam0' : 190,
    'tuXDiam1' : 191,
    'tuXFeed' : 192,
    'tuXRetract' : 193,
    'tuZEnd' : 194,
    'tuZFeed' : 195,
    'tuZRetract' : 196,
    'tuZStart' : 197,
    'xAccel' : 198,
    'xBackInc' : 199,
    'xBacklash' : 200,
    'xDoneDelay' : 201,
    'xDroFinalDist' : 202,
    'xDROInch' : 203,
    'xDROPos' : 204,
    'xHomeDir' : 205,
    'xHomeDist' : 206,
    'xHomeDistBackoff' : 207,
    'xHomeDistRev' : 208,
    'xHomeEna' : 209,
    'xHomeEnd' : 210,
    'xHomeInv' : 211,
    'xHomeLoc' : 212,
    'xHomeSpeed' : 213,
    'xHomeStart' : 214,
    'xInvDRO' : 215,
    'xInvDir' : 216,
    'xInvEnc' : 217,
    'xInvMpg' : 218,
    'xJogMax' : 219,
    'xJogMin' : 220,
    'xLimEna' : 221,
    'xLimNegInv' : 222,
    'xLimPosInv' : 223,
    'xMpgInc' : 224,
    'xMpgMax' : 225,
    'xJogSpeed' : 226,
    'xMaxSpeed' : 227,
    'xMicroSteps' : 228,
    'xMinSpeed' : 229,
    'xMotorRatio' : 230,
    'xMotorSteps' : 231,
    'xRetractLoc' : 232,
    'xPitch' : 233,
    'xProbeDist' : 234,
    'xSvPosition' : 235,
    'xSvHomeOffset' : 236,
    'xSvDROPosition' : 237,
    'xSvDROOffset' : 238,
    'zAccel' : 239,
    'zBackInc' : 240,
    'zBacklash' : 241,
    'zDoneDelay' : 242,
    'zDroFinalDist' : 243,
    'zDROPos' : 244,
    'zDROInch' : 245,
    'zHomeDir' : 246,
    'zHomeDist' : 247,
    'zHomeDistRev' : 248,
    'zHomeDistBackoff' : 249,
    'zHomeEna' : 250,
    'zHomeEnd' : 251,
    'zHomeInv' : 252,
    'zHomeLoc' : 253,
    'zHomeSpeed' : 254,
    'zHomeStart' : 255,
    'zInvDRO' : 256,
    'zInvDir' : 257,
    'zInvEnc' : 258,
    'zInvMpg' : 259,
    'zJogMax' : 260,
    'zJogMin' : 261,
    'zMpgInc' : 262,
    'zMpgMax' : 263,
    'zJogSpeed' : 264,
    'zLimEna' : 265,
    'zLimNegInv' : 266,
    'zLimPosInv' : 267,
    'zMaxSpeed' : 268,
    'zMicroSteps' : 269,
    'zMinSpeed' : 270,
    'zMotorRatio' : 271,
    'zMotorSteps' : 272,
    'zRetractLoc' : 273,
    'zPitch' : 274,
    'zProbeDist' : 275,
    'zProbeSpeed' : 276,
    'zSvPosition' : 277,
    'zSvHomeOffset' : 278,
    'zSvDROPosition' : 279,
    'zSvDROOffset' : 280,
    'cfgJogDebug' : 281,
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
    'cfgFpga',
    'cfgFpgaFreq',
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
    'cfgSyncSPI',
    'cfgTaperCycleDist',
    'cfgTestMode',
    'cfgTestRPM',
    'cfgTurnSync',
    'cfgThreadSync',
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
