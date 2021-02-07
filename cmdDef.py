
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
SPINDLE_STOP         =  17
SPINDLE_UPDATE       =  18
SPINDLE_JOG          =  19
SPINDLE_JOG_SPEED    =  20

# end operations

CMD_PAUSE            =  21
CMD_RESUME           =  22
CMD_STOP             =  23
CMD_DONE             =  24
CMD_MEASURE          =  25

# setup operations

CMD_CLEAR            =  26
CMD_SETUP            =  27
CMD_SPSETUP          =  28
CMD_SYNCSETUP        =  29
CMD_ZSETUP           =  30
CMD_ZSYNSETUP        =  31
CMD_XSETUP           =  32
CMD_XSYNSETUP        =  33

# state information

READSTAT             =  34
READISTATE           =  35

# load processor and xilinx parameters

LOADVAL              =  36
LOADMULTI            =  37
READVAL              =  38
LOADXREG             =  39
READXREG             =  40

# move command operations

CLEARQUE             =  41
QUEMOVE              =  42
MOVEQUESTATUS        =  43

# location and debug info

READALL              =  44
READDBG              =  45
CLRDBG               =  46

# encoder commands

ENCSTART             =  47
ENCSTOP              =  48

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
    ("MOVEQUESTATUS", None),            #  43
    ("READALL", "readAll"),             #  44
    ("READDBG", "readDbg"),             #  45
    ("CLRDBG", "clearDbg"),             #  46
    ("ENCSTART", None),                 #  47
    ("ENCSTOP", None),                  #  48
    )
