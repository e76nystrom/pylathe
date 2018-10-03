
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
CMD_XSETUP           =  26
CMD_XSYNSETUP        =  27

# state information

READSTAT             =  28
READISTATE           =  29

# load processor and xilinx parameters

LOADVAL              =  30
LOADMULTI            =  31
READVAL              =  32
LOADXREG             =  33
READXREG             =  34

# move command operations

CLEARQUE             =  35
QUEMOVE              =  36
MOVEQUESTATUS        =  37

# location and debug info

READALL              =  38
READDBG              =  39
CLRDBG               =  40

# encoder commands

ENCSTART             =  41
ENCSTOP              =  42

# ack read

ACKREAD              =  43

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
    ("CMD_XSETUP", "xSetup"),           #  26
    ("CMD_XSYNSETUP", "xSynSetup"),     #  27
    ("READSTAT", "None"),               #  28
    ("READISTATE", "None"),             #  29
    ("LOADVAL", "None"),                #  30
    ("LOADMULTI", "None"),              #  31
    ("READVAL", "None"),                #  32
    ("LOADXREG", "None"),               #  33
    ("READXREG", "None"),               #  34
    ("CLEARQUE", "None"),               #  35
    ("QUEMOVE", "None"),                #  36
    ("MOVEQUESTATUS", "None"),          #  37
    ("READALL", "None"),                #  38
    ("READDBG", "None"),                #  39
    ("CLRDBG", "None"),                 #  40
    ("ENCSTART", "None"),               #  41
    ("ENCSTOP", "None"),                #  42
    ("ACKREAD", "None"),                #  43
    )
