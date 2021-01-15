
# bit definitions

# common move command bits

CMD_MSK          = (7 << 0)     # move mask
CMD_MOV          = (1 << 0)     # move a set distance
CMD_JOG          = (2 << 0)     # move while cmd are present
CMD_SYN          = (3 << 0)     # move dist synchronized to rotation
CMD_MAX          = (4 << 0)     # rapid move
CMD_SPEED        = (5 << 0)     # jog at speed
JOGSLOW          = (6 << 0)     # slow jog for home or probe
SYN_START        = (1 << 4)     # start on sync pulse
SYN_LEFT         = (1 << 5)     # start sync left
SYN_TAPER        = (1 << 6)     # taper on other axis
FIND_HOME        = (1 << 7)     # find home
CLEAR_HOME       = (1 << 8)     # move off of home
FIND_PROBE       = (1 << 9)     # find probe
CLEAR_PROBE      = (1 << 10)    # move off of probe
DRO_POS          = (1 << 11)    # use dro for moving
DRO_UPD          = (1 << 12)    # update internal position from dro

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
Z_SYN_TAPER      = (1 << 6)     # taper on z

# x direction

XPOS             = 1            # x in positive direction
XNEG             = -1           # x in negative direction

# feed types

FEED_PITCH       = 0            # feed inch per rev
FEED_TPI         = 1            # feed threads per inch
FEED_METRIC      = 2            # feed mm per rev

# home flag

HOME_SET         = (1 << 0)     # 
HOME_CLR         = (1 << 1)     # 
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
MV_XLIMIT        = (1 << 4)     # at limit switch
MV_ZLIMIT        = (1 << 5)     # at limit switch
MV_XHOME_ACTIVE  = (1 << 6)     # x home active
MV_XHOME         = (1 << 7)     # x home success
MV_ZHOME_ACTIVE  = (1 << 8)     # z home active
MV_ZHOME         = (1 << 9)     # z home success
MV_MEASURE       = (1 << 10)    # pause for measurement

# pause flags

PAUSE_ENA_Z_JOG  = (1 << 0)     # enable z job during pause
PAUSE_ENA_X_JOG  = (1 << 1)     # enable x jog during pause
DISABLE_JOG      = (1 << 2)     # jogging disabled
PAUSE_READ_X     = (1 << 3)     # read x after pause
PAUSE_READ_Z     = (1 << 4)     # read z after pause

# thread flags

TH_THREAD        = (1 << 0)     # threading
TH_INTERNAL      = (1 << 1)     # internal threads
TH_LEFT          = (1 << 2)     # left hand thread
TH_RUNOUT        = (1 << 3)     # runout with thread

# parameters for op_done

PARM_START       = 0            # start of operation
PARM_DONE        = 1            # done operation

# isr active flags

SYNC_ACTIVE_EXT  = (1 << 0)     # active for sync board
SYNC_ACTIVE_TMR  = (1 << 1)     # active for internal timer
SYNC_ACTIVE_ENC  = (1 << 2)     # active for encoder
SYNC_ACTIVE_STEP = (1 << 3)     # active for stepper
SYNC_ACTIVE_TAPER = (1 << 4)    # active for taper
SYNC_ACTIVE_THREAD = (1 << 5)   # active for threading

# encoder direct flags

Z_ENCODER_DIRECT = (1 << 0)     # z sync directly from encoder
X_ENCODER_DIRECT = (1 << 1)     # x sync directly from encoder
