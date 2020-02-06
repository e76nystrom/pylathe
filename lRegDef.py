
# fpga registers


# phase control

F_Ld_Phase_Len   =  0           # phase length
F_Rd_Phase_Syn   =  1           # read phase at sync pulse
F_Phase_Max      =  2           # number of phase registers

# controller

F_Ld_Ctrl_Data   =  0           # load controller data
F_Ctrl_Cmd       =  1           # controller command
F_Ld_Seq         =  2           # load sequence
F_Rd_Seq         =  3           # read sequence
F_Rd_Ctr         =  4           # read counter
F_Ctrl_Max       =  5           # number of controller registers

# reader

F_Ld_Read_Data   =  0           # load reader data
F_Read           =  1           # read data
F_Read_Max       =  2           # number of reader registers

# PWM

F_Ld_PWM_Max     =  0           # pwm counter maximum
F_Ld_PWM_Trig    =  0           # pwm trigger
F_PWM_Max        =  1           # number of pwm registers

# encoder

F_Ld_Enc_Cycle   =  0           # load encoder cycle
F_Ld_Int_Cycle   =  1           # load internal cycle
F_Rd_Cmp_Cyc_Clks =  2          # read cmp cycle clocks
F_Enc_Max        =  3           # number of encoder registers

# debug frequency

F_Ld_Dbg_Freq    =  0           # debug frequency
F_Ld_Dbg_Count   =  1           # debug count
F_Dbg_Freq_Max   =  2           # number of debug frequency regs

# sync accel

F_Ld_D           =  0           # axis d
F_Ld_Incr1       =  1           # axis incr1
F_Ld_Incr2       =  2           # axis incr2
F_Ld_Accel_Val   =  3           # axis accel value
F_Ld_Accel_Count =  4           # axis accel count
F_Rd_XPos        =  5           # axis x pos
F_Rd_YPos        =  6           # axis y pos
F_Rd_Sum         =  7           # axis sum
F_Rd_Accel_Sum   =  8           # axis accel sum
F_Rd_Accel_Ctr   =  9           # axis accel counter
F_Sync_Max       = 10           # number of sync registers

# distance registers

F_Ld_Dist        =  0           # axis distance
F_Rd_Dist        =  1           # read axis distance
F_Rd_Acl_Steps   =  2           # read accel steps
F_Dist_Max       =  3           # number of distance registers

# location registers

F_Ld_Loc         =  0           # axis location
F_Rd_Loc         =  1           # read axis location
F_Loc_Max        =  2           # number of location registers

# axis

F_Ld_Axis_Ctl    =  0           # axis control register
F_Ld_Freq        =  1           # frequency
F_Sync_Base      =  2           # sync registers
F_Dist_Base      = 12           # distance registers
F_Loc_Base       = 15           # location registers
F_Axis_Max       = 17           # number of axis registers

# register definitions

F_Noop           =  0           # register 0

# status registers

F_Rd_Status      =  1           # status register

# control registers

F_Ld_Run_Ctl     =  2           # run control register
F_Ld_Sync_Ctl    =  3           # sync control register
F_Ld_Cfg_Ctl     =  4           # config control register
F_Ld_Clk_Ctl     =  5           # clock control register
F_Ld_Dsp_Reg     =  6           # display register

# controller

F_Ctrl_Base      =  7           # controller

# reader

F_Read_Base      = 12           # reader

# debug frequency control

F_Dbg_Freq_Base  = 14           # dbg frequency

# spindle speed

F_Rd_Idx_Clks    = 16           # read clocks between index pulses

# pwm

F_PWM_Base       = 17           # pwm control

# base for modules

F_Enc_Base       = 19           # encoder registers
F_Phase_Base     = 22           # phase registers
F_ZAxis_Base     = 24           # z axis registers
F_XAxis_Base     = 41           # x axis registers
F_Cmd_Max        = 58           # number of commands

# xilinx table

xRegTable = ( \
    "F_Noop",                           #   0
    "F_Rd_Status",                      #   1
    "F_Ld_Run_Ctl",                     #   2
    "F_Ld_Sync_Ctl",                    #   3
    "F_Ld_Cfg_Ctl",                     #   4
    "F_Ld_Clk_Ctl",                     #   5
    "F_Ld_Dsp_Reg",                     #   6
    "F_Ctrl_Base-F_Ld_Ctrl_Data",       #   7
    "F_Ctrl_Base-F_Ctrl_Cmd",           #   8
    "F_Ctrl_Base-F_Ld_Seq",             #   9
    "F_Ctrl_Base-F_Rd_Seq",             #  10
    "F_Ctrl_Base-F_Rd_Ctr",             #  11
    "F_Read_Base-F_Ld_Read_Data",       #  12
    "F_Read_Base-F_Read",               #  13
    "F_Dbg_Freq_Base-F_Ld_Dbg_Freq",    #  14
    "F_Dbg_Freq_Base-F_Ld_Dbg_Count",   #  15
    "F_Rd_Idx_Clks",                    #  16
    "F_PWM_Base-F_Ld_PWM_Max",          #  17
    "F_PWM_Base-F_Ld_PWM_Trig",         #  17
    "F_Enc_Base-F_Ld_Enc_Cycle",        #  19
    "F_Enc_Base-F_Ld_Int_Cycle",        #  20
    "F_Enc_Base-F_Rd_Cmp_Cyc_Clks",     #  21
    "F_Phase_Base-F_Ld_Phase_Len",      #  22
    "F_Phase_Base-F_Rd_Phase_Syn",      #  23
    "F_ZAxis_Base-F_Ld_Axis_Ctl",       #  24
    "F_ZAxis_Base-F_Ld_Freq",           #  25
    "F_ZAxis_Base-F_Ld_D",              #  26
    "F_ZAxis_Base-F_Ld_Incr1",          #  27
    "F_ZAxis_Base-F_Ld_Incr2",          #  28
    "F_ZAxis_Base-F_Ld_Accel_Val",      #  29
    "F_ZAxis_Base-F_Ld_Accel_Count",    #  30
    "F_ZAxis_Base-F_Rd_XPos",           #  31
    "F_ZAxis_Base-F_Rd_YPos",           #  32
    "F_ZAxis_Base-F_Rd_Sum",            #  33
    "F_ZAxis_Base-F_Rd_Accel_Sum",      #  34
    "F_ZAxis_Base-F_Rd_Accel_Ctr",      #  35
    "F_ZAxis_Base-F_Ld_Dist",           #  36
    "F_ZAxis_Base-F_Rd_Dist",           #  37
    "F_ZAxis_Base-F_Rd_Acl_Steps",      #  38
    "F_ZAxis_Base-F_Ld_Loc",            #  39
    "F_ZAxis_Base-F_Rd_Loc",            #  40
    "F_XAxis_Base-F_Ld_Axis_Ctl",       #  41
    "F_XAxis_Base-F_Ld_Freq",           #  42
    "F_XAxis_Base-F_Ld_D",              #  43
    "F_XAxis_Base-F_Ld_Incr1",          #  44
    "F_XAxis_Base-F_Ld_Incr2",          #  45
    "F_XAxis_Base-F_Ld_Accel_Val",      #  46
    "F_XAxis_Base-F_Ld_Accel_Count",    #  47
    "F_XAxis_Base-F_Rd_XPos",           #  48
    "F_XAxis_Base-F_Rd_YPos",           #  49
    "F_XAxis_Base-F_Rd_Sum",            #  50
    "F_XAxis_Base-F_Rd_Accel_Sum",      #  51
    "F_XAxis_Base-F_Rd_Accel_Ctr",      #  52
    "F_XAxis_Base-F_Ld_Dist",           #  53
    "F_XAxis_Base-F_Rd_Dist",           #  54
    "F_XAxis_Base-F_Rd_Acl_Steps",      #  55
    "F_XAxis_Base-F_Ld_Loc",            #  56
    "F_XAxis_Base-F_Rd_Loc",            #  57
    )

fpgaSizeTable = ( \
    1,              #   0 F_Noop
    4,              #   1 F_Rd_Status
    1,              #   2 F_Ld_Run_Ctl
    1,              #   3 F_Ld_Sync_Ctl
    1,              #   4 F_Ld_Cfg_Ctl
    1,              #   5 F_Ld_Clk_Ctl
    1,              #   6 F_Ld_Dsp_Reg
    0,              #   7 F_Ctrl_Base, F_Ld_Ctrl_Data
    1,              #   8 F_Ctrl_Base, F_Ctrl_Cmd
    1,              #   9 F_Ctrl_Base, F_Ld_Seq
    1,              #  10 F_Ctrl_Base, F_Rd_Seq
    1,              #  11 F_Ctrl_Base, F_Rd_Ctr
    0,              #  12 F_Read_Base, F_Ld_Read_Data
    0,              #  13 F_Read_Base, F_Read
    2,              #  14 F_Dbg_Freq_Base, F_Ld_Dbg_Freq
    4,              #  15 F_Dbg_Freq_Base, F_Ld_Dbg_Count
    4,              #  16 F_Rd_Idx_Clks
    4,              #  17 F_PWM_Base, F_Ld_PWM_Max
    4,              #  17 F_PWM_Base, F_Ld_PWM_Trig
    2,              #  19 F_Enc_Base, F_Ld_Enc_Cycle
    2,              #  20 F_Enc_Base, F_Ld_Int_Cycle
    4,              #  21 F_Enc_Base, F_Rd_Cmp_Cyc_Clks
    2,              #  22 F_Phase_Base, F_Ld_Phase_Len
    4,              #  23 F_Phase_Base, F_Rd_Phase_Syn
    1,              #  24 F_ZAxis_Base, F_Ld_Axis_Ctl
    4,              #  25 F_ZAxis_Base, F_Ld_Freq
    4,              #  26 F_ZAxis_Base, F_Sync_Base, F_Ld_D
    4,              #  27 F_ZAxis_Base, F_Sync_Base, F_Ld_Incr1
    4,              #  28 F_ZAxis_Base, F_Sync_Base, F_Ld_Incr2
    4,              #  29 F_ZAxis_Base, F_Sync_Base, F_Ld_Accel_Val
    4,              #  30 F_ZAxis_Base, F_Sync_Base, F_Ld_Accel_Count
    4,              #  31 F_ZAxis_Base, F_Sync_Base, F_Rd_XPos
    4,              #  32 F_ZAxis_Base, F_Sync_Base, F_Rd_YPos
    4,              #  33 F_ZAxis_Base, F_Sync_Base, F_Rd_Sum
    4,              #  34 F_ZAxis_Base, F_Sync_Base, F_Rd_Accel_Sum
    4,              #  35 F_ZAxis_Base, F_Sync_Base, F_Rd_Accel_Ctr
    4,              #  36 F_ZAxis_Base, F_Dist_Base, F_Ld_Dist
    4,              #  37 F_ZAxis_Base, F_Dist_Base, F_Rd_Dist
    4,              #  38 F_ZAxis_Base, F_Dist_Base, F_Rd_Acl_Steps
    4,              #  39 F_ZAxis_Base, F_Loc_Base, F_Ld_Loc
    4,              #  40 F_ZAxis_Base, F_Loc_Base, F_Rd_Loc
    1,              #  41 F_XAxis_Base, F_Ld_Axis_Ctl
    4,              #  42 F_XAxis_Base, F_Ld_Freq
    4,              #  43 F_XAxis_Base, F_Sync_Base, F_Ld_D
    4,              #  44 F_XAxis_Base, F_Sync_Base, F_Ld_Incr1
    4,              #  45 F_XAxis_Base, F_Sync_Base, F_Ld_Incr2
    4,              #  46 F_XAxis_Base, F_Sync_Base, F_Ld_Accel_Val
    4,              #  47 F_XAxis_Base, F_Sync_Base, F_Ld_Accel_Count
    4,              #  48 F_XAxis_Base, F_Sync_Base, F_Rd_XPos
    4,              #  49 F_XAxis_Base, F_Sync_Base, F_Rd_YPos
    4,              #  50 F_XAxis_Base, F_Sync_Base, F_Rd_Sum
    4,              #  51 F_XAxis_Base, F_Sync_Base, F_Rd_Accel_Sum
    4,              #  52 F_XAxis_Base, F_Sync_Base, F_Rd_Accel_Ctr
    4,              #  53 F_XAxis_Base, F_Dist_Base, F_Ld_Dist
    4,              #  54 F_XAxis_Base, F_Dist_Base, F_Rd_Dist
    4,              #  55 F_XAxis_Base, F_Dist_Base, F_Rd_Acl_Steps
    4,              #  56 F_XAxis_Base, F_Loc_Base, F_Ld_Loc
    4,              #  57 F_XAxis_Base, F_Loc_Base, F_Rd_Loc
    )

importList = ( \
 xRegTable, \
 F_Ld_Phase_Len, \
 F_Rd_Phase_Syn, \
 F_Phase_Max, \
 F_Ld_Ctrl_Data, \
 F_Ctrl_Cmd, \
 F_Ld_Seq, \
 F_Rd_Seq, \
 F_Rd_Ctr, \
 F_Ctrl_Max, \
 F_Ld_Read_Data, \
 F_Read, \
 F_Read_Max, \
 F_Ld_PWM_Max, \
 F_Ld_PWM_Trig, \
 F_PWM_Max, \
 F_Ld_Enc_Cycle, \
 F_Ld_Int_Cycle, \
 F_Rd_Cmp_Cyc_Clks, \
 F_Enc_Max, \
 F_Ld_Dbg_Freq, \
 F_Ld_Dbg_Count, \
 F_Dbg_Freq_Max, \
 F_Ld_D, \
 F_Ld_Incr1, \
 F_Ld_Incr2, \
 F_Ld_Accel_Val, \
 F_Ld_Accel_Count, \
 F_Rd_XPos, \
 F_Rd_YPos, \
 F_Rd_Sum, \
 F_Rd_Accel_Sum, \
 F_Rd_Accel_Ctr, \
 F_Sync_Max, \
 F_Ld_Dist, \
 F_Rd_Dist, \
 F_Rd_Acl_Steps, \
 F_Dist_Max, \
 F_Ld_Loc, \
 F_Rd_Loc, \
 F_Loc_Max, \
 F_Ld_Axis_Ctl, \
 F_Ld_Freq, \
 F_Sync_Base, \
 F_Dist_Base, \
 F_Loc_Base, \
 F_Axis_Max, \
 F_Noop, \
 F_Rd_Status, \
 F_Ld_Run_Ctl, \
 F_Ld_Sync_Ctl, \
 F_Ld_Cfg_Ctl, \
 F_Ld_Clk_Ctl, \
 F_Ld_Dsp_Reg, \
 F_Ctrl_Base, \
 F_Read_Base, \
 F_Dbg_Freq_Base, \
 F_Rd_Idx_Clks, \
 F_PWM_Base, \
 F_Enc_Base, \
 F_Phase_Base, \
 F_ZAxis_Base, \
 F_XAxis_Base, \
 F_Cmd_Max, \
)
