
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
CMD_ZSETUP           =  24
CMD_ZSYNSETUP        =  25
CMD_ZTAPERSETUP      =  26
CMD_XSETUP           =  27
CMD_XSYNSETUP        =  28
CMD_XTAPERSETUP      =  29

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
