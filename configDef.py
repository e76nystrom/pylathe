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
cfgDROStep       =  29          # config step pulse controls dro
cfgDraw          =  30          # config draw paths
cfgEncoder       =  31          # config encoder counts per revolution
cfgEStop         =  32          # config estop enable
cfgEStopInv      =  33          # config estop invert
cfgExtDro        =  34          # config external digital readout
cfgFcy           =  35          # config microprocessor clock frequency
cfgFpga          =  36          # config fpga interface present
cfgFpgaFreq      =  37          # config fpga frequency
cfgFreqMult      =  38          # config fpga frequency multiplier
cfgHomeInPlace   =  39          # config home in place
cfgIntSync       =  40          # config internal sync
cfgInvEncDir     =  41          # config fpga invert encoder direction
cfgLCD           =  42          # config enable lcd
cfgMega          =  43          # config control link to mega
cfgMPG           =  44          # config enable manual pulse generator
cfgPrbInv        =  45          # config invert probe signal
cfgRemDbg        =  46          # config print remote debug info
cfgSpEncCap      =  47          # config encoder on capture interrupt
cfgSpEncoder     =  48          # config spindle encoder
cfgSpSync        =  49          # config spindle using timer
cfgSpSyncBoard   =  50          # config spindle sync board
cfgSpUseEncoder  =  51          # config use spindle encoder for threading
cfgSyncSPI       =  52          # config sync comm through spi
cfgTaperCycleDist =  53         # config taper cycle distance
cfgTestMode      =  54          # conifg test mode
cfgTestRPM       =  55          # config fpga test rpm value
cfgTurnSync      =  56          # config for turning synchronization
cfgThreadSync    =  57          # config for threading synchronization

# communications cxonfig

commPort         =  58          # comm port
commRate         =  59          # comm baud rate

# cutoff config

cuPause          =  60          # cutoff pause before cutting
cuRPM            =  61          # cutoff rpm
cuToolWidth      =  62          # cutoff tool width
cuXEnd           =  63          # cutoff x end
cuXFeed          =  64          # cutoff x feed
cuXRetract       =  65          # cutoff x retract
cuXStart         =  66          # cutoff x start
cuZCutoff        =  67          # cutoff offset to z cutoff
cuZRetract       =  68          # cutoff offset to z retract
cuZStart         =  69          # cutoff z location

# dro position

droXPos          =  70          # dro x position
droZPos          =  71          # dro z position

# external dro

extDroPort       =  72          # external dro port
extDroRate       =  73          # external dro baud Rate

# face config

faAddFeed        =  74          # face 
faPasses         =  75          # face 
faPause          =  76          # face pause before cutting
faRPM            =  77          # face 
faSPInt          =  78          # face 
faSpring         =  79          # face 
faXEnd           =  80          # face 
faXFeed          =  81          # face 
faXRetract       =  82          # face 
faXStart         =  83          # face 
faZEnd           =  84          # face 
faZFeed          =  85          # face 
faZRetract       =  86          # face 
faZStart         =  87          # face 

# jog config

jogInc           =  88          # jog 
jogXPos          =  89          # jog 
jogXPosDiam      =  90          # jog 
jogZPos          =  91          # jog 

# jog panel config

jpSurfaceSpeed   =  92          # jogpanle fpm or rpm
jpXDroDiam       =  93          # jogpanel x dro diameter

# jog time parameters

jogTimeInitial   =  94          # jog time initial
jogTimeInc       =  95          # jog time increment
jogTimeMax       =  96          # jog time max

# keypad

keypadPort       =  97          # external dro port
keypadRate       =  98          # external dro baud Rate

# main panel

mainPanel        =  99          # name of main panel

# mega config

cfgMegaVFD       = 100          # mega vfd speed mode
cfgMegaEncTest   = 101          # mega encoder test
cfgMegaEncLines  = 102          # mega encoder lines

# spindle config

spAccel          = 103          # spindle acceleration
spAccelTime      = 104          # spindle acceleration time
spCurRange       = 105          # spindle current range
spInvDir         = 106          # spindle invert direction
spJogAccelTime   = 107          # spindle jog acceleration time
spJogMax         = 108          # spindle jog max speed
spJogMin         = 109          # spindle jog min speed
spJTimeInc       = 110          # spindle jog increment
spJTimeInitial   = 111          # spindle jog initial time 
spJTimeMax       = 112          # spindle jog max
spMaxRPM         = 113          # spindle jog max rpm
spMicroSteps     = 114          # spindle micro steps
spMinRPM         = 115          # spindle minimum rpm
spMotorSteps     = 116          # spindle motor stpes per revolution
spMotorTest      = 117          # use stepper drive to test motor
spPWMFreq        = 118          # spindle pwm frequency
spMegaSim        = 119          # spindle use mega to simulate index and encoder
spRangeMin1      = 120          # spindle speed range 1 minimum
spRangeMin2      = 121          # spindle speed range 2 minimum
spRangeMin3      = 122          # spindle speed range 3 minimum
spRangeMin4      = 123          # spindle speed range 4 minimum
spRangeMin5      = 124          # spindle speed range 5 minimum
spRangeMin6      = 125          # spindle speed range 6 minimum
spRangeMax1      = 126          # spindle speed range 1 maximum
spRangeMax2      = 127          # spindle speed range 2 maximum
spRangeMax3      = 128          # spindle speed range 3 maximum
spRangeMax4      = 129          # spindle speed range 4 maximum
spRangeMax5      = 130          # spindle speed range 5 maximum
spRangeMax6      = 131          # spindle speed range 6 maximum
spRanges         = 132          # spindle number of speed ranges
spStepDrive      = 133          # spindle stepper drive
spSwitch         = 134          # spindle off on switch
spTestEncoder    = 135          # spindle test generate encoder test pulse
spTestIndex      = 136          # spindle test generate internal index pulse
spVarSpeed       = 137          # spindle variable speed

# sync communications config

syncPort         = 138          # sync comm port
syncRate         = 139          # sync comm baud rate

# threading config

thAddFeed        = 140          # thread feed to add after done
thAlternate      = 141          # thread alternate thread flanks
thAngle          = 142          # thread half angle of thread
thFirstFeed      = 143          # thread first feed for thread area calc
thFirstFeedBtn   = 144          # thread button to select first feed
thInternal       = 145          # thread internal threads
thLastFeed       = 146          # thread last feed for thread area calculation
thLastFeedBtn    = 147          # thread button to select last feed
thLeftHand       = 148          # thread left hand 
thMM             = 149          # thread button for mm
thPasses         = 150          # thread number of passes
thPause          = 151          # thread pause between passes
thRPM            = 152          # thread speed for threading operation
thRunout         = 153          # thread runout for rh exit or lh entrance
thSPInt          = 154          # thread spring pass interval
thSpring         = 155          # thread number of spring passes at end
thTPI            = 156          # thread select thread in threads per inch
thThread         = 157          # thread field containing tpi or pitch
thXDepth         = 158          # thread x depth of thread
thXRetract       = 159          # thread x retract
thXStart         = 160          # thread x diameter
thXTaper         = 161          # thread x taper
thZ0             = 162          # thread z right end of thread left start
thZ1             = 163          # thread z right start left end
thZRetract       = 164          # thread z retract

# taper config

tpAddFeed        = 165          # tp 
tpAngle          = 166          # tp 
tpAngleBtn       = 167          # tp 
tpDeltaBtn       = 168          # tp 
tpInternal       = 169          # tp 
tpLargeDiam      = 170          # tp 
tpPasses         = 171          # tp 
tpPause          = 172          # tp 
tpRPM            = 173          # tp 
tpSPInt          = 174          # tp 
tpSmallDiam      = 175          # tp 
tpSpring         = 176          # tp 
tpTaperSel       = 177          # tp 
tpXDelta         = 178          # tp 
tpXFeed          = 179          # tp 
tpXFinish        = 180          # tp 
tpXInFeed        = 181          # tp 
tpXRetract       = 182          # tp 
tpZDelta         = 183          # tp 
tpZFeed          = 184          # tp 
tpZLength        = 185          # tp 
tpZRetract       = 186          # tp 
tpZStart         = 187          # tp 

# turn config

tuAddFeed        = 188          # turn 
tuInternal       = 189          # turn internal
tuManual         = 190          # turn manual mode
tuPasses         = 191          # turn 
tuPause          = 192          # turn 
tuRPM            = 193          # turn 
tuSPInt          = 194          # turn 
tuSpring         = 195          # turn 
tuXDiam0         = 196          # turn 
tuXDiam1         = 197          # turn 
tuXFeed          = 198          # turn 
tuXRetract       = 199          # turn 
tuZEnd           = 200          # turn 
tuZFeed          = 201          # turn 
tuZRetract       = 202          # turn 
tuZStart         = 203          # turn 

# x axis config

xAccel           = 204          # x axis 
xBackInc         = 205          # z axis distance to go past for taking out backlash
xBacklash        = 206          # x axis 
xDoneDelay       = 207          # x axis done to read dro delay
xDroFinalDist    = 208          # x dro final approach dist
xDROInch         = 209          # x axis 
xDROPos          = 210          # x axis use dro to go to correct position
xHomeDir         = 211          # x axis 
xHomeDist        = 212          # x axis 
xHomeDistBackoff = 213          # x axis 
xHomeDistRev     = 214          # x axis 
xHomeEna         = 215          # x axis 
xHomeEnd         = 216          # x axis 
xHomeInv         = 217          # x axis 
xHomeLoc         = 218          # x axis 
xHomeSpeed       = 219          # x axis 
xHomeStart       = 220          # x axis 
xInvDRO          = 221          # x axis invert dro
xInvDir          = 222          # x axis invert stepper direction
xInvEnc          = 223          # x axis 
xInvMpg          = 224          # x axis invert mpg direction
xJogMax          = 225          # x axis 
xJogMin          = 226          # x axis 
xLimEna          = 227          # x axis limits enable
xLimNegInv       = 228          # x axis negative limit invert
xLimPosInv       = 229          # x axis positive limit invert
xMpgInc          = 230          # x axis jog increment
xMpgMax          = 231          # x axis jog maximum
xJogSpeed        = 232          # x axis 
xMaxSpeed        = 233          # x axis 
xMicroSteps      = 234          # x axis 
xMinSpeed        = 235          # x axis 
xMotorRatio      = 236          # x axis 
xMotorSteps      = 237          # x axis 
xRetractLoc      = 238          # x axis 
xPitch           = 239          # x axis 
xProbeDist       = 240          # x axis 

# x axis position config

xSvPosition      = 241          # x axis 
xSvHomeOffset    = 242          # x axis 
xSvDROPosition   = 243          # x axis 
xSvDROOffset     = 244          # x axis 

# z axis config

zAccel           = 245          # z axis 
zBackInc         = 246          # z axis distance to go past for taking out backlash
zBacklash        = 247          # z axis 
zDoneDelay       = 248          # z axis done to read dro delay
zDroFinalDist    = 249          # z dro final approach dist
zDROPos          = 250          # z axis use dro to go to correct position
zDROInch         = 251          # z axis 
zHomeDir         = 252          # z axis 
zHomeDist        = 253          # z axis 
zHomeDistRev     = 254          # z axis 
zHomeDistBackoff = 255          # z axis 
zHomeEna         = 256          # z axis 
zHomeEnd         = 257          # z axis 
zHomeInv         = 258          # z axis 
zHomeLoc         = 259          # z axis 
zHomeSpeed       = 260          # z axis 
zHomeStart       = 261          # z axis 
zInvDRO          = 262          # z axis 
zInvDir          = 263          # z axis 
zInvEnc          = 264          # z axis 
zInvMpg          = 265          # z axis 
zJogMax          = 266          # z axis 
zJogMin          = 267          # z axis 
zMpgInc          = 268          # z axis jog increment
zMpgMax          = 269          # z axis jog maximum
zJogSpeed        = 270          # z axis 
zLimEna          = 271          # z axis limits enable
zLimNegInv       = 272          # z axis negative limit invert
zLimPosInv       = 273          # z axis positive limit invert
zMaxSpeed        = 274          # z axis 
zMicroSteps      = 275          # z axis 
zMinSpeed        = 276          # z axis 
zMotorRatio      = 277          # z axis 
zMotorSteps      = 278          # z axis 
zRetractLoc      = 279          # z axis 
zPitch           = 280          # z axis 
zProbeDist       = 281          # z axis 
zProbeSpeed      = 282          # z axis 

# z axis position config

zSvPosition      = 283          # z axis 
zSvHomeOffset    = 284          # z axis 
zSvDROPosition   = 285          # z axis 
zSvDROOffset     = 286          # z axis 
cfgJogDebug      = 287          # debug jogging

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
    'cfgDROStep' : 29,
    'cfgDraw' : 30,
    'cfgEncoder' : 31,
    'cfgEStop' : 32,
    'cfgEStopInv' : 33,
    'cfgExtDro' : 34,
    'cfgFcy' : 35,
    'cfgFpga' : 36,
    'cfgFpgaFreq' : 37,
    'cfgFreqMult' : 38,
    'cfgHomeInPlace' : 39,
    'cfgIntSync' : 40,
    'cfgInvEncDir' : 41,
    'cfgLCD' : 42,
    'cfgMega' : 43,
    'cfgMPG' : 44,
    'cfgPrbInv' : 45,
    'cfgRemDbg' : 46,
    'cfgSpEncCap' : 47,
    'cfgSpEncoder' : 48,
    'cfgSpSync' : 49,
    'cfgSpSyncBoard' : 50,
    'cfgSpUseEncoder' : 51,
    'cfgSyncSPI' : 52,
    'cfgTaperCycleDist' : 53,
    'cfgTestMode' : 54,
    'cfgTestRPM' : 55,
    'cfgTurnSync' : 56,
    'cfgThreadSync' : 57,
    'commPort' : 58,
    'commRate' : 59,
    'cuPause' : 60,
    'cuRPM' : 61,
    'cuToolWidth' : 62,
    'cuXEnd' : 63,
    'cuXFeed' : 64,
    'cuXRetract' : 65,
    'cuXStart' : 66,
    'cuZCutoff' : 67,
    'cuZRetract' : 68,
    'cuZStart' : 69,
    'droXPos' : 70,
    'droZPos' : 71,
    'extDroPort' : 72,
    'extDroRate' : 73,
    'faAddFeed' : 74,
    'faPasses' : 75,
    'faPause' : 76,
    'faRPM' : 77,
    'faSPInt' : 78,
    'faSpring' : 79,
    'faXEnd' : 80,
    'faXFeed' : 81,
    'faXRetract' : 82,
    'faXStart' : 83,
    'faZEnd' : 84,
    'faZFeed' : 85,
    'faZRetract' : 86,
    'faZStart' : 87,
    'jogInc' : 88,
    'jogXPos' : 89,
    'jogXPosDiam' : 90,
    'jogZPos' : 91,
    'jpSurfaceSpeed' : 92,
    'jpXDroDiam' : 93,
    'jogTimeInitial' : 94,
    'jogTimeInc' : 95,
    'jogTimeMax' : 96,
    'keypadPort' : 97,
    'keypadRate' : 98,
    'mainPanel' : 99,
    'cfgMegaVFD' : 100,
    'cfgMegaEncTest' : 101,
    'cfgMegaEncLines' : 102,
    'spAccel' : 103,
    'spAccelTime' : 104,
    'spCurRange' : 105,
    'spInvDir' : 106,
    'spJogAccelTime' : 107,
    'spJogMax' : 108,
    'spJogMin' : 109,
    'spJTimeInc' : 110,
    'spJTimeInitial' : 111,
    'spJTimeMax' : 112,
    'spMaxRPM' : 113,
    'spMicroSteps' : 114,
    'spMinRPM' : 115,
    'spMotorSteps' : 116,
    'spMotorTest' : 117,
    'spPWMFreq' : 118,
    'spMegaSim' : 119,
    'spRangeMin1' : 120,
    'spRangeMin2' : 121,
    'spRangeMin3' : 122,
    'spRangeMin4' : 123,
    'spRangeMin5' : 124,
    'spRangeMin6' : 125,
    'spRangeMax1' : 126,
    'spRangeMax2' : 127,
    'spRangeMax3' : 128,
    'spRangeMax4' : 129,
    'spRangeMax5' : 130,
    'spRangeMax6' : 131,
    'spRanges' : 132,
    'spStepDrive' : 133,
    'spSwitch' : 134,
    'spTestEncoder' : 135,
    'spTestIndex' : 136,
    'spVarSpeed' : 137,
    'syncPort' : 138,
    'syncRate' : 139,
    'thAddFeed' : 140,
    'thAlternate' : 141,
    'thAngle' : 142,
    'thFirstFeed' : 143,
    'thFirstFeedBtn' : 144,
    'thInternal' : 145,
    'thLastFeed' : 146,
    'thLastFeedBtn' : 147,
    'thLeftHand' : 148,
    'thMM' : 149,
    'thPasses' : 150,
    'thPause' : 151,
    'thRPM' : 152,
    'thRunout' : 153,
    'thSPInt' : 154,
    'thSpring' : 155,
    'thTPI' : 156,
    'thThread' : 157,
    'thXDepth' : 158,
    'thXRetract' : 159,
    'thXStart' : 160,
    'thXTaper' : 161,
    'thZ0' : 162,
    'thZ1' : 163,
    'thZRetract' : 164,
    'tpAddFeed' : 165,
    'tpAngle' : 166,
    'tpAngleBtn' : 167,
    'tpDeltaBtn' : 168,
    'tpInternal' : 169,
    'tpLargeDiam' : 170,
    'tpPasses' : 171,
    'tpPause' : 172,
    'tpRPM' : 173,
    'tpSPInt' : 174,
    'tpSmallDiam' : 175,
    'tpSpring' : 176,
    'tpTaperSel' : 177,
    'tpXDelta' : 178,
    'tpXFeed' : 179,
    'tpXFinish' : 180,
    'tpXInFeed' : 181,
    'tpXRetract' : 182,
    'tpZDelta' : 183,
    'tpZFeed' : 184,
    'tpZLength' : 185,
    'tpZRetract' : 186,
    'tpZStart' : 187,
    'tuAddFeed' : 188,
    'tuInternal' : 189,
    'tuManual' : 190,
    'tuPasses' : 191,
    'tuPause' : 192,
    'tuRPM' : 193,
    'tuSPInt' : 194,
    'tuSpring' : 195,
    'tuXDiam0' : 196,
    'tuXDiam1' : 197,
    'tuXFeed' : 198,
    'tuXRetract' : 199,
    'tuZEnd' : 200,
    'tuZFeed' : 201,
    'tuZRetract' : 202,
    'tuZStart' : 203,
    'xAccel' : 204,
    'xBackInc' : 205,
    'xBacklash' : 206,
    'xDoneDelay' : 207,
    'xDroFinalDist' : 208,
    'xDROInch' : 209,
    'xDROPos' : 210,
    'xHomeDir' : 211,
    'xHomeDist' : 212,
    'xHomeDistBackoff' : 213,
    'xHomeDistRev' : 214,
    'xHomeEna' : 215,
    'xHomeEnd' : 216,
    'xHomeInv' : 217,
    'xHomeLoc' : 218,
    'xHomeSpeed' : 219,
    'xHomeStart' : 220,
    'xInvDRO' : 221,
    'xInvDir' : 222,
    'xInvEnc' : 223,
    'xInvMpg' : 224,
    'xJogMax' : 225,
    'xJogMin' : 226,
    'xLimEna' : 227,
    'xLimNegInv' : 228,
    'xLimPosInv' : 229,
    'xMpgInc' : 230,
    'xMpgMax' : 231,
    'xJogSpeed' : 232,
    'xMaxSpeed' : 233,
    'xMicroSteps' : 234,
    'xMinSpeed' : 235,
    'xMotorRatio' : 236,
    'xMotorSteps' : 237,
    'xRetractLoc' : 238,
    'xPitch' : 239,
    'xProbeDist' : 240,
    'xSvPosition' : 241,
    'xSvHomeOffset' : 242,
    'xSvDROPosition' : 243,
    'xSvDROOffset' : 244,
    'zAccel' : 245,
    'zBackInc' : 246,
    'zBacklash' : 247,
    'zDoneDelay' : 248,
    'zDroFinalDist' : 249,
    'zDROPos' : 250,
    'zDROInch' : 251,
    'zHomeDir' : 252,
    'zHomeDist' : 253,
    'zHomeDistRev' : 254,
    'zHomeDistBackoff' : 255,
    'zHomeEna' : 256,
    'zHomeEnd' : 257,
    'zHomeInv' : 258,
    'zHomeLoc' : 259,
    'zHomeSpeed' : 260,
    'zHomeStart' : 261,
    'zInvDRO' : 262,
    'zInvDir' : 263,
    'zInvEnc' : 264,
    'zInvMpg' : 265,
    'zJogMax' : 266,
    'zJogMin' : 267,
    'zMpgInc' : 268,
    'zMpgMax' : 269,
    'zJogSpeed' : 270,
    'zLimEna' : 271,
    'zLimNegInv' : 272,
    'zLimPosInv' : 273,
    'zMaxSpeed' : 274,
    'zMicroSteps' : 275,
    'zMinSpeed' : 276,
    'zMotorRatio' : 277,
    'zMotorSteps' : 278,
    'zRetractLoc' : 279,
    'zPitch' : 280,
    'zProbeDist' : 281,
    'zProbeSpeed' : 282,
    'zSvPosition' : 283,
    'zSvHomeOffset' : 284,
    'zSvDROPosition' : 285,
    'zSvDROOffset' : 286,
    'cfgJogDebug' : 287,
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
    'cfgDROStep',
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
