# fpga bits

# z control register

zReset       = 0x01             # reset flag
zStart       = 0x02             # start z
zSrc_Syn     = 0x04             # run z synchronized
zSrc_Frq     = 0x00             # run z from clock source
zDir_In      = 0x08             # move z in positive dir
zDir_Pos     = 0x08             # move z in positive dir
zDir_Neg     = 0x00             # move z in negative dir
zSet_Loc     = 0x10             # set z location
zBacklash    = 0x20             # backlash move no pos upd
zWait_Sync   = 0x40             # wait for sync to start

# x control register

xReset       = 0x01             # x reset
xStart       = 0x02             # start x
xSrc_Syn     = 0x04             # run x synchronized
xSrc_Frq     = 0x00             # run x from clock source
xDir_In      = 0x08             # move x in positive dir
xDir_Pos     = 0x08             # x positive direction
xDir_Neg     = 0x00             # x negative direction
xSet_Loc     = 0x10             # set x location
xBacklash    = 0x20             # x backlash move no pos upd

# taper control register

tEna         = 0x01             # taper enable
tZ           = 0x02             # one for taper z
tX           = 0x00             # zero for taper x

# position control register

pReset       = 0x01             # reset position
pLimit       = 0x02             # set flag on limit reached
pZero        = 0x04             # set flag on zero reached

# configuration register

zStep_Pol    = 0x01             # z step pulse polarity
zDir_Pol     = 0x02             # z direction polarity
xStep_Pol    = 0x04             # x step pulse polarity
xDir_Pol     = 0x08             # x direction polarity
enc_Pol      = 0x10             # encoder dir polarity
zPulse_Mult  = 0x20             # enable pulse multiplier

# debug control register

Dbg_Ena      = 0x01             # enable debugging
Dbg_Sel      = 0x02             # select dbg encoder
Dbg_Dir      = 0x04             # debug direction
Dbg_Count    = 0x08             # gen count num dbg clks
Dbg_Init     = 0x10             # init z modules
Dbg_Rsyn     = 0x20             # running in sync mode
Dbg_Move     = 0x40             # used debug clock for move

# status register

s_Z_Done_Int = 0x01             # z done interrrupt
s_X_Done_Int = 0x02             # x done interrupt
s_Dbg_Done   = 0x04             # debug done
s_Z_Start    = 0x08             # z start
s_X_Start    = 0x10             # x start
s_Enc_Dir_In = 0x20             # encoder direction in

importList = ( \
 zReset, \
 zStart, \
 zSrc_Syn, \
 zSrc_Frq, \
 zDir_In, \
 zDir_Pos, \
 zDir_Neg, \
 zSet_Loc, \
 zBacklash, \
 zWait_Sync, \
 xReset, \
 xStart, \
 xSrc_Syn, \
 xSrc_Frq, \
 xDir_In, \
 xDir_Pos, \
 xDir_Neg, \
 xSet_Loc, \
 xBacklash, \
 tEna, \
 tZ, \
 tX, \
 pReset, \
 pLimit, \
 pZero, \
 zStep_Pol, \
 zDir_Pol, \
 xStep_Pol, \
 xDir_Pol, \
 enc_Pol, \
 zPulse_Mult, \
 Dbg_Ena, \
 Dbg_Sel, \
 Dbg_Dir, \
 Dbg_Count, \
 Dbg_Init, \
 Dbg_Rsyn, \
 Dbg_Move, \
 s_Z_Done_Int, \
 s_X_Done_Int, \
 s_Dbg_Done, \
 s_Z_Start, \
 s_X_Start, \
 s_Enc_Dir_In, \
)
