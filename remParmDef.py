
# parameters

# spindle parameters

SP_STEPS             =   0	# 0x00
SP_MICRO             =   1	# 0x01
SP_MIN_RPM           =   2	# 0x02
SP_MAX_RPM           =   3	# 0x03
SP_RPM               =   4	# 0x04
SP_ACCEL_TIME        =   5	# 0x05
SP_ACCEL             =   6	# 0x06
SP_JOG_MIN_RPM       =   7	# 0x07
SP_JOG_MAX_RPM       =   8	# 0x08
SP_JOG_RPM           =   9	# 0x09
SP_JOG_ACCEL_TIME    =  10	# 0x0a
SP_JOG_TIME_INITIAL  =  11	# 0x0b
SP_JOG_TIME_INC      =  12	# 0x0c
SP_JOG_TIME_MAX      =  13	# 0x0d
SP_JOG_DIR           =  14	# 0x0e
SP_DIR_FLAG          =  15	# 0x0f
SP_TEST_INDEX        =  16	# 0x10
SP_TEST_ENCODER      =  17	# 0x11

# z axis parameters

Z_PITCH              =  18	# 0x12
Z_RATIO              =  19	# 0x13
Z_MICRO              =  20	# 0x14
Z_MOTOR              =  21	# 0x15
Z_ACCEL_TIME         =  22	# 0x16
Z_ACCEL              =  23	# 0x17
Z_BACKLASH           =  24	# 0x18
Z_STEP_FACTOR        =  25	# 0x19
Z_DIR_FLAG           =  26	# 0x1a
Z_MPG_FLAG           =  27	# 0x1b

# x axis parameters

X_PITCH              =  28	# 0x1c
X_RATIO              =  29	# 0x1d
X_MICRO              =  30	# 0x1e
X_MOTOR              =  31	# 0x1f
X_ACCEL_TIME         =  32	# 0x20
X_ACCEL              =  33	# 0x21
X_BACKLASH           =  34	# 0x22
X_STEP_FACTOR        =  35	# 0x23
X_DIR_FLAG           =  36	# 0x24
X_MPG_FLAG           =  37	# 0x25
X_DIAMETER           =  38	# 0x26

# z move parameters

Z_MOVE_MIN           =  39	# 0x27
Z_MOVE_MAX           =  40	# 0x28

# z jog parameters

Z_JOG_MIN            =  41	# 0x29
Z_JOG_MAX            =  42	# 0x2a
Z_JOG_SPEED          =  43	# 0x2b

# x move parameters

X_MOVE_MIN           =  44	# 0x2c
X_MOVE_MAX           =  45	# 0x2d

# x jog parameters

X_JOG_MIN            =  46	# 0x2e
X_JOG_MAX            =  47	# 0x2f
X_JOG_SPEED          =  48	# 0x30

# pass information

TOTAL_PASSES         =  49	# 0x31
CURRENT_PASS         =  50	# 0x32
MV_STATUS            =  51	# 0x33

# z axis move values

Z_MOVE_DIST          =  52	# 0x34
Z_MOVE_POS           =  53	# 0x35
Z_JOG_DIR            =  54	# 0x36
Z_SET_LOC            =  55	# 0x37
Z_LOC                =  56	# 0x38
Z_FLAG               =  57	# 0x39
Z_ABS_LOC            =  58	# 0x3a
Z_MPG_INC            =  59	# 0x3b
Z_MPG_MAX            =  60	# 0x3c

# x axis move values

X_MOVE_DIST          =  61	# 0x3d
X_MOVE_POS           =  62	# 0x3e
X_JOG_DIR            =  63	# 0x3f
X_SET_LOC            =  64	# 0x40
X_LOC                =  65	# 0x41
X_FLAG               =  66	# 0x42
X_ABS_LOC            =  67	# 0x43
X_MPG_INC            =  68	# 0x44
X_MPG_MAX            =  69	# 0x45

# common jog parameters

JOG_TIME_INITIAL     =  70	# 0x46
JOG_TIME_INC         =  71	# 0x47
JOG_TIME_MAX         =  72	# 0x48

# taper parameters

TAPER_CYCLE_DIST     =  73	# 0x49

# index pulse variables

INDEX_PRE_SCALER     =  74	# 0x4a
LAST_INDEX_PERIOD    =  75	# 0x4b
INDEX_PERIOD         =  76	# 0x4c
REV_COUNTER          =  77	# 0x4d

# z home offset

Z_HOME_OFFSET        =  78	# 0x4e

# x home offset

X_HOME_OFFSET        =  79	# 0x4f

# z home parameters

Z_HOME_SPEED         =  80	# 0x50
Z_HOME_DIST          =  81	# 0x51
Z_HOME_DIST_REV      =  82	# 0x52
Z_HOME_DIST_BACKOFF  =  83	# 0x53
Z_HOME_DIR           =  84	# 0x54

# x home parameters

X_HOME_SPEED         =  85	# 0x55
X_HOME_DIST          =  86	# 0x56
X_HOME_DIST_REV      =  87	# 0x57
X_HOME_DIST_BACKOFF  =  88	# 0x58
X_HOME_DIR           =  89	# 0x59

# x home test parameters

X_HOME_LOC           =  90	# 0x5a
X_HOME_START         =  91	# 0x5b
X_HOME_END           =  92	# 0x5c

# z dro

Z_DRO_LOC            =  93	# 0x5d
Z_DRO_OFFSET         =  94	# 0x5e
Z_DRO_COUNT_INCH     =  95	# 0x5f
Z_DRO_FACTOR         =  96	# 0x60
Z_DRO_INVERT         =  97	# 0x61
Z_USE_DRO            =  98	# 0x62
Z_DONE_DELAY         =  99	# 0x63
Z_DRO_FINAL_DIST     = 100	# 0x64

# x dro

X_DRO_LOC            = 101	# 0x65
X_DRO_OFFSET         = 102	# 0x66
X_DRO_COUNT_INCH     = 103	# 0x67
X_DRO_FACTOR         = 104	# 0x68
X_DRO_INVERT         = 105	# 0x69
X_USE_DRO            = 106	# 0x6a
X_DONE_DELAY         = 107	# 0x6b
X_DRO_FINAL_DIST     = 108	# 0x6c

# x home or probe status

X_HOME_STATUS        = 109	# 0x6d

# Z home or probe status

Z_HOME_STATUS        = 110	# 0x6e

# probe configuration

PROBE_SPEED          = 111	# 0x6f
PROBE_DIST           = 112	# 0x70
PROBE_INV            = 113	# 0x71

# configuration

STEPPER_DRIVE        = 114	# 0x72
MOTOR_TEST           = 115	# 0x73
SPINDLE_ENCODER      = 116	# 0x74
SPINDLE_SYNC_BOARD   = 117	# 0x75
SPINDLE_INTERNAL_SYNC = 118	# 0x76
TURN_SYNC            = 119	# 0x77
THREAD_SYNC          = 120	# 0x78
CAP_TMR_ENABLE       = 121	# 0x79
CFG_FPGA             = 122	# 0x7a
CFG_MEGA             = 123	# 0x7b
CFG_MPG              = 124	# 0x7c
CFG_DRO              = 125	# 0x7d
CFG_LCD              = 126	# 0x7e
CFG_FCY              = 127	# 0x7f
CFG_SWITCH           = 128	# 0x80
CFG_VAR_SPEED        = 129	# 0x81

# setup

SETUP_DONE           = 130	# 0x82

# encoder counts per revolution

ENC_PER_REV          = 131	# 0x83

# test encoder setup variables

ENC_ENABLE           = 132	# 0x84
ENC_PRE_SCALER       = 133	# 0x85
ENC_TIMER            = 134	# 0x86
ENC_RUN_COUNT        = 135	# 0x87

# test encoder status variables

ENC_RUN              = 136	# 0x88
ENC_COUNTER          = 137	# 0x89
ENC_REV_COUNTER      = 138	# 0x8a

# measured spindle speed

RPM                  = 139	# 0x8b

# fpga frequency variables

FPGA_FREQUENCY       = 140	# 0x8c
FREQ_MULT            = 141	# 0x8d

# xilinx configuration register

X_CFG_REG            = 142	# 0x8e

# z sync parameters

L_SYNC_CYCLE         = 143	# 0x8f
L_SYNC_OUTPUT        = 144	# 0x90
L_SYNC_IN_PRESCALER  = 145	# 0x91
L_SYNC_OUT_PRESCALER = 146	# 0x92

# x sync parameters

L_X_SYNC_CYCLE       = 147	# 0x93
L_X_SYNC_OUTPUT      = 148	# 0x94
L_X_SYNC_IN_PRESCALER = 149	# 0x95
L_X_SYNC_OUT_PRESCALER = 150	# 0x96

# threading variables

TH_Z_START           = 151	# 0x97
TH_X_START           = 152	# 0x98
TAN_THREAD_ANGLE     = 153	# 0x99
X_FEED               = 154	# 0x9a
RUNOUT_DISTANCE      = 155	# 0x9b
RUNOUT_DEPTH         = 156	# 0x9c

# jog debug

JOG_DEBUG            = 157	# 0x9d

# motor and speed control

PWM_FREQ             = 158	# 0x9e
MIN_SPEED            = 159	# 0x9f
MAX_SPEED            = 160	# 0xa0

# current operation

CURRENT_OP           = 161	# 0xa1

# global limits and home

LIMIT_OVERRIDE       = 162	# 0xa2
COMMON_LIMITS        = 163	# 0xa3
LIMITS_ENABLED       = 164	# 0xa4
COMMON_HOME          = 165	# 0xa5

# z limits and home

Z_LIM_ENA            = 166	# 0xa6
Z_LIM_NEG_INV        = 167	# 0xa7
Z_LIM_POS_INV        = 168	# 0xa8
Z_HOME_ENA           = 169	# 0xa9
Z_HOME_INV           = 170	# 0xaa

# x limits and home

X_LIM_ENA            = 171	# 0xab
X_LIM_NEG_INV        = 172	# 0xac
X_LIM_POS_INV        = 173	# 0xad
X_HOME_ENA           = 174	# 0xae
X_HOME_INV           = 175	# 0xaf

# e stop

E_STOP_ENA           = 176	# 0xb0
E_STOP_INV           = 177	# 0xb1

# command pause

CMD_PAUSED           = 178	# 0xb2

# arc parameters

ARC_RADIUS           = 179	# 0xb3
ARC_X_CENTER         = 180	# 0xb4
ARC_Z_CENTER         = 181	# 0xb5
ARC_X_START          = 182	# 0xb6
ARC_Z_START          = 183	# 0xb7
ARC_X_END            = 184	# 0xb8
ARC_Z_END            = 185	# 0xb9
MEGA_VFD             = 186	# 0xba
MEGA_SIM             = 187	# 0xbb
USB_ENA              = 188	# 0xbc
MAX_PARM             = 189	# 0xbd

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
    ('LAST_INDEX_PERIOD', 'uint_t', 'lastIndexPeriod'),
    ('INDEX_PERIOD', 'uint_t', 'indexPeriod'),
    ('REV_COUNTER', 'uint_t', 'revCounter'),
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
    ('SPINDLE_INTERNAL_SYNC', 'char', 'spindleInternalSync'),
    ('TURN_SYNC', 'char', 'turnSync'),
    ('THREAD_SYNC', 'char', 'threadSync'),
    ('CAP_TMR_ENABLE', 'char', 'capTmrEnable'),
    ('CFG_FPGA', 'char', 'cfgFpga'),
    ('CFG_MEGA', 'char', 'cfgMega'),
    ('CFG_MPG', 'char', 'cfgMpg'),
    ('CFG_DRO', 'char', 'cfgDro'),
    ('CFG_LCD', 'char', 'cfgLcd'),
    ('CFG_FCY', 'uint_t', 'cfgFcy'),
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
    ('L_SYNC_IN_PRESCALER', 'uint16_t', 'lSyncInPrescaler'),
    ('L_SYNC_OUT_PRESCALER', 'uint16_t', 'lSyncOutPrescaler'),
    ('L_X_SYNC_CYCLE', 'uint16_t', 'lXSyncCycle'),
    ('L_X_SYNC_OUTPUT', 'uint16_t', 'lXSyncOutput'),
    ('L_X_SYNC_IN_PRESCALER', 'uint16_t', 'lXSyncInPrescaler'),
    ('L_X_SYNC_OUT_PRESCALER', 'uint16_t', 'lXSyncOutPrescaler'),
    ('TH_Z_START', 'int32_t', 'thZStart'),
    ('TH_X_START', 'int32_t', 'thXStart'),
    ('TAN_THREAD_ANGLE', 'float', 'tanThreadAngle'),
    ('X_FEED', 'int32_t', 'xFeed'),
    ('RUNOUT_DISTANCE', 'float', 'runoutDistance'),
    ('RUNOUT_DEPTH', 'float', 'runoutDepth'),
    ('JOG_DEBUG', 'char', 'jogDebug'),
    ('PWM_FREQ', 'uint_t', 'pwmFreq'),
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
    ('MEGA_VFD', 'char', 'megaVfd'),
    ('MEGA_SIM', 'char', 'megaSim'),
    ('USB_ENA', 'char', 'usbEna'),
    ('MAX_PARM', 'int16_t', 'maxParm'),
    )
