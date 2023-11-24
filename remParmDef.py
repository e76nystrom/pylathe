
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
SP_DIR_INV           =  15	# 0x0f
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
Z_DIR_INV            =  26	# 0x1a
Z_MPG_INV            =  27	# 0x1b

# x axis parameters

X_PITCH              =  28	# 0x1c
X_RATIO              =  29	# 0x1d
X_MICRO              =  30	# 0x1e
X_MOTOR              =  31	# 0x1f
X_ACCEL_TIME         =  32	# 0x20
X_ACCEL              =  33	# 0x21
X_BACKLASH           =  34	# 0x22
X_STEP_FACTOR        =  35	# 0x23
X_DIR_INV            =  36	# 0x24
X_MPG_INV            =  37	# 0x25
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
DRO_STEP             = 189	# 0xbd
MAX_PARM             = 190	# 0xbe

remParmTable = ( \
    ("SP_STEPS",               "int16_t",  "spSteps"            ), # 0x00   0
    ("SP_MICRO",               "int16_t",  "spMicro"            ), # 0x01   1
    ("SP_MIN_RPM",             "float",    "spMinRpm"           ), # 0x02   2
    ("SP_MAX_RPM",             "float",    "spMaxRpm"           ), # 0x03   3
    ("SP_RPM",                 "float",    "spRpm"              ), # 0x04   4
    ("SP_ACCEL_TIME",          "float",    "spAccelTime"        ), # 0x05   5
    ("SP_ACCEL",               "float",    "spAccel"            ), # 0x06   6
    ("SP_JOG_MIN_RPM",         "float",    "spJogMinRpm"        ), # 0x07   7
    ("SP_JOG_MAX_RPM",         "float",    "spJogMaxRpm"        ), # 0x08   8
    ("SP_JOG_RPM",             "float",    "spJogRpm"           ), # 0x09   9
    ("SP_JOG_ACCEL_TIME",      "float",    "spJogAccelTime"     ), # 0x0a  10
    ("SP_JOG_TIME_INITIAL",    "float",    "spJogTimeInitial"   ), # 0x0b  11
    ("SP_JOG_TIME_INC",        "float",    "spJogTimeInc"       ), # 0x0c  12
    ("SP_JOG_TIME_MAX",        "float",    "spJogTimeMax"       ), # 0x0d  13
    ("SP_JOG_DIR",             "char",     "spJogDir"           ), # 0x0e  14
    ("SP_DIR_INV",             "char",     "spDirInv"           ), # 0x0f  15
    ("SP_TEST_INDEX",          "char",     "spTestIndex"        ), # 0x10  16
    ("SP_TEST_ENCODER",        "char",     "spTestEncoder"      ), # 0x11  17
    ("Z_PITCH",                "float",    "zPitch"             ), # 0x12  18
    ("Z_RATIO",                "float",    "zRatio"             ), # 0x13  19
    ("Z_MICRO",                "int16_t",  "zMicro"             ), # 0x14  20
    ("Z_MOTOR",                "int16_t",  "zMotor"             ), # 0x15  21
    ("Z_ACCEL_TIME",           "float",    "zAccelTime"         ), # 0x16  22
    ("Z_ACCEL",                "float",    "zAccel"             ), # 0x17  23
    ("Z_BACKLASH",             "float",    "zBacklash"          ), # 0x18  24
    ("Z_STEP_FACTOR",          "int",      "zStepFactor"        ), # 0x19  25
    ("Z_DIR_INV",              "char",     "zDirInv"            ), # 0x1a  26
    ("Z_MPG_INV",              "char",     "zMpgInv"            ), # 0x1b  27
    ("X_PITCH",                "float",    "xPitch"             ), # 0x1c  28
    ("X_RATIO",                "float",    "xRatio"             ), # 0x1d  29
    ("X_MICRO",                "int16_t",  "xMicro"             ), # 0x1e  30
    ("X_MOTOR",                "int16_t",  "xMotor"             ), # 0x1f  31
    ("X_ACCEL_TIME",           "float",    "xAccelTime"         ), # 0x20  32
    ("X_ACCEL",                "float",    "xAccel"             ), # 0x21  33
    ("X_BACKLASH",             "float",    "xBacklash"          ), # 0x22  34
    ("X_STEP_FACTOR",          "int",      "xStepFactor"        ), # 0x23  35
    ("X_DIR_INV",              "char",     "xDirInv"            ), # 0x24  36
    ("X_MPG_INV",              "char",     "xMpgInv"            ), # 0x25  37
    ("X_DIAMETER",             "int",      "xDiameter"          ), # 0x26  38
    ("Z_MOVE_MIN",             "float",    "zMoveMin"           ), # 0x27  39
    ("Z_MOVE_MAX",             "float",    "zMoveMax"           ), # 0x28  40
    ("Z_JOG_MIN",              "float",    "zJogMin"            ), # 0x29  41
    ("Z_JOG_MAX",              "float",    "zJogMax"            ), # 0x2a  42
    ("Z_JOG_SPEED",            "float",    "zJogSpeed"          ), # 0x2b  43
    ("X_MOVE_MIN",             "float",    "xMoveMin"           ), # 0x2c  44
    ("X_MOVE_MAX",             "float",    "xMoveMax"           ), # 0x2d  45
    ("X_JOG_MIN",              "float",    "xJogMin"            ), # 0x2e  46
    ("X_JOG_MAX",              "float",    "xJogMax"            ), # 0x2f  47
    ("X_JOG_SPEED",            "float",    "xJogSpeed"          ), # 0x30  48
    ("TOTAL_PASSES",           "int16_t",  "totalPasses"        ), # 0x31  49
    ("CURRENT_PASS",           "int16_t",  "currentPass"        ), # 0x32  50
    ("MV_STATUS",              "int16_t",  "mvStatus"           ), # 0x33  51
    ("Z_MOVE_DIST",            "float",    "zMoveDist"          ), # 0x34  52
    ("Z_MOVE_POS",             "float",    "zMovePos"           ), # 0x35  53
    ("Z_JOG_DIR",              "int",      "zJogDir"            ), # 0x36  54
    ("Z_SET_LOC",              "float",    "zSetLoc"            ), # 0x37  55
    ("Z_LOC",                  "int",      "zLoc"               ), # 0x38  56
    ("Z_FLAG",                 "int",      "zFlag"              ), # 0x39  57
    ("Z_ABS_LOC",              "int",      "zAbsLoc"            ), # 0x3a  58
    ("Z_MPG_INC",              "int",      "zMpgInc"            ), # 0x3b  59
    ("Z_MPG_MAX",              "int",      "zMpgMax"            ), # 0x3c  60
    ("X_MOVE_DIST",            "float",    "xMoveDist"          ), # 0x3d  61
    ("X_MOVE_POS",             "float",    "xMovePos"           ), # 0x3e  62
    ("X_JOG_DIR",              "int",      "xJogDir"            ), # 0x3f  63
    ("X_SET_LOC",              "float",    "xSetLoc"            ), # 0x40  64
    ("X_LOC",                  "int",      "xLoc"               ), # 0x41  65
    ("X_FLAG",                 "int",      "xFlag"              ), # 0x42  66
    ("X_ABS_LOC",              "int",      "xAbsLoc"            ), # 0x43  67
    ("X_MPG_INC",              "int",      "xMpgInc"            ), # 0x44  68
    ("X_MPG_MAX",              "int",      "xMpgMax"            ), # 0x45  69
    ("JOG_TIME_INITIAL",       "float",    "jogTimeInitial"     ), # 0x46  70
    ("JOG_TIME_INC",           "float",    "jogTimeInc"         ), # 0x47  71
    ("JOG_TIME_MAX",           "float",    "jogTimeMax"         ), # 0x48  72
    ("TAPER_CYCLE_DIST",       "float",    "taperCycleDist"     ), # 0x49  73
    ("INDEX_PRE_SCALER",       "int",      "indexPreScaler"     ), # 0x4a  74
    ("LAST_INDEX_PERIOD",      "uint_t",   "lastIndexPeriod"    ), # 0x4b  75
    ("INDEX_PERIOD",           "uint_t",   "indexPeriod"        ), # 0x4c  76
    ("REV_COUNTER",            "uint_t",   "revCounter"         ), # 0x4d  77
    ("Z_HOME_OFFSET",          "int",      "zHomeOffset"        ), # 0x4e  78
    ("X_HOME_OFFSET",          "int",      "xHomeOffset"        ), # 0x4f  79
    ("Z_HOME_SPEED",           "float",    "zHomeSpeed"         ), # 0x50  80
    ("Z_HOME_DIST",            "float",    "zHomeDist"          ), # 0x51  81
    ("Z_HOME_DIST_REV",        "float",    "zHomeDistRev"       ), # 0x52  82
    ("Z_HOME_DIST_BACKOFF",    "float",    "zHomeDistBackoff"   ), # 0x53  83
    ("Z_HOME_DIR",             "int",      "zHomeDir"           ), # 0x54  84
    ("X_HOME_SPEED",           "float",    "xHomeSpeed"         ), # 0x55  85
    ("X_HOME_DIST",            "float",    "xHomeDist"          ), # 0x56  86
    ("X_HOME_DIST_REV",        "float",    "xHomeDistRev"       ), # 0x57  87
    ("X_HOME_DIST_BACKOFF",    "float",    "xHomeDistBackoff"   ), # 0x58  88
    ("X_HOME_DIR",             "int",      "xHomeDir"           ), # 0x59  89
    ("X_HOME_LOC",             "int",      "xHomeLoc"           ), # 0x5a  90
    ("X_HOME_START",           "int",      "xHomeStart"         ), # 0x5b  91
    ("X_HOME_END",             "int",      "xHomeEnd"           ), # 0x5c  92
    ("Z_DRO_LOC",              "int",      "zDroLoc"            ), # 0x5d  93
    ("Z_DRO_OFFSET",           "int",      "zDroOffset"         ), # 0x5e  94
    ("Z_DRO_COUNT_INCH",       "int",      "zDroCountInch"      ), # 0x5f  95
    ("Z_DRO_FACTOR",           "int",      "zDroFactor"         ), # 0x60  96
    ("Z_DRO_INVERT",           "int",      "zDroInvert"         ), # 0x61  97
    ("Z_USE_DRO",              "char",     "zUseDro"            ), # 0x62  98
    ("Z_DONE_DELAY",           "int",      "zDoneDelay"         ), # 0x63  99
    ("Z_DRO_FINAL_DIST",       "int",      "zDroFinalDist"      ), # 0x64 100
    ("X_DRO_LOC",              "int",      "xDroLoc"            ), # 0x65 101
    ("X_DRO_OFFSET",           "int",      "xDroOffset"         ), # 0x66 102
    ("X_DRO_COUNT_INCH",       "int",      "xDroCountInch"      ), # 0x67 103
    ("X_DRO_FACTOR",           "int",      "xDroFactor"         ), # 0x68 104
    ("X_DRO_INVERT",           "int",      "xDroInvert"         ), # 0x69 105
    ("X_USE_DRO",              "char",     "xUseDro"            ), # 0x6a 106
    ("X_DONE_DELAY",           "int",      "xDoneDelay"         ), # 0x6b 107
    ("X_DRO_FINAL_DIST",       "int",      "xDroFinalDist"      ), # 0x6c 108
    ("X_HOME_STATUS",          "int",      "xHomeStatus"        ), # 0x6d 109
    ("Z_HOME_STATUS",          "int",      "zHomeStatus"        ), # 0x6e 110
    ("PROBE_SPEED",            "float",    "probeSpeed"         ), # 0x6f 111
    ("PROBE_DIST",             "int",      "probeDist"          ), # 0x70 112
    ("PROBE_INV",              "int",      "probeInv"           ), # 0x71 113
    ("STEPPER_DRIVE",          "char",     "stepperDrive"       ), # 0x72 114
    ("MOTOR_TEST",             "char",     "motorTest"          ), # 0x73 115
    ("SPINDLE_ENCODER",        "char",     "spindleEncoder"     ), # 0x74 116
    ("SPINDLE_SYNC_BOARD",     "char",     "spindleSyncBoard"   ), # 0x75 117
    ("SPINDLE_INTERNAL_SYNC",  "char",     "spindleInternalSync"), # 0x76 118
    ("TURN_SYNC",              "char",     "turnSync"           ), # 0x77 119
    ("THREAD_SYNC",            "char",     "threadSync"         ), # 0x78 120
    ("CAP_TMR_ENABLE",         "char",     "capTmrEnable"       ), # 0x79 121
    ("CFG_FPGA",               "char",     "cfgFpga"            ), # 0x7a 122
    ("CFG_MEGA",               "char",     "cfgMega"            ), # 0x7b 123
    ("CFG_MPG",                "char",     "cfgMpg"             ), # 0x7c 124
    ("CFG_DRO",                "char",     "cfgDro"             ), # 0x7d 125
    ("CFG_LCD",                "char",     "cfgLcd"             ), # 0x7e 126
    ("CFG_FCY",                "uint_t",   "cfgFcy"             ), # 0x7f 127
    ("CFG_SWITCH",             "int",      "cfgSwitch"          ), # 0x80 128
    ("CFG_VAR_SPEED",          "int",      "cfgVarSpeed"        ), # 0x81 129
    ("SETUP_DONE",             "char",     "setupDone"          ), # 0x82 130
    ("ENC_PER_REV",            "uint16_t", "encPerRev"          ), # 0x83 131
    ("ENC_ENABLE",             "char",     "encEnable"          ), # 0x84 132
    ("ENC_PRE_SCALER",         "uint16_t", "encPreScaler"       ), # 0x85 133
    ("ENC_TIMER",              "uint16_t", "encTimer"           ), # 0x86 134
    ("ENC_RUN_COUNT",          "int",      "encRunCount"        ), # 0x87 135
    ("ENC_RUN",                "char",     "encRun"             ), # 0x88 136
    ("ENC_COUNTER",            "int16_t",  "encCounter"         ), # 0x89 137
    ("ENC_REV_COUNTER",        "int32_t",  "encRevCounter"      ), # 0x8a 138
    ("RPM",                    "int16_t",  "rpm"                ), # 0x8b 139
    ("FPGA_FREQUENCY",         "int32_t",  "fpgaFrequency"      ), # 0x8c 140
    ("FREQ_MULT",              "int16_t",  "freqMult"           ), # 0x8d 141
    ("X_CFG_REG",              "int16_t",  "xCfgReg"            ), # 0x8e 142
    ("L_SYNC_CYCLE",           "uint16_t", "lSyncCycle"         ), # 0x8f 143
    ("L_SYNC_OUTPUT",          "uint16_t", "lSyncOutput"        ), # 0x90 144
    ("L_SYNC_IN_PRESCALER",    "uint16_t", "lSyncInPrescaler"   ), # 0x91 145
    ("L_SYNC_OUT_PRESCALER",   "uint16_t", "lSyncOutPrescaler"  ), # 0x92 146
    ("L_X_SYNC_CYCLE",         "uint16_t", "lXSyncCycle"        ), # 0x93 147
    ("L_X_SYNC_OUTPUT",        "uint16_t", "lXSyncOutput"       ), # 0x94 148
    ("L_X_SYNC_IN_PRESCALER",  "uint16_t", "lXSyncInPrescaler"  ), # 0x95 149
    ("L_X_SYNC_OUT_PRESCALER", "uint16_t", "lXSyncOutPrescaler" ), # 0x96 150
    ("TH_Z_START",             "int32_t",  "thZStart"           ), # 0x97 151
    ("TH_X_START",             "int32_t",  "thXStart"           ), # 0x98 152
    ("TAN_THREAD_ANGLE",       "float",    "tanThreadAngle"     ), # 0x99 153
    ("X_FEED",                 "int32_t",  "xFeed"              ), # 0x9a 154
    ("RUNOUT_DISTANCE",        "float",    "runoutDistance"     ), # 0x9b 155
    ("RUNOUT_DEPTH",           "float",    "runoutDepth"        ), # 0x9c 156
    ("JOG_DEBUG",              "char",     "jogDebug"           ), # 0x9d 157
    ("PWM_FREQ",               "uint_t",   "pwmFreq"            ), # 0x9e 158
    ("MIN_SPEED",              "int16_t",  "minSpeed"           ), # 0x9f 159
    ("MAX_SPEED",              "int16_t",  "maxSpeed"           ), # 0xa0 160
    ("CURRENT_OP",             "char",     "currentOp"          ), # 0xa1 161
    ("LIMIT_OVERRIDE",         "char",     "limitOverride"      ), # 0xa2 162
    ("COMMON_LIMITS",          "char",     "commonLimits"       ), # 0xa3 163
    ("LIMITS_ENABLED",         "char",     "limitsEnabled"      ), # 0xa4 164
    ("COMMON_HOME",            "char",     "commonHome"         ), # 0xa5 165
    ("Z_LIM_ENA",              "char",     "zLimEna"            ), # 0xa6 166
    ("Z_LIM_NEG_INV",          "char",     "zLimNegInv"         ), # 0xa7 167
    ("Z_LIM_POS_INV",          "char",     "zLimPosInv"         ), # 0xa8 168
    ("Z_HOME_ENA",             "char",     "zHomeEna"           ), # 0xa9 169
    ("Z_HOME_INV",             "char",     "zHomeInv"           ), # 0xaa 170
    ("X_LIM_ENA",              "char",     "xLimEna"            ), # 0xab 171
    ("X_LIM_NEG_INV",          "char",     "xLimNegInv"         ), # 0xac 172
    ("X_LIM_POS_INV",          "char",     "xLimPosInv"         ), # 0xad 173
    ("X_HOME_ENA",             "char",     "xHomeEna"           ), # 0xae 174
    ("X_HOME_INV",             "char",     "xHomeInv"           ), # 0xaf 175
    ("E_STOP_ENA",             "char",     "eStopEna"           ), # 0xb0 176
    ("E_STOP_INV",             "char",     "eStopInv"           ), # 0xb1 177
    ("CMD_PAUSED",             "char",     "cmdPaused"          ), # 0xb2 178
    ("ARC_RADIUS",             "float",    "arcRadius"          ), # 0xb3 179
    ("ARC_X_CENTER",           "int",      "arcXCenter"         ), # 0xb4 180
    ("ARC_Z_CENTER",           "int",      "arcZCenter"         ), # 0xb5 181
    ("ARC_X_START",            "int",      "arcXStart"          ), # 0xb6 182
    ("ARC_Z_START",            "int",      "arcZStart"          ), # 0xb7 183
    ("ARC_X_END",              "int",      "arcXEnd"            ), # 0xb8 184
    ("ARC_Z_END",              "int",      "arcZEnd"            ), # 0xb9 185
    ("MEGA_VFD",               "char",     "megaVfd"            ), # 0xba 186
    ("MEGA_SIM",               "char",     "megaSim"            ), # 0xbb 187
    ("USB_ENA",                "char",     "usbEna"             ), # 0xbc 188
    ("DRO_STEP",               "char",     "droStep"            ), # 0xbd 189
    ("MAX_PARM",               "int16_t",  "maxParm"            ), # 0xbe 190
    )
