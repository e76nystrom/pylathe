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
cfgSpSync        =  14          # config spindle using timer
cfgSpSyncBoard   =  15          # config spindle sync board
cfgSpEncoder     =  16          # config spindle encoder
cfgTaperCycleDist =  17         # config taper cycle distance
cfgTestMode      =  18          # conifg test mode
cfgTestRPM       =  19          # config xilinx test rpm value
cfgXFreq         =  20          # config xilinx frequency
cfgXilinx        =  21          # config xilinx interface present

# communications config

commPort         =  22          # comm port
commRate         =  23          # comm baud rate

# cutoff config

cuPause          =  24          # cutoff pause before cutting
cuRPM            =  25          # cutoff rpm
cuToolWidth      =  26          # cutoff tool width
cuXEnd           =  27          # cutoff x end
cuXFeed          =  28          # cutoff x feed
cuXRetract       =  29          # cutoff x retract
cuXStart         =  30          # cutoff x start
cuZCutoff        =  31          # cutoff offset to z cutoff
cuZRetract       =  32          # cutoff offset to z retract
cuZStart         =  33          # cutoff z location

# dro position

droXPos          =  34          # dro x position
droZPos          =  35          # dro z position

# external dro

extDroPort       =  36          # external dro port
extDroRate       =  37          # external dro baud Rate

# face config

faAddFeed        =  38          # face 
faPasses         =  39          # face 
faPause          =  40          # face pause before cutting
faRPM            =  41          # face 
faSPInt          =  42          # face 
faSpring         =  43          # face 
faXEnd           =  44          # face 
faXFeed          =  45          # face 
faXRetract       =  46          # face 
faXStart         =  47          # face 
faZEnd           =  48          # face 
faZFeed          =  49          # face 
faZRetract       =  50          # face 
faZStart         =  51          # face 

# jog config

jogInc           =  52          # jog 
jogXPos          =  53          # jog 
jogXPosDiam      =  54          # jog 
jogZPos          =  55          # jog 

# jog panel config

jpSurfaceSpeed   =  56          # jogpanle fpm or rpm
jpXDroDiam       =  57          # jogpanel x dro diameter

# jog time parameters

jogTimeInitial   =  58          # jog time initial
jogTimeInc       =  59          # jog time increment
jogTimeMax       =  60          # jog time max

# keypad

keypadPort       =  61          # external dro port
keypadRate       =  62          # external dro baud Rate

# main panel

mainPanel        =  63          # name of main panel

# spindle config

spAccel          =  64          # spindle acceleration
spAccelTime      =  65          # spindle accelerationtime
spInvDir         =  66          # spindle invert direction
spJogAccelTime   =  67          # spindle jog acceleration time
spJogMax         =  68          # spindle jog max speed
spJogMin         =  69          # spindle jog min speed
spJTimeInc       =  70          # spindle jog increment
spJTimeInitial   =  71          # spindle jog initial time 
spJTimeMax       =  72          # spindle jog max
spMaxRPM         =  73          # spindle jog max rpm
spMicroSteps     =  74          # spindle micro steps
spMinRPM         =  75          # spindle minimum rpm
spMotorSteps     =  76          # spindle motor stpes per revolution
spMotorTest      =  77          # use stepper drive to test motor
spStepDrive      =  78          # spindle stepper drive
spTestEncoder    =  79          # spindle test generate encoder test pulse
spTestIndex      =  80          # spindle test generate internal index pulse

# sync communications config

syncPort         =  81          # sync comm port
syncRate         =  82          # sync comm baud rate

# threading config

thAddFeed        =  83          # thread feed to add after done
thAlternate      =  84          # thread althernate thread flanks
thAngle          =  85          # thread hanlf angle of thread
thFirstFeed      =  86          # thread first feed for thread area calc
thFirstFeedBtn   =  87          # thread button to select first feed
thInternal       =  88          # thread internal threads
thLastFeed       =  89          # thread last feed for thread area calculation
thLastFeedBtn    =  90          # thread button to select last feed
thLeftHand       =  91          # thread left hand 
thMM             =  92          # thread button for mm
thPasses         =  93          # thread number of passes
thPause          =  94          # thread pause between passes
thRPM            =  95          # thread speed for threading operation
thRunout         =  96          # thread runout for rh exit or lh entrance
thSPInt          =  97          # thread spring pass interval
thSpring         =  98          # thread number of spring passes at end
thTPI            =  99          # thread select thread in threads per inch
thThread         = 100          # thread field containing tpi or pitch
thXDepth         = 101          # thread x depth of thread
thXRetract       = 102          # thread x retract
thXStart         = 103          # thread x diameter
thXTaper         = 104          # thread x taper
thZ0             = 105          # thread z right end of thread left start
thZ1             = 106          # thread z right start left end
thZRetract       = 107          # thread z retract

# taper config

tpAddFeed        = 108          # tp 
tpAngle          = 109          # tp 
tpAngleBtn       = 110          # tp 
tpDeltaBtn       = 111          # tp 
tpInternal       = 112          # tp 
tpLargeDiam      = 113          # tp 
tpPasses         = 114          # tp 
tpPause          = 115          # tp 
tpRPM            = 116          # tp 
tpSPInt          = 117          # tp 
tpSmallDiam      = 118          # tp 
tpSpring         = 119          # tp 
tpTaperSel       = 120          # tp 
tpXDelta         = 121          # tp 
tpXFeed          = 122          # tp 
tpXFinish        = 123          # tp 
tpXInFeed        = 124          # tp 
tpXRetract       = 125          # tp 
tpZDelta         = 126          # tp 
tpZFeed          = 127          # tp 
tpZLength        = 128          # tp 
tpZRetract       = 129          # tp 
tpZStart         = 130          # tp 

# turn config

tuAddFeed        = 131          # turn 
tuInternal       = 132          # turn internal
tuPasses         = 133          # turn 
tuPause          = 134          # turn 
tuRPM            = 135          # turn 
tuSPInt          = 136          # turn 
tuSpring         = 137          # turn 
tuXDiam0         = 138          # turn 
tuXDiam1         = 139          # turn 
tuXFeed          = 140          # turn 
tuXRetract       = 141          # turn 
tuZEnd           = 142          # turn 
tuZFeed          = 143          # turn 
tuZRetract       = 144          # turn 
tuZStart         = 145          # turn 

# x axis config

xAccel           = 146          # x axis 
xBacklash        = 147          # x axis 
xDROInch         = 148          # x axis 
xHomeBackoffDist = 149          # x axis 
xHomeDir         = 150          # x axis 
xHomeDist        = 151          # x axis 
xHomeEnd         = 152          # x axis 
xHomeLoc         = 153          # x axis 
xHomeSpeed       = 154          # x axis 
xHomeStart       = 155          # x axis 
xInvDRO          = 156          # x axis invert dro
xInvDir          = 157          # x axis invert stepper direction
xInvEnc          = 158          # x axis 
xInvMpg          = 159          # x axis invert mpg direction
xJogMax          = 160          # x axis 
xJogMin          = 161          # x axis 
xMpgInc          = 162          # x axis jog increment
xMpgMax          = 163          # x axis jog maximum
xJogSpeed        = 164          # x axis 
xMaxSpeed        = 165          # x axis 
xMicroSteps      = 166          # x axis 
xMinSpeed        = 167          # x axis 
xMotorRatio      = 168          # x axis 
xMotorSteps      = 169          # x axis 
xParkLoc         = 170          # x axis 
xPitch           = 171          # x axis 
xProbeDist       = 172          # x axis 

# x axis position config

xSvPosition      = 173          # z axis 
xSvHomeOffset    = 174          # z axis 
xSvDROPosition   = 175          # x axis 
xSvDROOffset     = 176          # x axis 

# z axis config

zAccel           = 177          # z axis 
zBackInc         = 178          # z axis distance to go past for taking out backlash
zBacklash        = 179          # z axis 
zDROInch         = 180          # z axis 
zInvDRO          = 181          # z axis 
zInvDir          = 182          # z axis 
zInvEnc          = 183          # z axis 
zInvMpg          = 184          # z axis 
zJogMax          = 185          # z axis 
zJogMin          = 186          # z axis 
zMpgInc          = 187          # z axis jog increment
zMpgMax          = 188          # z axis jog maximum
zJogSpeed        = 189          # z axis 
zMaxSpeed        = 190          # z axis 
zMicroSteps      = 191          # z axis 
zMinSpeed        = 192          # z axis 
zMotorRatio      = 193          # z axis 
zMotorSteps      = 194          # z axis 
zParkLoc         = 195          # z axis 
zPitch           = 196          # z axis 
zProbeDist       = 197          # z axis 
zProbeSpeed      = 198          # z axis 

# z axis position config

zSvPosition      = 199          # z axis 
zSvHomeOffset    = 200          # z axis 
zSvDROPosition   = 201          # z axis 
zSvDROOffset     = 202          # z axis 

config = { \
    'faPasses' : 39,
    'cfgFreqMult' : 7,
    'spStepDrive' : 78,
    'faZRetract' : 50,
    'tpZFeed' : 127,
    'tuPasses' : 133,
    'thInternal' : 88,
    'zInvDir' : 182,
    'spMicroSteps' : 74,
    'jogXPos' : 53,
    'zJogSpeed' : 189,
    'xMpgInc' : 162,
    'jogZPos' : 55,
    'thAlternate' : 84,
    'jogInc' : 52,
    'tuAddFeed' : 131,
    'tpRPM' : 116,
    'faZStart' : 51,
    'tuZStart' : 145,
    'tpTaperSel' : 120,
    'thXTaper' : 104,
    'tpZRetract' : 129,
    'thXStart' : 103,
    'xHomeStart' : 155,
    'thSPInt' : 97,
    'zMaxSpeed' : 190,
    'cfgTestRPM' : 19,
    'tpLargeDiam' : 113,
    'thSpring' : 98,
    'xHomeEnd' : 152,
    'cfgMPG' : 11,
    'xMinSpeed' : 167,
    'xHomeDir' : 150,
    'keypadPort' : 61,
    'faZFeed' : 49,
    'cfgSpSync' : 14,
    'thAddFeed' : 83,
    'thRunout' : 96,
    'xJogSpeed' : 164,
    'zMpgInc' : 187,
    'cuXRetract' : 29,
    'tpZStart' : 130,
    'cuToolWidth' : 26,
    'spJogMax' : 68,
    'tuRPM' : 135,
    'thLastFeedBtn' : 90,
    'cfgDraw' : 3,
    'faXFeed' : 45,
    'xSvDROPosition' : 175,
    'cfgXFreq' : 20,
    'tuSPInt' : 136,
    'cfgLCD' : 10,
    'extDroRate' : 37,
    'xJogMax' : 160,
    'tpXInFeed' : 124,
    'thFirstFeed' : 86,
    'xHomeDist' : 151,
    'jogTimeInitial' : 58,
    'faAddFeed' : 38,
    'xJogMin' : 161,
    'xMotorSteps' : 169,
    'faXEnd' : 44,
    'spJogMin' : 69,
    'xPitch' : 171,
    'cfgExtDro' : 5,
    'xSvHomeOffset' : 174,
    'tpAngle' : 109,
    'faXStart' : 47,
    'cfgEncoder' : 4,
    'faSPInt' : 42,
    'tpXFinish' : 123,
    'zSvPosition' : 199,
    'tpAddFeed' : 108,
    'tpDeltaBtn' : 111,
    'thLeftHand' : 91,
    'tpPasses' : 114,
    'xHomeSpeed' : 154,
    'thXRetract' : 102,
    'xHomeBackoffDist' : 149,
    'cfgDRO' : 2,
    'cfgSpSyncBoard' : 15,
    'commPort' : 22,
    'droZPos' : 35,
    'thFirstFeedBtn' : 87,
    'zMinSpeed' : 192,
    'thRPM' : 95,
    'thZ1' : 106,
    'keypadRate' : 62,
    'zSvHomeOffset' : 200,
    'xInvDRO' : 156,
    'tuSpring' : 137,
    'xMotorRatio' : 168,
    'syncPort' : 81,
    'thThread' : 100,
    'cfgDbgSave' : 1,
    'thXDepth' : 101,
    'cuXEnd' : 27,
    'tuPause' : 134,
    'xProbeDist' : 172,
    'xMaxSpeed' : 165,
    'xDROInch' : 148,
    'xInvDir' : 157,
    'tuZFeed' : 143,
    'zInvEnc' : 183,
    'cuZRetract' : 32,
    'zSvDROOffset' : 202,
    'spJTimeInc' : 70,
    'cfgPrbInv' : 12,
    'tpSmallDiam' : 118,
    'tpZLength' : 128,
    'cuXFeed' : 28,
    'zInvMpg' : 184,
    'thPasses' : 93,
    'spMotorSteps' : 76,
    'cuZStart' : 33,
    'tpZDelta' : 126,
    'zAccel' : 177,
    'tpXRetract' : 125,
    'cfgTestMode' : 18,
    'tpXFeed' : 122,
    'thPause' : 94,
    'xInvEnc' : 158,
    'spMinRPM' : 75,
    'tpSpring' : 119,
    'tuZEnd' : 142,
    'tuXFeed' : 140,
    'jogTimeMax' : 60,
    'faSpring' : 43,
    'spJTimeInitial' : 71,
    'cfgXilinx' : 21,
    'thZRetract' : 107,
    'xHomeLoc' : 153,
    'thTPI' : 99,
    'tpXDelta' : 121,
    'tpAngleBtn' : 110,
    'tpPause' : 115,
    'zBacklash' : 179,
    'cfgInvEncDir' : 9,
    'syncRate' : 82,
    'faPause' : 40,
    'thZ0' : 105,
    'zMpgMax' : 188,
    'spTestEncoder' : 79,
    'xMpgMax' : 163,
    'faXRetract' : 46,
    'cuXStart' : 30,
    'cfgHomeInPlace' : 8,
    'jpSurfaceSpeed' : 56,
    'xSvDROOffset' : 176,
    'zParkLoc' : 195,
    'faRPM' : 41,
    'spMaxRPM' : 73,
    'cfgFcy' : 6,
    'zMicroSteps' : 191,
    'thLastFeed' : 89,
    'zDROInch' : 180,
    'tuXRetract' : 141,
    'tuInternal' : 132,
    'extDroPort' : 36,
    'cuRPM' : 25,
    'xInvMpg' : 159,
    'tuZRetract' : 144,
    'tpSPInt' : 117,
    'spTestIndex' : 80,
    'zJogMin' : 186,
    'zMotorRatio' : 193,
    'zPitch' : 196,
    'spInvDir' : 66,
    'spJogAccelTime' : 67,
    'zBackInc' : 178,
    'spJTimeMax' : 72,
    'zSvDROPosition' : 201,
    'xBacklash' : 147,
    'mainPanel' : 63,
    'cfgSpEncoder' : 16,
    'thAngle' : 85,
    'jogTimeInc' : 59,
    'zMotorSteps' : 194,
    'jogXPosDiam' : 54,
    'cuZCutoff' : 31,
    'xAccel' : 146,
    'spAccelTime' : 65,
    'zInvDRO' : 181,
    'cuPause' : 24,
    'commRate' : 23,
    'cfgCmdDis' : 0,
    'spAccel' : 64,
    'zJogMax' : 185,
    'droXPos' : 34,
    'zProbeDist' : 197,
    'faZEnd' : 48,
    'xParkLoc' : 170,
    'xSvPosition' : 173,
    'jpXDroDiam' : 57,
    'spMotorTest' : 77,
    'xMicroSteps' : 166,
    'cfgTaperCycleDist' : 17,
    'tpInternal' : 112,
    'cfgRemDbg' : 13,
    'thMM' : 92,
    'zProbeSpeed' : 198,
    'tuXDiam0' : 138,
    'tuXDiam1' : 139,
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
    'cfgSpSync',
    'cfgSpSyncBoard',
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
