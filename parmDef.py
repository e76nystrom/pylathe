
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
SP_TEST_ENCODER      =  13

# z axis parameters

Z_PITCH              =  14
Z_RATIO              =  15
Z_MICRO              =  16
Z_MOTOR              =  17
Z_ACCEL_TIME         =  18
Z_ACCEL              =  19
Z_BACKLASH           =  20
Z_DIR_FLAG           =  21
Z_MPG_FLAG           =  22

# x axis parameters

X_PITCH              =  23
X_RATIO              =  24
X_MICRO              =  25
X_MOTOR              =  26
X_ACCEL_TIME         =  27
X_ACCEL              =  28
X_BACKLASH           =  29
X_DIR_FLAG           =  30
X_MPG_FLAG           =  31
X_DIAMETER           =  32

# z move parameters

Z_MOVE_MIN           =  33
Z_MOVE_MAX           =  34

# z jog parameters

Z_JOG_MIN            =  35
Z_JOG_MAX            =  36
Z_JOG_SPEED          =  37

# x move parameters

X_MOVE_MIN           =  38
X_MOVE_MAX           =  39

# x jog parameters

X_JOG_MIN            =  40
X_JOG_MAX            =  41
X_JOG_SPEED          =  42

# pass information

TOTAL_PASSES         =  43
CURRENT_PASS         =  44
MV_STATUS            =  45

# z axis move values

Z_MOVE_DIST          =  46
Z_MOVE_POS           =  47
Z_JOG_DIR            =  48
Z_SET_LOC            =  49
Z_LOC                =  50
Z_FLAG               =  51
Z_ABS_LOC            =  52
Z_MPG_INC            =  53
Z_MPG_MAX            =  54

# x axis move values

X_MOVE_DIST          =  55
X_MOVE_POS           =  56
X_JOG_DIR            =  57
X_SET_LOC            =  58
X_LOC                =  59
X_FLAG               =  60
X_ABS_LOC            =  61
X_MPG_INC            =  62
X_MPG_MAX            =  63

# taper parameters

TAPER_CYCLE_DIST     =  64

# index pulse variables

INDEX_PRE_SCALER     =  65
LAST_INDEX_PERIOD    =  66
INDEX_PERIOD         =  67
REV_COUNTER          =  68

# z home offset

Z_HOME_OFFSET        =  69

# z dro

Z_DRO_POS            =  70
Z_DRO_OFFSET         =  71
Z_DRO_INCH           =  72
Z_DRO_INVERT         =  73

# x home parameters

X_HOME_SPEED         =  74
X_HOME_DIST          =  75
X_HOME_BACKOFF_DIST  =  76
X_HOME_DIR           =  77

# x home test parameters

X_HOME_LOC           =  78
X_HOME_START         =  79
X_HOME_END           =  80
X_HOME_OFFSET        =  81
X_DRO_POS            =  82
X_DRO_OFFSET         =  83
X_DRO_INCH           =  84
X_DRO_INVERT         =  85

# x home or probe status

X_HOME_DONE          =  86
X_HOME_STATUS        =  87

# Z home or probe status

Z_HOME_DONE          =  88
Z_HOME_STATUS        =  89

# probe configuration

PROBE_SPEED          =  90
PROBE_DIST           =  91
PROBE_INV            =  92

# configuration

STEPPER_DRIVE        =  93
MOTOR_TEST           =  94
SPINDLE_ENCODER      =  95
CFG_XILINX           =  96
CFG_MPG              =  97
CFG_DRO              =  98
CFG_LCD              =  99
CFG_FCY              = 100

# setup

SETUP_DONE           = 101

# encoder counts per revolution

ENC_PER_REV          = 102

# test encoder setup variables

ENC_ENABLE           = 103
ENC_PRE_SCALER       = 104
ENC_TIMER            = 105
ENC_RUN_COUNT        = 106

# test encoder status variables

ENC_RUN              = 107
ENC_COUNTER          = 108
ENC_REV_COUNTER      = 109

# measured spindle speed

RPM                  = 110

# xilinx frequency variables

X_FREQUENCY          = 111
FREQ_MULT            = 112

# xilinx configuration register

X_CFG_REG            = 113

# max parameter number

MAX_PARM             = 114

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
    ('TAPER_CYCLE_DIST', 'float', 'taperCycleDist'),
    ('INDEX_PRE_SCALER', 'int', 'indexPreScaler'),
    ('LAST_INDEX_PERIOD', 'unsigned int', 'lastIndexPeriod'),
    ('INDEX_PERIOD', 'unsigned int', 'indexPeriod'),
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
    ('SPINDLE_ENCODER', 'char', 'spindleEncoder'),
    ('CFG_XILINX', 'char', 'cfgXilinx'),
    ('CFG_MPG', 'char', 'cfgMpg'),
    ('CFG_DRO', 'char', 'cfgDro'),
    ('CFG_LCD', 'char', 'cfgLcd'),
    ('CFG_FCY', 'int', 'cfgFcy'),
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
    ('MAX_PARM', 'int16_t', 'maxParm'),
    )
