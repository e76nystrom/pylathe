
# parameters

# spindle parameters

SP_STEPS             =   0
SP_MICRO             =   1
SP_MIN_RPM           =   2
SP_MAX_RPM           =   3
SP_RPM               =   4
SP_ACCEL_TIME        =   5
SP_ACCEL             =   6
SP_JOG_MIN_RPM       =   7
SP_JOG_MAX_RPM       =   8
SP_JOG_RPM           =   9
SP_JOG_ACCEL_TIME    =  10
SP_JOG_TIME_INITIAL  =  11
SP_JOG_TIME_INC      =  12
SP_JOG_TIME_MAX      =  13
SP_JOG_DIR           =  14
SP_DIR_FLAG          =  15
SP_TEST_INDEX        =  16
SP_TEST_ENCODER      =  17

# z axis parameters

Z_PITCH              =  18
Z_RATIO              =  19
Z_MICRO              =  20
Z_MOTOR              =  21
Z_ACCEL_TIME         =  22
Z_ACCEL              =  23
Z_BACKLASH           =  24
Z_STEP_FACTOR        =  25
Z_DIR_FLAG           =  26
Z_MPG_FLAG           =  27

# x axis parameters

X_PITCH              =  28
X_RATIO              =  29
X_MICRO              =  30
X_MOTOR              =  31
X_ACCEL_TIME         =  32
X_ACCEL              =  33
X_BACKLASH           =  34
X_STEP_FACTOR        =  35
X_DIR_FLAG           =  36
X_MPG_FLAG           =  37
X_DIAMETER           =  38

# z move parameters

Z_MOVE_MIN           =  39
Z_MOVE_MAX           =  40

# z jog parameters

Z_JOG_MIN            =  41
Z_JOG_MAX            =  42
Z_JOG_SPEED          =  43

# x move parameters

X_MOVE_MIN           =  44
X_MOVE_MAX           =  45

# x jog parameters

X_JOG_MIN            =  46
X_JOG_MAX            =  47
X_JOG_SPEED          =  48

# pass information

TOTAL_PASSES         =  49
CURRENT_PASS         =  50
MV_STATUS            =  51

# z axis move values

Z_MOVE_DIST          =  52
Z_MOVE_POS           =  53
Z_JOG_DIR            =  54
Z_SET_LOC            =  55
Z_LOC                =  56
Z_FLAG               =  57
Z_ABS_LOC            =  58
Z_MPG_INC            =  59
Z_MPG_MAX            =  60

# x axis move values

X_MOVE_DIST          =  61
X_MOVE_POS           =  62
X_JOG_DIR            =  63
X_SET_LOC            =  64
X_LOC                =  65
X_FLAG               =  66
X_ABS_LOC            =  67
X_MPG_INC            =  68
X_MPG_MAX            =  69

# common jog parameters

JOG_TIME_INITIAL     =  70
JOG_TIME_INC         =  71
JOG_TIME_MAX         =  72

# taper parameters

TAPER_CYCLE_DIST     =  73

# index pulse variables

INDEX_PRE_SCALER     =  74
LAST_INDEX_PERIOD    =  75
INDEX_PERIOD         =  76
REV_COUNTER          =  77

# z home offset

Z_HOME_OFFSET        =  78

# x home offset

X_HOME_OFFSET        =  79

# z home parameters

Z_HOME_SPEED         =  80
Z_HOME_DIST          =  81
Z_HOME_DIST_REV      =  82
Z_HOME_DIST_BACKOFF  =  83
Z_HOME_DIR           =  84

# x home parameters

X_HOME_SPEED         =  85
X_HOME_DIST          =  86
X_HOME_DIST_REV      =  87
X_HOME_DIST_BACKOFF  =  88
X_HOME_DIR           =  89

# x home test parameters

X_HOME_LOC           =  90
X_HOME_START         =  91
X_HOME_END           =  92

# z dro

Z_DRO_LOC            =  93
Z_DRO_OFFSET         =  94
Z_DRO_COUNT_INCH     =  95
Z_DRO_FACTOR         =  96
Z_DRO_INVERT         =  97
Z_USE_DRO            =  98
Z_DONE_DELAY         =  99
Z_DRO_FINAL_DIST     = 100

# x dro

X_DRO_LOC            = 101
X_DRO_OFFSET         = 102
X_DRO_COUNT_INCH     = 103
X_DRO_FACTOR         = 104
X_DRO_INVERT         = 105
X_USE_DRO            = 106
X_DONE_DELAY         = 107
X_DRO_FINAL_DIST     = 108

# x home or probe status

X_HOME_STATUS        = 109

# Z home or probe status

Z_HOME_STATUS        = 110

# probe configuration

PROBE_SPEED          = 111
PROBE_DIST           = 112
PROBE_INV            = 113

# configuration

STEPPER_DRIVE        = 114
MOTOR_TEST           = 115
SPINDLE_ENCODER      = 116
SPINDLE_SYNC_BOARD   = 117
TURN_SYNC            = 118
THREAD_SYNC          = 119
CAP_TMR_ENABLE       = 120
CFG_FPGA             = 121
CFG_MEGA             = 122
CFG_MPG              = 123
CFG_DRO              = 124
CFG_LCD              = 125
CFG_FCY              = 126
CFG_SWITCH           = 127
CFG_VAR_SPEED        = 128

# setup

SETUP_DONE           = 129

# encoder counts per revolution

ENC_PER_REV          = 130

# test encoder setup variables

ENC_ENABLE           = 131
ENC_PRE_SCALER       = 132
ENC_TIMER            = 133
ENC_RUN_COUNT        = 134

# test encoder status variables

ENC_RUN              = 135
ENC_COUNTER          = 136
ENC_REV_COUNTER      = 137

# measured spindle speed

RPM                  = 138

# fpga frequency variables

FPGA_FREQUENCY       = 139
FREQ_MULT            = 140

# xilinx configuration register

X_CFG_REG            = 141

# sync parameters

L_SYNC_CYCLE         = 142
L_SYNC_OUTPUT        = 143
L_SYNC_PRESCALER     = 144

# threading variables

TH_Z_START           = 145
TH_X_START           = 146
TAN_THREAD_ANGLE     = 147
X_FEED               = 148
RUNOUT_DISTANCE      = 149
RUNOUT_DEPTH         = 150

# jog debug

JOG_DEBUG            = 151

# motor and speed control

PWM_FREQ             = 152
MIN_SPEED            = 153
MAX_SPEED            = 154

# current operation

CURRENT_OP           = 155

# global limits and home

LIMIT_OVERRIDE       = 156
COMMON_LIMITS        = 157
LIMITS_ENABLED       = 158
COMMON_HOME          = 159

# z limits and home

Z_LIM_ENA            = 160
Z_LIM_NEG_INV        = 161
Z_LIM_POS_INV        = 162
Z_HOME_ENA           = 163
Z_HOME_INV           = 164

# x limits and home

X_LIM_ENA            = 165
X_LIM_NEG_INV        = 166
X_LIM_POS_INV        = 167
X_HOME_ENA           = 168
X_HOME_INV           = 169

# e stop

E_STOP_ENA           = 170
E_STOP_INV           = 171

# command pause

CMD_PAUSED           = 172

# arc parameters

ARC_RADIUS           = 173
ARC_X_CENTER         = 174
ARC_Z_CENTER         = 175
ARC_X_START          = 176
ARC_Z_START          = 177
ARC_X_END            = 178
ARC_Z_END            = 179
MAX_PARM             = 180

parmTable = ( \
    ('SP_STEPS', 'int16_t', 'spSteps'),
    ('SP_MICRO', 'int16_t', 'spMicro'),
    ('SP_MIN_RPM', 'float', 'spMinRpm'),
    ('SP_MAX_RPM', 'float', 'spMaxRpm'),
    ('SP_RPM', 'float', 'spRpm'),
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
    ('Z_HOME_DIST_REV', 'float', 'zHomeDistRev'),
    ('Z_HOME_DIST_BACKOFF', 'float', 'zHomeDistBackoff'),
    ('Z_HOME_DIR', 'int', 'zHomeDir'),
    ('X_HOME_SPEED', 'float', 'xHomeSpeed'),
    ('X_HOME_DIST', 'float', 'xHomeDist'),
    ('X_HOME_DIST_REV', 'float', 'xHomeDistRev'),
    ('X_HOME_DIST_BACKOFF', 'float', 'xHomeDistBackoff'),
    ('X_HOME_DIR', 'int', 'xHomeDir'),
    ('X_HOME_LOC', 'int', 'xHomeLoc'),
    ('X_HOME_START', 'int', 'xHomeStart'),
    ('X_HOME_END', 'int', 'xHomeEnd'),
    ('Z_DRO_LOC', 'int', 'zDroLoc'),
    ('Z_DRO_OFFSET', 'int', 'zDroOffset'),
    ('Z_DRO_COUNT_INCH', 'int', 'zDroCountInch'),
    ('Z_DRO_FACTOR', 'int', 'zDroFactor'),
    ('Z_DRO_INVERT', 'int', 'zDroInvert'),
    ('Z_USE_DRO', 'char', 'zUseDro'),
    ('Z_DONE_DELAY', 'int', 'zDoneDelay'),
    ('Z_DRO_FINAL_DIST', 'int', 'zDroFinalDist'),
    ('X_DRO_LOC', 'int', 'xDroLoc'),
    ('X_DRO_OFFSET', 'int', 'xDroOffset'),
    ('X_DRO_COUNT_INCH', 'int', 'xDroCountInch'),
    ('X_DRO_FACTOR', 'int', 'xDroFactor'),
    ('X_DRO_INVERT', 'int', 'xDroInvert'),
    ('X_USE_DRO', 'char', 'xUseDro'),
    ('X_DONE_DELAY', 'int', 'xDoneDelay'),
    ('X_DRO_FINAL_DIST', 'int', 'xDroFinalDist'),
    ('X_HOME_STATUS', 'int', 'xHomeStatus'),
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
    ('CFG_MEGA', 'char', 'cfgMega'),
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
    ('CMD_PAUSED', 'char', 'cmdPaused'),
    ('ARC_RADIUS', 'float', 'arcRadius'),
    ('ARC_X_CENTER', 'int', 'arcXCenter'),
    ('ARC_Z_CENTER', 'int', 'arcZCenter'),
    ('ARC_X_START', 'int', 'arcXStart'),
    ('ARC_Z_START', 'int', 'arcZStart'),
    ('ARC_X_END', 'int', 'arcXEnd'),
    ('ARC_Z_END', 'int', 'arcZEnd'),
    ('MAX_PARM', 'int16_t', 'maxParm'),
    )
