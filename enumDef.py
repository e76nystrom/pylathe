
# enums

# axis control states

AXIS_IDLE        =  0           # idle
AXIS_WAIT_BACKLASH =  1         # wait for backlash move complete
AXIS_START_MOVE  =  2           # start axis move
AXIS_WAIT_MOVE   =  3           # wait for move complete
AXIS_DELAY       =  4           # wait for position to settle
AXIS_DONE        =  5           # clean up state
AXIS_STATES      =  6           # number of states

axisStatesList = ( \
    "AXIS_IDLE",
    "AXIS_WAIT_BACKLASH",
    "AXIS_START_MOVE",
    "AXIS_WAIT_MOVE",
    "AXIS_DELAY",
    "AXIS_DONE",
    "AXIS_STATES",
    )

axisStatesText = ( \
    "idle",
    "wait for backlash move complete",
    "start axis move",
    "wait for move complete",
    "wait for position to settle",
    "clean up state",
    "number of states",
    )

# move control states

M_IDLE           =  0           # idle state
M_WAIT_Z         =  1           # wait for z to complete
M_WAIT_X         =  2           # wait for x to complete
M_WAIT_SPINDLE   =  3           # wait for spindle start
M_WAIT_SYNC_PARMS =  4          # wait for sync parameters
M_WAIT_SYNC_CMD  =  5           # wait for sync command
M_START_SYNC     =  6           # start sync
M_WAIT_SYNC_READY =  7          # wait for sync
M_WAIT_SYNC_DONE =  8           # wait for sync done
M_WAIT_MEASURE_DONE =  9        # wait for measurement done
M_WAIT_PROBE     = 10           # wait for probe to complete
M_WAIT_MEASURE   = 11           # wait for measurement to complete
M_WAIT_SAFE_X    = 12           # wait for move to safe x to complete
M_WAIT_SAFE_Z    = 13           # wait for move to safe z to complete
M_WAIT_ARC       = 14           # wait for arc move to complete

mStatesList = ( \
    "M_IDLE",
    "M_WAIT_Z",
    "M_WAIT_X",
    "M_WAIT_SPINDLE",
    "M_WAIT_SYNC_PARMS",
    "M_WAIT_SYNC_CMD",
    "M_START_SYNC",
    "M_WAIT_SYNC_READY",
    "M_WAIT_SYNC_DONE",
    "M_WAIT_MEASURE_DONE",
    "M_WAIT_PROBE",
    "M_WAIT_MEASURE",
    "M_WAIT_SAFE_X",
    "M_WAIT_SAFE_Z",
    "M_WAIT_ARC",
    )

mStatesText = ( \
    "idle state",
    "wait for z to complete",
    "wait for x to complete",
    "wait for spindle start",
    "wait for sync parameters",
    "wait for sync command",
    "start sync",
    "wait for sync",
    "wait for sync done",
    "wait for measurement done",
    "wait for probe to complete",
    "wait for measurement to complete",
    "wait for move to safe x to complete",
    "wait for move to safe z to complete",
    "wait for arc move to complete",
    )

# move control commands

Q_MOVE_Z         =  0           # move z
Q_MOVE_X         =  1           # move x
Q_SAVE_Z         =  2           # save z
Q_SAVE_X         =  3           # save x
Q_SAVE_Z_OFFSET  =  4           # save z offset
Q_SAVE_X_OFFSET  =  5           # save x offset
Q_SAVE_TAPER     =  6           # save taper
Q_MOVE_Z_X       =  7           # move x in sync with z
Q_MOVE_X_Z       =  8           # move z in sync with x
Q_TAPER_Z_X      =  9           # taper x
Q_TAPER_X_Z      = 10           # taper z
Q_START_SPINDLE  = 11           # spindle start
Q_STOP_SPINDLE   = 12           # spindle stop
Q_Z_SYN_SETUP    = 13           # z sync setup
Q_X_SYN_SETUP    = 14           # x sync setup
Q_SEND_SYNC_PARMS = 15          # send sync parameters
Q_SYNC_COMMAND   = 16           # send sync command
Q_PASS_NUM       = 17           # set pass number
Q_QUE_PAUSE      = 18           # pause queue
Q_MOVE_Z_OFFSET  = 19           # move z offset
Q_SAVE_FEED_TYPE = 20           # save feed type
Q_Z_FEED_SETUP   = 21           # setup z feed
Q_X_FEED_SETUP   = 22           # setup x feed
Q_SAVE_FLAGS     = 23           # save thread flags
Q_PROBE_Z        = 24           # probe in z direction
Q_PROBE_X        = 25           # probe in x direction
Q_SAVE_Z_DRO     = 26           # save z dro reading
Q_SAVE_X_DRO     = 27           # save x dro reading
Q_QUE_PARM       = 28           # save parameter in queue
Q_MOVE_ARC       = 29           # move in an arc
Q_OP_DONE        = 30           # operation done

mCommandsList = ( \
    "Q_MOVE_Z",
    "Q_MOVE_X",
    "Q_SAVE_Z",
    "Q_SAVE_X",
    "Q_SAVE_Z_OFFSET",
    "Q_SAVE_X_OFFSET",
    "Q_SAVE_TAPER",
    "Q_MOVE_Z_X",
    "Q_MOVE_X_Z",
    "Q_TAPER_Z_X",
    "Q_TAPER_X_Z",
    "Q_START_SPINDLE",
    "Q_STOP_SPINDLE",
    "Q_Z_SYN_SETUP",
    "Q_X_SYN_SETUP",
    "Q_SEND_SYNC_PARMS",
    "Q_SYNC_COMMAND",
    "Q_PASS_NUM",
    "Q_QUE_PAUSE",
    "Q_MOVE_Z_OFFSET",
    "Q_SAVE_FEED_TYPE",
    "Q_Z_FEED_SETUP",
    "Q_X_FEED_SETUP",
    "Q_SAVE_FLAGS",
    "Q_PROBE_Z",
    "Q_PROBE_X",
    "Q_SAVE_Z_DRO",
    "Q_SAVE_X_DRO",
    "Q_QUE_PARM",
    "Q_MOVE_ARC",
    "Q_OP_DONE",
    )

mCommandsText = ( \
    "move z",
    "move x",
    "save z",
    "save x",
    "save z offset",
    "save x offset",
    "save taper",
    "move x in sync with z",
    "move z in sync with x",
    "taper x",
    "taper z",
    "spindle start",
    "spindle stop",
    "z sync setup",
    "x sync setup",
    "send sync parameters",
    "send sync command",
    "set pass number",
    "pause queue",
    "move z offset",
    "save feed type",
    "setup z feed",
    "setup x feed",
    "save thread flags",
    "probe in z direction",
    "probe in x direction",
    "save z dro reading",
    "save x dro reading",
    "save parameter in queue",
    "move in an arc",
    "operation done",
    )

# move control operation

OP_TURN          =  0           # turn
OP_FACE          =  1           # face
OP_CUTOFF        =  2           # cutoff
OP_TAPER         =  3           # taper
OP_THREAD        =  4           # thread
OP_ARC           =  5           # arc

operationsList = ( \
    "OP_TURN",
    "OP_FACE",
    "OP_CUTOFF",
    "OP_TAPER",
    "OP_THREAD",
    "OP_ARC",
    )

operationsText = ( \
    "turn",
    "face",
    "cutoff",
    "taper",
    "thread",
    "arc",
    )

# home control states

H_IDLE           =  0           # idle state
H_HOME           =  1           # found home switch
H_OFF_HOME       =  2           # off home switch
H_BACKOFF        =  3           # backoff dist from switch
H_SLOW           =  4           # found home slowly

hStatesList = ( \
    "H_IDLE",
    "H_HOME",
    "H_OFF_HOME",
    "H_BACKOFF",
    "H_SLOW",
    )

hStatesText = ( \
    "idle state",
    "found home switch",
    "off home switch",
    "backoff dist from switch",
    "found home slowly",
    )

# debug axis message types

D_BASE           =  0           # axis base
D_MOV            =  1           # move location
D_LOC            =  2           # location
D_DST            =  3           # distance
D_STP            =  4           # steps
D_ST             =  5           # state
D_BSTP           =  6           # backlash steps
D_DRO            =  7           # dro location
D_PDRO           =  8           # pass dro location
D_EXP            =  9           # expected location
D_ERR            = 10           # error with respect to dro
D_WT             = 11           # wait
D_DN             = 12           # done
D_EST            = 13           # spindle encoder start count
D_EDN            = 14           # spindle encoder done count
D_X              = 15           # 
D_Y              = 16           # 
D_IDXD           = 17           # dro at index pulse
D_IDXP           = 18           # position at index pulse
D_AMAX           = 19           # axis maximum

DAxisMessageList = ( \
    "D_BASE",
    "D_MOV",
    "D_LOC",
    "D_DST",
    "D_STP",
    "D_ST",
    "D_BSTP",
    "D_DRO",
    "D_PDRO",
    "D_EXP",
    "D_ERR",
    "D_WT",
    "D_DN",
    "D_EST",
    "D_EDN",
    "D_X",
    "D_Y",
    "D_IDXD",
    "D_IDXP",
    "D_AMAX",
    )

DAxisMessageText = ( \
    "axis base",
    "move location",
    "location",
    "distance",
    "steps",
    "state",
    "backlash steps",
    "dro location",
    "pass dro location",
    "expected location",
    "error with respect to dro",
    "wait",
    "done",
    "spindle encoder start count",
    "spindle encoder done count",
    "",
    "",
    "dro at index pulse",
    "position at index pulse",
    "axis maximum",
    )

# debug message types

D_PASS           =  0           # pass done
D_DONE           =  1           # all operations done
D_TEST           =  2           # test message
D_HST            =  3           # home state
D_MSTA           =  4           # move state
D_MCMD           =  5           # move command
D_XBASE          =  6           # x base
D_XMOV           =  7           # x move location
D_XLOC           =  8           # x location
D_XDST           =  9           # x distance
D_XSTP           = 10           # x steps
D_XST            = 11           # x state
D_XBSTP          = 12           # x backlash steps
D_XDRO           = 13           # x dro location
D_XPDRO          = 14           # x pass dro location
D_XEXP           = 15           # x expected location
D_XERR           = 16           # x error with respect to dro
D_XWT            = 17           # x wait
D_XDN            = 18           # x done
D_XEST           = 19           # x spindle encoder start count
D_XEDN           = 20           # x spindle encoder done count
D_XX             = 21           # x 
D_XY             = 22           # x 
D_XIDXD          = 23           # x dro at index pulse
D_XIDXP          = 24           # x position at index pulse
D_ZBASE          = 25           # Z base
D_ZMOV           = 26           # z move location
D_ZLOC           = 27           # z location
D_ZDST           = 28           # z distance
D_ZSTP           = 29           # z steps
D_ZST            = 30           # z state
D_ZBSTP          = 31           # z backlash steps
D_ZDRO           = 32           # z dro location
D_ZPDRO          = 33           # z pass dro location
D_ZEXP           = 34           # z expected location
D_ZERR           = 35           # z error with respect to dro
D_ZWT            = 36           # z wait
D_ZDN            = 37           # z done
D_ZEST           = 38           # z spindle encoder start count
D_ZEDN           = 39           # Z spindle encoder done count
D_ZX             = 40           # z 
D_ZY             = 41           # z 
D_ZIDXD          = 42           # z dro at index pulse
D_ZIDXP          = 43           # z position at index pulse
D_MAX            = 44           # debug maximum

dMessageList = ( \
    "D_PASS",
    "D_DONE",
    "D_TEST",
    "D_HST",
    "D_MSTA",
    "D_MCMD",
    "D_XBASE",
    "D_XMOV",
    "D_XLOC",
    "D_XDST",
    "D_XSTP",
    "D_XST",
    "D_XBSTP",
    "D_XDRO",
    "D_XPDRO",
    "D_XEXP",
    "D_XERR",
    "D_XWT",
    "D_XDN",
    "D_XEST",
    "D_XEDN",
    "D_XX",
    "D_XY",
    "D_XIDXD",
    "D_XIDXP",
    "D_ZBASE",
    "D_ZMOV",
    "D_ZLOC",
    "D_ZDST",
    "D_ZSTP",
    "D_ZST",
    "D_ZBSTP",
    "D_ZDRO",
    "D_ZPDRO",
    "D_ZEXP",
    "D_ZERR",
    "D_ZWT",
    "D_ZDN",
    "D_ZEST",
    "D_ZEDN",
    "D_ZX",
    "D_ZY",
    "D_ZIDXD",
    "D_ZIDXP",
    "D_MAX",
    )

dMessageText = ( \
    "pass done",
    "all operations done",
    "test message",
    "home state",
    "move state",
    "move command",
    "x base",
    "x move location",
    "x location",
    "x distance",
    "x steps",
    "x state",
    "x backlash steps",
    "x dro location",
    "x pass dro location",
    "x expected location",
    "x error with respect to dro",
    "x wait",
    "x done",
    "x spindle encoder start count",
    "x spindle encoder done count",
    "x ",
    "x ",
    "x dro at index pulse",
    "x position at index pulse",
    "Z base",
    "z move location",
    "z location",
    "z distance",
    "z steps",
    "z state",
    "z backlash steps",
    "z dro location",
    "z pass dro location",
    "z expected location",
    "z error with respect to dro",
    "z wait",
    "z done",
    "z spindle encoder start count",
    "Z spindle encoder done count",
    "z ",
    "z ",
    "z dro at index pulse",
    "z position at index pulse",
    "debug maximum",
    )

# pylathe update events

EV_ZLOC          =  0           # z location
EV_XLOC          =  1           # x location
EV_RPM           =  2           # rpm
EV_READ_ALL      =  3           # all values
EV_ERROR         =  4           # event error
EV_MAX           =  5           # maximum event

evEventsList = ( \
    "EV_ZLOC",
    "EV_XLOC",
    "EV_RPM",
    "EV_READ_ALL",
    "EV_ERROR",
    "EV_MAX",
    )

evEventsText = ( \
    "z location",
    "x location",
    "rpm",
    "all values",
    "event error",
    "maximum event",
    )

# turning sync selector

SEL_TU_SPEED     =  0           # Motor Speed
SEL_TU_STEP      =  1           # Stepper
SEL_TU_ENC       =  2           # Encoder
SEL_TU_ISYN      =  3           # Int Syn
SEL_TU_ESYN      =  4           # Ext Syn
SEL_TU_SYN       =  5           # Sync

selTurnList = ( \
    "SEL_TU_SPEED",
    "SEL_TU_STEP",
    "SEL_TU_ENC",
    "SEL_TU_ISYN",
    "SEL_TU_ESYN",
    "SEL_TU_SYN",
    )

selTurnText = ( \
    "Motor Speed",
    "Stepper",
    "Encoder",
    "Int Syn",
    "Ext Syn",
    "Sync",
    )

# threading sync selector

SEL_TH_NO_ENC    =  0           # No Encoder
SEL_TH_STEP      =  1           # Stepper
SEL_TH_ENC       =  2           # Encoder
SEL_TH_ISYN_RENC =  3           # Int Syn, Runout Enc
SEL_TH_ESYN_RENC =  4           # Ext Syn, Runout Enc
SEL_TH_ESYN_RSYN =  5           # Ext Syn, Runout Syn
SEL_TH_SYN       =  6           # Syn, Runout Syn

selThreadList = ( \
    "SEL_TH_NO_ENC",
    "SEL_TH_STEP",
    "SEL_TH_ENC",
    "SEL_TH_ISYN_RENC",
    "SEL_TH_ESYN_RENC",
    "SEL_TH_ESYN_RSYN",
    "SEL_TH_SYN",
    )

selThreadText = ( \
    "No Encoder",
    "Stepper",
    "Encoder",
    "Int Syn, Runout Enc",
    "Ext Syn, Runout Enc",
    "Ext Syn, Runout Syn",
    "Syn, Runout Syn",
    )

# arc config selector

SEL_ARC_END      =  0           # End
SEL_ARC_CORNER   =  1           # Corner
SEL_ARC_SMALL    =  2           # Small Ball
SEL_ARC_LARGE    =  3           # Large Ball
SEL_ARC_SMALL_STEM =  4         # Small Stem
SEL_ARC_LARGE_STEM =  5         # Large Stem

selArcTypeList = ( \
    "SEL_ARC_END",
    "SEL_ARC_CORNER",
    "SEL_ARC_SMALL",
    "SEL_ARC_LARGE",
    "SEL_ARC_SMALL_STEM",
    "SEL_ARC_LARGE_STEM",
    )

selArcTypeText = ( \
    "End",
    "Corner",
    "Small Ball",
    "Large Ball",
    "Small Stem",
    "Large Stem",
    )

# riscv actions

R_NONE           =  0           # 'NO' no operation
R_OP_START       =  1           # 'OS' start
R_OP_DONE        =  2           # 'OD' done
R_SETUP          =  3           # 'SU' setup
R_RESUME         =  4           # 'RE' resume
R_STOP           =  5           # 'SP' stop
R_STOP_X         =  6           # 'SX' stop x
R_STOP_Z         =  7           # 'SZ' stop z
R_DONE           =  8           # 'DN' done
R_SET_LOC_X      =  9           # 'LX' set x loc
R_SET_LOC_Z      = 10           # 'LZ' set z loc
R_PAUSE          = 11           # 'PA' pause
R_START_SPIN     = 12           # 'S+' start spindle
R_STOP_SPIN      = 13           # 'S-' stop spindle
R_PASS           = 14           # 'PS' pass
R_SET_ACCEL      = 15           # 'SA' set accel parm
R_SET_ACCEL_Q    = 16           # 'SQ' set accel parm queued
R_SET_DATA       = 17           # 'SD' set data
R_GET_DATA       = 18           # 'GD' set data
R_SAVE_Z         = 19           # 'VZ' save z
R_SAVE_X         = 20           # 'VX' save x
R_STEPS_Z        = 21           # 'IZ' save z steps inch
R_STEPS_X        = 22           # 'IX' save x steps inch
R_HOFS_Z         = 23           # 'HZ' home offset z
R_HOFS_X         = 24           # 'HX' home offset x
R_MOVE_Z         = 25           # 'MZ' move z
R_MOVE_X         = 26           # 'MX' move x
R_MOVE_REL_Z     = 27           # 'RZ' move z
R_MOVE_REL_X     = 28           # 'RX' move x
R_READ_ALL       = 29           # 'RA' read all status
R_READ_DBG       = 30           # 'RD' read all status
R_MAX_CMD        = 31           # 'MX' max value

riscvCmdList = ( \
    "R_NONE",
    "R_OP_START",
    "R_OP_DONE",
    "R_SETUP",
    "R_RESUME",
    "R_STOP",
    "R_STOP_X",
    "R_STOP_Z",
    "R_DONE",
    "R_SET_LOC_X",
    "R_SET_LOC_Z",
    "R_PAUSE",
    "R_START_SPIN",
    "R_STOP_SPIN",
    "R_PASS",
    "R_SET_ACCEL",
    "R_SET_ACCEL_Q",
    "R_SET_DATA",
    "R_GET_DATA",
    "R_SAVE_Z",
    "R_SAVE_X",
    "R_STEPS_Z",
    "R_STEPS_X",
    "R_HOFS_Z",
    "R_HOFS_X",
    "R_MOVE_Z",
    "R_MOVE_X",
    "R_MOVE_REL_Z",
    "R_MOVE_REL_X",
    "R_READ_ALL",
    "R_READ_DBG",
    "R_MAX_CMD",
    )

riscvCmdText = ( \
    "'NO' no operation",
    "'OS' start",
    "'OD' done",
    "'SU' setup",
    "'RE' resume",
    "'SP' stop",
    "'SX' stop x",
    "'SZ' stop z",
    "'DN' done",
    "'LX' set x loc",
    "'LZ' set z loc",
    "'PA' pause",
    "'S+' start spindle",
    "'S-' stop spindle",
    "'PS' pass",
    "'SA' set accel parm",
    "'SQ' set accel parm queued",
    "'SD' set data",
    "'GD' set data",
    "'VZ' save z",
    "'VX' save x",
    "'IZ' save z steps inch",
    "'IX' save x steps inch",
    "'HZ' home offset z",
    "'HX' home offset x",
    "'MZ' move z",
    "'MX' move x",
    "'RZ' move z",
    "'RX' move x",
    "'RA' read all status",
    "'RD' read all status",
    "'MX' max value",
    )

# riscv axis name

RA_NONE          =  0           # 
RA_Z_AXIS        =  1           # 
RA_X_AXIS        =  2           # 

RiscvAxisNameTypeList = ( \
    "RA_NONE",
    "RA_Z_AXIS",
    "RA_X_AXIS",
    )

RiscvAxisNameTypeText = ( \
    "",
    "",
    "",
    )

# riscv data

RD_NONE          =  0           # 
RD_Z_BACKLASH    =  1           # 
RD_X_BACKLASH    =  2           # 

RiscvDataTypeList = ( \
    "RD_NONE",
    "RD_Z_BACKLASH",
    "RD_X_BACKLASH",
    )

RiscvDataTypeText = ( \
    "",
    "",
    "",
    )

# riscv accel types

RP_Z_TURN        =  0           # 'ZT'
RP_Z_TAPER       =  1           # 'ZP'
RP_Z_MOVE        =  2           # 'ZM'
RP_Z_JOG         =  3           # 'ZJ'
RP_Z_SLOW        =  4           # 'ZS'
RP_X_TURN        =  5           # 'XT'
RP_X_TAPER       =  6           # 'XP'
RP_X_MOVE        =  7           # 'XM'
RP_X_JOG         =  8           # 'XJ'
RP_X_SLOW        =  9           # 'XS'
RP_MAX           = 10           # 

accelTypeList = ( \
    "RP_Z_TURN",
    "RP_Z_TAPER",
    "RP_Z_MOVE",
    "RP_Z_JOG",
    "RP_Z_SLOW",
    "RP_X_TURN",
    "RP_X_TAPER",
    "RP_X_MOVE",
    "RP_X_JOG",
    "RP_X_SLOW",
    "RP_MAX",
    )

accelTypeText = ( \
    "'ZT'",
    "'ZP'",
    "'ZM'",
    "'ZJ'",
    "'ZS'",
    "'XT'",
    "'XP'",
    "'XM'",
    "'XJ'",
    "'XS'",
    "",
    )

# riscv accel axis base index

RP_Z_BASE        =  0           # 
RP_X_BASE        =  5           # 

accelBaseList = ( \
    "RP_Z_BASE",
    "RP_X_BASE",
    )

accelBaseText = ( \
    "",
    "",
    )

# riscv axis states

RS_IDLE          =  0           # 
RS_WAIT_BACKLASH =  1           # 
RS_WAIT          =  2           # 
RS_WAIT_TAPER    =  3           # 

RiscvAxisStateTypeList = ( \
    "RS_IDLE",
    "RS_WAIT_BACKLASH",
    "RS_WAIT",
    "RS_WAIT_TAPER",
    )

RiscvAxisStateTypeText = ( \
    "",
    "",
    "",
    "",
    )

# riscv accel parameters

RP_INITIAL_SUM   =  0           # 
RP_INCR1         =  1           # 
RP_INCR2         =  2           # 
RP_ACCEL_VAL     =  3           # 
RP_ACCEL_COUNT   =  4           # 
RP_FREQ_DIV      =  5           # 

RiscvSyncParmTypeList = ( \
    "RP_INITIAL_SUM",
    "RP_INCR1",
    "RP_INCR2",
    "RP_ACCEL_VAL",
    "RP_ACCEL_COUNT",
    "RP_FREQ_DIV",
    )

RiscvSyncParmTypeText = ( \
    "",
    "",
    "",
    "",
    "",
    "",
    )

# riscv run wait states

RW_NONE          =  0           # 'NO' none
RW_PAUSE         =  1           # 'PS' wait pause
RW_SPIN_START    =  2           # 'S+' wait spindle start
RW_SPIN_STOP     =  3           # 'S-' wait spindle stop
RW_WAIT_X        =  4           # 'WX' wait x done
RW_WAIT_Z        =  5           # 'WZ' wait z done

riscvRunWaitList = ( \
    "RW_NONE",
    "RW_PAUSE",
    "RW_SPIN_START",
    "RW_SPIN_STOP",
    "RW_WAIT_X",
    "RW_WAIT_Z",
    )

riscvRunWaitText = ( \
    "'NO' none",
    "'PS' wait pause",
    "'S+' wait spindle start",
    "'S-' wait spindle stop",
    "'WX' wait x done",
    "'WZ' wait z done",
    )
