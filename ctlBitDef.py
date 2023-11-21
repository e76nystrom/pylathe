
# bit definitions

# common move command bits

CMD_MSK          = (7 << 0)     # 0x07 move mask
CMD_MOV          = (1 << 0)     # 0x01 move a set distance
CMD_JOG          = (2 << 0)     # 0x02 move while cmd are present
CMD_SYN          = (3 << 0)     # 0x03 move dist synchronized to rotation
CMD_MAX          = (4 << 0)     # 0x04 rapid move
CMD_SPEED        = (5 << 0)     # 0x05 jog at speed
JOG_SLOW         = (6 << 0)     # 0x06 slow jog for home or probe
SYN_START        = (1 << 3)     # 0x08 start on sync pulse
SYN_LEFT         = (1 << 4)     # 0x10 start sync left
SYN_TAPER        = (1 << 5)     # 0x20 taper on other axis
DIST_MODE        = (1 << 6)     # 0x40 distance update mode
FIND_HOME        = (1 << 7)     # 0x80 find home
CLEAR_HOME       = (1 << 8)     # 0x100 move off of home
FIND_PROBE       = (1 << 9)     # 0x200 find probe
CLEAR_PROBE      = (1 << 10)    # 0x400 move off of probe
DRO_POS          = (1 << 11)    # 0x800 use dro for moving
DRO_UPD          = (1 << 12)    # 0x1000 update internal position from dro

# common definitions

DIR_POS          = 1            # 0x01 positive direction
DIR_NEG          = -1           # 0x-1 negative direction

# z direction

ZPOS             = 1            # 0x01 z in positive direction
ZNEG             = -1           # 0x-1 z in negative direction

# x direction

XPOS             = 1            # 0x01 x in positive direction
XNEG             = -1           # 0x-1 x in negative direction

# feed types

FEED_PITCH       = 0            # 0x00 feed inch per rev
FEED_TPI         = 1            # 0x01 feed threads per inch
FEED_METRIC      = 2            # 0x02 feed mm per rev

# home flag

HOME_SET         = (1 << 0)     # 0x01 
HOME_CLR         = (1 << 1)     # 0x02 
PROBE_SET        = (1 << 2)     # 0x04 
PROBE_CLR        = (1 << 3)     # 0x08 

# home direction

HOME_FWD         = 0            # 0x00 
HOME_REV         = 1            # 0x01 

# home status

HOME_ACTIVE      = 0            # 0x00 
HOME_SUCCESS     = 1            # 0x01 
HOME_FAIL        = 2            # 0x02 

# probe status

PROBE_SUCCESS    = 1            # 0x01 
PROBE_FAIL       = 2            # 0x02 

# movement status

MV_PAUSE         = (1 << 0)     # 0x01 movement paused
MV_READ_X        = (1 << 1)     # 0x02 pause x may change
MV_READ_Z        = (1 << 2)     # 0x04 pause z may change
MV_ACTIVE        = (1 << 3)     # 0x08 movement active
MV_DONE          = (1 << 4)     # 0x10 movement active
MV_X_LIMIT       = (1 << 5)     # 0x20 at limit switch
MV_Z_LIMIT       = (1 << 6)     # 0x40 at limit switch
MV_X_HOME_ACTIVE = (1 << 7)     # 0x80 x home active
MV_X_HOME        = (1 << 8)     # 0x100 x home success
MV_Z_HOME_ACTIVE = (1 << 9)     # 0x200 z home active
MV_Z_HOME        = (1 << 10)    # 0x400 z home success
MV_MEASURE       = (1 << 11)    # 0x800 pause for measurement
MV_ESTOP         = (1 << 12)    # 0x1000 estop

# pause flags

DISABLE_JOG      = (1 << 0)     # 0x01 jogging disabled
PAUSE_ENA_Z_JOG  = (1 << 1)     # 0x02 enable z job during pause
PAUSE_ENA_X_JOG  = (1 << 2)     # 0x04 enable x jog during pause
PAUSE_READ_Z     = (1 << 3)     # 0x08 read z after pause
PAUSE_READ_X     = (1 << 4)     # 0x10 read x after pause

# thread flags

TH_THREAD        = (1 << 0)     # 0x01 threading
TH_INTERNAL      = (1 << 1)     # 0x02 internal threads
TH_LEFT          = (1 << 2)     # 0x04 left hand thread
TH_RUNOUT        = (1 << 3)     # 0x08 runout with thread

# parameters for op_done

PARM_START       = 0            # 0x00 start of operation
PARM_DONE        = 1            # 0x01 done operation

# encoder direct flags

Z_ENCODER_DIRECT = (1 << 0)     # 0x01 z sync directly from encoder
X_ENCODER_DIRECT = (1 << 1)     # 0x02 x sync directly from encoder

# point by point movement commands

PCMD_INCX_HLDZ_S1 = (0 << 0)    # 0x00 step x hold z then step 1
PCMD_INCX_HLDZ_SN = (1 << 0)    # 0x01 step x hold z 1 then step z
PCMD_HLDX_S1_INCZ = (2 << 0)    # 0x02 step x hold z then step 1
PCMD_HLDX_SN_INCZ = (3 << 0)    # 0x03 hold x 1 then step x increment z
PCMD_EXTEND      = (4 << 0)     # 0x04 extend command
PCMD_SPARE_0     = (5 << 0)     # 0x05 spare 0
PCMD_SPARE_1     = (5 << 0)     # 0x05 spare 1
PCMD_SET_DIR     = (7 << 0)     # 0x07 set direction
PCMD_X_NEG       = (1 << 0)     # 0x01 mov x negative
PCMD_Z_NEG       = (1 << 1)     # 0x02 mov z negative
PCMD_DIR_FLAG    = (1 << 2)     # 0x04 direction flag
PCMD_CMD_MASK    = (7 << 0)     # 0x07 command mask
PEXT_OFFSET      = (8)          # 0x08 
PEXT_INCX        = (0 << 0)     # 0x00 step x
PEXT_INCZ        = (1 << 0)     # 0x01 step z
PEXT_INCX_INCZ   = (2 << 0)     # 0x02 step x and z
PEXT_INCX2_INCZ  = (3 << 0)     # 0x03 step x 2 step z
PCMD_RPT_SHIFT   = (3)          # 0x03 repeat mask
PCMD_RPT_SHORT   = (32)         # 0x20 repeat short
PCMD_RPT_MASK    = (0x1f << PCMD_RPT_SHIFT)# 0xf8 repeat shift

# isr active flags

A_S              = 6            # 0x06 shift for arc syn
SYNC_ACTIVE_EXT  = (1 << 0)     # 0x01 sync board
SYNC_ACTIVE_TMR  = (1 << 1)     # 0x02 internal timer
SYNC_ACTIVE_ENC  = (1 << 2)     # 0x04 encoder
SYNC_ACTIVE_STEP = (1 << 3)     # 0x08 stepper
SYNC_ACTIVE_TAPER = (1 << 4)    # 0x10 taper
SYNC_ACTIVE_THREAD = (1 << 5)   # 0x20 threading
ARC_ACTIVE_EXT   = (SYNC_ACTIVE_EXT << A_S)# 0x40 arc sync board
ARC_ACTIVE_TMR   = (SYNC_ACTIVE_TMR << A_S)# 0x80 arc int tmr
ARC_ACTIVE_ENC   = (SYNC_ACTIVE_ENC << A_S)# 0x100 arc encoder
ARC_ACTIVE_STEP  = (SYNC_ACTIVE_STEP << A_S)# 0x200 arc stepper
