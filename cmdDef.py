
# commands

# z motion commands

ZMOVEABS             =   0
ZMOVEREL             =   1
ZJMOV                =   2
ZJSPEED              =   3
ZSTOP                =   4
ZSETLOC              =   5

# x motion commands

XMOVEABS             =   6
XMOVEREL             =   7
XJMOV                =   8
XJSPEED              =   9
XSTOP                =  10
XSETLOC              =  11
XHOMEAXIS            =  12

# spindle operations

SPINDLE_START        =  13
SPINDLE_JOG          =  14
SPINDLE_JOG_SPEED    =  15
SPINDLE_STOP         =  16

# end operations

CMD_PAUSE            =  17
CMD_RESUME           =  18
CMD_STOP             =  19
CMD_MEASURE          =  20

# setup operations

CMD_CLEAR            =  21
CMD_SETUP            =  22
CMD_SPSETUP          =  23
CMD_SYNCSETUP        =  24
CMD_ZSETUP           =  25
CMD_ZSYNSETUP        =  26
CMD_XSETUP           =  27
CMD_XSYNSETUP        =  28

# state information

READSTAT             =  29
READISTATE           =  30

# load processor and xilinx parameters

LOADVAL              =  31
LOADMULTI            =  32
READVAL              =  33
LOADXREG             =  34
READXREG             =  35

# move command operations

CLEARQUE             =  36
QUEMOVE              =  37
MOVEQUESTATUS        =  38

# location and debug info

READALL              =  39
READDBG              =  40
CLRDBG               =  41

# encoder commands

ENCSTART             =  42
ENCSTOP              =  43

# command table

cmdTable = ( \
    ("ZMOVEABS", "zMoveAbs"),           #   0
    ("ZMOVEREL", "zMoveRel"),           #   1
    ("ZJMOV", "zJogMove"),              #   2
    ("ZJSPEED", "zJogSpeed"),           #   3
    ("ZSTOP", "zStop"),                 #   4
    ("ZSETLOC", None),                  #   5
    ("XMOVEABS", "xMoveAbs"),           #   6
    ("XMOVEREL", "xMoveRel"),           #   7
    ("XJMOV", "xJogMove"),              #   8
    ("XJSPEED", "xJogSpeed"),           #   9
    ("XSTOP", "xStop"),                 #  10
    ("XSETLOC", None),                  #  11
    ("XHOMEAXIS", "xHomeAxis"),         #  12
    ("SPINDLE_START", "spindleStart"),  #  13
    ("SPINDLE_JOG", "spindleJog"),      #  14
    ("SPINDLE_JOG_SPEED", "spindleJogSpeed"),#  15
    ("SPINDLE_STOP", "spindleStop"),    #  16
    ("CMD_PAUSE", "pauseCmd"),          #  17
    ("CMD_RESUME", "resumeCmd"),        #  18
    ("CMD_STOP", "stopCmd"),            #  19
    ("CMD_MEASURE", "measureCmd"),      #  20
    ("CMD_CLEAR", "clearCmd"),          #  21
    ("CMD_SETUP", "setup"),             #  22
    ("CMD_SPSETUP", "spindleSetup"),    #  23
    ("CMD_SYNCSETUP", "syncSetup"),     #  24
    ("CMD_ZSETUP", "zSetup"),           #  25
    ("CMD_ZSYNSETUP", None),            #  26
    ("CMD_XSETUP", "xSetup"),           #  27
    ("CMD_XSYNSETUP", None),            #  28
    ("READSTAT", None),                 #  29
    ("READISTATE", None),               #  30
    ("LOADVAL", None),                  #  31
    ("LOADMULTI", None),                #  32
    ("READVAL", None),                  #  33
    ("LOADXREG", None),                 #  34
    ("READXREG", None),                 #  35
    ("CLEARQUE", "clearQue"),           #  36
    ("QUEMOVE", None),                  #  37
    ("MOVEQUESTATUS", None),            #  38
    ("READALL", "readAll"),             #  39
    ("READDBG", "readDbg"),             #  40
    ("CLRDBG", "clearDbg"),             #  41
    ("ENCSTART", None),                 #  42
    ("ENCSTOP", None),                  #  43
    )
