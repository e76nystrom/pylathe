# fpga registers


# phase control

F_Ld_Phase_Len   =  0           # 'LLN' phase length
F_Rd_Phase_Syn   =  1           # 'RSY' read phase at sync pulse
F_Phase_Max      =  2           # number of phase registers

# PWM

F_Ld_PWM_Max     =  0           # 'MAX' pwm counter maximum
F_Ld_PWM_Trig    =  1           # 'TRG' pwm trigger
F_PWM_Max        =  2           # number of pwm registers

# encoder

F_Ld_Enc_Prescale =  0          # 'EPS' load encoder prescale
F_Ld_Enc_Cycle   =  1           # 'LEC' load encoder cycle
F_Ld_Int_Cycle   =  2           # 'LIC' load internal cycle
F_Rd_Cmp_Cyc_Clks =  3          # 'RCC' read cmp cycle clocks
F_Enc_Max        =  4           # number of encoder registers

# debug frequency

F_Ld_Dbg_Freq    =  0           # 'DBF' debug frequency
F_Ld_Dbg_Count   =  1           # 'DBC' debug clock count
F_Ld_Sync_Count  =  2           # 'DBS' debug sync length
F_Dbg_Freq_Max   =  3           # number of debug frequency regs

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

# runout

F_Ld_RunOut_Ctl  =  0           # 'CTL' runout control reg
F_Ld_Run_Limit   =  1           # 'LIM' runout limit

# register definitions

F_Noop           =  0           # 'NO' reg 0

# status registers

F_Rd_Status      =  1           # 'RSTS' status reg
F_Rd_Inputs      =  2           # 'RINP' inputs reg

# control registers

F_Ld_Sync_Ctl    =  3           # 'LSYN' sync control reg
F_Ld_Cfg_Ctl     =  4           # 'LCFG' config control reg
F_Ld_Clk_Ctl     =  5           # 'LCLK' clock control reg
F_Ld_Out_Reg     =  6           # 'LDOU' output reg
F_Ld_Dsp_Reg     =  7           # 'LDSP' display reg

# debug frequency control

F_Dbg_Freq_Base  =  8           # 'D' dbg frequency

# spindle speed

F_Rd_Idx_Clks    = 11           # 'RIDX' clocks per index

# pwm

F_PWM_Base       = 12           # 'P' pwm control

# base for modules

F_Enc_Base       = 14           # 'E' encoder registers
F_Phase_Base     = 18           # 'H' phase registers
F_RunOut_Base    = 20           # 'R' runout registers
F_ZAxis_Base     = 22           # 'Z' z axis registers
F_XAxis_Base     = 46           # 'X' x axis registers
F_Spindle_Base   = 70           # 'S' spindle registers
F_Cmd_Max        = 95           # number of commands
# fpga table

xRegTable = ( \
    "F_Noop",                           #   0 x00
    "F_Rd_Status",                      #   1 x01
    "F_Rd_Inputs",                      #   2 x02
    "F_Ld_Sync_Ctl",                    #   3 x03
    "F_Ld_Cfg_Ctl",                     #   4 x04
    "F_Ld_Clk_Ctl",                     #   5 x05
    "F_Ld_Out_Reg",                     #   6 x06
    "F_Ld_Dsp_Reg",                     #   7 x07
    "F_Dbg_Freq_Base+F_Ld_Dbg_Freq",    #   8 x08
    "F_Dbg_Freq_Base+F_Ld_Dbg_Count",   #   9 x09
    "F_Dbg_Freq_Base+F_Ld_Sync_Count",  #  10 x0a
    "F_Rd_Idx_Clks",                    #  11 x0b
    "F_PWM_Base+F_Ld_PWM_Max",          #  12 x0c
    "F_PWM_Base+F_Ld_PWM_Trig",         #  13 x0d
    "F_Enc_Base+F_Ld_Enc_Prescale",     #  14 x0e
    "F_Enc_Base+F_Ld_Enc_Cycle",        #  15 x0f
    "F_Enc_Base+F_Ld_Int_Cycle",        #  16 x10
    "F_Enc_Base+F_Rd_Cmp_Cyc_Clks",     #  17 x11
    "F_Phase_Base+F_Ld_Phase_Len",      #  18 x12
    "F_Phase_Base+F_Rd_Phase_Syn",      #  19 x13
    "F_RunOut_Base+F_Ld_RunOut_Ctl",    #  20 x14
    "F_RunOut_Base+F_Ld_Run_Limit",     #  21 x15
    "F_ZAxis_Base+F_Rd_Axis_Status",    #  22 x16
    "F_ZAxis_Base+F_Ld_Axis_Ctl",       #  23 x17
    "F_ZAxis_Base+F_Rd_Axis_Ctl",       #  24 x18
    "F_ZAxis_Base+F_Ld_Freq",           #  25 x19
    "F_ZAxis_Base+F_Ld_D",              #  26 x1a
    "F_ZAxis_Base+F_Ld_Incr1",          #  27 x1b
    "F_ZAxis_Base+F_Ld_Incr2",          #  28 x1c
    "F_ZAxis_Base+F_Ld_Accel_Val",      #  29 x1d
    "F_ZAxis_Base+F_Ld_Accel_Count",    #  30 x1e
    "F_ZAxis_Base+F_Rd_XPos",           #  31 x1f
    "F_ZAxis_Base+F_Rd_YPos",           #  32 x20
    "F_ZAxis_Base+F_Rd_Sum",            #  33 x21
    "F_ZAxis_Base+F_Rd_Accel_Sum",      #  34 x22
    "F_ZAxis_Base+F_Rd_Accel_Ctr",      #  35 x23
    "F_ZAxis_Base+F_Ld_Dist",           #  36 x24
    "F_ZAxis_Base+F_Ld_Max_Dist",       #  37 x25
    "F_ZAxis_Base+F_Rd_Dist",           #  38 x26
    "F_ZAxis_Base+F_Rd_Accel_Steps",    #  39 x27
    "F_ZAxis_Base+F_Ld_Loc",            #  40 x28
    "F_ZAxis_Base+F_Rd_Loc",            #  41 x29
    "F_ZAxis_Base+F_Ld_Dro",            #  42 x2a
    "F_ZAxis_Base+F_Ld_Dro_End",        #  43 x2b
    "F_ZAxis_Base+F_Ld_Dro_Limit",      #  44 x2c
    "F_ZAxis_Base+F_Rd_Dro",            #  45 x2d
    "F_XAxis_Base+F_Rd_Axis_Status",    #  46 x2e
    "F_XAxis_Base+F_Ld_Axis_Ctl",       #  47 x2f
    "F_XAxis_Base+F_Rd_Axis_Ctl",       #  48 x30
    "F_XAxis_Base+F_Ld_Freq",           #  49 x31
    "F_XAxis_Base+F_Ld_D",              #  50 x32
    "F_XAxis_Base+F_Ld_Incr1",          #  51 x33
    "F_XAxis_Base+F_Ld_Incr2",          #  52 x34
    "F_XAxis_Base+F_Ld_Accel_Val",      #  53 x35
    "F_XAxis_Base+F_Ld_Accel_Count",    #  54 x36
    "F_XAxis_Base+F_Rd_XPos",           #  55 x37
    "F_XAxis_Base+F_Rd_YPos",           #  56 x38
    "F_XAxis_Base+F_Rd_Sum",            #  57 x39
    "F_XAxis_Base+F_Rd_Accel_Sum",      #  58 x3a
    "F_XAxis_Base+F_Rd_Accel_Ctr",      #  59 x3b
    "F_XAxis_Base+F_Ld_Dist",           #  60 x3c
    "F_XAxis_Base+F_Ld_Max_Dist",       #  61 x3d
    "F_XAxis_Base+F_Rd_Dist",           #  62 x3e
    "F_XAxis_Base+F_Rd_Accel_Steps",    #  63 x3f
    "F_XAxis_Base+F_Ld_Loc",            #  64 x40
    "F_XAxis_Base+F_Rd_Loc",            #  65 x41
    "F_XAxis_Base+F_Ld_Dro",            #  66 x42
    "F_XAxis_Base+F_Ld_Dro_End",        #  67 x43
    "F_XAxis_Base+F_Ld_Dro_Limit",      #  68 x44
    "F_XAxis_Base+F_Rd_Dro",            #  69 x45
    "F_Spindle_Base+F_Ld_Sp_Ctl",       #  70 x46
    "F_Spindle_Base+F_Ld_Sp_Freq",      #  71 x47
    "F_Spindle_Base+F_Ld_Jog_Ctl",      #  72 x48
    "F_Spindle_Base+F_Ld_Jog_Inc",      #  73 x49
    "F_Spindle_Base+F_Ld_Jog_Back",     #  74 x4a
    "F_Spindle_Base+F_Ld_D",            #  75 x4b
    "F_Spindle_Base+F_Ld_Incr1",        #  76 x4c
    "F_Spindle_Base+F_Ld_Incr2",        #  77 x4d
    "F_Spindle_Base+F_Ld_Accel_Val",    #  78 x4e
    "F_Spindle_Base+F_Ld_Accel_Count",  #  79 x4f
    "F_Spindle_Base+F_Rd_XPos",         #  80 x50
    "F_Spindle_Base+F_Rd_YPos",         #  81 x51
    "F_Spindle_Base+F_Rd_Sum",          #  82 x52
    "F_Spindle_Base+F_Rd_Accel_Sum",    #  83 x53
    "F_Spindle_Base+F_Rd_Accel_Ctr",    #  84 x54
    "F_Spindle_Base+F_Ld_Dist",         #  85 x55
    "F_Spindle_Base+F_Ld_Max_Dist",     #  86 x56
    "F_Spindle_Base+F_Rd_Dist",         #  87 x57
    "F_Spindle_Base+F_Rd_Accel_Steps",  #  88 x58
    "F_Spindle_Base+F_Ld_Loc",          #  89 x59
    "F_Spindle_Base+F_Rd_Loc",          #  90 x5a
    "F_Spindle_Base+F_Ld_Dro",          #  91 x5b
    "F_Spindle_Base+F_Ld_Dro_End",      #  92 x5c
    "F_Spindle_Base+F_Ld_Dro_Limit",    #  93 x5d
    "F_Spindle_Base+F_Rd_Dro",          #  94 x5e
    )

fpgaSizeTable = ( \
    1,              #   0 F_Noop
    4,              #   1 F_Rd_Status
    4,              #   2 F_Rd_Inputs
    1,              #   3 F_Ld_Sync_Ctl
    3,              #   4 F_Ld_Cfg_Ctl
    1,              #   5 F_Ld_Clk_Ctl
    1,              #   6 F_Ld_Out_Reg
    1,              #   7 F_Ld_Dsp_Reg
    2,              #   8 F_Dbg_Freq_Base, F_Ld_Dbg_Freq
    4,              #   9 F_Dbg_Freq_Base, F_Ld_Dbg_Count
    4,              #  10 F_Dbg_Freq_Base, F_Ld_Sync_Count
    4,              #  11 F_Rd_Idx_Clks
    4,              #  12 F_PWM_Base, F_Ld_PWM_Max
    4,              #  13 F_PWM_Base, F_Ld_PWM_Trig
    2,              #  14 F_Enc_Base, F_Ld_Enc_Prescale
    2,              #  15 F_Enc_Base, F_Ld_Enc_Cycle
    2,              #  16 F_Enc_Base, F_Ld_Int_Cycle
    4,              #  17 F_Enc_Base, F_Rd_Cmp_Cyc_Clks
    2,              #  18 F_Phase_Base, F_Ld_Phase_Len
    4,              #  19 F_Phase_Base, F_Rd_Phase_Syn
    1,              #  20 F_RunOut_Base, F_Ld_RunOut_Ctl
    4,              #  21 F_RunOut_Base, F_Ld_Run_Limit
    1,              #  22 F_ZAxis_Base, F_Rd_Axis_Status
    2,              #  23 F_ZAxis_Base, F_Ld_Axis_Ctl
    2,              #  24 F_ZAxis_Base, F_Rd_Axis_Ctl
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
    4,              #  36 F_ZAxis_Base, F_Sync_Base, F_Ld_Dist
    4,              #  37 F_ZAxis_Base, F_Sync_Base, F_Ld_Max_Dist
    4,              #  38 F_ZAxis_Base, F_Sync_Base, F_Rd_Dist
    4,              #  39 F_ZAxis_Base, F_Sync_Base, F_Rd_Accel_Steps
    4,              #  40 F_ZAxis_Base, F_Sync_Base, F_Ld_Loc
    4,              #  41 F_ZAxis_Base, F_Sync_Base, F_Rd_Loc
    4,              #  42 F_ZAxis_Base, F_Sync_Base, F_Ld_Dro
    4,              #  43 F_ZAxis_Base, F_Sync_Base, F_Ld_Dro_End
    4,              #  44 F_ZAxis_Base, F_Sync_Base, F_Ld_Dro_Limit
    4,              #  45 F_ZAxis_Base, F_Sync_Base, F_Rd_Dro
    1,              #  46 F_XAxis_Base, F_Rd_Axis_Status
    2,              #  47 F_XAxis_Base, F_Ld_Axis_Ctl
    2,              #  48 F_XAxis_Base, F_Rd_Axis_Ctl
    4,              #  49 F_XAxis_Base, F_Ld_Freq
    4,              #  50 F_XAxis_Base, F_Sync_Base, F_Ld_D
    4,              #  51 F_XAxis_Base, F_Sync_Base, F_Ld_Incr1
    4,              #  52 F_XAxis_Base, F_Sync_Base, F_Ld_Incr2
    4,              #  53 F_XAxis_Base, F_Sync_Base, F_Ld_Accel_Val
    4,              #  54 F_XAxis_Base, F_Sync_Base, F_Ld_Accel_Count
    4,              #  55 F_XAxis_Base, F_Sync_Base, F_Rd_XPos
    4,              #  56 F_XAxis_Base, F_Sync_Base, F_Rd_YPos
    4,              #  57 F_XAxis_Base, F_Sync_Base, F_Rd_Sum
    4,              #  58 F_XAxis_Base, F_Sync_Base, F_Rd_Accel_Sum
    4,              #  59 F_XAxis_Base, F_Sync_Base, F_Rd_Accel_Ctr
    4,              #  60 F_XAxis_Base, F_Sync_Base, F_Ld_Dist
    4,              #  61 F_XAxis_Base, F_Sync_Base, F_Ld_Max_Dist
    4,              #  62 F_XAxis_Base, F_Sync_Base, F_Rd_Dist
    4,              #  63 F_XAxis_Base, F_Sync_Base, F_Rd_Accel_Steps
    4,              #  64 F_XAxis_Base, F_Sync_Base, F_Ld_Loc
    4,              #  65 F_XAxis_Base, F_Sync_Base, F_Rd_Loc
    4,              #  66 F_XAxis_Base, F_Sync_Base, F_Ld_Dro
    4,              #  67 F_XAxis_Base, F_Sync_Base, F_Ld_Dro_End
    4,              #  68 F_XAxis_Base, F_Sync_Base, F_Ld_Dro_Limit
    4,              #  69 F_XAxis_Base, F_Sync_Base, F_Rd_Dro
    1,              #  70 F_Spindle_Base, F_Ld_Sp_Ctl
    4,              #  71 F_Spindle_Base, F_Ld_Sp_Freq
    4,              #  72 F_Spindle_Base, F_Sp_Jog_Base, F_Ld_Jog_Ctl
    4,              #  73 F_Spindle_Base, F_Sp_Jog_Base, F_Ld_Jog_Inc
    4,              #  74 F_Spindle_Base, F_Sp_Jog_Base, F_Ld_Jog_Back
    4,              #  75 F_Spindle_Base, F_Sp_Sync_Base, F_Ld_D
    4,              #  76 F_Spindle_Base, F_Sp_Sync_Base, F_Ld_Incr1
    4,              #  77 F_Spindle_Base, F_Sp_Sync_Base, F_Ld_Incr2
    4,              #  78 F_Spindle_Base, F_Sp_Sync_Base, F_Ld_Accel_Val
    4,              #  79 F_Spindle_Base, F_Sp_Sync_Base, F_Ld_Accel_Count
    4,              #  80 F_Spindle_Base, F_Sp_Sync_Base, F_Rd_XPos
    4,              #  81 F_Spindle_Base, F_Sp_Sync_Base, F_Rd_YPos
    4,              #  82 F_Spindle_Base, F_Sp_Sync_Base, F_Rd_Sum
    4,              #  83 F_Spindle_Base, F_Sp_Sync_Base, F_Rd_Accel_Sum
    4,              #  84 F_Spindle_Base, F_Sp_Sync_Base, F_Rd_Accel_Ctr
    4,              #  85 F_Spindle_Base, F_Sp_Sync_Base, F_Ld_Dist
    4,              #  86 F_Spindle_Base, F_Sp_Sync_Base, F_Ld_Max_Dist
    4,              #  87 F_Spindle_Base, F_Sp_Sync_Base, F_Rd_Dist
    4,              #  88 F_Spindle_Base, F_Sp_Sync_Base, F_Rd_Accel_Steps
    4,              #  89 F_Spindle_Base, F_Sp_Sync_Base, F_Ld_Loc
    4,              #  90 F_Spindle_Base, F_Sp_Sync_Base, F_Rd_Loc
    4,              #  91 F_Spindle_Base, F_Sp_Sync_Base, F_Ld_Dro
    4,              #  92 F_Spindle_Base, F_Sp_Sync_Base, F_Ld_Dro_End
    4,              #  93 F_Spindle_Base, F_Sp_Sync_Base, F_Ld_Dro_Limit
    4,              #  94 F_Spindle_Base, F_Sp_Sync_Base, F_Rd_Dro
    )
