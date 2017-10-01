# config table

# system config

cfgCmdDis        =   0          # config disable sending commands
cfgDbgSave       =   1          # config save debug info
cfgDRO           =   2          # config dro present
cfgDraw          =   3          # config draw paths
cfgEncoder       =   4          # config xilinx encoder counts per revolution
cfgFcy           =   5          # config microprocesssor clock frequency
cfgFreqMult      =   6          # config xilinx frequency multiplier
cfgInvEncDir     =   7          # config xilinx invert encoder direction
cfgLCD           =   8          # config enable lcd
cfgMPG           =   9          # config enable manual pulse generator
cfgPrbInv        =  10          # config invert probe signal
cfgRemDbg        =  11          # config print remote debug info
cfgTestMode      =  12          # conifg test mode
cfgTestRPM       =  13          # config xilinx test rpm value
cfgXFreq         =  14          # config xilinx frequency
cfgXilinx        =  15          # config xilinx interface present

# communications config

commPort         =  16          # comm port
commRate         =  17          # comm baud rate

# cutoff config

cuPause          =  18          # cutoff pause before cutting
cuRPM            =  19          # cutoff rpm
cuToolWidth      =  20          # cutoff tool width
cuXEnd           =  21          # cutoff x end
cuXFeed          =  22          # cutoff x feed
cuXRetract       =  23          # cutoff x retract
cuXStart         =  24          # cutoff x start
cuZCutoff        =  25          # cutoff offset to z cutoff
cuZRetract       =  26          # cutoff offset to z retract
cuZStart         =  27          # cutoff z location

# dro position

droXPos          =  28          # dro x position 
droZPos          =  29          # dro z position 

# face config

faAddFeed        =  30          # face 
faPasses         =  31          # face 
faPause          =  32          # face pause before cutting
faRPM            =  33          # face 
faSPInt          =  34          # face 
faSpring         =  35          # face 
faXEnd           =  36          # face 
faXFeed          =  37          # face 
faXRetract       =  38          # face 
faXStart         =  39          # face 
faZEnd           =  40          # face 
faZFeed          =  41          # face 
faZRetract       =  42          # face 
faZStart         =  43          # face 

# jog config

jogInc           =  44          # jog 
jogXPos          =  45          # jog 
jogXPosDiam      =  46          # jog 
jogZPos          =  47          # jog 

# main panel

mainPanel        =  48          # name of main panel

# spindle config

spAccel          =  49          # spindle acceleration
spAccelTime      =  50          # spindle accelerationtime
spInvDir         =  51          # spindle invert direction
spJogAccelTime   =  52          # spindle jog acceleration time
spJogMax         =  53          # spindle jog max speed
spJogMin         =  54          # spindle jog min speed
spMaxRPM         =  55          # spindle jog max rpm
spMicroSteps     =  56          # spindle micro steps
spMinRPM         =  57          # spindle minimum rpm
spMotorSteps     =  58          # spindle motor stpes per revolution
spStepDrive      =  59          # spindle stepper drive
spTestIndex      =  60          # spindle test generate internal index pulse

# threading config

thAddFeed        =  61          # thread 
thAlternate      =  62          # thread 
thAngle          =  63          # thread 
thExitRev        =  64          # thread 
thFirstFeed      =  65          # thread 
thFirstFeedBtn   =  66          # thread 
thHFactor        =  67          # thread 
thInternal       =  68          # thread 
thLastFeed       =  69          # thread 
thLastFeedBtn    =  70          # thread 
thMM             =  71          # thread 
thPasses         =  72          # thread 
thPause          =  73          # thread 
thPitch          =  74          # thread 
thRPM            =  75          # thread 
thSPInt          =  76          # thread 
thSpring         =  77          # thread 
thTPI            =  78          # thread 
thXDepth         =  79          # thread 
thXRetract       =  80          # thread 
thXStart         =  81          # thread 
thXTaper         =  82          # thread 
thZEnd           =  83          # thread 
thZRetract       =  84          # thread 
thZStart         =  85          # thread 

# taper config

tpAddFeed        =  86          # tp 
tpAngle          =  87          # tp 
tpAngleBtn       =  88          # tp 
tpDeltaBtn       =  89          # tp 
tpInternal       =  90          # tp 
tpLargeDiam      =  91          # tp 
tpLargeDiamText  =  92          # tp 
tpPasses         =  93          # tp 
tpPause          =  94          # tp 
tpRPM            =  95          # tp 
tpSPInt          =  96          # tp 
tpSmallDiam      =  97          # tp 
tpSmallDiamText  =  98          # tp 
tpSpring         =  99          # tp 
tpTaperSel       = 100          # tp 
tpXDelta         = 101          # tp 
tpXFeed          = 102          # tp 
tpXFinish        = 103          # tp 
tpXInFeed        = 104          # tp 
tpXRetract       = 105          # tp 
tpZDelta         = 106          # tp 
tpZFeed          = 107          # tp 
tpZLength        = 108          # tp 
tpZRetract       = 109          # tp 
tpZStart         = 110          # tp 

# turn config

tuAddFeed        = 111          # turn 
tuPasses         = 112          # turn 
tuPause          = 113          # turn 
tuRPM            = 114          # turn 
tuSPInt          = 115          # turn 
tuSpring         = 116          # turn 
tuXEnd           = 117          # turn 
tuXFeed          = 118          # turn 
tuXRetract       = 119          # turn 
tuXStart         = 120          # turn 
tuZEnd           = 121          # turn 
tuZFeed          = 122          # turn 
tuZRetract       = 123          # turn 
tuZStart         = 124          # turn 

# x axis config

xAccel           = 125          # turn 
xBacklash        = 126          # turn 
xDROInch         = 127          # turn 
xHomeBackoffDist = 128          # x axis 
xHomeDir         = 129          # x axis 
xHomeDist        = 130          # x axis 
xHomeEnd         = 131          # x axis 
xHomeLoc         = 132          # x axis 
xHomeSpeed       = 133          # x axis 
xHomeStart       = 134          # x axis 
xInvDRO          = 135          # x axis 
xInvDir          = 136          # x axis 
xInvEnc          = 137          # x axis 
xInvMpg          = 138          # x axis 
xJogMax          = 139          # x axis 
xJogMin          = 140          # x axis 
xJogSpeed        = 141          # x axis 
xMaxSpeed        = 142          # x axis 
xMicroSteps      = 143          # x axis 
xMinSpeed        = 144          # x axis 
xMotorRatio      = 145          # x axis 
xMotorSteps      = 146          # x axis 
xParkLoc         = 147          # x axis 
xPitch           = 148          # x axis 
xProbeDist       = 149          # x axis 

# x axis position config

xSvPosition      = 150          # z axis 
xSvHomeOffset    = 151          # z axis 
xSvDROPosition   = 152          # x axis 
xSvDROOffset     = 153          # x axis 

# z axis config

zAccel           = 154          # z axis 
zBacklash        = 155          # z axis 
zDROInch         = 156          # z axis 
zInvDRO          = 157          # z axis 
zInvDir          = 158          # z axis 
zInvEnc          = 159          # z axis 
zInvMpg          = 160          # z axis 
zJogMax          = 161          # z axis 
zJogMin          = 162          # z axis 
zJogSpeed        = 163          # z axis 
zMaxSpeed        = 164          # z axis 
zMicroSteps      = 165          # z axis 
zMinSpeed        = 166          # z axis 
zMotorRatio      = 167          # z axis 
zMotorSteps      = 168          # z axis 
zParkLoc         = 169          # z axis 
zPitch           = 170          # z axis 
zProbeDist       = 171          # z axis 
zProbeSpeed      = 172          # z axis 

# z axis position config

zSvPosition      = 173          # z axis 
zSvHomeOffset    = 174          # z axis 
zSvDROPosition   = 175          # z axis 
zSvDROOffset     = 176          # z axis 

config = { \
    'faPasses' : 31,
    'cfgFreqMult' : 6,
    'spStepDrive' : 59,
    'faZRetract' : 42,
    'thZStart' : 85,
    'tpZFeed' : 107,
    'tuPasses' : 112,
    'zInvDir' : 158,
    'spMicroSteps' : 56,
    'jogXPos' : 45,
    'zJogSpeed' : 163,
    'jogZPos' : 47,
    'thAlternate' : 62,
    'jogInc' : 44,
    'tuAddFeed' : 111,
    'tpRPM' : 95,
    'faZStart' : 43,
    'tuZStart' : 124,
    'tpTaperSel' : 100,
    'thXTaper' : 82,
    'tpZRetract' : 109,
    'thXStart' : 81,
    'xHomeStart' : 134,
    'thSPInt' : 76,
    'zMaxSpeed' : 164,
    'cfgTestRPM' : 13,
    'xHomeLoc' : 132,
    'thSpring' : 77,
    'xHomeEnd' : 131,
    'cfgMPG' : 9,
    'xHomeBackoffDist' : 128,
    'xMinSpeed' : 144,
    'xHomeDir' : 129,
    'xMotorSteps' : 146,
    'faZFeed' : 41,
    'thAddFeed' : 61,
    'thXRetract' : 80,
    'xJogSpeed' : 141,
    'cuXRetract' : 23,
    'tpZStart' : 110,
    'cuToolWidth' : 20,
    'spJogMax' : 53,
    'tuRPM' : 114,
    'thLastFeedBtn' : 70,
    'cfgDraw' : 3,
    'faXFeed' : 37,
    'xSvDROPosition' : 152,
    'cfgXFreq' : 14,
    'tuSPInt' : 115,
    'cfgLCD' : 8,
    'xJogMax' : 139,
    'thHFactor' : 67,
    'thFirstFeed' : 65,
    'faAddFeed' : 30,
    'xJogMin' : 140,
    'faXEnd' : 36,
    'spJogMin' : 54,
    'xPitch' : 148,
    'xSvHomeOffset' : 151,
    'tpAngle' : 87,
    'faXStart' : 39,
    'cfgEncoder' : 4,
    'faSPInt' : 34,
    'tpSmallDiam' : 97,
    'tpXFinish' : 103,
    'zSvPosition' : 173,
    'tpAddFeed' : 86,
    'tpDeltaBtn' : 89,
    'tpPasses' : 93,
    'xHomeSpeed' : 133,
    'cfgCmdDis' : 0,
    'cfgDRO' : 2,
    'commPort' : 16,
    'thExitRev' : 64,
    'thZEnd' : 83,
    'thFirstFeedBtn' : 66,
    'zMinSpeed' : 166,
    'thRPM' : 75,
    'droZPos' : 29,
    'tpZDelta' : 106,
    'zSvHomeOffset' : 174,
    'xInvDRO' : 135,
    'tuSpring' : 116,
    'xMotorRatio' : 145,
    'tuXFeed' : 118,
    'cfgDbgSave' : 1,
    'tpSmallDiamText' : 98,
    'thXDepth' : 79,
    'cuXEnd' : 21,
    'tuPause' : 113,
    'xProbeDist' : 149,
    'xMaxSpeed' : 142,
    'xDROInch' : 127,
    'xInvDir' : 136,
    'tuZFeed' : 122,
    'zInvEnc' : 159,
    'cuZRetract' : 26,
    'xHomeDist' : 130,
    'cfgPrbInv' : 10,
    'thPitch' : 74,
    'tpZLength' : 108,
    'cuXFeed' : 22,
    'zInvMpg' : 160,
    'thPasses' : 72,
    'spMotorSteps' : 58,
    'cuZStart' : 27,
    'zSvDROOffset' : 176,
    'zAccel' : 154,
    'tpXRetract' : 105,
    'cfgTestMode' : 12,
    'tpXFeed' : 102,
    'thPause' : 73,
    'xInvEnc' : 137,
    'spMinRPM' : 57,
    'tpSpring' : 99,
    'tuZEnd' : 121,
    'faSpring' : 35,
    'thInternal' : 68,
    'thZRetract' : 84,
    'thTPI' : 78,
    'tpXDelta' : 101,
    'zMotorSteps' : 168,
    'tuXEnd' : 117,
    'tpAngleBtn' : 88,
    'tpPause' : 94,
    'zBacklash' : 155,
    'cfgInvEncDir' : 7,
    'faPause' : 32,
    'faXRetract' : 38,
    'cuXStart' : 24,
    'xSvDROOffset' : 153,
    'zParkLoc' : 169,
    'faRPM' : 33,
    'spMaxRPM' : 55,
    'cfgFcy' : 5,
    'zMicroSteps' : 165,
    'thLastFeed' : 69,
    'zDROInch' : 156,
    'tuXRetract' : 119,
    'cuRPM' : 19,
    'xInvMpg' : 138,
    'tuZRetract' : 123,
    'tpSPInt' : 96,
    'spTestIndex' : 60,
    'zJogMin' : 162,
    'zMotorRatio' : 167,
    'zPitch' : 170,
    'spInvDir' : 51,
    'spJogAccelTime' : 52,
    'zSvDROPosition' : 175,
    'xBacklash' : 126,
    'mainPanel' : 48,
    'tpLargeDiam' : 91,
    'thAngle' : 63,
    'tuXStart' : 120,
    'jogXPosDiam' : 46,
    'cuZCutoff' : 25,
    'xAccel' : 125,
    'spAccelTime' : 50,
    'tpLargeDiamText' : 92,
    'zInvDRO' : 157,
    'cuPause' : 18,
    'commRate' : 17,
    'cfgXilinx' : 15,
    'spAccel' : 49,
    'zJogMax' : 161,
    'droXPos' : 28,
    'tpXInFeed' : 104,
    'zProbeDist' : 171,
    'faZEnd' : 40,
    'xParkLoc' : 147,
    'xSvPosition' : 150,
    'xMicroSteps' : 143,
    'tpInternal' : 90,
    'cfgRemDbg' : 11,
    'thMM' : 71,
    'zProbeSpeed' : 172,
    }

configTable = ( \
    'cfgCmdDis',
    'cfgDbgSave',
    'cfgDRO',
    'cfgDraw',
    'cfgEncoder',
    'cfgFcy',
    'cfgFreqMult',
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
    'tuPasses',
    'tuPause',
    'tuRPM',
    'tuSPInt',
    'tuSpring',
    'tuXEnd',
    'tuXFeed',
    'tuXRetract',
    'tuXStart',
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
