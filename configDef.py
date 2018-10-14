# config table

# system config

cfgCmdDis        =   0          # config disable sending commands
cfgDbgSave       =   1          # config save debug info
cfgDRO           =   2          # config dro present
cfgDraw          =   3          # config draw paths
cfgEncoder       =   4          # config encoder counts per revolution
cfgExtDro        =   5          # config external digital readout
cfgFcy           =   6          # config microprocesssor clock frequency
cfgFreqMult      =   7          # config xilinx frequency multiplier
cfgHomeInPlace   =   8          # config home in place
cfgInvEncDir     =   9          # config xilinx invert encoder direction
cfgLCD           =  10          # config enable lcd
cfgMPG           =  11          # config enable manual pulse generator
cfgPrbInv        =  12          # config invert probe signal
cfgRemDbg        =  13          # config print remote debug info
cfgSpEncCap      =  14          # config encoder on capture interrupt
cfgSpEncoder     =  15          # config spindle encoder
cfgSpSync        =  16          # config spindle using timer
cfgSpSyncBoard   =  17          # config spindle sync board
cfgSpUseEncoder  =  18          # config use spindle encoder for threading
cfgTaperCycleDist =  19         # config taper cycle distance
cfgTestMode      =  20          # conifg test mode
cfgTestRPM       =  21          # config xilinx test rpm value
cfgXFreq         =  22          # config xilinx frequency
cfgXilinx        =  23          # config xilinx interface present

# communications config

commPort         =  24          # comm port
commRate         =  25          # comm baud rate

# cutoff config

cuPause          =  26          # cutoff pause before cutting
cuRPM            =  27          # cutoff rpm
cuToolWidth      =  28          # cutoff tool width
cuXEnd           =  29          # cutoff x end
cuXFeed          =  30          # cutoff x feed
cuXRetract       =  31          # cutoff x retract
cuXStart         =  32          # cutoff x start
cuZCutoff        =  33          # cutoff offset to z cutoff
cuZRetract       =  34          # cutoff offset to z retract
cuZStart         =  35          # cutoff z location

# dro position

droXPos          =  36          # dro x position
droZPos          =  37          # dro z position

# external dro

extDroPort       =  38          # external dro port
extDroRate       =  39          # external dro baud Rate

# face config

faAddFeed        =  40          # face 
faPasses         =  41          # face 
faPause          =  42          # face pause before cutting
faRPM            =  43          # face 
faSPInt          =  44          # face 
faSpring         =  45          # face 
faXEnd           =  46          # face 
faXFeed          =  47          # face 
faXRetract       =  48          # face 
faXStart         =  49          # face 
faZEnd           =  50          # face 
faZFeed          =  51          # face 
faZRetract       =  52          # face 
faZStart         =  53          # face 

# jog config

jogInc           =  54          # jog 
jogXPos          =  55          # jog 
jogXPosDiam      =  56          # jog 
jogZPos          =  57          # jog 

# jog panel config

jpSurfaceSpeed   =  58          # jogpanle fpm or rpm
jpXDroDiam       =  59          # jogpanel x dro diameter

# jog time parameters

jogTimeInitial   =  60          # jog time initial
jogTimeInc       =  61          # jog time increment
jogTimeMax       =  62          # jog time max

# keypad

keypadPort       =  63          # external dro port
keypadRate       =  64          # external dro baud Rate

# main panel

mainPanel        =  65          # name of main panel

# spindle config

spAccel          =  66          # spindle acceleration
spAccelTime      =  67          # spindle accelerationtime
spInvDir         =  68          # spindle invert direction
spJogAccelTime   =  69          # spindle jog acceleration time
spJogMax         =  70          # spindle jog max speed
spJogMin         =  71          # spindle jog min speed
spJTimeInc       =  72          # spindle jog increment
spJTimeInitial   =  73          # spindle jog initial time 
spJTimeMax       =  74          # spindle jog max
spMaxRPM         =  75          # spindle jog max rpm
spMicroSteps     =  76          # spindle micro steps
spMinRPM         =  77          # spindle minimum rpm
spMotorSteps     =  78          # spindle motor stpes per revolution
spMotorTest      =  79          # use stepper drive to test motor
spStepDrive      =  80          # spindle stepper drive
spTestEncoder    =  81          # spindle test generate encoder test pulse
spTestIndex      =  82          # spindle test generate internal index pulse

# sync communications config

syncPort         =  83          # sync comm port
syncRate         =  84          # sync comm baud rate

# threading config

thAddFeed        =  85          # thread feed to add after done
thAlternate      =  86          # thread althernate thread flanks
thAngle          =  87          # thread hanlf angle of thread
thFirstFeed      =  88          # thread first feed for thread area calc
thFirstFeedBtn   =  89          # thread button to select first feed
thInternal       =  90          # thread internal threads
thLastFeed       =  91          # thread last feed for thread area calculation
thLastFeedBtn    =  92          # thread button to select last feed
thLeftHand       =  93          # thread left hand 
thMM             =  94          # thread button for mm
thPasses         =  95          # thread number of passes
thPause          =  96          # thread pause between passes
thRPM            =  97          # thread speed for threading operation
thRunout         =  98          # thread runout for rh exit or lh entrance
thSPInt          =  99          # thread spring pass interval
thSpring         = 100          # thread number of spring passes at end
thTPI            = 101          # thread select thread in threads per inch
thThread         = 102          # thread field containing tpi or pitch
thXDepth         = 103          # thread x depth of thread
thXRetract       = 104          # thread x retract
thXStart         = 105          # thread x diameter
thXTaper         = 106          # thread x taper
thZ0             = 107          # thread z right end of thread left start
thZ1             = 108          # thread z right start left end
thZRetract       = 109          # thread z retract

# taper config

tpAddFeed        = 110          # tp 
tpAngle          = 111          # tp 
tpAngleBtn       = 112          # tp 
tpDeltaBtn       = 113          # tp 
tpInternal       = 114          # tp 
tpLargeDiam      = 115          # tp 
tpPasses         = 116          # tp 
tpPause          = 117          # tp 
tpRPM            = 118          # tp 
tpSPInt          = 119          # tp 
tpSmallDiam      = 120          # tp 
tpSpring         = 121          # tp 
tpTaperSel       = 122          # tp 
tpXDelta         = 123          # tp 
tpXFeed          = 124          # tp 
tpXFinish        = 125          # tp 
tpXInFeed        = 126          # tp 
tpXRetract       = 127          # tp 
tpZDelta         = 128          # tp 
tpZFeed          = 129          # tp 
tpZLength        = 130          # tp 
tpZRetract       = 131          # tp 
tpZStart         = 132          # tp 

# turn config

tuAddFeed        = 133          # turn 
tuInternal       = 134          # turn internal
tuPasses         = 135          # turn 
tuPause          = 136          # turn 
tuRPM            = 137          # turn 
tuSPInt          = 138          # turn 
tuSpring         = 139          # turn 
tuXDiam0         = 140          # turn 
tuXDiam1         = 141          # turn 
tuXFeed          = 142          # turn 
tuXRetract       = 143          # turn 
tuZEnd           = 144          # turn 
tuZFeed          = 145          # turn 
tuZRetract       = 146          # turn 
tuZStart         = 147          # turn 

# x axis config

xAccel           = 148          # x axis 
xBacklash        = 149          # x axis 
xDROInch         = 150          # x axis 
xHomeBackoffDist = 151          # x axis 
xHomeDir         = 152          # x axis 
xHomeDist        = 153          # x axis 
xHomeEnd         = 154          # x axis 
xHomeLoc         = 155          # x axis 
xHomeSpeed       = 156          # x axis 
xHomeStart       = 157          # x axis 
xInvDRO          = 158          # x axis invert dro
xInvDir          = 159          # x axis invert stepper direction
xInvEnc          = 160          # x axis 
xInvMpg          = 161          # x axis invert mpg direction
xJogMax          = 162          # x axis 
xJogMin          = 163          # x axis 
xMpgInc          = 164          # x axis jog increment
xMpgMax          = 165          # x axis jog maximum
xJogSpeed        = 166          # x axis 
xMaxSpeed        = 167          # x axis 
xMicroSteps      = 168          # x axis 
xMinSpeed        = 169          # x axis 
xMotorRatio      = 170          # x axis 
xMotorSteps      = 171          # x axis 
xParkLoc         = 172          # x axis 
xPitch           = 173          # x axis 
xProbeDist       = 174          # x axis 

# x axis position config

xSvPosition      = 175          # z axis 
xSvHomeOffset    = 176          # z axis 
xSvDROPosition   = 177          # x axis 
xSvDROOffset     = 178          # x axis 

# z axis config

zAccel           = 179          # z axis 
zBackInc         = 180          # z axis distance to go past for taking out backlash
zBacklash        = 181          # z axis 
zDROInch         = 182          # z axis 
zInvDRO          = 183          # z axis 
zInvDir          = 184          # z axis 
zInvEnc          = 185          # z axis 
zInvMpg          = 186          # z axis 
zJogMax          = 187          # z axis 
zJogMin          = 188          # z axis 
zMpgInc          = 189          # z axis jog increment
zMpgMax          = 190          # z axis jog maximum
zJogSpeed        = 191          # z axis 
zMaxSpeed        = 192          # z axis 
zMicroSteps      = 193          # z axis 
zMinSpeed        = 194          # z axis 
zMotorRatio      = 195          # z axis 
zMotorSteps      = 196          # z axis 
zParkLoc         = 197          # z axis 
zPitch           = 198          # z axis 
zProbeDist       = 199          # z axis 
zProbeSpeed      = 200          # z axis 

# z axis position config

zSvPosition      = 201          # z axis 
zSvHomeOffset    = 202          # z axis 
zSvDROPosition   = 203          # z axis 
zSvDROOffset     = 204          # z axis 

config = { \
    'faPasses' : 41,
    'cfgFreqMult' : 7,
    'spStepDrive' : 80,
    'faZRetract' : 52,
    'tpZFeed' : 129,
    'tuPasses' : 135,
    'thInternal' : 90,
    'cfgSpUseEncoder' : 18,
    'spMicroSteps' : 76,
    'jogXPos' : 55,
    'zJogSpeed' : 191,
    'xMpgInc' : 164,
    'jogZPos' : 57,
    'thAlternate' : 86,
    'jogInc' : 54,
    'tuAddFeed' : 133,
    'tpRPM' : 118,
    'faZStart' : 53,
    'tuZStart' : 147,
    'tpTaperSel' : 122,
    'thXTaper' : 106,
    'tpZRetract' : 131,
    'thXStart' : 105,
    'xHomeStart' : 157,
    'thSPInt' : 99,
    'zMaxSpeed' : 192,
    'cfgTestRPM' : 21,
    'tpLargeDiam' : 115,
    'thSpring' : 100,
    'xHomeEnd' : 154,
    'thAngle' : 87,
    'xMinSpeed' : 169,
    'xHomeDir' : 152,
    'keypadPort' : 63,
    'faZFeed' : 51,
    'cfgSpSync' : 16,
    'thAddFeed' : 85,
    'thRunout' : 98,
    'xJogSpeed' : 166,
    'zMpgInc' : 189,
    'cuXRetract' : 31,
    'tpZStart' : 132,
    'cuToolWidth' : 28,
    'spJogMax' : 70,
    'tuRPM' : 137,
    'thLastFeedBtn' : 92,
    'cfgDraw' : 3,
    'faXFeed' : 47,
    'xSvDROPosition' : 177,
    'cfgXFreq' : 22,
    'tuSPInt' : 138,
    'cfgLCD' : 10,
    'extDroRate' : 39,
    'cfgSpEncCap' : 14,
    'xJogMax' : 162,
    'zInvDir' : 184,
    'tpXInFeed' : 126,
    'thFirstFeed' : 88,
    'xHomeDist' : 153,
    'jogTimeInitial' : 60,
    'faAddFeed' : 40,
    'xJogMin' : 163,
    'xMotorSteps' : 171,
    'faXEnd' : 46,
    'spJogMin' : 71,
    'xPitch' : 173,
    'cfgExtDro' : 5,
    'xSvHomeOffset' : 176,
    'tpAngle' : 111,
    'faXStart' : 49,
    'cfgEncoder' : 4,
    'faSPInt' : 44,
    'tpXFinish' : 125,
    'zSvPosition' : 201,
    'tpAddFeed' : 110,
    'tpDeltaBtn' : 113,
    'thLeftHand' : 93,
    'tpPasses' : 116,
    'xHomeSpeed' : 156,
    'thXRetract' : 104,
    'xHomeBackoffDist' : 151,
    'cfgDRO' : 2,
    'cfgSpSyncBoard' : 17,
    'commPort' : 24,
    'droZPos' : 37,
    'thFirstFeedBtn' : 89,
    'zMinSpeed' : 194,
    'thRPM' : 97,
    'thZ1' : 108,
    'keypadRate' : 64,
    'zSvHomeOffset' : 202,
    'xInvDRO' : 158,
    'tuSpring' : 139,
    'xMotorRatio' : 170,
    'syncPort' : 83,
    'thThread' : 102,
    'cfgDbgSave' : 1,
    'thXDepth' : 103,
    'cuXEnd' : 29,
    'tuPause' : 136,
    'xProbeDist' : 174,
    'xMaxSpeed' : 167,
    'xDROInch' : 150,
    'xInvDir' : 159,
    'tuZFeed' : 145,
    'zInvEnc' : 185,
    'cuZRetract' : 34,
    'zSvDROOffset' : 204,
    'spJTimeInc' : 72,
    'cfgPrbInv' : 12,
    'tpSmallDiam' : 120,
    'tpZLength' : 130,
    'cuXFeed' : 30,
    'zInvMpg' : 186,
    'thPasses' : 95,
    'spMotorSteps' : 78,
    'cuZStart' : 35,
    'tpZDelta' : 128,
    'zAccel' : 179,
    'tpXRetract' : 127,
    'cfgTestMode' : 20,
    'tpXFeed' : 124,
    'thPause' : 96,
    'xInvEnc' : 160,
    'spMinRPM' : 77,
    'tpSpring' : 121,
    'tuZEnd' : 144,
    'tuXFeed' : 142,
    'jogTimeMax' : 62,
    'faSpring' : 45,
    'spJTimeInitial' : 73,
    'cfgXilinx' : 23,
    'thZRetract' : 109,
    'xHomeLoc' : 155,
    'thTPI' : 101,
    'tpXDelta' : 123,
    'tpAngleBtn' : 112,
    'tpPause' : 117,
    'zBacklash' : 181,
    'cfgInvEncDir' : 9,
    'syncRate' : 84,
    'faPause' : 42,
    'thZ0' : 107,
    'zMpgMax' : 190,
    'spTestEncoder' : 81,
    'xMpgMax' : 165,
    'faXRetract' : 48,
    'cuXStart' : 32,
    'cfgHomeInPlace' : 8,
    'jpSurfaceSpeed' : 58,
    'xSvDROOffset' : 178,
    'zParkLoc' : 197,
    'faRPM' : 43,
    'spMaxRPM' : 75,
    'cfgFcy' : 6,
    'zMicroSteps' : 193,
    'thLastFeed' : 91,
    'zDROInch' : 182,
    'tuXRetract' : 143,
    'tuInternal' : 134,
    'extDroPort' : 38,
    'cuRPM' : 27,
    'xInvMpg' : 161,
    'tuZRetract' : 146,
    'tpSPInt' : 119,
    'spTestIndex' : 82,
    'zJogMin' : 188,
    'zMotorRatio' : 195,
    'zPitch' : 198,
    'spInvDir' : 68,
    'spJogAccelTime' : 69,
    'zBackInc' : 180,
    'spJTimeMax' : 74,
    'zSvDROPosition' : 203,
    'xBacklash' : 149,
    'mainPanel' : 65,
    'cfgSpEncoder' : 15,
    'cfgMPG' : 11,
    'jogTimeInc' : 61,
    'zMotorSteps' : 196,
    'jogXPosDiam' : 56,
    'cuZCutoff' : 33,
    'xAccel' : 148,
    'spAccelTime' : 67,
    'zInvDRO' : 183,
    'cuPause' : 26,
    'commRate' : 25,
    'cfgCmdDis' : 0,
    'spAccel' : 66,
    'zJogMax' : 187,
    'droXPos' : 36,
    'zProbeDist' : 199,
    'faZEnd' : 50,
    'xParkLoc' : 172,
    'xSvPosition' : 175,
    'jpXDroDiam' : 59,
    'spMotorTest' : 79,
    'xMicroSteps' : 168,
    'cfgTaperCycleDist' : 19,
    'tpInternal' : 114,
    'cfgRemDbg' : 13,
    'thMM' : 94,
    'zProbeSpeed' : 200,
    'tuXDiam0' : 140,
    'tuXDiam1' : 141,
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
    'cfgSpEncCap',
    'cfgSpEncoder',
    'cfgSpSync',
    'cfgSpSyncBoard',
    'cfgSpUseEncoder',
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
