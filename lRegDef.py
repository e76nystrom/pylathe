# fpga registers


# phase control

F_Ld_Phase_Len   =  0           # 'LLN' phase length
F_Rd_Phase_Syn   =  1           # 'RSY' read phase at sync pulse
F_Phase_Max      =  2           # number of phase registers

# controller

F_Ld_Ctrl_Data   =  0           # 'LCD' load controller data
F_Ctrl_Cmd       =  1           # 'CMD' controller command
F_Ld_Seq         =  2           # 'LSQ' load sequence
F_Rd_Seq         =  3           # 'RSQ' read sequence
F_Rd_Ctr         =  4           # 'RCT' read counter
F_Ctrl_Max       =  5           # number of controller registers

# reader

F_Ld_Read_Data   =  0           # 'LDR' load reader data
F_Read           =  1           # 'RD'  read data
F_Read_Max       =  2           # number of reader registers

# PWM

F_Ld_PWM_Max     =  0           # 'MAX' pwm counter maximum
F_Ld_PWM_Trig    =  0           # 'TRG' pwm trigger
F_PWM_Max        =  1           # number of pwm registers

# encoder

F_Ld_Enc_Cycle   =  0           # 'LEC' load encoder cycle
F_Ld_Int_Cycle   =  1           # 'LIC' load internal cycle
F_Rd_Cmp_Cyc_C   =  2           # 'RCC' read cmp cycle clocks
F_Enc_Max        =  3           # number of encoder registers

# debug frequency

F_Ld_Dbg_Freq    =  0           # 'DBF' debug frequency
F_Ld_Dbg_Count   =  1           # 'DBC' debug count
F_Dbg_Freq_Max   =  2           # number of debug frequency regs

# sync accel

F_Ld_D           =  0           # 'LD'  axis d
F_Ld_Incr1       =  1           # 'LI1' axis incr1
F_Ld_Incr2       =  2           # 'LI2' axis incr2
F_Ld_Accel_Val   =  3           # 'LAV' axis accel value
F_Ld_Accel_Count =  4           # 'LAC' axis accel count
F_Rd_XPos        =  5           # 'RX'  axis x pos
F_Rd_YPos        =  6           # 'RY'  axis y pos
F_Rd_Sum         =  7           # 'RSU' axis sum
F_Rd_Accel_Sum   =  8           # 'RAS' axis accel sum
F_Rd_Accel_Ctr   =  9           # 'RAC' axis accel counter
F_Ld_Dist        = 10           # 'LD'  axis distance
F_Ld_Max_Dist    = 11           # 'LMD' jog maximum distance
F_Ld_Backlash    = 12           # 'LB'  jog backlash
F_Rd_Dist        = 13           # 'RD'  read axis distance
F_Rd_Accel_Steps = 14           # 'RAS' read accel steps
F_Ld_Loc         = 15           # 'LL'  axis location
F_Rd_Loc         = 16           # 'RL'  read axis location
F_Ld_Mpg_Delta   = 17           # 'LMD' Mpg delta values
F_Ld_Mpg_Dist    = 18           # 'LMS' Mpg dist values
F_Ld_Mpg_Div     = 19           # 'LMV' Mpg div values
F_Ld_Dro         = 20           # 'LDR' axis dro
F_Ld_Dro_End     = 21           # 'LDE' axis dro end
F_Ld_Dro_Limit   = 22           # 'LDL' axis dro decel limit
F_Rd_Dro         = 23           # 'RDR' read axis dro
F_Sync_Max       = 24           # number of sync registers

# jog registers

F_Ld_Jog_Ctl     =  0           # 'CT' jog control
F_Ld_Jog_Inc     =  1           # 'IN' jog increment
F_Ld_Jog_Back    =  2           # 'JB' jog backlash increment
F_Jog_Max        =  3           # number of jog registers

# axis

F_Rd_Axis_Status =  0           # 'RAS' read axis status
F_Ld_Axis_Ctl    =  1           # 'LAC' set axis control reg
F_Rd_Axis_Ctl    =  2           # 'RAC' read axis control reg
F_Ld_Freq        =  3           # 'LFR' frequency
F_Sync_Base      =  4           # sync registers
F_Axis_Max       = 28           # num of axis regs

# spindle

F_Ld_Sp_Ctl      =  0           # 'LCT' spindle control reg
F_Ld_Sp_Freq     =  1           # 'LFR' freq for step spindle
F_Sp_Jog_Base    =  2           # 'J' spindle jog
F_Sp_Sync_Base   =  5           # spindle sync

# register definitions

F_Noop           =  0           # 'NO' reg 0

# status registers

F_Rd_Status      =  1           # 'RST' status reg
F_Rd_Inputs      =  2           # 'RIN' inputs reg

# control registers

F_Ld_Run_Ctl     =  3           # 'LRU' set run control reg
F_Rd_Run_Ctl     =  4           # 'RRU' read run control reg
F_Ld_Sync_Ctl    =  5           # 'LSY' sync control reg
F_Ld_Cfg_Ctl     =  6           # 'LCF' config control reg
F_Ld_Clk_Ctl     =  7           # 'LCL' clock control reg
F_Ld_Dsp_Reg     =  8           # 'LDS' display reg

# controller

F_Ctrl_Base      =  9           # 'C' controller

# reader

F_Read_Base      = 14           # 'R' reader

# debug frequency control

F_Dbg_Freq_Base  = 16           # 'D' dbg frequency

# spindle speed

F_Rd_Idx_Clks    = 18           # 'RIX' clocks per index

# step spindle frequency generator


# pwm

F_PWM_Base       = 19           # 'P' pwm control

# base for modules

F_Enc_Base       = 21           # 'E' encoder registers
F_Phase_Base     = 24           # 'H' phase registers
F_ZAxis_Base     = 26           # 'Z' z axis registers
F_XAxis_Base     = 54           # 'X' x axis registers
F_Spindle_Base   = 82           # 'S' spindle registers
F_Cmd_Max        = 111          # number of commands
# fpga table

xRegTable = ( \
    "F_Noop",                           #   0 x00
    "F_Rd_Status",                      #   1 x01
    "F_Rd_Inputs",                      #   2 x02
    "F_Ld_Run_Ctl",                     #   3 x03
    "F_Rd_Run_Ctl",                     #   4 x04
    "F_Ld_Sync_Ctl",                    #   5 x05
    "F_Ld_Cfg_Ctl",                     #   6 x06
    "F_Ld_Clk_Ctl",                     #   7 x07
    "F_Ld_Dsp_Reg",                     #   8 x08
    "F_Ctrl_Base+F_Ld_Ctrl_Data",       #   9 x09
    "F_Ctrl_Base+F_Ctrl_Cmd",           #  10 x0a
    "F_Ctrl_Base+F_Ld_Seq",             #  11 x0b
    "F_Ctrl_Base+F_Rd_Seq",             #  12 x0c
    "F_Ctrl_Base+F_Rd_Ctr",             #  13 x0d
    "F_Read_Base+F_Ld_Read_Data",       #  14 x0e
    "F_Read_Base+F_Read",               #  15 x0f
    "F_Dbg_Freq_Base+F_Ld_Dbg_Freq",    #  16 x10
    "F_Dbg_Freq_Base+F_Ld_Dbg_Count",   #  17 x11
    "F_Rd_Idx_Clks",                    #  18 x12
    "F_PWM_Base+F_Ld_PWM_Max",          #  19 x13
    "F_PWM_Base+F_Ld_PWM_Trig",         #  19 x13
    "F_Enc_Base+F_Ld_Enc_Cycle",        #  21 x15
    "F_Enc_Base+F_Ld_Int_Cycle",        #  22 x16
    "F_Enc_Base+F_Rd_Cmp_Cyc_C",        #  23 x17
    "F_Phase_Base+F_Ld_Phase_Len",      #  24 x18
    "F_Phase_Base+F_Rd_Phase_Syn",      #  25 x19
    "F_ZAxis_Base+F_Rd_Axis_Status",    #  26 x1a
    "F_ZAxis_Base+F_Ld_Axis_Ctl",       #  27 x1b
    "F_ZAxis_Base+F_Rd_Axis_Ctl",       #  28 x1c
    "F_ZAxis_Base+F_Ld_Freq",           #  29 x1d
    "F_ZAxis_Base+F_Ld_D",              #  30 x1e
    "F_ZAxis_Base+F_Ld_Incr1",          #  31 x1f
    "F_ZAxis_Base+F_Ld_Incr2",          #  32 x20
    "F_ZAxis_Base+F_Ld_Accel_Val",      #  33 x21
    "F_ZAxis_Base+F_Ld_Accel_Count",    #  34 x22
    "F_ZAxis_Base+F_Rd_XPos",           #  35 x23
    "F_ZAxis_Base+F_Rd_YPos",           #  36 x24
    "F_ZAxis_Base+F_Rd_Sum",            #  37 x25
    "F_ZAxis_Base+F_Rd_Accel_Sum",      #  38 x26
    "F_ZAxis_Base+F_Rd_Accel_Ctr",      #  39 x27
    "F_ZAxis_Base+F_Ld_Dist",           #  40 x28
    "F_ZAxis_Base+F_Ld_Max_Dist",       #  41 x29
    "F_ZAxis_Base+F_Ld_Backlash",       #  42 x2a
    "F_ZAxis_Base+F_Rd_Dist",           #  43 x2b
    "F_ZAxis_Base+F_Rd_Accel_Steps",    #  44 x2c
    "F_ZAxis_Base+F_Ld_Loc",            #  45 x2d
    "F_ZAxis_Base+F_Rd_Loc",            #  46 x2e
    "F_ZAxis_Base+F_Ld_Mpg_Delta",      #  47 x2f
    "F_ZAxis_Base+F_Ld_Mpg_Dist",       #  48 x30
    "F_ZAxis_Base+F_Ld_Mpg_Div",        #  49 x31
    "F_ZAxis_Base+F_Ld_Dro",            #  50 x32
    "F_ZAxis_Base+F_Ld_Dro_End",        #  51 x33
    "F_ZAxis_Base+F_Ld_Dro_Limit",      #  52 x34
    "F_ZAxis_Base+F_Rd_Dro",            #  53 x35
    "F_XAxis_Base+F_Rd_Axis_Status",    #  54 x36
    "F_XAxis_Base+F_Ld_Axis_Ctl",       #  55 x37
    "F_XAxis_Base+F_Rd_Axis_Ctl",       #  56 x38
    "F_XAxis_Base+F_Ld_Freq",           #  57 x39
    "F_XAxis_Base+F_Ld_D",              #  58 x3a
    "F_XAxis_Base+F_Ld_Incr1",          #  59 x3b
    "F_XAxis_Base+F_Ld_Incr2",          #  60 x3c
    "F_XAxis_Base+F_Ld_Accel_Val",      #  61 x3d
    "F_XAxis_Base+F_Ld_Accel_Count",    #  62 x3e
    "F_XAxis_Base+F_Rd_XPos",           #  63 x3f
    "F_XAxis_Base+F_Rd_YPos",           #  64 x40
    "F_XAxis_Base+F_Rd_Sum",            #  65 x41
    "F_XAxis_Base+F_Rd_Accel_Sum",      #  66 x42
    "F_XAxis_Base+F_Rd_Accel_Ctr",      #  67 x43
    "F_XAxis_Base+F_Ld_Dist",           #  68 x44
    "F_XAxis_Base+F_Ld_Max_Dist",       #  69 x45
    "F_XAxis_Base+F_Ld_Backlash",       #  70 x46
    "F_XAxis_Base+F_Rd_Dist",           #  71 x47
    "F_XAxis_Base+F_Rd_Accel_Steps",    #  72 x48
    "F_XAxis_Base+F_Ld_Loc",            #  73 x49
    "F_XAxis_Base+F_Rd_Loc",            #  74 x4a
    "F_XAxis_Base+F_Ld_Mpg_Delta",      #  75 x4b
    "F_XAxis_Base+F_Ld_Mpg_Dist",       #  76 x4c
    "F_XAxis_Base+F_Ld_Mpg_Div",        #  77 x4d
    "F_XAxis_Base+F_Ld_Dro",            #  78 x4e
    "F_XAxis_Base+F_Ld_Dro_End",        #  79 x4f
    "F_XAxis_Base+F_Ld_Dro_Limit",      #  80 x50
    "F_XAxis_Base+F_Rd_Dro",            #  81 x51
    "F_Spindle_Base+F_Ld_Sp_Ctl",       #  82 x52
    "F_Spindle_Base+F_Ld_Sp_Freq",      #  83 x53
    "F_Spindle_Base+F_Ld_Jog_Ctl",      #  84 x54
    "F_Spindle_Base+F_Ld_Jog_Inc",      #  85 x55
    "F_Spindle_Base+F_Ld_Jog_Back",     #  86 x56
    "F_Spindle_Base+F_Ld_D",            #  87 x57
    "F_Spindle_Base+F_Ld_Incr1",        #  88 x58
    "F_Spindle_Base+F_Ld_Incr2",        #  89 x59
    "F_Spindle_Base+F_Ld_Accel_Val",    #  90 x5a
    "F_Spindle_Base+F_Ld_Accel_Count",  #  91 x5b
    "F_Spindle_Base+F_Rd_XPos",         #  92 x5c
    "F_Spindle_Base+F_Rd_YPos",         #  93 x5d
    "F_Spindle_Base+F_Rd_Sum",          #  94 x5e
    "F_Spindle_Base+F_Rd_Accel_Sum",    #  95 x5f
    "F_Spindle_Base+F_Rd_Accel_Ctr",    #  96 x60
    "F_Spindle_Base+F_Ld_Dist",         #  97 x61
    "F_Spindle_Base+F_Ld_Max_Dist",     #  98 x62
    "F_Spindle_Base+F_Ld_Backlash",     #  99 x63
    "F_Spindle_Base+F_Rd_Dist",         # 100 x64
    "F_Spindle_Base+F_Rd_Accel_Steps",  # 101 x65
    "F_Spindle_Base+F_Ld_Loc",          # 102 x66
    "F_Spindle_Base+F_Rd_Loc",          # 103 x67
    "F_Spindle_Base+F_Ld_Mpg_Delta",    # 104 x68
    "F_Spindle_Base+F_Ld_Mpg_Dist",     # 105 x69
    "F_Spindle_Base+F_Ld_Mpg_Div",      # 106 x6a
    "F_Spindle_Base+F_Ld_Dro",          # 107 x6b
    "F_Spindle_Base+F_Ld_Dro_End",      # 108 x6c
    "F_Spindle_Base+F_Ld_Dro_Limit",    # 109 x6d
    "F_Spindle_Base+F_Rd_Dro",          # 110 x6e
    )

fpgaSizeTable = ( \
    1,              #   0 F_Noop
    4,              #   1 F_Rd_Status
    4,              #   2 F_Rd_Inputs
    1,              #   3 F_Ld_Run_Ctl
    1,              #   4 F_Rd_Run_Ctl
    1,              #   5 F_Ld_Sync_Ctl
    3,              #   6 F_Ld_Cfg_Ctl
    1,              #   7 F_Ld_Clk_Ctl
    1,              #   8 F_Ld_Dsp_Reg
    0,              #   9 F_Ctrl_Base, F_Ld_Ctrl_Data
    1,              #  10 F_Ctrl_Base, F_Ctrl_Cmd
    1,              #  11 F_Ctrl_Base, F_Ld_Seq
    4,              #  12 F_Ctrl_Base, F_Rd_Seq
    4,              #  13 F_Ctrl_Base, F_Rd_Ctr
    0,              #  14 F_Read_Base, F_Ld_Read_Data
    0,              #  15 F_Read_Base, F_Read
    2,              #  16 F_Dbg_Freq_Base, F_Ld_Dbg_Freq
    4,              #  17 F_Dbg_Freq_Base, F_Ld_Dbg_Count
    4,              #  18 F_Rd_Idx_Clks
    4,              #  19 F_PWM_Base, F_Ld_PWM_Max
    4,              #  19 F_PWM_Base, F_Ld_PWM_Trig
    2,              #  21 F_Enc_Base, F_Ld_Enc_Cycle
    2,              #  22 F_Enc_Base, F_Ld_Int_Cycle
    4,              #  23 F_Enc_Base, F_Rd_Cmp_Cyc_C
    2,              #  24 F_Phase_Base, F_Ld_Phase_Len
    4,              #  25 F_Phase_Base, F_Rd_Phase_Syn
    1,              #  26 F_ZAxis_Base, F_Rd_Axis_Status
    2,              #  27 F_ZAxis_Base, F_Ld_Axis_Ctl
    2,              #  28 F_ZAxis_Base, F_Rd_Axis_Ctl
    4,              #  29 F_ZAxis_Base, F_Ld_Freq
    4,              #  30 F_ZAxis_Base, F_Sync_Base, F_Ld_D
    4,              #  31 F_ZAxis_Base, F_Sync_Base, F_Ld_Incr1
    4,              #  32 F_ZAxis_Base, F_Sync_Base, F_Ld_Incr2
    4,              #  33 F_ZAxis_Base, F_Sync_Base, F_Ld_Accel_Val
    4,              #  34 F_ZAxis_Base, F_Sync_Base, F_Ld_Accel_Count
    4,              #  35 F_ZAxis_Base, F_Sync_Base, F_Rd_XPos
    4,              #  36 F_ZAxis_Base, F_Sync_Base, F_Rd_YPos
    4,              #  37 F_ZAxis_Base, F_Sync_Base, F_Rd_Sum
    4,              #  38 F_ZAxis_Base, F_Sync_Base, F_Rd_Accel_Sum
    4,              #  39 F_ZAxis_Base, F_Sync_Base, F_Rd_Accel_Ctr
    4,              #  40 F_ZAxis_Base, F_Sync_Base, F_Ld_Dist
    4,              #  41 F_ZAxis_Base, F_Sync_Base, F_Ld_Max_Dist
    4,              #  42 F_ZAxis_Base, F_Sync_Base, F_Ld_Backlash
    4,              #  43 F_ZAxis_Base, F_Sync_Base, F_Rd_Dist
    4,              #  44 F_ZAxis_Base, F_Sync_Base, F_Rd_Accel_Steps
    4,              #  45 F_ZAxis_Base, F_Sync_Base, F_Ld_Loc
    4,              #  46 F_ZAxis_Base, F_Sync_Base, F_Rd_Loc
    4,              #  47 F_ZAxis_Base, F_Sync_Base, F_Ld_Mpg_Delta
    4,              #  48 F_ZAxis_Base, F_Sync_Base, F_Ld_Mpg_Dist
    4,              #  49 F_ZAxis_Base, F_Sync_Base, F_Ld_Mpg_Div
    4,              #  50 F_ZAxis_Base, F_Sync_Base, F_Ld_Dro
    4,              #  51 F_ZAxis_Base, F_Sync_Base, F_Ld_Dro_End
    4,              #  52 F_ZAxis_Base, F_Sync_Base, F_Ld_Dro_Limit
    4,              #  53 F_ZAxis_Base, F_Sync_Base, F_Rd_Dro
    1,              #  54 F_XAxis_Base, F_Rd_Axis_Status
    2,              #  55 F_XAxis_Base, F_Ld_Axis_Ctl
    2,              #  56 F_XAxis_Base, F_Rd_Axis_Ctl
    4,              #  57 F_XAxis_Base, F_Ld_Freq
    4,              #  58 F_XAxis_Base, F_Sync_Base, F_Ld_D
    4,              #  59 F_XAxis_Base, F_Sync_Base, F_Ld_Incr1
    4,              #  60 F_XAxis_Base, F_Sync_Base, F_Ld_Incr2
    4,              #  61 F_XAxis_Base, F_Sync_Base, F_Ld_Accel_Val
    4,              #  62 F_XAxis_Base, F_Sync_Base, F_Ld_Accel_Count
    4,              #  63 F_XAxis_Base, F_Sync_Base, F_Rd_XPos
    4,              #  64 F_XAxis_Base, F_Sync_Base, F_Rd_YPos
    4,              #  65 F_XAxis_Base, F_Sync_Base, F_Rd_Sum
    4,              #  66 F_XAxis_Base, F_Sync_Base, F_Rd_Accel_Sum
    4,              #  67 F_XAxis_Base, F_Sync_Base, F_Rd_Accel_Ctr
    4,              #  68 F_XAxis_Base, F_Sync_Base, F_Ld_Dist
    4,              #  69 F_XAxis_Base, F_Sync_Base, F_Ld_Max_Dist
    4,              #  70 F_XAxis_Base, F_Sync_Base, F_Ld_Backlash
    4,              #  71 F_XAxis_Base, F_Sync_Base, F_Rd_Dist
    4,              #  72 F_XAxis_Base, F_Sync_Base, F_Rd_Accel_Steps
    4,              #  73 F_XAxis_Base, F_Sync_Base, F_Ld_Loc
    4,              #  74 F_XAxis_Base, F_Sync_Base, F_Rd_Loc
    4,              #  75 F_XAxis_Base, F_Sync_Base, F_Ld_Mpg_Delta
    4,              #  76 F_XAxis_Base, F_Sync_Base, F_Ld_Mpg_Dist
    4,              #  77 F_XAxis_Base, F_Sync_Base, F_Ld_Mpg_Div
    4,              #  78 F_XAxis_Base, F_Sync_Base, F_Ld_Dro
    4,              #  79 F_XAxis_Base, F_Sync_Base, F_Ld_Dro_End
    4,              #  80 F_XAxis_Base, F_Sync_Base, F_Ld_Dro_Limit
    4,              #  81 F_XAxis_Base, F_Sync_Base, F_Rd_Dro
    1,              #  82 F_Spindle_Base, F_Ld_Sp_Ctl
    4,              #  83 F_Spindle_Base, F_Ld_Sp_Freq
    4,              #  84 F_Spindle_Base, F_Sp_Jog_Base, F_Ld_Jog_Ctl
    4,              #  85 F_Spindle_Base, F_Sp_Jog_Base, F_Ld_Jog_Inc
    4,              #  86 F_Spindle_Base, F_Sp_Jog_Base, F_Ld_Jog_Back
    4,              #  87 F_Spindle_Base, F_Sp_Sync_Base, F_Ld_D
    4,              #  88 F_Spindle_Base, F_Sp_Sync_Base, F_Ld_Incr1
    4,              #  89 F_Spindle_Base, F_Sp_Sync_Base, F_Ld_Incr2
    4,              #  90 F_Spindle_Base, F_Sp_Sync_Base, F_Ld_Accel_Val
    4,              #  91 F_Spindle_Base, F_Sp_Sync_Base, F_Ld_Accel_Count
    4,              #  92 F_Spindle_Base, F_Sp_Sync_Base, F_Rd_XPos
    4,              #  93 F_Spindle_Base, F_Sp_Sync_Base, F_Rd_YPos
    4,              #  94 F_Spindle_Base, F_Sp_Sync_Base, F_Rd_Sum
    4,              #  95 F_Spindle_Base, F_Sp_Sync_Base, F_Rd_Accel_Sum
    4,              #  96 F_Spindle_Base, F_Sp_Sync_Base, F_Rd_Accel_Ctr
    4,              #  97 F_Spindle_Base, F_Sp_Sync_Base, F_Ld_Dist
    4,              #  98 F_Spindle_Base, F_Sp_Sync_Base, F_Ld_Max_Dist
    4,              #  99 F_Spindle_Base, F_Sp_Sync_Base, F_Ld_Backlash
    4,              # 100 F_Spindle_Base, F_Sp_Sync_Base, F_Rd_Dist
    4,              # 101 F_Spindle_Base, F_Sp_Sync_Base, F_Rd_Accel_Steps
    4,              # 102 F_Spindle_Base, F_Sp_Sync_Base, F_Ld_Loc
    4,              # 103 F_Spindle_Base, F_Sp_Sync_Base, F_Rd_Loc
    4,              # 104 F_Spindle_Base, F_Sp_Sync_Base, F_Ld_Mpg_Delta
    4,              # 105 F_Spindle_Base, F_Sp_Sync_Base, F_Ld_Mpg_Dist
    4,              # 106 F_Spindle_Base, F_Sp_Sync_Base, F_Ld_Mpg_Div
    4,              # 107 F_Spindle_Base, F_Sp_Sync_Base, F_Ld_Dro
    4,              # 108 F_Spindle_Base, F_Sp_Sync_Base, F_Ld_Dro_End
    4,              # 109 F_Spindle_Base, F_Sp_Sync_Base, F_Ld_Dro_Limit
    4,              # 110 F_Spindle_Base, F_Sp_Sync_Base, F_Rd_Dro
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
 F_Rd_Cmp_Cyc_C, \
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
 F_Ld_Dist, \
 F_Ld_Max_Dist, \
 F_Ld_Backlash, \
 F_Rd_Dist, \
 F_Rd_Accel_Steps, \
 F_Ld_Loc, \
 F_Rd_Loc, \
 F_Ld_Mpg_Delta, \
 F_Ld_Mpg_Dist, \
 F_Ld_Mpg_Div, \
 F_Ld_Dro, \
 F_Ld_Dro_End, \
 F_Ld_Dro_Limit, \
 F_Rd_Dro, \
 F_Sync_Max, \
 F_Ld_Jog_Ctl, \
 F_Ld_Jog_Inc, \
 F_Ld_Jog_Back, \
 F_Jog_Max, \
 F_Rd_Axis_Status, \
 F_Ld_Axis_Ctl, \
 F_Rd_Axis_Ctl, \
 F_Ld_Freq, \
 F_Sync_Base, \
 F_Axis_Max, \
 F_Ld_Sp_Ctl, \
 F_Ld_Sp_Freq, \
 F_Sp_Jog_Base, \
 F_Sp_Sync_Base, \
 F_Noop, \
 F_Rd_Status, \
 F_Rd_Inputs, \
 F_Ld_Run_Ctl, \
 F_Rd_Run_Ctl, \
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
