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
spCurRange       =  68          # spindle current range
spInvDir         =  69          # spindle invert direction
spJogAccelTime   =  70          # spindle jog acceleration time
spJogMax         =  71          # spindle jog max speed
spJogMin         =  72          # spindle jog min speed
spJTimeInc       =  73          # spindle jog increment
spJTimeInitial   =  74          # spindle jog initial time 
spJTimeMax       =  75          # spindle jog max
spMaxRPM         =  76          # spindle jog max rpm
spMicroSteps     =  77          # spindle micro steps
spMinRPM         =  78          # spindle minimum rpm
spMotorSteps     =  79          # spindle motor stpes per revolution
spMotorTest      =  80          # use stepper drive to test motor
spPWMFreq        =  81          # spindle pwm frequency
spRangeMin1      =  82          # spindle speed range 1 minimum
spRangeMin2      =  83          # spindle speed range 2 minimum
spRangeMin3      =  84          # spindle speed range 3 minimum
spRangeMin4      =  85          # spindle speed range 4 minimum
spRangeMin5      =  86          # spindle speed range 5 minimum
spRangeMin6      =  87          # spindle speed range 6 minimum
spRangeMax1      =  88          # spindle speed range 1 maximum
spRangeMax2      =  89          # spindle speed range 2 maximum
spRangeMax3      =  90          # spindle speed range 3 maximum
spRangeMax4      =  91          # spindle speed range 4 maximum
spRangeMax5      =  92          # spindle speed range 5 maximum
spRangeMax6      =  93          # spindle speed range 6 maximum
spRanges         =  94          # spindle number of speed ranges
spStepDrive      =  95          # spindle stepper drive
spSwitch         =  96          # spindle off on switch
spTestEncoder    =  97          # spindle test generate encoder test pulse
spTestIndex      =  98          # spindle test generate internal index pulse
spVarSpeed       =  99          # spindle variable speed

# sync communications config

syncPort         = 100          # sync comm port
syncRate         = 101          # sync comm baud rate

# threading config

thAddFeed        = 102          # thread feed to add after done
thAlternate      = 103          # thread althernate thread flanks
thAngle          = 104          # thread hanlf angle of thread
thFirstFeed      = 105          # thread first feed for thread area calc
thFirstFeedBtn   = 106          # thread button to select first feed
thInternal       = 107          # thread internal threads
thLastFeed       = 108          # thread last feed for thread area calculation
thLastFeedBtn    = 109          # thread button to select last feed
thLeftHand       = 110          # thread left hand 
thMM             = 111          # thread button for mm
thPasses         = 112          # thread number of passes
thPause          = 113          # thread pause between passes
thRPM            = 114          # thread speed for threading operation
thRunout         = 115          # thread runout for rh exit or lh entrance
thSPInt          = 116          # thread spring pass interval
thSpring         = 117          # thread number of spring passes at end
thTPI            = 118          # thread select thread in threads per inch
thThread         = 119          # thread field containing tpi or pitch
thXDepth         = 120          # thread x depth of thread
thXRetract       = 121          # thread x retract
thXStart         = 122          # thread x diameter
thXTaper         = 123          # thread x taper
thZ0             = 124          # thread z right end of thread left start
thZ1             = 125          # thread z right start left end
thZRetract       = 126          # thread z retract

# taper config

tpAddFeed        = 127          # tp 
tpAngle          = 128          # tp 
tpAngleBtn       = 129          # tp 
tpDeltaBtn       = 130          # tp 
tpInternal       = 131          # tp 
tpLargeDiam      = 132          # tp 
tpPasses         = 133          # tp 
tpPause          = 134          # tp 
tpRPM            = 135          # tp 
tpSPInt          = 136          # tp 
tpSmallDiam      = 137          # tp 
tpSpring         = 138          # tp 
tpTaperSel       = 139          # tp 
tpXDelta         = 140          # tp 
tpXFeed          = 141          # tp 
tpXFinish        = 142          # tp 
tpXInFeed        = 143          # tp 
tpXRetract       = 144          # tp 
tpZDelta         = 145          # tp 
tpZFeed          = 146          # tp 
tpZLength        = 147          # tp 
tpZRetract       = 148          # tp 
tpZStart         = 149          # tp 

# turn config

tuAddFeed        = 150          # turn 
tuInternal       = 151          # turn internal
tuPasses         = 152          # turn 
tuPause          = 153          # turn 
tuRPM            = 154          # turn 
tuSPInt          = 155          # turn 
tuSpring         = 156          # turn 
tuXDiam0         = 157          # turn 
tuXDiam1         = 158          # turn 
tuXFeed          = 159          # turn 
tuXRetract       = 160          # turn 
tuZEnd           = 161          # turn 
tuZFeed          = 162          # turn 
tuZRetract       = 163          # turn 
tuZStart         = 164          # turn 

# x axis config

xAccel           = 165          # x axis 
xBacklash        = 166          # x axis 
xDROInch         = 167          # x axis 
xHomeBackoffDist = 168          # x axis 
xHomeDir         = 169          # x axis 
xHomeDist        = 170          # x axis 
xHomeEnd         = 171          # x axis 
xHomeLoc         = 172          # x axis 
xHomeSpeed       = 173          # x axis 
xHomeStart       = 174          # x axis 
xInvDRO          = 175          # x axis invert dro
xInvDir          = 176          # x axis invert stepper direction
xInvEnc          = 177          # x axis 
xInvMpg          = 178          # x axis invert mpg direction
xJogMax          = 179          # x axis 
xJogMin          = 180          # x axis 
xMpgInc          = 181          # x axis jog increment
xMpgMax          = 182          # x axis jog maximum
xJogSpeed        = 183          # x axis 
xMaxSpeed        = 184          # x axis 
xMicroSteps      = 185          # x axis 
xMinSpeed        = 186          # x axis 
xMotorRatio      = 187          # x axis 
xMotorSteps      = 188          # x axis 
xParkLoc         = 189          # x axis 
xPitch           = 190          # x axis 
xProbeDist       = 191          # x axis 
xDROPos          = 192          # x axis 

# x axis position config

xSvPosition      = 193          # x axis 
xSvHomeOffset    = 194          # x axis 
xSvDROPosition   = 195          # x axis 
xSvDROOffset     = 196          # x axis 

# z axis config

zAccel           = 197          # z axis 
zBackInc         = 198          # z axis distance to go past for taking out backlash
zBacklash        = 199          # z axis 
zDROInch         = 200          # z axis 
zInvDRO          = 201          # z axis 
zInvDir          = 202          # z axis 
zInvEnc          = 203          # z axis 
zInvMpg          = 204          # z axis 
zJogMax          = 205          # z axis 
zJogMin          = 206          # z axis 
zMpgInc          = 207          # z axis jog increment
zMpgMax          = 208          # z axis jog maximum
zJogSpeed        = 209          # z axis 
zMaxSpeed        = 210          # z axis 
zMicroSteps      = 211          # z axis 
zMinSpeed        = 212          # z axis 
zMotorRatio      = 213          # z axis 
zMotorSteps      = 214          # z axis 
zParkLoc         = 215          # z axis 
zPitch           = 216          # z axis 
zProbeDist       = 217          # z axis 
zProbeSpeed      = 218          # z axis 
zDROPos          = 219          # x axis 

# z axis position config

zSvPosition      = 220          # z axis 
zSvHomeOffset    = 221          # z axis 
zSvDROPosition   = 222          # z axis 
zSvDROOffset     = 223          # z axis 

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
    'cfgXFreq' : 22,
    'cfgXilinx' : 23,
    'commPort' : 24,
    'commRate' : 25,
    'cuPause' : 26,
    'cuRPM' : 27,
    'cuToolWidth' : 28,
    'cuXEnd' : 29,
    'cuXFeed' : 30,
    'cuXRetract' : 31,
    'cuXStart' : 32,
    'cuZCutoff' : 33,
    'cuZRetract' : 34,
    'cuZStart' : 35,
    'droXPos' : 36,
    'droZPos' : 37,
    'extDroPort' : 38,
    'extDroRate' : 39,
    'faAddFeed' : 40,
    'faPasses' : 41,
    'faPause' : 42,
    'faRPM' : 43,
    'faSPInt' : 44,
    'faSpring' : 45,
    'faXEnd' : 46,
    'faXFeed' : 47,
    'faXRetract' : 48,
    'faXStart' : 49,
    'faZEnd' : 50,
    'faZFeed' : 51,
    'faZRetract' : 52,
    'faZStart' : 53,
    'jogInc' : 54,
    'jogXPos' : 55,
    'jogXPosDiam' : 56,
    'jogZPos' : 57,
    'jpSurfaceSpeed' : 58,
    'jpXDroDiam' : 59,
    'jogTimeInitial' : 60,
    'jogTimeInc' : 61,
    'jogTimeMax' : 62,
    'keypadPort' : 63,
    'keypadRate' : 64,
    'mainPanel' : 65,
    'spAccel' : 66,
    'spAccelTime' : 67,
    'spCurRange' : 68,
    'spInvDir' : 69,
    'spJogAccelTime' : 70,
    'spJogMax' : 71,
    'spJogMin' : 72,
    'spJTimeInc' : 73,
    'spJTimeInitial' : 74,
    'spJTimeMax' : 75,
    'spMaxRPM' : 76,
    'spMicroSteps' : 77,
    'spMinRPM' : 78,
    'spMotorSteps' : 79,
    'spMotorTest' : 80,
    'spPWMFreq' : 81,
    'spRangeMin1' : 82,
    'spRangeMin2' : 83,
    'spRangeMin3' : 84,
    'spRangeMin4' : 85,
    'spRangeMin5' : 86,
    'spRangeMin6' : 87,
    'spRangeMax1' : 88,
    'spRangeMax2' : 89,
    'spRangeMax3' : 90,
    'spRangeMax4' : 91,
    'spRangeMax5' : 92,
    'spRangeMax6' : 93,
    'spRanges' : 94,
    'spStepDrive' : 95,
    'spSwitch' : 96,
    'spTestEncoder' : 97,
    'spTestIndex' : 98,
    'spVarSpeed' : 99,
    'syncPort' : 100,
    'syncRate' : 101,
    'thAddFeed' : 102,
    'thAlternate' : 103,
    'thAngle' : 104,
    'thFirstFeed' : 105,
    'thFirstFeedBtn' : 106,
    'thInternal' : 107,
    'thLastFeed' : 108,
    'thLastFeedBtn' : 109,
    'thLeftHand' : 110,
    'thMM' : 111,
    'thPasses' : 112,
    'thPause' : 113,
    'thRPM' : 114,
    'thRunout' : 115,
    'thSPInt' : 116,
    'thSpring' : 117,
    'thTPI' : 118,
    'thThread' : 119,
    'thXDepth' : 120,
    'thXRetract' : 121,
    'thXStart' : 122,
    'thXTaper' : 123,
    'thZ0' : 124,
    'thZ1' : 125,
    'thZRetract' : 126,
    'tpAddFeed' : 127,
    'tpAngle' : 128,
    'tpAngleBtn' : 129,
    'tpDeltaBtn' : 130,
    'tpInternal' : 131,
    'tpLargeDiam' : 132,
    'tpPasses' : 133,
    'tpPause' : 134,
    'tpRPM' : 135,
    'tpSPInt' : 136,
    'tpSmallDiam' : 137,
    'tpSpring' : 138,
    'tpTaperSel' : 139,
    'tpXDelta' : 140,
    'tpXFeed' : 141,
    'tpXFinish' : 142,
    'tpXInFeed' : 143,
    'tpXRetract' : 144,
    'tpZDelta' : 145,
    'tpZFeed' : 146,
    'tpZLength' : 147,
    'tpZRetract' : 148,
    'tpZStart' : 149,
    'tuAddFeed' : 150,
    'tuInternal' : 151,
    'tuPasses' : 152,
    'tuPause' : 153,
    'tuRPM' : 154,
    'tuSPInt' : 155,
    'tuSpring' : 156,
    'tuXDiam0' : 157,
    'tuXDiam1' : 158,
    'tuXFeed' : 159,
    'tuXRetract' : 160,
    'tuZEnd' : 161,
    'tuZFeed' : 162,
    'tuZRetract' : 163,
    'tuZStart' : 164,
    'xAccel' : 165,
    'xBacklash' : 166,
    'xDROInch' : 167,
    'xHomeBackoffDist' : 168,
    'xHomeDir' : 169,
    'xHomeDist' : 170,
    'xHomeEnd' : 171,
    'xHomeLoc' : 172,
    'xHomeSpeed' : 173,
    'xHomeStart' : 174,
    'xInvDRO' : 175,
    'xInvDir' : 176,
    'xInvEnc' : 177,
    'xInvMpg' : 178,
    'xJogMax' : 179,
    'xJogMin' : 180,
    'xMpgInc' : 181,
    'xMpgMax' : 182,
    'xJogSpeed' : 183,
    'xMaxSpeed' : 184,
    'xMicroSteps' : 185,
    'xMinSpeed' : 186,
    'xMotorRatio' : 187,
    'xMotorSteps' : 188,
    'xParkLoc' : 189,
    'xPitch' : 190,
    'xProbeDist' : 191,
    'xDROPos' : 192,
    'xSvPosition' : 193,
    'xSvHomeOffset' : 194,
    'xSvDROPosition' : 195,
    'xSvDROOffset' : 196,
    'zAccel' : 197,
    'zBackInc' : 198,
    'zBacklash' : 199,
    'zDROInch' : 200,
    'zInvDRO' : 201,
    'zInvDir' : 202,
    'zInvEnc' : 203,
    'zInvMpg' : 204,
    'zJogMax' : 205,
    'zJogMin' : 206,
    'zMpgInc' : 207,
    'zMpgMax' : 208,
    'zJogSpeed' : 209,
    'zMaxSpeed' : 210,
    'zMicroSteps' : 211,
    'zMinSpeed' : 212,
    'zMotorRatio' : 213,
    'zMotorSteps' : 214,
    'zParkLoc' : 215,
    'zPitch' : 216,
    'zProbeDist' : 217,
    'zProbeSpeed' : 218,
    'zDROPos' : 219,
    'zSvPosition' : 220,
    'zSvHomeOffset' : 221,
    'zSvDROPosition' : 222,
    'zSvDROOffset' : 223,
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
    'xDROPos',
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
