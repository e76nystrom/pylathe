
# commands

# z motion commands

C_ZMOVEABS           =   0	# 0x00
C_ZMOVEREL           =   1	# 0x01
C_ZJMOV              =   2	# 0x02
C_ZJSPEED            =   3	# 0x03
C_ZSTOP              =   4	# 0x04
C_ZSETLOC            =   5	# 0x05
C_ZHOMEFWD           =   6	# 0x06
C_ZHOMEREV           =   7	# 0x07

# x motion commands

C_XMOVEABS           =   8	# 0x08
C_XMOVEREL           =   9	# 0x09
C_XJMOV              =  10	# 0x0a
C_XJSPEED            =  11	# 0x0b
C_XSTOP              =  12	# 0x0c
C_XSETLOC            =  13	# 0x0d
C_XHOMEFWD           =  14	# 0x0e
C_XHOMEREV           =  15	# 0x0f

# spindle operations

C_SPINDLE_START      =  16	# 0x10
C_SPINDLE_STOP       =  17	# 0x11
C_SPINDLE_UPDATE     =  18	# 0x12
C_SPINDLE_JOG        =  19	# 0x13
C_SPINDLE_JOG_SPEED  =  20	# 0x14

# end operations

C_CMD_PAUSE          =  21	# 0x15
C_CMD_RESUME         =  22	# 0x16
C_CMD_STOP           =  23	# 0x17
C_CMD_DONE           =  24	# 0x18
C_CMD_MEASURE        =  25	# 0x19

# setup operations

C_CMD_CLEAR          =  26	# 0x1a
C_CMD_SETUP          =  27	# 0x1b
C_CMD_SPSETUP        =  28	# 0x1c
C_CMD_SYNCSETUP      =  29	# 0x1d
C_CMD_ZSETUP         =  30	# 0x1e
C_CMD_ZSYNSETUP      =  31	# 0x1f
C_CMD_ZSETLOC        =  32	# 0x20
C_CMD_XSETUP         =  33	# 0x21
C_CMD_XSYNSETUP      =  34	# 0x22
C_CMD_XSETLOC        =  35	# 0x23

# state information

C_READSTAT           =  36	# 0x24
C_READISTATE         =  37	# 0x25

# load processor and xilinx parameters

C_LOADVAL            =  38	# 0x26
C_LOADMULTI          =  39	# 0x27
C_READVAL            =  40	# 0x28
C_LOADXREG           =  41	# 0x29
C_READXREG           =  42	# 0x2a

# move command operations

C_CLEARQUE           =  43	# 0x2b
C_QUEMOVE            =  44	# 0x2c
C_MOVEMULTI          =  45	# 0x2d
C_MOVEQUESTATUS      =  46	# 0x2e

# location and debug info

C_READALL            =  47	# 0x2f
C_READDBG            =  48	# 0x30
C_CLRDBG             =  49	# 0x31

# encoder commands

C_ENCSTART           =  50	# 0x32
C_ENCSTOP            =  51	# 0x33

#  mega commands 

C_SET_MEGA_VAL       =  52	# 0x34
C_READ_MEGA_VAL      =  53	# 0x35

# command table

cmdTable = ( \
    ("C_ZMOVEABS        ", "cZMoveAbs"       ), #   0
    ("C_ZMOVEREL        ", "cZMoveRel"       ), #   1
    ("C_ZJMOV           ", "cZJogMove"       ), #   2
    ("C_ZJSPEED         ", "cZJogSpeed"      ), #   3
    ("C_ZSTOP           ", "cZStop"          ), #   4
    ("C_ZSETLOC         ", None              ), #   5
    ("C_ZHOMEFWD        ", "cZHomeFwd"       ), #   6
    ("C_ZHOMEREV        ", "cZHomeRev"       ), #   7
    ("C_XMOVEABS        ", "cXMoveAbs"       ), #   8
    ("C_XMOVEREL        ", "cXMoveRel"       ), #   9
    ("C_XJMOV           ", "cXJogMove"       ), #  10
    ("C_XJSPEED         ", "cXJogSpeed"      ), #  11
    ("C_XSTOP           ", "cXStop"          ), #  12
    ("C_XSETLOC         ", None              ), #  13
    ("C_XHOMEFWD        ", "cXHomeFwd"       ), #  14
    ("C_XHOMEREV        ", "cXHomeRev"       ), #  15
    ("C_SPINDLE_START   ", "cSpindleStart"   ), #  16
    ("C_SPINDLE_STOP    ", "cSpindleStop"    ), #  17
    ("C_SPINDLE_UPDATE  ", "cSpindleUpdate"  ), #  18
    ("C_SPINDLE_JOG     ", "cSpindleJog"     ), #  19
    ("C_SPINDLE_JOG_SPEED", "cSpindleJogSpeed"),#  20
    ("C_CMD_PAUSE       ", "cPauseCmd"       ), #  21
    ("C_CMD_RESUME      ", "cResumeCmd"      ), #  22
    ("C_CMD_STOP        ", "cStopCmd"        ), #  23
    ("C_CMD_DONE        ", "cDoneCmd"        ), #  24
    ("C_CMD_MEASURE     ", "cMeasureCmd"     ), #  25
    ("C_CMD_CLEAR       ", "cClearCmd"       ), #  26
    ("C_CMD_SETUP       ", "cSetup"          ), #  27
    ("C_CMD_SPSETUP     ", "cSpindleSetup"   ), #  28
    ("C_CMD_SYNCSETUP   ", "cSyncSetup"      ), #  29
    ("C_CMD_ZSETUP      ", "cZSetup"         ), #  30
    ("C_CMD_ZSYNSETUP   ", None              ), #  31
    ("C_CMD_ZSETLOC     ", "cZSetLoc"        ), #  32
    ("C_CMD_XSETUP      ", "cXSetup"         ), #  33
    ("C_CMD_XSYNSETUP   ", None              ), #  34
    ("C_CMD_XSETLOC     ", "cXSetLoc"        ), #  35
    ("C_READSTAT        ", None              ), #  36
    ("C_READISTATE      ", None              ), #  37
    ("C_LOADVAL         ", None              ), #  38
    ("C_LOADMULTI       ", None              ), #  39
    ("C_READVAL         ", None              ), #  40
    ("C_LOADXREG        ", None              ), #  41
    ("C_READXREG        ", None              ), #  42
    ("C_CLEARQUE        ", "cClearQue"       ), #  43
    ("C_QUEMOVE         ", None              ), #  44
    ("C_MOVEMULTI       ", None              ), #  45
    ("C_MOVEQUESTATUS   ", None              ), #  46
    ("C_READALL         ", "cReadAll"        ), #  47
    ("C_READDBG         ", "cReadDbg"        ), #  48
    ("C_CLRDBG          ", "cClearDbg"       ), #  49
    ("C_ENCSTART        ", None              ), #  50
    ("C_ENCSTOP         ", None              ), #  51
    ("C_SET_MEGA_VAL    ", None              ), #  52
    ("C_READ_MEGA_VAL   ", None              ), #  53
    )
