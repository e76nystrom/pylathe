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
spMotorTest      =  59          # use stepper drive to test motor
spStepDrive      =  60          # spindle stepper drive
spTestIndex      =  61          # spindle test generate internal index pulse

# threading config

thAddFeed        =  62          # thread 
thAlternate      =  63          # thread 
thAngle          =  64          # thread 
thExitRev        =  65          # thread 
thFirstFeed      =  66          # thread 
thFirstFeedBtn   =  67          # thread 
thHFactor        =  68          # thread 
thInternal       =  69          # thread 
thLastFeed       =  70          # thread 
thLastFeedBtn    =  71          # thread 
thMM             =  72          # thread 
thPasses         =  73          # thread 
thPause          =  74          # thread 
thPitch          =  75          # thread 
thRPM            =  76          # thread 
thSPInt          =  77          # thread 
thSpring         =  78          # thread 
thTPI            =  79          # thread 
thXDepth         =  80          # thread 
thXRetract       =  81          # thread 
thXStart         =  82          # thread 
thXTaper         =  83          # thread 
thZEnd           =  84          # thread 
thZRetract       =  85          # thread 
thZStart         =  86          # thread 

# taper config

tpAddFeed        =  87          # tp 
tpAngle          =  88          # tp 
tpAngleBtn       =  89          # tp 
tpDeltaBtn       =  90          # tp 
tpInternal       =  91          # tp 
tpLargeDiam      =  92          # tp 
tpLargeDiamText  =  93          # tp 
tpPasses         =  94          # tp 
tpPause          =  95          # tp 
tpRPM            =  96          # tp 
tpSPInt          =  97          # tp 
tpSmallDiam      =  98          # tp 
tpSmallDiamText  =  99          # tp 
tpSpring         = 100          # tp 
tpTaperSel       = 101          # tp 
tpXDelta         = 102          # tp 
tpXFeed          = 103          # tp 
tpXFinish        = 104          # tp 
tpXInFeed        = 105          # tp 
tpXRetract       = 106          # tp 
tpZDelta         = 107          # tp 
tpZFeed          = 108          # tp 
tpZLength        = 109          # tp 
tpZRetract       = 110          # tp 
tpZStart         = 111          # tp 

# turn config

tuAddFeed        = 112          # turn 
tuPasses         = 113          # turn 
tuPause          = 114          # turn 
tuRPM            = 115          # turn 
tuSPInt          = 116          # turn 
tuSpring         = 117          # turn 
tuXEnd           = 118          # turn 
tuXFeed          = 119          # turn 
tuXRetract       = 120          # turn 
tuXStart         = 121          # turn 
tuZEnd           = 122          # turn 
tuZFeed          = 123          # turn 
tuZRetract       = 124          # turn 
tuZStart         = 125          # turn 

# x axis config

xAccel           = 126          # turn 
xBacklash        = 127          # turn 
xDROInch         = 128          # turn 
xHomeBackoffDist = 129          # x axis 
xHomeDir         = 130          # x axis 
xHomeDist        = 131          # x axis 
xHomeEnd         = 132          # x axis 
xHomeLoc         = 133          # x axis 
xHomeSpeed       = 134          # x axis 
xHomeStart       = 135          # x axis 
xInvDRO          = 136          # x axis 
xInvDir          = 137          # x axis 
xInvEnc          = 138          # x axis 
xInvMpg          = 139          # x axis 
xJogMax          = 140          # x axis 
xJogMin          = 141          # x axis 
xJogSpeed        = 142          # x axis 
xMaxSpeed        = 143          # x axis 
xMicroSteps      = 144          # x axis 
xMinSpeed        = 145          # x axis 
xMotorRatio      = 146          # x axis 
xMotorSteps      = 147          # x axis 
xParkLoc         = 148          # x axis 
xPitch           = 149          # x axis 
xProbeDist       = 150          # x axis 

# x axis position config

xSvPosition      = 151          # z axis 
xSvHomeOffset    = 152          # z axis 
xSvDROPosition   = 153          # x axis 
xSvDROOffset     = 154          # x axis 

# z axis config

zAccel           = 155          # z axis 
zBacklash        = 156          # z axis 
zDROInch         = 157          # z axis 
zInvDRO          = 158          # z axis 
zInvDir          = 159          # z axis 
zInvEnc          = 160          # z axis 
zInvMpg          = 161          # z axis 
zJogMax          = 162          # z axis 
zJogMin          = 163          # z axis 
zJogSpeed        = 164          # z axis 
zMaxSpeed        = 165          # z axis 
zMicroSteps      = 166          # z axis 
zMinSpeed        = 167          # z axis 
zMotorRatio      = 168          # z axis 
zMotorSteps      = 169          # z axis 
zParkLoc         = 170          # z axis 
zPitch           = 171          # z axis 
zProbeDist       = 172          # z axis 
zProbeSpeed      = 173          # z axis 

# z axis position config

zSvPosition      = 174          # z axis 
zSvHomeOffset    = 175          # z axis 
zSvDROPosition   = 176          # z axis 
zSvDROOffset     = 177          # z axis 

config = { \
    'faPasses' : 31,
    'cfgFreqMult' : 6,
    'spStepDrive' : 60,
    'faZRetract' : 42,
    'thZStart' : 86,
    'tpZFeed' : 108,
    'tuPasses' : 113,
    'zInvDir' : 159,
    'spMicroSteps' : 56,
    'jogXPos' : 45,
    'zJogSpeed' : 164,
    'jogZPos' : 47,
    'thAlternate' : 63,
    'jogInc' : 44,
    'tuAddFeed' : 112,
    'tpRPM' : 96,
    'faZStart' : 43,
    'tuZStart' : 125,
    'tpTaperSel' : 101,
    'thXTaper' : 83,
    'tpZRetract' : 110,
    'thXStart' : 82,
    'xHomeStart' : 135,
    'thSPInt' : 77,
    'zMaxSpeed' : 165,
    'cfgTestRPM' : 13,
    'xHomeLoc' : 133,
    'thSpring' : 78,
    'xHomeEnd' : 132,
    'cfgMPG' : 9,
    'xHomeBackoffDist' : 129,
    'xMinSpeed' : 145,
    'xHomeDir' : 130,
    'xMotorSteps' : 147,
    'faZFeed' : 41,
    'thAddFeed' : 62,
    'thXRetract' : 81,
    'xJogSpeed' : 142,
    'cuXRetract' : 23,
    'tpZStart' : 111,
    'cuToolWidth' : 20,
    'spJogMax' : 53,
    'tuRPM' : 115,
    'thLastFeedBtn' : 71,
    'cfgDraw' : 3,
    'faXFeed' : 37,
    'xSvDROPosition' : 153,
    'cfgXFreq' : 14,
    'tuSPInt' : 116,
    'cfgLCD' : 8,
    'xJogMax' : 140,
    'thHFactor' : 68,
    'thFirstFeed' : 66,
    'faAddFeed' : 30,
    'xJogMin' : 141,
    'faXEnd' : 36,
    'spJogMin' : 54,
    'xPitch' : 149,
    'xSvHomeOffset' : 152,
    'tpAngle' : 88,
    'faXStart' : 39,
    'cfgEncoder' : 4,
    'faSPInt' : 34,
    'tpSmallDiam' : 98,
    'tpXFinish' : 104,
    'zSvPosition' : 174,
    'tpAddFeed' : 87,
    'tpDeltaBtn' : 90,
    'tpPasses' : 94,
    'xHomeSpeed' : 134,
    'cfgCmdDis' : 0,
    'cfgDRO' : 2,
    'commPort' : 16,
    'thExitRev' : 65,
    'thZEnd' : 84,
    'thFirstFeedBtn' : 67,
    'zMinSpeed' : 167,
    'thRPM' : 76,
    'droZPos' : 29,
    'tpZDelta' : 107,
    'zSvHomeOffset' : 175,
    'xInvDRO' : 136,
    'tuSpring' : 117,
    'xMotorRatio' : 146,
    'tuXFeed' : 119,
    'cfgDbgSave' : 1,
    'tpSmallDiamText' : 99,
    'thXDepth' : 80,
    'cuXEnd' : 21,
    'tuPause' : 114,
    'xProbeDist' : 150,
    'xMaxSpeed' : 143,
    'xDROInch' : 128,
    'xInvDir' : 137,
    'tuZFeed' : 123,
    'zInvEnc' : 160,
    'cuZRetract' : 26,
    'xHomeDist' : 131,
    'cfgPrbInv' : 10,
    'thPitch' : 75,
    'tpZLength' : 109,
    'cuXFeed' : 22,
    'zInvMpg' : 161,
    'thPasses' : 73,
    'spMotorSteps' : 58,
    'cuZStart' : 27,
    'zSvDROOffset' : 177,
    'zAccel' : 155,
    'tpXRetract' : 106,
    'cfgTestMode' : 12,
    'tpXFeed' : 103,
    'thPause' : 74,
    'xInvEnc' : 138,
    'spMinRPM' : 57,
    'tpSpring' : 100,
    'tuZEnd' : 122,
    'faSpring' : 35,
    'thInternal' : 69,
    'thZRetract' : 85,
    'thTPI' : 79,
    'tpXDelta' : 102,
    'zMotorSteps' : 169,
    'tuXEnd' : 118,
    'tpAngleBtn' : 89,
    'tpPause' : 95,
    'zBacklash' : 156,
    'cfgInvEncDir' : 7,
    'faPause' : 32,
    'faXRetract' : 38,
    'cuXStart' : 24,
    'xSvDROOffset' : 154,
    'zParkLoc' : 170,
    'faRPM' : 33,
    'spMaxRPM' : 55,
    'cfgFcy' : 5,
    'zMicroSteps' : 166,
    'thLastFeed' : 70,
    'zDROInch' : 157,
    'tuXRetract' : 120,
    'cuRPM' : 19,
    'xInvMpg' : 139,
    'tuZRetract' : 124,
    'tpSPInt' : 97,
    'spTestIndex' : 61,
    'zJogMin' : 163,
    'zMotorRatio' : 168,
    'zPitch' : 171,
    'spInvDir' : 51,
    'spJogAccelTime' : 52,
    'zSvDROPosition' : 176,
    'xBacklash' : 127,
    'mainPanel' : 48,
    'tpLargeDiam' : 92,
    'thAngle' : 64,
    'tuXStart' : 121,
    'jogXPosDiam' : 46,
    'cuZCutoff' : 25,
    'xAccel' : 126,
    'spAccelTime' : 50,
    'tpLargeDiamText' : 93,
    'zInvDRO' : 158,
    'cuPause' : 18,
    'commRate' : 17,
    'cfgXilinx' : 15,
    'spAccel' : 49,
    'zJogMax' : 162,
    'droXPos' : 28,
    'tpXInFeed' : 105,
    'zProbeDist' : 172,
    'faZEnd' : 40,
    'xParkLoc' : 148,
    'xSvPosition' : 151,
    'spMotorTest' : 59,
    'xMicroSteps' : 144,
    'tpInternal' : 91,
    'cfgRemDbg' : 11,
    'thMM' : 72,
    'zProbeSpeed' : 173,
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
