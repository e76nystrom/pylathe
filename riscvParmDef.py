
# parameters
R_MV_STATUS          =   0	# 0x00
R_JOG_PAUSE          =   1	# 0x01
R_CUR_PASS           =   2	# 0x02
R_CFG_VAL            =   3	# 0x03
R_P_RPM              =   4	# 0x04
R_PWM_DIV            =   5	# 0x05
R_PWM_CTR            =   6	# 0x06
R_Z_STEPS_INCH       =   7	# 0x07
R_Z_SAVED_LOC        =   8	# 0x08
R_Z_HOME_OFFSET      =   9	# 0x09
R_Z_LOC              =  10	# 0x0a
R_Z_DRO              =  11	# 0x0b
R_Z_JOG_INC          =  12	# 0x0c
R_Z_HOME_STATUS      =  13	# 0x0d
R_Z_HOME_FIND_FWD    =  14	# 0x0e
R_Z_HOME_FIND_REV    =  15	# 0x0f
R_Z_HOME_BACKOFF     =  16	# 0x10
R_Z_HOME_SLOW        =  17	# 0x11
R_Z_TEST_LIM_MIN     =  18	# 0x12
R_Z_TEST_LIM_MAX     =  19	# 0x13
R_Z_TEST_HOME_MIN    =  20	# 0x14
R_Z_TEST_HOME_MAX    =  21	# 0x15
R_Z_TEST_PROBE       =  22	# 0x16
R_X_STEPS_INCH       =  23	# 0x17
R_X_SAVED_LOC        =  24	# 0x18
R_X_HOME_OFFSET      =  25	# 0x19
R_X_LOC              =  26	# 0x1a
R_X_DRO              =  27	# 0x1b
R_X_JOG_INC          =  28	# 0x1c
R_X_HOME_STATUS      =  29	# 0x1d
R_X_HOME_FIND_FWD    =  30	# 0x1e
R_X_HOME_FIND_REV    =  31	# 0x1f
R_X_HOME_BACKOFF     =  32	# 0x20
R_X_HOME_SLOW        =  33	# 0x21
R_X_TEST_LIM_MIN     =  34	# 0x22
R_X_TEST_LIM_MAX     =  35	# 0x23
R_X_TEST_HOME_MIN    =  36	# 0x24
R_X_TEST_HOME_MAX    =  37	# 0x25
R_X_TEST_PROBE       =  38	# 0x26

riscvParmTable = ( \
    ("R_MV_STATUS",       "uint32_t", "rMvStatus"    ), # 0x00   0
    ("R_JOG_PAUSE",       "int",      "rJogPause"    ), # 0x01   1
    ("R_CUR_PASS",        "int",      "rCurPass"     ), # 0x02   2
    ("R_CFG_VAL",         "int",      "rCfgVal"      ), # 0x03   3
    ("R_P_RPM",           "int",      "rPRpm"        ), # 0x04   4
    ("R_PWM_DIV",         "int",      "rPwmDiv"      ), # 0x05   5
    ("R_PWM_CTR",         "int",      "rPwmCtr"      ), # 0x06   6
    ("R_Z_STEPS_INCH",    "int",      "rZStepsInch"  ), # 0x07   7
    ("R_Z_SAVED_LOC",     "int",      "rZSavedLoc"   ), # 0x08   8
    ("R_Z_HOME_OFFSET",   "int",      "rZHomeOffset" ), # 0x09   9
    ("R_Z_LOC",           "int",      "rZLoc"        ), # 0x0a  10
    ("R_Z_DRO",           "int",      "rZDro"        ), # 0x0b  11
    ("R_Z_JOG_INC",       "int",      "rZJogInc"     ), # 0x0c  12
    ("R_Z_HOME_STATUS",   "int",      "rZHomeStatus" ), # 0x0d  13
    ("R_Z_HOME_FIND_FWD", "int",      "rZHomeFindFwd"), # 0x0e  14
    ("R_Z_HOME_FIND_REV", "int",      "rZHomeFindRev"), # 0x0f  15
    ("R_Z_HOME_BACKOFF",  "int",      "rZHomeBackoff"), # 0x10  16
    ("R_Z_HOME_SLOW",     "int",      "rZHomeSlow"   ), # 0x11  17
    ("R_Z_TEST_LIM_MIN",  "int",      "rZTestLimMin" ), # 0x12  18
    ("R_Z_TEST_LIM_MAX",  "int",      "rZTestLimMax" ), # 0x13  19
    ("R_Z_TEST_HOME_MIN", "int",      "rZTestHomeMin"), # 0x14  20
    ("R_Z_TEST_HOME_MAX", "int",      "rZTestHomeMax"), # 0x15  21
    ("R_Z_TEST_PROBE",    "int",      "rZTestProbe"  ), # 0x16  22
    ("R_X_STEPS_INCH",    "int",      "rXStepsInch"  ), # 0x17  23
    ("R_X_SAVED_LOC",     "int",      "rXSavedLoc"   ), # 0x18  24
    ("R_X_HOME_OFFSET",   "int",      "rXHomeOffset" ), # 0x19  25
    ("R_X_LOC",           "int",      "rXLoc"        ), # 0x1a  26
    ("R_X_DRO",           "int",      "rXDro"        ), # 0x1b  27
    ("R_X_JOG_INC",       "int",      "rXJogInc"     ), # 0x1c  28
    ("R_X_HOME_STATUS",   "int",      "rXHomeStatus" ), # 0x1d  29
    ("R_X_HOME_FIND_FWD", "int",      "rXHomeFindFwd"), # 0x1e  30
    ("R_X_HOME_FIND_REV", "int",      "rXHomeFindRev"), # 0x1f  31
    ("R_X_HOME_BACKOFF",  "int",      "rXHomeBackoff"), # 0x20  32
    ("R_X_HOME_SLOW",     "int",      "rXHomeSlow"   ), # 0x21  33
    ("R_X_TEST_LIM_MIN",  "int",      "rXTestLimMin" ), # 0x22  34
    ("R_X_TEST_LIM_MAX",  "int",      "rXTestLimMax" ), # 0x23  35
    ("R_X_TEST_HOME_MIN", "int",      "rXTestHomeMin"), # 0x24  36
    ("R_X_TEST_HOME_MAX", "int",      "rXTestHomeMax"), # 0x25  37
    ("R_X_TEST_PROBE",    "int",      "rXTestProbe"  ), # 0x26  38
    )
