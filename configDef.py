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
cfgTestMode      =  13          # conifg test mode
cfgTestRPM       =  14          # config xilinx test rpm value
cfgXFreq         =  15          # config xilinx frequency
cfgXilinx        =  16          # config xilinx interface present

# communications config

commPort         =  17          # comm port
commRate         =  18          # comm baud rate

# cutoff config

cuPause          =  19          # cutoff pause before cutting
cuRPM            =  20          # cutoff rpm
cuToolWidth      =  21          # cutoff tool width
cuXEnd           =  22          # cutoff x end
cuXFeed          =  23          # cutoff x feed
cuXRetract       =  24          # cutoff x retract
cuXStart         =  25          # cutoff x start
cuZCutoff        =  26          # cutoff offset to z cutoff
cuZRetract       =  27          # cutoff offset to z retract
cuZStart         =  28          # cutoff z location

# dro position

droXPos          =  29          # dro x position 
droZPos          =  30          # dro z position 

# face config

faAddFeed        =  31          # face 
faPasses         =  32          # face 
faPause          =  33          # face pause before cutting
faRPM            =  34          # face 
faSPInt          =  35          # face 
faSpring         =  36          # face 
faXEnd           =  37          # face 
faXFeed          =  38          # face 
faXRetract       =  39          # face 
faXStart         =  40          # face 
faZEnd           =  41          # face 
faZFeed          =  42          # face 
faZRetract       =  43          # face 
faZStart         =  44          # face 

# jog config

jogInc           =  45          # jog 
jogXPos          =  46          # jog 
jogXPosDiam      =  47          # jog 
jogZPos          =  48          # jog 

# main panel

mainPanel        =  49          # name of main panel

# spindle config

spAccel          =  50          # spindle acceleration
spAccelTime      =  51          # spindle accelerationtime
spInvDir         =  52          # spindle invert direction
spJogAccelTime   =  53          # spindle jog acceleration time
spJogMax         =  54          # spindle jog max speed
spJogMin         =  55          # spindle jog min speed
spMaxRPM         =  56          # spindle jog max rpm
spMicroSteps     =  57          # spindle micro steps
spMinRPM         =  58          # spindle minimum rpm
spMotorSteps     =  59          # spindle motor stpes per revolution
spMotorTest      =  60          # use stepper drive to test motor
spStepDrive      =  61          # spindle stepper drive
spTestIndex      =  62          # spindle test generate internal index pulse

# threading config

thAddFeed        =  63          # thread 
thAlternate      =  64          # thread 
thAngle          =  65          # thread 
thExitRev        =  66          # thread 
thFirstFeed      =  67          # thread 
thFirstFeedBtn   =  68          # thread 
thHFactor        =  69          # thread 
thInternal       =  70          # thread 
thLastFeed       =  71          # thread 
thLastFeedBtn    =  72          # thread 
thMM             =  73          # thread 
thPasses         =  74          # thread 
thPause          =  75          # thread 
thPitch          =  76          # thread 
thRPM            =  77          # thread 
thSPInt          =  78          # thread 
thSpring         =  79          # thread 
thTPI            =  80          # thread 
thXDepth         =  81          # thread 
thXRetract       =  82          # thread 
thXStart         =  83          # thread 
thXTaper         =  84          # thread 
thZEnd           =  85          # thread 
thZRetract       =  86          # thread 
thZStart         =  87          # thread 

# taper config

tpAddFeed        =  88          # tp 
tpAngle          =  89          # tp 
tpAngleBtn       =  90          # tp 
tpDeltaBtn       =  91          # tp 
tpInternal       =  92          # tp 
tpLargeDiam      =  93          # tp 
tpLargeDiamText  =  94          # tp 
tpPasses         =  95          # tp 
tpPause          =  96          # tp 
tpRPM            =  97          # tp 
tpSPInt          =  98          # tp 
tpSmallDiam      =  99          # tp 
tpSmallDiamText  = 100          # tp 
tpSpring         = 101          # tp 
tpTaperSel       = 102          # tp 
tpXDelta         = 103          # tp 
tpXFeed          = 104          # tp 
tpXFinish        = 105          # tp 
tpXInFeed        = 106          # tp 
tpXRetract       = 107          # tp 
tpZDelta         = 108          # tp 
tpZFeed          = 109          # tp 
tpZLength        = 110          # tp 
tpZRetract       = 111          # tp 
tpZStart         = 112          # tp 

# turn config

tuAddFeed        = 113          # turn 
tuInternal       = 114          # turn internal
tuPasses         = 115          # turn 
tuPause          = 116          # turn 
tuRPM            = 117          # turn 
tuSPInt          = 118          # turn 
tuSpring         = 119          # turn 
tuXDiam0         = 120          # turn 
tuXDiam0Text     = 121          # turn 
tuXDiam1         = 122          # turn 
tuXDiam1Text     = 123          # turn 
tuXFeed          = 124          # turn 
tuXRetract       = 125          # turn 
tuZEnd           = 126          # turn 
tuZFeed          = 127          # turn 
tuZRetract       = 128          # turn 
tuZStart         = 129          # turn 

# x axis config

xAccel           = 130          # turn 
xBacklash        = 131          # turn 
xDROInch         = 132          # turn 
xHomeBackoffDist = 133          # x axis 
xHomeDir         = 134          # x axis 
xHomeDist        = 135          # x axis 
xHomeEnd         = 136          # x axis 
xHomeLoc         = 137          # x axis 
xHomeSpeed       = 138          # x axis 
xHomeStart       = 139          # x axis 
xInvDRO          = 140          # x axis 
xInvDir          = 141          # x axis 
xInvEnc          = 142          # x axis 
xInvMpg          = 143          # x axis 
xJogMax          = 144          # x axis 
xJogMin          = 145          # x axis 
xJogSpeed        = 146          # x axis 
xMaxSpeed        = 147          # x axis 
xMicroSteps      = 148          # x axis 
xMinSpeed        = 149          # x axis 
xMotorRatio      = 150          # x axis 
xMotorSteps      = 151          # x axis 
xParkLoc         = 152          # x axis 
xPitch           = 153          # x axis 
xProbeDist       = 154          # x axis 

# x axis position config

xSvPosition      = 155          # z axis 
xSvHomeOffset    = 156          # z axis 
xSvDROPosition   = 157          # x axis 
xSvDROOffset     = 158          # x axis 

# z axis config

zAccel           = 159          # z axis 
zBacklash        = 160          # z axis 
zDROInch         = 161          # z axis 
zInvDRO          = 162          # z axis 
zInvDir          = 163          # z axis 
zInvEnc          = 164          # z axis 
zInvMpg          = 165          # z axis 
zJogMax          = 166          # z axis 
zJogMin          = 167          # z axis 
zJogSpeed        = 168          # z axis 
zMaxSpeed        = 169          # z axis 
zMicroSteps      = 170          # z axis 
zMinSpeed        = 171          # z axis 
zMotorRatio      = 172          # z axis 
zMotorSteps      = 173          # z axis 
zParkLoc         = 174          # z axis 
zPitch           = 175          # z axis 
zProbeDist       = 176          # z axis 
zProbeSpeed      = 177          # z axis 

# z axis position config

zSvPosition      = 178          # z axis 
zSvHomeOffset    = 179          # z axis 
zSvDROPosition   = 180          # z axis 
zSvDROOffset     = 181          # z axis 

config = { \
    'faPasses' : 32,
    'cfgFreqMult' : 6,
    'spStepDrive' : 61,
    'faZRetract' : 43,
    'thZStart' : 87,
    'tpZFeed' : 109,
    'tuPasses' : 115,
    'zInvDir' : 163,
    'spMicroSteps' : 57,
    'jogXPos' : 46,
    'zJogSpeed' : 168,
    'jogZPos' : 48,
    'thAlternate' : 64,
    'jogInc' : 45,
    'tuAddFeed' : 113,
    'tpRPM' : 97,
    'faZStart' : 44,
    'tuZStart' : 129,
    'tpTaperSel' : 102,
    'thXTaper' : 84,
    'tpZRetract' : 111,
    'thXStart' : 83,
    'xHomeStart' : 139,
    'thSPInt' : 78,
    'zMaxSpeed' : 169,
    'cfgTestRPM' : 14,
    'xHomeLoc' : 137,
    'thSpring' : 79,
    'xHomeEnd' : 136,
    'cfgMPG' : 10,
    'xHomeBackoffDist' : 133,
    'xMinSpeed' : 149,
    'xHomeDir' : 134,
    'xMotorSteps' : 151,
    'faZFeed' : 42,
    'thAddFeed' : 63,
    'thXRetract' : 82,
    'xJogSpeed' : 146,
    'cuXRetract' : 24,
    'tpZStart' : 112,
    'cuToolWidth' : 21,
    'spJogMax' : 54,
    'tuRPM' : 117,
    'thLastFeedBtn' : 72,
    'cfgDraw' : 3,
    'faXFeed' : 38,
    'xSvDROPosition' : 157,
    'cfgXFreq' : 15,
    'tuSPInt' : 118,
    'cfgLCD' : 9,
    'xJogMax' : 144,
    'thHFactor' : 69,
    'thFirstFeed' : 67,
    'faAddFeed' : 31,
    'xJogMin' : 145,
    'faXEnd' : 37,
    'spJogMin' : 55,
    'xPitch' : 153,
    'xSvHomeOffset' : 156,
    'tpAngle' : 89,
    'faXStart' : 40,
    'cfgEncoder' : 4,
    'faSPInt' : 35,
    'tpSmallDiam' : 99,
    'tpXFinish' : 105,
    'zSvPosition' : 178,
    'tpAddFeed' : 88,
    'tpDeltaBtn' : 91,
    'tpPasses' : 95,
    'xHomeSpeed' : 138,
    'cfgCmdDis' : 0,
    'cfgDRO' : 2,
    'commPort' : 17,
    'thExitRev' : 66,
    'thZEnd' : 85,
    'thFirstFeedBtn' : 68,
    'zMinSpeed' : 171,
    'thRPM' : 77,
    'droZPos' : 30,
    'tpZDelta' : 108,
    'zSvHomeOffset' : 179,
    'xInvDRO' : 140,
    'tuSpring' : 119,
    'xMotorRatio' : 150,
    'tuInternal' : 114,
    'cfgDbgSave' : 1,
    'tpSmallDiamText' : 100,
    'thXDepth' : 81,
    'cuXEnd' : 22,
    'tuPause' : 116,
    'xProbeDist' : 154,
    'xMaxSpeed' : 147,
    'xDROInch' : 132,
    'xInvDir' : 141,
    'tuZFeed' : 127,
    'zInvEnc' : 164,
    'cuZRetract' : 27,
    'xHomeDist' : 135,
    'cfgPrbInv' : 11,
    'thPitch' : 76,
    'tpZLength' : 110,
    'cuXFeed' : 23,
    'zInvMpg' : 165,
    'thPasses' : 74,
    'spMotorSteps' : 59,
    'cuZStart' : 28,
    'zSvDROOffset' : 181,
    'zAccel' : 159,
    'tpXRetract' : 107,
    'cfgTestMode' : 13,
    'tpXFeed' : 104,
    'thPause' : 75,
    'xInvEnc' : 142,
    'spMinRPM' : 58,
    'tpSpring' : 101,
    'tuZEnd' : 126,
    'tuXFeed' : 124,
    'faSpring' : 36,
    'thInternal' : 70,
    'thZRetract' : 86,
    'thTPI' : 80,
    'tpXDelta' : 103,
    'tuXDiam1Text' : 123,
    'tpAngleBtn' : 90,
    'tpPause' : 96,
    'zBacklash' : 160,
    'cfgInvEncDir' : 8,
    'faPause' : 33,
    'faXRetract' : 39,
    'cuXStart' : 25,
    'cfgHomeInPlace' : 7,
    'xSvDROOffset' : 158,
    'zParkLoc' : 174,
    'faRPM' : 34,
    'spMaxRPM' : 56,
    'cfgFcy' : 5,
    'zMicroSteps' : 170,
    'thLastFeed' : 71,
    'zDROInch' : 161,
    'tuXRetract' : 125,
    'cuRPM' : 20,
    'xInvMpg' : 143,
    'tuZRetract' : 128,
    'tpSPInt' : 98,
    'spTestIndex' : 62,
    'zJogMin' : 167,
    'zMotorRatio' : 172,
    'zPitch' : 175,
    'spInvDir' : 52,
    'spJogAccelTime' : 53,
    'zSvDROPosition' : 180,
    'xBacklash' : 131,
    'mainPanel' : 49,
    'tpLargeDiam' : 93,
    'thAngle' : 65,
    'zMotorSteps' : 173,
    'jogXPosDiam' : 47,
    'cuZCutoff' : 26,
    'xAccel' : 130,
    'spAccelTime' : 51,
    'tpLargeDiamText' : 94,
    'zInvDRO' : 162,
    'cuPause' : 19,
    'commRate' : 18,
    'cfgXilinx' : 16,
    'spAccel' : 50,
    'zJogMax' : 166,
    'droXPos' : 29,
    'tuXDiam0Text' : 121,
    'tpXInFeed' : 106,
    'zProbeDist' : 176,
    'faZEnd' : 41,
    'xParkLoc' : 152,
    'xSvPosition' : 155,
    'spMotorTest' : 60,
    'xMicroSteps' : 148,
    'tpInternal' : 92,
    'cfgRemDbg' : 12,
    'thMM' : 73,
    'zProbeSpeed' : 177,
    'tuXDiam0' : 120,
    'tuXDiam1' : 122,
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
