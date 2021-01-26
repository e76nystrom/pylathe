
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
CMD_DONE             =  23
CMD_MEASURE          =  24

# setup operations

CMD_CLEAR            =  25
CMD_SETUP            =  26
CMD_SPSETUP          =  27
CMD_SYNCSETUP        =  28
CMD_ZSETUP           =  29
CMD_ZSYNSETUP        =  30
CMD_XSETUP           =  31
CMD_XSYNSETUP        =  32

# state information

READSTAT             =  33
READISTATE           =  34

# load processor and xilinx parameters

LOADVAL              =  35
LOADMULTI            =  36
READVAL              =  37
LOADXREG             =  38
READXREG             =  39

# move command operations

CLEARQUE             =  40
QUEMOVE              =  41
MOVEQUESTATUS        =  42

# location and debug info

READALL              =  43
READDBG              =  44
CLRDBG               =  45

# encoder commands

ENCSTART             =  46
ENCSTOP              =  47

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
    ("CMD_DONE", "doneCmd"),            #  23
    ("CMD_MEASURE", "measureCmd"),      #  24
    ("CMD_CLEAR", "clearCmd"),          #  25
    ("CMD_SETUP", "setup"),             #  26
    ("CMD_SPSETUP", "spindleSetup"),    #  27
    ("CMD_SYNCSETUP", "syncSetup"),     #  28
    ("CMD_ZSETUP", "zSetup"),           #  29
    ("CMD_ZSYNSETUP", None),            #  30
    ("CMD_XSETUP", "xSetup"),           #  31
    ("CMD_XSYNSETUP", None),            #  32
    ("READSTAT", None),                 #  33
    ("READISTATE", None),               #  34
    ("LOADVAL", None),                  #  35
    ("LOADMULTI", None),                #  36
    ("READVAL", None),                  #  37
    ("LOADXREG", None),                 #  38
    ("READXREG", None),                 #  39
    ("CLEARQUE", "clearQue"),           #  40
    ("QUEMOVE", None),                  #  41
    ("MOVEQUESTATUS", None),            #  42
    ("READALL", "readAll"),             #  43
    ("READDBG", "readDbg"),             #  44
    ("CLRDBG", "clearDbg"),             #  45
    ("ENCSTART", None),                 #  46
    ("ENCSTOP", None),                  #  47
    )
