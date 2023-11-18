
# parameters
R_MV_STATUS          =   0	# 0x00
R_JOG_PAUSE          =   1	# 0x01
R_CUR_PASS           =   2	# 0x02
R_P_RPM              =   3	# 0x03
R_P_X_LOC            =   4	# 0x04
R_P_Z_LOC            =   5	# 0x05
R_P_X_DRO            =   6	# 0x06
R_P_Z_DRO            =   7	# 0x07
R_X_JOG_INC          =   8	# 0x08
R_Z_JOG_INC          =   9	# 0x09

parmTable = ( \
    ('R_MV_STATUS', 'uint32_t', 'rMvStatus'),
    ('R_JOG_PAUSE', 'int', 'rJogPause'),
    ('R_CUR_PASS', 'int', 'rCurPass'),
    ('R_P_RPM', 'int', 'rPRpm'),
    ('R_P_X_LOC', 'int', 'rPXLoc'),
    ('R_P_Z_LOC', 'int', 'rPZLoc'),
    ('R_P_X_DRO', 'int', 'rPXDro'),
    ('R_P_Z_DRO', 'int', 'rPZDro'),
    ('R_X_JOG_INC', 'int', 'rXJogInc'),
    ('R_Z_JOG_INC', 'int', 'rZJogInc'),
    )
