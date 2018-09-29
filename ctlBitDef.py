
# bit definitions

# common move command bits

CMD_MSK          = (7 << 0)     # move mask
CMD_MOV          = (1 << 0)     # move a set distance
CMD_JOG          = (2 << 0)     # move while cmd are present
CMD_SYN          = (3 << 0)     # move dist synchronized to rotation
CMD_MAX          = (4 << 0)     # rapid move
CMD_SPEED        = (5 << 0)     # jog at speed
JOGSLOW          = (6 << 0)     # slow jog for home or probe

# common definitions

DIR_POS          = 1            # positive direction
DIR_NEG          = -1           # negative direction

# z move command bits

Z_SYN_START      = (1 << 4)     # start on sync pulse
Z_SYN_LEFT       = (1 << 5)     # start sync left
X_SYN_TAPER      = (1 << 6)     # taper on x

# z direction

ZPOS             = 1            # z in positive direction
ZNEG             = -1           # z in negative direction

# x move command bits

X_SYN_START      = (1 << 4)     # start on sync pulse
Z_SYN_TAPER      = (1 << 5)     # taper on z
XFIND_HOME       = (1 << 6)     # find home
XCLEAR_HOME      = (1 << 7)     # move off of home
FIND_PROBE       = (1 << 8)     # find home
CLEAR_PROBE      = (1 << 9)     # move off of home

# x direction

XPOS             = 1            # x in positive direction
XNEG             = -1           # x in negative direction

# feed types

FEED_PITCH       = 0            # feed inch per rev
FEED_TPI         = 1            # feed threads per inch
FEED_METRIC      = 2            # feed mm per rev

# home flag

FIND_HOME        = (1 << 0)     # 
CLEAR_HOME       = (1 << 1)     # 
PROBE_SET        = (1 << 2)     # 
PROBE_CLR        = (1 << 3)     # 

# home status

HOME_ACTIVE      = 0            # 
HOME_SUCCESS     = 1            # 
HOME_FAIL        = 2            # 

# probe status

PROBE_SUCCESS    = 1            # 
PROBE_FAIL       = 2            # 

# movement status

MV_PAUSE         = (1 << 0)     # movement paused
MV_READ_X        = (1 << 1)     # pause x may change
MV_READ_Z        = (1 << 2)     # pause z may change
MV_ACTIVE        = (1 << 3)     # movement active
MV_HOME_ACTIVE   = (1 << 4)     # home active
MV_XHOME         = (1 << 5)     # X home success
MV_MEASURE       = (1 << 6)     # pause for measurement

# pause flags

PAUSE_ENA_Z_JOG  = (1 << 0)     # enable z job during pause
PAUSE_ENA_X_JOG  = (1 << 1)     # enable x jog during pause
DISABLE_JOG      = (1 << 2)     # jogging disabled
PAUSE_READ_X     = (1 << 3)     # read x after pause
PAUSE_READ_Z     = (1 << 4)     # read z after pause

# thread flags

TH_RUNOUT        = (1 << 0)     # runout with thread
TH_LEFT          = (1 << 1)     # left hand thread
TH_INTERNAL      = (1 << 2)     # internal threads

# parameters for op_done

PARM_START       = 0            # start of operation
PARM_DONE        = 1            # done operation

# x isr active flags

SYNC_ACTIVE_ENC  = 1            # x from spindle encoder
SYNC_ACTIVE_TMR  = 2            # x from internal timer
