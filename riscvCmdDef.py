
# commands
R_NONE               =   0	# 0x00
R_READ_ALL           =   1	# 0x01
R_READ_DBG           =   2	# 0x02
R_SETUP              =   3	# 0x03
R_RESUME             =   4	# 0x04
R_STOP               =   5	# 0x05
R_STOP_X             =   6	# 0x06
R_STOP_Z             =   7	# 0x07
R_DONE               =   8	# 0x08
R_SEND_DONE          =   9	# 0x09
R_STR_SPIN           =  10	# 0x0a
R_STP_SPIN           =  11	# 0x0b
R_UPD_SPIN           =  12	# 0x0c
R_SET_LOC_X          =  13	# 0x0d
R_SET_LOC_Z          =  14	# 0x0e
R_SET_ACCEL          =  15	# 0x0f
R_SET_DATA           =  16	# 0x10
R_GET_DATA           =  17	# 0x11
R_JOG_Z              =  18	# 0x12
R_JOG_X              =  19	# 0x13
R_HOME_Z             =  20	# 0x14
R_HOME_X             =  21	# 0x15
R_OP_START           =  22	# 0x16
R_OP_DONE            =  23	# 0x17
R_PAUSE              =  24	# 0x18
R_ENC_SCL_STR        =  25	# 0x19
R_STR_SPIN_Q         =  26	# 0x1a
R_STP_SPIN_Q         =  27	# 0x1b
R_PASS               =  28	# 0x1c
R_SET_ACCEL_Q        =  29	# 0x1d
R_SET_DATA_Q         =  30	# 0x1e
R_MOVE_Z             =  31	# 0x1f
R_MOVE_X             =  32	# 0x20
R_MOVE_REL_Z         =  33	# 0x21
R_MOVE_REL_X         =  34	# 0x22

# command table

cmdTable = ( \
    ("R_NONE",        ), # 0x00  0
    ("R_READ_ALL",    ), # 0x01  1
    ("R_READ_DBG",    ), # 0x02  2
    ("R_SETUP",       ), # 0x03  3
    ("R_RESUME",      ), # 0x04  4
    ("R_STOP",        ), # 0x05  5
    ("R_STOP_X",      ), # 0x06  6
    ("R_STOP_Z",      ), # 0x07  7
    ("R_DONE",        ), # 0x08  8
    ("R_SEND_DONE",   ), # 0x09  9
    ("R_STR_SPIN",    ), # 0x0a 10
    ("R_STP_SPIN",    ), # 0x0b 11
    ("R_UPD_SPIN",    ), # 0x0c 12
    ("R_SET_LOC_X",   ), # 0x0d 13
    ("R_SET_LOC_Z",   ), # 0x0e 14
    ("R_SET_ACCEL",   ), # 0x0f 15
    ("R_SET_DATA",    ), # 0x10 16
    ("R_GET_DATA",    ), # 0x11 17
    ("R_JOG_Z",       ), # 0x12 18
    ("R_JOG_X",       ), # 0x13 19
    ("R_HOME_Z",      ), # 0x14 20
    ("R_HOME_X",      ), # 0x15 21
    ("R_OP_START",    ), # 0x16 22
    ("R_OP_DONE",     ), # 0x17 23
    ("R_PAUSE",       ), # 0x18 24
    ("R_ENC_SCL_STR", ), # 0x19 25
    ("R_STR_SPIN_Q",  ), # 0x1a 26
    ("R_STP_SPIN_Q",  ), # 0x1b 27
    ("R_PASS",        ), # 0x1c 28
    ("R_SET_ACCEL_Q", ), # 0x1d 29
    ("R_SET_DATA_Q",  ), # 0x1e 30
    ("R_MOVE_Z",      ), # 0x1f 31
    ("R_MOVE_X",      ), # 0x20 32
    ("R_MOVE_REL_Z",  ), # 0x21 33
    ("R_MOVE_REL_X",  ), # 0x22 34
    )
