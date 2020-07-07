# config table

# system config

cfgCmdDis        =   0          # config disable sending commands
cfgDbgSave       =   1          # config save debug info
cfgDRO           =   2          # config dro present
cfgDraw          =   3          # config draw paths
cfgEncoder       =   4          # config encoder counts per revolution
cfgEStop         =   5          # config estop enable
cfgEStopInv      =   6          # config estop invert
cfgExtDro        =   7          # config external digital readout
cfgFcy           =   8          # config microprocesssor clock frequency
cfgFreqMult      =   9          # config fpga frequency multiplier
cfgHomeInPlace   =  10          # config home in place
cfgInvEncDir     =  11          # config fpga invert encoder direction
cfgLCD           =  12          # config enable lcd
cfgMPG           =  13          # config enable manual pulse generator
cfgPrbInv        =  14          # config invert probe signal
cfgRemDbg        =  15          # config print remote debug info
cfgSpEncCap      =  16          # config encoder on capture interrupt
cfgSpEncoder     =  17          # config spindle encoder
cfgSpSync        =  18          # config spindle using timer
cfgSpSyncBoard   =  19          # config spindle sync board
cfgSpUseEncoder  =  20          # config use spindle encoder for threading
cfgTaperCycleDist =  21         # config taper cycle distance
cfgTestMode      =  22          # conifg test mode
cfgTestRPM       =  23          # config fpga test rpm value
cfgTurnSync      =  24          # config for turning synchronization
cfgThreadSync    =  25          # config for threading synchronization
cfgFpgaFreq      =  26          # config fpga frequency
cfgFpga          =  27          # config fpga interface present

# communications config

commPort         =  28          # comm port
commRate         =  29          # comm baud rate

# cutoff config

cuPause          =  30          # cutoff pause before cutting
cuRPM            =  31          # cutoff rpm
cuToolWidth      =  32          # cutoff tool width
cuXEnd           =  33          # cutoff x end
cuXFeed          =  34          # cutoff x feed
cuXRetract       =  35          # cutoff x retract
cuXStart         =  36          # cutoff x start
cuZCutoff        =  37          # cutoff offset to z cutoff
cuZRetract       =  38          # cutoff offset to z retract
cuZStart         =  39          # cutoff z location

# dro position

droXPos          =  40          # dro x position
droZPos          =  41          # dro z position

# external dro

extDroPort       =  42          # external dro port
extDroRate       =  43          # external dro baud Rate

# face config

faAddFeed        =  44          # face 
faPasses         =  45          # face 
faPause          =  46          # face pause before cutting
faRPM            =  47          # face 
faSPInt          =  48          # face 
faSpring         =  49          # face 
faXEnd           =  50          # face 
faXFeed          =  51          # face 
faXRetract       =  52          # face 
faXStart         =  53          # face 
faZEnd           =  54          # face 
faZFeed          =  55          # face 
faZRetract       =  56          # face 
faZStart         =  57          # face 

# jog config

jogInc           =  58          # jog 
jogXPos          =  59          # jog 
jogXPosDiam      =  60          # jog 
jogZPos          =  61          # jog 

# jog panel config

jpSurfaceSpeed   =  62          # jogpanle fpm or rpm
jpXDroDiam       =  63          # jogpanel x dro diameter

# jog time parameters

jogTimeInitial   =  64          # jog time initial
jogTimeInc       =  65          # jog time increment
jogTimeMax       =  66          # jog time max

# keypad

keypadPort       =  67          # external dro port
keypadRate       =  68          # external dro baud Rate

# main panel

mainPanel        =  69          # name of main panel

# spindle config

spAccel          =  70          # spindle acceleration
spAccelTime      =  71          # spindle accelerationtime
spCurRange       =  72          # spindle current range
spInvDir         =  73          # spindle invert direction
spJogAccelTime   =  74          # spindle jog acceleration time
spJogMax         =  75          # spindle jog max speed
spJogMin         =  76          # spindle jog min speed
spJTimeInc       =  77          # spindle jog increment
spJTimeInitial   =  78          # spindle jog initial time 
spJTimeMax       =  79          # spindle jog max
spMaxRPM         =  80          # spindle jog max rpm
spMicroSteps     =  81          # spindle micro steps
spMinRPM         =  82          # spindle minimum rpm
spMotorSteps     =  83          # spindle motor stpes per revolution
spMotorTest      =  84          # use stepper drive to test motor
spPWMFreq        =  85          # spindle pwm frequency
spRangeMin1      =  86          # spindle speed range 1 minimum
spRangeMin2      =  87          # spindle speed range 2 minimum
spRangeMin3      =  88          # spindle speed range 3 minimum
spRangeMin4      =  89          # spindle speed range 4 minimum
spRangeMin5      =  90          # spindle speed range 5 minimum
spRangeMin6      =  91          # spindle speed range 6 minimum
spRangeMax1      =  92          # spindle speed range 1 maximum
spRangeMax2      =  93          # spindle speed range 2 maximum
spRangeMax3      =  94          # spindle speed range 3 maximum
spRangeMax4      =  95          # spindle speed range 4 maximum
spRangeMax5      =  96          # spindle speed range 5 maximum
spRangeMax6      =  97          # spindle speed range 6 maximum
spRanges         =  98          # spindle number of speed ranges
spStepDrive      =  99          # spindle stepper drive
spSwitch         = 100          # spindle off on switch
spTestEncoder    = 101          # spindle test generate encoder test pulse
spTestIndex      = 102          # spindle test generate internal index pulse
spVarSpeed       = 103          # spindle variable speed

# sync communications config

syncPort         = 104          # sync comm port
syncRate         = 105          # sync comm baud rate

# threading config

thAddFeed        = 106          # thread feed to add after done
thAlternate      = 107          # thread althernate thread flanks
thAngle          = 108          # thread hanlf angle of thread
thFirstFeed      = 109          # thread first feed for thread area calc
thFirstFeedBtn   = 110          # thread button to select first feed
thInternal       = 111          # thread internal threads
thLastFeed       = 112          # thread last feed for thread area calculation
thLastFeedBtn    = 113          # thread button to select last feed
thLeftHand       = 114          # thread left hand 
thMM             = 115          # thread button for mm
thPasses         = 116          # thread number of passes
thPause          = 117          # thread pause between passes
thRPM            = 118          # thread speed for threading operation
thRunout         = 119          # thread runout for rh exit or lh entrance
thSPInt          = 120          # thread spring pass interval
thSpring         = 121          # thread number of spring passes at end
thTPI            = 122          # thread select thread in threads per inch
thThread         = 123          # thread field containing tpi or pitch
thXDepth         = 124          # thread x depth of thread
thXRetract       = 125          # thread x retract
thXStart         = 126          # thread x diameter
thXTaper         = 127          # thread x taper
thZ0             = 128          # thread z right end of thread left start
thZ1             = 129          # thread z right start left end
thZRetract       = 130          # thread z retract

# taper config

tpAddFeed        = 131          # tp 
tpAngle          = 132          # tp 
tpAngleBtn       = 133          # tp 
tpDeltaBtn       = 134          # tp 
tpInternal       = 135          # tp 
tpLargeDiam      = 136          # tp 
tpPasses         = 137          # tp 
tpPause          = 138          # tp 
tpRPM            = 139          # tp 
tpSPInt          = 140          # tp 
tpSmallDiam      = 141          # tp 
tpSpring         = 142          # tp 
tpTaperSel       = 143          # tp 
tpXDelta         = 144          # tp 
tpXFeed          = 145          # tp 
tpXFinish        = 146          # tp 
tpXInFeed        = 147          # tp 
tpXRetract       = 148          # tp 
tpZDelta         = 149          # tp 
tpZFeed          = 150          # tp 
tpZLength        = 151          # tp 
tpZRetract       = 152          # tp 
tpZStart         = 153          # tp 

# turn config

tuAddFeed        = 154          # turn 
tuInternal       = 155          # turn internal
tuPasses         = 156          # turn 
tuPause          = 157          # turn 
tuRPM            = 158          # turn 
tuSPInt          = 159          # turn 
tuSpring         = 160          # turn 
tuXDiam0         = 161          # turn 
tuXDiam1         = 162          # turn 
tuXFeed          = 163          # turn 
tuXRetract       = 164          # turn 
tuZEnd           = 165          # turn 
tuZFeed          = 166          # turn 
tuZRetract       = 167          # turn 
tuZStart         = 168          # turn 

# x axis config

xAccel           = 169          # x axis 
xBacklash        = 170          # x axis 
xDoneDelay       = 171          # x axis done to read dro delay
xDroFinalDist    = 172          # x dro final approach dist
xDROInch         = 173          # x axis 
xDROPos          = 174          # x axis use dro to go to correct position
xHomeBackoffDist = 175          # x axis 
xHomeDir         = 176          # x axis 
xHomeDist        = 177          # x axis 
xHomeEna         = 178          # x axis 
xHomeEnd         = 179          # x axis 
xHomeInv         = 180          # x axis 
xHomeLoc         = 181          # x axis 
xHomeSpeed       = 182          # x axis 
xHomeStart       = 183          # x axis 
xInvDRO          = 184          # x axis invert dro
xInvDir          = 185          # x axis invert stepper direction
xInvEnc          = 186          # x axis 
xInvMpg          = 187          # x axis invert mpg direction
xJogMax          = 188          # x axis 
xJogMin          = 189          # x axis 
xLimEna          = 190          # x axis limits enable
xLimNegInv       = 191          # x axis negative limit invert
xLimPosInv       = 192          # x axis positive limit invert
xMpgInc          = 193          # x axis jog increment
xMpgMax          = 194          # x axis jog maximum
xJogSpeed        = 195          # x axis 
xMaxSpeed        = 196          # x axis 
xMicroSteps      = 197          # x axis 
xMinSpeed        = 198          # x axis 
xMotorRatio      = 199          # x axis 
xMotorSteps      = 200          # x axis 
xParkLoc         = 201          # x axis 
xPitch           = 202          # x axis 
xProbeDist       = 203          # x axis 

# x axis position config

xSvPosition      = 204          # x axis 
xSvHomeOffset    = 205          # x axis 
xSvDROPosition   = 206          # x axis 
xSvDROOffset     = 207          # x axis 

# z axis config

zAccel           = 208          # z axis 
zBackInc         = 209          # z axis distance to go past for taking out backlash
zBacklash        = 210          # z axis 
zDROInch         = 211          # z axis 
zHomeEna         = 212          # z axis 
zHomeInv         = 213          # z axis 
zInvDRO          = 214          # z axis 
zInvDir          = 215          # z axis 
zInvEnc          = 216          # z axis 
zInvMpg          = 217          # z axis 
zJogMax          = 218          # z axis 
zJogMin          = 219          # z axis 
zMpgInc          = 220          # z axis jog increment
zMpgMax          = 221          # z axis jog maximum
zJogSpeed        = 222          # z axis 
zLimEna          = 223          # z axis limits enable
zLimNegInv       = 224          # z axis negative limit invert
zLimPosInv       = 225          # z axis positive limit invert
zMaxSpeed        = 226          # z axis 
zMicroSteps      = 227          # z axis 
zMinSpeed        = 228          # z axis 
zMotorRatio      = 229          # z axis 
zMotorSteps      = 230          # z axis 
zParkLoc         = 231          # z axis 
zPitch           = 232          # z axis 
zProbeDist       = 233          # z axis 
zProbeSpeed      = 234          # z axis 
zDROPos          = 235          # z axis use dro to go to correct position

# z axis position config

zSvPosition      = 236          # z axis 
zSvHomeOffset    = 237          # z axis 
zSvDROPosition   = 238          # z axis 
zSvDROOffset     = 239          # z axis 
cfgJogDebug      = 240          # debug jogging

config = { \
    'cfgCmdDis' : 0,
    'cfgDbgSave' : 1,
    'cfgDRO' : 2,
    'cfgDraw' : 3,
    'cfgEncoder' : 4,
    'cfgEStop' : 5,
    'cfgEStopInv' : 6,
    'cfgExtDro' : 7,
    'cfgFcy' : 8,
    'cfgFreqMult' : 9,
    'cfgHomeInPlace' : 10,
    'cfgInvEncDir' : 11,
    'cfgLCD' : 12,
    'cfgMPG' : 13,
    'cfgPrbInv' : 14,
    'cfgRemDbg' : 15,
    'cfgSpEncCap' : 16,
    'cfgSpEncoder' : 17,
    'cfgSpSync' : 18,
    'cfgSpSyncBoard' : 19,
    'cfgSpUseEncoder' : 20,
    'cfgTaperCycleDist' : 21,
    'cfgTestMode' : 22,
    'cfgTestRPM' : 23,
    'cfgTurnSync' : 24,
    'cfgThreadSync' : 25,
    'cfgFpgaFreq' : 26,
    'cfgFpga' : 27,
    'commPort' : 28,
    'commRate' : 29,
    'cuPause' : 30,
    'cuRPM' : 31,
    'cuToolWidth' : 32,
    'cuXEnd' : 33,
    'cuXFeed' : 34,
    'cuXRetract' : 35,
    'cuXStart' : 36,
    'cuZCutoff' : 37,
    'cuZRetract' : 38,
    'cuZStart' : 39,
    'droXPos' : 40,
    'droZPos' : 41,
    'extDroPort' : 42,
    'extDroRate' : 43,
    'faAddFeed' : 44,
    'faPasses' : 45,
    'faPause' : 46,
    'faRPM' : 47,
    'faSPInt' : 48,
    'faSpring' : 49,
    'faXEnd' : 50,
    'faXFeed' : 51,
    'faXRetract' : 52,
    'faXStart' : 53,
    'faZEnd' : 54,
    'faZFeed' : 55,
    'faZRetract' : 56,
    'faZStart' : 57,
    'jogInc' : 58,
    'jogXPos' : 59,
    'jogXPosDiam' : 60,
    'jogZPos' : 61,
    'jpSurfaceSpeed' : 62,
    'jpXDroDiam' : 63,
    'jogTimeInitial' : 64,
    'jogTimeInc' : 65,
    'jogTimeMax' : 66,
    'keypadPort' : 67,
    'keypadRate' : 68,
    'mainPanel' : 69,
    'spAccel' : 70,
    'spAccelTime' : 71,
    'spCurRange' : 72,
    'spInvDir' : 73,
    'spJogAccelTime' : 74,
    'spJogMax' : 75,
    'spJogMin' : 76,
    'spJTimeInc' : 77,
    'spJTimeInitial' : 78,
    'spJTimeMax' : 79,
    'spMaxRPM' : 80,
    'spMicroSteps' : 81,
    'spMinRPM' : 82,
    'spMotorSteps' : 83,
    'spMotorTest' : 84,
    'spPWMFreq' : 85,
    'spRangeMin1' : 86,
    'spRangeMin2' : 87,
    'spRangeMin3' : 88,
    'spRangeMin4' : 89,
    'spRangeMin5' : 90,
    'spRangeMin6' : 91,
    'spRangeMax1' : 92,
    'spRangeMax2' : 93,
    'spRangeMax3' : 94,
    'spRangeMax4' : 95,
    'spRangeMax5' : 96,
    'spRangeMax6' : 97,
    'spRanges' : 98,
    'spStepDrive' : 99,
    'spSwitch' : 100,
    'spTestEncoder' : 101,
    'spTestIndex' : 102,
    'spVarSpeed' : 103,
    'syncPort' : 104,
    'syncRate' : 105,
    'thAddFeed' : 106,
    'thAlternate' : 107,
    'thAngle' : 108,
    'thFirstFeed' : 109,
    'thFirstFeedBtn' : 110,
    'thInternal' : 111,
    'thLastFeed' : 112,
    'thLastFeedBtn' : 113,
    'thLeftHand' : 114,
    'thMM' : 115,
    'thPasses' : 116,
    'thPause' : 117,
    'thRPM' : 118,
    'thRunout' : 119,
    'thSPInt' : 120,
    'thSpring' : 121,
    'thTPI' : 122,
    'thThread' : 123,
    'thXDepth' : 124,
    'thXRetract' : 125,
    'thXStart' : 126,
    'thXTaper' : 127,
    'thZ0' : 128,
    'thZ1' : 129,
    'thZRetract' : 130,
    'tpAddFeed' : 131,
    'tpAngle' : 132,
    'tpAngleBtn' : 133,
    'tpDeltaBtn' : 134,
    'tpInternal' : 135,
    'tpLargeDiam' : 136,
    'tpPasses' : 137,
    'tpPause' : 138,
    'tpRPM' : 139,
    'tpSPInt' : 140,
    'tpSmallDiam' : 141,
    'tpSpring' : 142,
    'tpTaperSel' : 143,
    'tpXDelta' : 144,
    'tpXFeed' : 145,
    'tpXFinish' : 146,
    'tpXInFeed' : 147,
    'tpXRetract' : 148,
    'tpZDelta' : 149,
    'tpZFeed' : 150,
    'tpZLength' : 151,
    'tpZRetract' : 152,
    'tpZStart' : 153,
    'tuAddFeed' : 154,
    'tuInternal' : 155,
    'tuPasses' : 156,
    'tuPause' : 157,
    'tuRPM' : 158,
    'tuSPInt' : 159,
    'tuSpring' : 160,
    'tuXDiam0' : 161,
    'tuXDiam1' : 162,
    'tuXFeed' : 163,
    'tuXRetract' : 164,
    'tuZEnd' : 165,
    'tuZFeed' : 166,
    'tuZRetract' : 167,
    'tuZStart' : 168,
    'xAccel' : 169,
    'xBacklash' : 170,
    'xDoneDelay' : 171,
    'xDroFinalDist' : 172,
    'xDROInch' : 173,
    'xDROPos' : 174,
    'xHomeBackoffDist' : 175,
    'xHomeDir' : 176,
    'xHomeDist' : 177,
    'xHomeEna' : 178,
    'xHomeEnd' : 179,
    'xHomeInv' : 180,
    'xHomeLoc' : 181,
    'xHomeSpeed' : 182,
    'xHomeStart' : 183,
    'xInvDRO' : 184,
    'xInvDir' : 185,
    'xInvEnc' : 186,
    'xInvMpg' : 187,
    'xJogMax' : 188,
    'xJogMin' : 189,
    'xLimEna' : 190,
    'xLimNegInv' : 191,
    'xLimPosInv' : 192,
    'xMpgInc' : 193,
    'xMpgMax' : 194,
    'xJogSpeed' : 195,
    'xMaxSpeed' : 196,
    'xMicroSteps' : 197,
    'xMinSpeed' : 198,
    'xMotorRatio' : 199,
    'xMotorSteps' : 200,
    'xParkLoc' : 201,
    'xPitch' : 202,
    'xProbeDist' : 203,
    'xSvPosition' : 204,
    'xSvHomeOffset' : 205,
    'xSvDROPosition' : 206,
    'xSvDROOffset' : 207,
    'zAccel' : 208,
    'zBackInc' : 209,
    'zBacklash' : 210,
    'zDROInch' : 211,
    'zHomeEna' : 212,
    'zHomeInv' : 213,
    'zInvDRO' : 214,
    'zInvDir' : 215,
    'zInvEnc' : 216,
    'zInvMpg' : 217,
    'zJogMax' : 218,
    'zJogMin' : 219,
    'zMpgInc' : 220,
    'zMpgMax' : 221,
    'zJogSpeed' : 222,
    'zLimEna' : 223,
    'zLimNegInv' : 224,
    'zLimPosInv' : 225,
    'zMaxSpeed' : 226,
    'zMicroSteps' : 227,
    'zMinSpeed' : 228,
    'zMotorRatio' : 229,
    'zMotorSteps' : 230,
    'zParkLoc' : 231,
    'zPitch' : 232,
    'zProbeDist' : 233,
    'zProbeSpeed' : 234,
    'zDROPos' : 235,
    'zSvPosition' : 236,
    'zSvHomeOffset' : 237,
    'zSvDROPosition' : 238,
    'zSvDROOffset' : 239,
    'cfgJogDebug' : 240,
    }

configTable = ( \
    'cfgCmdDis',
    'cfgDbgSave',
    'cfgDRO',
    'cfgDraw',
    'cfgEncoder',
    'cfgEStop',
    'cfgEStopInv',
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
    'cfgFpgaFreq',
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
    'xHomeEna',
    'xHomeEnd',
    'xHomeInv',
    'xHomeLoc',
    'xHomeSpeed',
    'xHomeStart',
    'xInvDRO',
    'xInvDir',
    'xInvEnc',
    'xInvMpg',
    'xJogMax',
    'xJogMin',
    'xLimEna',
    'xLimNegInv',
    'xLimPosInv',
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
    'zHomeEna',
    'zHomeInv',
    'zInvDRO',
    'zInvDir',
    'zInvEnc',
    'zInvMpg',
    'zJogMax',
    'zJogMin',
    'zMpgInc',
    'zMpgMax',
    'zJogSpeed',
    'zLimEna',
    'zLimNegInv',
    'zLimPosInv',
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
    'cfgJogDebug',
    )
