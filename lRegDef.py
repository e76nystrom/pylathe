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
F_Ld_PWM_Trig    =  1           # 'TRG' pwm trigger
F_PWM_Max        =  2           # number of pwm registers

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

F_Ld_D           =  0           # 'LIS' axis initial sum
F_Ld_Incr1       =  1           # 'LI1' axis incr1
F_Ld_Incr2       =  2           # 'LI2' axis incr2
F_Ld_Accel_Val   =  3           # 'LAV' axis accel value
F_Ld_Accel_Count =  4           # 'LAC' axis accel count
F_Rd_XPos        =  5           # 'RX'  axis x pos
F_Rd_YPos        =  6           # 'RY'  axis y pos
F_Rd_Sum         =  7           # 'RSU' axis sum
F_Rd_Accel_Sum   =  8           # 'RAS' axis accel sum
F_Rd_Accel_Ctr   =  9           # 'RAC' axis accel counter
F_Ld_Dist        = 10           # 'LDS' axis distance
F_Ld_Max_Dist    = 11           # 'LMD' jog maximum distance
F_Rd_Dist        = 12           # 'RDS' read axis distance
F_Rd_Accel_Steps = 13           # 'RAS' read accel steps
F_Ld_Loc         = 14           # 'LLC' axis location
F_Rd_Loc         = 15           # 'RLC' read axis location
F_Ld_Dro         = 16           # 'LDR' axis dro
F_Ld_Dro_End     = 17           # 'LDE' axis dro end
F_Ld_Dro_Limit   = 18           # 'LDL' axis dro decel limit
F_Rd_Dro         = 19           # 'RDR' read axis dro
F_Sync_Max       = 20           # number of sync registers

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
F_Axis_Max       = 24           # num of axis regs

# spindle

F_Ld_Sp_Ctl      =  0           # 'LCT' spindle control reg
F_Ld_Sp_Freq     =  1           # 'LFR' freq for step spindle
F_Sp_Jog_Base    =  2           # 'J' spindle jog
F_Sp_Sync_Base   =  5           # spindle sync

# register definitions

F_Noop           =  0           # 'NO' reg 0

# status registers

F_Rd_Status      =  1           # 'RSTS' status reg
F_Rd_Inputs      =  2           # 'RINP' inputs reg

# control registers

F_Ld_Run_Ctl     =  3           # 'LRUN' set run control reg
F_Rd_Run_Ctl     =  4           # 'RRUN' read run control reg
F_Ld_Sync_Ctl    =  5           # 'LSYN' sync control reg
F_Ld_Cfg_Ctl     =  6           # 'LCFG' config control reg
F_Ld_Clk_Ctl     =  7           # 'LCLK' clock control reg
F_Ld_Out_Reg     =  8           # 'LDOU' output reg
F_Ld_Dsp_Reg     =  9           # 'LDSP' display reg

# controller

F_Ctrl_Base      = 10           # 'C' controller

# reader

F_Read_Base      = 15           # 'R' reader

# debug frequency control

F_Dbg_Freq_Base  = 17           # 'D' dbg frequency

# spindle speed

F_Rd_Idx_Clks    = 19           # 'RIDX' clocks per index

# step spindle frequency generator


# pwm

F_PWM_Base       = 20           # 'P' pwm control

# base for modules

F_Enc_Base       = 22           # 'E' encoder registers
F_Phase_Base     = 25           # 'H' phase registers
F_ZAxis_Base     = 27           # 'Z' z axis registers
F_XAxis_Base     = 51           # 'X' x axis registers
F_Spindle_Base   = 75           # 'S' spindle registers
F_Cmd_Max        = 100          # number of commands
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
    "F_Ld_Out_Reg",                     #   8 x08
    "F_Ld_Dsp_Reg",                     #   9 x09
    "F_Ctrl_Base+F_Ld_Ctrl_Data",       #  10 x0a
    "F_Ctrl_Base+F_Ctrl_Cmd",           #  11 x0b
    "F_Ctrl_Base+F_Ld_Seq",             #  12 x0c
    "F_Ctrl_Base+F_Rd_Seq",             #  13 x0d
    "F_Ctrl_Base+F_Rd_Ctr",             #  14 x0e
    "F_Read_Base+F_Ld_Read_Data",       #  15 x0f
    "F_Read_Base+F_Read",               #  16 x10
    "F_Dbg_Freq_Base+F_Ld_Dbg_Freq",    #  17 x11
    "F_Dbg_Freq_Base+F_Ld_Dbg_Count",   #  18 x12
    "F_Rd_Idx_Clks",                    #  19 x13
    "F_PWM_Base+F_Ld_PWM_Max",          #  20 x14
    "F_PWM_Base+F_Ld_PWM_Trig",         #  21 x15
    "F_Enc_Base+F_Ld_Enc_Cycle",        #  22 x16
    "F_Enc_Base+F_Ld_Int_Cycle",        #  23 x17
    "F_Enc_Base+F_Rd_Cmp_Cyc_C",        #  24 x18
    "F_Phase_Base+F_Ld_Phase_Len",      #  25 x19
    "F_Phase_Base+F_Rd_Phase_Syn",      #  26 x1a
    "F_ZAxis_Base+F_Rd_Axis_Status",    #  27 x1b
    "F_ZAxis_Base+F_Ld_Axis_Ctl",       #  28 x1c
    "F_ZAxis_Base+F_Rd_Axis_Ctl",       #  29 x1d
    "F_ZAxis_Base+F_Ld_Freq",           #  30 x1e
    "F_ZAxis_Base+F_Ld_D",              #  31 x1f
    "F_ZAxis_Base+F_Ld_Incr1",          #  32 x20
    "F_ZAxis_Base+F_Ld_Incr2",          #  33 x21
    "F_ZAxis_Base+F_Ld_Accel_Val",      #  34 x22
    "F_ZAxis_Base+F_Ld_Accel_Count",    #  35 x23
    "F_ZAxis_Base+F_Rd_XPos",           #  36 x24
    "F_ZAxis_Base+F_Rd_YPos",           #  37 x25
    "F_ZAxis_Base+F_Rd_Sum",            #  38 x26
    "F_ZAxis_Base+F_Rd_Accel_Sum",      #  39 x27
    "F_ZAxis_Base+F_Rd_Accel_Ctr",      #  40 x28
    "F_ZAxis_Base+F_Ld_Dist",           #  41 x29
    "F_ZAxis_Base+F_Ld_Max_Dist",       #  42 x2a
    "F_ZAxis_Base+F_Rd_Dist",           #  43 x2b
    "F_ZAxis_Base+F_Rd_Accel_Steps",    #  44 x2c
    "F_ZAxis_Base+F_Ld_Loc",            #  45 x2d
    "F_ZAxis_Base+F_Rd_Loc",            #  46 x2e
    "F_ZAxis_Base+F_Ld_Dro",            #  47 x2f
    "F_ZAxis_Base+F_Ld_Dro_End",        #  48 x30
    "F_ZAxis_Base+F_Ld_Dro_Limit",      #  49 x31
    "F_ZAxis_Base+F_Rd_Dro",            #  50 x32
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
    "F_XAxis_Base+F_Ld_Max_Dist",       #  66 x42
    "F_XAxis_Base+F_Rd_Dist",           #  67 x43
    "F_XAxis_Base+F_Rd_Accel_Steps",    #  68 x44
    "F_XAxis_Base+F_Ld_Loc",            #  69 x45
    "F_XAxis_Base+F_Rd_Loc",            #  70 x46
    "F_XAxis_Base+F_Ld_Dro",            #  71 x47
    "F_XAxis_Base+F_Ld_Dro_End",        #  72 x48
    "F_XAxis_Base+F_Ld_Dro_Limit",      #  73 x49
    "F_XAxis_Base+F_Rd_Dro",            #  74 x4a
    "F_Spindle_Base+F_Ld_Sp_Ctl",       #  75 x4b
    "F_Spindle_Base+F_Ld_Sp_Freq",      #  76 x4c
    "F_Spindle_Base+F_Ld_Jog_Ctl",      #  77 x4d
    "F_Spindle_Base+F_Ld_Jog_Inc",      #  78 x4e
    "F_Spindle_Base+F_Ld_Jog_Back",     #  79 x4f
    "F_Spindle_Base+F_Ld_D",            #  80 x50
    "F_Spindle_Base+F_Ld_Incr1",        #  81 x51
    "F_Spindle_Base+F_Ld_Incr2",        #  82 x52
    "F_Spindle_Base+F_Ld_Accel_Val",    #  83 x53
    "F_Spindle_Base+F_Ld_Accel_Count",  #  84 x54
    "F_Spindle_Base+F_Rd_XPos",         #  85 x55
    "F_Spindle_Base+F_Rd_YPos",         #  86 x56
    "F_Spindle_Base+F_Rd_Sum",          #  87 x57
    "F_Spindle_Base+F_Rd_Accel_Sum",    #  88 x58
    "F_Spindle_Base+F_Rd_Accel_Ctr",    #  89 x59
    "F_Spindle_Base+F_Ld_Dist",         #  90 x5a
    "F_Spindle_Base+F_Ld_Max_Dist",     #  91 x5b
    "F_Spindle_Base+F_Rd_Dist",         #  92 x5c
    "F_Spindle_Base+F_Rd_Accel_Steps",  #  93 x5d
    "F_Spindle_Base+F_Ld_Loc",          #  94 x5e
    "F_Spindle_Base+F_Rd_Loc",          #  95 x5f
    "F_Spindle_Base+F_Ld_Dro",          #  96 x60
    "F_Spindle_Base+F_Ld_Dro_End",      #  97 x61
    "F_Spindle_Base+F_Ld_Dro_Limit",    #  98 x62
    "F_Spindle_Base+F_Rd_Dro",          #  99 x63
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
    1,              #   8 F_Ld_Out_Reg
    1,              #   9 F_Ld_Dsp_Reg
    0,              #  10 F_Ctrl_Base, F_Ld_Ctrl_Data
    1,              #  11 F_Ctrl_Base, F_Ctrl_Cmd
    1,              #  12 F_Ctrl_Base, F_Ld_Seq
    4,              #  13 F_Ctrl_Base, F_Rd_Seq
    4,              #  14 F_Ctrl_Base, F_Rd_Ctr
    0,              #  15 F_Read_Base, F_Ld_Read_Data
    0,              #  16 F_Read_Base, F_Read
    2,              #  17 F_Dbg_Freq_Base, F_Ld_Dbg_Freq
    4,              #  18 F_Dbg_Freq_Base, F_Ld_Dbg_Count
    4,              #  19 F_Rd_Idx_Clks
    4,              #  20 F_PWM_Base, F_Ld_PWM_Max
    4,              #  21 F_PWM_Base, F_Ld_PWM_Trig
    2,              #  22 F_Enc_Base, F_Ld_Enc_Cycle
    2,              #  23 F_Enc_Base, F_Ld_Int_Cycle
    4,              #  24 F_Enc_Base, F_Rd_Cmp_Cyc_C
    2,              #  25 F_Phase_Base, F_Ld_Phase_Len
    4,              #  26 F_Phase_Base, F_Rd_Phase_Syn
    1,              #  27 F_ZAxis_Base, F_Rd_Axis_Status
    2,              #  28 F_ZAxis_Base, F_Ld_Axis_Ctl
    2,              #  29 F_ZAxis_Base, F_Rd_Axis_Ctl
    4,              #  30 F_ZAxis_Base, F_Ld_Freq
    4,              #  31 F_ZAxis_Base, F_Sync_Base, F_Ld_D
    4,              #  32 F_ZAxis_Base, F_Sync_Base, F_Ld_Incr1
    4,              #  33 F_ZAxis_Base, F_Sync_Base, F_Ld_Incr2
    4,              #  34 F_ZAxis_Base, F_Sync_Base, F_Ld_Accel_Val
    4,              #  35 F_ZAxis_Base, F_Sync_Base, F_Ld_Accel_Count
    4,              #  36 F_ZAxis_Base, F_Sync_Base, F_Rd_XPos
    4,              #  37 F_ZAxis_Base, F_Sync_Base, F_Rd_YPos
    4,              #  38 F_ZAxis_Base, F_Sync_Base, F_Rd_Sum
    4,              #  39 F_ZAxis_Base, F_Sync_Base, F_Rd_Accel_Sum
    4,              #  40 F_ZAxis_Base, F_Sync_Base, F_Rd_Accel_Ctr
    4,              #  41 F_ZAxis_Base, F_Sync_Base, F_Ld_Dist
    4,              #  42 F_ZAxis_Base, F_Sync_Base, F_Ld_Max_Dist
    4,              #  43 F_ZAxis_Base, F_Sync_Base, F_Rd_Dist
    4,              #  44 F_ZAxis_Base, F_Sync_Base, F_Rd_Accel_Steps
    4,              #  45 F_ZAxis_Base, F_Sync_Base, F_Ld_Loc
    4,              #  46 F_ZAxis_Base, F_Sync_Base, F_Rd_Loc
    4,              #  47 F_ZAxis_Base, F_Sync_Base, F_Ld_Dro
    4,              #  48 F_ZAxis_Base, F_Sync_Base, F_Ld_Dro_End
    4,              #  49 F_ZAxis_Base, F_Sync_Base, F_Ld_Dro_Limit
    4,              #  50 F_ZAxis_Base, F_Sync_Base, F_Rd_Dro
    1,              #  51 F_XAxis_Base, F_Rd_Axis_Status
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
    4,              #  65 F_XAxis_Base, F_Sync_Base, F_Ld_Dist
    4,              #  66 F_XAxis_Base, F_Sync_Base, F_Ld_Max_Dist
    4,              #  67 F_XAxis_Base, F_Sync_Base, F_Rd_Dist
    4,              #  68 F_XAxis_Base, F_Sync_Base, F_Rd_Accel_Steps
    4,              #  69 F_XAxis_Base, F_Sync_Base, F_Ld_Loc
    4,              #  70 F_XAxis_Base, F_Sync_Base, F_Rd_Loc
    4,              #  71 F_XAxis_Base, F_Sync_Base, F_Ld_Dro
    4,              #  72 F_XAxis_Base, F_Sync_Base, F_Ld_Dro_End
    4,              #  73 F_XAxis_Base, F_Sync_Base, F_Ld_Dro_Limit
    4,              #  74 F_XAxis_Base, F_Sync_Base, F_Rd_Dro
    1,              #  75 F_Spindle_Base, F_Ld_Sp_Ctl
    4,              #  76 F_Spindle_Base, F_Ld_Sp_Freq
    4,              #  77 F_Spindle_Base, F_Sp_Jog_Base, F_Ld_Jog_Ctl
    4,              #  78 F_Spindle_Base, F_Sp_Jog_Base, F_Ld_Jog_Inc
    4,              #  79 F_Spindle_Base, F_Sp_Jog_Base, F_Ld_Jog_Back
    4,              #  80 F_Spindle_Base, F_Sp_Sync_Base, F_Ld_D
    4,              #  81 F_Spindle_Base, F_Sp_Sync_Base, F_Ld_Incr1
    4,              #  82 F_Spindle_Base, F_Sp_Sync_Base, F_Ld_Incr2
    4,              #  83 F_Spindle_Base, F_Sp_Sync_Base, F_Ld_Accel_Val
    4,              #  84 F_Spindle_Base, F_Sp_Sync_Base, F_Ld_Accel_Count
    4,              #  85 F_Spindle_Base, F_Sp_Sync_Base, F_Rd_XPos
    4,              #  86 F_Spindle_Base, F_Sp_Sync_Base, F_Rd_YPos
    4,              #  87 F_Spindle_Base, F_Sp_Sync_Base, F_Rd_Sum
    4,              #  88 F_Spindle_Base, F_Sp_Sync_Base, F_Rd_Accel_Sum
    4,              #  89 F_Spindle_Base, F_Sp_Sync_Base, F_Rd_Accel_Ctr
    4,              #  90 F_Spindle_Base, F_Sp_Sync_Base, F_Ld_Dist
    4,              #  91 F_Spindle_Base, F_Sp_Sync_Base, F_Ld_Max_Dist
    4,              #  92 F_Spindle_Base, F_Sp_Sync_Base, F_Rd_Dist
    4,              #  93 F_Spindle_Base, F_Sp_Sync_Base, F_Rd_Accel_Steps
    4,              #  94 F_Spindle_Base, F_Sp_Sync_Base, F_Ld_Loc
    4,              #  95 F_Spindle_Base, F_Sp_Sync_Base, F_Rd_Loc
    4,              #  96 F_Spindle_Base, F_Sp_Sync_Base, F_Ld_Dro
    4,              #  97 F_Spindle_Base, F_Sp_Sync_Base, F_Ld_Dro_End
    4,              #  98 F_Spindle_Base, F_Sp_Sync_Base, F_Ld_Dro_Limit
    4,              #  99 F_Spindle_Base, F_Sp_Sync_Base, F_Rd_Dro
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
 F_Rd_Dist, \
 F_Rd_Accel_Steps, \
 F_Ld_Loc, \
 F_Rd_Loc, \
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
 F_Ld_Out_Reg, \
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
