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
spRangeMin1      =  81          # spindle speed range 1 minimum
spRangeMin2      =  82          # spindle speed range 2 minimum
spRangeMin3      =  83          # spindle speed range 3 minimum
spRangeMin4      =  84          # spindle speed range 4 minimum
spRangeMin5      =  85          # spindle speed range 5 minimum
spRangeMin6      =  86          # spindle speed range 6 minimum
spRangeMax1      =  87          # spindle speed range 1 maximum
spRangeMax2      =  88          # spindle speed range 2 maximum
spRangeMax3      =  89          # spindle speed range 3 maximum
spRangeMax4      =  90          # spindle speed range 4 maximum
spRangeMax5      =  91          # spindle speed range 5 maximum
spRangeMax6      =  92          # spindle speed range 6 maximum
spRanges         =  93          # spindle number of speed ranges
spStepDrive      =  94          # spindle stepper drive
spSwitch         =  95          # spindle off on switch
spTestEncoder    =  96          # spindle test generate encoder test pulse
spTestIndex      =  97          # spindle test generate internal index pulse
spVarSpeed       =  98          # spindle variable speed

# sync communications config

syncPort         =  99          # sync comm port
syncRate         = 100          # sync comm baud rate

# threading config

thAddFeed        = 101          # thread feed to add after done
thAlternate      = 102          # thread althernate thread flanks
thAngle          = 103          # thread hanlf angle of thread
thFirstFeed      = 104          # thread first feed for thread area calc
thFirstFeedBtn   = 105          # thread button to select first feed
thInternal       = 106          # thread internal threads
thLastFeed       = 107          # thread last feed for thread area calculation
thLastFeedBtn    = 108          # thread button to select last feed
thLeftHand       = 109          # thread left hand 
thMM             = 110          # thread button for mm
thPasses         = 111          # thread number of passes
thPause          = 112          # thread pause between passes
thRPM            = 113          # thread speed for threading operation
thRunout         = 114          # thread runout for rh exit or lh entrance
thSPInt          = 115          # thread spring pass interval
thSpring         = 116          # thread number of spring passes at end
thTPI            = 117          # thread select thread in threads per inch
thThread         = 118          # thread field containing tpi or pitch
thXDepth         = 119          # thread x depth of thread
thXRetract       = 120          # thread x retract
thXStart         = 121          # thread x diameter
thXTaper         = 122          # thread x taper
thZ0             = 123          # thread z right end of thread left start
thZ1             = 124          # thread z right start left end
thZRetract       = 125          # thread z retract

# taper config

tpAddFeed        = 126          # tp 
tpAngle          = 127          # tp 
tpAngleBtn       = 128          # tp 
tpDeltaBtn       = 129          # tp 
tpInternal       = 130          # tp 
tpLargeDiam      = 131          # tp 
tpPasses         = 132          # tp 
tpPause          = 133          # tp 
tpRPM            = 134          # tp 
tpSPInt          = 135          # tp 
tpSmallDiam      = 136          # tp 
tpSpring         = 137          # tp 
tpTaperSel       = 138          # tp 
tpXDelta         = 139          # tp 
tpXFeed          = 140          # tp 
tpXFinish        = 141          # tp 
tpXInFeed        = 142          # tp 
tpXRetract       = 143          # tp 
tpZDelta         = 144          # tp 
tpZFeed          = 145          # tp 
tpZLength        = 146          # tp 
tpZRetract       = 147          # tp 
tpZStart         = 148          # tp 

# turn config

tuAddFeed        = 149          # turn 
tuInternal       = 150          # turn internal
tuPasses         = 151          # turn 
tuPause          = 152          # turn 
tuRPM            = 153          # turn 
tuSPInt          = 154          # turn 
tuSpring         = 155          # turn 
tuXDiam0         = 156          # turn 
tuXDiam1         = 157          # turn 
tuXFeed          = 158          # turn 
tuXRetract       = 159          # turn 
tuZEnd           = 160          # turn 
tuZFeed          = 161          # turn 
tuZRetract       = 162          # turn 
tuZStart         = 163          # turn 

# x axis config

xAccel           = 164          # x axis 
xBacklash        = 165          # x axis 
xDROInch         = 166          # x axis 
xHomeBackoffDist = 167          # x axis 
xHomeDir         = 168          # x axis 
xHomeDist        = 169          # x axis 
xHomeEnd         = 170          # x axis 
xHomeLoc         = 171          # x axis 
xHomeSpeed       = 172          # x axis 
xHomeStart       = 173          # x axis 
xInvDRO          = 174          # x axis invert dro
xInvDir          = 175          # x axis invert stepper direction
xInvEnc          = 176          # x axis 
xInvMpg          = 177          # x axis invert mpg direction
xJogMax          = 178          # x axis 
xJogMin          = 179          # x axis 
xMpgInc          = 180          # x axis jog increment
xMpgMax          = 181          # x axis jog maximum
xJogSpeed        = 182          # x axis 
xMaxSpeed        = 183          # x axis 
xMicroSteps      = 184          # x axis 
xMinSpeed        = 185          # x axis 
xMotorRatio      = 186          # x axis 
xMotorSteps      = 187          # x axis 
xParkLoc         = 188          # x axis 
xPitch           = 189          # x axis 
xProbeDist       = 190          # x axis 

# x axis position config

xSvPosition      = 191          # z axis 
xSvHomeOffset    = 192          # z axis 
xSvDROPosition   = 193          # x axis 
xSvDROOffset     = 194          # x axis 

# z axis config

zAccel           = 195          # z axis 
zBackInc         = 196          # z axis distance to go past for taking out backlash
zBacklash        = 197          # z axis 
zDROInch         = 198          # z axis 
zInvDRO          = 199          # z axis 
zInvDir          = 200          # z axis 
zInvEnc          = 201          # z axis 
zInvMpg          = 202          # z axis 
zJogMax          = 203          # z axis 
zJogMin          = 204          # z axis 
zMpgInc          = 205          # z axis jog increment
zMpgMax          = 206          # z axis jog maximum
zJogSpeed        = 207          # z axis 
zMaxSpeed        = 208          # z axis 
zMicroSteps      = 209          # z axis 
zMinSpeed        = 210          # z axis 
zMotorRatio      = 211          # z axis 
zMotorSteps      = 212          # z axis 
zParkLoc         = 213          # z axis 
zPitch           = 214          # z axis 
zProbeDist       = 215          # z axis 
zProbeSpeed      = 216          # z axis 

# z axis position config

zSvPosition      = 217          # z axis 
zSvHomeOffset    = 218          # z axis 
zSvDROPosition   = 219          # z axis 
zSvDROOffset     = 220          # z axis 

config = { \
    'faPasses' : 41,
    'cfgFreqMult' : 7,
    'spStepDrive' : 94,
    'faZRetract' : 52,
    'tpZFeed' : 145,
    'tuPasses' : 151,
    'thXDepth' : 119,
    'thInternal' : 106,
    'cfgSpUseEncoder' : 18,
    'spMicroSteps' : 77,
    'spRangeMin2' : 82,
    'jogXPos' : 55,
    'zJogSpeed' : 207,
    'xMpgInc' : 180,
    'jogZPos' : 57,
    'thAlternate' : 102,
    'jogInc' : 54,
    'tuAddFeed' : 149,
    'tpRPM' : 134,
    'faZStart' : 53,
    'tuZStart' : 163,
    'tpTaperSel' : 138,
    'thXTaper' : 122,
    'tpZRetract' : 147,
    'thXStart' : 121,
    'thPasses' : 111,
    'xHomeStart' : 173,
    'thSPInt' : 115,
    'zMaxSpeed' : 208,
    'cfgTestRPM' : 21,
    'syncPort' : 99,
    'tpLargeDiam' : 131,
    'thSpring' : 116,
    'xHomeEnd' : 170,
    'thAngle' : 103,
    'xMinSpeed' : 185,
    'xHomeDir' : 168,
    'keypadPort' : 63,
    'faZFeed' : 51,
    'cfgSpSync' : 16,
    'thAddFeed' : 101,
    'thRunout' : 114,
    'xJogSpeed' : 182,
    'zMpgInc' : 205,
    'cuXRetract' : 31,
    'tpZStart' : 148,
    'cuToolWidth' : 28,
    'spJogMax' : 71,
    'tuRPM' : 153,
    'thLastFeedBtn' : 108,
    'cfgDraw' : 3,
    'faXFeed' : 47,
    'xSvDROPosition' : 193,
    'cfgXFreq' : 22,
    'tuSPInt' : 154,
    'cfgLCD' : 10,
    'extDroRate' : 39,
    'cfgSpEncCap' : 14,
    'xJogMax' : 178,
    'zInvDir' : 200,
    'tpXInFeed' : 142,
    'thFirstFeed' : 104,
    'xHomeDist' : 169,
    'jogTimeInitial' : 60,
    'faAddFeed' : 40,
    'xJogMin' : 179,
    'xMotorSteps' : 187,
    'faXEnd' : 46,
    'spJogMin' : 72,
    'xPitch' : 189,
    'cfgExtDro' : 5,
    'xSvHomeOffset' : 192,
    'tpAngle' : 127,
    'faXStart' : 49,
    'cfgEncoder' : 4,
    'faSPInt' : 44,
    'tpXFinish' : 141,
    'zSvPosition' : 217,
    'tpAddFeed' : 126,
    'tpDeltaBtn' : 129,
    'thLeftHand' : 109,
    'tpPasses' : 132,
    'xHomeSpeed' : 172,
    'thXRetract' : 120,
    'xAccel' : 164,
    'xHomeBackoffDist' : 167,
    'cfgDRO' : 2,
    'cfgSpSyncBoard' : 17,
    'commPort' : 24,
    'droZPos' : 37,
    'thFirstFeedBtn' : 105,
    'zMinSpeed' : 210,
    'thRPM' : 113,
    'thZ1' : 124,
    'keypadRate' : 64,
    'zSvHomeOffset' : 218,
    'xInvDRO' : 174,
    'tuSpring' : 155,
    'spRangeMax5' : 91,
    'spRangeMax4' : 90,
    'tuPause' : 152,
    'spRangeMax6' : 92,
    'spRangeMax1' : 87,
    'spRangeMax3' : 89,
    'spRangeMax2' : 88,
    'thThread' : 118,
    'cfgDbgSave' : 1,
    'spRangeMin6' : 86,
    'spRangeMin5' : 85,
    'spRangeMin4' : 84,
    'spRangeMin3' : 83,
    'cuXEnd' : 29,
    'spRangeMin1' : 81,
    'xProbeDist' : 190,
    'xMaxSpeed' : 183,
    'xDROInch' : 166,
    'xInvDir' : 175,
    'tuZFeed' : 161,
    'zInvEnc' : 201,
    'cuZRetract' : 34,
    'zSvDROOffset' : 220,
    'spJTimeInc' : 73,
    'cfgPrbInv' : 12,
    'tpSmallDiam' : 136,
    'tpZLength' : 146,
    'cuXFeed' : 30,
    'zInvMpg' : 202,
    'spRanges' : 93,
    'spMotorSteps' : 79,
    'cuZStart' : 35,
    'tpZDelta' : 144,
    'zAccel' : 195,
    'tpXRetract' : 143,
    'cfgTestMode' : 20,
    'tpXFeed' : 140,
    'thPause' : 112,
    'xInvEnc' : 176,
    'spMinRPM' : 78,
    'tpSpring' : 137,
    'tuZEnd' : 160,
    'tuXFeed' : 158,
    'jogTimeMax' : 62,
    'faSpring' : 45,
    'spJTimeInitial' : 74,
    'cfgXilinx' : 23,
    'thZRetract' : 125,
    'xHomeLoc' : 171,
    'thTPI' : 117,
    'tpXDelta' : 139,
    'tpAngleBtn' : 128,
    'tpPause' : 133,
    'zBacklash' : 197,
    'cfgInvEncDir' : 9,
    'syncRate' : 100,
    'faPause' : 42,
    'thZ0' : 123,
    'zMpgMax' : 206,
    'spTestEncoder' : 96,
    'xMpgMax' : 181,
    'faXRetract' : 48,
    'cuXStart' : 32,
    'cfgHomeInPlace' : 8,
    'jpSurfaceSpeed' : 58,
    'xSvDROOffset' : 194,
    'zParkLoc' : 213,
    'faRPM' : 43,
    'spMaxRPM' : 76,
    'cfgFcy' : 6,
    'zMicroSteps' : 209,
    'spSwitch' : 95,
    'thLastFeed' : 107,
    'zDROInch' : 198,
    'tuXRetract' : 159,
    'tuInternal' : 150,
    'xMotorRatio' : 186,
    'extDroPort' : 38,
    'cuRPM' : 27,
    'xInvMpg' : 177,
    'tuZRetract' : 162,
    'tpSPInt' : 135,
    'spTestIndex' : 97,
    'zJogMin' : 204,
    'zMotorRatio' : 211,
    'zPitch' : 214,
    'spInvDir' : 69,
    'spJogAccelTime' : 70,
    'zBackInc' : 196,
    'spJTimeMax' : 75,
    'zSvDROPosition' : 219,
    'spVarSpeed' : 98,
    'xBacklash' : 165,
    'mainPanel' : 65,
    'cfgSpEncoder' : 15,
    'cfgMPG' : 11,
    'jogTimeInc' : 61,
    'zMotorSteps' : 212,
    'jogXPosDiam' : 56,
    'cuZCutoff' : 33,
    'spCurRange' : 68,
    'spAccelTime' : 67,
    'zInvDRO' : 199,
    'cuPause' : 26,
    'commRate' : 25,
    'cfgCmdDis' : 0,
    'spAccel' : 66,
    'zJogMax' : 203,
    'droXPos' : 36,
    'zProbeDist' : 215,
    'faZEnd' : 50,
    'xParkLoc' : 188,
    'xSvPosition' : 191,
    'jpXDroDiam' : 59,
    'spMotorTest' : 80,
    'xMicroSteps' : 184,
    'cfgTaperCycleDist' : 19,
    'tpInternal' : 130,
    'cfgRemDbg' : 13,
    'thMM' : 110,
    'zProbeSpeed' : 216,
    'tuXDiam0' : 156,
    'tuXDiam1' : 157,
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
