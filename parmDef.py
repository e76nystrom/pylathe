
# parameters

# spindle parameters

SP_STEPS             =   0
SP_MICRO             =   1
SP_MIN_RPM           =   2
SP_MAX_RPM           =   3
SP_ACCEL_TIME        =   4
SP_ACCEL             =   5
SP_JOG_MIN_RPM       =   6
SP_JOG_MAX_RPM       =   7
SP_JOG_RPM           =   8
SP_JOG_ACCEL_TIME    =   9
SP_JOG_TIME_INITIAL  =  10
SP_JOG_TIME_INC      =  11
SP_JOG_TIME_MAX      =  12
SP_JOG_DIR           =  13
SP_DIR_FLAG          =  14
SP_TEST_INDEX        =  15
SP_TEST_ENCODER      =  16

# z axis parameters

Z_PITCH              =  17
Z_RATIO              =  18
Z_MICRO              =  19
Z_MOTOR              =  20
Z_ACCEL_TIME         =  21
Z_ACCEL              =  22
Z_BACKLASH           =  23
X_STEP_FACTOR        =  24
Z_DIR_FLAG           =  25
Z_MPG_FLAG           =  26

# x axis parameters

X_PITCH              =  27
X_RATIO              =  28
X_MICRO              =  29
X_MOTOR              =  30
X_ACCEL_TIME         =  31
X_ACCEL              =  32
X_BACKLASH           =  33
X_DIR_FLAG           =  34
X_MPG_FLAG           =  35
X_DIAMETER           =  36

# z move parameters

Z_MOVE_MIN           =  37
Z_MOVE_MAX           =  38

# z jog parameters

Z_JOG_MIN            =  39
Z_JOG_MAX            =  40
Z_JOG_SPEED          =  41

# x move parameters

X_MOVE_MIN           =  42
X_MOVE_MAX           =  43

# x jog parameters

X_JOG_MIN            =  44
X_JOG_MAX            =  45
X_JOG_SPEED          =  46

# pass information

TOTAL_PASSES         =  47
CURRENT_PASS         =  48
MV_STATUS            =  49

# z axis move values

Z_MOVE_DIST          =  50
Z_MOVE_POS           =  51
Z_JOG_DIR            =  52
Z_SET_LOC            =  53
Z_LOC                =  54
Z_FLAG               =  55
Z_ABS_LOC            =  56
Z_MPG_INC            =  57
Z_MPG_MAX            =  58

# x axis move values

X_MOVE_DIST          =  59
X_MOVE_POS           =  60
X_JOG_DIR            =  61
X_SET_LOC            =  62
X_LOC                =  63
X_FLAG               =  64
X_ABS_LOC            =  65
X_MPG_INC            =  66
X_MPG_MAX            =  67

# common jog parameters

JOG_TIME_INITIAL     =  68
JOG_TIME_INC         =  69
JOG_TIME_MAX         =  70

# taper parameters

TAPER_CYCLE_DIST     =  71

# index pulse variables

INDEX_PRE_SCALER     =  72
LAST_INDEX_PERIOD    =  73
INDEX_PERIOD         =  74
REV_COUNTER          =  75

# z home offset

Z_HOME_OFFSET        =  76

# z dro

Z_DRO_POS            =  77
Z_DRO_OFFSET         =  78
Z_DRO_COUNT_INCH     =  79
Z_DRO_INVERT         =  80
Z_USE_DRO            =  81

# x home parameters

X_HOME_SPEED         =  82
X_HOME_DIST          =  83
X_HOME_BACKOFF_DIST  =  84
X_HOME_DIR           =  85

# x home test parameters

X_HOME_LOC           =  86
X_HOME_START         =  87
X_HOME_END           =  88
X_HOME_OFFSET        =  89
X_DRO_POS            =  90
X_DRO_OFFSET         =  91
X_DRO_COUNT_INCH     =  92
X_DRO_FACTOR         =  93
X_DRO_INVERT         =  94
X_USE_DRO            =  95
X_DONE_DELAY         =  96

# x home or probe status

X_HOME_DONE          =  97
X_HOME_STATUS        =  98

# Z home or probe status

Z_HOME_DONE          =  99
Z_HOME_STATUS        = 100

# probe configuration

PROBE_SPEED          = 101
PROBE_DIST           = 102
PROBE_INV            = 103

# configuration

STEPPER_DRIVE        = 104
MOTOR_TEST           = 105
SPINDLE_ENCODER      = 106
SPINDLE_SYNC_BOARD   = 107
TURN_SYNC            = 108
THREAD_SYNC          = 109
CAP_TMR_ENABLE       = 110
CFG_XILINX           = 111
CFG_MPG              = 112
CFG_DRO              = 113
CFG_LCD              = 114
CFG_FCY              = 115
CFG_SWITCH           = 116
CFG_VAR_SPEED        = 117

# setup

SETUP_DONE           = 118

# encoder counts per revolution

ENC_PER_REV          = 119

# test encoder setup variables

ENC_ENABLE           = 120
ENC_PRE_SCALER       = 121
ENC_TIMER            = 122
ENC_RUN_COUNT        = 123

# test encoder status variables

ENC_RUN              = 124
ENC_COUNTER          = 125
ENC_REV_COUNTER      = 126

# measured spindle speed

RPM                  = 127

# xilinx frequency variables

X_FREQUENCY          = 128
FREQ_MULT            = 129

# xilinx configuration register

X_CFG_REG            = 130

# sync parameters

L_SYNC_CYCLE         = 131
L_SYNC_OUTPUT        = 132
L_SYNC_PRESCALER     = 133

# threading variables

TH_Z_START           = 134
TH_X_START           = 135
TAN_THREAD_ANGLE     = 136
X_FEED               = 137
RUNOUT_DISTANCE      = 138
RUNOUT_DEPTH         = 139

# jog debug

JOG_DEBUG            = 140

# motor and speed control

PWM_FREQ             = 141
MIN_SPEED            = 142
MAX_SPEED            = 143

# current operation

CURRENT_OP           = 144
MAX_PARM             = 145

parmTable = ( \
    ('SP_STEPS', 'int16_t', 'spSteps'),
    ('SP_MICRO', 'int16_t', 'spMicro'),
    ('SP_MIN_RPM', 'float', 'spMinRpm'),
    ('SP_MAX_RPM', 'float', 'spMaxRpm'),
    ('SP_ACCEL_TIME', 'float', 'spAccelTime'),
    ('SP_ACCEL', 'float', 'spAccel'),
    ('SP_JOG_MIN_RPM', 'float', 'spJogMinRpm'),
    ('SP_JOG_MAX_RPM', 'float', 'spJogMaxRpm'),
    ('SP_JOG_RPM', 'float', 'spJogRpm'),
    ('SP_JOG_ACCEL_TIME', 'float', 'spJogAccelTime'),
    ('SP_JOG_TIME_INITIAL', 'float', 'spJogTimeInitial'),
    ('SP_JOG_TIME_INC', 'float', 'spJogTimeInc'),
    ('SP_JOG_TIME_MAX', 'float', 'spJogTimeMax'),
    ('SP_JOG_DIR', 'char', 'spJogDir'),
    ('SP_DIR_FLAG', 'char', 'spDirFlag'),
    ('SP_TEST_INDEX', 'char', 'spTestIndex'),
    ('SP_TEST_ENCODER', 'char', 'spTestEncoder'),
    ('Z_PITCH', 'float', 'zPitch'),
    ('Z_RATIO', 'float', 'zRatio'),
    ('Z_MICRO', 'int16_t', 'zMicro'),
    ('Z_MOTOR', 'int16_t', 'zMotor'),
    ('Z_ACCEL_TIME', 'float', 'zAccelTime'),
    ('Z_ACCEL', 'float', 'zAccel'),
    ('Z_BACKLASH', 'float', 'zBacklash'),
    ('X_STEP_FACTOR', 'int', 'xStepFactor'),
    ('Z_DIR_FLAG', 'char', 'zDirFlag'),
    ('Z_MPG_FLAG', 'char', 'zMpgFlag'),
    ('X_PITCH', 'float', 'xPitch'),
    ('X_RATIO', 'float', 'xRatio'),
    ('X_MICRO', 'int16_t', 'xMicro'),
    ('X_MOTOR', 'int16_t', 'xMotor'),
    ('X_ACCEL_TIME', 'float', 'xAccelTime'),
    ('X_ACCEL', 'float', 'xAccel'),
    ('X_BACKLASH', 'float', 'xBacklash'),
    ('X_DIR_FLAG', 'char', 'xDirFlag'),
    ('X_MPG_FLAG', 'char', 'xMpgFlag'),
    ('X_DIAMETER', 'int', 'xDiameter'),
    ('Z_MOVE_MIN', 'float', 'zMoveMin'),
    ('Z_MOVE_MAX', 'float', 'zMoveMax'),
    ('Z_JOG_MIN', 'float', 'zJogMin'),
    ('Z_JOG_MAX', 'float', 'zJogMax'),
    ('Z_JOG_SPEED', 'float', 'zJogSpeed'),
    ('X_MOVE_MIN', 'float', 'xMoveMin'),
    ('X_MOVE_MAX', 'float', 'xMoveMax'),
    ('X_JOG_MIN', 'float', 'xJogMin'),
    ('X_JOG_MAX', 'float', 'xJogMax'),
    ('X_JOG_SPEED', 'float', 'xJogSpeed'),
    ('TOTAL_PASSES', 'int16_t', 'totalPasses'),
    ('CURRENT_PASS', 'int16_t', 'currentPass'),
    ('MV_STATUS', 'int16_t', 'mvStatus'),
    ('Z_MOVE_DIST', 'float', 'zMoveDist'),
    ('Z_MOVE_POS', 'float', 'zMovePos'),
    ('Z_JOG_DIR', 'int', 'zJogDir'),
    ('Z_SET_LOC', 'float', 'zSetLoc'),
    ('Z_LOC', 'int', 'zLoc'),
    ('Z_FLAG', 'int', 'zFlag'),
    ('Z_ABS_LOC', 'int', 'zAbsLoc'),
    ('Z_MPG_INC', 'int', 'zMpgInc'),
    ('Z_MPG_MAX', 'int', 'zMpgMax'),
    ('X_MOVE_DIST', 'float', 'xMoveDist'),
    ('X_MOVE_POS', 'float', 'xMovePos'),
    ('X_JOG_DIR', 'int', 'xJogDir'),
    ('X_SET_LOC', 'float', 'xSetLoc'),
    ('X_LOC', 'int', 'xLoc'),
    ('X_FLAG', 'int', 'xFlag'),
    ('X_ABS_LOC', 'int', 'xAbsLoc'),
    ('X_MPG_INC', 'int', 'xMpgInc'),
    ('X_MPG_MAX', 'int', 'xMpgMax'),
    ('JOG_TIME_INITIAL', 'float', 'jogTimeInitial'),
    ('JOG_TIME_INC', 'float', 'jogTimeInc'),
    ('JOG_TIME_MAX', 'float', 'jogTimeMax'),
    ('TAPER_CYCLE_DIST', 'float', 'taperCycleDist'),
    ('INDEX_PRE_SCALER', 'int', 'indexPreScaler'),
    ('LAST_INDEX_PERIOD', 'unsigned int', 'lastIndexPeriod'),
    ('INDEX_PERIOD', 'unsigned int', 'indexPeriod'),
    ('REV_COUNTER', 'unsigned int', 'revCounter'),
    ('Z_HOME_OFFSET', 'int', 'zHomeOffset'),
    ('Z_DRO_POS', 'int', 'zDroPos'),
    ('Z_DRO_OFFSET', 'int', 'zDroOffset'),
    ('Z_DRO_COUNT_INCH', 'int', 'zDroCountInch'),
    ('Z_DRO_INVERT', 'int', 'zDroInvert'),
    ('Z_USE_DRO', 'char', 'zUseDro'),
    ('X_HOME_SPEED', 'float', 'xHomeSpeed'),
    ('X_HOME_DIST', 'float', 'xHomeDist'),
    ('X_HOME_BACKOFF_DIST', 'float', 'xHomeBackoffDist'),
    ('X_HOME_DIR', 'int', 'xHomeDir'),
    ('X_HOME_LOC', 'int', 'xHomeLoc'),
    ('X_HOME_START', 'int', 'xHomeStart'),
    ('X_HOME_END', 'int', 'xHomeEnd'),
    ('X_HOME_OFFSET', 'int', 'xHomeOffset'),
    ('X_DRO_POS', 'int', 'xDroPos'),
    ('X_DRO_OFFSET', 'int', 'xDroOffset'),
    ('X_DRO_COUNT_INCH', 'int', 'xDroCountInch'),
    ('X_DRO_FACTOR', 'int', 'xDroFactor'),
    ('X_DRO_INVERT', 'int', 'xDroInvert'),
    ('X_USE_DRO', 'char', 'xUseDro'),
    ('X_DONE_DELAY', 'int', 'xDoneDelay'),
    ('X_HOME_DONE', 'int', 'xHomeDone'),
    ('X_HOME_STATUS', 'int', 'xHomeStatus'),
    ('Z_HOME_DONE', 'int', 'zHomeDone'),
    ('Z_HOME_STATUS', 'int', 'zHomeStatus'),
    ('PROBE_SPEED', 'float', 'probeSpeed'),
    ('PROBE_DIST', 'int', 'probeDist'),
    ('PROBE_INV', 'int', 'probeInv'),
    ('STEPPER_DRIVE', 'char', 'stepperDrive'),
    ('MOTOR_TEST', 'char', 'motorTest'),
    ('SPINDLE_ENCODER', 'char', 'spindleEncoder'),
    ('SPINDLE_SYNC_BOARD', 'char', 'spindleSyncBoard'),
    ('TURN_SYNC', 'char', 'turnSync'),
    ('THREAD_SYNC', 'char', 'threadSync'),
    ('CAP_TMR_ENABLE', 'char', 'capTmrEnable'),
    ('CFG_XILINX', 'char', 'cfgXilinx'),
    ('CFG_MPG', 'char', 'cfgMpg'),
    ('CFG_DRO', 'char', 'cfgDro'),
    ('CFG_LCD', 'char', 'cfgLcd'),
    ('CFG_FCY', 'int', 'cfgFcy'),
    ('CFG_SWITCH', 'int', 'cfgSwitch'),
    ('CFG_VAR_SPEED', 'int', 'cfgVarSpeed'),
    ('SETUP_DONE', 'char', 'setupDone'),
    ('ENC_PER_REV', 'uint16_t', 'encPerRev'),
    ('ENC_ENABLE', 'char', 'encEnable'),
    ('ENC_PRE_SCALER', 'uint16_t', 'encPreScaler'),
    ('ENC_TIMER', 'uint16_t', 'encTimer'),
    ('ENC_RUN_COUNT', 'int', 'encRunCount'),
    ('ENC_RUN', 'char', 'encRun'),
    ('ENC_COUNTER', 'int16_t', 'encCounter'),
    ('ENC_REV_COUNTER', 'int32_t', 'encRevCounter'),
    ('RPM', 'int16_t', 'rpm'),
    ('X_FREQUENCY', 'int32_t', 'xFrequency'),
    ('FREQ_MULT', 'int16_t', 'freqMult'),
    ('X_CFG_REG', 'int16_t', 'xCfgReg'),
    ('L_SYNC_CYCLE', 'uint16_t', 'lSyncCycle'),
    ('L_SYNC_OUTPUT', 'uint16_t', 'lSyncOutput'),
    ('L_SYNC_PRESCALER', 'uint16_t', 'lSyncPrescaler'),
    ('TH_Z_START', 'int32_t', 'thZStart'),
    ('TH_X_START', 'int32_t', 'thXStart'),
    ('TAN_THREAD_ANGLE', 'float', 'tanThreadAngle'),
    ('X_FEED', 'int16_t', 'xFeed'),
    ('RUNOUT_DISTANCE', 'float', 'runoutDistance'),
    ('RUNOUT_DEPTH', 'float', 'runoutDepth'),
    ('JOG_DEBUG', 'char', 'jogDebug'),
    ('PWM_FREQ', 'int16_t', 'pwmFreq'),
    ('MIN_SPEED', 'int16_t', 'minSpeed'),
    ('MAX_SPEED', 'int16_t', 'maxSpeed'),
    ('CURRENT_OP', 'char', 'currentOp'),
    ('MAX_PARM', 'int16_t', 'maxParm'),
    )
