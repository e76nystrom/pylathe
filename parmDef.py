
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
SP_JOG_DIR           =  10
SP_DIR_FLAG          =  11
SP_TEST_INDEX        =  12

# z axis parameters

Z_PITCH              =  13
Z_RATIO              =  14
Z_MICRO              =  15
Z_MOTOR              =  16
Z_ACCEL_TIME         =  17
Z_ACCEL              =  18
Z_BACKLASH           =  19
Z_DIR_FLAG           =  20
Z_MPG_FLAG           =  21

# x axis parameters

X_PITCH              =  22
X_RATIO              =  23
X_MICRO              =  24
X_MOTOR              =  25
X_ACCEL_TIME         =  26
X_ACCEL              =  27
X_BACKLASH           =  28
X_DIR_FLAG           =  29
X_MPG_FLAG           =  30
X_DIAMETER           =  31

# z move parameters

Z_MOVE_MIN           =  32
Z_MOVE_MAX           =  33

# z jog parameters

Z_JOG_MIN            =  34
Z_JOG_MAX            =  35
Z_JOG_SPEED          =  36

# x move parameters

X_MOVE_MIN           =  37
X_MOVE_MAX           =  38

# x jog parameters

X_JOG_MIN            =  39
X_JOG_MAX            =  40
X_JOG_SPEED          =  41

# pass information

TOTAL_PASSES         =  42
CURRENT_PASS         =  43
MV_STATUS            =  44

# z axis move values

Z_MOVE_DIST          =  45
Z_MOVE_POS           =  46
Z_JOG_DIR            =  47
Z_SET_LOC            =  48
Z_LOC                =  49
Z_FLAG               =  50
Z_ABS_LOC            =  51
Z_MPG_INC            =  52

# x axis move values

X_MOVE_DIST          =  53
X_MOVE_POS           =  54
X_JOG_DIR            =  55
X_SET_LOC            =  56
X_LOC                =  57
X_FLAG               =  58
X_ABS_LOC            =  59
X_MPG_INC            =  60

# taper parameters

TAPER_CYCLE_DIST     =  61

# index pulse variables

INDEX_PRE_SCALER     =  62
LAST_INDEX_PERIOD    =  63
INDEX_PERIOD         =  64
REV_COUNTER          =  65

# z home offset

Z_HOME_OFFSET        =  66

# z dro

Z_DRO_POS            =  67
Z_DRO_OFFSET         =  68
Z_DRO_INCH           =  69
Z_DRO_INVERT         =  70

# x home parameters

X_HOME_SPEED         =  71
X_HOME_DIST          =  72
X_HOME_BACKOFF_DIST  =  73
X_HOME_DIR           =  74

# x home test parameters

X_HOME_LOC           =  75
X_HOME_START         =  76
X_HOME_END           =  77
X_HOME_OFFSET        =  78
X_DRO_POS            =  79
X_DRO_OFFSET         =  80
X_DRO_INCH           =  81
X_DRO_INVERT         =  82

# x home or probe status

X_HOME_DONE          =  83
X_HOME_STATUS        =  84

# Z home or probe status

Z_HOME_DONE          =  85
Z_HOME_STATUS        =  86

# probe configuration

PROBE_SPEED          =  87
PROBE_DIST           =  88
PROBE_INV            =  89

# configuration

STEPPER_DRIVE        =  90
MOTOR_TEST           =  91
CFG_XILINX           =  92
CFG_MPG              =  93
CFG_DRO              =  94
CFG_LCD              =  95
CFG_FCY              =  96

# setup

SETUP_DONE           =  97

# encoder counts per revolution

ENC_MAX              =  98

# test encoder setup variables

ENC_ENABLE           =  99
ENC_PRE_SCALER       = 100
ENC_TIMER            = 101
ENC_RUN_COUNT        = 102

# test encoder status variables

ENC_RUN              = 103
ENC_COUNTER          = 104
ENC_REV_COUNTER      = 105

# measured spindle speed

RPM                  = 106

# xilinx frequency variables

X_FREQUENCY          = 107
FREQ_MULT            = 108

# xilinx configuration register

X_CFG_REG            = 109

# max parameter number

MAX_PARM             = 110

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
    ('SP_JOG_DIR', 'char', 'spJogDir'),
    ('SP_DIR_FLAG', 'char', 'spDirFlag'),
    ('SP_TEST_INDEX', 'char', 'spTestIndex'),
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
    ('X_MOVE_DIST', 'float', 'xMoveDist'),
    ('X_MOVE_POS', 'float', 'xMovePos'),
    ('X_JOG_DIR', 'int', 'xJogDir'),
    ('X_SET_LOC', 'float', 'xSetLoc'),
    ('X_LOC', 'int', 'xLoc'),
    ('X_FLAG', 'int', 'xFlag'),
    ('X_ABS_LOC', 'int', 'xAbsLoc'),
    ('X_MPG_INC', 'int', 'xMpgInc'),
    ('TAPER_CYCLE_DIST', 'float', 'taperCycleDist'),
    ('INDEX_PRE_SCALER', 'int', 'indexPreScaler'),
    ('LAST_INDEX_PERIOD', 'int', 'lastIndexPeriod'),
    ('INDEX_PERIOD', 'int', 'indexPeriod'),
    ('REV_COUNTER', 'unsigned int', 'revCounter'),
    ('Z_HOME_OFFSET', 'float', 'zHomeOffset'),
    ('Z_DRO_POS', 'int', 'zDroPos'),
    ('Z_DRO_OFFSET', 'float', 'zDroOffset'),
    ('Z_DRO_INCH', 'int', 'zDroInch'),
    ('Z_DRO_INVERT', 'int', 'zDroInvert'),
    ('X_HOME_SPEED', 'float', 'xHomeSpeed'),
    ('X_HOME_DIST', 'float', 'xHomeDist'),
    ('X_HOME_BACKOFF_DIST', 'float', 'xHomeBackoffDist'),
    ('X_HOME_DIR', 'int', 'xHomeDir'),
    ('X_HOME_LOC', 'int', 'xHomeLoc'),
    ('X_HOME_START', 'int', 'xHomeStart'),
    ('X_HOME_END', 'int', 'xHomeEnd'),
    ('X_HOME_OFFSET', 'float', 'xHomeOffset'),
    ('X_DRO_POS', 'int', 'xDroPos'),
    ('X_DRO_OFFSET', 'float', 'xDroOffset'),
    ('X_DRO_INCH', 'int', 'xDroInch'),
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
    ('CFG_XILINX', 'char', 'cfgXilinx'),
    ('CFG_MPG', 'char', 'cfgMpg'),
    ('CFG_DRO', 'char', 'cfgDro'),
    ('CFG_LCD', 'char', 'cfgLcd'),
    ('CFG_FCY', 'int', 'cfgFcy'),
    ('SETUP_DONE', 'char', 'setupDone'),
    ('ENC_MAX', 'uint16_t', 'encMax'),
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
    ('MAX_PARM', 'int16_t', 'maxParm'),
    )
