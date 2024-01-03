# config table

# arc panel

arcAddFeed        =   0         # arc 
arcBallDist       =   1         # arc 
arcCCW            =   2         # arc 
arcDiam           =   3         # arc 
arcFeed           =   4         # arc 
arcFinish         =   5         # arc 
arcLargeEnd       =   6         # arc 
arcLargeStem      =   7         # arc 
arcPasses         =   8         # arc 
arcPause          =   9         # arc 
arcRetract        =  10         # arc 
arcRadius         =  11         # arc 
arcRPM            =  12         # arc 
arcSmallEnd       =  13         # arc 
arcSmallStem      =  14         # arc 
arcSPInt          =  15         # arc 
arcSpring         =  16         # arc 
arcToolAngle      =  17         # arc 
arcToolRad        =  18         # arc 
arcType           =  19         # arc 
arcXFeed          =  20         # arc 
arcZFeed          =  21         # arc 
arcZStart         =  22         # arc 

# system config

cfgCmdDis         =  23         # config disable sending commands
cfgCommonLimits   =  24         # config all limit switches on one pin
cfgLimitsEnabled  =  25         # config limits enabled
cfgCommonHome     =  26         # config all switches on one pin
cfgDbgSave        =  27         # config save debug info
cfgDRO            =  28         # config dro present
cfgDROStep        =  29         # config step pulse controls dro
cfgDraw           =  30         # config draw paths
cfgEncoder        =  31         # config encoder counts per revolution
cfgEStop          =  32         # config estop enable
cfgEStopInv       =  33         # config estop invert
cfgExtDro         =  34         # config external digital readout
cfgFcy            =  35         # config microprocessor clock frequency
cfgFpga           =  36         # config fpga interface present
cfgFpgaFreq       =  37         # config fpga frequency
cfgFreqMult       =  38         # config fpga frequency multiplier
cfgHomeInPlace    =  39         # config home in place
cfgIntSync        =  40         # config internal sync
cfgInvEncDir      =  41         # config fpga invert encoder direction
cfgLCD            =  42         # config enable lcd
cfgMega           =  43         # config control link to mega
cfgMPG            =  44         # config enable manual pulse generator
cfgPrbInv         =  45         # config invert probe signal
cfgRemDbg         =  46         # config print remote debug info
cfgRunoutSync     =  47         # config runout synchronization
cfgSpEncCap       =  48         # config encoder on capture interrupt
cfgSpEncoder      =  49         # config spindle encoder
cfgSpSync         =  50         # config spindle using timer
cfgSpSyncBoard    =  51         # config spindle sync board
cfgSpUseEncoder   =  52         # config use spindle encoder for threading
cfgSyncSPI        =  53         # config sync comm through spi
cfgTaperCycleDist =  54         # config taper cycle distance
cfgTestMode       =  55         # config test mode
cfgTestRPM        =  56         # config fpga test rpm value
cfgTurnSync       =  57         # config turning synchronization
cfgThreadSync     =  58         # config threading synchronization

# communications config

commPort          =  59         # comm port
commRate          =  60         # comm baud rate

# cutoff config

cuPause           =  61         # cutoff pause before cutting
cuRPM             =  62         # cutoff rpm
cuToolWidth       =  63         # cutoff tool width
cuXEnd            =  64         # cutoff x end
cuXFeed           =  65         # cutoff x feed
cuXRetract        =  66         # cutoff x retract
cuXStart          =  67         # cutoff x start
cuZCutoff         =  68         # cutoff offset to z cutoff
cuZRetract        =  69         # cutoff offset to z retract
cuZStart          =  70         # cutoff z location

# dro position

droXPos           =  71         # dro x position
droZPos           =  72         # dro z position

# external dro

extDroPort        =  73         # external dro port
extDroRate        =  74         # external dro baud Rate

# face config

faAddFeed         =  75         # face 
faPasses          =  76         # face 
faPause           =  77         # face pause before cutting
faRPM             =  78         # face 
faSPInt           =  79         # face 
faSpring          =  80         # face 
faXEnd            =  81         # face 
faXFeed           =  82         # face 
faXRetract        =  83         # face 
faXStart          =  84         # face 
faZEnd            =  85         # face 
faZFeed           =  86         # face 
faZRetract        =  87         # face 
faZStart          =  88         # face 

# jog config

jogInc            =  89         # jog 
jogXPos           =  90         # jog 
jogXPosDiam       =  91         # jog 
jogZPos           =  92         # jog 

# jog panel config

jpSurfaceSpeed    =  93         # jog panel fpm or rpm
jpXDroDiam        =  94         # jog panel x dro diameter

# jog time parameters

jogTimeInitial    =  95         # jog time initial
jogTimeInc        =  96         # jog time increment
jogTimeMax        =  97         # jog time max

# keypad

keypadPort        =  98         # external dro port
keypadRate        =  99         # external dro baud Rate

# main panel

mainPanel         = 100         # name of main panel

# mega config

cfgMegaVFD        = 101         # mega vfd speed mode
cfgMegaEncTest    = 102         # mega encoder test
cfgMegaEncLines   = 103         # mega encoder lines

# spindle config

spAccel           = 104         # spindle acceleration
spAccelTime       = 105         # spindle acceleration time
spCurRange        = 106         # spindle current range
spInvDir          = 107         # spindle invert direction
spJogAccelTime    = 108         # spindle jog acceleration time
spJogMax          = 109         # spindle jog max speed
spJogMin          = 110         # spindle jog min speed
spJTimeInc        = 111         # spindle jog increment
spJTimeInitial    = 112         # spindle jog initial time 
spJTimeMax        = 113         # spindle jog max
spMaxRPM          = 114         # spindle jog max rpm
spMicroSteps      = 115         # spindle micro steps
spMinRPM          = 116         # spindle minimum rpm
spMotorSteps      = 117         # spindle motor steps per revolution
spMotorTest       = 118         # use stepper drive to test motor
spPWMFreq         = 119         # spindle pwm frequency
spMegaSim         = 120         # spindle use mega to simulate index and encoder
spRangeMin1       = 121         # spindle speed range 1 minimum
spRangeMin2       = 122         # spindle speed range 2 minimum
spRangeMin3       = 123         # spindle speed range 3 minimum
spRangeMin4       = 124         # spindle speed range 4 minimum
spRangeMin5       = 125         # spindle speed range 5 minimum
spRangeMin6       = 126         # spindle speed range 6 minimum
spRangeMax1       = 127         # spindle speed range 1 maximum
spRangeMax2       = 128         # spindle speed range 2 maximum
spRangeMax3       = 129         # spindle speed range 3 maximum
spRangeMax4       = 130         # spindle speed range 4 maximum
spRangeMax5       = 131         # spindle speed range 5 maximum
spRangeMax6       = 132         # spindle speed range 6 maximum
spRanges          = 133         # spindle number of speed ranges
spStepDrive       = 134         # spindle stepper drive
spSwitch          = 135         # spindle off on switch
spTestEncoder     = 136         # spindle test generate encoder test pulse
spTestIndex       = 137         # spindle test generate internal index pulse
spVarSpeed        = 138         # spindle variable speed

# sync communications config

syncPort          = 139         # sync comm port
syncRate          = 140         # sync comm baud rate

# threading config

thAddFeed         = 141         # thread feed to add after done
thAlternate       = 142         # thread alternate thread flanks
thAngle           = 143         # thread half angle of thread
thFirstFeed       = 144         # thread first feed for thread area calc
thFirstFeedBtn    = 145         # thread button to select first feed
thInternal        = 146         # thread internal threads
thLastFeed        = 147         # thread last feed for thread area calculation
thLastFeedBtn     = 148         # thread button to select last feed
thLeftHand        = 149         # thread left hand 
thMM              = 150         # thread button for mm
thPasses          = 151         # thread number of passes
thPause           = 152         # thread pause between passes
thRPM             = 153         # thread speed for threading operation
thRunout          = 154         # thread runout for rh exit or lh entrance
thSPInt           = 155         # thread spring pass interval
thSpring          = 156         # thread number of spring passes at end
thTPI             = 157         # thread select thread in threads per inch
thThread          = 158         # thread field containing tpi or pitch
thXDepth          = 159         # thread x depth of thread
thXRetract        = 160         # thread x retract
thXStart          = 161         # thread x diameter
thXTaper          = 162         # thread x taper
thZ0              = 163         # thread z right end of thread left start
thZ1              = 164         # thread z right start left end
thZRetract        = 165         # thread z retract

# taper config

tpAddFeed         = 166         # tp 
tpAngle           = 167         # tp 
tpAngleBtn        = 168         # tp 
tpDeltaBtn        = 169         # tp 
tpInternal        = 170         # tp 
tpLargeDiam       = 171         # tp 
tpPasses          = 172         # tp 
tpPause           = 173         # tp 
tpRPM             = 174         # tp 
tpSPInt           = 175         # tp 
tpSmallDiam       = 176         # tp 
tpSpring          = 177         # tp 
tpTaperSel        = 178         # tp 
tpXDelta          = 179         # tp 
tpXFeed           = 180         # tp 
tpXFinish         = 181         # tp 
tpXInFeed         = 182         # tp 
tpXRetract        = 183         # tp 
tpZDelta          = 184         # tp 
tpZFeed           = 185         # tp 
tpZLength         = 186         # tp 
tpZRetract        = 187         # tp 
tpZStart          = 188         # tp 

# turn config

tuAddFeed         = 189         # turn 
tuInternal        = 190         # turn internal
tuManual          = 191         # turn manual mode
tuPasses          = 192         # turn 
tuPause           = 193         # turn 
tuRPM             = 194         # turn 
tuSPInt           = 195         # turn 
tuSpring          = 196         # turn 
tuXDiam0          = 197         # turn 
tuXDiam1          = 198         # turn 
tuXFeed           = 199         # turn 
tuXRetract        = 200         # turn 
tuZEnd            = 201         # turn 
tuZFeed           = 202         # turn 
tuZRetract        = 203         # turn 
tuZStart          = 204         # turn 

# x axis config

xAccel            = 205         # x axis 
xBackInc          = 206         # z axis distance to go past for taking out backlash
xBacklash         = 207         # x axis 
xDoneDelay        = 208         # x axis done to read dro delay
xDroFinalDist     = 209         # x dro final approach dist
xDROInch          = 210         # x axis 
xDROPos           = 211         # x axis use dro to go to correct position
xHomeDir          = 212         # x axis 
xHomeDist         = 213         # x axis 
xHomeDistBackoff  = 214         # x axis 
xHomeDistRev      = 215         # x axis 
xHomeEna          = 216         # x axis 
xHomeEnd          = 217         # x axis 
xHomeInv          = 218         # x axis 
xHomeLoc          = 219         # x axis 
xHomeSpeed        = 220         # x axis 
xHomeStart        = 221         # x axis 
xInvDRO           = 222         # x axis invert dro
xInvDir           = 223         # x axis invert stepper direction
xInvEnc           = 224         # x axis 
xInvMpg           = 225         # x axis invert mpg direction
xJogMax           = 226         # x axis 
xJogMin           = 227         # x axis 
xLimEna           = 228         # x axis limits enable
xLimNegInv        = 229         # x axis negative limit invert
xLimPosInv        = 230         # x axis positive limit invert
xMpgInc           = 231         # x axis jog increment
xMpgMax           = 232         # x axis jog maximum
xJogSpeed         = 233         # x axis 
xMaxSpeed         = 234         # x axis 
xMicroSteps       = 235         # x axis 
xMinSpeed         = 236         # x axis 
xMotorRatio       = 237         # x axis 
xMotorSteps       = 238         # x axis 
xRetractLoc       = 239         # x axis 
xPitch            = 240         # x axis 
xProbeDist        = 241         # x axis 
xTstLimitMin      = 242         # x axis test limit minimum
xTstLimitMax      = 243         # x axis test limit maximum
xTstHomeMin       = 244         # x axis test home minimum
xTstHomeMax       = 245         # x axis test home maximum
xTstProbe         = 246         # x axis test probe

# x axis position config

xSvPosition       = 247         # x axis 
xSvHomeOffset     = 248         # x axis 
xSvDROPosition    = 249         # x axis 
xSvDROOffset      = 250         # x axis 

# z axis config

zAccel            = 251         # z axis 
zBackInc          = 252         # z axis distance to go past for taking out backlash
zBacklash         = 253         # z axis 
zDoneDelay        = 254         # z axis done to read dro delay
zDroFinalDist     = 255         # z dro final approach dist
zDROPos           = 256         # z axis use dro to go to correct position
zDROInch          = 257         # z axis 
zHomeDir          = 258         # z axis 
zHomeDist         = 259         # z axis 
zHomeDistRev      = 260         # z axis 
zHomeDistBackoff  = 261         # z axis 
zHomeEna          = 262         # z axis 
zHomeEnd          = 263         # z axis 
zHomeInv          = 264         # z axis 
zHomeLoc          = 265         # z axis 
zHomeSpeed        = 266         # z axis 
zHomeStart        = 267         # z axis 
zInvDRO           = 268         # z axis 
zInvDir           = 269         # z axis 
zInvEnc           = 270         # z axis 
zInvMpg           = 271         # z axis 
zJogMax           = 272         # z axis 
zJogMin           = 273         # z axis 
zMpgInc           = 274         # z axis jog increment
zMpgMax           = 275         # z axis jog maximum
zJogSpeed         = 276         # z axis 
zLimEna           = 277         # z axis limits enable
zLimNegInv        = 278         # z axis negative limit invert
zLimPosInv        = 279         # z axis positive limit invert
zMaxSpeed         = 280         # z axis 
zMicroSteps       = 281         # z axis 
zMinSpeed         = 282         # z axis 
zMotorRatio       = 283         # z axis 
zMotorSteps       = 284         # z axis 
zRetractLoc       = 285         # z axis 
zPitch            = 286         # z axis 
zProbeDist        = 287         # z axis 
zProbeSpeed       = 288         # z axis 
zTstLimitMin      = 289         # z axis test limit minimum
zTstLimitMax      = 290         # z axis test limit maximum
zTstHomeMin       = 291         # z axis test home minimum
zTstHomeMax       = 292         # z axis test home maximum
zTstProbe         = 293         # z axis test probe

# z axis position config

zSvPosition       = 294         # z axis 
zSvHomeOffset     = 295         # z axis 
zSvDROPosition    = 296         # z axis 
zSvDROOffset      = 297         # z axis 
cfgJogDebug       = 298         # debug jogging

MAX_CFG_INDEX = 299

config = { \
    'arcAddFeed'        : 0,
    'arcBallDist'       : 1,
    'arcCCW'            : 2,
    'arcDiam'           : 3,
    'arcFeed'           : 4,
    'arcFinish'         : 5,
    'arcLargeEnd'       : 6,
    'arcLargeStem'      : 7,
    'arcPasses'         : 8,
    'arcPause'          : 9,
    'arcRPM'            : 12,
    'arcRadius'         : 11,
    'arcRetract'        : 10,
    'arcSPInt'          : 15,
    'arcSmallEnd'       : 13,
    'arcSmallStem'      : 14,
    'arcSpring'         : 16,
    'arcToolAngle'      : 17,
    'arcToolRad'        : 18,
    'arcType'           : 19,
    'arcXFeed'          : 20,
    'arcZFeed'          : 21,
    'arcZStart'         : 22,
    'cfgCmdDis'         : 23,
    'cfgCommonHome'     : 26,
    'cfgCommonLimits'   : 24,
    'cfgDRO'            : 28,
    'cfgDROStep'        : 29,
    'cfgDbgSave'        : 27,
    'cfgDraw'           : 30,
    'cfgEStop'          : 32,
    'cfgEStopInv'       : 33,
    'cfgEncoder'        : 31,
    'cfgExtDro'         : 34,
    'cfgFcy'            : 35,
    'cfgFpga'           : 36,
    'cfgFpgaFreq'       : 37,
    'cfgFreqMult'       : 38,
    'cfgHomeInPlace'    : 39,
    'cfgIntSync'        : 40,
    'cfgInvEncDir'      : 41,
    'cfgJogDebug'       : 298,
    'cfgLCD'            : 42,
    'cfgLimitsEnabled'  : 25,
    'cfgMPG'            : 44,
    'cfgMega'           : 43,
    'cfgMegaEncLines'   : 103,
    'cfgMegaEncTest'    : 102,
    'cfgMegaVFD'        : 101,
    'cfgPrbInv'         : 45,
    'cfgRemDbg'         : 46,
    'cfgRunoutSync'     : 47,
    'cfgSpEncCap'       : 48,
    'cfgSpEncoder'      : 49,
    'cfgSpSync'         : 50,
    'cfgSpSyncBoard'    : 51,
    'cfgSpUseEncoder'   : 52,
    'cfgSyncSPI'        : 53,
    'cfgTaperCycleDist' : 54,
    'cfgTestMode'       : 55,
    'cfgTestRPM'        : 56,
    'cfgThreadSync'     : 58,
    'cfgTurnSync'       : 57,
    'commPort'          : 59,
    'commRate'          : 60,
    'cuPause'           : 61,
    'cuRPM'             : 62,
    'cuToolWidth'       : 63,
    'cuXEnd'            : 64,
    'cuXFeed'           : 65,
    'cuXRetract'        : 66,
    'cuXStart'          : 67,
    'cuZCutoff'         : 68,
    'cuZRetract'        : 69,
    'cuZStart'          : 70,
    'droXPos'           : 71,
    'droZPos'           : 72,
    'extDroPort'        : 73,
    'extDroRate'        : 74,
    'faAddFeed'         : 75,
    'faPasses'          : 76,
    'faPause'           : 77,
    'faRPM'             : 78,
    'faSPInt'           : 79,
    'faSpring'          : 80,
    'faXEnd'            : 81,
    'faXFeed'           : 82,
    'faXRetract'        : 83,
    'faXStart'          : 84,
    'faZEnd'            : 85,
    'faZFeed'           : 86,
    'faZRetract'        : 87,
    'faZStart'          : 88,
    'jogInc'            : 89,
    'jogTimeInc'        : 96,
    'jogTimeInitial'    : 95,
    'jogTimeMax'        : 97,
    'jogXPos'           : 90,
    'jogXPosDiam'       : 91,
    'jogZPos'           : 92,
    'jpSurfaceSpeed'    : 93,
    'jpXDroDiam'        : 94,
    'keypadPort'        : 98,
    'keypadRate'        : 99,
    'mainPanel'         : 100,
    'spAccel'           : 104,
    'spAccelTime'       : 105,
    'spCurRange'        : 106,
    'spInvDir'          : 107,
    'spJTimeInc'        : 111,
    'spJTimeInitial'    : 112,
    'spJTimeMax'        : 113,
    'spJogAccelTime'    : 108,
    'spJogMax'          : 109,
    'spJogMin'          : 110,
    'spMaxRPM'          : 114,
    'spMegaSim'         : 120,
    'spMicroSteps'      : 115,
    'spMinRPM'          : 116,
    'spMotorSteps'      : 117,
    'spMotorTest'       : 118,
    'spPWMFreq'         : 119,
    'spRangeMax1'       : 127,
    'spRangeMax2'       : 128,
    'spRangeMax3'       : 129,
    'spRangeMax4'       : 130,
    'spRangeMax5'       : 131,
    'spRangeMax6'       : 132,
    'spRangeMin1'       : 121,
    'spRangeMin2'       : 122,
    'spRangeMin3'       : 123,
    'spRangeMin4'       : 124,
    'spRangeMin5'       : 125,
    'spRangeMin6'       : 126,
    'spRanges'          : 133,
    'spStepDrive'       : 134,
    'spSwitch'          : 135,
    'spTestEncoder'     : 136,
    'spTestIndex'       : 137,
    'spVarSpeed'        : 138,
    'syncPort'          : 139,
    'syncRate'          : 140,
    'thAddFeed'         : 141,
    'thAlternate'       : 142,
    'thAngle'           : 143,
    'thFirstFeed'       : 144,
    'thFirstFeedBtn'    : 145,
    'thInternal'        : 146,
    'thLastFeed'        : 147,
    'thLastFeedBtn'     : 148,
    'thLeftHand'        : 149,
    'thMM'              : 150,
    'thPasses'          : 151,
    'thPause'           : 152,
    'thRPM'             : 153,
    'thRunout'          : 154,
    'thSPInt'           : 155,
    'thSpring'          : 156,
    'thTPI'             : 157,
    'thThread'          : 158,
    'thXDepth'          : 159,
    'thXRetract'        : 160,
    'thXStart'          : 161,
    'thXTaper'          : 162,
    'thZ0'              : 163,
    'thZ1'              : 164,
    'thZRetract'        : 165,
    'tpAddFeed'         : 166,
    'tpAngle'           : 167,
    'tpAngleBtn'        : 168,
    'tpDeltaBtn'        : 169,
    'tpInternal'        : 170,
    'tpLargeDiam'       : 171,
    'tpPasses'          : 172,
    'tpPause'           : 173,
    'tpRPM'             : 174,
    'tpSPInt'           : 175,
    'tpSmallDiam'       : 176,
    'tpSpring'          : 177,
    'tpTaperSel'        : 178,
    'tpXDelta'          : 179,
    'tpXFeed'           : 180,
    'tpXFinish'         : 181,
    'tpXInFeed'         : 182,
    'tpXRetract'        : 183,
    'tpZDelta'          : 184,
    'tpZFeed'           : 185,
    'tpZLength'         : 186,
    'tpZRetract'        : 187,
    'tpZStart'          : 188,
    'tuAddFeed'         : 189,
    'tuInternal'        : 190,
    'tuManual'          : 191,
    'tuPasses'          : 192,
    'tuPause'           : 193,
    'tuRPM'             : 194,
    'tuSPInt'           : 195,
    'tuSpring'          : 196,
    'tuXDiam0'          : 197,
    'tuXDiam1'          : 198,
    'tuXFeed'           : 199,
    'tuXRetract'        : 200,
    'tuZEnd'            : 201,
    'tuZFeed'           : 202,
    'tuZRetract'        : 203,
    'tuZStart'          : 204,
    'xAccel'            : 205,
    'xBackInc'          : 206,
    'xBacklash'         : 207,
    'xDROInch'          : 210,
    'xDROPos'           : 211,
    'xDoneDelay'        : 208,
    'xDroFinalDist'     : 209,
    'xHomeDir'          : 212,
    'xHomeDist'         : 213,
    'xHomeDistBackoff'  : 214,
    'xHomeDistRev'      : 215,
    'xHomeEna'          : 216,
    'xHomeEnd'          : 217,
    'xHomeInv'          : 218,
    'xHomeLoc'          : 219,
    'xHomeSpeed'        : 220,
    'xHomeStart'        : 221,
    'xInvDRO'           : 222,
    'xInvDir'           : 223,
    'xInvEnc'           : 224,
    'xInvMpg'           : 225,
    'xJogMax'           : 226,
    'xJogMin'           : 227,
    'xJogSpeed'         : 233,
    'xLimEna'           : 228,
    'xLimNegInv'        : 229,
    'xLimPosInv'        : 230,
    'xMaxSpeed'         : 234,
    'xMicroSteps'       : 235,
    'xMinSpeed'         : 236,
    'xMotorRatio'       : 237,
    'xMotorSteps'       : 238,
    'xMpgInc'           : 231,
    'xMpgMax'           : 232,
    'xPitch'            : 240,
    'xProbeDist'        : 241,
    'xRetractLoc'       : 239,
    'xSvDROOffset'      : 250,
    'xSvDROPosition'    : 249,
    'xSvHomeOffset'     : 248,
    'xSvPosition'       : 247,
    'xTstHomeMax'       : 245,
    'xTstHomeMin'       : 244,
    'xTstLimitMax'      : 243,
    'xTstLimitMin'      : 242,
    'xTstProbe'         : 246,
    'zAccel'            : 251,
    'zBackInc'          : 252,
    'zBacklash'         : 253,
    'zDROInch'          : 257,
    'zDROPos'           : 256,
    'zDoneDelay'        : 254,
    'zDroFinalDist'     : 255,
    'zHomeDir'          : 258,
    'zHomeDist'         : 259,
    'zHomeDistBackoff'  : 261,
    'zHomeDistRev'      : 260,
    'zHomeEna'          : 262,
    'zHomeEnd'          : 263,
    'zHomeInv'          : 264,
    'zHomeLoc'          : 265,
    'zHomeSpeed'        : 266,
    'zHomeStart'        : 267,
    'zInvDRO'           : 268,
    'zInvDir'           : 269,
    'zInvEnc'           : 270,
    'zInvMpg'           : 271,
    'zJogMax'           : 272,
    'zJogMin'           : 273,
    'zJogSpeed'         : 276,
    'zLimEna'           : 277,
    'zLimNegInv'        : 278,
    'zLimPosInv'        : 279,
    'zMaxSpeed'         : 280,
    'zMicroSteps'       : 281,
    'zMinSpeed'         : 282,
    'zMotorRatio'       : 283,
    'zMotorSteps'       : 284,
    'zMpgInc'           : 274,
    'zMpgMax'           : 275,
    'zPitch'            : 286,
    'zProbeDist'        : 287,
    'zProbeSpeed'       : 288,
    'zRetractLoc'       : 285,
    'zSvDROOffset'      : 297,
    'zSvDROPosition'    : 296,
    'zSvHomeOffset'     : 295,
    'zSvPosition'       : 294,
    'zTstHomeMax'       : 292,
    'zTstHomeMin'       : 291,
    'zTstLimitMax'      : 290,
    'zTstLimitMin'      : 289,
    'zTstProbe'         : 293,
    }

configTable = ( \
    'arcAddFeed',
    'arcBallDist',
    'arcCCW',
    'arcDiam',
    'arcFeed',
    'arcFinish',
    'arcLargeEnd',
    'arcLargeStem',
    'arcPasses',
    'arcPause',
    'arcRetract',
    'arcRadius',
    'arcRPM',
    'arcSmallEnd',
    'arcSmallStem',
    'arcSPInt',
    'arcSpring',
    'arcToolAngle',
    'arcToolRad',
    'arcType',
    'arcXFeed',
    'arcZFeed',
    'arcZStart',
    'cfgCmdDis',
    'cfgCommonLimits',
    'cfgLimitsEnabled',
    'cfgCommonHome',
    'cfgDbgSave',
    'cfgDRO',
    'cfgDROStep',
    'cfgDraw',
    'cfgEncoder',
    'cfgEStop',
    'cfgEStopInv',
    'cfgExtDro',
    'cfgFcy',
    'cfgFpga',
    'cfgFpgaFreq',
    'cfgFreqMult',
    'cfgHomeInPlace',
    'cfgIntSync',
    'cfgInvEncDir',
    'cfgLCD',
    'cfgMega',
    'cfgMPG',
    'cfgPrbInv',
    'cfgRemDbg',
    'cfgRunoutSync',
    'cfgSpEncCap',
    'cfgSpEncoder',
    'cfgSpSync',
    'cfgSpSyncBoard',
    'cfgSpUseEncoder',
    'cfgSyncSPI',
    'cfgTaperCycleDist',
    'cfgTestMode',
    'cfgTestRPM',
    'cfgTurnSync',
    'cfgThreadSync',
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
    'cfgMegaVFD',
    'cfgMegaEncTest',
    'cfgMegaEncLines',
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
    'spMegaSim',
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
    'tuManual',
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
    'xBackInc',
    'xBacklash',
    'xDoneDelay',
    'xDroFinalDist',
    'xDROInch',
    'xDROPos',
    'xHomeDir',
    'xHomeDist',
    'xHomeDistBackoff',
    'xHomeDistRev',
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
    'xRetractLoc',
    'xPitch',
    'xProbeDist',
    'xTstLimitMin',
    'xTstLimitMax',
    'xTstHomeMin',
    'xTstHomeMax',
    'xTstProbe',
    'xSvPosition',
    'xSvHomeOffset',
    'xSvDROPosition',
    'xSvDROOffset',
    'zAccel',
    'zBackInc',
    'zBacklash',
    'zDoneDelay',
    'zDroFinalDist',
    'zDROPos',
    'zDROInch',
    'zHomeDir',
    'zHomeDist',
    'zHomeDistRev',
    'zHomeDistBackoff',
    'zHomeEna',
    'zHomeEnd',
    'zHomeInv',
    'zHomeLoc',
    'zHomeSpeed',
    'zHomeStart',
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
    'zRetractLoc',
    'zPitch',
    'zProbeDist',
    'zProbeSpeed',
    'zTstLimitMin',
    'zTstLimitMax',
    'zTstHomeMin',
    'zTstHomeMax',
    'zTstProbe',
    'zSvPosition',
    'zSvHomeOffset',
    'zSvDROPosition',
    'zSvDROOffset',
    'cfgJogDebug',
    )

CFG_STR_LEN = 17

