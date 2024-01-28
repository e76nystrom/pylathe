
# parameters
R_MV_STATUS          =   0	# 0x00
R_JOG_PAUSE          =   1	# 0x01
R_CUR_PASS           =   2	# 0x02
R_CFG_VAL            =   3	# 0x03
R_SP_RPM             =   4	# 0x04
R_PWM_DIV            =   5	# 0x05
R_PWM_CTR            =   6	# 0x06
R_SYN_ENC_PRE_SCALER =   7	# 0x07
R_SYN_ENC_CYCLE      =   8	# 0x08
R_SYN_OUT_CYCLE      =   9	# 0x09
R_STEP_DRV           =  10	# 0x0a
R_ENC_PER_REV        =  11	# 0x0b
R_SP_STEP_MULT       =  12	# 0x0c
R_TURN_SYNC          =  13	# 0x0d
R_THREAD_SYNC        =  14	# 0x0e
R_RUNOUT_SYNC        =  15	# 0x0f
R_THREAD_FLAGS       =  16	# 0x10
R_RUNOUT_DIST        =  17	# 0x11
R_RUNOUT_DEPTH       =  18	# 0x12
R_Z_STEPS_INCH       =  19	# 0x13
R_Z_SAVED_LOC        =  20	# 0x14
R_Z_HOME_OFFSET      =  21	# 0x15
R_Z_LOC              =  22	# 0x16
R_Z_DRO              =  23	# 0x17
R_Z_JOG_INC          =  24	# 0x18
R_Z_HOME_STATUS      =  25	# 0x19
R_Z_HOME_FIND_FWD    =  26	# 0x1a
R_Z_HOME_FIND_REV    =  27	# 0x1b
R_Z_HOME_BACKOFF     =  28	# 0x1c
R_Z_HOME_SLOW        =  29	# 0x1d
R_Z_TEST_LIM_MIN     =  30	# 0x1e
R_Z_TEST_LIM_MAX     =  31	# 0x1f
R_Z_TEST_HOME_MIN    =  32	# 0x20
R_Z_TEST_HOME_MAX    =  33	# 0x21
R_Z_TEST_PROBE       =  34	# 0x22
R_X_STEPS_INCH       =  35	# 0x23
R_X_SAVED_LOC        =  36	# 0x24
R_X_HOME_OFFSET      =  37	# 0x25
R_X_LOC              =  38	# 0x26
R_X_DRO              =  39	# 0x27
R_X_JOG_INC          =  40	# 0x28
R_X_HOME_STATUS      =  41	# 0x29
R_X_HOME_FIND_FWD    =  42	# 0x2a
R_X_HOME_FIND_REV    =  43	# 0x2b
R_X_HOME_BACKOFF     =  44	# 0x2c
R_X_HOME_SLOW        =  45	# 0x2d
R_X_TEST_LIM_MIN     =  46	# 0x2e
R_X_TEST_LIM_MAX     =  47	# 0x2f
R_X_TEST_HOME_MIN    =  48	# 0x30
R_X_TEST_HOME_MAX    =  49	# 0x31
R_X_TEST_PROBE       =  50	# 0x32

riscvParmTable = ( \
    ("R_MV_STATUS",          "uint32_t", "rMvStatus"       ), # 0x00   0
    ("R_JOG_PAUSE",          "int",      "rJogPause"       ), # 0x01   1
    ("R_CUR_PASS",           "int",      "rCurPass"        ), # 0x02   2
    ("R_CFG_VAL",            "int",      "rCfgVal"         ), # 0x03   3
    ("R_SP_RPM",             "int",      "rSpRpm"          ), # 0x04   4
    ("R_PWM_DIV",            "int",      "rPwmDiv"         ), # 0x05   5
    ("R_PWM_CTR",            "int",      "rPwmCtr"         ), # 0x06   6
    ("R_SYN_ENC_PRE_SCALER", "int",      "rSynEncPreScaler"), # 0x07   7
    ("R_SYN_ENC_CYCLE",      "int",      "rSynEncCycle"    ), # 0x08   8
    ("R_SYN_OUT_CYCLE",      "int",      "rSynOutCycle"    ), # 0x09   9
    ("R_STEP_DRV",           "int",      "rStepDrv"        ), # 0x0a  10
    ("R_ENC_PER_REV",        "int",      "rEncPerRev"      ), # 0x0b  11
    ("R_SP_STEP_MULT",       "int",      "rSpStepMult"     ), # 0x0c  12
    ("R_TURN_SYNC",          "int",      "rTurnSync"       ), # 0x0d  13
    ("R_THREAD_SYNC",        "int",      "rThreadSync"     ), # 0x0e  14
    ("R_RUNOUT_SYNC",        "int",      "rRunoutSync"     ), # 0x0f  15
    ("R_THREAD_FLAGS",       "int",      "rThreadFlags"    ), # 0x10  16
    ("R_RUNOUT_DIST",        "int",      "rRunoutDist"     ), # 0x11  17
    ("R_RUNOUT_DEPTH",       "int",      "rRunoutDepth"    ), # 0x12  18
    ("R_Z_STEPS_INCH",       "int",      "rZStepsInch"     ), # 0x13  19
    ("R_Z_SAVED_LOC",        "int",      "rZSavedLoc"      ), # 0x14  20
    ("R_Z_HOME_OFFSET",      "int",      "rZHomeOffset"    ), # 0x15  21
    ("R_Z_LOC",              "int",      "rZLoc"           ), # 0x16  22
    ("R_Z_DRO",              "int",      "rZDro"           ), # 0x17  23
    ("R_Z_JOG_INC",          "int",      "rZJogInc"        ), # 0x18  24
    ("R_Z_HOME_STATUS",      "int",      "rZHomeStatus"    ), # 0x19  25
    ("R_Z_HOME_FIND_FWD",    "int",      "rZHomeFindFwd"   ), # 0x1a  26
    ("R_Z_HOME_FIND_REV",    "int",      "rZHomeFindRev"   ), # 0x1b  27
    ("R_Z_HOME_BACKOFF",     "int",      "rZHomeBackoff"   ), # 0x1c  28
    ("R_Z_HOME_SLOW",        "int",      "rZHomeSlow"      ), # 0x1d  29
    ("R_Z_TEST_LIM_MIN",     "int",      "rZTestLimMin"    ), # 0x1e  30
    ("R_Z_TEST_LIM_MAX",     "int",      "rZTestLimMax"    ), # 0x1f  31
    ("R_Z_TEST_HOME_MIN",    "int",      "rZTestHomeMin"   ), # 0x20  32
    ("R_Z_TEST_HOME_MAX",    "int",      "rZTestHomeMax"   ), # 0x21  33
    ("R_Z_TEST_PROBE",       "int",      "rZTestProbe"     ), # 0x22  34
    ("R_X_STEPS_INCH",       "int",      "rXStepsInch"     ), # 0x23  35
    ("R_X_SAVED_LOC",        "int",      "rXSavedLoc"      ), # 0x24  36
    ("R_X_HOME_OFFSET",      "int",      "rXHomeOffset"    ), # 0x25  37
    ("R_X_LOC",              "int",      "rXLoc"           ), # 0x26  38
    ("R_X_DRO",              "int",      "rXDro"           ), # 0x27  39
    ("R_X_JOG_INC",          "int",      "rXJogInc"        ), # 0x28  40
    ("R_X_HOME_STATUS",      "int",      "rXHomeStatus"    ), # 0x29  41
    ("R_X_HOME_FIND_FWD",    "int",      "rXHomeFindFwd"   ), # 0x2a  42
    ("R_X_HOME_FIND_REV",    "int",      "rXHomeFindRev"   ), # 0x2b  43
    ("R_X_HOME_BACKOFF",     "int",      "rXHomeBackoff"   ), # 0x2c  44
    ("R_X_HOME_SLOW",        "int",      "rXHomeSlow"      ), # 0x2d  45
    ("R_X_TEST_LIM_MIN",     "int",      "rXTestLimMin"    ), # 0x2e  46
    ("R_X_TEST_LIM_MAX",     "int",      "rXTestLimMax"    ), # 0x2f  47
    ("R_X_TEST_HOME_MIN",    "int",      "rXTestHomeMin"   ), # 0x30  48
    ("R_X_TEST_HOME_MAX",    "int",      "rXTestHomeMax"   ), # 0x31  49
    ("R_X_TEST_PROBE",       "int",      "rXTestProbe"     ), # 0x32  50
    )
