
# commands

# z motion commands

C_Z_MOVE_ABS         =   0	# 0x00
C_Z_MOVE_REL         =   1	# 0x01
C_Z_J_MOV            =   2	# 0x02
C_Z_J_SPEED          =   3	# 0x03
C_Z_STOP             =   4	# 0x04
C_Z_SET_LOC          =   5	# 0x05
C_Z_HOME_FWD         =   6	# 0x06
C_Z_HOME_REV         =   7	# 0x07

# x motion commands

C_X_MOVE_ABS         =   8	# 0x08
C_X_MOVE_REL         =   9	# 0x09
C_X_J_MOV            =  10	# 0x0a
C_X_J_SPEED          =  11	# 0x0b
C_X_STOP             =  12	# 0x0c
C_X_SET_LOC          =  13	# 0x0d
C_X_HOME_FWD         =  14	# 0x0e
C_X_HOME_REV         =  15	# 0x0f

# spindle operations

C_SPINDLE_START      =  16	# 0x10
C_SPINDLE_STOP       =  17	# 0x11
C_SPINDLE_UPDATE     =  18	# 0x12
C_SPINDLE_JOG        =  19	# 0x13
C_SPINDLE_JOG_SPEED  =  20	# 0x14

# end operations

C_CMD_PAUSE          =  21	# 0x15
C_CMD_RESUME         =  22	# 0x16
C_CMD_STOP           =  23	# 0x17
C_CMD_DONE           =  24	# 0x18
C_CMD_MEASURE        =  25	# 0x19

# setup operations

C_CMD_CLEAR          =  26	# 0x1a
C_CMD_SETUP          =  27	# 0x1b
C_CMD_SP_SETUP       =  28	# 0x1c
C_CMD_SYNC_SETUP     =  29	# 0x1d
C_CMD_Z_SETUP        =  30	# 0x1e
C_CMD_Z_SYN_SETUP    =  31	# 0x1f
C_CMD_Z_SET_LOC      =  32	# 0x20
C_CMD_X_SETUP        =  33	# 0x21
C_CMD_X_SYN_SETUP    =  34	# 0x22
C_CMD_X_SET_LOC      =  35	# 0x23

# state information

C_READ_STAT          =  36	# 0x24
C_READ_I_STATE       =  37	# 0x25

# load processor and xilinx parameters

C_LOAD_VAL           =  38	# 0x26
C_LOAD_MULTI         =  39	# 0x27
C_READ_VAL           =  40	# 0x28
C_LOAD_X_REG         =  41	# 0x29
C_READ_X_REG         =  42	# 0x2a

# move command operations

C_CLEAR_QUE          =  43	# 0x2b
C_QUE_MOVE           =  44	# 0x2c
C_MOVE_MULTI         =  45	# 0x2d
C_MOVE_QUE_STATUS    =  46	# 0x2e

# location and debug info

C_READ_ALL           =  47	# 0x2f
C_READ_DBG           =  48	# 0x30
C_CLR_DBG            =  49	# 0x31

# encoder commands

C_ENC_START          =  50	# 0x32
C_ENC_STOP           =  51	# 0x33

#  mega commands 

C_SET_MEGA_VAL       =  52	# 0x34
C_READ_MEGA_VAL      =  53	# 0x35
C_SEND_DONE          =  54	# 0x36

# command table

cmdTable = ( \
    ("C_Z_MOVE_ABS",        "cZMoveAbs"       ), # 0x00  0
    ("C_Z_MOVE_REL",        "cZMoveRel"       ), # 0x01  1
    ("C_Z_J_MOV",           "cZJogMove"       ), # 0x02  2
    ("C_Z_J_SPEED",         "cZJogSpeed"      ), # 0x03  3
    ("C_Z_STOP",            "cZStop"          ), # 0x04  4
    ("C_Z_SET_LOC",         None              ), # 0x05  5
    ("C_Z_HOME_FWD",        "cZHomeFwd"       ), # 0x06  6
    ("C_Z_HOME_REV",        "cZHomeRev"       ), # 0x07  7
    ("C_X_MOVE_ABS",        "cXMoveAbs"       ), # 0x08  8
    ("C_X_MOVE_REL",        "cXMoveRel"       ), # 0x09  9
    ("C_X_J_MOV",           "cXJogMove"       ), # 0x0a 10
    ("C_X_J_SPEED",         "cXJogSpeed"      ), # 0x0b 11
    ("C_X_STOP",            "cXStop"          ), # 0x0c 12
    ("C_X_SET_LOC",         None              ), # 0x0d 13
    ("C_X_HOME_FWD",        "cXHomeFwd"       ), # 0x0e 14
    ("C_X_HOME_REV",        "cXHomeRev"       ), # 0x0f 15
    ("C_SPINDLE_START",     "cSpindleStart"   ), # 0x10 16
    ("C_SPINDLE_STOP",      "cSpindleStop"    ), # 0x11 17
    ("C_SPINDLE_UPDATE",    "cSpindleUpdate"  ), # 0x12 18
    ("C_SPINDLE_JOG",       "cSpindleJog"     ), # 0x13 19
    ("C_SPINDLE_JOG_SPEED", "cSpindleJogSpeed"), # 0x14 20
    ("C_CMD_PAUSE",         "cPauseCmd"       ), # 0x15 21
    ("C_CMD_RESUME",        "cResumeCmd"      ), # 0x16 22
    ("C_CMD_STOP",          "cStopCmd"        ), # 0x17 23
    ("C_CMD_DONE",          "cDoneCmd"        ), # 0x18 24
    ("C_CMD_MEASURE",       "cMeasureCmd"     ), # 0x19 25
    ("C_CMD_CLEAR",         "cClearCmd"       ), # 0x1a 26
    ("C_CMD_SETUP",         "cSetup"          ), # 0x1b 27
    ("C_CMD_SP_SETUP",      "cSpindleSetup"   ), # 0x1c 28
    ("C_CMD_SYNC_SETUP",    "cSyncSetup"      ), # 0x1d 29
    ("C_CMD_Z_SETUP",       "cZSetup"         ), # 0x1e 30
    ("C_CMD_Z_SYN_SETUP",   None              ), # 0x1f 31
    ("C_CMD_Z_SET_LOC",     "cZSetLoc"        ), # 0x20 32
    ("C_CMD_X_SETUP",       "cXSetup"         ), # 0x21 33
    ("C_CMD_X_SYN_SETUP",   None              ), # 0x22 34
    ("C_CMD_X_SET_LOC",     "cXSetLoc"        ), # 0x23 35
    ("C_READ_STAT",         None              ), # 0x24 36
    ("C_READ_I_STATE",      None              ), # 0x25 37
    ("C_LOAD_VAL",          None              ), # 0x26 38
    ("C_LOAD_MULTI",        None              ), # 0x27 39
    ("C_READ_VAL",          None              ), # 0x28 40
    ("C_LOAD_X_REG",        None              ), # 0x29 41
    ("C_READ_X_REG",        None              ), # 0x2a 42
    ("C_CLEAR_QUE",         "cClearQue"       ), # 0x2b 43
    ("C_QUE_MOVE",          None              ), # 0x2c 44
    ("C_MOVE_MULTI",        None              ), # 0x2d 45
    ("C_MOVE_QUE_STATUS",   None              ), # 0x2e 46
    ("C_READ_ALL",          "cReadAll"        ), # 0x2f 47
    ("C_READ_DBG",          "cReadDbg"        ), # 0x30 48
    ("C_CLR_DBG",           "cClearDbg"       ), # 0x31 49
    ("C_ENC_START",         None              ), # 0x32 50
    ("C_ENC_STOP",          None              ), # 0x33 51
    ("C_SET_MEGA_VAL",      None              ), # 0x34 52
    ("C_READ_MEGA_VAL",     None              ), # 0x35 53
    ("C_SEND_DONE",         "cSendDone"       ), # 0x36 54
    )
