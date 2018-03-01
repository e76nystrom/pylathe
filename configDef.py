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

# jog time parameters

jogTimeInitial   =  56          # jog time initial
jogTimeInc       =  57          # jog time increment
jogTimeMax       =  58          # jog time max

# keypad

keypadPort       =  59          # external dro port
keypadRate       =  60          # external dro baud Rate

# main panel

mainPanel        =  61          # name of main panel

# spindle config

spAccel          =  62          # spindle acceleration
spAccelTime      =  63          # spindle accelerationtime
spInvDir         =  64          # spindle invert direction
spJogAccelTime   =  65          # spindle jog acceleration time
spJogMax         =  66          # spindle jog max speed
spJogMin         =  67          # spindle jog min speed
spJTimeInc       =  68          # spindle jog increment
spJTimeInitial   =  69          # spindle jog initial time 
spJTimeMax       =  70          # spindle jog max
spMaxRPM         =  71          # spindle jog max rpm
spMicroSteps     =  72          # spindle micro steps
spMinRPM         =  73          # spindle minimum rpm
spMotorSteps     =  74          # spindle motor stpes per revolution
spMotorTest      =  75          # use stepper drive to test motor
spStepDrive      =  76          # spindle stepper drive
spTestEncoder    =  77          # spindle test generate encoder test pulse
spTestIndex      =  78          # spindle test generate internal index pulse

# threading config

thAddFeed        =  79          # thread feed to add after done
thAlternate      =  80          # thread althernate thread flanks
thAngle          =  81          # thread hanlf angle of thread
thFirstFeed      =  82          # thread first feed for thread area calc
thFirstFeedBtn   =  83          # thread button to select first feed
thInternal       =  84          # thread internal threads
thLastFeed       =  85          # thread last feed for thread area calculation
thLastFeedBtn    =  86          # thread button to select last feed
thLeftHand       =  87          # thread left hand 
thMM             =  88          # thread button for mm
thPasses         =  89          # thread number of passes
thPause          =  90          # thread pause between passes
thRPM            =  91          # thread speed for threading operation
thRunout         =  92          # thread runout for rh exit or lh entrance
thSPInt          =  93          # thread spring pass interval
thSpring         =  94          # thread number of spring passes at end
thTPI            =  95          # thread select thread in threads per inch
thThread         =  96          # thread field containing tpi or pitch
thXDepth         =  97          # thread x depth of thread
thXRetract       =  98          # thread x retract
thXStart         =  99          # thread x diameter
thXTaper         = 100          # thread x taper
thZ0             = 101          # thread z right end of thread left start
thZ1             = 102          # thread z right start left end
thZRetract       = 103          # thread z retract

# taper config

tpAddFeed        = 104          # tp 
tpAngle          = 105          # tp 
tpAngleBtn       = 106          # tp 
tpDeltaBtn       = 107          # tp 
tpInternal       = 108          # tp 
tpLargeDiam      = 109          # tp 
tpPasses         = 110          # tp 
tpPause          = 111          # tp 
tpRPM            = 112          # tp 
tpSPInt          = 113          # tp 
tpSmallDiam      = 114          # tp 
tpSpring         = 115          # tp 
tpTaperSel       = 116          # tp 
tpXDelta         = 117          # tp 
tpXFeed          = 118          # tp 
tpXFinish        = 119          # tp 
tpXInFeed        = 120          # tp 
tpXRetract       = 121          # tp 
tpZDelta         = 122          # tp 
tpZFeed          = 123          # tp 
tpZLength        = 124          # tp 
tpZRetract       = 125          # tp 
tpZStart         = 126          # tp 

# turn config

tuAddFeed        = 127          # turn 
tuInternal       = 128          # turn internal
tuPasses         = 129          # turn 
tuPause          = 130          # turn 
tuRPM            = 131          # turn 
tuSPInt          = 132          # turn 
tuSpring         = 133          # turn 
tuXDiam0         = 134          # turn 
tuXDiam1         = 135          # turn 
tuXFeed          = 136          # turn 
tuXRetract       = 137          # turn 
tuZEnd           = 138          # turn 
tuZFeed          = 139          # turn 
tuZRetract       = 140          # turn 
tuZStart         = 141          # turn 

# x axis config

xAccel           = 142          # x axis 
xBacklash        = 143          # x axis 
xDROInch         = 144          # x axis 
xHomeBackoffDist = 145          # x axis 
xHomeDir         = 146          # x axis 
xHomeDist        = 147          # x axis 
xHomeEnd         = 148          # x axis 
xHomeLoc         = 149          # x axis 
xHomeSpeed       = 150          # x axis 
xHomeStart       = 151          # x axis 
xInvDRO          = 152          # x axis invert dro
xInvDir          = 153          # x axis invert stepper direction
xInvEnc          = 154          # x axis 
xInvMpg          = 155          # x axis invert mpg direction
xJogMax          = 156          # x axis 
xJogMin          = 157          # x axis 
xMpgInc          = 158          # x axis jog increment
xMpgMax          = 159          # x axis jog maximum
xJogSpeed        = 160          # x axis 
xMaxSpeed        = 161          # x axis 
xMicroSteps      = 162          # x axis 
xMinSpeed        = 163          # x axis 
xMotorRatio      = 164          # x axis 
xMotorSteps      = 165          # x axis 
xParkLoc         = 166          # x axis 
xPitch           = 167          # x axis 
xProbeDist       = 168          # x axis 

# x axis position config

xSvPosition      = 169          # z axis 
xSvHomeOffset    = 170          # z axis 
xSvDROPosition   = 171          # x axis 
xSvDROOffset     = 172          # x axis 

# z axis config

zAccel           = 173          # z axis 
zBackInc         = 174          # z axis distance to go past for taking out backlash
zBacklash        = 175          # z axis 
zDROInch         = 176          # z axis 
zInvDRO          = 177          # z axis 
zInvDir          = 178          # z axis 
zInvEnc          = 179          # z axis 
zInvMpg          = 180          # z axis 
zJogMax          = 181          # z axis 
zJogMin          = 182          # z axis 
zMpgInc          = 183          # z axis jog increment
zMpgMax          = 184          # z axis jog maximum
zJogSpeed        = 185          # z axis 
zMaxSpeed        = 186          # z axis 
zMicroSteps      = 187          # z axis 
zMinSpeed        = 188          # z axis 
zMotorRatio      = 189          # z axis 
zMotorSteps      = 190          # z axis 
zParkLoc         = 191          # z axis 
zPitch           = 192          # z axis 
zProbeDist       = 193          # z axis 
zProbeSpeed      = 194          # z axis 

# z axis position config

zSvPosition      = 195          # z axis 
zSvHomeOffset    = 196          # z axis 
zSvDROPosition   = 197          # z axis 
zSvDROOffset     = 198          # z axis 

config = { \
    'faPasses' : 37,
    'cfgFreqMult' : 7,
    'spStepDrive' : 76,
    'faZRetract' : 48,
    'tpZFeed' : 123,
    'tuPasses' : 129,
    'zInvDir' : 178,
    'spMicroSteps' : 72,
    'jogXPos' : 51,
    'zJogSpeed' : 185,
    'xMpgInc' : 158,
    'jogZPos' : 53,
    'thAlternate' : 80,
    'jogInc' : 50,
    'tuAddFeed' : 127,
    'tpRPM' : 112,
    'faZStart' : 49,
    'tuZStart' : 141,
    'tpTaperSel' : 116,
    'thXTaper' : 100,
    'tpZRetract' : 125,
    'thXStart' : 99,
    'xHomeStart' : 151,
    'thSPInt' : 93,
    'zMaxSpeed' : 186,
    'cfgTestRPM' : 17,
    'tpLargeDiam' : 109,
    'thSpring' : 94,
    'xHomeEnd' : 148,
    'cfgMPG' : 11,
    'xHomeBackoffDist' : 145,
    'xMinSpeed' : 163,
    'xHomeDir' : 146,
    'keypadPort' : 59,
    'faZFeed' : 47,
    'thAddFeed' : 79,
    'thRunout' : 92,
    'xJogSpeed' : 160,
    'zMpgInc' : 183,
    'cuXRetract' : 27,
    'tpZStart' : 126,
    'cuToolWidth' : 24,
    'spJogMax' : 66,
    'tuRPM' : 131,
    'thLastFeedBtn' : 86,
    'cfgDraw' : 3,
    'faXFeed' : 43,
    'xSvDROPosition' : 171,
    'cfgXFreq' : 18,
    'tuSPInt' : 132,
    'cfgLCD' : 10,
    'extDroRate' : 35,
    'xJogMax' : 156,
    'tpXInFeed' : 120,
    'thFirstFeed' : 82,
    'xHomeDist' : 147,
    'jogTimeInitial' : 56,
    'faAddFeed' : 36,
    'xJogMin' : 157,
    'xMotorSteps' : 165,
    'faXEnd' : 42,
    'spJogMin' : 67,
    'xPitch' : 167,
    'cfgExtDro' : 5,
    'xSvHomeOffset' : 170,
    'tpAngle' : 105,
    'faXStart' : 45,
    'cfgEncoder' : 4,
    'faSPInt' : 40,
    'tpXFinish' : 119,
    'zSvPosition' : 195,
    'tpAddFeed' : 104,
    'tpDeltaBtn' : 107,
    'thLeftHand' : 87,
    'tpPasses' : 110,
    'xHomeSpeed' : 150,
    'thXRetract' : 98,
    'cfgCmdDis' : 0,
    'cfgDRO' : 2,
    'commPort' : 20,
    'droZPos' : 33,
    'thFirstFeedBtn' : 83,
    'zMinSpeed' : 188,
    'thRPM' : 91,
    'thZ1' : 102,
    'keypadRate' : 60,
    'zSvHomeOffset' : 196,
    'xInvDRO' : 152,
    'tuSpring' : 133,
    'xMotorRatio' : 164,
    'tuInternal' : 128,
    'thThread' : 96,
    'cfgDbgSave' : 1,
    'thXDepth' : 97,
    'cuXEnd' : 25,
    'tuPause' : 130,
    'xProbeDist' : 168,
    'xMaxSpeed' : 161,
    'xDROInch' : 144,
    'xInvDir' : 153,
    'tuZFeed' : 139,
    'zInvEnc' : 179,
    'cuZRetract' : 30,
    'zSvDROOffset' : 198,
    'spJTimeInc' : 68,
    'cfgPrbInv' : 12,
    'tpSmallDiam' : 114,
    'tpZLength' : 124,
    'cuXFeed' : 26,
    'zInvMpg' : 180,
    'thPasses' : 89,
    'spMotorSteps' : 74,
    'cuZStart' : 31,
    'tpZDelta' : 122,
    'zAccel' : 173,
    'tpXRetract' : 121,
    'cfgTestMode' : 16,
    'tpXFeed' : 118,
    'thPause' : 90,
    'xInvEnc' : 154,
    'spMinRPM' : 73,
    'tpSpring' : 115,
    'tuZEnd' : 138,
    'tuXFeed' : 136,
    'jogTimeMax' : 58,
    'faSpring' : 41,
    'spJTimeInitial' : 69,
    'thInternal' : 84,
    'thZRetract' : 103,
    'xHomeLoc' : 149,
    'thTPI' : 95,
    'tpXDelta' : 117,
    'tpAngleBtn' : 106,
    'tpPause' : 111,
    'zBacklash' : 175,
    'cfgInvEncDir' : 9,
    'faPause' : 38,
    'thZ0' : 101,
    'zMpgMax' : 184,
    'spTestEncoder' : 77,
    'xMpgMax' : 159,
    'faXRetract' : 44,
    'cuXStart' : 28,
    'cfgHomeInPlace' : 8,
    'jpSurfaceSpeed' : 54,
    'xSvDROOffset' : 172,
    'zParkLoc' : 191,
    'faRPM' : 39,
    'spMaxRPM' : 71,
    'cfgFcy' : 6,
    'zMicroSteps' : 187,
    'thLastFeed' : 85,
    'zDROInch' : 176,
    'tuXRetract' : 137,
    'extDroPort' : 34,
    'cuRPM' : 23,
    'xInvMpg' : 155,
    'tuZRetract' : 140,
    'tpSPInt' : 113,
    'spTestIndex' : 78,
    'zJogMin' : 182,
    'zMotorRatio' : 189,
    'zPitch' : 192,
    'spInvDir' : 64,
    'spJogAccelTime' : 65,
    'zBackInc' : 174,
    'spJTimeMax' : 70,
    'zSvDROPosition' : 197,
    'xBacklash' : 143,
    'mainPanel' : 61,
    'cfgSpEncoder' : 14,
    'thAngle' : 81,
    'jogTimeInc' : 57,
    'zMotorSteps' : 190,
    'jogXPosDiam' : 52,
    'cuZCutoff' : 29,
    'xAccel' : 142,
    'spAccelTime' : 63,
    'zInvDRO' : 177,
    'cuPause' : 22,
    'commRate' : 21,
    'cfgXilinx' : 19,
    'spAccel' : 62,
    'zJogMax' : 181,
    'droXPos' : 32,
    'zProbeDist' : 193,
    'faZEnd' : 46,
    'xParkLoc' : 166,
    'xSvPosition' : 169,
    'jpXDroDiam' : 55,
    'spMotorTest' : 75,
    'xMicroSteps' : 162,
    'cfgTaperCycleDist' : 15,
    'tpInternal' : 108,
    'cfgRemDbg' : 13,
    'thMM' : 88,
    'zProbeSpeed' : 194,
    'tuXDiam0' : 134,
    'tuXDiam1' : 135,
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
    'jogTimeInitial',
    'jogTimeInc',
    'jogTimeMax',
    'keypadPort',
    'keypadRate',
    'mainPanel',
    'spAccel',
    'spAccelTime',
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
    'xMpgInc',
    'xMpgMax',
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
    'zMpgInc',
    'zMpgMax',
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
