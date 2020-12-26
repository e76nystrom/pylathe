
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
Z_STEP_FACTOR        =  24
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
X_STEP_FACTOR        =  34
X_DIR_FLAG           =  35
X_MPG_FLAG           =  36
X_DIAMETER           =  37

# z move parameters

Z_MOVE_MIN           =  38
Z_MOVE_MAX           =  39

# z jog parameters

Z_JOG_MIN            =  40
Z_JOG_MAX            =  41
Z_JOG_SPEED          =  42

# x move parameters

X_MOVE_MIN           =  43
X_MOVE_MAX           =  44

# x jog parameters

X_JOG_MIN            =  45
X_JOG_MAX            =  46
X_JOG_SPEED          =  47

# pass information

TOTAL_PASSES         =  48
CURRENT_PASS         =  49
MV_STATUS            =  50

# z axis move values

Z_MOVE_DIST          =  51
Z_MOVE_POS           =  52
Z_JOG_DIR            =  53
Z_SET_LOC            =  54
Z_LOC                =  55
Z_FLAG               =  56
Z_ABS_LOC            =  57
Z_MPG_INC            =  58
Z_MPG_MAX            =  59

# x axis move values

X_MOVE_DIST          =  60
X_MOVE_POS           =  61
X_JOG_DIR            =  62
X_SET_LOC            =  63
X_LOC                =  64
X_FLAG               =  65
X_ABS_LOC            =  66
X_MPG_INC            =  67
X_MPG_MAX            =  68

# common jog parameters

JOG_TIME_INITIAL     =  69
JOG_TIME_INC         =  70
JOG_TIME_MAX         =  71

# taper parameters

TAPER_CYCLE_DIST     =  72

# index pulse variables

INDEX_PRE_SCALER     =  73
LAST_INDEX_PERIOD    =  74
INDEX_PERIOD         =  75
REV_COUNTER          =  76

# z home offset

Z_HOME_OFFSET        =  77

# x home offset

X_HOME_OFFSET        =  78

# z home parameters

Z_HOME_SPEED         =  79
Z_HOME_DIST          =  80
Z_HOME_BACKOFF_DIST  =  81
Z_HOME_DIR           =  82

# x home parameters

X_HOME_SPEED         =  83
X_HOME_DIST          =  84
X_HOME_BACKOFF_DIST  =  85
X_HOME_DIR           =  86

# x home test parameters

X_HOME_LOC           =  87
X_HOME_START         =  88
X_HOME_END           =  89

# z dro

Z_DRO_POS            =  90
Z_DRO_OFFSET         =  91
Z_DRO_COUNT_INCH     =  92
Z_DRO_FACTOR         =  93
Z_DRO_INVERT         =  94
Z_USE_DRO            =  95
Z_DONE_DELAY         =  96
Z_DRO_FINAL_DIST     =  97

# x dro

X_DRO_POS            =  98
X_DRO_OFFSET         =  99
X_DRO_COUNT_INCH     = 100
X_DRO_FACTOR         = 101
X_DRO_INVERT         = 102
X_USE_DRO            = 103
X_DONE_DELAY         = 104
X_DRO_FINAL_DIST     = 105

# x home or probe status

X_HOME_DONE          = 106
X_HOME_STATUS        = 107

# Z home or probe status

Z_HOME_DONE          = 108
Z_HOME_STATUS        = 109

# probe configuration

PROBE_SPEED          = 110
PROBE_DIST           = 111
PROBE_INV            = 112

# configuration

STEPPER_DRIVE        = 113
MOTOR_TEST           = 114
SPINDLE_ENCODER      = 115
SPINDLE_SYNC_BOARD   = 116
TURN_SYNC            = 117
THREAD_SYNC          = 118
CAP_TMR_ENABLE       = 119
CFG_FPGA             = 120
CFG_MPG              = 121
CFG_DRO              = 122
CFG_LCD              = 123
CFG_FCY              = 124
CFG_SWITCH           = 125
CFG_VAR_SPEED        = 126

# setup

SETUP_DONE           = 127

# encoder counts per revolution

ENC_PER_REV          = 128

# test encoder setup variables

ENC_ENABLE           = 129
ENC_PRE_SCALER       = 130
ENC_TIMER            = 131
ENC_RUN_COUNT        = 132

# test encoder status variables

ENC_RUN              = 133
ENC_COUNTER          = 134
ENC_REV_COUNTER      = 135

# measured spindle speed

RPM                  = 136

# fpga frequency variables

FPGA_FREQUENCY       = 137
FREQ_MULT            = 138

# xilinx configuration register

X_CFG_REG            = 139

# sync parameters

L_SYNC_CYCLE         = 140
L_SYNC_OUTPUT        = 141
L_SYNC_PRESCALER     = 142

# threading variables

TH_Z_START           = 143
TH_X_START           = 144
TAN_THREAD_ANGLE     = 145
X_FEED               = 146
RUNOUT_DISTANCE      = 147
RUNOUT_DEPTH         = 148

# jog debug

JOG_DEBUG            = 149

# motor and speed control

PWM_FREQ             = 150
MIN_SPEED            = 151
MAX_SPEED            = 152

# current operation

CURRENT_OP           = 153

# global limits and home

LIMIT_OVERRIDE       = 154
COMMON_LIMITS        = 155
LIMITS_ENABLED       = 156
COMMON_HOME          = 157

# z limits and home

Z_LIM_ENA            = 158
Z_LIM_NEG_INV        = 159
Z_LIM_POS_INV        = 160
Z_HOME_ENA           = 161
Z_HOME_INV           = 162

# x limits and home

X_LIM_ENA            = 163
X_LIM_NEG_INV        = 164
X_LIM_POS_INV        = 165
X_HOME_ENA           = 166
X_HOME_INV           = 167

# e stop

E_STOP_ENA           = 168
E_STOP_INV           = 169
MAX_PARM             = 170

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
    ('Z_STEP_FACTOR', 'int', 'zStepFactor'),
    ('Z_DIR_FLAG', 'char', 'zDirFlag'),
    ('Z_MPG_FLAG', 'char', 'zMpgFlag'),
    ('X_PITCH', 'float', 'xPitch'),
    ('X_RATIO', 'float', 'xRatio'),
    ('X_MICRO', 'int16_t', 'xMicro'),
    ('X_MOTOR', 'int16_t', 'xMotor'),
    ('X_ACCEL_TIME', 'float', 'xAccelTime'),
    ('X_ACCEL', 'float', 'xAccel'),
    ('X_BACKLASH', 'float', 'xBacklash'),
    ('X_STEP_FACTOR', 'int', 'xStepFactor'),
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
    ('X_HOME_OFFSET', 'int', 'xHomeOffset'),
    ('Z_HOME_SPEED', 'float', 'zHomeSpeed'),
    ('Z_HOME_DIST', 'float', 'zHomeDist'),
    ('Z_HOME_BACKOFF_DIST', 'float', 'zHomeBackoffDist'),
    ('Z_HOME_DIR', 'int', 'zHomeDir'),
    ('X_HOME_SPEED', 'float', 'xHomeSpeed'),
    ('X_HOME_DIST', 'float', 'xHomeDist'),
    ('X_HOME_BACKOFF_DIST', 'float', 'xHomeBackoffDist'),
    ('X_HOME_DIR', 'int', 'xHomeDir'),
    ('X_HOME_LOC', 'int', 'xHomeLoc'),
    ('X_HOME_START', 'int', 'xHomeStart'),
    ('X_HOME_END', 'int', 'xHomeEnd'),
    ('Z_DRO_POS', 'int', 'zDroPos'),
    ('Z_DRO_OFFSET', 'int', 'zDroOffset'),
    ('Z_DRO_COUNT_INCH', 'int', 'zDroCountInch'),
    ('Z_DRO_FACTOR', 'int', 'zDroFactor'),
    ('Z_DRO_INVERT', 'int', 'zDroInvert'),
    ('Z_USE_DRO', 'char', 'zUseDro'),
    ('Z_DONE_DELAY', 'int', 'zDoneDelay'),
    ('Z_DRO_FINAL_DIST', 'int', 'zDroFinalDist'),
    ('X_DRO_POS', 'int', 'xDroPos'),
    ('X_DRO_OFFSET', 'int', 'xDroOffset'),
    ('X_DRO_COUNT_INCH', 'int', 'xDroCountInch'),
    ('X_DRO_FACTOR', 'int', 'xDroFactor'),
    ('X_DRO_INVERT', 'int', 'xDroInvert'),
    ('X_USE_DRO', 'char', 'xUseDro'),
    ('X_DONE_DELAY', 'int', 'xDoneDelay'),
    ('X_DRO_FINAL_DIST', 'int', 'xDroFinalDist'),
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
    ('CFG_FPGA', 'char', 'cfgFpga'),
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
    ('FPGA_FREQUENCY', 'int32_t', 'fpgaFrequency'),
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
    ('LIMIT_OVERRIDE', 'char', 'limitOverride'),
    ('COMMON_LIMITS', 'char', 'commonLimits'),
    ('LIMITS_ENABLED', 'char', 'limitsEnabled'),
    ('COMMON_HOME', 'char', 'commonHome'),
    ('Z_LIM_ENA', 'char', 'zLimEna'),
    ('Z_LIM_NEG_INV', 'char', 'zLimNegInv'),
    ('Z_LIM_POS_INV', 'char', 'zLimPosInv'),
    ('Z_HOME_ENA', 'char', 'zHomeEna'),
    ('Z_HOME_INV', 'char', 'zHomeInv'),
    ('X_LIM_ENA', 'char', 'xLimEna'),
    ('X_LIM_NEG_INV', 'char', 'xLimNegInv'),
    ('X_LIM_POS_INV', 'char', 'xLimPosInv'),
    ('X_HOME_ENA', 'char', 'xHomeEna'),
    ('X_HOME_INV', 'char', 'xHomeInv'),
    ('E_STOP_ENA', 'char', 'eStopEna'),
    ('E_STOP_INV', 'char', 'eStopInv'),
    ('MAX_PARM', 'int16_t', 'maxParm'),
    )
