
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
Z_DIR_FLAG           =  24
Z_MPG_FLAG           =  25

# x axis parameters

X_PITCH              =  26
X_RATIO              =  27
X_MICRO              =  28
X_MOTOR              =  29
X_ACCEL_TIME         =  30
X_ACCEL              =  31
X_BACKLASH           =  32
X_DIR_FLAG           =  33
X_MPG_FLAG           =  34
X_DIAMETER           =  35

# z move parameters

Z_MOVE_MIN           =  36
Z_MOVE_MAX           =  37

# z jog parameters

Z_JOG_MIN            =  38
Z_JOG_MAX            =  39
Z_JOG_SPEED          =  40

# x move parameters

X_MOVE_MIN           =  41
X_MOVE_MAX           =  42

# x jog parameters

X_JOG_MIN            =  43
X_JOG_MAX            =  44
X_JOG_SPEED          =  45

# pass information

TOTAL_PASSES         =  46
CURRENT_PASS         =  47
MV_STATUS            =  48

# z axis move values

Z_MOVE_DIST          =  49
Z_MOVE_POS           =  50
Z_JOG_DIR            =  51
Z_SET_LOC            =  52
Z_LOC                =  53
Z_FLAG               =  54
Z_ABS_LOC            =  55
Z_MPG_INC            =  56
Z_MPG_MAX            =  57

# x axis move values

X_MOVE_DIST          =  58
X_MOVE_POS           =  59
X_JOG_DIR            =  60
X_SET_LOC            =  61
X_LOC                =  62
X_FLAG               =  63
X_ABS_LOC            =  64
X_MPG_INC            =  65
X_MPG_MAX            =  66

# common jog parameters

JOG_TIME_INITIAL     =  67
JOG_TIME_INC         =  68
JOG_TIME_MAX         =  69

# taper parameters

TAPER_CYCLE_DIST     =  70

# index pulse variables

INDEX_PRE_SCALER     =  71
LAST_INDEX_PERIOD    =  72
INDEX_PERIOD         =  73
REV_COUNTER          =  74

# z home offset

Z_HOME_OFFSET        =  75

# z dro

Z_DRO_POS            =  76
Z_DRO_OFFSET         =  77
Z_DRO_COUNT_INCH     =  78
Z_DRO_INVERT         =  79

# x home parameters

X_HOME_SPEED         =  80
X_HOME_DIST          =  81
X_HOME_BACKOFF_DIST  =  82
X_HOME_DIR           =  83

# x home test parameters

X_HOME_LOC           =  84
X_HOME_START         =  85
X_HOME_END           =  86
X_HOME_OFFSET        =  87
X_DRO_POS            =  88
X_DRO_OFFSET         =  89
X_DRO_COUNT_INCH     =  90
X_DRO_INVERT         =  91

# x home or probe status

X_HOME_DONE          =  92
X_HOME_STATUS        =  93

# Z home or probe status

Z_HOME_DONE          =  94
Z_HOME_STATUS        =  95

# probe configuration

PROBE_SPEED          =  96
PROBE_DIST           =  97
PROBE_INV            =  98

# configuration

STEPPER_DRIVE        =  99
MOTOR_TEST           = 100
SPINDLE_ENCODER      = 101
SPINDLE_SYNC_BOARD   = 102
TURN_SYNC            = 103
THREAD_SYNC          = 104
CAP_TMR_ENABLE       = 105
CFG_XILINX           = 106
CFG_MPG              = 107
CFG_DRO              = 108
CFG_LCD              = 109
CFG_FCY              = 110
CFG_SWITCH           = 111
CFG_VAR_SPEED        = 112

# setup

SETUP_DONE           = 113

# encoder counts per revolution

ENC_PER_REV          = 114

# test encoder setup variables

ENC_ENABLE           = 115
ENC_PRE_SCALER       = 116
ENC_TIMER            = 117
ENC_RUN_COUNT        = 118

# test encoder status variables

ENC_RUN              = 119
ENC_COUNTER          = 120
ENC_REV_COUNTER      = 121

# measured spindle speed

RPM                  = 122

# xilinx frequency variables

X_FREQUENCY          = 123
FREQ_MULT            = 124

# xilinx configuration register

X_CFG_REG            = 125

# sync parameters

L_SYNC_CYCLE         = 126
L_SYNC_OUTPUT        = 127
L_SYNC_PRESCALER     = 128

# threading variables

TH_Z_START           = 129
TH_X_START           = 130
TAN_THREAD_ANGLE     = 131
X_FEED               = 132
RUNOUT_DISTANCE      = 133
RUNOUT_DEPTH         = 134

# jog debug

JOG_DEBUG            = 135

# motor and speed control

PWM_FREQ             = 136
MIN_SPEED            = 137
MAX_SPEED            = 138

# current operation

CURRENT_OP           = 139
MAX_PARM             = 140

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
    ('X_DRO_INVERT', 'int', 'xDroInvert'),
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
