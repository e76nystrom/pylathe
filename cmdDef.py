
# commands

# z motion commands

ZMOVEABS             =   1
ZMOVEREL             =   2
ZJMOV                =   3
ZJSPEED              =   4
ZSTOP                =   5
ZSETLOC              =   6

# x motion commands

XMOVEABS             =   8
XMOVEREL             =   9
XJMOV                =  10
XJSPEED              =  11
XSTOP                =  12
XSETLOC              =  13
XHOMEAXIS            =  14

# spindle operations

SPINDLE_START        =  16
SPINDLE_JOG          =  17
SPINDLE_JOG_SPEED    =  18
SPINDLE_STOP         =  19

# end operations

CMD_PAUSE            =  21
CMD_RESUME           =  22
CMD_STOP             =  23
CMD_MEASURE          =  24

# setup operations

CMD_CLEAR            =  26
CMD_SETUP            =  27
CMD_SPSETUP          =  28
CMD_ZSETUP           =  29
CMD_ZSYNSETUP        =  30
CMD_ZTAPERSETUP      =  31
CMD_XSETUP           =  32
CMD_XSYNSETUP        =  33
CMD_XTAPERSETUP      =  34

# state information

READSTAT             =  36
READISTATE           =  37

# load processor and xilinx parameters

LOADVAL              =  39
LOADMULTI            =  40
READVAL              =  41
LOADXREG             =  42
READXREG             =  43

# move command operations

CLEARQUE             =  45
QUEMOVE              =  46
MOVEQUESTATUS        =  47

# location and debug info

READALL              =  49
READDBG              =  50
CLRDBG               =  51

# encoder commands

ENCSTART             =  53
ENCSTOP              =  54

# command table

cmdTable = ( \
    ("ZMOVEABS", "None"),               #   0
    ("ZMOVEREL", "None"),               #   1
    ("ZJMOV", "None"),                  #   2
    ("ZJSPEED", "None"),                #   3
    ("ZSTOP", "None"),                  #   4
    ("ZSETLOC", "None"),                #   5
    ("XMOVEABS", "None"),               #   6
    ("XMOVEREL", "None"),               #   7
    ("XJMOV", "None"),                  #   8
    ("XJSPEED", "None"),                #   9
    ("XSTOP", "None"),                  #  10
    ("XSETLOC", "None"),                #  11
    ("XHOMEAXIS", "None"),              #  12
    ("SPINDLE_START", "spindleStart"),  #  13
    ("SPINDLE_JOG", "None"),            #  14
    ("SPINDLE_JOG_SPEED", "None"),      #  15
    ("SPINDLE_STOP", "spindleStop"),    #  16
    ("CMD_PAUSE", "pauseCmd"),          #  17
    ("CMD_RESUME", "resumeCmd"),        #  18
    ("CMD_STOP", "stopCmd"),            #  19
    ("CMD_MEASURE", "measureCmd"),      #  20
    ("CMD_CLEAR", "clearCmd"),          #  21
    ("CMD_SETUP", "setup"),             #  22
    ("CMD_SPSETUP", "spindleSetup"),    #  23
    ("CMD_ZSETUP", "zSetup"),           #  24
    ("CMD_ZSYNSETUP", "zSynSetup"),     #  25
    ("CMD_ZTAPERSETUP", "zTaperSetup"), #  26
    ("CMD_XSETUP", "xSetup"),           #  27
    ("CMD_XSYNSETUP", "xSynSetup"),     #  28
    ("CMD_XTAPERSETUP", "xTaperSetup"), #  29
    ("READSTAT", "None"),               #  30
    ("READISTATE", "None"),             #  31
    ("LOADVAL", "None"),                #  32
    ("LOADMULTI", "None"),              #  33
    ("READVAL", "None"),                #  34
    ("LOADXREG", "None"),               #  35
    ("READXREG", "None"),               #  36
    ("CLEARQUE", "None"),               #  37
    ("QUEMOVE", "None"),                #  38
    ("MOVEQUESTATUS", "None"),          #  39
    ("READALL", "None"),                #  40
    ("READDBG", "None"),                #  41
    ("CLRDBG", "None"),                 #  42
    ("ENCSTART", "None"),               #  43
    ("ENCSTOP", "None"),                #  44
    )
