# config table

# arc panel

arcAddFeed       =   0          # arc 
arcAEnd          =   1          # arc 
arcAStart        =   2          # arc 
arcCX            =   3          # arc 
arcCZ            =   4          # arc 
arcDiam          =   5          # arc 
arcFeed          =   6          # arc 
arcPasses        =   7          # arc 
arcPause         =   8          # arc 
arcRetract       =   9          # arc 
arcRadius        =  10          # arc 
arcRPM           =  11          # arc 
arcSPInt         =  12          # arc 
arcSpring        =  13          # arc 
arcStemDiam      =  14          # arc 
arcToolRad       =  15          # arc 
arcZFeed         =  16          # arc 

# system config

cfgCmdDis        =  17          # config disable sending commands
cfgCommonLimits  =  18          # config all limit switches on one pin
cfgLimitsEnabled =  19          # config limits enabled
cfgCommonHome    =  20          # config all switches on one pin
cfgDbgSave       =  21          # config save debug info
cfgDRO           =  22          # config dro present
cfgDraw          =  23          # config draw paths
cfgEncoder       =  24          # config encoder counts per revolution
cfgEStop         =  25          # config estop enable
cfgEStopInv      =  26          # config estop invert
cfgExtDro        =  27          # config external digital readout
cfgFcy           =  28          # config microprocesssor clock frequency
cfgFreqMult      =  29          # config fpga frequency multiplier
cfgHomeInPlace   =  30          # config home in place
cfgInvEncDir     =  31          # config fpga invert encoder direction
cfgLCD           =  32          # config enable lcd
cfgMPG           =  33          # config enable manual pulse generator
cfgPrbInv        =  34          # config invert probe signal
cfgRemDbg        =  35          # config print remote debug info
cfgSpEncCap      =  36          # config encoder on capture interrupt
cfgSpEncoder     =  37          # config spindle encoder
cfgSpSync        =  38          # config spindle using timer
cfgSpSyncBoard   =  39          # config spindle sync board
cfgSpUseEncoder  =  40          # config use spindle encoder for threading
cfgTaperCycleDist =  41         # config taper cycle distance
cfgTestMode      =  42          # conifg test mode
cfgTestRPM       =  43          # config fpga test rpm value
cfgTurnSync      =  44          # config for turning synchronization
cfgThreadSync    =  45          # config for threading synchronization
cfgFpgaFreq      =  46          # config fpga frequency
cfgFpga          =  47          # config fpga interface present

# communications config

commPort         =  48          # comm port
commRate         =  49          # comm baud rate

# cutoff config

cuPause          =  50          # cutoff pause before cutting
cuRPM            =  51          # cutoff rpm
cuToolWidth      =  52          # cutoff tool width
cuXEnd           =  53          # cutoff x end
cuXFeed          =  54          # cutoff x feed
cuXRetract       =  55          # cutoff x retract
cuXStart         =  56          # cutoff x start
cuZCutoff        =  57          # cutoff offset to z cutoff
cuZRetract       =  58          # cutoff offset to z retract
cuZStart         =  59          # cutoff z location

# dro position

droXPos          =  60          # dro x position
droZPos          =  61          # dro z position

# external dro

extDroPort       =  62          # external dro port
extDroRate       =  63          # external dro baud Rate

# face config

faAddFeed        =  64          # face 
faPasses         =  65          # face 
faPause          =  66          # face pause before cutting
faRPM            =  67          # face 
faSPInt          =  68          # face 
faSpring         =  69          # face 
faXEnd           =  70          # face 
faXFeed          =  71          # face 
faXRetract       =  72          # face 
faXStart         =  73          # face 
faZEnd           =  74          # face 
faZFeed          =  75          # face 
faZRetract       =  76          # face 
faZStart         =  77          # face 

# jog config

jogInc           =  78          # jog 
jogXPos          =  79          # jog 
jogXPosDiam      =  80          # jog 
jogZPos          =  81          # jog 

# jog panel config

jpSurfaceSpeed   =  82          # jogpanle fpm or rpm
jpXDroDiam       =  83          # jogpanel x dro diameter

# jog time parameters

jogTimeInitial   =  84          # jog time initial
jogTimeInc       =  85          # jog time increment
jogTimeMax       =  86          # jog time max

# keypad

keypadPort       =  87          # external dro port
keypadRate       =  88          # external dro baud Rate

# main panel

mainPanel        =  89          # name of main panel

# spindle config

spAccel          =  90          # spindle acceleration
spAccelTime      =  91          # spindle accelerationtime
spCurRange       =  92          # spindle current range
spInvDir         =  93          # spindle invert direction
spJogAccelTime   =  94          # spindle jog acceleration time
spJogMax         =  95          # spindle jog max speed
spJogMin         =  96          # spindle jog min speed
spJTimeInc       =  97          # spindle jog increment
spJTimeInitial   =  98          # spindle jog initial time 
spJTimeMax       =  99          # spindle jog max
spMaxRPM         = 100          # spindle jog max rpm
spMicroSteps     = 101          # spindle micro steps
spMinRPM         = 102          # spindle minimum rpm
spMotorSteps     = 103          # spindle motor stpes per revolution
spMotorTest      = 104          # use stepper drive to test motor
spPWMFreq        = 105          # spindle pwm frequency
spRangeMin1      = 106          # spindle speed range 1 minimum
spRangeMin2      = 107          # spindle speed range 2 minimum
spRangeMin3      = 108          # spindle speed range 3 minimum
spRangeMin4      = 109          # spindle speed range 4 minimum
spRangeMin5      = 110          # spindle speed range 5 minimum
spRangeMin6      = 111          # spindle speed range 6 minimum
spRangeMax1      = 112          # spindle speed range 1 maximum
spRangeMax2      = 113          # spindle speed range 2 maximum
spRangeMax3      = 114          # spindle speed range 3 maximum
spRangeMax4      = 115          # spindle speed range 4 maximum
spRangeMax5      = 116          # spindle speed range 5 maximum
spRangeMax6      = 117          # spindle speed range 6 maximum
spRanges         = 118          # spindle number of speed ranges
spStepDrive      = 119          # spindle stepper drive
spSwitch         = 120          # spindle off on switch
spTestEncoder    = 121          # spindle test generate encoder test pulse
spTestIndex      = 122          # spindle test generate internal index pulse
spVarSpeed       = 123          # spindle variable speed

# sync communications config

syncPort         = 124          # sync comm port
syncRate         = 125          # sync comm baud rate

# threading config

thAddFeed        = 126          # thread feed to add after done
thAlternate      = 127          # thread althernate thread flanks
thAngle          = 128          # thread hanlf angle of thread
thFirstFeed      = 129          # thread first feed for thread area calc
thFirstFeedBtn   = 130          # thread button to select first feed
thInternal       = 131          # thread internal threads
thLastFeed       = 132          # thread last feed for thread area calculation
thLastFeedBtn    = 133          # thread button to select last feed
thLeftHand       = 134          # thread left hand 
thMM             = 135          # thread button for mm
thPasses         = 136          # thread number of passes
thPause          = 137          # thread pause between passes
thRPM            = 138          # thread speed for threading operation
thRunout         = 139          # thread runout for rh exit or lh entrance
thSPInt          = 140          # thread spring pass interval
thSpring         = 141          # thread number of spring passes at end
thTPI            = 142          # thread select thread in threads per inch
thThread         = 143          # thread field containing tpi or pitch
thXDepth         = 144          # thread x depth of thread
thXRetract       = 145          # thread x retract
thXStart         = 146          # thread x diameter
thXTaper         = 147          # thread x taper
thZ0             = 148          # thread z right end of thread left start
thZ1             = 149          # thread z right start left end
thZRetract       = 150          # thread z retract

# taper config

tpAddFeed        = 151          # tp 
tpAngle          = 152          # tp 
tpAngleBtn       = 153          # tp 
tpDeltaBtn       = 154          # tp 
tpInternal       = 155          # tp 
tpLargeDiam      = 156          # tp 
tpPasses         = 157          # tp 
tpPause          = 158          # tp 
tpRPM            = 159          # tp 
tpSPInt          = 160          # tp 
tpSmallDiam      = 161          # tp 
tpSpring         = 162          # tp 
tpTaperSel       = 163          # tp 
tpXDelta         = 164          # tp 
tpXFeed          = 165          # tp 
tpXFinish        = 166          # tp 
tpXInFeed        = 167          # tp 
tpXRetract       = 168          # tp 
tpZDelta         = 169          # tp 
tpZFeed          = 170          # tp 
tpZLength        = 171          # tp 
tpZRetract       = 172          # tp 
tpZStart         = 173          # tp 

# turn config

tuAddFeed        = 174          # turn 
tuInternal       = 175          # turn internal
tuManual         = 176          # turn manual mode
tuPasses         = 177          # turn 
tuPause          = 178          # turn 
tuRPM            = 179          # turn 
tuSPInt          = 180          # turn 
tuSpring         = 181          # turn 
tuXDiam0         = 182          # turn 
tuXDiam1         = 183          # turn 
tuXFeed          = 184          # turn 
tuXRetract       = 185          # turn 
tuZEnd           = 186          # turn 
tuZFeed          = 187          # turn 
tuZRetract       = 188          # turn 
tuZStart         = 189          # turn 

# x axis config

xAccel           = 190          # x axis 
xBackInc         = 191          # z axis distance to go past for taking out backlash
xBacklash        = 192          # x axis 
xDoneDelay       = 193          # x axis done to read dro delay
xDroFinalDist    = 194          # x dro final approach dist
xDROInch         = 195          # x axis 
xDROPos          = 196          # x axis use dro to go to correct position
xHomeDir         = 197          # x axis 
xHomeDist        = 198          # x axis 
xHomeDistBackoff = 199          # x axis 
xHomeDistRev     = 200          # x axis 
xHomeEna         = 201          # x axis 
xHomeEnd         = 202          # x axis 
xHomeInv         = 203          # x axis 
xHomeLoc         = 204          # x axis 
xHomeSpeed       = 205          # x axis 
xHomeStart       = 206          # x axis 
xInvDRO          = 207          # x axis invert dro
xInvDir          = 208          # x axis invert stepper direction
xInvEnc          = 209          # x axis 
xInvMpg          = 210          # x axis invert mpg direction
xJogMax          = 211          # x axis 
xJogMin          = 212          # x axis 
xLimEna          = 213          # x axis limits enable
xLimNegInv       = 214          # x axis negative limit invert
xLimPosInv       = 215          # x axis positive limit invert
xMpgInc          = 216          # x axis jog increment
xMpgMax          = 217          # x axis jog maximum
xJogSpeed        = 218          # x axis 
xMaxSpeed        = 219          # x axis 
xMicroSteps      = 220          # x axis 
xMinSpeed        = 221          # x axis 
xMotorRatio      = 222          # x axis 
xMotorSteps      = 223          # x axis 
xParkLoc         = 224          # x axis 
xPitch           = 225          # x axis 
xProbeDist       = 226          # x axis 

# x axis position config

xSvPosition      = 227          # x axis 
xSvHomeOffset    = 228          # x axis 
xSvDROPosition   = 229          # x axis 
xSvDROOffset     = 230          # x axis 

# z axis config

zAccel           = 231          # z axis 
zBackInc         = 232          # z axis distance to go past for taking out backlash
zBacklash        = 233          # z axis 
zDoneDelay       = 234          # z axis done to read dro delay
zDroFinalDist    = 235          # z dro final approach dist
zDROPos          = 236          # z axis use dro to go to correct position
zDROInch         = 237          # z axis 
zHomeDir         = 238          # z axis 
zHomeDist        = 239          # z axis 
zHomeDistRev     = 240          # z axis 
zHomeDistBackoff = 241          # z axis 
zHomeEna         = 242          # z axis 
zHomeEnd         = 243          # z axis 
zHomeInv         = 244          # z axis 
zHomeLoc         = 245          # z axis 
zHomeSpeed       = 246          # z axis 
zHomeStart       = 247          # z axis 
zInvDRO          = 248          # z axis 
zInvDir          = 249          # z axis 
zInvEnc          = 250          # z axis 
zInvMpg          = 251          # z axis 
zJogMax          = 252          # z axis 
zJogMin          = 253          # z axis 
zMpgInc          = 254          # z axis jog increment
zMpgMax          = 255          # z axis jog maximum
zJogSpeed        = 256          # z axis 
zLimEna          = 257          # z axis limits enable
zLimNegInv       = 258          # z axis negative limit invert
zLimPosInv       = 259          # z axis positive limit invert
zMaxSpeed        = 260          # z axis 
zMicroSteps      = 261          # z axis 
zMinSpeed        = 262          # z axis 
zMotorRatio      = 263          # z axis 
zMotorSteps      = 264          # z axis 
zParkLoc         = 265          # z axis 
zPitch           = 266          # z axis 
zProbeDist       = 267          # z axis 
zProbeSpeed      = 268          # z axis 

# z axis position config

zSvPosition      = 269          # z axis 
zSvHomeOffset    = 270          # z axis 
zSvDROPosition   = 271          # z axis 
zSvDROOffset     = 272          # z axis 
cfgJogDebug      = 273          # debug jogging

config = { \
    'arcAddFeed' : 0,
    'arcAEnd' : 1,
    'arcAStart' : 2,
    'arcCX' : 3,
    'arcCZ' : 4,
    'arcDiam' : 5,
    'arcFeed' : 6,
    'arcPasses' : 7,
    'arcPause' : 8,
    'arcRetract' : 9,
    'arcRadius' : 10,
    'arcRPM' : 11,
    'arcSPInt' : 12,
    'arcSpring' : 13,
    'arcStemDiam' : 14,
    'arcToolRad' : 15,
    'arcZFeed' : 16,
    'cfgCmdDis' : 17,
    'cfgCommonLimits' : 18,
    'cfgLimitsEnabled' : 19,
    'cfgCommonHome' : 20,
    'cfgDbgSave' : 21,
    'cfgDRO' : 22,
    'cfgDraw' : 23,
    'cfgEncoder' : 24,
    'cfgEStop' : 25,
    'cfgEStopInv' : 26,
    'cfgExtDro' : 27,
    'cfgFcy' : 28,
    'cfgFreqMult' : 29,
    'cfgHomeInPlace' : 30,
    'cfgInvEncDir' : 31,
    'cfgLCD' : 32,
    'cfgMPG' : 33,
    'cfgPrbInv' : 34,
    'cfgRemDbg' : 35,
    'cfgSpEncCap' : 36,
    'cfgSpEncoder' : 37,
    'cfgSpSync' : 38,
    'cfgSpSyncBoard' : 39,
    'cfgSpUseEncoder' : 40,
    'cfgTaperCycleDist' : 41,
    'cfgTestMode' : 42,
    'cfgTestRPM' : 43,
    'cfgTurnSync' : 44,
    'cfgThreadSync' : 45,
    'cfgFpgaFreq' : 46,
    'cfgFpga' : 47,
    'commPort' : 48,
    'commRate' : 49,
    'cuPause' : 50,
    'cuRPM' : 51,
    'cuToolWidth' : 52,
    'cuXEnd' : 53,
    'cuXFeed' : 54,
    'cuXRetract' : 55,
    'cuXStart' : 56,
    'cuZCutoff' : 57,
    'cuZRetract' : 58,
    'cuZStart' : 59,
    'droXPos' : 60,
    'droZPos' : 61,
    'extDroPort' : 62,
    'extDroRate' : 63,
    'faAddFeed' : 64,
    'faPasses' : 65,
    'faPause' : 66,
    'faRPM' : 67,
    'faSPInt' : 68,
    'faSpring' : 69,
    'faXEnd' : 70,
    'faXFeed' : 71,
    'faXRetract' : 72,
    'faXStart' : 73,
    'faZEnd' : 74,
    'faZFeed' : 75,
    'faZRetract' : 76,
    'faZStart' : 77,
    'jogInc' : 78,
    'jogXPos' : 79,
    'jogXPosDiam' : 80,
    'jogZPos' : 81,
    'jpSurfaceSpeed' : 82,
    'jpXDroDiam' : 83,
    'jogTimeInitial' : 84,
    'jogTimeInc' : 85,
    'jogTimeMax' : 86,
    'keypadPort' : 87,
    'keypadRate' : 88,
    'mainPanel' : 89,
    'spAccel' : 90,
    'spAccelTime' : 91,
    'spCurRange' : 92,
    'spInvDir' : 93,
    'spJogAccelTime' : 94,
    'spJogMax' : 95,
    'spJogMin' : 96,
    'spJTimeInc' : 97,
    'spJTimeInitial' : 98,
    'spJTimeMax' : 99,
    'spMaxRPM' : 100,
    'spMicroSteps' : 101,
    'spMinRPM' : 102,
    'spMotorSteps' : 103,
    'spMotorTest' : 104,
    'spPWMFreq' : 105,
    'spRangeMin1' : 106,
    'spRangeMin2' : 107,
    'spRangeMin3' : 108,
    'spRangeMin4' : 109,
    'spRangeMin5' : 110,
    'spRangeMin6' : 111,
    'spRangeMax1' : 112,
    'spRangeMax2' : 113,
    'spRangeMax3' : 114,
    'spRangeMax4' : 115,
    'spRangeMax5' : 116,
    'spRangeMax6' : 117,
    'spRanges' : 118,
    'spStepDrive' : 119,
    'spSwitch' : 120,
    'spTestEncoder' : 121,
    'spTestIndex' : 122,
    'spVarSpeed' : 123,
    'syncPort' : 124,
    'syncRate' : 125,
    'thAddFeed' : 126,
    'thAlternate' : 127,
    'thAngle' : 128,
    'thFirstFeed' : 129,
    'thFirstFeedBtn' : 130,
    'thInternal' : 131,
    'thLastFeed' : 132,
    'thLastFeedBtn' : 133,
    'thLeftHand' : 134,
    'thMM' : 135,
    'thPasses' : 136,
    'thPause' : 137,
    'thRPM' : 138,
    'thRunout' : 139,
    'thSPInt' : 140,
    'thSpring' : 141,
    'thTPI' : 142,
    'thThread' : 143,
    'thXDepth' : 144,
    'thXRetract' : 145,
    'thXStart' : 146,
    'thXTaper' : 147,
    'thZ0' : 148,
    'thZ1' : 149,
    'thZRetract' : 150,
    'tpAddFeed' : 151,
    'tpAngle' : 152,
    'tpAngleBtn' : 153,
    'tpDeltaBtn' : 154,
    'tpInternal' : 155,
    'tpLargeDiam' : 156,
    'tpPasses' : 157,
    'tpPause' : 158,
    'tpRPM' : 159,
    'tpSPInt' : 160,
    'tpSmallDiam' : 161,
    'tpSpring' : 162,
    'tpTaperSel' : 163,
    'tpXDelta' : 164,
    'tpXFeed' : 165,
    'tpXFinish' : 166,
    'tpXInFeed' : 167,
    'tpXRetract' : 168,
    'tpZDelta' : 169,
    'tpZFeed' : 170,
    'tpZLength' : 171,
    'tpZRetract' : 172,
    'tpZStart' : 173,
    'tuAddFeed' : 174,
    'tuInternal' : 175,
    'tuManual' : 176,
    'tuPasses' : 177,
    'tuPause' : 178,
    'tuRPM' : 179,
    'tuSPInt' : 180,
    'tuSpring' : 181,
    'tuXDiam0' : 182,
    'tuXDiam1' : 183,
    'tuXFeed' : 184,
    'tuXRetract' : 185,
    'tuZEnd' : 186,
    'tuZFeed' : 187,
    'tuZRetract' : 188,
    'tuZStart' : 189,
    'xAccel' : 190,
    'xBackInc' : 191,
    'xBacklash' : 192,
    'xDoneDelay' : 193,
    'xDroFinalDist' : 194,
    'xDROInch' : 195,
    'xDROPos' : 196,
    'xHomeDir' : 197,
    'xHomeDist' : 198,
    'xHomeDistBackoff' : 199,
    'xHomeDistRev' : 200,
    'xHomeEna' : 201,
    'xHomeEnd' : 202,
    'xHomeInv' : 203,
    'xHomeLoc' : 204,
    'xHomeSpeed' : 205,
    'xHomeStart' : 206,
    'xInvDRO' : 207,
    'xInvDir' : 208,
    'xInvEnc' : 209,
    'xInvMpg' : 210,
    'xJogMax' : 211,
    'xJogMin' : 212,
    'xLimEna' : 213,
    'xLimNegInv' : 214,
    'xLimPosInv' : 215,
    'xMpgInc' : 216,
    'xMpgMax' : 217,
    'xJogSpeed' : 218,
    'xMaxSpeed' : 219,
    'xMicroSteps' : 220,
    'xMinSpeed' : 221,
    'xMotorRatio' : 222,
    'xMotorSteps' : 223,
    'xParkLoc' : 224,
    'xPitch' : 225,
    'xProbeDist' : 226,
    'xSvPosition' : 227,
    'xSvHomeOffset' : 228,
    'xSvDROPosition' : 229,
    'xSvDROOffset' : 230,
    'zAccel' : 231,
    'zBackInc' : 232,
    'zBacklash' : 233,
    'zDoneDelay' : 234,
    'zDroFinalDist' : 235,
    'zDROPos' : 236,
    'zDROInch' : 237,
    'zHomeDir' : 238,
    'zHomeDist' : 239,
    'zHomeDistRev' : 240,
    'zHomeDistBackoff' : 241,
    'zHomeEna' : 242,
    'zHomeEnd' : 243,
    'zHomeInv' : 244,
    'zHomeLoc' : 245,
    'zHomeSpeed' : 246,
    'zHomeStart' : 247,
    'zInvDRO' : 248,
    'zInvDir' : 249,
    'zInvEnc' : 250,
    'zInvMpg' : 251,
    'zJogMax' : 252,
    'zJogMin' : 253,
    'zMpgInc' : 254,
    'zMpgMax' : 255,
    'zJogSpeed' : 256,
    'zLimEna' : 257,
    'zLimNegInv' : 258,
    'zLimPosInv' : 259,
    'zMaxSpeed' : 260,
    'zMicroSteps' : 261,
    'zMinSpeed' : 262,
    'zMotorRatio' : 263,
    'zMotorSteps' : 264,
    'zParkLoc' : 265,
    'zPitch' : 266,
    'zProbeDist' : 267,
    'zProbeSpeed' : 268,
    'zSvPosition' : 269,
    'zSvHomeOffset' : 270,
    'zSvDROPosition' : 271,
    'zSvDROOffset' : 272,
    'cfgJogDebug' : 273,
    }

configTable = ( \
    'arcAddFeed',
    'arcAEnd',
    'arcAStart',
    'arcCX',
    'arcCZ',
    'arcDiam',
    'arcFeed',
    'arcPasses',
    'arcPause',
    'arcRetract',
    'arcRadius',
    'arcRPM',
    'arcSPInt',
    'arcSpring',
    'arcStemDiam',
    'arcToolRad',
    'arcZFeed',
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
