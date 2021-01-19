
# commands

# z motion commands

ZMOVEABS             =   0
ZMOVEREL             =   1
ZJMOV                =   2
ZJSPEED              =   3
ZSTOP                =   4
ZSETLOC              =   5
ZHOMEFWD             =   6
ZHOMEREV             =   7

# x motion commands

XMOVEABS             =   8
XMOVEREL             =   9
XJMOV                =  10
XJSPEED              =  11
XSTOP                =  12
XSETLOC              =  13
XHOMEFWD             =  14
XHOMEREV             =  15

# spindle operations

SPINDLE_START        =  16
SPINDLE_JOG          =  17
SPINDLE_JOG_SPEED    =  18
SPINDLE_STOP         =  19

# end operations

CMD_PAUSE            =  20
CMD_RESUME           =  21
CMD_STOP             =  22
CMD_MEASURE          =  23

# setup operations

CMD_CLEAR            =  24
CMD_SETUP            =  25
CMD_SPSETUP          =  26
CMD_SYNCSETUP        =  27
CMD_ZSETUP           =  28
CMD_ZSYNSETUP        =  29
CMD_XSETUP           =  30
CMD_XSYNSETUP        =  31

# state information

READSTAT             =  32
READISTATE           =  33

# load processor and xilinx parameters

LOADVAL              =  34
LOADMULTI            =  35
READVAL              =  36
LOADXREG             =  37
READXREG             =  38

# move command operations

CLEARQUE             =  39
QUEMOVE              =  40
MOVEQUESTATUS        =  41

# location and debug info

READALL              =  42
READDBG              =  43
CLRDBG               =  44

# encoder commands

ENCSTART             =  45
ENCSTOP              =  46

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
    ("SPINDLE_JOG", "spindleJog"),      #  17
    ("SPINDLE_JOG_SPEED", "spindleJogSpeed"),#  18
    ("SPINDLE_STOP", "spindleStop"),    #  19
    ("CMD_PAUSE", "pauseCmd"),          #  20
    ("CMD_RESUME", "resumeCmd"),        #  21
    ("CMD_STOP", "stopCmd"),            #  22
    ("CMD_MEASURE", "measureCmd"),      #  23
    ("CMD_CLEAR", "clearCmd"),          #  24
    ("CMD_SETUP", "setup"),             #  25
    ("CMD_SPSETUP", "spindleSetup"),    #  26
    ("CMD_SYNCSETUP", "syncSetup"),     #  27
    ("CMD_ZSETUP", "zSetup"),           #  28
    ("CMD_ZSYNSETUP", None),            #  29
    ("CMD_XSETUP", "xSetup"),           #  30
    ("CMD_XSYNSETUP", None),            #  31
    ("READSTAT", None),                 #  32
    ("READISTATE", None),               #  33
    ("LOADVAL", None),                  #  34
    ("LOADMULTI", None),                #  35
    ("READVAL", None),                  #  36
    ("LOADXREG", None),                 #  37
    ("READXREG", None),                 #  38
    ("CLEARQUE", "clearQue"),           #  39
    ("QUEMOVE", None),                  #  40
    ("MOVEQUESTATUS", None),            #  41
    ("READALL", "readAll"),             #  42
    ("READDBG", "readDbg"),             #  43
    ("CLRDBG", "clearDbg"),             #  44
    ("ENCSTART", None),                 #  45
    ("ENCSTOP", None),                  #  46
    )
