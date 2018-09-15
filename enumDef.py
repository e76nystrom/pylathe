
# enums

# z control states

ZIDLE            =  0           # idle
ZWAITBKLS        =  1           # wait for backlash move complete
ZSTARTMOVE       =  2           # start z move
ZWAITMOVE        =  3           # wait for move complete
ZDONE            =  4           # clean up state

zStatesList = ( \
    "ZIDLE",
    "ZWAITBKLS",
    "ZSTARTMOVE",
    "ZWAITMOVE",
    "ZDONE",
    )

# x control states

XIDLE            =  0           # idle
XWAITBKLS        =  1           # wait for backlash move complete
XSTARTMOVE       =  2           # start x move
XWAITMOVE        =  3           # wait for move complete
XDONE            =  4           # clean up state

xStatesList = ( \
    "XIDLE",
    "XWAITBKLS",
    "XSTARTMOVE",
    "XWAITMOVE",
    "XDONE",
    )

# move control states

M_IDLE           =  0           # idle state
M_WAIT_Z         =  1           # wait for z to complete
M_WAIT_X         =  2           # wait for x to complete
M_WAIT_SPINDLE   =  3           # wait for spindle start
M_WAIT_SYNC_READY =  4          # wait for sync
M_WAIT_SYNC_DONE =  5           # wait for sync done
M_WAIT_PROBE     =  6           # wait for probe to complete
M_WAIT_MEASURE   =  7           # wait for measurement to complete
M_WAIT_SAFE_X    =  8           # wait for move to safe x to complete
M_WAIT_SAFE_Z    =  9           # wait for move to safe z to complete

mStatesList = ( \
    "M_IDLE",
    "M_WAIT_Z",
    "M_WAIT_X",
    "M_WAIT_SPINDLE",
    "M_WAIT_SYNC_READY",
    "M_WAIT_SYNC_DONE",
    "M_WAIT_PROBE",
    "M_WAIT_MEASURE",
    "M_WAIT_SAFE_X",
    "M_WAIT_SAFE_Z",
    )

# move control commands

MOVE_Z           =  0           # move z
MOVE_X           =  1           # move x
SAVE_Z           =  2           # save z
SAVE_X           =  3           # save x
SAVE_Z_OFFSET    =  4           # save z offset
SAVE_X_OFFSET    =  5           # save z offset
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
SAVE_DIAMETER    = 17           # save turn diameter
SAVE_FEED_TYPE   = 18           # save feed type
Z_FEED_SETUP     = 19           # setup z feed
X_FEED_SETUP     = 20           # setup x feed
SAVE_RUNOUT      = 21           # save thread runout
SAVE_DEPTH       = 22           # save thread depth
SAVE_FLAGS       = 23           # save thread flags
PROBE_Z          = 24           # probe in z direction
PROBE_X          = 25           # probe in x direction
SAVE_Z_DRO       = 26           # save z dro reading
SAVE_X_DRO       = 27           # save x dro reading
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
    "SAVE_DIAMETER",
    "SAVE_FEED_TYPE",
    "Z_FEED_SETUP",
    "X_FEED_SETUP",
    "SAVE_RUNOUT",
    "SAVE_DEPTH",
    "SAVE_FLAGS",
    "PROBE_Z",
    "PROBE_X",
    "SAVE_Z_DRO",
    "SAVE_X_DRO",
    "OP_DONE",
    )

# home control states

H_IDLE           =  0           # idle state
H_CHECK_ONHOME   =  1           # 
H_WAIT_FINDHOME  =  2           # 
H_BACKOFF_HOME   =  3           # 
H_WAIT_BACKOFF   =  4           # 
H_WAIT_SLOWFIND  =  5           # 

hStatesList = ( \
    "H_IDLE",
    "H_CHECK_ONHOME",
    "H_WAIT_FINDHOME",
    "H_BACKOFF_HOME",
    "H_WAIT_BACKOFF",
    "H_WAIT_SLOWFIND",
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
D_XWT            = 12           # x wait
D_XDN            = 13           # x done
D_XEST           = 14           # x spindle encoder start count
D_XEDN           = 15           # x spindle encoder done count
D_ZMOV           = 16           # z move location
D_ZLOC           = 17           # z location
D_ZDST           = 18           # z distance
D_ZSTP           = 19           # z steps
D_ZST            = 20           # z state
D_ZBSTP          = 21           # z backlash steps
D_ZDRO           = 22           # z dro location
D_ZPDRO          = 23           # z pass dro location
D_ZEXP           = 24           # z expected location
D_ZWT            = 25           # z wait
D_ZDN            = 26           # z done
D_ZEST           = 27           # z spindle encoder start count
D_ZEDN           = 28           # Z spindle encoder done count
D_ZX             = 29           # z 
D_ZY             = 30           # z 
D_HST            = 31           # home state
D_MSTA           = 32           # move state
D_MCMD           = 33           # move command

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
    "D_XWT",
    "D_XDN",
    "D_XEST",
    "D_XEDN",
    "D_ZMOV",
    "D_ZLOC",
    "D_ZDST",
    "D_ZSTP",
    "D_ZST",
    "D_ZBSTP",
    "D_ZDRO",
    "D_ZPDRO",
    "D_ZEXP",
    "D_ZWT",
    "D_ZDN",
    "D_ZEST",
    "D_ZEDN",
    "D_ZX",
    "D_ZY",
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
