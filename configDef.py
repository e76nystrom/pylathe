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

# jog panel config

jpSurfaceSpeed   =  53          # jogpanle fpm or rpm
jpXDroDiam       =  54          # jogpanel x dro diameter

# main panel

mainPanel        =  55          # name of main panel

# spindle config

spAccel          =  56          # spindle acceleration
spAccelTime      =  57          # spindle accelerationtime
spInvDir         =  58          # spindle invert direction
spJogAccelTime   =  59          # spindle jog acceleration time
spJogMax         =  60          # spindle jog max speed
spJogMin         =  61          # spindle jog min speed
spMaxRPM         =  62          # spindle jog max rpm
spMicroSteps     =  63          # spindle micro steps
spMinRPM         =  64          # spindle minimum rpm
spMotorSteps     =  65          # spindle motor stpes per revolution
spMotorTest      =  66          # use stepper drive to test motor
spStepDrive      =  67          # spindle stepper drive
spTestIndex      =  68          # spindle test generate internal index pulse

# threading config

thAddFeed        =  69          # thread feed to add after done
thAlternate      =  70          # thread althernate thread flanks
thAngle          =  71          # thread hanlf angle of thread
thFirstFeed      =  72          # thread first feed for thread area calc
thFirstFeedBtn   =  73          # thread button to select first feed
thInternal       =  74          # thread internal threads
thLastFeed       =  75          # thread last feed for thread area calculation
thLastFeedBtn    =  76          # thread button to select last feed
thLeftHand       =  77          # thread left hand 
thMM             =  78          # thread button for mm
thPasses         =  79          # thread number of passes
thPause          =  80          # thread pause between passes
thRPM            =  81          # thread speed for threading operation
thRunout         =  82          # thread runout for rh exit or lh entrance
thSPInt          =  83          # thread spring pass interval
thSpring         =  84          # thread number of spring passes at end
thTPI            =  85          # thread select thread in threads per inch
thThread         =  86          # thread field containing tpi or pitch
thXDepth         =  87          # thread x depth of thread
thXRetract       =  88          # thread x retract
thXStart         =  89          # thread x diameter
thXTaper         =  90          # thread x taper
thZEnd           =  91          # thread z end of thread
thZRetract       =  92          # thread z retract
thZStart         =  93          # thread z start

# taper config

tpAddFeed        =  94          # tp 
tpAngle          =  95          # tp 
tpAngleBtn       =  96          # tp 
tpDeltaBtn       =  97          # tp 
tpInternal       =  98          # tp 
tpLargeDiam      =  99          # tp 
tpLargeDiamText  = 100          # tp 
tpPasses         = 101          # tp 
tpPause          = 102          # tp 
tpRPM            = 103          # tp 
tpSPInt          = 104          # tp 
tpSmallDiam      = 105          # tp 
tpSmallDiamText  = 106          # tp 
tpSpring         = 107          # tp 
tpTaperSel       = 108          # tp 
tpXDelta         = 109          # tp 
tpXFeed          = 110          # tp 
tpXFinish        = 111          # tp 
tpXInFeed        = 112          # tp 
tpXRetract       = 113          # tp 
tpZDelta         = 114          # tp 
tpZFeed          = 115          # tp 
tpZLength        = 116          # tp 
tpZRetract       = 117          # tp 
tpZStart         = 118          # tp 

# turn config

tuAddFeed        = 119          # turn 
tuInternal       = 120          # turn internal
tuPasses         = 121          # turn 
tuPause          = 122          # turn 
tuRPM            = 123          # turn 
tuSPInt          = 124          # turn 
tuSpring         = 125          # turn 
tuXDiam0         = 126          # turn 
tuXDiam0Text     = 127          # turn 
tuXDiam1         = 128          # turn 
tuXDiam1Text     = 129          # turn 
tuXFeed          = 130          # turn 
tuXRetract       = 131          # turn 
tuZEnd           = 132          # turn 
tuZFeed          = 133          # turn 
tuZRetract       = 134          # turn 
tuZStart         = 135          # turn 

# x axis config

xAccel           = 136          # x axis 
xBacklash        = 137          # x axis 
xDROInch         = 138          # x axis 
xHomeBackoffDist = 139          # x axis 
xHomeDir         = 140          # x axis 
xHomeDist        = 141          # x axis 
xHomeEnd         = 142          # x axis 
xHomeLoc         = 143          # x axis 
xHomeSpeed       = 144          # x axis 
xHomeStart       = 145          # x axis 
xInvDRO          = 146          # x axis invert dro
xInvDir          = 147          # x axis invert stepper direction
xInvEnc          = 148          # x axis 
xInvMpg          = 149          # x axis invert mpg direction
xJogMax          = 150          # x axis 
xJogMin          = 151          # x axis 
xJogSpeed        = 152          # x axis 
xMaxSpeed        = 153          # x axis 
xMicroSteps      = 154          # x axis 
xMinSpeed        = 155          # x axis 
xMotorRatio      = 156          # x axis 
xMotorSteps      = 157          # x axis 
xParkLoc         = 158          # x axis 
xPitch           = 159          # x axis 
xProbeDist       = 160          # x axis 

# x axis position config

xSvPosition      = 161          # z axis 
xSvHomeOffset    = 162          # z axis 
xSvDROPosition   = 163          # x axis 
xSvDROOffset     = 164          # x axis 

# z axis config

zAccel           = 165          # z axis 
zBackInc         = 166          # z axis distance to go past for taking out backlash
zBacklash        = 167          # z axis 
zDROInch         = 168          # z axis 
zInvDRO          = 169          # z axis 
zInvDir          = 170          # z axis 
zInvEnc          = 171          # z axis 
zInvMpg          = 172          # z axis 
zJogMax          = 173          # z axis 
zJogMin          = 174          # z axis 
zJogSpeed        = 175          # z axis 
zMaxSpeed        = 176          # z axis 
zMicroSteps      = 177          # z axis 
zMinSpeed        = 178          # z axis 
zMotorRatio      = 179          # z axis 
zMotorSteps      = 180          # z axis 
zParkLoc         = 181          # z axis 
zPitch           = 182          # z axis 
zProbeDist       = 183          # z axis 
zProbeSpeed      = 184          # z axis 

# z axis position config

zSvPosition      = 185          # z axis 
zSvHomeOffset    = 186          # z axis 
zSvDROPosition   = 187          # z axis 
zSvDROOffset     = 188          # z axis 

config = { \
    'faPasses' : 36,
    'cfgFreqMult' : 7,
    'spStepDrive' : 67,
    'faZRetract' : 47,
    'thZStart' : 93,
    'tpZFeed' : 115,
    'tuPasses' : 121,
    'zInvDir' : 170,
    'spMicroSteps' : 63,
    'jogXPos' : 50,
    'zJogSpeed' : 175,
    'jogZPos' : 52,
    'thPause' : 80,
    'jogInc' : 49,
    'tuAddFeed' : 119,
    'tpRPM' : 103,
    'faZStart' : 48,
    'tuZStart' : 135,
    'tpTaperSel' : 108,
    'thXTaper' : 90,
    'tpZRetract' : 117,
    'thXStart' : 89,
    'xHomeStart' : 145,
    'thSPInt' : 83,
    'zMaxSpeed' : 176,
    'cfgTestRPM' : 16,
    'xHomeLoc' : 143,
    'thSpring' : 84,
    'xHomeEnd' : 142,
    'cfgMPG' : 11,
    'xHomeBackoffDist' : 139,
    'xMinSpeed' : 155,
    'xHomeDir' : 140,
    'xMotorSteps' : 157,
    'faZFeed' : 46,
    'thAddFeed' : 69,
    'thRunout' : 82,
    'xJogSpeed' : 152,
    'cuXRetract' : 26,
    'tpZStart' : 118,
    'cuToolWidth' : 23,
    'spJogMax' : 60,
    'tuRPM' : 123,
    'thLastFeedBtn' : 76,
    'cfgDraw' : 3,
    'faXFeed' : 42,
    'xSvDROPosition' : 163,
    'cfgXFreq' : 17,
    'tuSPInt' : 124,
    'cfgLCD' : 10,
    'extDroRate' : 34,
    'xJogMax' : 150,
    'tpXInFeed' : 112,
    'thFirstFeed' : 72,
    'faAddFeed' : 35,
    'xJogMin' : 151,
    'faXEnd' : 41,
    'spJogMin' : 61,
    'xPitch' : 159,
    'cfgExtDro' : 5,
    'xSvHomeOffset' : 162,
    'tpAngle' : 95,
    'faXStart' : 44,
    'cfgEncoder' : 4,
    'faSPInt' : 39,
    'tpXFinish' : 111,
    'zSvPosition' : 185,
    'tpAddFeed' : 94,
    'tpDeltaBtn' : 97,
    'thLeftHand' : 77,
    'tpPasses' : 101,
    'xHomeSpeed' : 144,
    'thXRetract' : 88,
    'cfgCmdDis' : 0,
    'cfgDRO' : 2,
    'commPort' : 19,
    'droZPos' : 32,
    'thZEnd' : 91,
    'thFirstFeedBtn' : 73,
    'zMinSpeed' : 178,
    'thRPM' : 81,
    'tpZDelta' : 114,
    'zSvHomeOffset' : 186,
    'xInvDRO' : 146,
    'tuSpring' : 125,
    'xMotorRatio' : 156,
    'tuInternal' : 120,
    'thThread' : 86,
    'cfgDbgSave' : 1,
    'tpSmallDiamText' : 106,
    'thXDepth' : 87,
    'cuXEnd' : 24,
    'tuPause' : 122,
    'xProbeDist' : 160,
    'xMaxSpeed' : 153,
    'xDROInch' : 138,
    'xInvDir' : 147,
    'tuZFeed' : 133,
    'zInvEnc' : 171,
    'cuZRetract' : 29,
    'xHomeDist' : 141,
    'cfgPrbInv' : 12,
    'tpSmallDiam' : 105,
    'tpZLength' : 116,
    'cuXFeed' : 25,
    'zInvMpg' : 172,
    'thPasses' : 79,
    'spMotorSteps' : 65,
    'cuZStart' : 30,
    'zSvDROOffset' : 188,
    'zAccel' : 165,
    'tpXRetract' : 113,
    'cfgTestMode' : 15,
    'tpXFeed' : 110,
    'thAlternate' : 70,
    'xInvEnc' : 148,
    'spMinRPM' : 64,
    'tpSpring' : 107,
    'tuZEnd' : 132,
    'tuXFeed' : 130,
    'faSpring' : 40,
    'thInternal' : 74,
    'thZRetract' : 92,
    'thTPI' : 85,
    'tpXDelta' : 109,
    'tuXDiam1Text' : 129,
    'tpAngleBtn' : 96,
    'tpPause' : 102,
    'zBacklash' : 167,
    'cfgInvEncDir' : 9,
    'faPause' : 37,
    'faXRetract' : 43,
    'cuXStart' : 27,
    'cfgHomeInPlace' : 8,
    'jpSurfaceSpeed' : 53,
    'xSvDROOffset' : 164,
    'zParkLoc' : 181,
    'faRPM' : 38,
    'spMaxRPM' : 62,
    'cfgFcy' : 6,
    'zMicroSteps' : 177,
    'thLastFeed' : 75,
    'zDROInch' : 168,
    'tuXRetract' : 131,
    'extDroPort' : 33,
    'cuRPM' : 22,
    'xInvMpg' : 149,
    'tuZRetract' : 134,
    'tpSPInt' : 104,
    'spTestIndex' : 68,
    'zJogMin' : 174,
    'zMotorRatio' : 179,
    'zPitch' : 182,
    'spInvDir' : 58,
    'spJogAccelTime' : 59,
    'zBackInc' : 166,
    'zSvDROPosition' : 187,
    'xBacklash' : 137,
    'mainPanel' : 55,
    'tpLargeDiam' : 99,
    'thAngle' : 71,
    'zMotorSteps' : 180,
    'jogXPosDiam' : 51,
    'cuZCutoff' : 28,
    'xAccel' : 136,
    'spAccelTime' : 57,
    'tpLargeDiamText' : 100,
    'zInvDRO' : 169,
    'cuPause' : 21,
    'commRate' : 20,
    'cfgXilinx' : 18,
    'spAccel' : 56,
    'zJogMax' : 173,
    'droXPos' : 31,
    'tuXDiam0Text' : 127,
    'zProbeDist' : 183,
    'faZEnd' : 45,
    'xParkLoc' : 158,
    'xSvPosition' : 161,
    'jpXDroDiam' : 54,
    'spMotorTest' : 66,
    'xMicroSteps' : 154,
    'cfgTaperCycleDist' : 14,
    'tpInternal' : 98,
    'cfgRemDbg' : 13,
    'thMM' : 78,
    'zProbeSpeed' : 184,
    'tuXDiam0' : 126,
    'tuXDiam1' : 128,
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
    'jpSurfaceSpeed',
    'jpXDroDiam',
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
