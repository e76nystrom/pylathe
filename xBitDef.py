
# xilinx bits

# z control register

ZRESET       = 0x01             # reset flag
ZSTART       = 0x02             # start z
ZSRC_SYN     = 0x04             # run z synchronized
ZSRC_FRQ     = 0x00             # run z from clock source
ZDIR_IN      = 0x08             # move z in positive dir
ZDIR_POS     = 0x08             # move z in positive dir
ZDIR_NEG     = 0x00             # move z in negative dir
ZSET_LOC     = 0x10             # set z location
ZBACKLASH    = 0x20             # backlash move no pos upd
ZWAIT_SYNC   = 0x40             # wait for sync to start

# x control register

XRESET       = 0x01             # x reset
XSTART       = 0x02             # start x
XSRC_SYN     = 0x04             # run x synchronized
XSRC_FRQ     = 0x00             # run x from clock source
XDIR_IN      = 0x08             # move x in positive dir
XDIR_POS     = 0x08             # x positive direction
XDIR_NEG     = 0x00             # x negative direction
XSET_LOC     = 0x10             # set x location
XBACKLASH    = 0x20             # x backlash move no pos upd

# taper control register

TENA         = 0x01             # taper enable
TZ           = 0x02             # one for taper z
TX           = 0x00             # zero for taper x

# position control register

PRESET       = 0x01             # reset position
PLIMIT       = 0x02             # set flag on limit reached
PZERO        = 0x04             # set flag on zero reached

# configuration register

ZSTEP_POL    = 0x01             # z step pulse polarity
ZDIR_POL     = 0x02             # z direction polarity
XSTEP_POL    = 0x04             # x step pulse polarity
XDIR_POL     = 0x08             # x direction polarity
ENC_POL      = 0x10             # encoder dir polarity
ZPULSE_MULT  = 0x20             # enable pulse multiplier

# debug control register

DBG_ENA      = 0x01             # enable debugging
DBG_SEL      = 0x02             # select dbg encoder
DBG_DIR      = 0x04             # debug direction
DBG_COUNT    = 0x08             # gen count num dbg clks
DBG_INIT     = 0x10             # init z modules
DBG_RSYN     = 0x20             # running in sync mode
DBG_MOVE     = 0x40             # used debug clock for move

# status register

S_Z_DONE_INT = 0x01             # z done interrrupt
S_X_DONE_INT = 0x02             # x done interrupt
S_DBG_DONE   = 0x04             # debug done
S_Z_START    = 0x08             # z start
S_X_START    = 0x10             # x start
S_ENC_DIR_IN = 0x20             # encoder direction in
