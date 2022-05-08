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

# mega config

cfgMegaVFD       =  98          # mega vfd speed mode
cfgMegaEncTest   =  99          # mega encoder test
cfgMegaEncLines  = 100          # mega encoder lines

# spindle config

spAccel          = 101          # spindle acceleration
spAccelTime      = 102          # spindle accelerationtime
spCurRange       = 103          # spindle current range
spInvDir         = 104          # spindle invert direction
spJogAccelTime   = 105          # spindle jog acceleration time
spJogMax         = 106          # spindle jog max speed
spJogMin         = 107          # spindle jog min speed
spJTimeInc       = 108          # spindle jog increment
spJTimeInitial   = 109          # spindle jog initial time 
spJTimeMax       = 110          # spindle jog max
spMaxRPM         = 111          # spindle jog max rpm
spMicroSteps     = 112          # spindle micro steps
spMinRPM         = 113          # spindle minimum rpm
spMotorSteps     = 114          # spindle motor stpes per revolution
spMotorTest      = 115          # use stepper drive to test motor
spPWMFreq        = 116          # spindle pwm frequency
spMegaSim        = 117          # spindle use mega to simulate index and encoder
spRangeMin1      = 118          # spindle speed range 1 minimum
spRangeMin2      = 119          # spindle speed range 2 minimum
spRangeMin3      = 120          # spindle speed range 3 minimum
spRangeMin4      = 121          # spindle speed range 4 minimum
spRangeMin5      = 122          # spindle speed range 5 minimum
spRangeMin6      = 123          # spindle speed range 6 minimum
spRangeMax1      = 124          # spindle speed range 1 maximum
spRangeMax2      = 125          # spindle speed range 2 maximum
spRangeMax3      = 126          # spindle speed range 3 maximum
spRangeMax4      = 127          # spindle speed range 4 maximum
spRangeMax5      = 128          # spindle speed range 5 maximum
spRangeMax6      = 129          # spindle speed range 6 maximum
spRanges         = 130          # spindle number of speed ranges
spStepDrive      = 131          # spindle stepper drive
spSwitch         = 132          # spindle off on switch
spTestEncoder    = 133          # spindle test generate encoder test pulse
spTestIndex      = 134          # spindle test generate internal index pulse
spVarSpeed       = 135          # spindle variable speed

# sync communications config

syncPort         = 136          # sync comm port
syncRate         = 137          # sync comm baud rate

# threading config

thAddFeed        = 138          # thread feed to add after done
thAlternate      = 139          # thread althernate thread flanks
thAngle          = 140          # thread hanlf angle of thread
thFirstFeed      = 141          # thread first feed for thread area calc
thFirstFeedBtn   = 142          # thread button to select first feed
thInternal       = 143          # thread internal threads
thLastFeed       = 144          # thread last feed for thread area calculation
thLastFeedBtn    = 145          # thread button to select last feed
thLeftHand       = 146          # thread left hand 
thMM             = 147          # thread button for mm
thPasses         = 148          # thread number of passes
thPause          = 149          # thread pause between passes
thRPM            = 150          # thread speed for threading operation
thRunout         = 151          # thread runout for rh exit or lh entrance
thSPInt          = 152          # thread spring pass interval
thSpring         = 153          # thread number of spring passes at end
thTPI            = 154          # thread select thread in threads per inch
thThread         = 155          # thread field containing tpi or pitch
thXDepth         = 156          # thread x depth of thread
thXRetract       = 157          # thread x retract
thXStart         = 158          # thread x diameter
thXTaper         = 159          # thread x taper
thZ0             = 160          # thread z right end of thread left start
thZ1             = 161          # thread z right start left end
thZRetract       = 162          # thread z retract

# taper config

tpAddFeed        = 163          # tp 
tpAngle          = 164          # tp 
tpAngleBtn       = 165          # tp 
tpDeltaBtn       = 166          # tp 
tpInternal       = 167          # tp 
tpLargeDiam      = 168          # tp 
tpPasses         = 169          # tp 
tpPause          = 170          # tp 
tpRPM            = 171          # tp 
tpSPInt          = 172          # tp 
tpSmallDiam      = 173          # tp 
tpSpring         = 174          # tp 
tpTaperSel       = 175          # tp 
tpXDelta         = 176          # tp 
tpXFeed          = 177          # tp 
tpXFinish        = 178          # tp 
tpXInFeed        = 179          # tp 
tpXRetract       = 180          # tp 
tpZDelta         = 181          # tp 
tpZFeed          = 182          # tp 
tpZLength        = 183          # tp 
tpZRetract       = 184          # tp 
tpZStart         = 185          # tp 

# turn config

tuAddFeed        = 186          # turn 
tuInternal       = 187          # turn internal
tuManual         = 188          # turn manual mode
tuPasses         = 189          # turn 
tuPause          = 190          # turn 
tuRPM            = 191          # turn 
tuSPInt          = 192          # turn 
tuSpring         = 193          # turn 
tuXDiam0         = 194          # turn 
tuXDiam1         = 195          # turn 
tuXFeed          = 196          # turn 
tuXRetract       = 197          # turn 
tuZEnd           = 198          # turn 
tuZFeed          = 199          # turn 
tuZRetract       = 200          # turn 
tuZStart         = 201          # turn 

# x axis config

xAccel           = 202          # x axis 
xBackInc         = 203          # z axis distance to go past for taking out backlash
xBacklash        = 204          # x axis 
xDoneDelay       = 205          # x axis done to read dro delay
xDroFinalDist    = 206          # x dro final approach dist
xDROInch         = 207          # x axis 
xDROPos          = 208          # x axis use dro to go to correct position
xHomeDir         = 209          # x axis 
xHomeDist        = 210          # x axis 
xHomeDistBackoff = 211          # x axis 
xHomeDistRev     = 212          # x axis 
xHomeEna         = 213          # x axis 
xHomeEnd         = 214          # x axis 
xHomeInv         = 215          # x axis 
xHomeLoc         = 216          # x axis 
xHomeSpeed       = 217          # x axis 
xHomeStart       = 218          # x axis 
xInvDRO          = 219          # x axis invert dro
xInvDir          = 220          # x axis invert stepper direction
xInvEnc          = 221          # x axis 
xInvMpg          = 222          # x axis invert mpg direction
xJogMax          = 223          # x axis 
xJogMin          = 224          # x axis 
xLimEna          = 225          # x axis limits enable
xLimNegInv       = 226          # x axis negative limit invert
xLimPosInv       = 227          # x axis positive limit invert
xMpgInc          = 228          # x axis jog increment
xMpgMax          = 229          # x axis jog maximum
xJogSpeed        = 230          # x axis 
xMaxSpeed        = 231          # x axis 
xMicroSteps      = 232          # x axis 
xMinSpeed        = 233          # x axis 
xMotorRatio      = 234          # x axis 
xMotorSteps      = 235          # x axis 
xRetractLoc      = 236          # x axis 
xPitch           = 237          # x axis 
xProbeDist       = 238          # x axis 

# x axis position config

xSvPosition      = 239          # x axis 
xSvHomeOffset    = 240          # x axis 
xSvDROPosition   = 241          # x axis 
xSvDROOffset     = 242          # x axis 

# z axis config

zAccel           = 243          # z axis 
zBackInc         = 244          # z axis distance to go past for taking out backlash
zBacklash        = 245          # z axis 
zDoneDelay       = 246          # z axis done to read dro delay
zDroFinalDist    = 247          # z dro final approach dist
zDROPos          = 248          # z axis use dro to go to correct position
zDROInch         = 249          # z axis 
zHomeDir         = 250          # z axis 
zHomeDist        = 251          # z axis 
zHomeDistRev     = 252          # z axis 
zHomeDistBackoff = 253          # z axis 
zHomeEna         = 254          # z axis 
zHomeEnd         = 255          # z axis 
zHomeInv         = 256          # z axis 
zHomeLoc         = 257          # z axis 
zHomeSpeed       = 258          # z axis 
zHomeStart       = 259          # z axis 
zInvDRO          = 260          # z axis 
zInvDir          = 261          # z axis 
zInvEnc          = 262          # z axis 
zInvMpg          = 263          # z axis 
zJogMax          = 264          # z axis 
zJogMin          = 265          # z axis 
zMpgInc          = 266          # z axis jog increment
zMpgMax          = 267          # z axis jog maximum
zJogSpeed        = 268          # z axis 
zLimEna          = 269          # z axis limits enable
zLimNegInv       = 270          # z axis negative limit invert
zLimPosInv       = 271          # z axis positive limit invert
zMaxSpeed        = 272          # z axis 
zMicroSteps      = 273          # z axis 
zMinSpeed        = 274          # z axis 
zMotorRatio      = 275          # z axis 
zMotorSteps      = 276          # z axis 
zRetractLoc      = 277          # z axis 
zPitch           = 278          # z axis 
zProbeDist       = 279          # z axis 
zProbeSpeed      = 280          # z axis 

# z axis position config

zSvPosition      = 281          # z axis 
zSvHomeOffset    = 282          # z axis 
zSvDROPosition   = 283          # z axis 
zSvDROOffset     = 284          # z axis 
cfgJogDebug      = 285          # debug jogging

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
    'cfgMegaVFD' : 98,
    'cfgMegaEncTest' : 99,
    'cfgMegaEncLines' : 100,
    'spAccel' : 101,
    'spAccelTime' : 102,
    'spCurRange' : 103,
    'spInvDir' : 104,
    'spJogAccelTime' : 105,
    'spJogMax' : 106,
    'spJogMin' : 107,
    'spJTimeInc' : 108,
    'spJTimeInitial' : 109,
    'spJTimeMax' : 110,
    'spMaxRPM' : 111,
    'spMicroSteps' : 112,
    'spMinRPM' : 113,
    'spMotorSteps' : 114,
    'spMotorTest' : 115,
    'spPWMFreq' : 116,
    'spMegaSim' : 117,
    'spRangeMin1' : 118,
    'spRangeMin2' : 119,
    'spRangeMin3' : 120,
    'spRangeMin4' : 121,
    'spRangeMin5' : 122,
    'spRangeMin6' : 123,
    'spRangeMax1' : 124,
    'spRangeMax2' : 125,
    'spRangeMax3' : 126,
    'spRangeMax4' : 127,
    'spRangeMax5' : 128,
    'spRangeMax6' : 129,
    'spRanges' : 130,
    'spStepDrive' : 131,
    'spSwitch' : 132,
    'spTestEncoder' : 133,
    'spTestIndex' : 134,
    'spVarSpeed' : 135,
    'syncPort' : 136,
    'syncRate' : 137,
    'thAddFeed' : 138,
    'thAlternate' : 139,
    'thAngle' : 140,
    'thFirstFeed' : 141,
    'thFirstFeedBtn' : 142,
    'thInternal' : 143,
    'thLastFeed' : 144,
    'thLastFeedBtn' : 145,
    'thLeftHand' : 146,
    'thMM' : 147,
    'thPasses' : 148,
    'thPause' : 149,
    'thRPM' : 150,
    'thRunout' : 151,
    'thSPInt' : 152,
    'thSpring' : 153,
    'thTPI' : 154,
    'thThread' : 155,
    'thXDepth' : 156,
    'thXRetract' : 157,
    'thXStart' : 158,
    'thXTaper' : 159,
    'thZ0' : 160,
    'thZ1' : 161,
    'thZRetract' : 162,
    'tpAddFeed' : 163,
    'tpAngle' : 164,
    'tpAngleBtn' : 165,
    'tpDeltaBtn' : 166,
    'tpInternal' : 167,
    'tpLargeDiam' : 168,
    'tpPasses' : 169,
    'tpPause' : 170,
    'tpRPM' : 171,
    'tpSPInt' : 172,
    'tpSmallDiam' : 173,
    'tpSpring' : 174,
    'tpTaperSel' : 175,
    'tpXDelta' : 176,
    'tpXFeed' : 177,
    'tpXFinish' : 178,
    'tpXInFeed' : 179,
    'tpXRetract' : 180,
    'tpZDelta' : 181,
    'tpZFeed' : 182,
    'tpZLength' : 183,
    'tpZRetract' : 184,
    'tpZStart' : 185,
    'tuAddFeed' : 186,
    'tuInternal' : 187,
    'tuManual' : 188,
    'tuPasses' : 189,
    'tuPause' : 190,
    'tuRPM' : 191,
    'tuSPInt' : 192,
    'tuSpring' : 193,
    'tuXDiam0' : 194,
    'tuXDiam1' : 195,
    'tuXFeed' : 196,
    'tuXRetract' : 197,
    'tuZEnd' : 198,
    'tuZFeed' : 199,
    'tuZRetract' : 200,
    'tuZStart' : 201,
    'xAccel' : 202,
    'xBackInc' : 203,
    'xBacklash' : 204,
    'xDoneDelay' : 205,
    'xDroFinalDist' : 206,
    'xDROInch' : 207,
    'xDROPos' : 208,
    'xHomeDir' : 209,
    'xHomeDist' : 210,
    'xHomeDistBackoff' : 211,
    'xHomeDistRev' : 212,
    'xHomeEna' : 213,
    'xHomeEnd' : 214,
    'xHomeInv' : 215,
    'xHomeLoc' : 216,
    'xHomeSpeed' : 217,
    'xHomeStart' : 218,
    'xInvDRO' : 219,
    'xInvDir' : 220,
    'xInvEnc' : 221,
    'xInvMpg' : 222,
    'xJogMax' : 223,
    'xJogMin' : 224,
    'xLimEna' : 225,
    'xLimNegInv' : 226,
    'xLimPosInv' : 227,
    'xMpgInc' : 228,
    'xMpgMax' : 229,
    'xJogSpeed' : 230,
    'xMaxSpeed' : 231,
    'xMicroSteps' : 232,
    'xMinSpeed' : 233,
    'xMotorRatio' : 234,
    'xMotorSteps' : 235,
    'xRetractLoc' : 236,
    'xPitch' : 237,
    'xProbeDist' : 238,
    'xSvPosition' : 239,
    'xSvHomeOffset' : 240,
    'xSvDROPosition' : 241,
    'xSvDROOffset' : 242,
    'zAccel' : 243,
    'zBackInc' : 244,
    'zBacklash' : 245,
    'zDoneDelay' : 246,
    'zDroFinalDist' : 247,
    'zDROPos' : 248,
    'zDROInch' : 249,
    'zHomeDir' : 250,
    'zHomeDist' : 251,
    'zHomeDistRev' : 252,
    'zHomeDistBackoff' : 253,
    'zHomeEna' : 254,
    'zHomeEnd' : 255,
    'zHomeInv' : 256,
    'zHomeLoc' : 257,
    'zHomeSpeed' : 258,
    'zHomeStart' : 259,
    'zInvDRO' : 260,
    'zInvDir' : 261,
    'zInvEnc' : 262,
    'zInvMpg' : 263,
    'zJogMax' : 264,
    'zJogMin' : 265,
    'zMpgInc' : 266,
    'zMpgMax' : 267,
    'zJogSpeed' : 268,
    'zLimEna' : 269,
    'zLimNegInv' : 270,
    'zLimPosInv' : 271,
    'zMaxSpeed' : 272,
    'zMicroSteps' : 273,
    'zMinSpeed' : 274,
    'zMotorRatio' : 275,
    'zMotorSteps' : 276,
    'zRetractLoc' : 277,
    'zPitch' : 278,
    'zProbeDist' : 279,
    'zProbeSpeed' : 280,
    'zSvPosition' : 281,
    'zSvHomeOffset' : 282,
    'zSvDROPosition' : 283,
    'zSvDROOffset' : 284,
    'cfgJogDebug' : 285,
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
    'cfgMegaVFD',
    'cfgMegaEncTest',
    'cfgMegaEncLines',
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
    'spMegaSim',
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
