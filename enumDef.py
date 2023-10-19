
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

MOVE_Z           =  0           # move z
MOVE_X           =  1           # move x
SAVE_Z           =  2           # save z
SAVE_X           =  3           # save x
SAVE_Z_OFFSET    =  4           # save z offset
SAVE_X_OFFSET    =  5           # save x offset
SAVE_TAPER       =  6           # save taper
MOVE_Z_X         =  7           # move x in sync with z
MOVE_X_Z         =  8           # move z in sync with x
TAPER_Z_X        =  9           # taper x
TAPER_X_Z        = 10           # taper z
START_SPINDLE    = 11           # spindle start
STOP_SPINDLE     = 12           # spindle stop
Z_SYN_SETUP      = 13           # z sync setup
X_SYN_SETUP      = 14           # x sync setup
SEND_SYNC_PARMS  = 15           # send sync parameters
SYNC_COMMAND     = 16           # send sync command
PASS_NUM         = 17           # set pass number
QUE_PAUSE        = 18           # pause queue
MOVE_Z_OFFSET    = 19           # move z offset
SAVE_FEED_TYPE   = 20           # save feed type
Z_FEED_SETUP     = 21           # setup z feed
X_FEED_SETUP     = 22           # setup x feed
SAVE_FLAGS       = 23           # save thread flags
PROBE_Z          = 24           # probe in z direction
PROBE_X          = 25           # probe in x direction
SAVE_Z_DRO       = 26           # save z dro reading
SAVE_X_DRO       = 27           # save x dro reading
QUE_PARM         = 28           # save parameter in queue
MOVE_ARC         = 29           # move in an arc
OP_DONE          = 30           # operation done

mCommandsList = ( \
    "MOVE_Z",
    "MOVE_X",
    "SAVE_Z",
    "SAVE_X",
    "SAVE_Z_OFFSET",
    "SAVE_X_OFFSET",
    "SAVE_TAPER",
    "MOVE_Z_X",
    "MOVE_X_Z",
    "TAPER_Z_X",
    "TAPER_X_Z",
    "START_SPINDLE",
    "STOP_SPINDLE",
    "Z_SYN_SETUP",
    "X_SYN_SETUP",
    "SEND_SYNC_PARMS",
    "SYNC_COMMAND",
    "PASS_NUM",
    "QUE_PAUSE",
    "MOVE_Z_OFFSET",
    "SAVE_FEED_TYPE",
    "Z_FEED_SETUP",
    "X_FEED_SETUP",
    "SAVE_FLAGS",
    "PROBE_Z",
    "PROBE_X",
    "SAVE_Z_DRO",
    "SAVE_X_DRO",
    "QUE_PARM",
    "MOVE_ARC",
    "OP_DONE",
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

# debug message types

D_PASS           =  0           # pass done
D_DONE           =  1           # all operations done
D_TEST           =  2           # test message
D_XMOV           =  3           # x move location
D_XLOC           =  4           # x location
D_XDST           =  5           # x distance
D_XSTP           =  6           # x steps
D_XST            =  7           # x state
D_XBSTP          =  8           # x backlash steps
D_XDRO           =  9           # x dro location
D_XPDRO          = 10           # x pass dro location
D_XEXP           = 11           # x expected location
D_XERR           = 12           # x error with respect to dro
D_XWT            = 13           # x wait
D_XDN            = 14           # x done
D_XEST           = 15           # x spindle encoder start count
D_XEDN           = 16           # x spindle encoder done count
D_XX             = 17           # x 
D_XY             = 18           # x 
D_ZMOV           = 19           # z move location
D_ZLOC           = 20           # z location
D_ZDST           = 21           # z distance
D_ZSTP           = 22           # z steps
D_ZST            = 23           # z state
D_ZBSTP          = 24           # z backlash steps
D_ZDRO           = 25           # z dro location
D_ZPDRO          = 26           # z pass dro location
D_ZEXP           = 27           # z expected location
D_ZERR           = 28           # z error with respect to dro
D_ZWT            = 29           # z wait
D_ZDN            = 30           # z done
D_ZEST           = 31           # z spindle encoder start count
D_ZEDN           = 32           # Z spindle encoder done count
D_ZX             = 33           # z 
D_ZY             = 34           # z 
D_XIDXD          = 35           # x dro at index pulse
D_XIDXP          = 36           # x position at index pulse
D_ZIDXD          = 37           # z dro at index pulse
D_ZIDXP          = 38           # z position at index pulse
D_HST            = 39           # home state
D_MSTA           = 40           # move state
D_MCMD           = 41           # move command

dMessageList = ( \
    "D_PASS",
    "D_DONE",
    "D_TEST",
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
    "D_XIDXD",
    "D_XIDXP",
    "D_ZIDXD",
    "D_ZIDXP",
    "D_HST",
    "D_MSTA",
    "D_MCMD",
    )

dMessageText = ( \
    "pass done",
    "all operations done",
    "test message",
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
    "x dro at index pulse",
    "x position at index pulse",
    "z dro at index pulse",
    "z position at index pulse",
    "home state",
    "move state",
    "move command",
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

R_NONE           =  0           # no operation
R_OP_START       =  1           # 
R_OP_DONE        =  2           # 
R_STOP           =  3           # stop
R_STOP_X         =  4           # stop x
R_STOP_Z         =  5           # stop z
R_RESUME         =  6           # resume
R_SET_LOC_X      =  7           # 
R_SET_LOC_Z      =  8           # 
R_PAUSE          =  9           # pause
R_START_SPIN     = 10           # start spindle
R_STOP_SPIN      = 11           # stop spindle
R_WAIT_Z         = 12           # wait z
R_WAIT_X         = 13           # wait x
R_PASS           = 14           # 
R_SEND_ACCEL     = 15           # send parm
R_SEND_DATA      = 16           # send data
R_MOVE_Z         = 17           # move z
R_MOVE_X         = 18           # move x
R_MOVE_REL_Z     = 19           # move z
R_MOVE_REL_X     = 20           # move x

selRiscvTypeList = ( \
    "R_NONE",
    "R_OP_START",
    "R_OP_DONE",
    "R_STOP",
    "R_STOP_X",
    "R_STOP_Z",
    "R_RESUME",
    "R_SET_LOC_X",
    "R_SET_LOC_Z",
    "R_PAUSE",
    "R_START_SPIN",
    "R_STOP_SPIN",
    "R_WAIT_Z",
    "R_WAIT_X",
    "R_PASS",
    "R_SEND_ACCEL",
    "R_SEND_DATA",
    "R_MOVE_Z",
    "R_MOVE_X",
    "R_MOVE_REL_Z",
    "R_MOVE_REL_X",
    )

selRiscvTypeText = ( \
    "no operation",
    "",
    "",
    "stop",
    "stop x",
    "stop z",
    "resume",
    "",
    "",
    "pause",
    "start spindle",
    "stop spindle",
    "wait z",
    "wait x",
    "",
    "send parm",
    "send data",
    "move z",
    "move x",
    "move z",
    "move x",
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

RP_Z_TURN        =  0           # 
RP_Z_BASE        =  0           # 
RP_Z_TAPER       =  1           # 
RP_Z_MOVE        =  2           # 
RP_Z_JOG         =  3           # 
RP_Z_SLOW        =  4           # 
RP_X_TURN        =  5           # 
RP_X_BASE        =  5           # 
RP_X_TAPER       =  6           # 
RP_X_MOVE        =  7           # 
RP_X_JOG         =  8           # 
RP_X_SLOW        =  9           # 
RP_MAX           = 10           # 

RiscvAccelTypeList = ( \
    "RP_Z_TURN",
    "RP_Z_BASE",
    "RP_Z_TAPER",
    "RP_Z_MOVE",
    "RP_Z_JOG",
    "RP_Z_SLOW",
    "RP_X_TURN",
    "RP_X_BASE",
    "RP_X_TAPER",
    "RP_X_MOVE",
    "RP_X_JOG",
    "RP_X_SLOW",
    "RP_MAX",
    )

RiscvAccelTypeText = ( \
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    )

# riscv axis states

RS_IDLE          =  0           # 
RS_WAIT_BACKLASH =  1           # 
RS_WAIT          =  2           # 

RiscvAxisStateTypeList = ( \
    "RS_IDLE",
    "RS_WAIT_BACKLASH",
    "RS_WAIT",
    )

RiscvAxisStateTypeText = ( \
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

RW_NONE          =  0           # 
RW_PAUSE         =  1           # 
RW_SPIN_START    =  2           # 
RW_SPIN_STOP     =  3           # 
RW_WAIT_X        =  4           # 
RW_WAIT_Z        =  5           # 

RiscvRunWaitTypeList = ( \
    "RW_NONE",
    "RW_PAUSE",
    "RW_SPIN_START",
    "RW_SPIN_STOP",
    "RW_WAIT_X",
    "RW_WAIT_Z",
    )

RiscvRunWaitTypeText = ( \
    "",
    "",
    "",
    "",
    "",
    "",
    )
