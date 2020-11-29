
# commands

# z motion commands

ZMOVEABS             =   0
ZMOVEREL             =   1
ZJMOV                =   2
ZJSPEED              =   3
ZSTOP                =   4
ZSETLOC              =   5
ZHOMEAXIS            =   6

# x motion commands

XMOVEABS             =   7
XMOVEREL             =   8
XJMOV                =   9
XJSPEED              =  10
XSTOP                =  11
XSETLOC              =  12
XHOMEAXIS            =  13

# spindle operations

SPINDLE_START        =  14
SPINDLE_JOG          =  15
SPINDLE_JOG_SPEED    =  16
SPINDLE_STOP         =  17

# end operations

CMD_PAUSE            =  18
CMD_RESUME           =  19
CMD_STOP             =  20
CMD_MEASURE          =  21

# setup operations

CMD_CLEAR            =  22
CMD_SETUP            =  23
CMD_SPSETUP          =  24
CMD_SYNCSETUP        =  25
CMD_ZSETUP           =  26
CMD_ZSYNSETUP        =  27
CMD_XSETUP           =  28
CMD_XSYNSETUP        =  29

# state information

READSTAT             =  30
READISTATE           =  31

# load processor and xilinx parameters

LOADVAL              =  32
LOADMULTI            =  33
READVAL              =  34
LOADXREG             =  35
READXREG             =  36

# move command operations

CLEARQUE             =  37
QUEMOVE              =  38
MOVEQUESTATUS        =  39

# location and debug info

READALL              =  40
READDBG              =  41
CLRDBG               =  42

# encoder commands

ENCSTART             =  43
ENCSTOP              =  44

# command table

cmdTable = ( \
    ("ZMOVEABS", "zMoveAbs"),           #   0
    ("ZMOVEREL", "zMoveRel"),           #   1
    ("ZJMOV", "zJogMove"),              #   2
    ("ZJSPEED", "zJogSpeed"),           #   3
    ("ZSTOP", "zStop"),                 #   4
    ("ZSETLOC", None),                  #   5
    ("ZHOMEAXIS", "zHomeAxis"),         #   6
    ("XMOVEABS", "xMoveAbs"),           #   7
    ("XMOVEREL", "xMoveRel"),           #   8
    ("XJMOV", "xJogMove"),              #   9
    ("XJSPEED", "xJogSpeed"),           #  10
    ("XSTOP", "xStop"),                 #  11
    ("XSETLOC", None),                  #  12
    ("XHOMEAXIS", "xHomeAxis"),         #  13
    ("SPINDLE_START", "spindleStart"),  #  14
    ("SPINDLE_JOG", "spindleJog"),      #  15
    ("SPINDLE_JOG_SPEED", "spindleJogSpeed"),#  16
    ("SPINDLE_STOP", "spindleStop"),    #  17
    ("CMD_PAUSE", "pauseCmd"),          #  18
    ("CMD_RESUME", "resumeCmd"),        #  19
    ("CMD_STOP", "stopCmd"),            #  20
    ("CMD_MEASURE", "measureCmd"),      #  21
    ("CMD_CLEAR", "clearCmd"),          #  22
    ("CMD_SETUP", "setup"),             #  23
    ("CMD_SPSETUP", "spindleSetup"),    #  24
    ("CMD_SYNCSETUP", "syncSetup"),     #  25
    ("CMD_ZSETUP", "zSetup"),           #  26
    ("CMD_ZSYNSETUP", None),            #  27
    ("CMD_XSETUP", "xSetup"),           #  28
    ("CMD_XSYNSETUP", None),            #  29
    ("READSTAT", None),                 #  30
    ("READISTATE", None),               #  31
    ("LOADVAL", None),                  #  32
    ("LOADMULTI", None),                #  33
    ("READVAL", None),                  #  34
    ("LOADXREG", None),                 #  35
    ("READXREG", None),                 #  36
    ("CLEARQUE", "clearQue"),           #  37
    ("QUEMOVE", None),                  #  38
    ("MOVEQUESTATUS", None),            #  39
    ("READALL", "readAll"),             #  40
    ("READDBG", "readDbg"),             #  41
    ("CLRDBG", "clearDbg"),             #  42
    ("ENCSTART", None),                 #  43
    ("ENCSTOP", None),                  #  44
    )
