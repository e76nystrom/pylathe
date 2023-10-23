
# parameters
R_MV_STATUS          =   0	# 0x00
R_CUR_PASS           =   1	# 0x01
R_PARM_RPM           =   2	# 0x02
R_PARM_X_LOC         =   3	# 0x03
R_PARM_Z_LOC         =   4	# 0x04
R_PARM_X_DRO         =   5	# 0x05
R_PARM_Z_DRO         =   6	# 0x06

parmTable = ( \
    ('R_MV_STATUS', 'uint32_t', 'rMvStatus'),
    ('R_CUR_PASS', 'int', 'rCurPass'),
    ('R_PARM_RPM', 'int', 'rParmRpm'),
    ('R_PARM_X_LOC', 'int', 'rParmXLoc'),
    ('R_PARM_Z_LOC', 'int', 'rParmZLoc'),
    ('R_PARM_X_DRO', 'int', 'rParmXDro'),
    ('R_PARM_Z_DRO', 'int', 'rParmZDro'),
    )
