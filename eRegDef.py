
# fpga registers

F_Noop           =  0           # register 0
F_Ld_Run_Ctl     =  1           # load run control register
F_Ld_Dbg_Ctl     =  2           # load debug control register
F_Ld_Enc_Cycle   =  3           # load encoder cycle
F_Ld_Int_Cycle   =  4           # load internal cycle
F_Rd_Cmp_Cyc_Clks =  5          # read cmp cycle clocks
F_Ld_Dbg_Freq    =  6           # load debug frequency
F_Ld_Dbg_Count   =  7           # load debug clocks

# xilinx table

xRegTable = ( \
    "F_Noop",                           #   0
    "F_Ld_Run_Ctl",                     #   1
    "F_Ld_Dbg_Ctl",                     #   2
    "F_Ld_Enc_Cycle",                   #   3
    "F_Ld_Int_Cycle",                   #   4
    "F_Rd_Cmp_Cyc_Clks",                #   5
    "F_Ld_Dbg_Freq",                    #   6
    "F_Ld_Dbg_Count",                   #   7
    )

importList = ( \
 xRegTable, \
 F_Noop, \
 F_Ld_Run_Ctl, \
 F_Ld_Dbg_Ctl, \
 F_Ld_Enc_Cycle, \
 F_Ld_Int_Cycle, \
 F_Rd_Cmp_Cyc_Clks, \
 F_Ld_Dbg_Freq, \
 F_Ld_Dbg_Count, \
)
