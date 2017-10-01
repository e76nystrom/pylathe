# config table

# system config

cfgCmdDis        =   0          # config disable sending commands
cfgDbgSave       =   1          # config save debug info
cfgDRO           =   2          # config dro present
cfgDraw          =   3          # config draw paths
cfgEncoder       =   4          # config xilinx encoder counts per revolution
cfgFcy           =   5          # config microprocesssor clock frequency
cfgFreqMult      =   6          # config xilinx frequency multiplier
cfgInvEncDir     =   7          # config xilinx invert encoder direction
cfgLCD           =   8          # config enable lcd
cfgMPG           =   9          # config enable manual pulse generator
cfgPrbInv        =  10          # config invert probe signal
cfgRemDbg        =  11          # config print remote debug info
cfgTestMode      =  12          # conifg test mode
cfgTestRPM       =  13          # config xilinx test rpm value
cfgXFreq         =  14          # config xilinx frequency
cfgXilinx        =  15          # config xilinx interface present

# communications config

commPort         =  16          # comm port
commRate         =  17          # comm baud rate

# cutoff config

cuPause          =  18          # cutoff pause before cutting
cuRPM            =  19          # cutoff rpm
cuToolWidth      =  20          # cutoff tool width
cuXEnd           =  21          # cutoff x end
cuXFeed          =  22          # cutoff x feed
cuXRetract       =  23          # cutoff x retract
cuXStart         =  24          # cutoff x start
cuZCutoff        =  25          # cutoff offset to z cutoff
cuZRetract       =  26          # cutoff offset to z retract
cuZStart         =  27          # cutoff z location

# dro position

droXPos          =  28          # dro x position 
droZPos          =  29          # dro z position 

# face config

faAddFeed        =  30          # face 
faPasses         =  31          # face 
faPause          =  32          # face pause before cutting
faRPM            =  33          # face 
faSPInt          =  34          # face 
faSpring         =  35          # face 
faXEnd           =  36          # face 
faXFeed          =  37          # face 
faXRetract       =  38          # face 
faXStart         =  39          # face 
faZEnd           =  40          # face 
faZFeed          =  41          # face 
faZRetract       =  42          # face 
faZStart         =  43          # face 

# jog config

jogInc           =  44          # jog 
jogXPos          =  45          # jog 
jogXPosDiam      =  46          # jog 
jogZPos          =  47          # jog 

# main panel

mainPanel        =  48          # name of main panel

# spindle config

spAccel          =  49          # spindle acceleration
spAccelTime      =  50          # spindle accelerationtime
spInvDir         =  51          # spindle invert direction
spJogAccelTime   =  52          # spindle jog acceleration time
spJogMax         =  53          # spindle jog max speed
spJogMin         =  54          # spindle jog min speed
spMaxRPM         =  55          # spindle jog max rpm
spMicroSteps     =  56          # spindle micro steps
spMinRPM         =  57          # spindle minimum rpm
spMotorSteps     =  58          # spindle motor stpes per revolution
spStepDrive      =  59          # spindle stepper drive
spTestIndex      =  60          # spindle test generate internal index pulse

# threading config

thAddFeed        =  61          # thread 
thAlternate      =  62          # thread 
thAngle          =  63          # thread 
thExitRev        =  64          # thread 
thFirstFeed      =  65          # thread 
thFirstFeedBtn   =  66          # thread 
thHFactor        =  67          # thread 
thInternal       =  68          # thread 
thLastFeed       =  69          # thread 
thLastFeedBtn    =  70          # thread 
thMM             =  71          # thread 
thPasses         =  72          # thread 
thPause          =  73          # thread 
thPitch          =  74          # thread 
thRPM            =  75          # thread 
thSPInt          =  76          # thread 
thSpring         =  77          # thread 
thTPI            =  78          # thread 
thXDepth         =  79          # thread 
thXRetract       =  80          # thread 
thXStart         =  81          # thread 
thXTaper         =  82          # thread 
thZEnd           =  83          # thread 
thZRetract       =  84          # thread 
thZStart         =  85          # thread 

# taper config

tpAddFeed        =  86          # tp 
tpAngle          =  87          # tp 
tpAngleBtn       =  88          # tp 
tpDeltaBtn       =  89          # tp 
tpInternal       =  90          # tp 
tpLargeDiam      =  91          # tp 
tpLargeDiamText  =  92          # tp 
tpPasses         =  93          # tp 
tpPause          =  94          # tp 
tpRPM            =  95          # tp 
tpSPInt          =  96          # tp 
tpSmallDiam      =  97          # tp 
tpSmallDiamText  =  98          # tp 
tpSpring         =  99          # tp 
tpTaperSel       = 100          # tp 
tpXDelta         = 101          # tp 
tpXFeed          = 102          # tp 
tpXFinish        = 103          # tp 
tpXInFeed        = 104          # tp 
tpXRetract       = 105          # tp 
tpZDelta         = 106          # tp 
tpZFeed          = 107          # tp 
tpZLength        = 108          # tp 
tpZRetract       = 109          # tp 
tpZStart         = 110          # tp 

# turn config

tuAddFeed        = 111          # turn 
tuPasses         = 112          # turn 
tuPause          = 113          # turn 
tuRPM            = 114          # turn 
tuSPInt          = 115          # turn 
tuSpring         = 116          # turn 
tuXEnd           = 117          # turn 
tuXFeed          = 118          # turn 
tuXRetract       = 119          # turn 
tuXStart         = 120          # turn 
tuZEnd           = 121          # turn 
tuZFeed          = 122          # turn 
tuZRetract       = 123          # turn 
tuZStart         = 124          # turn 

# x axis config

xAccel           = 125          # turn 
xBacklash        = 126          # turn 
xDROInch         = 127          # turn 
xHomeBackoffDist = 128          # x axis 
xHomeDir         = 129          # x axis 
xHomeDist        = 130          # x axis 
xHomeEnd         = 131          # x axis 
xHomeLoc         = 132          # x axis 
xHomeSpeed       = 133          # x axis 
xHomeStart       = 134          # x axis 
xInvDRO          = 135          # x axis 
xInvDir          = 136          # x axis 
xInvEnc          = 137          # x axis 
xInvMpg          = 138          # x axis 
xJogMax          = 139          # x axis 
xJogMin          = 140          # x axis 
xJogSpeed        = 141          # x axis 
xMaxSpeed        = 142          # x axis 
xMicroSteps      = 143          # x axis 
xMinSpeed        = 144          # x axis 
xMotorRatio      = 145          # x axis 
xMotorSteps      = 146          # x axis 
xParkLoc         = 147          # x axis 
xPitch           = 148          # x axis 
xProbeDist       = 149          # x axis 

# x axis position config

xSvPosition      = 150          # z axis 
xSvHomeOffset    = 151          # z axis 
xSvDROPosition   = 152          # x axis 
xSvDROOffset     = 153          # x axis 

# z axis config

zAccel           = 154          # z axis 
zBacklash        = 155          # z axis 
zDROInch         = 156          # z axis 
zInvDRO          = 157          # z axis 
zInvDir          = 158          # z axis 
zInvEnc          = 159          # z axis 
zInvMpg          = 160          # z axis 
zJogMax          = 161          # z axis 
zJogMin          = 162          # z axis 
zJogSpeed        = 163          # z axis 
zMaxSpeed        = 164          # z axis 
zMicroSteps      = 165          # z axis 
zMinSpeed        = 166          # z axis 
zMotorRatio      = 167          # z axis 
zMotorSteps      = 168          # z axis 
zParkLoc         = 169          # z axis 
zPitch           = 170          # z axis 
zProbeDist       = 171          # z axis 
zProbeSpeed      = 172          # z axis 

# z axis position config

zSvPosition      = 173          # z axis 
zSvHomeOffset    = 174          # z axis 
zSvDROPosition   = 175          # z axis 
zSvDROOffset     = 176          # z axis 
