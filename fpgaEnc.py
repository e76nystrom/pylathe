
# xilinx bits

# run control register

ctlReset     = 0x01             # reset
ctlTestClock = 0x02             # testclock
ctlSpare     = 0x04             # spare

# debug control register

DbgEna       = 0x01             # enable debugging
DbgSel       = 0x02             # select dbg encoder
DbgDir       = 0x04             # debug direction
DbgCount     = 0x08             # gen count num dbg clks

importList = ( \
 ctlReset, \
 ctlTestClock, \
 ctlSpare, \
 DbgEna, \
 DbgSel, \
 DbgDir, \
 DbgCount, \
)
