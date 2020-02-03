# config table

# system config

cfgCmdDis        =   0          # config disable sending commands
cfgDbgSave       =   1          # config save debug info
cfgDRO           =   2          # config dro present
cfgDraw          =   3          # config draw paths
cfgEncoder       =   4          # config encoder counts per revolution
cfgExtDro        =   5          # config external digital readout
cfgFcy           =   6          # config microprocesssor clock frequency
cfgFreqMult      =   7          # config fpga frequency multiplier
cfgHomeInPlace   =   8          # config home in place
cfgInvEncDir     =   9          # config fpga invert encoder direction
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
cfgTestRPM       =  21          # config fpga test rpm value
cfgTurnSync      =  22          # config for turning synchronization
cfgThreadSync    =  23          # config for threading synchronization
cfgXFreq         =  24          # config fpga frequency
cfgFpga          =  25          # config fpga interface present

# communications config

commPort         =  26          # comm port
commRate         =  27          # comm baud rate

# cutoff config

cuPause          =  28          # cutoff pause before cutting
cuRPM            =  29          # cutoff rpm
cuToolWidth      =  30          # cutoff tool width
cuXEnd           =  31          # cutoff x end
cuXFeed          =  32          # cutoff x feed
cuXRetract       =  33          # cutoff x retract
cuXStart         =  34          # cutoff x start
cuZCutoff        =  35          # cutoff offset to z cutoff
cuZRetract       =  36          # cutoff offset to z retract
cuZStart         =  37          # cutoff z location

# dro position

droXPos          =  38          # dro x position
droZPos          =  39          # dro z position

# external dro

extDroPort       =  40          # external dro port
extDroRate       =  41          # external dro baud Rate

# face config

faAddFeed        =  42          # face 
faPasses         =  43          # face 
faPause          =  44          # face pause before cutting
faRPM            =  45          # face 
faSPInt          =  46          # face 
faSpring         =  47          # face 
faXEnd           =  48          # face 
faXFeed          =  49          # face 
faXRetract       =  50          # face 
faXStart         =  51          # face 
faZEnd           =  52          # face 
faZFeed          =  53          # face 
faZRetract       =  54          # face 
faZStart         =  55          # face 

# jog config

jogInc           =  56          # jog 
jogXPos          =  57          # jog 
jogXPosDiam      =  58          # jog 
jogZPos          =  59          # jog 

# jog panel config

jpSurfaceSpeed   =  60          # jogpanle fpm or rpm
jpXDroDiam       =  61          # jogpanel x dro diameter

# jog time parameters

jogTimeInitial   =  62          # jog time initial
jogTimeInc       =  63          # jog time increment
jogTimeMax       =  64          # jog time max

# keypad

keypadPort       =  65          # external dro port
keypadRate       =  66          # external dro baud Rate

# main panel

mainPanel        =  67          # name of main panel

# spindle config

spAccel          =  68          # spindle acceleration
spAccelTime      =  69          # spindle accelerationtime
spCurRange       =  70          # spindle current range
spInvDir         =  71          # spindle invert direction
spJogAccelTime   =  72          # spindle jog acceleration time
spJogMax         =  73          # spindle jog max speed
spJogMin         =  74          # spindle jog min speed
spJTimeInc       =  75          # spindle jog increment
spJTimeInitial   =  76          # spindle jog initial time 
spJTimeMax       =  77          # spindle jog max
spMaxRPM         =  78          # spindle jog max rpm
spMicroSteps     =  79          # spindle micro steps
spMinRPM         =  80          # spindle minimum rpm
spMotorSteps     =  81          # spindle motor stpes per revolution
spMotorTest      =  82          # use stepper drive to test motor
spPWMFreq        =  83          # spindle pwm frequency
spRangeMin1      =  84          # spindle speed range 1 minimum
spRangeMin2      =  85          # spindle speed range 2 minimum
spRangeMin3      =  86          # spindle speed range 3 minimum
spRangeMin4      =  87          # spindle speed range 4 minimum
spRangeMin5      =  88          # spindle speed range 5 minimum
spRangeMin6      =  89          # spindle speed range 6 minimum
spRangeMax1      =  90          # spindle speed range 1 maximum
spRangeMax2      =  91          # spindle speed range 2 maximum
spRangeMax3      =  92          # spindle speed range 3 maximum
spRangeMax4      =  93          # spindle speed range 4 maximum
spRangeMax5      =  94          # spindle speed range 5 maximum
spRangeMax6      =  95          # spindle speed range 6 maximum
spRanges         =  96          # spindle number of speed ranges
spStepDrive      =  97          # spindle stepper drive
spSwitch         =  98          # spindle off on switch
spTestEncoder    =  99          # spindle test generate encoder test pulse
spTestIndex      = 100          # spindle test generate internal index pulse
spVarSpeed       = 101          # spindle variable speed

# sync communications config

syncPort         = 102          # sync comm port
syncRate         = 103          # sync comm baud rate

# threading config

thAddFeed        = 104          # thread feed to add after done
thAlternate      = 105          # thread althernate thread flanks
thAngle          = 106          # thread hanlf angle of thread
thFirstFeed      = 107          # thread first feed for thread area calc
thFirstFeedBtn   = 108          # thread button to select first feed
thInternal       = 109          # thread internal threads
thLastFeed       = 110          # thread last feed for thread area calculation
thLastFeedBtn    = 111          # thread button to select last feed
thLeftHand       = 112          # thread left hand 
thMM             = 113          # thread button for mm
thPasses         = 114          # thread number of passes
thPause          = 115          # thread pause between passes
thRPM            = 116          # thread speed for threading operation
thRunout         = 117          # thread runout for rh exit or lh entrance
thSPInt          = 118          # thread spring pass interval
thSpring         = 119          # thread number of spring passes at end
thTPI            = 120          # thread select thread in threads per inch
thThread         = 121          # thread field containing tpi or pitch
thXDepth         = 122          # thread x depth of thread
thXRetract       = 123          # thread x retract
thXStart         = 124          # thread x diameter
thXTaper         = 125          # thread x taper
thZ0             = 126          # thread z right end of thread left start
thZ1             = 127          # thread z right start left end
thZRetract       = 128          # thread z retract

# taper config

tpAddFeed        = 129          # tp 
tpAngle          = 130          # tp 
tpAngleBtn       = 131          # tp 
tpDeltaBtn       = 132          # tp 
tpInternal       = 133          # tp 
tpLargeDiam      = 134          # tp 
tpPasses         = 135          # tp 
tpPause          = 136          # tp 
tpRPM            = 137          # tp 
tpSPInt          = 138          # tp 
tpSmallDiam      = 139          # tp 
tpSpring         = 140          # tp 
tpTaperSel       = 141          # tp 
tpXDelta         = 142          # tp 
tpXFeed          = 143          # tp 
tpXFinish        = 144          # tp 
tpXInFeed        = 145          # tp 
tpXRetract       = 146          # tp 
tpZDelta         = 147          # tp 
tpZFeed          = 148          # tp 
tpZLength        = 149          # tp 
tpZRetract       = 150          # tp 
tpZStart         = 151          # tp 

# turn config

tuAddFeed        = 152          # turn 
tuInternal       = 153          # turn internal
tuPasses         = 154          # turn 
tuPause          = 155          # turn 
tuRPM            = 156          # turn 
tuSPInt          = 157          # turn 
tuSpring         = 158          # turn 
tuXDiam0         = 159          # turn 
tuXDiam1         = 160          # turn 
tuXFeed          = 161          # turn 
tuXRetract       = 162          # turn 
tuZEnd           = 163          # turn 
tuZFeed          = 164          # turn 
tuZRetract       = 165          # turn 
tuZStart         = 166          # turn 

# x axis config

xAccel           = 167          # x axis 
xBacklash        = 168          # x axis 
xDoneDelay       = 169          # x axis done to read dro delay
xDroFinalDist    = 170          # x dro final approach dist
xDROInch         = 171          # x axis 
xDROPos          = 172          # x axis use dro to go to correct position
xHomeBackoffDist = 173          # x axis 
xHomeDir         = 174          # x axis 
xHomeDist        = 175          # x axis 
xHomeEnd         = 176          # x axis 
xHomeLoc         = 177          # x axis 
xHomeSpeed       = 178          # x axis 
xHomeStart       = 179          # x axis 
xInvDRO          = 180          # x axis invert dro
xInvDir          = 181          # x axis invert stepper direction
xInvEnc          = 182          # x axis 
xInvMpg          = 183          # x axis invert mpg direction
xJogMax          = 184          # x axis 
xJogMin          = 185          # x axis 
xMpgInc          = 186          # x axis jog increment
xMpgMax          = 187          # x axis jog maximum
xJogSpeed        = 188          # x axis 
xMaxSpeed        = 189          # x axis 
xMicroSteps      = 190          # x axis 
xMinSpeed        = 191          # x axis 
xMotorRatio      = 192          # x axis 
xMotorSteps      = 193          # x axis 
xParkLoc         = 194          # x axis 
xPitch           = 195          # x axis 
xProbeDist       = 196          # x axis 

# x axis position config

xSvPosition      = 197          # x axis 
xSvHomeOffset    = 198          # x axis 
xSvDROPosition   = 199          # x axis 
xSvDROOffset     = 200          # x axis 

# z axis config

zAccel           = 201          # z axis 
zBackInc         = 202          # z axis distance to go past for taking out backlash
zBacklash        = 203          # z axis 
zDROInch         = 204          # z axis 
zInvDRO          = 205          # z axis 
zInvDir          = 206          # z axis 
zInvEnc          = 207          # z axis 
zInvMpg          = 208          # z axis 
zJogMax          = 209          # z axis 
zJogMin          = 210          # z axis 
zMpgInc          = 211          # z axis jog increment
zMpgMax          = 212          # z axis jog maximum
zJogSpeed        = 213          # z axis 
zMaxSpeed        = 214          # z axis 
zMicroSteps      = 215          # z axis 
zMinSpeed        = 216          # z axis 
zMotorRatio      = 217          # z axis 
zMotorSteps      = 218          # z axis 
zParkLoc         = 219          # z axis 
zPitch           = 220          # z axis 
zProbeDist       = 221          # z axis 
zProbeSpeed      = 222          # z axis 
zDROPos          = 223          # z axis use dro to go to correct position

# z axis position config

zSvPosition      = 224          # z axis 
zSvHomeOffset    = 225          # z axis 
zSvDROPosition   = 226          # z axis 
zSvDROOffset     = 227          # z axis 

config = { \
    'cfgCmdDis' : 0,
    'cfgDbgSave' : 1,
    'cfgDRO' : 2,
    'cfgDraw' : 3,
    'cfgEncoder' : 4,
    'cfgExtDro' : 5,
    'cfgFcy' : 6,
    'cfgFreqMult' : 7,
    'cfgHomeInPlace' : 8,
    'cfgInvEncDir' : 9,
    'cfgLCD' : 10,
    'cfgMPG' : 11,
    'cfgPrbInv' : 12,
    'cfgRemDbg' : 13,
    'cfgSpEncCap' : 14,
    'cfgSpEncoder' : 15,
    'cfgSpSync' : 16,
    'cfgSpSyncBoard' : 17,
    'cfgSpUseEncoder' : 18,
    'cfgTaperCycleDist' : 19,
    'cfgTestMode' : 20,
    'cfgTestRPM' : 21,
    'cfgTurnSync' : 22,
    'cfgThreadSync' : 23,
    'cfgXFreq' : 24,
    'cfgFpga' : 25,
    'commPort' : 26,
    'commRate' : 27,
    'cuPause' : 28,
    'cuRPM' : 29,
    'cuToolWidth' : 30,
    'cuXEnd' : 31,
    'cuXFeed' : 32,
    'cuXRetract' : 33,
    'cuXStart' : 34,
    'cuZCutoff' : 35,
    'cuZRetract' : 36,
    'cuZStart' : 37,
    'droXPos' : 38,
    'droZPos' : 39,
    'extDroPort' : 40,
    'extDroRate' : 41,
    'faAddFeed' : 42,
    'faPasses' : 43,
    'faPause' : 44,
    'faRPM' : 45,
    'faSPInt' : 46,
    'faSpring' : 47,
    'faXEnd' : 48,
    'faXFeed' : 49,
    'faXRetract' : 50,
    'faXStart' : 51,
    'faZEnd' : 52,
    'faZFeed' : 53,
    'faZRetract' : 54,
    'faZStart' : 55,
    'jogInc' : 56,
    'jogXPos' : 57,
    'jogXPosDiam' : 58,
    'jogZPos' : 59,
    'jpSurfaceSpeed' : 60,
    'jpXDroDiam' : 61,
    'jogTimeInitial' : 62,
    'jogTimeInc' : 63,
    'jogTimeMax' : 64,
    'keypadPort' : 65,
    'keypadRate' : 66,
    'mainPanel' : 67,
    'spAccel' : 68,
    'spAccelTime' : 69,
    'spCurRange' : 70,
    'spInvDir' : 71,
    'spJogAccelTime' : 72,
    'spJogMax' : 73,
    'spJogMin' : 74,
    'spJTimeInc' : 75,
    'spJTimeInitial' : 76,
    'spJTimeMax' : 77,
    'spMaxRPM' : 78,
    'spMicroSteps' : 79,
    'spMinRPM' : 80,
    'spMotorSteps' : 81,
    'spMotorTest' : 82,
    'spPWMFreq' : 83,
    'spRangeMin1' : 84,
    'spRangeMin2' : 85,
    'spRangeMin3' : 86,
    'spRangeMin4' : 87,
    'spRangeMin5' : 88,
    'spRangeMin6' : 89,
    'spRangeMax1' : 90,
    'spRangeMax2' : 91,
    'spRangeMax3' : 92,
    'spRangeMax4' : 93,
    'spRangeMax5' : 94,
    'spRangeMax6' : 95,
    'spRanges' : 96,
    'spStepDrive' : 97,
    'spSwitch' : 98,
    'spTestEncoder' : 99,
    'spTestIndex' : 100,
    'spVarSpeed' : 101,
    'syncPort' : 102,
    'syncRate' : 103,
    'thAddFeed' : 104,
    'thAlternate' : 105,
    'thAngle' : 106,
    'thFirstFeed' : 107,
    'thFirstFeedBtn' : 108,
    'thInternal' : 109,
    'thLastFeed' : 110,
    'thLastFeedBtn' : 111,
    'thLeftHand' : 112,
    'thMM' : 113,
    'thPasses' : 114,
    'thPause' : 115,
    'thRPM' : 116,
    'thRunout' : 117,
    'thSPInt' : 118,
    'thSpring' : 119,
    'thTPI' : 120,
    'thThread' : 121,
    'thXDepth' : 122,
    'thXRetract' : 123,
    'thXStart' : 124,
    'thXTaper' : 125,
    'thZ0' : 126,
    'thZ1' : 127,
    'thZRetract' : 128,
    'tpAddFeed' : 129,
    'tpAngle' : 130,
    'tpAngleBtn' : 131,
    'tpDeltaBtn' : 132,
    'tpInternal' : 133,
    'tpLargeDiam' : 134,
    'tpPasses' : 135,
    'tpPause' : 136,
    'tpRPM' : 137,
    'tpSPInt' : 138,
    'tpSmallDiam' : 139,
    'tpSpring' : 140,
    'tpTaperSel' : 141,
    'tpXDelta' : 142,
    'tpXFeed' : 143,
    'tpXFinish' : 144,
    'tpXInFeed' : 145,
    'tpXRetract' : 146,
    'tpZDelta' : 147,
    'tpZFeed' : 148,
    'tpZLength' : 149,
    'tpZRetract' : 150,
    'tpZStart' : 151,
    'tuAddFeed' : 152,
    'tuInternal' : 153,
    'tuPasses' : 154,
    'tuPause' : 155,
    'tuRPM' : 156,
    'tuSPInt' : 157,
    'tuSpring' : 158,
    'tuXDiam0' : 159,
    'tuXDiam1' : 160,
    'tuXFeed' : 161,
    'tuXRetract' : 162,
    'tuZEnd' : 163,
    'tuZFeed' : 164,
    'tuZRetract' : 165,
    'tuZStart' : 166,
    'xAccel' : 167,
    'xBacklash' : 168,
    'xDoneDelay' : 169,
    'xDroFinalDist' : 170,
    'xDROInch' : 171,
    'xDROPos' : 172,
    'xHomeBackoffDist' : 173,
    'xHomeDir' : 174,
    'xHomeDist' : 175,
    'xHomeEnd' : 176,
    'xHomeLoc' : 177,
    'xHomeSpeed' : 178,
    'xHomeStart' : 179,
    'xInvDRO' : 180,
    'xInvDir' : 181,
    'xInvEnc' : 182,
    'xInvMpg' : 183,
    'xJogMax' : 184,
    'xJogMin' : 185,
    'xMpgInc' : 186,
    'xMpgMax' : 187,
    'xJogSpeed' : 188,
    'xMaxSpeed' : 189,
    'xMicroSteps' : 190,
    'xMinSpeed' : 191,
    'xMotorRatio' : 192,
    'xMotorSteps' : 193,
    'xParkLoc' : 194,
    'xPitch' : 195,
    'xProbeDist' : 196,
    'xSvPosition' : 197,
    'xSvHomeOffset' : 198,
    'xSvDROPosition' : 199,
    'xSvDROOffset' : 200,
    'zAccel' : 201,
    'zBackInc' : 202,
    'zBacklash' : 203,
    'zDROInch' : 204,
    'zInvDRO' : 205,
    'zInvDir' : 206,
    'zInvEnc' : 207,
    'zInvMpg' : 208,
    'zJogMax' : 209,
    'zJogMin' : 210,
    'zMpgInc' : 211,
    'zMpgMax' : 212,
    'zJogSpeed' : 213,
    'zMaxSpeed' : 214,
    'zMicroSteps' : 215,
    'zMinSpeed' : 216,
    'zMotorRatio' : 217,
    'zMotorSteps' : 218,
    'zParkLoc' : 219,
    'zPitch' : 220,
    'zProbeDist' : 221,
    'zProbeSpeed' : 222,
    'zDROPos' : 223,
    'zSvPosition' : 224,
    'zSvHomeOffset' : 225,
    'zSvDROPosition' : 226,
    'zSvDROOffset' : 227,
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
    'cfgTurnSync',
    'cfgThreadSync',
    'cfgXFreq',
    'cfgFpga',
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
    'spCurRange',
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
    'spPWMFreq',
    'spRangeMin1',
    'spRangeMin2',
    'spRangeMin3',
    'spRangeMin4',
    'spRangeMin5',
    'spRangeMin6',
    'spRangeMax1',
    'spRangeMax2',
    'spRangeMax3',
    'spRangeMax4',
    'spRangeMax5',
    'spRangeMax6',
    'spRanges',
    'spStepDrive',
    'spSwitch',
    'spTestEncoder',
    'spTestIndex',
    'spVarSpeed',
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
    'xDoneDelay',
    'xDroFinalDist',
    'xDROInch',
    'xDROPos',
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
    'zDROPos',
    'zSvPosition',
    'zSvHomeOffset',
    'zSvDROPosition',
    'zSvDROOffset',
    )
