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
spIndex           = 108         # spindle index pulse
spJogAccelTime    = 109         # spindle jog acceleration time
spJogMax          = 110         # spindle jog max speed
spJogMin          = 111         # spindle jog min speed
spJTimeInc        = 112         # spindle jog increment
spJTimeInitial    = 113         # spindle jog initial time 
spJTimeMax        = 114         # spindle jog max
spMaxRPM          = 115         # spindle jog max rpm
spMicroSteps      = 116         # spindle micro steps
spMinRPM          = 117         # spindle minimum rpm
spMotorSteps      = 118         # spindle motor steps per revolution
spMotorTest       = 119         # use stepper drive to test motor
spPWMFreq         = 120         # spindle pwm frequency
spMegaSim         = 121         # spindle use mega to simulate index and encoder
spRangeMin1       = 122         # spindle speed range 1 minimum
spRangeMin2       = 123         # spindle speed range 2 minimum
spRangeMin3       = 124         # spindle speed range 3 minimum
spRangeMin4       = 125         # spindle speed range 4 minimum
spRangeMin5       = 126         # spindle speed range 5 minimum
spRangeMin6       = 127         # spindle speed range 6 minimum
spRangeMax1       = 128         # spindle speed range 1 maximum
spRangeMax2       = 129         # spindle speed range 2 maximum
spRangeMax3       = 130         # spindle speed range 3 maximum
spRangeMax4       = 131         # spindle speed range 4 maximum
spRangeMax5       = 132         # spindle speed range 5 maximum
spRangeMax6       = 133         # spindle speed range 6 maximum
spRanges          = 134         # spindle number of speed ranges
spStepDrive       = 135         # spindle stepper drive
spStepMult        = 136         # spindle step multiplier
spSwitch          = 137         # spindle off on switch
spTestEncoder     = 138         # spindle test generate encoder test pulse
spTestIndex       = 139         # spindle test generate internal index pulse
spVarSpeed        = 140         # spindle variable speed

# sync communications config

syncPort          = 141         # sync comm port
syncRate          = 142         # sync comm baud rate

# threading config

thAddFeed         = 143         # thread feed to add after done
thAlternate       = 144         # thread alternate thread flanks
thAngle           = 145         # thread half angle of thread
thFirstFeed       = 146         # thread first feed for thread area calc
thFirstFeedBtn    = 147         # thread button to select first feed
thInternal        = 148         # thread internal threads
thLastFeed        = 149         # thread last feed for thread area calculation
thLastFeedBtn     = 150         # thread button to select last feed
thLeftHand        = 151         # thread left hand 
thMM              = 152         # thread button for mm
thPasses          = 153         # thread number of passes
thPause           = 154         # thread pause between passes
thRPM             = 155         # thread speed for threading operation
thRunout          = 156         # thread runout for rh exit or lh entrance
thSPInt           = 157         # thread spring pass interval
thSpring          = 158         # thread number of spring passes at end
thTPI             = 159         # thread select thread in threads per inch
thThread          = 160         # thread field containing tpi or pitch
thXDepth          = 161         # thread x depth of thread
thXRetract        = 162         # thread x retract
thXStart          = 163         # thread x diameter
thXTaper          = 164         # thread x taper
thZ0              = 165         # thread z right end of thread left start
thZ1              = 166         # thread z right start left end
thZRetract        = 167         # thread z retract

# taper config

tpAddFeed         = 168         # tp 
tpAngle           = 169         # tp 
tpAngleBtn        = 170         # tp 
tpDeltaBtn        = 171         # tp 
tpInternal        = 172         # tp 
tpLargeDiam       = 173         # tp 
tpPasses          = 174         # tp 
tpPause           = 175         # tp 
tpRPM             = 176         # tp 
tpSPInt           = 177         # tp 
tpSmallDiam       = 178         # tp 
tpSpring          = 179         # tp 
tpTaperSel        = 180         # tp 
tpXDelta          = 181         # tp 
tpXFeed           = 182         # tp 
tpXFinish         = 183         # tp 
tpXInFeed         = 184         # tp 
tpXRetract        = 185         # tp 
tpZDelta          = 186         # tp 
tpZFeed           = 187         # tp 
tpZLength         = 188         # tp 
tpZRetract        = 189         # tp 
tpZStart          = 190         # tp 

# turn config

tuAddFeed         = 191         # turn 
tuInternal        = 192         # turn internal
tuManual          = 193         # turn manual mode
tuPasses          = 194         # turn 
tuPause           = 195         # turn 
tuRPM             = 196         # turn 
tuSPInt           = 197         # turn 
tuSpring          = 198         # turn 
tuXDiam0          = 199         # turn 
tuXDiam1          = 200         # turn 
tuXFeed           = 201         # turn 
tuXRetract        = 202         # turn 
tuZEnd            = 203         # turn 
tuZFeed           = 204         # turn 
tuZRetract        = 205         # turn 
tuZStart          = 206         # turn 

# x axis config

xAccel            = 207         # x axis 
xBackInc          = 208         # z axis distance to go past for taking out backlash
xBacklash         = 209         # x axis 
xDoneDelay        = 210         # x axis done to read dro delay
xDroFinalDist     = 211         # x dro final approach dist
xDROInch          = 212         # x axis 
xDROPos           = 213         # x axis use dro to go to correct position
xHomeDir          = 214         # x axis 
xHomeDist         = 215         # x axis 
xHomeDistBackoff  = 216         # x axis 
xHomeDistRev      = 217         # x axis 
xHomeEna          = 218         # x axis 
xHomeEnd          = 219         # x axis 
xHomeInv          = 220         # x axis 
xHomeLoc          = 221         # x axis 
xHomeSpeed        = 222         # x axis 
xHomeStart        = 223         # x axis 
xInvDRO           = 224         # x axis invert dro
xInvDir           = 225         # x axis invert stepper direction
xInvEnc           = 226         # x axis 
xInvMpg           = 227         # x axis invert mpg direction
xJogMax           = 228         # x axis 
xJogMin           = 229         # x axis 
xLimEna           = 230         # x axis limits enable
xLimNegInv        = 231         # x axis negative limit invert
xLimPosInv        = 232         # x axis positive limit invert
xMpgInc           = 233         # x axis jog increment
xMpgMax           = 234         # x axis jog maximum
xJogSpeed         = 235         # x axis 
xMaxSpeed         = 236         # x axis 
xMicroSteps       = 237         # x axis 
xMinSpeed         = 238         # x axis 
xMotorRatio       = 239         # x axis 
xMotorSteps       = 240         # x axis 
xRetractLoc       = 241         # x axis 
xPitch            = 242         # x axis 
xProbeDist        = 243         # x axis 
xTstLimitMin      = 244         # x axis test limit minimum
xTstLimitMax      = 245         # x axis test limit maximum
xTstHomeMin       = 246         # x axis test home minimum
xTstHomeMax       = 247         # x axis test home maximum
xTstProbe         = 248         # x axis test probe

# x axis position config

xSvPosition       = 249         # x axis 
xSvHomeOffset     = 250         # x axis 
xSvDROPosition    = 251         # x axis 
xSvDROOffset      = 252         # x axis 

# z axis config

zAccel            = 253         # z axis 
zBackInc          = 254         # z axis distance to go past for taking out backlash
zBacklash         = 255         # z axis 
zDoneDelay        = 256         # z axis done to read dro delay
zDroFinalDist     = 257         # z dro final approach dist
zDROPos           = 258         # z axis use dro to go to correct position
zDROInch          = 259         # z axis 
zHomeDir          = 260         # z axis 
zHomeDist         = 261         # z axis 
zHomeDistRev      = 262         # z axis 
zHomeDistBackoff  = 263         # z axis 
zHomeEna          = 264         # z axis 
zHomeEnd          = 265         # z axis 
zHomeInv          = 266         # z axis 
zHomeLoc          = 267         # z axis 
zHomeSpeed        = 268         # z axis 
zHomeStart        = 269         # z axis 
zInvDRO           = 270         # z axis 
zInvDir           = 271         # z axis 
zInvEnc           = 272         # z axis 
zInvMpg           = 273         # z axis 
zJogMax           = 274         # z axis 
zJogMin           = 275         # z axis 
zMpgInc           = 276         # z axis jog increment
zMpgMax           = 277         # z axis jog maximum
zJogSpeed         = 278         # z axis 
zLimEna           = 279         # z axis limits enable
zLimNegInv        = 280         # z axis negative limit invert
zLimPosInv        = 281         # z axis positive limit invert
zMaxSpeed         = 282         # z axis 
zMicroSteps       = 283         # z axis 
zMinSpeed         = 284         # z axis 
zMotorRatio       = 285         # z axis 
zMotorSteps       = 286         # z axis 
zRetractLoc       = 287         # z axis 
zPitch            = 288         # z axis 
zProbeDist        = 289         # z axis 
zProbeSpeed       = 290         # z axis 
zTstLimitMin      = 291         # z axis test limit minimum
zTstLimitMax      = 292         # z axis test limit maximum
zTstHomeMin       = 293         # z axis test home minimum
zTstHomeMax       = 294         # z axis test home maximum
zTstProbe         = 295         # z axis test probe

# z axis position config

zSvPosition       = 296         # z axis 
zSvHomeOffset     = 297         # z axis 
zSvDROPosition    = 298         # z axis 
zSvDROOffset      = 299         # z axis 
cfgJogDebug       = 300         # debug jogging

MAX_CFG_INDEX = 301

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
    'cfgJogDebug'       : 300,
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
    'spIndex'           : 108,
    'spInvDir'          : 107,
    'spJTimeInc'        : 112,
    'spJTimeInitial'    : 113,
    'spJTimeMax'        : 114,
    'spJogAccelTime'    : 109,
    'spJogMax'          : 110,
    'spJogMin'          : 111,
    'spMaxRPM'          : 115,
    'spMegaSim'         : 121,
    'spMicroSteps'      : 116,
    'spMinRPM'          : 117,
    'spMotorSteps'      : 118,
    'spMotorTest'       : 119,
    'spPWMFreq'         : 120,
    'spRangeMax1'       : 128,
    'spRangeMax2'       : 129,
    'spRangeMax3'       : 130,
    'spRangeMax4'       : 131,
    'spRangeMax5'       : 132,
    'spRangeMax6'       : 133,
    'spRangeMin1'       : 122,
    'spRangeMin2'       : 123,
    'spRangeMin3'       : 124,
    'spRangeMin4'       : 125,
    'spRangeMin5'       : 126,
    'spRangeMin6'       : 127,
    'spRanges'          : 134,
    'spStepDrive'       : 135,
    'spStepMult'        : 136,
    'spSwitch'          : 137,
    'spTestEncoder'     : 138,
    'spTestIndex'       : 139,
    'spVarSpeed'        : 140,
    'syncPort'          : 141,
    'syncRate'          : 142,
    'thAddFeed'         : 143,
    'thAlternate'       : 144,
    'thAngle'           : 145,
    'thFirstFeed'       : 146,
    'thFirstFeedBtn'    : 147,
    'thInternal'        : 148,
    'thLastFeed'        : 149,
    'thLastFeedBtn'     : 150,
    'thLeftHand'        : 151,
    'thMM'              : 152,
    'thPasses'          : 153,
    'thPause'           : 154,
    'thRPM'             : 155,
    'thRunout'          : 156,
    'thSPInt'           : 157,
    'thSpring'          : 158,
    'thTPI'             : 159,
    'thThread'          : 160,
    'thXDepth'          : 161,
    'thXRetract'        : 162,
    'thXStart'          : 163,
    'thXTaper'          : 164,
    'thZ0'              : 165,
    'thZ1'              : 166,
    'thZRetract'        : 167,
    'tpAddFeed'         : 168,
    'tpAngle'           : 169,
    'tpAngleBtn'        : 170,
    'tpDeltaBtn'        : 171,
    'tpInternal'        : 172,
    'tpLargeDiam'       : 173,
    'tpPasses'          : 174,
    'tpPause'           : 175,
    'tpRPM'             : 176,
    'tpSPInt'           : 177,
    'tpSmallDiam'       : 178,
    'tpSpring'          : 179,
    'tpTaperSel'        : 180,
    'tpXDelta'          : 181,
    'tpXFeed'           : 182,
    'tpXFinish'         : 183,
    'tpXInFeed'         : 184,
    'tpXRetract'        : 185,
    'tpZDelta'          : 186,
    'tpZFeed'           : 187,
    'tpZLength'         : 188,
    'tpZRetract'        : 189,
    'tpZStart'          : 190,
    'tuAddFeed'         : 191,
    'tuInternal'        : 192,
    'tuManual'          : 193,
    'tuPasses'          : 194,
    'tuPause'           : 195,
    'tuRPM'             : 196,
    'tuSPInt'           : 197,
    'tuSpring'          : 198,
    'tuXDiam0'          : 199,
    'tuXDiam1'          : 200,
    'tuXFeed'           : 201,
    'tuXRetract'        : 202,
    'tuZEnd'            : 203,
    'tuZFeed'           : 204,
    'tuZRetract'        : 205,
    'tuZStart'          : 206,
    'xAccel'            : 207,
    'xBackInc'          : 208,
    'xBacklash'         : 209,
    'xDROInch'          : 212,
    'xDROPos'           : 213,
    'xDoneDelay'        : 210,
    'xDroFinalDist'     : 211,
    'xHomeDir'          : 214,
    'xHomeDist'         : 215,
    'xHomeDistBackoff'  : 216,
    'xHomeDistRev'      : 217,
    'xHomeEna'          : 218,
    'xHomeEnd'          : 219,
    'xHomeInv'          : 220,
    'xHomeLoc'          : 221,
    'xHomeSpeed'        : 222,
    'xHomeStart'        : 223,
    'xInvDRO'           : 224,
    'xInvDir'           : 225,
    'xInvEnc'           : 226,
    'xInvMpg'           : 227,
    'xJogMax'           : 228,
    'xJogMin'           : 229,
    'xJogSpeed'         : 235,
    'xLimEna'           : 230,
    'xLimNegInv'        : 231,
    'xLimPosInv'        : 232,
    'xMaxSpeed'         : 236,
    'xMicroSteps'       : 237,
    'xMinSpeed'         : 238,
    'xMotorRatio'       : 239,
    'xMotorSteps'       : 240,
    'xMpgInc'           : 233,
    'xMpgMax'           : 234,
    'xPitch'            : 242,
    'xProbeDist'        : 243,
    'xRetractLoc'       : 241,
    'xSvDROOffset'      : 252,
    'xSvDROPosition'    : 251,
    'xSvHomeOffset'     : 250,
    'xSvPosition'       : 249,
    'xTstHomeMax'       : 247,
    'xTstHomeMin'       : 246,
    'xTstLimitMax'      : 245,
    'xTstLimitMin'      : 244,
    'xTstProbe'         : 248,
    'zAccel'            : 253,
    'zBackInc'          : 254,
    'zBacklash'         : 255,
    'zDROInch'          : 259,
    'zDROPos'           : 258,
    'zDoneDelay'        : 256,
    'zDroFinalDist'     : 257,
    'zHomeDir'          : 260,
    'zHomeDist'         : 261,
    'zHomeDistBackoff'  : 263,
    'zHomeDistRev'      : 262,
    'zHomeEna'          : 264,
    'zHomeEnd'          : 265,
    'zHomeInv'          : 266,
    'zHomeLoc'          : 267,
    'zHomeSpeed'        : 268,
    'zHomeStart'        : 269,
    'zInvDRO'           : 270,
    'zInvDir'           : 271,
    'zInvEnc'           : 272,
    'zInvMpg'           : 273,
    'zJogMax'           : 274,
    'zJogMin'           : 275,
    'zJogSpeed'         : 278,
    'zLimEna'           : 279,
    'zLimNegInv'        : 280,
    'zLimPosInv'        : 281,
    'zMaxSpeed'         : 282,
    'zMicroSteps'       : 283,
    'zMinSpeed'         : 284,
    'zMotorRatio'       : 285,
    'zMotorSteps'       : 286,
    'zMpgInc'           : 276,
    'zMpgMax'           : 277,
    'zPitch'            : 288,
    'zProbeDist'        : 289,
    'zProbeSpeed'       : 290,
    'zRetractLoc'       : 287,
    'zSvDROOffset'      : 299,
    'zSvDROPosition'    : 298,
    'zSvHomeOffset'     : 297,
    'zSvPosition'       : 296,
    'zTstHomeMax'       : 294,
    'zTstHomeMin'       : 293,
    'zTstLimitMax'      : 292,
    'zTstLimitMin'      : 291,
    'zTstProbe'         : 295,
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
    'spIndex',
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
    'spStepMult',
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

