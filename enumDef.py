
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
Q_SAVE_FEED      = 20           # save current feed
Q_SAVE_FEED_TYPE = 21           # save feed type
Q_Z_FEED_SETUP   = 22           # setup z feed
Q_X_FEED_SETUP   = 23           # setup x feed
Q_SAVE_FLAGS     = 24           # save thread flags
Q_PROBE_Z        = 25           # probe in z direction
Q_PROBE_X        = 26           # probe in x direction
Q_SAVE_Z_DRO     = 27           # save z dro reading
Q_SAVE_X_DRO     = 28           # save x dro reading
Q_QUE_PARM       = 29           # save parameter in queue
Q_MOVE_ARC       = 30           # move in an arc
Q_OP_DONE        = 31           # operation done

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
    "Q_SAVE_FEED",
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
    "save current feed",
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

H_IDLE           =  0           # 'HI' idle state
H_HOME           =  1           # 'HF' found home switch
H_OFF_HOME       =  2           # 'OF' off home switch
H_BACKOFF        =  3           # 'BF' backoff dist from switch
H_SLOW           =  4           # 'HS' found home slowly

hStatesList = ( \
    "H_IDLE",
    "H_HOME",
    "H_OFF_HOME",
    "H_BACKOFF",
    "H_SLOW",
    )

hStatesText = ( \
    " idle state",
    " found home switch",
    " off home switch",
    " backoff dist from switch",
    " found home slowly",
    )

# debug axis message types

D_BASE           =  0           # axis base
D_MVCM           =  1           # move command
D_ACTL           =  2           # axisctl
D_MOV            =  3           # move location
D_CUR            =  4           # current location
D_LOC            =  5           # end location
D_DST            =  6           # distance
D_STP            =  7           # steps
D_ST             =  8           # state
D_BSTP           =  9           # backlash steps
D_DRO            = 10           # dro location
D_PDRO           = 11           # pass dro location
D_EXP            = 12           # expected location
D_ERR            = 13           # error with respect to dro
D_WT             = 14           # wait
D_DN             = 15           # done
D_EST            = 16           # spindle encoder start count
D_EDN            = 17           # spindle encoder done count
D_X              = 18           # 
D_Y              = 19           # 
D_IDXD           = 20           # dro at index pulse
D_IDXP           = 21           # position at index pulse
D_AMAX           = 22           # axis maximum

DAxisMessageList = ( \
    "D_BASE",
    "D_MVCM",
    "D_ACTL",
    "D_MOV",
    "D_CUR",
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
    "move command",
    "axisctl",
    "move location",
    "current location",
    "end location",
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

D_PASS           =  0           # 'PASS' pass done
D_DONE           =  1           # 'DONE' all operations done
D_TEST           =  2           # 'TEST' test message
D_HST            =  3           # 'HSTA' home state
D_MSTA           =  4           # 'MSTA' move state
D_MCMD           =  5           # 'MCMD' move command
D_XBASE          =  6           # 'XBAS' x base
D_XMVCM          =  7           # 'XMVC' x move command
D_XACTL          =  8           # 'XCTL' x axis ctl
D_XMOV           =  9           # 'XMOV' x move to location
D_XCUR           = 10           # 'XCUR' x current location
D_XLOC           = 11           # 'XLOC' x end location
D_XDST           = 12           # 'XDST' x distance
D_XSTP           = 13           # 'XSTP' x steps
D_XST            = 14           # 'XSTA' x state
D_XBSTP          = 15           # 'XBLS' x backlash steps
D_XDRO           = 16           # 'XDRO' x dro location
D_XPDRO          = 17           # 'XPDR' x pass dro location
D_XEXP           = 18           # 'XEXP' x expected location
D_XERR           = 19           # 'XERR' x error with respect to dro
D_XWT            = 20           # 'XWAT' x wait
D_XDN            = 21           # 'XDNE' x done
D_XEST           = 22           # 'XEST' x spindle encoder start count
D_XEDN           = 23           # 'XEDN' x spindle encoder done count
D_XX             = 24           # 'XICT' x input count
D_XY             = 25           # 'XOCT' x output count
D_XIDXD          = 26           # 'XIDR' x dro at index pulse
D_XIDXP          = 27           # 'XIPO' x position at index pulse
D_ZBASE          = 28           # 'ZBAS' Z base
D_ZMVCM          = 29           # 'ZMVC' z move command
D_ZACTL          = 30           # 'ZCTL' z axis ctl
D_ZMOV           = 31           # 'ZMOV' z move location
D_ZCUR           = 32           # 'ZCUR' x current location
D_ZLOC           = 33           # 'ZLOC' z end location
D_ZDST           = 34           # 'ZDST' z distance
D_ZSTP           = 35           # 'ZSTP' z steps
D_ZST            = 36           # 'ZSTA' z state
D_ZBSTP          = 37           # 'ZBLS' z backlash steps
D_ZDRO           = 38           # 'ZDRO' z dro location
D_ZPDRO          = 39           # 'ZPDR' z pass dro location
D_ZEXP           = 40           # 'ZEXP' z expected location
D_ZERR           = 41           # 'ZERR' z error with respect to dro
D_ZWT            = 42           # 'ZWAT' z wait
D_ZDN            = 43           # 'ZDNE' z done
D_ZEST           = 44           # 'ZEST' z spindle encoder start count
D_ZEDN           = 45           # 'ZEDN' Z spindle encoder done count
D_ZX             = 46           # 'ZICT' z input count
D_ZY             = 47           # 'ZOCT' z output count
D_ZIDXD          = 48           # 'ZIDR' z dro at index pulse
D_ZIDXP          = 49           # 'ZIPO' z position at index pulse
D_MAX            = 50           # 'MAX ' debug maximum

dMessageList = ( \
    "D_PASS",
    "D_DONE",
    "D_TEST",
    "D_HST",
    "D_MSTA",
    "D_MCMD",
    "D_XBASE",
    "D_XMVCM",
    "D_XACTL",
    "D_XMOV",
    "D_XCUR",
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
    "D_ZMVCM",
    "D_ZACTL",
    "D_ZMOV",
    "D_ZCUR",
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
    " pass done",
    " all operations done",
    " test message",
    " home state",
    " move state",
    " move command",
    " x base",
    " x move command",
    " x axis ctl",
    " x move to location",
    " x current location",
    " x end location",
    " x distance",
    " x steps",
    " x state",
    " x backlash steps",
    " x dro location",
    " x pass dro location",
    " x expected location",
    " x error with respect to dro",
    " x wait",
    " x done",
    " x spindle encoder start count",
    " x spindle encoder done count",
    " x input count",
    " x output count",
    " x dro at index pulse",
    " x position at index pulse",
    " Z base",
    " z move command",
    " z axis ctl",
    " z move location",
    " x current location",
    " z end location",
    " z distance",
    " z steps",
    " z state",
    " z backlash steps",
    " z dro location",
    " z pass dro location",
    " z expected location",
    " z error with respect to dro",
    " z wait",
    " z done",
    " z spindle encoder start count",
    " Z spindle encoder done count",
    " z input count",
    " z output count",
    " z dro at index pulse",
    " z position at index pulse",
    "'MAX ' debug maximum",
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

SEL_TU_SPEED     =  0           # 'MS' Motor Speed
SEL_TU_STEP      =  1           # 'ST' Stepper
SEL_TU_ENC       =  2           # 'EN' Encoder
SEL_TU_SYN       =  3           # 'SY' Sync
SEL_TU_ISYN      =  4           # 'IS' Int Syn
SEL_TU_ESYN      =  5           # 'ES' Ext Syn

selTurnList = ( \
    "SEL_TU_SPEED",
    "SEL_TU_STEP",
    "SEL_TU_ENC",
    "SEL_TU_SYN",
    "SEL_TU_ISYN",
    "SEL_TU_ESYN",
    )

selTurnText = ( \
    " Motor Speed",
    " Stepper",
    " Encoder",
    " Sync",
    " Int Syn",
    " Ext Syn",
    )

# threading sync selector

SEL_TH_NO_ENC    =  0           # 'NO' No Encoder
SEL_TH_STEP      =  1           # 'ST' Stepper
SEL_TH_ENC       =  2           # 'EN' Encoder
SEL_TH_SYN       =  3           # 'SY' Syn
SEL_TH_ISYN      =  4           # 'IS' Syn
SEL_TH_ESYN      =  5           # 'ES' Syn

selThreadList = ( \
    "SEL_TH_NO_ENC",
    "SEL_TH_STEP",
    "SEL_TH_ENC",
    "SEL_TH_SYN",
    "SEL_TH_ISYN",
    "SEL_TH_ESYN",
    )

selThreadText = ( \
    " No Encoder",
    " Stepper",
    " Encoder",
    " Syn",
    " Syn",
    " Syn",
    )

# runout sync selector

SEL_RU_NO_ENC    =  0           # 'NO' No Encoder
SEL_RU_STEP      =  1           # 'ST' Stepper
SEL_RU_ENC       =  2           # 'EN' Encoder
SEL_RU_SYN       =  3           # 'SY' Syn
SEL_RU_ISYN      =  4           # 'IS' Int Syn
SEL_RU_ESYN      =  5           # 'ES' Ext Syn

selRunoutList = ( \
    "SEL_RU_NO_ENC",
    "SEL_RU_STEP",
    "SEL_RU_ENC",
    "SEL_RU_SYN",
    "SEL_RU_ISYN",
    "SEL_RU_ESYN",
    )

selRunoutText = ( \
    " No Encoder",
    " Stepper",
    " Encoder",
    " Syn",
    " Int Syn",
    " Ext Syn",
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

# mpg control states

MPG_DISABLED     =  0           # 'DS' disabled
MPG_CHECK_QUE    =  1           # 'CQ' check queue
MPG_DIR_CHANGE_WAIT =  2        # 'DC' wait for direction change
MPG_WAIT_BACKLASH =  3          # 'WB' wait for backlash

mpgStateList = ( \
    "MPG_DISABLED",
    "MPG_CHECK_QUE",
    "MPG_DIR_CHANGE_WAIT",
    "MPG_WAIT_BACKLASH",
    )

mpgStateText = ( \
    " disabled",
    " check queue",
    " wait for direction change",
    " wait for backlash",
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

# accel types

A_TURN           =  0           # 'TU'
A_TAPER          =  1           # 'TP'
A_MOVE           =  2           # 'MV'
A_JOG            =  3           # 'JG'
A_SLOW           =  4           # 'JS'

accelTypeList = ( \
    "A_TURN",
    "A_TAPER",
    "A_MOVE",
    "A_JOG",
    "A_SLOW",
    )

accelTypeText = ( \
    "",
    "",
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
RP_SP_RUN        = 10           # 'SR'
RP_SP_JOG        = 11           # 'SJ'
RP_MAX           = 12           # 

axisAccelTypeList = ( \
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
    "RP_SP_RUN",
    "RP_SP_JOG",
    "RP_MAX",
    )

axisAccelTypeText = ( \
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
    "",
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

RS_IDLE          =  0           # 'ID' idle
RS_WAIT_BACKLASH =  1           # 'WB' wait backlash
RS_WAIT          =  2           # 'WD' wait done
RS_WAIT_TAPER    =  3           # 'WT' wait taper
RS_WAIT_RUNOUT   =  4           # 'WR' wait runout

riscvAxisStateList = ( \
    "RS_IDLE",
    "RS_WAIT_BACKLASH",
    "RS_WAIT",
    "RS_WAIT_TAPER",
    "RS_WAIT_RUNOUT",
    )

riscvAxisStateText = ( \
    " idle",
    " wait backlash",
    " wait done",
    " wait taper",
    " wait runout",
    )

# riscv accel parameters

RP_INITIAL_SUM   =  0           # 
RP_INCR1         =  1           # 
RP_INCR2         =  2           # 
RP_ACCEL_VAL     =  3           # 
RP_ACCEL_COUNT   =  4           # 
RP_ACCEL_MAX     =  5           # 
RP_FREQ_DIV      =  6           # 

RiscvSyncParmTypeList = ( \
    "RP_INITIAL_SUM",
    "RP_INCR1",
    "RP_INCR2",
    "RP_ACCEL_VAL",
    "RP_ACCEL_COUNT",
    "RP_ACCEL_MAX",
    "RP_FREQ_DIV",
    )

RiscvSyncParmTypeText = ( \
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    )

# riscv run wait states

RW_NONE          =  0           # 'NO' none
RW_PAUSE         =  1           # 'WP' wait pause
RW_SPIN_START    =  2           # 'W+' wait spindle start
RW_SPIN_STOP     =  3           # 'W-' wait spindle stop
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
    " none",
    " wait pause",
    " wait spindle start",
    " wait spindle stop",
    " wait x done",
    " wait z done",
    )

# move commands in ctlbits

CMD_NONE         =  0           # 'NO' no command
CMD_MOV          =  1           # 'MV' move a set distance
CMD_JOG          =  2           # 'JG' move while cmd are present
CMD_SYN          =  3           # 'SY' move dist synchronized to rotation
CMD_MAX          =  4           # 'MX' rapid move
CMD_SPEED        =  5           # 'CS' jog at speed
JOG_SLOW         =  6           # 'JS' slow jog for home or probe

moveCmdList = ( \
    "CMD_NONE",
    "CMD_MOV",
    "CMD_JOG",
    "CMD_SYN",
    "CMD_MAX",
    "CMD_SPEED",
    "JOG_SLOW",
    )

moveCmdText = ( \
    " no command",
    " move a set distance",
    " move while cmd are present",
    " move dist synchronized to rotation",
    " rapid move",
    " jog at speed",
    " slow jog for home or probe",
    )

# sync commands in ctlbits

M_SYN_NONE       =  0           # 'SN' sync with encoder
M_SYN_ENC        =  1           # 'SE' sync with encoder
M_SYN_SYNC       =  2           # 'SS' sync with encoder scaler
M_SYN_ENC_RSYNC  =  3           # 'ES' sync encoder runout encoder scaler
M_SYN_ENC_RENC   =  4           # 'EE' sync encoder runout encoder

syncCmdsList = ( \
    "M_SYN_NONE",
    "M_SYN_ENC",
    "M_SYN_SYNC",
    "M_SYN_ENC_RSYNC",
    "M_SYN_ENC_RENC",
    )

syncCmdsText = ( \
    " sync with encoder",
    " sync with encoder",
    " sync with encoder scaler",
    " sync encoder runout encoder scaler",
    " sync encoder runout encoder",
    )

# riscv run wait states

M_RSV_0          =  0           # 'R0' no command
M_RSV_1          =  1           # 'R1' no command
M_RSV_2          =  2           # 'R2' no command
M_SYN_START      =  3           # 'SS' start on sync pulse
M_SYN_LEFT       =  4           # 'SL' start sync left
M_SYN_TAPER      =  5           # 'ST' taper on other axis
M_DIST_MODE      =  6           # 'DM' distance update mode
M_FIND_HOME      =  7           # 'FH' find home
M_CLEAR_HOME     =  8           # 'CH' move off of home
M_FIND_PROBE     =  9           # 'FP' find probe
M_CLEAR_PROBE    = 10           # 'CP' move off of probe
M_DRO_POS        = 11           # 'DP' use dro for moving
M_DRO_UPD        = 12           # 'DU' update internal position from dro
M_ENA_THREAD     = 13           # 'TH' thread enabled
M_ENA_RUNOUT     = 14           # 'RO' runout enabled
M_INTERNAL_OP    = 15           # 'IN' internal operation
M_BIT_MAX        = 16           # 'MX' number of bits

moveBitList = ( \
    "M_RSV_0",
    "M_RSV_1",
    "M_RSV_2",
    "M_SYN_START",
    "M_SYN_LEFT",
    "M_SYN_TAPER",
    "M_DIST_MODE",
    "M_FIND_HOME",
    "M_CLEAR_HOME",
    "M_FIND_PROBE",
    "M_CLEAR_PROBE",
    "M_DRO_POS",
    "M_DRO_UPD",
    "M_ENA_THREAD",
    "M_ENA_RUNOUT",
    "M_INTERNAL_OP",
    "M_BIT_MAX",
    )

moveBitText = ( \
    " no command",
    " no command",
    " no command",
    " start on sync pulse",
    " start sync left",
    " taper on other axis",
    " distance update mode",
    " find home",
    " move off of home",
    " find probe",
    " move off of probe",
    " use dro for moving",
    " update internal position from dro",
    " thread enabled",
    " runout enabled",
    " internal operation",
    " number of bits",
    )

# movement status

R_MV_PAUSE       =  0           # 'PA' movement paused
R_MV_READ_X      =  1           # 'RX' pause x may change
R_MV_READ_Z      =  2           # 'RZ' pause z may change
R_MV_ACTIVE      =  3           # 'AC' movement active
R_MV_DONE        =  4           # 'DN' movement active
R_MV_X_LIMIT     =  5           # 'XL' at limit switch
R_MV_Z_LIMIT     =  6           # 'ZL' at limit switch
R_MV_X_HOME_ACTIVE =  7         # 'XA' x home active
R_MV_X_HOME      =  8           # 'XH' x home success
R_MV_Z_HOME_ACTIVE =  9         # 'ZA' z home active
R_MV_Z_HOME      = 10           # 'ZH' z home success
R_MV_MEASURE     = 11           # 'MS' pause for measurement
R_MV_ESTOP       = 12           # 'ES' estop
R_MV_MAX         = 13           # number of bits

mvStatusBitsList = ( \
    "R_MV_PAUSE",
    "R_MV_READ_X",
    "R_MV_READ_Z",
    "R_MV_ACTIVE",
    "R_MV_DONE",
    "R_MV_X_LIMIT",
    "R_MV_Z_LIMIT",
    "R_MV_X_HOME_ACTIVE",
    "R_MV_X_HOME",
    "R_MV_Z_HOME_ACTIVE",
    "R_MV_Z_HOME",
    "R_MV_MEASURE",
    "R_MV_ESTOP",
    "R_MV_MAX",
    )

mvStatusBitsText = ( \
    " movement paused",
    " pause x may change",
    " pause z may change",
    " movement active",
    " movement active",
    " at limit switch",
    " at limit switch",
    " x home active",
    " x home success",
    " z home active",
    " z home success",
    " pause for measurement",
    " estop",
    "number of bits",
    )

# pause flags

R_DISABLE_JOG    =  0           # 'DJ' jogging disabled
R_PAUSE_ENA_Z_JOG =  1          # 'EZ' enable z job during pause
R_PAUSE_ENA_X_JOG =  2          # 'EX' enable x jog during pause
R_PAUSE_READ_Z   =  3           # 'RX' read z after pause
R_PAUSE_READ_X   =  4           # 'RZ' read x after pause
R_PAUSE_MAX      =  5           # number of bits

pauseBitsList = ( \
    "R_DISABLE_JOG",
    "R_PAUSE_ENA_Z_JOG",
    "R_PAUSE_ENA_X_JOG",
    "R_PAUSE_READ_Z",
    "R_PAUSE_READ_X",
    "R_PAUSE_MAX",
    )

pauseBitsText = ( \
    " jogging disabled",
    " enable z job during pause",
    " enable x jog during pause",
    " read z after pause",
    " read x after pause",
    "number of bits",
    )

# fpga clock values

E_CLK_NONE       =  0           # 'NO' 
E_CLK_FREQ       =  1           # 'FR' 
E_CLK_CH         =  2           # 'CH' 
E_CLK_INT_CLK    =  3           # 'IC' 
E_CLK_SLV_FREQ   =  4           # 'SF' 
E_CLK_SLV_CH     =  5           # 'SC' 
E_CLK_SPINDLE    =  6           # 'SP' 
E_CLK_DBG_FREQ   =  7           # 'DF' 

fpgaClkSelList = ( \
    "E_CLK_NONE",
    "E_CLK_FREQ",
    "E_CLK_CH",
    "E_CLK_INT_CLK",
    "E_CLK_SLV_FREQ",
    "E_CLK_SLV_CH",
    "E_CLK_SPINDLE",
    "E_CLK_DBG_FREQ",
    )

fpgaClkSelText = ( \
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    )
