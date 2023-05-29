
# commands

# z motion commands

ZMOVEABS             =   0	# 0x00
ZMOVEREL             =   1	# 0x01
ZJMOV                =   2	# 0x02
ZJSPEED              =   3	# 0x03
ZSTOP                =   4	# 0x04
ZSETLOC              =   5	# 0x05
ZHOMEFWD             =   6	# 0x06
ZHOMEREV             =   7	# 0x07

# x motion commands

XMOVEABS             =   8	# 0x08
XMOVEREL             =   9	# 0x09
XJMOV                =  10	# 0x0a
XJSPEED              =  11	# 0x0b
XSTOP                =  12	# 0x0c
XSETLOC              =  13	# 0x0d
XHOMEFWD             =  14	# 0x0e
XHOMEREV             =  15	# 0x0f

# spindle operations

SPINDLE_START        =  16	# 0x10
SPINDLE_STOP         =  17	# 0x11
SPINDLE_UPDATE       =  18	# 0x12
SPINDLE_JOG          =  19	# 0x13
SPINDLE_JOG_SPEED    =  20	# 0x14

# end operations

CMD_PAUSE            =  21	# 0x15
CMD_RESUME           =  22	# 0x16
CMD_STOP             =  23	# 0x17
CMD_DONE             =  24	# 0x18
CMD_MEASURE          =  25	# 0x19

# setup operations

CMD_CLEAR            =  26	# 0x1a
CMD_SETUP            =  27	# 0x1b
CMD_SPSETUP          =  28	# 0x1c
CMD_SYNCSETUP        =  29	# 0x1d
CMD_ZSETUP           =  30	# 0x1e
CMD_ZSYNSETUP        =  31	# 0x1f
CMD_XSETUP           =  32	# 0x20
CMD_XSYNSETUP        =  33	# 0x21

# state information

READSTAT             =  34	# 0x22
READISTATE           =  35	# 0x23

# load processor and xilinx parameters

LOADVAL              =  36	# 0x24
LOADMULTI            =  37	# 0x25
READVAL              =  38	# 0x26
LOADXREG             =  39	# 0x27
READXREG             =  40	# 0x28

# move command operations

CLEARQUE             =  41	# 0x29
QUEMOVE              =  42	# 0x2a
MOVEMULTI            =  43	# 0x2b
MOVEQUESTATUS        =  44	# 0x2c

# location and debug info

READALL              =  45	# 0x2d
READDBG              =  46	# 0x2e
CLRDBG               =  47	# 0x2f

# encoder commands

ENCSTART             =  48	# 0x30
ENCSTOP              =  49	# 0x31

#  mega commands 

SET_MEGA_VAL         =  50	# 0x32
READ_MEGA_VAL        =  51	# 0x33

# command table

cmdTable = ( \
    ("ZMOVEABS", "zMoveAbs"),           #   0
    ("ZMOVEREL", "zMoveRel"),           #   1
    ("ZJMOV", "zJogMove"),              #   2
    ("ZJSPEED", "zJogSpeed"),           #   3
    ("ZSTOP", "zStop"),                 #   4
    ("ZSETLOC", None),                  #   5
    ("ZHOMEFWD", "zHomeFwd"),           #   6
    ("ZHOMEREV", "zHomeRev"),           #   7
    ("XMOVEABS", "xMoveAbs"),           #   8
    ("XMOVEREL", "xMoveRel"),           #   9
    ("XJMOV", "xJogMove"),              #  10
    ("XJSPEED", "xJogSpeed"),           #  11
    ("XSTOP", "xStop"),                 #  12
    ("XSETLOC", None),                  #  13
    ("XHOMEFWD", "xHomeFwd"),           #  14
    ("XHOMEREV", "xHomeRev"),           #  15
    ("SPINDLE_START", "spindleStart"),  #  16
    ("SPINDLE_STOP", "spindleStop"),    #  17
    ("SPINDLE_UPDATE", "spindleUpdate"),#  18
    ("SPINDLE_JOG", "spindleJog"),      #  19
    ("SPINDLE_JOG_SPEED", "spindleJogSpeed"),#  20
    ("CMD_PAUSE", "pauseCmd"),          #  21
    ("CMD_RESUME", "resumeCmd"),        #  22
    ("CMD_STOP", "stopCmd"),            #  23
    ("CMD_DONE", "doneCmd"),            #  24
    ("CMD_MEASURE", "measureCmd"),      #  25
    ("CMD_CLEAR", "clearCmd"),          #  26
    ("CMD_SETUP", "setup"),             #  27
    ("CMD_SPSETUP", "spindleSetup"),    #  28
    ("CMD_SYNCSETUP", "syncSetup"),     #  29
    ("CMD_ZSETUP", "zSetup"),           #  30
    ("CMD_ZSYNSETUP", None),            #  31
    ("CMD_XSETUP", "xSetup"),           #  32
    ("CMD_XSYNSETUP", None),            #  33
    ("READSTAT", None),                 #  34
    ("READISTATE", None),               #  35
    ("LOADVAL", None),                  #  36
    ("LOADMULTI", None),                #  37
    ("READVAL", None),                  #  38
    ("LOADXREG", None),                 #  39
    ("READXREG", None),                 #  40
    ("CLEARQUE", "clearQue"),           #  41
    ("QUEMOVE", None),                  #  42
    ("MOVEMULTI", None),                #  43
    ("MOVEQUESTATUS", None),            #  44
    ("READALL", "readAll"),             #  45
    ("READDBG", "readDbg"),             #  46
    ("CLRDBG", "clearDbg"),             #  47
    ("ENCSTART", None),                 #  48
    ("ENCSTOP", None),                  #  49
    ("SET_MEGA_VAL", None),             #  50
    ("READ_MEGA_VAL", None),            #  51
    )
