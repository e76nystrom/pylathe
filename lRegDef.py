
# fpga registers


# phase control

F_Ld_Phase_Len   =  0           # phase length
F_Rd_Phase_Syn   =  1           # read phase at sync pulse
F_Phase_Max      =  2           # number of phase registers

# controller

F_Ld_Ctrl_Data   =  0           # load controller data
F_Ctrl_Cmd       =  1           # controller command
F_Ctrl_Max       =  2           # number of controller registers

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

# debug frequency control

F_Dbg_Freq_Base  =  9           # dbg frequency

# spindle speed

F_Rd_Idx_Clks    = 11           # read clocks between index pulses

# pwm

F_PWM_Base       = 12           # pwm control

# base for modules

F_Enc_Base       = 14           # encoder registers
F_Phase_Base     = 17           # phase registers
F_ZAxis_Base     = 19           # z axis registers
F_XAxis_Base     = 36           # x axis registers
F_Cmd_Max        = 53           # number of commands

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
    "F_Dbg_Freq_Base-F_Ld_Dbg_Freq",    #   9
    "F_Dbg_Freq_Base-F_Ld_Dbg_Count",   #  10
    "F_Rd_Idx_Clks",                    #  11
    "F_PWM_Base-F_Ld_PWM_Max",          #  12
    "F_PWM_Base-F_Ld_PWM_Trig",         #  12
    "F_Enc_Base-F_Ld_Enc_Cycle",        #  14
    "F_Enc_Base-F_Ld_Int_Cycle",        #  15
    "F_Enc_Base-F_Rd_Cmp_Cyc_Clks",     #  16
    "F_Phase_Base-F_Ld_Phase_Len",      #  17
    "F_Phase_Base-F_Rd_Phase_Syn",      #  18
    "F_ZAxis_Base-F_Ld_Axis_Ctl",       #  19
    "F_ZAxis_Base-F_Ld_Freq",           #  20
    "F_ZAxis_Base-F_Ld_D",              #  21
    "F_ZAxis_Base-F_Ld_Incr1",          #  22
    "F_ZAxis_Base-F_Ld_Incr2",          #  23
    "F_ZAxis_Base-F_Ld_Accel_Val",      #  24
    "F_ZAxis_Base-F_Ld_Accel_Count",    #  25
    "F_ZAxis_Base-F_Rd_XPos",           #  26
    "F_ZAxis_Base-F_Rd_YPos",           #  27
    "F_ZAxis_Base-F_Rd_Sum",            #  28
    "F_ZAxis_Base-F_Rd_Accel_Sum",      #  29
    "F_ZAxis_Base-F_Rd_Accel_Ctr",      #  30
    "F_ZAxis_Base-F_Ld_Dist",           #  31
    "F_ZAxis_Base-F_Rd_Dist",           #  32
    "F_ZAxis_Base-F_Rd_Acl_Steps",      #  33
    "F_ZAxis_Base-F_Ld_Loc",            #  34
    "F_ZAxis_Base-F_Rd_Loc",            #  35
    "F_XAxis_Base-F_Ld_Axis_Ctl",       #  36
    "F_XAxis_Base-F_Ld_Freq",           #  37
    "F_XAxis_Base-F_Ld_D",              #  38
    "F_XAxis_Base-F_Ld_Incr1",          #  39
    "F_XAxis_Base-F_Ld_Incr2",          #  40
    "F_XAxis_Base-F_Ld_Accel_Val",      #  41
    "F_XAxis_Base-F_Ld_Accel_Count",    #  42
    "F_XAxis_Base-F_Rd_XPos",           #  43
    "F_XAxis_Base-F_Rd_YPos",           #  44
    "F_XAxis_Base-F_Rd_Sum",            #  45
    "F_XAxis_Base-F_Rd_Accel_Sum",      #  46
    "F_XAxis_Base-F_Rd_Accel_Ctr",      #  47
    "F_XAxis_Base-F_Ld_Dist",           #  48
    "F_XAxis_Base-F_Rd_Dist",           #  49
    "F_XAxis_Base-F_Rd_Acl_Steps",      #  50
    "F_XAxis_Base-F_Ld_Loc",            #  51
    "F_XAxis_Base-F_Rd_Loc",            #  52
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
    4,              #   8 F_Ctrl_Base, F_Ctrl_Cmd
    2,              #   9 F_Dbg_Freq_Base, F_Ld_Dbg_Freq
    4,              #  10 F_Dbg_Freq_Base, F_Ld_Dbg_Count
    4,              #  11 F_Rd_Idx_Clks
    4,              #  12 F_PWM_Base, F_Ld_PWM_Max
    4,              #  12 F_PWM_Base, F_Ld_PWM_Trig
    2,              #  14 F_Enc_Base, F_Ld_Enc_Cycle
    2,              #  15 F_Enc_Base, F_Ld_Int_Cycle
    4,              #  16 F_Enc_Base, F_Rd_Cmp_Cyc_Clks
    2,              #  17 F_Phase_Base, F_Ld_Phase_Len
    4,              #  18 F_Phase_Base, F_Rd_Phase_Syn
    1,              #  19 F_ZAxis_Base, F_Ld_Axis_Ctl
    4,              #  20 F_ZAxis_Base, F_Ld_Freq
    4,              #  21 F_ZAxis_Base, F_Sync_Base, F_Ld_D
    4,              #  22 F_ZAxis_Base, F_Sync_Base, F_Ld_Incr1
    4,              #  23 F_ZAxis_Base, F_Sync_Base, F_Ld_Incr2
    4,              #  24 F_ZAxis_Base, F_Sync_Base, F_Ld_Accel_Val
    4,              #  25 F_ZAxis_Base, F_Sync_Base, F_Ld_Accel_Count
    4,              #  26 F_ZAxis_Base, F_Sync_Base, F_Rd_XPos
    4,              #  27 F_ZAxis_Base, F_Sync_Base, F_Rd_YPos
    4,              #  28 F_ZAxis_Base, F_Sync_Base, F_Rd_Sum
    4,              #  29 F_ZAxis_Base, F_Sync_Base, F_Rd_Accel_Sum
    4,              #  30 F_ZAxis_Base, F_Sync_Base, F_Rd_Accel_Ctr
    4,              #  31 F_ZAxis_Base, F_Dist_Base, F_Ld_Dist
    4,              #  32 F_ZAxis_Base, F_Dist_Base, F_Rd_Dist
    4,              #  33 F_ZAxis_Base, F_Dist_Base, F_Rd_Acl_Steps
    4,              #  34 F_ZAxis_Base, F_Loc_Base, F_Ld_Loc
    4,              #  35 F_ZAxis_Base, F_Loc_Base, F_Rd_Loc
    1,              #  36 F_XAxis_Base, F_Ld_Axis_Ctl
    4,              #  37 F_XAxis_Base, F_Ld_Freq
    4,              #  38 F_XAxis_Base, F_Sync_Base, F_Ld_D
    4,              #  39 F_XAxis_Base, F_Sync_Base, F_Ld_Incr1
    4,              #  40 F_XAxis_Base, F_Sync_Base, F_Ld_Incr2
    4,              #  41 F_XAxis_Base, F_Sync_Base, F_Ld_Accel_Val
    4,              #  42 F_XAxis_Base, F_Sync_Base, F_Ld_Accel_Count
    4,              #  43 F_XAxis_Base, F_Sync_Base, F_Rd_XPos
    4,              #  44 F_XAxis_Base, F_Sync_Base, F_Rd_YPos
    4,              #  45 F_XAxis_Base, F_Sync_Base, F_Rd_Sum
    4,              #  46 F_XAxis_Base, F_Sync_Base, F_Rd_Accel_Sum
    4,              #  47 F_XAxis_Base, F_Sync_Base, F_Rd_Accel_Ctr
    4,              #  48 F_XAxis_Base, F_Dist_Base, F_Ld_Dist
    4,              #  49 F_XAxis_Base, F_Dist_Base, F_Rd_Dist
    4,              #  50 F_XAxis_Base, F_Dist_Base, F_Rd_Acl_Steps
    4,              #  51 F_XAxis_Base, F_Loc_Base, F_Ld_Loc
    4,              #  52 F_XAxis_Base, F_Loc_Base, F_Rd_Loc
    )

importList = ( \
 xRegTable, \
 F_Ld_Phase_Len, \
 F_Rd_Phase_Syn, \
 F_Phase_Max, \
 F_Ld_Ctrl_Data, \
 F_Ctrl_Cmd, \
 F_Ctrl_Max, \
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
 F_Dbg_Freq_Base, \
 F_Rd_Idx_Clks, \
 F_PWM_Base, \
 F_Enc_Base, \
 F_Phase_Base, \
 F_ZAxis_Base, \
 F_XAxis_Base, \
 F_Cmd_Max, \
)
