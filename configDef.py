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
cfgFcy           =  34          # config microprocessor clock frequency
cfgFpga          =  35          # config fpga interface present
cfgFpgaFreq      =  36          # config fpga frequency
cfgFreqMult      =  37          # config fpga frequency multiplier
cfgHomeInPlace   =  38          # config home in place
cfgIntSync       =  39          # config internal sync
cfgInvEncDir     =  40          # config fpga invert encoder direction
cfgLCD           =  41          # config enable lcd
cfgMega          =  42          # config control link to mega
cfgMPG           =  43          # config enable manual pulse generator
cfgPrbInv        =  44          # config invert probe signal
cfgRemDbg        =  45          # config print remote debug info
cfgSpEncCap      =  46          # config encoder on capture interrupt
cfgSpEncoder     =  47          # config spindle encoder
cfgSpSync        =  48          # config spindle using timer
cfgSpSyncBoard   =  49          # config spindle sync board
cfgSpUseEncoder  =  50          # config use spindle encoder for threading
cfgSyncSPI       =  51          # config sync comm through spi
cfgTaperCycleDist =  52         # config taper cycle distance
cfgTestMode      =  53          # conifg test mode
cfgTestRPM       =  54          # config fpga test rpm value
cfgTurnSync      =  55          # config for turning synchronization
cfgThreadSync    =  56          # config for threading synchronization

# communications cxonfig

commPort         =  57          # comm port
commRate         =  58          # comm baud rate

# cutoff config

cuPause          =  59          # cutoff pause before cutting
cuRPM            =  60          # cutoff rpm
cuToolWidth      =  61          # cutoff tool width
cuXEnd           =  62          # cutoff x end
cuXFeed          =  63          # cutoff x feed
cuXRetract       =  64          # cutoff x retract
cuXStart         =  65          # cutoff x start
cuZCutoff        =  66          # cutoff offset to z cutoff
cuZRetract       =  67          # cutoff offset to z retract
cuZStart         =  68          # cutoff z location

# dro position

droXPos          =  69          # dro x position
droZPos          =  70          # dro z position

# external dro

extDroPort       =  71          # external dro port
extDroRate       =  72          # external dro baud Rate

# face config

faAddFeed        =  73          # face 
faPasses         =  74          # face 
faPause          =  75          # face pause before cutting
faRPM            =  76          # face 
faSPInt          =  77          # face 
faSpring         =  78          # face 
faXEnd           =  79          # face 
faXFeed          =  80          # face 
faXRetract       =  81          # face 
faXStart         =  82          # face 
faZEnd           =  83          # face 
faZFeed          =  84          # face 
faZRetract       =  85          # face 
faZStart         =  86          # face 

# jog config

jogInc           =  87          # jog 
jogXPos          =  88          # jog 
jogXPosDiam      =  89          # jog 
jogZPos          =  90          # jog 

# jog panel config

jpSurfaceSpeed   =  91          # jogpanle fpm or rpm
jpXDroDiam       =  92          # jogpanel x dro diameter

# jog time parameters

jogTimeInitial   =  93          # jog time initial
jogTimeInc       =  94          # jog time increment
jogTimeMax       =  95          # jog time max

# keypad

keypadPort       =  96          # external dro port
keypadRate       =  97          # external dro baud Rate

# main panel

mainPanel        =  98          # name of main panel

# mega config

cfgMegaVFD       =  99          # mega vfd speed mode
cfgMegaEncTest   = 100          # mega encoder test
cfgMegaEncLines  = 101          # mega encoder lines

# spindle config

spAccel          = 102          # spindle acceleration
spAccelTime      = 103          # spindle acceleration time
spCurRange       = 104          # spindle current range
spInvDir         = 105          # spindle invert direction
spJogAccelTime   = 106          # spindle jog acceleration time
spJogMax         = 107          # spindle jog max speed
spJogMin         = 108          # spindle jog min speed
spJTimeInc       = 109          # spindle jog increment
spJTimeInitial   = 110          # spindle jog initial time 
spJTimeMax       = 111          # spindle jog max
spMaxRPM         = 112          # spindle jog max rpm
spMicroSteps     = 113          # spindle micro steps
spMinRPM         = 114          # spindle minimum rpm
spMotorSteps     = 115          # spindle motor stpes per revolution
spMotorTest      = 116          # use stepper drive to test motor
spPWMFreq        = 117          # spindle pwm frequency
spMegaSim        = 118          # spindle use mega to simulate index and encoder
spRangeMin1      = 119          # spindle speed range 1 minimum
spRangeMin2      = 120          # spindle speed range 2 minimum
spRangeMin3      = 121          # spindle speed range 3 minimum
spRangeMin4      = 122          # spindle speed range 4 minimum
spRangeMin5      = 123          # spindle speed range 5 minimum
spRangeMin6      = 124          # spindle speed range 6 minimum
spRangeMax1      = 125          # spindle speed range 1 maximum
spRangeMax2      = 126          # spindle speed range 2 maximum
spRangeMax3      = 127          # spindle speed range 3 maximum
spRangeMax4      = 128          # spindle speed range 4 maximum
spRangeMax5      = 129          # spindle speed range 5 maximum
spRangeMax6      = 130          # spindle speed range 6 maximum
spRanges         = 131          # spindle number of speed ranges
spStepDrive      = 132          # spindle stepper drive
spSwitch         = 133          # spindle off on switch
spTestEncoder    = 134          # spindle test generate encoder test pulse
spTestIndex      = 135          # spindle test generate internal index pulse
spVarSpeed       = 136          # spindle variable speed

# sync communications config

syncPort         = 137          # sync comm port
syncRate         = 138          # sync comm baud rate

# threading config

thAddFeed        = 139          # thread feed to add after done
thAlternate      = 140          # thread alternate thread flanks
thAngle          = 141          # thread half angle of thread
thFirstFeed      = 142          # thread first feed for thread area calc
thFirstFeedBtn   = 143          # thread button to select first feed
thInternal       = 144          # thread internal threads
thLastFeed       = 145          # thread last feed for thread area calculation
thLastFeedBtn    = 146          # thread button to select last feed
thLeftHand       = 147          # thread left hand 
thMM             = 148          # thread button for mm
thPasses         = 149          # thread number of passes
thPause          = 150          # thread pause between passes
thRPM            = 151          # thread speed for threading operation
thRunout         = 152          # thread runout for rh exit or lh entrance
thSPInt          = 153          # thread spring pass interval
thSpring         = 154          # thread number of spring passes at end
thTPI            = 155          # thread select thread in threads per inch
thThread         = 156          # thread field containing tpi or pitch
thXDepth         = 157          # thread x depth of thread
thXRetract       = 158          # thread x retract
thXStart         = 159          # thread x diameter
thXTaper         = 160          # thread x taper
thZ0             = 161          # thread z right end of thread left start
thZ1             = 162          # thread z right start left end
thZRetract       = 163          # thread z retract

# taper config

tpAddFeed        = 164          # tp 
tpAngle          = 165          # tp 
tpAngleBtn       = 166          # tp 
tpDeltaBtn       = 167          # tp 
tpInternal       = 168          # tp 
tpLargeDiam      = 169          # tp 
tpPasses         = 170          # tp 
tpPause          = 171          # tp 
tpRPM            = 172          # tp 
tpSPInt          = 173          # tp 
tpSmallDiam      = 174          # tp 
tpSpring         = 175          # tp 
tpTaperSel       = 176          # tp 
tpXDelta         = 177          # tp 
tpXFeed          = 178          # tp 
tpXFinish        = 179          # tp 
tpXInFeed        = 180          # tp 
tpXRetract       = 181          # tp 
tpZDelta         = 182          # tp 
tpZFeed          = 183          # tp 
tpZLength        = 184          # tp 
tpZRetract       = 185          # tp 
tpZStart         = 186          # tp 

# turn config

tuAddFeed        = 187          # turn 
tuInternal       = 188          # turn internal
tuManual         = 189          # turn manual mode
tuPasses         = 190          # turn 
tuPause          = 191          # turn 
tuRPM            = 192          # turn 
tuSPInt          = 193          # turn 
tuSpring         = 194          # turn 
tuXDiam0         = 195          # turn 
tuXDiam1         = 196          # turn 
tuXFeed          = 197          # turn 
tuXRetract       = 198          # turn 
tuZEnd           = 199          # turn 
tuZFeed          = 200          # turn 
tuZRetract       = 201          # turn 
tuZStart         = 202          # turn 

# x axis config

xAccel           = 203          # x axis 
xBackInc         = 204          # z axis distance to go past for taking out backlash
xBacklash        = 205          # x axis 
xDoneDelay       = 206          # x axis done to read dro delay
xDroFinalDist    = 207          # x dro final approach dist
xDROInch         = 208          # x axis 
xDROPos          = 209          # x axis use dro to go to correct position
xHomeDir         = 210          # x axis 
xHomeDist        = 211          # x axis 
xHomeDistBackoff = 212          # x axis 
xHomeDistRev     = 213          # x axis 
xHomeEna         = 214          # x axis 
xHomeEnd         = 215          # x axis 
xHomeInv         = 216          # x axis 
xHomeLoc         = 217          # x axis 
xHomeSpeed       = 218          # x axis 
xHomeStart       = 219          # x axis 
xInvDRO          = 220          # x axis invert dro
xInvDir          = 221          # x axis invert stepper direction
xInvEnc          = 222          # x axis 
xInvMpg          = 223          # x axis invert mpg direction
xJogMax          = 224          # x axis 
xJogMin          = 225          # x axis 
xLimEna          = 226          # x axis limits enable
xLimNegInv       = 227          # x axis negative limit invert
xLimPosInv       = 228          # x axis positive limit invert
xMpgInc          = 229          # x axis jog increment
xMpgMax          = 230          # x axis jog maximum
xJogSpeed        = 231          # x axis 
xMaxSpeed        = 232          # x axis 
xMicroSteps      = 233          # x axis 
xMinSpeed        = 234          # x axis 
xMotorRatio      = 235          # x axis 
xMotorSteps      = 236          # x axis 
xRetractLoc      = 237          # x axis 
xPitch           = 238          # x axis 
xProbeDist       = 239          # x axis 

# x axis position config

xSvPosition      = 240          # x axis 
xSvHomeOffset    = 241          # x axis 
xSvDROPosition   = 242          # x axis 
xSvDROOffset     = 243          # x axis 

# z axis config

zAccel           = 244          # z axis 
zBackInc         = 245          # z axis distance to go past for taking out backlash
zBacklash        = 246          # z axis 
zDoneDelay       = 247          # z axis done to read dro delay
zDroFinalDist    = 248          # z dro final approach dist
zDROPos          = 249          # z axis use dro to go to correct position
zDROInch         = 250          # z axis 
zHomeDir         = 251          # z axis 
zHomeDist        = 252          # z axis 
zHomeDistRev     = 253          # z axis 
zHomeDistBackoff = 254          # z axis 
zHomeEna         = 255          # z axis 
zHomeEnd         = 256          # z axis 
zHomeInv         = 257          # z axis 
zHomeLoc         = 258          # z axis 
zHomeSpeed       = 259          # z axis 
zHomeStart       = 260          # z axis 
zInvDRO          = 261          # z axis 
zInvDir          = 262          # z axis 
zInvEnc          = 263          # z axis 
zInvMpg          = 264          # z axis 
zJogMax          = 265          # z axis 
zJogMin          = 266          # z axis 
zMpgInc          = 267          # z axis jog increment
zMpgMax          = 268          # z axis jog maximum
zJogSpeed        = 269          # z axis 
zLimEna          = 270          # z axis limits enable
zLimNegInv       = 271          # z axis negative limit invert
zLimPosInv       = 272          # z axis positive limit invert
zMaxSpeed        = 273          # z axis 
zMicroSteps      = 274          # z axis 
zMinSpeed        = 275          # z axis 
zMotorRatio      = 276          # z axis 
zMotorSteps      = 277          # z axis 
zRetractLoc      = 278          # z axis 
zPitch           = 279          # z axis 
zProbeDist       = 280          # z axis 
zProbeSpeed      = 281          # z axis 

# z axis position config

zSvPosition      = 282          # z axis 
zSvHomeOffset    = 283          # z axis 
zSvDROPosition   = 284          # z axis 
zSvDROOffset     = 285          # z axis 
cfgJogDebug      = 286          # debug jogging

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
    'cfgIntSync' : 39,
    'cfgInvEncDir' : 40,
    'cfgLCD' : 41,
    'cfgMega' : 42,
    'cfgMPG' : 43,
    'cfgPrbInv' : 44,
    'cfgRemDbg' : 45,
    'cfgSpEncCap' : 46,
    'cfgSpEncoder' : 47,
    'cfgSpSync' : 48,
    'cfgSpSyncBoard' : 49,
    'cfgSpUseEncoder' : 50,
    'cfgSyncSPI' : 51,
    'cfgTaperCycleDist' : 52,
    'cfgTestMode' : 53,
    'cfgTestRPM' : 54,
    'cfgTurnSync' : 55,
    'cfgThreadSync' : 56,
    'commPort' : 57,
    'commRate' : 58,
    'cuPause' : 59,
    'cuRPM' : 60,
    'cuToolWidth' : 61,
    'cuXEnd' : 62,
    'cuXFeed' : 63,
    'cuXRetract' : 64,
    'cuXStart' : 65,
    'cuZCutoff' : 66,
    'cuZRetract' : 67,
    'cuZStart' : 68,
    'droXPos' : 69,
    'droZPos' : 70,
    'extDroPort' : 71,
    'extDroRate' : 72,
    'faAddFeed' : 73,
    'faPasses' : 74,
    'faPause' : 75,
    'faRPM' : 76,
    'faSPInt' : 77,
    'faSpring' : 78,
    'faXEnd' : 79,
    'faXFeed' : 80,
    'faXRetract' : 81,
    'faXStart' : 82,
    'faZEnd' : 83,
    'faZFeed' : 84,
    'faZRetract' : 85,
    'faZStart' : 86,
    'jogInc' : 87,
    'jogXPos' : 88,
    'jogXPosDiam' : 89,
    'jogZPos' : 90,
    'jpSurfaceSpeed' : 91,
    'jpXDroDiam' : 92,
    'jogTimeInitial' : 93,
    'jogTimeInc' : 94,
    'jogTimeMax' : 95,
    'keypadPort' : 96,
    'keypadRate' : 97,
    'mainPanel' : 98,
    'cfgMegaVFD' : 99,
    'cfgMegaEncTest' : 100,
    'cfgMegaEncLines' : 101,
    'spAccel' : 102,
    'spAccelTime' : 103,
    'spCurRange' : 104,
    'spInvDir' : 105,
    'spJogAccelTime' : 106,
    'spJogMax' : 107,
    'spJogMin' : 108,
    'spJTimeInc' : 109,
    'spJTimeInitial' : 110,
    'spJTimeMax' : 111,
    'spMaxRPM' : 112,
    'spMicroSteps' : 113,
    'spMinRPM' : 114,
    'spMotorSteps' : 115,
    'spMotorTest' : 116,
    'spPWMFreq' : 117,
    'spMegaSim' : 118,
    'spRangeMin1' : 119,
    'spRangeMin2' : 120,
    'spRangeMin3' : 121,
    'spRangeMin4' : 122,
    'spRangeMin5' : 123,
    'spRangeMin6' : 124,
    'spRangeMax1' : 125,
    'spRangeMax2' : 126,
    'spRangeMax3' : 127,
    'spRangeMax4' : 128,
    'spRangeMax5' : 129,
    'spRangeMax6' : 130,
    'spRanges' : 131,
    'spStepDrive' : 132,
    'spSwitch' : 133,
    'spTestEncoder' : 134,
    'spTestIndex' : 135,
    'spVarSpeed' : 136,
    'syncPort' : 137,
    'syncRate' : 138,
    'thAddFeed' : 139,
    'thAlternate' : 140,
    'thAngle' : 141,
    'thFirstFeed' : 142,
    'thFirstFeedBtn' : 143,
    'thInternal' : 144,
    'thLastFeed' : 145,
    'thLastFeedBtn' : 146,
    'thLeftHand' : 147,
    'thMM' : 148,
    'thPasses' : 149,
    'thPause' : 150,
    'thRPM' : 151,
    'thRunout' : 152,
    'thSPInt' : 153,
    'thSpring' : 154,
    'thTPI' : 155,
    'thThread' : 156,
    'thXDepth' : 157,
    'thXRetract' : 158,
    'thXStart' : 159,
    'thXTaper' : 160,
    'thZ0' : 161,
    'thZ1' : 162,
    'thZRetract' : 163,
    'tpAddFeed' : 164,
    'tpAngle' : 165,
    'tpAngleBtn' : 166,
    'tpDeltaBtn' : 167,
    'tpInternal' : 168,
    'tpLargeDiam' : 169,
    'tpPasses' : 170,
    'tpPause' : 171,
    'tpRPM' : 172,
    'tpSPInt' : 173,
    'tpSmallDiam' : 174,
    'tpSpring' : 175,
    'tpTaperSel' : 176,
    'tpXDelta' : 177,
    'tpXFeed' : 178,
    'tpXFinish' : 179,
    'tpXInFeed' : 180,
    'tpXRetract' : 181,
    'tpZDelta' : 182,
    'tpZFeed' : 183,
    'tpZLength' : 184,
    'tpZRetract' : 185,
    'tpZStart' : 186,
    'tuAddFeed' : 187,
    'tuInternal' : 188,
    'tuManual' : 189,
    'tuPasses' : 190,
    'tuPause' : 191,
    'tuRPM' : 192,
    'tuSPInt' : 193,
    'tuSpring' : 194,
    'tuXDiam0' : 195,
    'tuXDiam1' : 196,
    'tuXFeed' : 197,
    'tuXRetract' : 198,
    'tuZEnd' : 199,
    'tuZFeed' : 200,
    'tuZRetract' : 201,
    'tuZStart' : 202,
    'xAccel' : 203,
    'xBackInc' : 204,
    'xBacklash' : 205,
    'xDoneDelay' : 206,
    'xDroFinalDist' : 207,
    'xDROInch' : 208,
    'xDROPos' : 209,
    'xHomeDir' : 210,
    'xHomeDist' : 211,
    'xHomeDistBackoff' : 212,
    'xHomeDistRev' : 213,
    'xHomeEna' : 214,
    'xHomeEnd' : 215,
    'xHomeInv' : 216,
    'xHomeLoc' : 217,
    'xHomeSpeed' : 218,
    'xHomeStart' : 219,
    'xInvDRO' : 220,
    'xInvDir' : 221,
    'xInvEnc' : 222,
    'xInvMpg' : 223,
    'xJogMax' : 224,
    'xJogMin' : 225,
    'xLimEna' : 226,
    'xLimNegInv' : 227,
    'xLimPosInv' : 228,
    'xMpgInc' : 229,
    'xMpgMax' : 230,
    'xJogSpeed' : 231,
    'xMaxSpeed' : 232,
    'xMicroSteps' : 233,
    'xMinSpeed' : 234,
    'xMotorRatio' : 235,
    'xMotorSteps' : 236,
    'xRetractLoc' : 237,
    'xPitch' : 238,
    'xProbeDist' : 239,
    'xSvPosition' : 240,
    'xSvHomeOffset' : 241,
    'xSvDROPosition' : 242,
    'xSvDROOffset' : 243,
    'zAccel' : 244,
    'zBackInc' : 245,
    'zBacklash' : 246,
    'zDoneDelay' : 247,
    'zDroFinalDist' : 248,
    'zDROPos' : 249,
    'zDROInch' : 250,
    'zHomeDir' : 251,
    'zHomeDist' : 252,
    'zHomeDistRev' : 253,
    'zHomeDistBackoff' : 254,
    'zHomeEna' : 255,
    'zHomeEnd' : 256,
    'zHomeInv' : 257,
    'zHomeLoc' : 258,
    'zHomeSpeed' : 259,
    'zHomeStart' : 260,
    'zInvDRO' : 261,
    'zInvDir' : 262,
    'zInvEnc' : 263,
    'zInvMpg' : 264,
    'zJogMax' : 265,
    'zJogMin' : 266,
    'zMpgInc' : 267,
    'zMpgMax' : 268,
    'zJogSpeed' : 269,
    'zLimEna' : 270,
    'zLimNegInv' : 271,
    'zLimPosInv' : 272,
    'zMaxSpeed' : 273,
    'zMicroSteps' : 274,
    'zMinSpeed' : 275,
    'zMotorRatio' : 276,
    'zMotorSteps' : 277,
    'zRetractLoc' : 278,
    'zPitch' : 279,
    'zProbeDist' : 280,
    'zProbeSpeed' : 281,
    'zSvPosition' : 282,
    'zSvHomeOffset' : 283,
    'zSvDROPosition' : 284,
    'zSvDROOffset' : 285,
    'cfgJogDebug' : 286,
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
    'cfgIntSync',
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
