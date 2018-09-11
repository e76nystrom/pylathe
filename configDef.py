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

# sync communications config

syncPort         =  79          # sync comm port
syncRate         =  80          # sync comm baud rate

# threading config

thAddFeed        =  81          # thread feed to add after done
thAlternate      =  82          # thread althernate thread flanks
thAngle          =  83          # thread hanlf angle of thread
thFirstFeed      =  84          # thread first feed for thread area calc
thFirstFeedBtn   =  85          # thread button to select first feed
thInternal       =  86          # thread internal threads
thLastFeed       =  87          # thread last feed for thread area calculation
thLastFeedBtn    =  88          # thread button to select last feed
thLeftHand       =  89          # thread left hand 
thMM             =  90          # thread button for mm
thPasses         =  91          # thread number of passes
thPause          =  92          # thread pause between passes
thRPM            =  93          # thread speed for threading operation
thRunout         =  94          # thread runout for rh exit or lh entrance
thSPInt          =  95          # thread spring pass interval
thSpring         =  96          # thread number of spring passes at end
thTPI            =  97          # thread select thread in threads per inch
thThread         =  98          # thread field containing tpi or pitch
thXDepth         =  99          # thread x depth of thread
thXRetract       = 100          # thread x retract
thXStart         = 101          # thread x diameter
thXTaper         = 102          # thread x taper
thZ0             = 103          # thread z right end of thread left start
thZ1             = 104          # thread z right start left end
thZRetract       = 105          # thread z retract

# taper config

tpAddFeed        = 106          # tp 
tpAngle          = 107          # tp 
tpAngleBtn       = 108          # tp 
tpDeltaBtn       = 109          # tp 
tpInternal       = 110          # tp 
tpLargeDiam      = 111          # tp 
tpPasses         = 112          # tp 
tpPause          = 113          # tp 
tpRPM            = 114          # tp 
tpSPInt          = 115          # tp 
tpSmallDiam      = 116          # tp 
tpSpring         = 117          # tp 
tpTaperSel       = 118          # tp 
tpXDelta         = 119          # tp 
tpXFeed          = 120          # tp 
tpXFinish        = 121          # tp 
tpXInFeed        = 122          # tp 
tpXRetract       = 123          # tp 
tpZDelta         = 124          # tp 
tpZFeed          = 125          # tp 
tpZLength        = 126          # tp 
tpZRetract       = 127          # tp 
tpZStart         = 128          # tp 

# turn config

tuAddFeed        = 129          # turn 
tuInternal       = 130          # turn internal
tuPasses         = 131          # turn 
tuPause          = 132          # turn 
tuRPM            = 133          # turn 
tuSPInt          = 134          # turn 
tuSpring         = 135          # turn 
tuXDiam0         = 136          # turn 
tuXDiam1         = 137          # turn 
tuXFeed          = 138          # turn 
tuXRetract       = 139          # turn 
tuZEnd           = 140          # turn 
tuZFeed          = 141          # turn 
tuZRetract       = 142          # turn 
tuZStart         = 143          # turn 

# x axis config

xAccel           = 144          # x axis 
xBacklash        = 145          # x axis 
xDROInch         = 146          # x axis 
xHomeBackoffDist = 147          # x axis 
xHomeDir         = 148          # x axis 
xHomeDist        = 149          # x axis 
xHomeEnd         = 150          # x axis 
xHomeLoc         = 151          # x axis 
xHomeSpeed       = 152          # x axis 
xHomeStart       = 153          # x axis 
xInvDRO          = 154          # x axis invert dro
xInvDir          = 155          # x axis invert stepper direction
xInvEnc          = 156          # x axis 
xInvMpg          = 157          # x axis invert mpg direction
xJogMax          = 158          # x axis 
xJogMin          = 159          # x axis 
xMpgInc          = 160          # x axis jog increment
xMpgMax          = 161          # x axis jog maximum
xJogSpeed        = 162          # x axis 
xMaxSpeed        = 163          # x axis 
xMicroSteps      = 164          # x axis 
xMinSpeed        = 165          # x axis 
xMotorRatio      = 166          # x axis 
xMotorSteps      = 167          # x axis 
xParkLoc         = 168          # x axis 
xPitch           = 169          # x axis 
xProbeDist       = 170          # x axis 

# x axis position config

xSvPosition      = 171          # z axis 
xSvHomeOffset    = 172          # z axis 
xSvDROPosition   = 173          # x axis 
xSvDROOffset     = 174          # x axis 

# z axis config

zAccel           = 175          # z axis 
zBackInc         = 176          # z axis distance to go past for taking out backlash
zBacklash        = 177          # z axis 
zDROInch         = 178          # z axis 
zInvDRO          = 179          # z axis 
zInvDir          = 180          # z axis 
zInvEnc          = 181          # z axis 
zInvMpg          = 182          # z axis 
zJogMax          = 183          # z axis 
zJogMin          = 184          # z axis 
zMpgInc          = 185          # z axis jog increment
zMpgMax          = 186          # z axis jog maximum
zJogSpeed        = 187          # z axis 
zMaxSpeed        = 188          # z axis 
zMicroSteps      = 189          # z axis 
zMinSpeed        = 190          # z axis 
zMotorRatio      = 191          # z axis 
zMotorSteps      = 192          # z axis 
zParkLoc         = 193          # z axis 
zPitch           = 194          # z axis 
zProbeDist       = 195          # z axis 
zProbeSpeed      = 196          # z axis 

# z axis position config

zSvPosition      = 197          # z axis 
zSvHomeOffset    = 198          # z axis 
zSvDROPosition   = 199          # z axis 
zSvDROOffset     = 200          # z axis 

config = { \
    'faPasses' : 37,
    'cfgFreqMult' : 7,
    'spStepDrive' : 76,
    'faZRetract' : 48,
    'tpZFeed' : 125,
    'tuPasses' : 131,
    'thInternal' : 86,
    'zInvDir' : 180,
    'spMicroSteps' : 72,
    'jogXPos' : 51,
    'zJogSpeed' : 187,
    'xMpgInc' : 160,
    'jogZPos' : 53,
    'thAlternate' : 82,
    'jogInc' : 50,
    'tuAddFeed' : 129,
    'tpRPM' : 114,
    'faZStart' : 49,
    'tuZStart' : 143,
    'tpTaperSel' : 118,
    'thXTaper' : 102,
    'tpZRetract' : 127,
    'thXStart' : 101,
    'xHomeStart' : 153,
    'thSPInt' : 95,
    'zMaxSpeed' : 188,
    'cfgTestRPM' : 17,
    'tpLargeDiam' : 111,
    'thSpring' : 96,
    'xHomeEnd' : 150,
    'cfgMPG' : 11,
    'xMinSpeed' : 165,
    'xHomeDir' : 148,
    'keypadPort' : 59,
    'faZFeed' : 47,
    'thAddFeed' : 81,
    'thRunout' : 94,
    'xJogSpeed' : 162,
    'zMpgInc' : 185,
    'cuXRetract' : 27,
    'tpZStart' : 128,
    'cuToolWidth' : 24,
    'spJogMax' : 66,
    'tuRPM' : 133,
    'thLastFeedBtn' : 88,
    'cfgDraw' : 3,
    'faXFeed' : 43,
    'xSvDROPosition' : 173,
    'cfgXFreq' : 18,
    'tuSPInt' : 134,
    'cfgLCD' : 10,
    'extDroRate' : 35,
    'xJogMax' : 158,
    'tpXInFeed' : 122,
    'thFirstFeed' : 84,
    'xHomeDist' : 149,
    'jogTimeInitial' : 56,
    'faAddFeed' : 36,
    'xJogMin' : 159,
    'xMotorSteps' : 167,
    'faXEnd' : 42,
    'spJogMin' : 67,
    'xPitch' : 169,
    'cfgExtDro' : 5,
    'xSvHomeOffset' : 172,
    'tpAngle' : 107,
    'faXStart' : 45,
    'cfgEncoder' : 4,
    'faSPInt' : 40,
    'tpXFinish' : 121,
    'zSvPosition' : 197,
    'tpAddFeed' : 106,
    'tpDeltaBtn' : 109,
    'thLeftHand' : 89,
    'tpPasses' : 112,
    'xHomeSpeed' : 152,
    'thXRetract' : 100,
    'xHomeBackoffDist' : 147,
    'cfgDRO' : 2,
    'commPort' : 20,
    'droZPos' : 33,
    'thFirstFeedBtn' : 85,
    'zMinSpeed' : 190,
    'thRPM' : 93,
    'thZ1' : 104,
    'keypadRate' : 60,
    'zSvHomeOffset' : 198,
    'xInvDRO' : 154,
    'tuSpring' : 135,
    'xMotorRatio' : 166,
    'syncPort' : 79,
    'thThread' : 98,
    'cfgDbgSave' : 1,
    'thXDepth' : 99,
    'cuXEnd' : 25,
    'tuPause' : 132,
    'xProbeDist' : 170,
    'xMaxSpeed' : 163,
    'xDROInch' : 146,
    'xInvDir' : 155,
    'tuZFeed' : 141,
    'zInvEnc' : 181,
    'cuZRetract' : 30,
    'zSvDROOffset' : 200,
    'spJTimeInc' : 68,
    'cfgPrbInv' : 12,
    'tpSmallDiam' : 116,
    'tpZLength' : 126,
    'cuXFeed' : 26,
    'zInvMpg' : 182,
    'thPasses' : 91,
    'spMotorSteps' : 74,
    'cuZStart' : 31,
    'tpZDelta' : 124,
    'zAccel' : 175,
    'tpXRetract' : 123,
    'cfgTestMode' : 16,
    'tpXFeed' : 120,
    'thPause' : 92,
    'xInvEnc' : 156,
    'spMinRPM' : 73,
    'tpSpring' : 117,
    'tuZEnd' : 140,
    'tuXFeed' : 138,
    'jogTimeMax' : 58,
    'faSpring' : 41,
    'spJTimeInitial' : 69,
    'cfgXilinx' : 19,
    'thZRetract' : 105,
    'xHomeLoc' : 151,
    'thTPI' : 97,
    'tpXDelta' : 119,
    'tpAngleBtn' : 108,
    'tpPause' : 113,
    'zBacklash' : 177,
    'cfgInvEncDir' : 9,
    'syncRate' : 80,
    'faPause' : 38,
    'thZ0' : 103,
    'zMpgMax' : 186,
    'spTestEncoder' : 77,
    'xMpgMax' : 161,
    'faXRetract' : 44,
    'cuXStart' : 28,
    'cfgHomeInPlace' : 8,
    'jpSurfaceSpeed' : 54,
    'xSvDROOffset' : 174,
    'zParkLoc' : 193,
    'faRPM' : 39,
    'spMaxRPM' : 71,
    'cfgFcy' : 6,
    'zMicroSteps' : 189,
    'thLastFeed' : 87,
    'zDROInch' : 178,
    'tuXRetract' : 139,
    'tuInternal' : 130,
    'extDroPort' : 34,
    'cuRPM' : 23,
    'xInvMpg' : 157,
    'tuZRetract' : 142,
    'tpSPInt' : 115,
    'spTestIndex' : 78,
    'zJogMin' : 184,
    'zMotorRatio' : 191,
    'zPitch' : 194,
    'spInvDir' : 64,
    'spJogAccelTime' : 65,
    'zBackInc' : 176,
    'spJTimeMax' : 70,
    'zSvDROPosition' : 199,
    'xBacklash' : 145,
    'mainPanel' : 61,
    'cfgSpEncoder' : 14,
    'thAngle' : 83,
    'jogTimeInc' : 57,
    'zMotorSteps' : 192,
    'jogXPosDiam' : 52,
    'cuZCutoff' : 29,
    'xAccel' : 144,
    'spAccelTime' : 63,
    'zInvDRO' : 179,
    'cuPause' : 22,
    'commRate' : 21,
    'cfgCmdDis' : 0,
    'spAccel' : 62,
    'zJogMax' : 183,
    'droXPos' : 32,
    'zProbeDist' : 195,
    'faZEnd' : 46,
    'xParkLoc' : 168,
    'xSvPosition' : 171,
    'jpXDroDiam' : 55,
    'spMotorTest' : 75,
    'xMicroSteps' : 164,
    'cfgTaperCycleDist' : 15,
    'tpInternal' : 110,
    'cfgRemDbg' : 13,
    'thMM' : 90,
    'zProbeSpeed' : 196,
    'tuXDiam0' : 136,
    'tuXDiam1' : 137,
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
