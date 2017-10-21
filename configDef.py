# config table

# system config

cfgCmdDis        =   0          # config disable sending commands
cfgDbgSave       =   1          # config save debug info
cfgDRO           =   2          # config dro present
cfgDraw          =   3          # config draw paths
cfgEncoder       =   4          # config xilinx encoder counts per revolution
cfgExtDro        =   5          # config external digital readout
cfgFcy           =   6          # config microprocesssor clock frequency
cfgFreqMult      =   7          # config xilinx frequency multiplier
cfgHomeInPlace   =   8          # config home in place
cfgInvEncDir     =   9          # config xilinx invert encoder direction
cfgLCD           =  10          # config enable lcd
cfgMPG           =  11          # config enable manual pulse generator
cfgPrbInv        =  12          # config invert probe signal
cfgRemDbg        =  13          # config print remote debug info
cfgTaperCycleDist =  14         # config taper cycle distance
cfgTestMode      =  15          # conifg test mode
cfgTestRPM       =  16          # config xilinx test rpm value
cfgXFreq         =  17          # config xilinx frequency
cfgXilinx        =  18          # config xilinx interface present

# communications config

commPort         =  19          # comm port
commRate         =  20          # comm baud rate

# cutoff config

cuPause          =  21          # cutoff pause before cutting
cuRPM            =  22          # cutoff rpm
cuToolWidth      =  23          # cutoff tool width
cuXEnd           =  24          # cutoff x end
cuXFeed          =  25          # cutoff x feed
cuXRetract       =  26          # cutoff x retract
cuXStart         =  27          # cutoff x start
cuZCutoff        =  28          # cutoff offset to z cutoff
cuZRetract       =  29          # cutoff offset to z retract
cuZStart         =  30          # cutoff z location

# dro position

droXPos          =  31          # dro x position
droZPos          =  32          # dro z position

# external dro

extDroPort       =  33          # external dro port
extDroRate       =  34          # external dro baud Rate

# face config

faAddFeed        =  35          # face 
faPasses         =  36          # face 
faPause          =  37          # face pause before cutting
faRPM            =  38          # face 
faSPInt          =  39          # face 
faSpring         =  40          # face 
faXEnd           =  41          # face 
faXFeed          =  42          # face 
faXRetract       =  43          # face 
faXStart         =  44          # face 
faZEnd           =  45          # face 
faZFeed          =  46          # face 
faZRetract       =  47          # face 
faZStart         =  48          # face 

# jog config

jogInc           =  49          # jog 
jogXPos          =  50          # jog 
jogXPosDiam      =  51          # jog 
jogZPos          =  52          # jog 

# main panel

mainPanel        =  53          # name of main panel

# spindle config

spAccel          =  54          # spindle acceleration
spAccelTime      =  55          # spindle accelerationtime
spInvDir         =  56          # spindle invert direction
spJogAccelTime   =  57          # spindle jog acceleration time
spJogMax         =  58          # spindle jog max speed
spJogMin         =  59          # spindle jog min speed
spMaxRPM         =  60          # spindle jog max rpm
spMicroSteps     =  61          # spindle micro steps
spMinRPM         =  62          # spindle minimum rpm
spMotorSteps     =  63          # spindle motor stpes per revolution
spMotorTest      =  64          # use stepper drive to test motor
spStepDrive      =  65          # spindle stepper drive
spTestIndex      =  66          # spindle test generate internal index pulse

# threading config

thAddFeed        =  67          # thread 
thAlternate      =  68          # thread 
thAngle          =  69          # thread 
thExitRev        =  70          # thread 
thFirstFeed      =  71          # thread 
thFirstFeedBtn   =  72          # thread 
thHFactor        =  73          # thread 
thInternal       =  74          # thread 
thLastFeed       =  75          # thread 
thLastFeedBtn    =  76          # thread 
thMM             =  77          # thread 
thPasses         =  78          # thread 
thPause          =  79          # thread 
thPitch          =  80          # thread 
thRPM            =  81          # thread 
thSPInt          =  82          # thread 
thSpring         =  83          # thread 
thTPI            =  84          # thread 
thXDepth         =  85          # thread 
thXRetract       =  86          # thread 
thXStart         =  87          # thread 
thXTaper         =  88          # thread 
thZEnd           =  89          # thread 
thZRetract       =  90          # thread 
thZStart         =  91          # thread 

# taper config

tpAddFeed        =  92          # tp 
tpAngle          =  93          # tp 
tpAngleBtn       =  94          # tp 
tpDeltaBtn       =  95          # tp 
tpInternal       =  96          # tp 
tpLargeDiam      =  97          # tp 
tpLargeDiamText  =  98          # tp 
tpPasses         =  99          # tp 
tpPause          = 100          # tp 
tpRPM            = 101          # tp 
tpSPInt          = 102          # tp 
tpSmallDiam      = 103          # tp 
tpSmallDiamText  = 104          # tp 
tpSpring         = 105          # tp 
tpTaperSel       = 106          # tp 
tpXDelta         = 107          # tp 
tpXFeed          = 108          # tp 
tpXFinish        = 109          # tp 
tpXInFeed        = 110          # tp 
tpXRetract       = 111          # tp 
tpZDelta         = 112          # tp 
tpZFeed          = 113          # tp 
tpZLength        = 114          # tp 
tpZRetract       = 115          # tp 
tpZStart         = 116          # tp 

# turn config

tuAddFeed        = 117          # turn 
tuInternal       = 118          # turn internal
tuPasses         = 119          # turn 
tuPause          = 120          # turn 
tuRPM            = 121          # turn 
tuSPInt          = 122          # turn 
tuSpring         = 123          # turn 
tuXDiam0         = 124          # turn 
tuXDiam0Text     = 125          # turn 
tuXDiam1         = 126          # turn 
tuXDiam1Text     = 127          # turn 
tuXFeed          = 128          # turn 
tuXRetract       = 129          # turn 
tuZEnd           = 130          # turn 
tuZFeed          = 131          # turn 
tuZRetract       = 132          # turn 
tuZStart         = 133          # turn 

# x axis config

xAccel           = 134          # turn 
xBacklash        = 135          # turn 
xDROInch         = 136          # turn 
xHomeBackoffDist = 137          # x axis 
xHomeDir         = 138          # x axis 
xHomeDist        = 139          # x axis 
xHomeEnd         = 140          # x axis 
xHomeLoc         = 141          # x axis 
xHomeSpeed       = 142          # x axis 
xHomeStart       = 143          # x axis 
xInvDRO          = 144          # x axis 
xInvDir          = 145          # x axis 
xInvEnc          = 146          # x axis 
xInvMpg          = 147          # x axis 
xJogMax          = 148          # x axis 
xJogMin          = 149          # x axis 
xJogSpeed        = 150          # x axis 
xMaxSpeed        = 151          # x axis 
xMicroSteps      = 152          # x axis 
xMinSpeed        = 153          # x axis 
xMotorRatio      = 154          # x axis 
xMotorSteps      = 155          # x axis 
xParkLoc         = 156          # x axis 
xPitch           = 157          # x axis 
xProbeDist       = 158          # x axis 

# x axis position config

xSvPosition      = 159          # z axis 
xSvHomeOffset    = 160          # z axis 
xSvDROPosition   = 161          # x axis 
xSvDROOffset     = 162          # x axis 

# z axis config

zAccel           = 163          # z axis 
zBackInc         = 164          # z axis distance to go past for taking out backlash
zBacklash        = 165          # z axis 
zDROInch         = 166          # z axis 
zInvDRO          = 167          # z axis 
zInvDir          = 168          # z axis 
zInvEnc          = 169          # z axis 
zInvMpg          = 170          # z axis 
zJogMax          = 171          # z axis 
zJogMin          = 172          # z axis 
zJogSpeed        = 173          # z axis 
zMaxSpeed        = 174          # z axis 
zMicroSteps      = 175          # z axis 
zMinSpeed        = 176          # z axis 
zMotorRatio      = 177          # z axis 
zMotorSteps      = 178          # z axis 
zParkLoc         = 179          # z axis 
zPitch           = 180          # z axis 
zProbeDist       = 181          # z axis 
zProbeSpeed      = 182          # z axis 

# z axis position config

zSvPosition      = 183          # z axis 
zSvHomeOffset    = 184          # z axis 
zSvDROPosition   = 185          # z axis 
zSvDROOffset     = 186          # z axis 

config = { \
    'faPasses' : 36,
    'cfgFreqMult' : 7,
    'spStepDrive' : 65,
    'faZRetract' : 47,
    'thZStart' : 91,
    'tpZFeed' : 113,
    'tuPasses' : 119,
    'zInvDir' : 168,
    'spMicroSteps' : 61,
    'jogXPos' : 50,
    'zJogSpeed' : 173,
    'jogZPos' : 52,
    'thPause' : 79,
    'jogInc' : 49,
    'tuAddFeed' : 117,
    'tpRPM' : 101,
    'faZStart' : 48,
    'tuZStart' : 133,
    'tpTaperSel' : 106,
    'thXTaper' : 88,
    'tpZRetract' : 115,
    'thXStart' : 87,
    'xHomeStart' : 143,
    'thSPInt' : 82,
    'zMaxSpeed' : 174,
    'cfgTestRPM' : 16,
    'xHomeLoc' : 141,
    'thSpring' : 83,
    'xHomeEnd' : 140,
    'cfgMPG' : 11,
    'xHomeBackoffDist' : 137,
    'xMinSpeed' : 153,
    'xHomeDir' : 138,
    'xMotorSteps' : 155,
    'faZFeed' : 46,
    'thAddFeed' : 67,
    'droZPos' : 32,
    'xJogSpeed' : 150,
    'cuXRetract' : 26,
    'tpZStart' : 116,
    'cuToolWidth' : 23,
    'spJogMax' : 58,
    'tuRPM' : 121,
    'thLastFeedBtn' : 76,
    'cfgDraw' : 3,
    'faXFeed' : 42,
    'xSvDROPosition' : 161,
    'cfgXFreq' : 17,
    'tuSPInt' : 122,
    'cfgLCD' : 10,
    'extDroRate' : 34,
    'xJogMax' : 148,
    'thHFactor' : 73,
    'thFirstFeed' : 71,
    'faAddFeed' : 35,
    'xJogMin' : 149,
    'faXEnd' : 41,
    'spJogMin' : 59,
    'xPitch' : 157,
    'cfgExtDro' : 5,
    'xSvHomeOffset' : 160,
    'tpAngle' : 93,
    'faXStart' : 44,
    'cfgEncoder' : 4,
    'faSPInt' : 39,
    'tpSmallDiam' : 103,
    'tpXFinish' : 109,
    'zSvPosition' : 183,
    'tpAddFeed' : 92,
    'tpDeltaBtn' : 95,
    'tpPasses' : 99,
    'xHomeSpeed' : 142,
    'thXRetract' : 86,
    'cfgCmdDis' : 0,
    'cfgDRO' : 2,
    'commPort' : 19,
    'thExitRev' : 70,
    'thZEnd' : 89,
    'thFirstFeedBtn' : 72,
    'zMinSpeed' : 176,
    'thRPM' : 81,
    'tpZDelta' : 112,
    'zSvHomeOffset' : 184,
    'xInvDRO' : 144,
    'tuSpring' : 123,
    'xMotorRatio' : 154,
    'tuInternal' : 118,
    'cfgDbgSave' : 1,
    'tpSmallDiamText' : 104,
    'thXDepth' : 85,
    'cuXEnd' : 24,
    'tuPause' : 120,
    'xProbeDist' : 158,
    'xMaxSpeed' : 151,
    'xDROInch' : 136,
    'xInvDir' : 145,
    'tuZFeed' : 131,
    'zInvEnc' : 169,
    'cuZRetract' : 29,
    'xHomeDist' : 139,
    'cfgPrbInv' : 12,
    'thPitch' : 80,
    'tpZLength' : 114,
    'cuXFeed' : 25,
    'zInvMpg' : 170,
    'thPasses' : 78,
    'spMotorSteps' : 63,
    'cuZStart' : 30,
    'zSvDROOffset' : 186,
    'zAccel' : 163,
    'tpXRetract' : 111,
    'cfgTestMode' : 15,
    'tpXFeed' : 108,
    'thAlternate' : 68,
    'xInvEnc' : 146,
    'spMinRPM' : 62,
    'tpSpring' : 105,
    'tuZEnd' : 130,
    'tuXFeed' : 128,
    'faSpring' : 40,
    'thInternal' : 74,
    'thZRetract' : 90,
    'thTPI' : 84,
    'tpXDelta' : 107,
    'tuXDiam1Text' : 127,
    'tpAngleBtn' : 94,
    'tpPause' : 100,
    'zBacklash' : 165,
    'cfgInvEncDir' : 9,
    'faPause' : 37,
    'faXRetract' : 43,
    'cuXStart' : 27,
    'cfgHomeInPlace' : 8,
    'xSvDROOffset' : 162,
    'zParkLoc' : 179,
    'faRPM' : 38,
    'spMaxRPM' : 60,
    'cfgFcy' : 6,
    'zMicroSteps' : 175,
    'thLastFeed' : 75,
    'zDROInch' : 166,
    'tuXRetract' : 129,
    'extDroPort' : 33,
    'cuRPM' : 22,
    'xInvMpg' : 147,
    'tuZRetract' : 132,
    'tpSPInt' : 102,
    'spTestIndex' : 66,
    'zJogMin' : 172,
    'zMotorRatio' : 177,
    'zPitch' : 180,
    'spInvDir' : 56,
    'spJogAccelTime' : 57,
    'zBackInc' : 164,
    'zSvDROPosition' : 185,
    'xBacklash' : 135,
    'mainPanel' : 53,
    'tpLargeDiam' : 97,
    'thAngle' : 69,
    'zMotorSteps' : 178,
    'jogXPosDiam' : 51,
    'cuZCutoff' : 28,
    'xAccel' : 134,
    'spAccelTime' : 55,
    'tpLargeDiamText' : 98,
    'zInvDRO' : 167,
    'cuPause' : 21,
    'commRate' : 20,
    'cfgXilinx' : 18,
    'spAccel' : 54,
    'zJogMax' : 171,
    'droXPos' : 31,
    'tuXDiam0Text' : 125,
    'tpXInFeed' : 110,
    'zProbeDist' : 181,
    'faZEnd' : 45,
    'xParkLoc' : 156,
    'xSvPosition' : 159,
    'spMotorTest' : 64,
    'xMicroSteps' : 152,
    'cfgTaperCycleDist' : 14,
    'tpInternal' : 96,
    'cfgRemDbg' : 13,
    'thMM' : 77,
    'zProbeSpeed' : 182,
    'tuXDiam0' : 124,
    'tuXDiam1' : 126,
    }

configTable = ( \
    'cfgCmdDis',
    'cfgDbgSave',
    'cfgDRO',
    'cfgDraw',
    'cfgEncoder',
    'cfgExtDro',
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
    'zBackInc',
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
