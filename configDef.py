# config table

# system config

cfgCmdDis        =   0          # config disable sending commands
cfgDbgSave       =   1          # config save debug info
cfgDRO           =   2          # config dro present
cfgDraw          =   3          # config draw paths
cfgEncoder       =   4          # config xilinx encoder counts per revolution
cfgFcy           =   5          # config microprocesssor clock frequency
cfgFreqMult      =   6          # config xilinx frequency multiplier
cfgHomeInPlace   =   7          # config home in place
cfgInvEncDir     =   8          # config xilinx invert encoder direction
cfgLCD           =   9          # config enable lcd
cfgMPG           =  10          # config enable manual pulse generator
cfgPrbInv        =  11          # config invert probe signal
cfgRemDbg        =  12          # config print remote debug info
cfgTaperCycleDist =  13         # config taper cycle distance
cfgTestMode      =  14          # conifg test mode
cfgTestRPM       =  15          # config xilinx test rpm value
cfgXFreq         =  16          # config xilinx frequency
cfgXilinx        =  17          # config xilinx interface present

# communications config

commPort         =  18          # comm port
commRate         =  19          # comm baud rate

# cutoff config

cuPause          =  20          # cutoff pause before cutting
cuRPM            =  21          # cutoff rpm
cuToolWidth      =  22          # cutoff tool width
cuXEnd           =  23          # cutoff x end
cuXFeed          =  24          # cutoff x feed
cuXRetract       =  25          # cutoff x retract
cuXStart         =  26          # cutoff x start
cuZCutoff        =  27          # cutoff offset to z cutoff
cuZRetract       =  28          # cutoff offset to z retract
cuZStart         =  29          # cutoff z location

# dro position

droXPos          =  30          # dro x position 
droZPos          =  31          # dro z position 

# face config

faAddFeed        =  32          # face 
faPasses         =  33          # face 
faPause          =  34          # face pause before cutting
faRPM            =  35          # face 
faSPInt          =  36          # face 
faSpring         =  37          # face 
faXEnd           =  38          # face 
faXFeed          =  39          # face 
faXRetract       =  40          # face 
faXStart         =  41          # face 
faZEnd           =  42          # face 
faZFeed          =  43          # face 
faZRetract       =  44          # face 
faZStart         =  45          # face 

# jog config

jogInc           =  46          # jog 
jogXPos          =  47          # jog 
jogXPosDiam      =  48          # jog 
jogZPos          =  49          # jog 

# main panel

mainPanel        =  50          # name of main panel

# spindle config

spAccel          =  51          # spindle acceleration
spAccelTime      =  52          # spindle accelerationtime
spInvDir         =  53          # spindle invert direction
spJogAccelTime   =  54          # spindle jog acceleration time
spJogMax         =  55          # spindle jog max speed
spJogMin         =  56          # spindle jog min speed
spMaxRPM         =  57          # spindle jog max rpm
spMicroSteps     =  58          # spindle micro steps
spMinRPM         =  59          # spindle minimum rpm
spMotorSteps     =  60          # spindle motor stpes per revolution
spMotorTest      =  61          # use stepper drive to test motor
spStepDrive      =  62          # spindle stepper drive
spTestIndex      =  63          # spindle test generate internal index pulse

# threading config

thAddFeed        =  64          # thread 
thAlternate      =  65          # thread 
thAngle          =  66          # thread 
thExitRev        =  67          # thread 
thFirstFeed      =  68          # thread 
thFirstFeedBtn   =  69          # thread 
thHFactor        =  70          # thread 
thInternal       =  71          # thread 
thLastFeed       =  72          # thread 
thLastFeedBtn    =  73          # thread 
thMM             =  74          # thread 
thPasses         =  75          # thread 
thPause          =  76          # thread 
thPitch          =  77          # thread 
thRPM            =  78          # thread 
thSPInt          =  79          # thread 
thSpring         =  80          # thread 
thTPI            =  81          # thread 
thXDepth         =  82          # thread 
thXRetract       =  83          # thread 
thXStart         =  84          # thread 
thXTaper         =  85          # thread 
thZEnd           =  86          # thread 
thZRetract       =  87          # thread 
thZStart         =  88          # thread 

# taper config

tpAddFeed        =  89          # tp 
tpAngle          =  90          # tp 
tpAngleBtn       =  91          # tp 
tpDeltaBtn       =  92          # tp 
tpInternal       =  93          # tp 
tpLargeDiam      =  94          # tp 
tpLargeDiamText  =  95          # tp 
tpPasses         =  96          # tp 
tpPause          =  97          # tp 
tpRPM            =  98          # tp 
tpSPInt          =  99          # tp 
tpSmallDiam      = 100          # tp 
tpSmallDiamText  = 101          # tp 
tpSpring         = 102          # tp 
tpTaperSel       = 103          # tp 
tpXDelta         = 104          # tp 
tpXFeed          = 105          # tp 
tpXFinish        = 106          # tp 
tpXInFeed        = 107          # tp 
tpXRetract       = 108          # tp 
tpZDelta         = 109          # tp 
tpZFeed          = 110          # tp 
tpZLength        = 111          # tp 
tpZRetract       = 112          # tp 
tpZStart         = 113          # tp 

# turn config

tuAddFeed        = 114          # turn 
tuInternal       = 115          # turn internal
tuPasses         = 116          # turn 
tuPause          = 117          # turn 
tuRPM            = 118          # turn 
tuSPInt          = 119          # turn 
tuSpring         = 120          # turn 
tuXDiam0         = 121          # turn 
tuXDiam0Text     = 122          # turn 
tuXDiam1         = 123          # turn 
tuXDiam1Text     = 124          # turn 
tuXFeed          = 125          # turn 
tuXRetract       = 126          # turn 
tuZEnd           = 127          # turn 
tuZFeed          = 128          # turn 
tuZRetract       = 129          # turn 
tuZStart         = 130          # turn 

# x axis config

xAccel           = 131          # turn 
xBacklash        = 132          # turn 
xDROInch         = 133          # turn 
xHomeBackoffDist = 134          # x axis 
xHomeDir         = 135          # x axis 
xHomeDist        = 136          # x axis 
xHomeEnd         = 137          # x axis 
xHomeLoc         = 138          # x axis 
xHomeSpeed       = 139          # x axis 
xHomeStart       = 140          # x axis 
xInvDRO          = 141          # x axis 
xInvDir          = 142          # x axis 
xInvEnc          = 143          # x axis 
xInvMpg          = 144          # x axis 
xJogMax          = 145          # x axis 
xJogMin          = 146          # x axis 
xJogSpeed        = 147          # x axis 
xMaxSpeed        = 148          # x axis 
xMicroSteps      = 149          # x axis 
xMinSpeed        = 150          # x axis 
xMotorRatio      = 151          # x axis 
xMotorSteps      = 152          # x axis 
xParkLoc         = 153          # x axis 
xPitch           = 154          # x axis 
xProbeDist       = 155          # x axis 

# x axis position config

xSvPosition      = 156          # z axis 
xSvHomeOffset    = 157          # z axis 
xSvDROPosition   = 158          # x axis 
xSvDROOffset     = 159          # x axis 

# z axis config

zAccel           = 160          # z axis 
zBacklash        = 161          # z axis 
zDROInch         = 162          # z axis 
zInvDRO          = 163          # z axis 
zInvDir          = 164          # z axis 
zInvEnc          = 165          # z axis 
zInvMpg          = 166          # z axis 
zJogMax          = 167          # z axis 
zJogMin          = 168          # z axis 
zJogSpeed        = 169          # z axis 
zMaxSpeed        = 170          # z axis 
zMicroSteps      = 171          # z axis 
zMinSpeed        = 172          # z axis 
zMotorRatio      = 173          # z axis 
zMotorSteps      = 174          # z axis 
zParkLoc         = 175          # z axis 
zPitch           = 176          # z axis 
zProbeDist       = 177          # z axis 
zProbeSpeed      = 178          # z axis 

# z axis position config

zSvPosition      = 179          # z axis 
zSvHomeOffset    = 180          # z axis 
zSvDROPosition   = 181          # z axis 
zSvDROOffset     = 182          # z axis 

config = { \
    'faPasses' : 33,
    'cfgFreqMult' : 6,
    'spStepDrive' : 62,
    'faZRetract' : 44,
    'thZStart' : 88,
    'tpZFeed' : 110,
    'tuPasses' : 116,
    'zInvDir' : 164,
    'spMicroSteps' : 58,
    'jogXPos' : 47,
    'zJogSpeed' : 169,
    'jogZPos' : 49,
    'thAlternate' : 65,
    'jogInc' : 46,
    'tuAddFeed' : 114,
    'tpRPM' : 98,
    'faZStart' : 45,
    'tuZStart' : 130,
    'tpTaperSel' : 103,
    'thXTaper' : 85,
    'tpZRetract' : 112,
    'thXStart' : 84,
    'xHomeStart' : 140,
    'thSPInt' : 79,
    'zMaxSpeed' : 170,
    'cfgTestRPM' : 15,
    'xHomeLoc' : 138,
    'thSpring' : 80,
    'xHomeEnd' : 137,
    'cfgMPG' : 10,
    'xHomeBackoffDist' : 134,
    'xMinSpeed' : 150,
    'xHomeDir' : 135,
    'xMotorSteps' : 152,
    'faZFeed' : 43,
    'thAddFeed' : 64,
    'thXRetract' : 83,
    'xJogSpeed' : 147,
    'cuXRetract' : 25,
    'tpZStart' : 113,
    'cuToolWidth' : 22,
    'spJogMax' : 55,
    'tuRPM' : 118,
    'thLastFeedBtn' : 73,
    'cfgDraw' : 3,
    'faXFeed' : 39,
    'xSvDROPosition' : 158,
    'cfgXFreq' : 16,
    'tuSPInt' : 119,
    'cfgLCD' : 9,
    'xJogMax' : 145,
    'thHFactor' : 70,
    'thFirstFeed' : 68,
    'faAddFeed' : 32,
    'xJogMin' : 146,
    'faXEnd' : 38,
    'spJogMin' : 56,
    'xPitch' : 154,
    'xSvHomeOffset' : 157,
    'tpAngle' : 90,
    'faXStart' : 41,
    'cfgEncoder' : 4,
    'faSPInt' : 36,
    'tpSmallDiam' : 100,
    'tpXFinish' : 106,
    'zSvPosition' : 179,
    'tpAddFeed' : 89,
    'tpDeltaBtn' : 92,
    'tpPasses' : 96,
    'xHomeSpeed' : 139,
    'cfgCmdDis' : 0,
    'cfgDRO' : 2,
    'commPort' : 18,
    'thExitRev' : 67,
    'thZEnd' : 86,
    'thFirstFeedBtn' : 69,
    'zMinSpeed' : 172,
    'thRPM' : 78,
    'droZPos' : 31,
    'tpZDelta' : 109,
    'zSvHomeOffset' : 180,
    'xInvDRO' : 141,
    'tuSpring' : 120,
    'xMotorRatio' : 151,
    'tuInternal' : 115,
    'cfgDbgSave' : 1,
    'tpSmallDiamText' : 101,
    'thXDepth' : 82,
    'cuXEnd' : 23,
    'tuPause' : 117,
    'xProbeDist' : 155,
    'xMaxSpeed' : 148,
    'xDROInch' : 133,
    'xInvDir' : 142,
    'tuZFeed' : 128,
    'zInvEnc' : 165,
    'cuZRetract' : 28,
    'xHomeDist' : 136,
    'cfgPrbInv' : 11,
    'thPitch' : 77,
    'tpZLength' : 111,
    'cuXFeed' : 24,
    'zInvMpg' : 166,
    'thPasses' : 75,
    'spMotorSteps' : 60,
    'cuZStart' : 29,
    'zSvDROOffset' : 182,
    'zAccel' : 160,
    'tpXRetract' : 108,
    'cfgTestMode' : 14,
    'tpXFeed' : 105,
    'thPause' : 76,
    'xInvEnc' : 143,
    'spMinRPM' : 59,
    'tpSpring' : 102,
    'tuZEnd' : 127,
    'tuXFeed' : 125,
    'faSpring' : 37,
    'thInternal' : 71,
    'thZRetract' : 87,
    'thTPI' : 81,
    'tpXDelta' : 104,
    'tuXDiam1Text' : 124,
    'tpAngleBtn' : 91,
    'tpPause' : 97,
    'zBacklash' : 161,
    'cfgInvEncDir' : 8,
    'faPause' : 34,
    'faXRetract' : 40,
    'cuXStart' : 26,
    'cfgHomeInPlace' : 7,
    'xSvDROOffset' : 159,
    'zParkLoc' : 175,
    'faRPM' : 35,
    'spMaxRPM' : 57,
    'cfgFcy' : 5,
    'zMicroSteps' : 171,
    'thLastFeed' : 72,
    'zDROInch' : 162,
    'tuXRetract' : 126,
    'cuRPM' : 21,
    'xInvMpg' : 144,
    'tuZRetract' : 129,
    'tpSPInt' : 99,
    'spTestIndex' : 63,
    'zJogMin' : 168,
    'zMotorRatio' : 173,
    'zPitch' : 176,
    'spInvDir' : 53,
    'spJogAccelTime' : 54,
    'zSvDROPosition' : 181,
    'xBacklash' : 132,
    'mainPanel' : 50,
    'tpLargeDiam' : 94,
    'thAngle' : 66,
    'zMotorSteps' : 174,
    'jogXPosDiam' : 48,
    'cuZCutoff' : 27,
    'xAccel' : 131,
    'spAccelTime' : 52,
    'tpLargeDiamText' : 95,
    'zInvDRO' : 163,
    'cuPause' : 20,
    'commRate' : 19,
    'cfgXilinx' : 17,
    'spAccel' : 51,
    'zJogMax' : 167,
    'droXPos' : 30,
    'tuXDiam0Text' : 122,
    'tpXInFeed' : 107,
    'zProbeDist' : 177,
    'faZEnd' : 42,
    'xParkLoc' : 153,
    'xSvPosition' : 156,
    'spMotorTest' : 61,
    'xMicroSteps' : 149,
    'cfgTaperCycleDist' : 13,
    'tpInternal' : 93,
    'cfgRemDbg' : 12,
    'thMM' : 74,
    'zProbeSpeed' : 178,
    'tuXDiam0' : 121,
    'tuXDiam1' : 123,
    }

configTable = ( \
    'cfgCmdDis',
    'cfgDbgSave',
    'cfgDRO',
    'cfgDraw',
    'cfgEncoder',
    'cfgFcy',
    'cfgFreqMult',
    'cfgHomeInPlace',
    'cfgInvEncDir',
    'cfgLCD',
    'cfgMPG',
    'cfgPrbInv',
    'cfgRemDbg',
    'cfgTaperCycleDist',
    'cfgTestMode',
    'cfgTestRPM',
    'cfgXFreq',
    'cfgXilinx',
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
    'mainPanel',
    'spAccel',
    'spAccelTime',
    'spInvDir',
    'spJogAccelTime',
    'spJogMax',
    'spJogMin',
    'spMaxRPM',
    'spMicroSteps',
    'spMinRPM',
    'spMotorSteps',
    'spMotorTest',
    'spStepDrive',
    'spTestIndex',
    'thAddFeed',
    'thAlternate',
    'thAngle',
    'thExitRev',
    'thFirstFeed',
    'thFirstFeedBtn',
    'thHFactor',
    'thInternal',
    'thLastFeed',
    'thLastFeedBtn',
    'thMM',
    'thPasses',
    'thPause',
    'thPitch',
    'thRPM',
    'thSPInt',
    'thSpring',
    'thTPI',
    'thXDepth',
    'thXRetract',
    'thXStart',
    'thXTaper',
    'thZEnd',
    'thZRetract',
    'thZStart',
    'tpAddFeed',
    'tpAngle',
    'tpAngleBtn',
    'tpDeltaBtn',
    'tpInternal',
    'tpLargeDiam',
    'tpLargeDiamText',
    'tpPasses',
    'tpPause',
    'tpRPM',
    'tpSPInt',
    'tpSmallDiam',
    'tpSmallDiamText',
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
    'tuXDiam0Text',
    'tuXDiam1',
    'tuXDiam1Text',
    'tuXFeed',
    'tuXRetract',
    'tuZEnd',
    'tuZFeed',
    'tuZRetract',
    'tuZStart',
    'xAccel',
    'xBacklash',
    'xDROInch',
    'xHomeBackoffDist',
    'xHomeDir',
    'xHomeDist',
    'xHomeEnd',
    'xHomeLoc',
    'xHomeSpeed',
    'xHomeStart',
    'xInvDRO',
    'xInvDir',
    'xInvEnc',
    'xInvMpg',
    'xJogMax',
    'xJogMin',
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
    'zBacklash',
    'zDROInch',
    'zInvDRO',
    'zInvDir',
    'zInvEnc',
    'zInvMpg',
    'zJogMax',
    'zJogMin',
    'zJogSpeed',
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
    )
