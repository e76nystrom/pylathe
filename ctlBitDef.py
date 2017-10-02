
# bit definitions

# common move command bits

CMD_MSK          = (7 << 0)     # move mask
CMD_MOV          = (1 << 0)     # move a set distance
CMD_JOG          = (2 << 0)     # move while cmd are present
CMD_SYN          = (3 << 0)     # move dist synchronized to rotation
CMD_MAX          = (4 << 0)     # rapid move
CMD_SPEED        = (5 << 0)     # jog at speed
JOGSLOW          = (6 << 0)     # slow jog for home or probe

# z move command bits

Z_SYN_START      = (1 << 4)     # start on sync pulse
X_SYN_TAPER      = (1 << 5)     # taper on x

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
MV_ACTIVE        = (1 << 1)     # movement active
MV_HOME_ACTIVE   = (1 << 2)     # home active
MV_XHOME         = (1 << 3)     # X home success
MV_MEASURE       = (1 << 4)     # pause for measurement