
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

# move control states

M_IDLE           =  0           # idle state
M_WAIT_Z         =  1           # wait for z to complete
M_WAIT_X         =  2           # wait for x to complete
M_WAIT_SPINDLE   =  3           # wait for spindle start
M_START_SYNC     =  4           # start sync
M_WAIT_SYNC_READY =  5          # wait for sync
M_WAIT_SYNC_DONE =  6           # wait for sync done
M_WAIT_MEASURE_DONE =  7        # wait for measurment done
M_WAIT_PROBE     =  8           # wait for probe to complete
M_WAIT_MEASURE   =  9           # wait for measurement to complete
M_WAIT_SAFE_X    = 10           # wait for move to safe x to complete
M_WAIT_SAFE_Z    = 11           # wait for move to safe z to complete
M_WAIT_ARC       = 12           # wait for arc move to complete

mStatesList = ( \
    "M_IDLE",
    "M_WAIT_Z",
    "M_WAIT_X",
    "M_WAIT_SPINDLE",
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

# move control commands

MOVE_Z           =  0           # move z
MOVE_X           =  1           # move x
SAVE_Z           =  2           # save z
SAVE_X           =  3           # save x
SAVE_Z_OFFSET    =  4           # save z offset
SAVE_X_OFFSET    =  5           # save x offset
SAVE_TAPER       =  6           # save taper
MOVE_ZX          =  7           # move x in sync with z
MOVE_XZ          =  8           # move z in sync with x
TAPER_ZX         =  9           # taper x
TAPER_XZ         = 10           # taper z
START_SPINDLE    = 11           # spindle start
STOP_SPINDLE     = 12           # spindle stop
Z_SYN_SETUP      = 13           # z sync setup
X_SYN_SETUP      = 14           # x sync setup
PASS_NUM         = 15           # set pass number
QUE_PAUSE        = 16           # pause queue
MOVE_Z_OFFSET    = 17           # move z offset
SAVE_FEED_TYPE   = 18           # save feed type
Z_FEED_SETUP     = 19           # setup z feed
X_FEED_SETUP     = 20           # setup x feed
SAVE_FLAGS       = 21           # save thread flags
PROBE_Z          = 22           # probe in z direction
PROBE_X          = 23           # probe in x direction
SAVE_Z_DRO       = 24           # save z dro reading
SAVE_X_DRO       = 25           # save x dro reading
QUE_PARM         = 26           # save parameter in queue
MOVE_ARC         = 27           # move in an arc
OP_DONE          = 28           # operation done

mCommandsList = ( \
    "MOVE_Z",
    "MOVE_X",
    "SAVE_Z",
    "SAVE_X",
    "SAVE_Z_OFFSET",
    "SAVE_X_OFFSET",
    "SAVE_TAPER",
    "MOVE_ZX",
    "MOVE_XZ",
    "TAPER_ZX",
    "TAPER_XZ",
    "START_SPINDLE",
    "STOP_SPINDLE",
    "Z_SYN_SETUP",
    "X_SYN_SETUP",
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
D_ZIDX           = 35           # z dro at index pulse 
D_HST            = 36           # home state
D_MSTA           = 37           # move state
D_MCMD           = 38           # move command

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
    "D_ZIDX",
    "D_HST",
    "D_MSTA",
    "D_MCMD",
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
SEL_TH_ENC       =  2           # Encoder Direct
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
    "Encoder Direct",
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
