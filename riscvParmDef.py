
# parameters
R_MV_STATUS          =   0	# 0x00
R_JOG_PAUSE          =   1	# 0x01
R_CUR_PASS           =   2	# 0x02
R_CFG_VAL            =   3	# 0x03
R_P_RPM              =   4	# 0x04
R_PWM_DIV            =   5	# 0x05
R_PWM_CTR            =   6	# 0x06
R_P_X_LOC            =   7	# 0x07
R_P_Z_LOC            =   8	# 0x08
R_P_X_DRO            =   9	# 0x09
R_P_Z_DRO            =  10	# 0x0a
R_X_JOG_INC          =  11	# 0x0b
R_Z_JOG_INC          =  12	# 0x0c

parmTable = ( \
    ("R_MV_STATUS", "uint32_t", "rMvStatus"), # 0x00   0
    ("R_JOG_PAUSE", "int",      "rJogPause"), # 0x01   1
    ("R_CUR_PASS",  "int",      "rCurPass" ), # 0x02   2
    ("R_CFG_VAL",   "int",      "rCfgVal"  ), # 0x03   3
    ("R_P_RPM",     "int",      "rPRpm"    ), # 0x04   4
    ("R_PWM_DIV",   "int",      "rPwmDiv"  ), # 0x05   5
    ("R_PWM_CTR",   "int",      "rPwmCtr"  ), # 0x06   6
    ("R_P_X_LOC",   "int",      "rPXLoc"   ), # 0x07   7
    ("R_P_Z_LOC",   "int",      "rPZLoc"   ), # 0x08   8
    ("R_P_X_DRO",   "int",      "rPXDro"   ), # 0x09   9
    ("R_P_Z_DRO",   "int",      "rPZDro"   ), # 0x0a  10
    ("R_X_JOG_INC", "int",      "rXJogInc" ), # 0x0b  11
    ("R_Z_JOG_INC", "int",      "rZJogInc" ), # 0x0c  12
    )
