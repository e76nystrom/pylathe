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
cfgSpEncoder     =  14          # config spindle encoder
cfgTaperCycleDist =  15         # config taper cycle distance
cfgTestMode      =  16          # conifg test mode
cfgTestRPM       =  17          # config xilinx test rpm value
cfgXFreq         =  18          # config xilinx frequency
cfgXilinx        =  19          # config xilinx interface present

# communications config

commPort         =  20          # comm port
commRate         =  21          # comm baud rate

# cutoff config

cuPause          =  22          # cutoff pause before cutting
cuRPM            =  23          # cutoff rpm
cuToolWidth      =  24          # cutoff tool width
cuXEnd           =  25          # cutoff x end
cuXFeed          =  26          # cutoff x feed
cuXRetract       =  27          # cutoff x retract
cuXStart         =  28          # cutoff x start
cuZCutoff        =  29          # cutoff offset to z cutoff
cuZRetract       =  30          # cutoff offset to z retract
cuZStart         =  31          # cutoff z location

# dro position

droXPos          =  32          # dro x position
droZPos          =  33          # dro z position

# external dro

extDroPort       =  34          # external dro port
extDroRate       =  35          # external dro baud Rate

# face config

faAddFeed        =  36          # face 
faPasses         =  37          # face 
faPause          =  38          # face pause before cutting
faRPM            =  39          # face 
faSPInt          =  40          # face 
faSpring         =  41          # face 
faXEnd           =  42          # face 
faXFeed          =  43          # face 
faXRetract       =  44          # face 
faXStart         =  45          # face 
faZEnd           =  46          # face 
faZFeed          =  47          # face 
faZRetract       =  48          # face 
faZStart         =  49          # face 

# jog config

jogInc           =  50          # jog 
jogXPos          =  51          # jog 
jogXPosDiam      =  52          # jog 
jogZPos          =  53          # jog 

# jog panel config

jpSurfaceSpeed   =  54          # jogpanle fpm or rpm
jpXDroDiam       =  55          # jogpanel x dro diameter

# main panel

mainPanel        =  56          # name of main panel

# spindle config

spAccel          =  57          # spindle acceleration
spAccelTime      =  58          # spindle accelerationtime
spInvDir         =  59          # spindle invert direction
spJogAccelTime   =  60          # spindle jog acceleration time
spJogMax         =  61          # spindle jog max speed
spJogMin         =  62          # spindle jog min speed
spMaxRPM         =  63          # spindle jog max rpm
spMicroSteps     =  64          # spindle micro steps
spMinRPM         =  65          # spindle minimum rpm
spMotorSteps     =  66          # spindle motor stpes per revolution
spMotorTest      =  67          # use stepper drive to test motor
spStepDrive      =  68          # spindle stepper drive
spTestEncoder    =  69          # spindle test generate encoder test pulse
spTestIndex      =  70          # spindle test generate internal index pulse

# threading config

thAddFeed        =  71          # thread feed to add after done
thAlternate      =  72          # thread althernate thread flanks
thAngle          =  73          # thread hanlf angle of thread
thFirstFeed      =  74          # thread first feed for thread area calc
thFirstFeedBtn   =  75          # thread button to select first feed
thInternal       =  76          # thread internal threads
thLastFeed       =  77          # thread last feed for thread area calculation
thLastFeedBtn    =  78          # thread button to select last feed
thLeftHand       =  79          # thread left hand 
thMM             =  80          # thread button for mm
thPasses         =  81          # thread number of passes
thPause          =  82          # thread pause between passes
thRPM            =  83          # thread speed for threading operation
thRunout         =  84          # thread runout for rh exit or lh entrance
thSPInt          =  85          # thread spring pass interval
thSpring         =  86          # thread number of spring passes at end
thTPI            =  87          # thread select thread in threads per inch
thThread         =  88          # thread field containing tpi or pitch
thXDepth         =  89          # thread x depth of thread
thXRetract       =  90          # thread x retract
thXStart         =  91          # thread x diameter
thXTaper         =  92          # thread x taper
thZ0             =  93          # thread z right end of thread left start
thZ1             =  94          # thread z right start left end
thZRetract       =  95          # thread z retract

# taper config

tpAddFeed        =  96          # tp 
tpAngle          =  97          # tp 
tpAngleBtn       =  98          # tp 
tpDeltaBtn       =  99          # tp 
tpInternal       = 100          # tp 
tpLargeDiam      = 101          # tp 
tpPasses         = 102          # tp 
tpPause          = 103          # tp 
tpRPM            = 104          # tp 
tpSPInt          = 105          # tp 
tpSmallDiam      = 106          # tp 
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
tuXDiam1         = 127          # turn 
tuXFeed          = 128          # turn 
tuXRetract       = 129          # turn 
tuZEnd           = 130          # turn 
tuZFeed          = 131          # turn 
tuZRetract       = 132          # turn 
tuZStart         = 133          # turn 

# x axis config

xAccel           = 134          # x axis 
xBacklash        = 135          # x axis 
xDROInch         = 136          # x axis 
xHomeBackoffDist = 137          # x axis 
xHomeDir         = 138          # x axis 
xHomeDist        = 139          # x axis 
xHomeEnd         = 140          # x axis 
xHomeLoc         = 141          # x axis 
xHomeSpeed       = 142          # x axis 
xHomeStart       = 143          # x axis 
xInvDRO          = 144          # x axis invert dro
xInvDir          = 145          # x axis invert stepper direction
xInvEnc          = 146          # x axis 
xInvMpg          = 147          # x axis invert mpg direction
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
    'faPasses' : 37,
    'cfgFreqMult' : 7,
    'spStepDrive' : 68,
    'faZRetract' : 48,
    'tpZFeed' : 115,
    'tuPasses' : 121,
    'zInvDir' : 168,
    'spMicroSteps' : 64,
    'jogXPos' : 51,
    'zJogSpeed' : 173,
    'jogZPos' : 53,
    'thPause' : 82,
    'jogInc' : 50,
    'tuAddFeed' : 119,
    'tpRPM' : 104,
    'faZStart' : 49,
    'tuZStart' : 133,
    'tpTaperSel' : 108,
    'thXTaper' : 92,
    'tpZRetract' : 117,
    'thXStart' : 91,
    'xHomeStart' : 143,
    'thSPInt' : 85,
    'zMaxSpeed' : 174,
    'cfgTestRPM' : 17,
    'tpLargeDiam' : 101,
    'thSpring' : 86,
    'xHomeEnd' : 140,
    'cfgMPG' : 11,
    'xHomeBackoffDist' : 137,
    'xMinSpeed' : 153,
    'xHomeDir' : 138,
    'xMotorSteps' : 155,
    'faZFeed' : 47,
    'thAddFeed' : 71,
    'thRunout' : 84,
    'xJogSpeed' : 150,
    'cuXRetract' : 27,
    'tpZStart' : 118,
    'cuToolWidth' : 24,
    'spJogMax' : 61,
    'tuRPM' : 123,
    'thLastFeedBtn' : 78,
    'cfgDraw' : 3,
    'faXFeed' : 43,
    'xSvDROPosition' : 161,
    'cfgXFreq' : 18,
    'tuSPInt' : 124,
    'cfgLCD' : 10,
    'extDroRate' : 35,
    'xJogMax' : 148,
    'tpXInFeed' : 112,
    'thFirstFeed' : 74,
    'faAddFeed' : 36,
    'xJogMin' : 149,
    'faXEnd' : 42,
    'spJogMin' : 62,
    'xPitch' : 157,
    'cfgExtDro' : 5,
    'xSvHomeOffset' : 160,
    'tpAngle' : 97,
    'faXStart' : 45,
    'cfgEncoder' : 4,
    'faSPInt' : 40,
    'tpXFinish' : 111,
    'zSvPosition' : 183,
    'tpAddFeed' : 96,
    'tpDeltaBtn' : 99,
    'thLeftHand' : 79,
    'tpPasses' : 102,
    'xHomeSpeed' : 142,
    'thXRetract' : 90,
    'cfgCmdDis' : 0,
    'cfgDRO' : 2,
    'commPort' : 20,
    'droZPos' : 33,
    'thFirstFeedBtn' : 75,
    'zMinSpeed' : 176,
    'thRPM' : 83,
    'thZ1' : 94,
    'tpZDelta' : 114,
    'zSvHomeOffset' : 184,
    'xInvDRO' : 144,
    'tuSpring' : 125,
    'xMotorRatio' : 154,
    'tuInternal' : 120,
    'thThread' : 88,
    'cfgDbgSave' : 1,
    'thXDepth' : 89,
    'cuXEnd' : 25,
    'tuPause' : 122,
    'xProbeDist' : 158,
    'xMaxSpeed' : 151,
    'xDROInch' : 136,
    'xInvDir' : 145,
    'tuZFeed' : 131,
    'zInvEnc' : 169,
    'cuZRetract' : 30,
    'xHomeDist' : 139,
    'cfgPrbInv' : 12,
    'tpSmallDiam' : 106,
    'tpZLength' : 116,
    'cuXFeed' : 26,
    'zInvMpg' : 170,
    'thPasses' : 81,
    'spMotorSteps' : 66,
    'cuZStart' : 31,
    'zSvDROOffset' : 186,
    'zAccel' : 163,
    'tpXRetract' : 113,
    'cfgTestMode' : 16,
    'tpXFeed' : 110,
    'thAlternate' : 72,
    'xInvEnc' : 146,
    'spMinRPM' : 65,
    'tpSpring' : 107,
    'tuZEnd' : 130,
    'tuXFeed' : 128,
    'faSpring' : 41,
    'thInternal' : 76,
    'thZRetract' : 95,
    'xHomeLoc' : 141,
    'thTPI' : 87,
    'tpXDelta' : 109,
    'tpAngleBtn' : 98,
    'tpPause' : 103,
    'zBacklash' : 165,
    'cfgInvEncDir' : 9,
    'faPause' : 38,
    'thZ0' : 93,
    'spTestEncoder' : 69,
    'faXRetract' : 44,
    'cuXStart' : 28,
    'cfgHomeInPlace' : 8,
    'jpSurfaceSpeed' : 54,
    'xSvDROOffset' : 162,
    'zParkLoc' : 179,
    'faRPM' : 39,
    'spMaxRPM' : 63,
    'cfgFcy' : 6,
    'zMicroSteps' : 175,
    'thLastFeed' : 77,
    'zDROInch' : 166,
    'tuXRetract' : 129,
    'extDroPort' : 34,
    'cuRPM' : 23,
    'xInvMpg' : 147,
    'tuZRetract' : 132,
    'tpSPInt' : 105,
    'spTestIndex' : 70,
    'zJogMin' : 172,
    'zMotorRatio' : 177,
    'zPitch' : 180,
    'spInvDir' : 59,
    'spJogAccelTime' : 60,
    'zBackInc' : 164,
    'zSvDROPosition' : 185,
    'xBacklash' : 135,
    'mainPanel' : 56,
    'cfgSpEncoder' : 14,
    'thAngle' : 73,
    'zMotorSteps' : 178,
    'jogXPosDiam' : 52,
    'cuZCutoff' : 29,
    'xAccel' : 134,
    'spAccelTime' : 58,
    'zInvDRO' : 167,
    'cuPause' : 22,
    'commRate' : 21,
    'cfgXilinx' : 19,
    'spAccel' : 57,
    'zJogMax' : 171,
    'droXPos' : 32,
    'zProbeDist' : 181,
    'faZEnd' : 46,
    'xParkLoc' : 156,
    'xSvPosition' : 159,
    'jpXDroDiam' : 55,
    'spMotorTest' : 67,
    'xMicroSteps' : 152,
    'cfgTaperCycleDist' : 15,
    'tpInternal' : 100,
    'cfgRemDbg' : 13,
    'thMM' : 80,
    'zProbeSpeed' : 182,
    'tuXDiam0' : 126,
    'tuXDiam1' : 127,
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
    'cfgSpEncoder',
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
    'spTestEncoder',
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
