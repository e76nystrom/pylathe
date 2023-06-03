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

# dro registers

F_Ld_Dro         =  0           # axis dro
F_Ld_Dro_End     =  1           # axis dro end
F_Ld_Dro_Limit   =  2           # axis dro deceleration limit
F_Rd_Dro         =  3           # read axis dro
F_Dro_Max        =  4           # number of dro registers

# jog registers

F_Ld_Jog_Ctl     =  0           # jog control
F_Ld_Jog_Inc     =  1           # jog increment
F_Ld_Jog_Back    =  2           # jog backlash increment
F_Jog_Max        =  3           # number of jog registers

# axis

F_Rd_Axis_Status =  0           # axis status
F_Ld_Axis_Ctl    =  1           # axis control register
F_Rd_Axis_Ctl    =  2           # axis control register
F_Ld_Freq        =  3           # frequency
F_Sync_Base      =  4           # sync registers
F_Dist_Base      = 14           # distance registers
F_Loc_Base       = 17           # location registers
F_Dro_Base       = 19           # dro registers
F_Jog_Base       = 23           # jog registers
F_Axis_Max       = 26           # number of axis registers

# spindle

F_Ld_Sp_Ctl      =  0           # spindle control register
F_Ld_Sp_Freq     =  1           # freq for step spindle
F_Sp_Sync_Base   =  2           # spindle sync
F_Sp_Jog_Base    = 12           # spindle jog

# register definitions

F_Noop           =  0           # register 0

# status registers

F_Rd_Status      =  1           # status register
F_Rd_Inputs      =  2           # inputs register

# control registers

F_Ld_Run_Ctl     =  3           # run control register
F_Ld_Sync_Ctl    =  4           # sync control register
F_Ld_Cfg_Ctl     =  5           # config control register
F_Ld_Clk_Ctl     =  6           # clock control register
F_Ld_Dsp_Reg     =  7           # display register

# controller

F_Ctrl_Base      =  8           # controller

# reader

F_Read_Base      = 13           # reader

# debug frequency control

F_Dbg_Freq_Base  = 15           # dbg frequency

# spindle speed

F_Rd_Idx_Clks    = 17           # read clocks between index pulses

# step spindle frequency generator


# pwm

F_PWM_Base       = 18           # pwm control

# base for modules

F_Enc_Base       = 20           # encoder registers
F_Phase_Base     = 23           # phase registers
F_ZAxis_Base     = 25           # z axis registers
F_XAxis_Base     = 51           # x axis registers
F_Spindle_Base   = 77           # spindle registers
F_Cmd_Max        = 92           # number of commands
# fpga table

xRegTable = ( \
    "F_Noop",                           #   0 x00
    "F_Rd_Status",                      #   1 x01
    "F_Rd_Inputs",                      #   2 x02
    "F_Ld_Run_Ctl",                     #   3 x03
    "F_Ld_Sync_Ctl",                    #   4 x04
    "F_Ld_Cfg_Ctl",                     #   5 x05
    "F_Ld_Clk_Ctl",                     #   6 x06
    "F_Ld_Dsp_Reg",                     #   7 x07
    "F_Ctrl_Base+F_Ld_Ctrl_Data",       #   8 x08
    "F_Ctrl_Base+F_Ctrl_Cmd",           #   9 x09
    "F_Ctrl_Base+F_Ld_Seq",             #  10 x0a
    "F_Ctrl_Base+F_Rd_Seq",             #  11 x0b
    "F_Ctrl_Base+F_Rd_Ctr",             #  12 x0c
    "F_Read_Base+F_Ld_Read_Data",       #  13 x0d
    "F_Read_Base+F_Read",               #  14 x0e
    "F_Dbg_Freq_Base+F_Ld_Dbg_Freq",    #  15 x0f
    "F_Dbg_Freq_Base+F_Ld_Dbg_Count",   #  16 x10
    "F_Rd_Idx_Clks",                    #  17 x11
    "F_PWM_Base+F_Ld_PWM_Max",          #  18 x12
    "F_PWM_Base+F_Ld_PWM_Trig",         #  18 x12
    "F_Enc_Base+F_Ld_Enc_Cycle",        #  20 x14
    "F_Enc_Base+F_Ld_Int_Cycle",        #  21 x15
    "F_Enc_Base+F_Rd_Cmp_Cyc_Clks",     #  22 x16
    "F_Phase_Base+F_Ld_Phase_Len",      #  23 x17
    "F_Phase_Base+F_Rd_Phase_Syn",      #  24 x18
    "F_ZAxis_Base+F_Rd_Axis_Status",    #  25 x19
    "F_ZAxis_Base+F_Ld_Axis_Ctl",       #  26 x1a
    "F_ZAxis_Base+F_Rd_Axis_Ctl",       #  27 x1b
    "F_ZAxis_Base+F_Ld_Freq",           #  28 x1c
    "F_ZAxis_Base+F_Ld_D",              #  29 x1d
    "F_ZAxis_Base+F_Ld_Incr1",          #  30 x1e
    "F_ZAxis_Base+F_Ld_Incr2",          #  31 x1f
    "F_ZAxis_Base+F_Ld_Accel_Val",      #  32 x20
    "F_ZAxis_Base+F_Ld_Accel_Count",    #  33 x21
    "F_ZAxis_Base+F_Rd_XPos",           #  34 x22
    "F_ZAxis_Base+F_Rd_YPos",           #  35 x23
    "F_ZAxis_Base+F_Rd_Sum",            #  36 x24
    "F_ZAxis_Base+F_Rd_Accel_Sum",      #  37 x25
    "F_ZAxis_Base+F_Rd_Accel_Ctr",      #  38 x26
    "F_ZAxis_Base+F_Ld_Dist",           #  39 x27
    "F_ZAxis_Base+F_Rd_Dist",           #  40 x28
    "F_ZAxis_Base+F_Rd_Acl_Steps",      #  41 x29
    "F_ZAxis_Base+F_Ld_Loc",            #  42 x2a
    "F_ZAxis_Base+F_Rd_Loc",            #  43 x2b
    "F_ZAxis_Base+F_Ld_Dro",            #  44 x2c
    "F_ZAxis_Base+F_Ld_Dro_End",        #  45 x2d
    "F_ZAxis_Base+F_Ld_Dro_Limit",      #  46 x2e
    "F_ZAxis_Base+F_Rd_Dro",            #  47 x2f
    "F_ZAxis_Base+F_Ld_Jog_Ctl",        #  48 x30
    "F_ZAxis_Base+F_Ld_Jog_Inc",        #  49 x31
    "F_ZAxis_Base+F_Ld_Jog_Back",       #  50 x32
    "F_XAxis_Base+F_Rd_Axis_Status",    #  51 x33
    "F_XAxis_Base+F_Ld_Axis_Ctl",       #  52 x34
    "F_XAxis_Base+F_Rd_Axis_Ctl",       #  53 x35
    "F_XAxis_Base+F_Ld_Freq",           #  54 x36
    "F_XAxis_Base+F_Ld_D",              #  55 x37
    "F_XAxis_Base+F_Ld_Incr1",          #  56 x38
    "F_XAxis_Base+F_Ld_Incr2",          #  57 x39
    "F_XAxis_Base+F_Ld_Accel_Val",      #  58 x3a
    "F_XAxis_Base+F_Ld_Accel_Count",    #  59 x3b
    "F_XAxis_Base+F_Rd_XPos",           #  60 x3c
    "F_XAxis_Base+F_Rd_YPos",           #  61 x3d
    "F_XAxis_Base+F_Rd_Sum",            #  62 x3e
    "F_XAxis_Base+F_Rd_Accel_Sum",      #  63 x3f
    "F_XAxis_Base+F_Rd_Accel_Ctr",      #  64 x40
    "F_XAxis_Base+F_Ld_Dist",           #  65 x41
    "F_XAxis_Base+F_Rd_Dist",           #  66 x42
    "F_XAxis_Base+F_Rd_Acl_Steps",      #  67 x43
    "F_XAxis_Base+F_Ld_Loc",            #  68 x44
    "F_XAxis_Base+F_Rd_Loc",            #  69 x45
    "F_XAxis_Base+F_Ld_Dro",            #  70 x46
    "F_XAxis_Base+F_Ld_Dro_End",        #  71 x47
    "F_XAxis_Base+F_Ld_Dro_Limit",      #  72 x48
    "F_XAxis_Base+F_Rd_Dro",            #  73 x49
    "F_XAxis_Base+F_Ld_Jog_Ctl",        #  74 x4a
    "F_XAxis_Base+F_Ld_Jog_Inc",        #  75 x4b
    "F_XAxis_Base+F_Ld_Jog_Back",       #  76 x4c
    "F_Spindle_Base+F_Ld_Sp_Ctl",       #  77 x4d
    "F_Spindle_Base+F_Ld_Sp_Freq",      #  78 x4e
    "F_Spindle_Base+F_Ld_D",            #  79 x4f
    "F_Spindle_Base+F_Ld_Incr1",        #  80 x50
    "F_Spindle_Base+F_Ld_Incr2",        #  81 x51
    "F_Spindle_Base+F_Ld_Accel_Val",    #  82 x52
    "F_Spindle_Base+F_Ld_Accel_Count",  #  83 x53
    "F_Spindle_Base+F_Rd_XPos",         #  84 x54
    "F_Spindle_Base+F_Rd_YPos",         #  85 x55
    "F_Spindle_Base+F_Rd_Sum",          #  86 x56
    "F_Spindle_Base+F_Rd_Accel_Sum",    #  87 x57
    "F_Spindle_Base+F_Rd_Accel_Ctr",    #  88 x58
    "F_Spindle_Base+F_Ld_Jog_Ctl",      #  89 x59
    "F_Spindle_Base+F_Ld_Jog_Inc",      #  90 x5a
    "F_Spindle_Base+F_Ld_Jog_Back",     #  91 x5b
    )

fpgaSizeTable = ( \
    1,              #   0 F_Noop
    4,              #   1 F_Rd_Status
    4,              #   2 F_Rd_Inputs
    1,              #   3 F_Ld_Run_Ctl
    1,              #   4 F_Ld_Sync_Ctl
    3,              #   5 F_Ld_Cfg_Ctl
    1,              #   6 F_Ld_Clk_Ctl
    1,              #   7 F_Ld_Dsp_Reg
    0,              #   8 F_Ctrl_Base, F_Ld_Ctrl_Data
    1,              #   9 F_Ctrl_Base, F_Ctrl_Cmd
    1,              #  10 F_Ctrl_Base, F_Ld_Seq
    4,              #  11 F_Ctrl_Base, F_Rd_Seq
    4,              #  12 F_Ctrl_Base, F_Rd_Ctr
    0,              #  13 F_Read_Base, F_Ld_Read_Data
    0,              #  14 F_Read_Base, F_Read
    2,              #  15 F_Dbg_Freq_Base, F_Ld_Dbg_Freq
    4,              #  16 F_Dbg_Freq_Base, F_Ld_Dbg_Count
    4,              #  17 F_Rd_Idx_Clks
    4,              #  18 F_PWM_Base, F_Ld_PWM_Max
    4,              #  18 F_PWM_Base, F_Ld_PWM_Trig
    2,              #  20 F_Enc_Base, F_Ld_Enc_Cycle
    2,              #  21 F_Enc_Base, F_Ld_Int_Cycle
    4,              #  22 F_Enc_Base, F_Rd_Cmp_Cyc_Clks
    2,              #  23 F_Phase_Base, F_Ld_Phase_Len
    4,              #  24 F_Phase_Base, F_Rd_Phase_Syn
    4,              #  25 F_ZAxis_Base, F_Rd_Axis_Status
    2,              #  26 F_ZAxis_Base, F_Ld_Axis_Ctl
    2,              #  27 F_ZAxis_Base, F_Rd_Axis_Ctl
    4,              #  28 F_ZAxis_Base, F_Ld_Freq
    4,              #  29 F_ZAxis_Base, F_Sync_Base, F_Ld_D
    4,              #  30 F_ZAxis_Base, F_Sync_Base, F_Ld_Incr1
    4,              #  31 F_ZAxis_Base, F_Sync_Base, F_Ld_Incr2
    4,              #  32 F_ZAxis_Base, F_Sync_Base, F_Ld_Accel_Val
    4,              #  33 F_ZAxis_Base, F_Sync_Base, F_Ld_Accel_Count
    4,              #  34 F_ZAxis_Base, F_Sync_Base, F_Rd_XPos
    4,              #  35 F_ZAxis_Base, F_Sync_Base, F_Rd_YPos
    4,              #  36 F_ZAxis_Base, F_Sync_Base, F_Rd_Sum
    4,              #  37 F_ZAxis_Base, F_Sync_Base, F_Rd_Accel_Sum
    4,              #  38 F_ZAxis_Base, F_Sync_Base, F_Rd_Accel_Ctr
    4,              #  39 F_ZAxis_Base, F_Dist_Base, F_Ld_Dist
    4,              #  40 F_ZAxis_Base, F_Dist_Base, F_Rd_Dist
    4,              #  41 F_ZAxis_Base, F_Dist_Base, F_Rd_Acl_Steps
    4,              #  42 F_ZAxis_Base, F_Loc_Base, F_Ld_Loc
    4,              #  43 F_ZAxis_Base, F_Loc_Base, F_Rd_Loc
    4,              #  44 F_ZAxis_Base, F_Dro_Base, F_Ld_Dro
    4,              #  45 F_ZAxis_Base, F_Dro_Base, F_Ld_Dro_End
    4,              #  46 F_ZAxis_Base, F_Dro_Base, F_Ld_Dro_Limit
    4,              #  47 F_ZAxis_Base, F_Dro_Base, F_Rd_Dro
    4,              #  48 F_ZAxis_Base, F_Jog_Base, F_Ld_Jog_Ctl
    4,              #  49 F_ZAxis_Base, F_Jog_Base, F_Ld_Jog_Inc
    4,              #  50 F_ZAxis_Base, F_Jog_Base, F_Ld_Jog_Back
    4,              #  51 F_XAxis_Base, F_Rd_Axis_Status
    2,              #  52 F_XAxis_Base, F_Ld_Axis_Ctl
    2,              #  53 F_XAxis_Base, F_Rd_Axis_Ctl
    4,              #  54 F_XAxis_Base, F_Ld_Freq
    4,              #  55 F_XAxis_Base, F_Sync_Base, F_Ld_D
    4,              #  56 F_XAxis_Base, F_Sync_Base, F_Ld_Incr1
    4,              #  57 F_XAxis_Base, F_Sync_Base, F_Ld_Incr2
    4,              #  58 F_XAxis_Base, F_Sync_Base, F_Ld_Accel_Val
    4,              #  59 F_XAxis_Base, F_Sync_Base, F_Ld_Accel_Count
    4,              #  60 F_XAxis_Base, F_Sync_Base, F_Rd_XPos
    4,              #  61 F_XAxis_Base, F_Sync_Base, F_Rd_YPos
    4,              #  62 F_XAxis_Base, F_Sync_Base, F_Rd_Sum
    4,              #  63 F_XAxis_Base, F_Sync_Base, F_Rd_Accel_Sum
    4,              #  64 F_XAxis_Base, F_Sync_Base, F_Rd_Accel_Ctr
    4,              #  65 F_XAxis_Base, F_Dist_Base, F_Ld_Dist
    4,              #  66 F_XAxis_Base, F_Dist_Base, F_Rd_Dist
    4,              #  67 F_XAxis_Base, F_Dist_Base, F_Rd_Acl_Steps
    4,              #  68 F_XAxis_Base, F_Loc_Base, F_Ld_Loc
    4,              #  69 F_XAxis_Base, F_Loc_Base, F_Rd_Loc
    4,              #  70 F_XAxis_Base, F_Dro_Base, F_Ld_Dro
    4,              #  71 F_XAxis_Base, F_Dro_Base, F_Ld_Dro_End
    4,              #  72 F_XAxis_Base, F_Dro_Base, F_Ld_Dro_Limit
    4,              #  73 F_XAxis_Base, F_Dro_Base, F_Rd_Dro
    4,              #  74 F_XAxis_Base, F_Jog_Base, F_Ld_Jog_Ctl
    4,              #  75 F_XAxis_Base, F_Jog_Base, F_Ld_Jog_Inc
    4,              #  76 F_XAxis_Base, F_Jog_Base, F_Ld_Jog_Back
    1,              #  77 F_Spindle_Base, F_Ld_Sp_Ctl
    4,              #  78 F_Spindle_Base, F_Ld_Sp_Freq
    4,              #  79 F_Spindle_Base, F_Sp_Sync_Base, F_Ld_D
    4,              #  80 F_Spindle_Base, F_Sp_Sync_Base, F_Ld_Incr1
    4,              #  81 F_Spindle_Base, F_Sp_Sync_Base, F_Ld_Incr2
    4,              #  82 F_Spindle_Base, F_Sp_Sync_Base, F_Ld_Accel_Val
    4,              #  83 F_Spindle_Base, F_Sp_Sync_Base, F_Ld_Accel_Count
    4,              #  84 F_Spindle_Base, F_Sp_Sync_Base, F_Rd_XPos
    4,              #  85 F_Spindle_Base, F_Sp_Sync_Base, F_Rd_YPos
    4,              #  86 F_Spindle_Base, F_Sp_Sync_Base, F_Rd_Sum
    4,              #  87 F_Spindle_Base, F_Sp_Sync_Base, F_Rd_Accel_Sum
    4,              #  88 F_Spindle_Base, F_Sp_Sync_Base, F_Rd_Accel_Ctr
    4,              #  89 F_Spindle_Base, F_Sp_Jog_Base, F_Ld_Jog_Ctl
    4,              #  90 F_Spindle_Base, F_Sp_Jog_Base, F_Ld_Jog_Inc
    4,              #  91 F_Spindle_Base, F_Sp_Jog_Base, F_Ld_Jog_Back
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
 F_Ld_Dro, \
 F_Ld_Dro_End, \
 F_Ld_Dro_Limit, \
 F_Rd_Dro, \
 F_Dro_Max, \
 F_Ld_Jog_Ctl, \
 F_Ld_Jog_Inc, \
 F_Ld_Jog_Back, \
 F_Jog_Max, \
 F_Rd_Axis_Status, \
 F_Ld_Axis_Ctl, \
 F_Rd_Axis_Ctl, \
 F_Ld_Freq, \
 F_Sync_Base, \
 F_Dist_Base, \
 F_Loc_Base, \
 F_Dro_Base, \
 F_Jog_Base, \
 F_Axis_Max, \
 F_Ld_Sp_Ctl, \
 F_Ld_Sp_Freq, \
 F_Sp_Sync_Base, \
 F_Sp_Jog_Base, \
 F_Noop, \
 F_Rd_Status, \
 F_Rd_Inputs, \
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
 F_Spindle_Base, \
 F_Cmd_Max, \
)
