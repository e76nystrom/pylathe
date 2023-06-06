
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
CMD_ZSETLOC          =  32	# 0x20
CMD_XSETUP           =  33	# 0x21
CMD_XSYNSETUP        =  34	# 0x22
CMD_XSETLOC          =  35	# 0x23

# state information

READSTAT             =  36	# 0x24
READISTATE           =  37	# 0x25

# load processor and xilinx parameters

LOADVAL              =  38	# 0x26
LOADMULTI            =  39	# 0x27
READVAL              =  40	# 0x28
LOADXREG             =  41	# 0x29
READXREG             =  42	# 0x2a

# move command operations

CLEARQUE             =  43	# 0x2b
QUEMOVE              =  44	# 0x2c
MOVEMULTI            =  45	# 0x2d
MOVEQUESTATUS        =  46	# 0x2e

# location and debug info

READALL              =  47	# 0x2f
READDBG              =  48	# 0x30
CLRDBG               =  49	# 0x31

# encoder commands

ENCSTART             =  50	# 0x32
ENCSTOP              =  51	# 0x33

#  mega commands 

SET_MEGA_VAL         =  52	# 0x34
READ_MEGA_VAL        =  53	# 0x35

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
    ("CMD_ZSETLOC", "zSetLoc"),         #  32
    ("CMD_XSETUP", "xSetup"),           #  33
    ("CMD_XSYNSETUP", None),            #  34
    ("CMD_XSETLOC", "xSetLoc"),         #  35
    ("READSTAT", None),                 #  36
    ("READISTATE", None),               #  37
    ("LOADVAL", None),                  #  38
    ("LOADMULTI", None),                #  39
    ("READVAL", None),                  #  40
    ("LOADXREG", None),                 #  41
    ("READXREG", None),                 #  42
    ("CLEARQUE", "clearQue"),           #  43
    ("QUEMOVE", None),                  #  44
    ("MOVEMULTI", None),                #  45
    ("MOVEQUESTATUS", None),            #  46
    ("READALL", "readAll"),             #  47
    ("READDBG", "readDbg"),             #  48
    ("CLRDBG", "clearDbg"),             #  49
    ("ENCSTART", None),                 #  50
    ("ENCSTOP", None),                  #  51
    ("SET_MEGA_VAL", None),             #  52
    ("READ_MEGA_VAL", None),            #  53
    )
