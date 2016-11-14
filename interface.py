#!/cygdrive/c/Python27/Python.exe

cmdList = \
[\
    "z motion commands",
    
    ["ZMOVEABS", "", "start z movement"],
    ["ZMOVEREL", "", "move z relative"],
    ["ZJMOV", "", "start z jog"],
    ["ZJSPEED", "", "start z jog at speed"],
    ["ZSTOP", "", "stop z movement"],
    ["ZHOME", "", "set current z location as home"],
    ["ZSETLOC", "", ""],
    ["ZGOHOME", "", "z go to home position"],
    
    "x motion commands",
    
    ["XMOVEABS", "", "start x movement"],
    ["XMOVEREL", "", "move x relative"],
    ["XJMOV", "", "start z jog"],
    ["XJSPEED", "", "start x jog at speed"],
    ["XSTOP", "", "stop x movement"],
    ["XHOME", "", "set current x location as home"],
    ["XSETLOC", "", ""],
    ["XGOHOME", "", "x go to home position"],
    ["XHOMEAXIS", "", "x home axis"],
    
    "spindle operations",
    
    ["SPINDLE_START", "spindleStart", "start spindle"],
    ["SPINDLE_JOG", "", "spindle jog"],
    ["SPINDLE_JOG_SPEED", "", "spindle jog at speed"],
    ["SPINDLE_STOP", "spindleStop", "stop spindle"],
    
    "start operations",
    
    ["CMD_TURN", "", "start turn operation"],
    ["CMD_FACE", "", "start face operation"],
    ["CMD_TAPER", "", "start taper operation"],
    ["CMD_ARC", "", "start arc operation"],
    ["CMD_THREAD", "", "start threading operation"],
    
    "end operations",
    
    ["CMD_PAUSE", "pauseCmd", "pause current operation"],
    ["CMD_RESUME", "resumeCmd", "resume current operation"],
    ["CMD_STOP", "stopCmd", "stop current operation"],
    
    "setup operations",
    
    ["CMD_CLEAR", "clearCmd", "clear all tables"],
    ["CMD_SETUP", "setup", "setup everything"],
    ["CMD_SPSETUP", "spindleSetup", "setup spindle"],

    ["CMD_ZSETUP", "zSetup", "setup z axis"],
    ["CMD_ZSYNSETUP", "zSynSetup", "setup z axis sync"],
    ["CMD_ZTAPERSETUP", "zTaperSetup", "setup z axis taper"],

    ["CMD_XSETUP", "xSetup", "setup x axis"],
    ["CMD_XSYNSETUP", "xSynSetup", "setup z axis sync"],
    ["CMD_XTAPERSETUP", "xTaperSetup", "setup z axis taper"],
    
    "state information",
    
    ["READSTAT", "", "read status"],
    ["READISTATE", "", "read states of state machines"],
    
    "load processor and xilinx parameters",
    
    ["LOADVAL", "", "load parameters"],
    ["READVAL", "", "read parameters"],
    ["LOADXREG", "", "load xilinx registers"],
    ["READXREG", "", "read xilinx registers"],

    "move command operations",

    ["CLEARQUE", "", "clear move que"],
    ["QUEMOVE", "", "que move command"],
    ["MOVEQUESTATUS", "", "read move queue status"],
    
    "location and debug info",
    
    ["READLOC", "", "read location"],
    ["READDBG", "", "read debug message"],
    ["CLRDBG", "", "clear debug message buffer"],

    "encoder commands",

    ["ENCSTART", "", "encoder start"],
    ["ENCSTOP", "", "encoder stop"],
]
    
parmList = \
[\
    "spindle parameters",
    
    ["SP_STEPS", "spindle motor steps", "int16_t"],
    ["SP_MICRO", "spindle micro steps", "int16_t"],
    ["SP_MIN_RPM", "spindle minimum rpm", "float"],
    ["SP_MAX_RPM", "spindle maxmum rpm", "float"],
    ["SP_ACCEL_TIME", "spindle accel time", "float"],
    ["SP_ACCEL", "spindle accel rpm/sec^2", "float"],
    ["SP_JOG_MIN_RPM", "spindle jog minimum rpm", "float"],
    ["SP_JOG_MAX_RPM", "spindle jog maxmum rpm", "float"],
    ["SP_JOG_RPM", "spindle jog rpm", "float"],
    ["SP_JOG_ACCEL_TIME", "spindle jog accel time", "float"],
    ["SP_DIR_FLAG", "spindle invert direction", "char"],
    ["SP_TEST_INDEX", "generate test index pulse", "char"],
    
    "z axis parameters",
    
    ["Z_PITCH", "z axis leadscrew pitch", "float"],
    ["Z_RATIO", "z axis ratio", "float"],
    ["Z_MICRO", "z axis micro steps", "int16_t"],
    ["Z_MOTOR", "z axis motor steps", "int16_t"],
    ["Z_ACCEL_TIME", "z axis acceleration", "float"],
    ["Z_ACCEL", "z accel rpm/sec^2", "float"],
    ["Z_BACKLASH", "z axis backlash", "float"],
    ["Z_DIR_FLAG", "z invert direction", "char"],
    ["Z_MPG_FLAG", "z invert mpg", "char"],
    
    "x axis parameters",
    
    ["X_PITCH", "x axis leadscrew pitch", "float"],
    ["X_RATIO", "x axis ratio", "float"],
    ["X_MICRO", "x axis micro steps", "int16_t"],
    ["X_MOTOR", "x axis motor steps", "int16_t"],
    ["X_ACCEL_TIME", "x axis acceleration", "float"],
    ["X_ACCEL", "z accel rpm/sec^2", "float"],
    ["X_BACKLASH", "x axis backlash", "float"],
    ["X_DIR_FLAG", "x invert direction", "char"],
    ["X_MPG_FLAG", "x invert mpg", "char"],
    ["X_DIAMETER", "x diameter", "int"],
    
    "z move parameters",
    
    ["Z_MOVE_MIN", "z move min speed", "float"],
    ["Z_MOVE_MAX", "z move max speed", "float"],
    
    "z jog parameters",
    
    ["Z_JOG_MIN", "z jog min speed", "float"],
    ["Z_JOG_MAX", "z jog max speed", "float"],
    ["Z_JOG_SPEED", "z jog speed", "float"],
    
    "x move parameters",
    
    ["X_MOVE_MIN", "x move min speed", "float"],
    ["X_MOVE_MAX", "x move max speed", "float"],
    
    "x jog parameters",
    
    ["X_JOG_MIN", "x jog min speed", "float"],
    ["X_JOG_MAX", "x jog max speed", "float"],
    ["X_JOG_SPEED", "x jog speed", "float"],
    
    "pass information",
    
    ["TOTAL_PASSES", "total passes", "int16_t"],
    ["CURRENT_PASS", "current passes", "int16_t"],
    
    "z axis move values",
    
    ["Z_MOVE_DIST", "z move distance", "float"],
    ["Z_MOVE_POS", "z move position", "float"],
    ["Z_JOG_DIR", "x jog direction", "int"],
    ["Z_SET_LOC", "z location to set", "float"],
    ["Z_LOC", "z dro location", "int"],
    ["Z_FLAG", "z move flag", "int"],
    ["Z_ABS_LOC", "z absolute location", "int"],
    ["Z_MPG_INC", "z man pulse gen incr", "int"],
    
    "x axis move values",

    ["X_MOVE_DIST", "x move distance", "float"],
    ["X_MOVE_POS", "x move position", "float"],
    ["X_JOG_DIR", "x jog direction", "int"],
    ["X_SET_LOC", "x location to set", "float"],
    ["X_LOC", "x dro location", "int"],
    ["X_FLAG", "x move flag", "int"],
    ["X_ABS_LOC", "x absolute location", "int"],
    ["X_MPG_INC", "X man pulse gen incr", "int"],
    
    # "z turn/face parameters",
    
    # ["Z_START_LOC", "z start", "float"],
    # ["Z_END_LOC", "z end", "float"],
    # ["Z_RETRACT", "z retract", "float"],
    # ["Z_FEED_PASS", "z feed per pass", "float"],
    
    # "x turn/face parameters",
    
    # ["X_START_LOC", "x start", "float"],
    # ["X_END_LOC", "x end", "float"],
    # ["X_RETRACT", "x retract", "float"],
    # ["X_FEED_PASS", "x feed per pass", "float"],
    # ["X_DIAMETER", "x diameter", "int"],
    
    "index pulse variables",

    ["INDEX_PRE_SCALER", "index prescaler", "int"],
    ["LAST_INDEX_PERIOD", "last index period", "int"],
    ["INDEX_PERIOD", "index period", "int"],
    ["REV_COUNTER", "revolutin counter", "unsigned int"],

    # "z home offsets",

    ["Z_HOME_OFFSET", "z offset home to zero", "float"],

    # "z encoder",

    ["Z_ENC_POS", "z encoder location", "int"],
    ["Z_ENC_OFFSET", "z encoder to zero", "float"],
    ["Z_ENC_INCH", "z encoder scale", "int"],
    ["Z_ENC_DIR", "z encoder direction", "int"],

    "x home parameters",

    ["X_HOME_SPEED", "x final homing speed", "float"],
    ["X_HOME_DIST", "x max homing distance", "float"],
    ["X_HOME_BACKOFF_DIST", "x home backoff dist", "float"],
    ["X_HOME_DIR", "x homing direction", "int"],

    "x home test parameters",

    ["X_HOME_LOC", "x home test location", "int"],
    ["X_HOME_START", "x start of home signal", "int"],
    ["X_HOME_END", "x end of home signal", "int"],

    # "x home offset",

    ["X_HOME_OFFSET", "x offset home to zero", "float"],

    # "x encoder",

    ["X_ENC_POS", "x encoder location", "int"],
    ["X_ENC_OFFSET", "x encoder to zero", "float"],
    ["X_ENC_INCH", "x encoder scale", "int"],
    ["X_ENC_DIR", "x encoder direction", "int"],

    "x home status",

    ["X_HOME_DONE", "x home done", "int"],
    ["X_HOME_STATUS", "x home status", "int"],

    "configuration",

    ["STEPPER_DRIVE", "stepper driven spindle", "char"],
    ["CFG_XILINX", "using xilinx", "char"],
    ["CFG_MPG", "manual pulse generator", "char"],
    ["CFG_DRO", "digital readout", "char"],
    ["CFG_LCD", "lcd display", "char"],
    ["CFG_FCY", "system clock speed", "int"],

    "setup",

    ["SETUP_DONE", "setup done", "char"],

    "encoder counts per revolution",

    ["ENC_MAX", "encoder counts per revolution", "uint16_t"],

    "test encoder setup variables",

    ["ENC_ENABLE", "encoder enable flag", "char"],
    ["ENC_PRE_SCALER", "encoder prescaler", "uint16_t"],
    ["ENC_TIMER", "encoder timer counts", "uint16_t"],
    ["ENC_RUN_COUNT", "encoder run count", "int"],

    "test encoder status variables",

    ["ENC_RUN", "encoder running flag", "char"],
    ["ENC_COUNTER", "encoder count in rev", "int16_t"],
    ["ENC_REV_COUNTER", "encoder revolution counter", "int32_t"],
 
    "measured spindle speed",

    ["RPM", "current rpm", "int16_t"],

    "xilinx frequency variables",

    ["X_FREQUENCY", "xilinx clock frequency", "int32_t"],
    ["FREQ_MULT", "frequency multiplier", "int16_t"],

    "xilinx configuration register",

    ["X_CFG_REG", "xilinx configuration register", "int16_t"],
 
    
    # ["", "", ""],

    "max parameter number",

    ["MAX_PARM", "maximum parameter", "int16_t"]
]
    
regList =\
[\
    "z move command bits",
    
    ["ZMSK", "(7 << 0)", "z move mask"],
    ["ZMOV", "(1 << 0)", "z a set distance"],
    ["ZJOG", "(2 << 0)", "z while cmd are present"],
    ["ZSYN", "(3 << 0)", "z dist sync to rotation"],
    ["ZMAX", "(4 << 0)", "z rapid move"],
    ["ZSPEED", "(5 << 0)", "z jog at speed"],
    ["Z_SYN_START", "(1 << 4)", "start on sync pulse"],
    ["X_SYN_TAPER", "(1 << 5)", "taper on x"],
    
    "z direction",
    
    ["ZPOS", "1", "z in positive direction"],
    ["ZNEG", "-1", "z in negative direction"],
    
    "x move command bits",
    
    ["XMSK", "(7 << 0)", "xmove mask"],
    ["XMOV", "(1 << 0)", "x a set distance"],
    ["XJOG", "(2 << 0)", "x while cmd are present"],
    ["XSYN", "(3 << 0)", "x dist sync to rotation"],
    ["XMAX", "(4 << 0)", "x rapid move"],
    ["XSPEED", "(5 << 0)", "z jog at speed"],
    ["XJOGSLOW", "(6 << 0)", "slow jog for finding home"],
    ["X_SYN_START", "(1 << 4)", "start on sync pulse"],
    ["Z_SYN_TAPER", "(1 << 5)", "taper on z"],
    ["XFIND_HOME", "(1 << 6)", "find home"],
    ["XCLEAR_HOME", "(1 << 7)", "move off of home"],
     
    "x direction",
    
    ["XPOS", "1", "x in positive direction"],
    ["XNEG", "-1", "x in negative direction"],
    
    "feed types",
    
    ["FEED_PITCH", "0", "feed inch per rev"],
    ["FEED_TPI", "1", "feed threads per inch"],
    ["FEED_METRIC", "2", "feed mm per rev"],

    "home flag",

    ["FIND_HOME", "(1 << 0)", ""],
    ["CLEAR_HOME", "(1 << 1)", ""],
    ["HOME_ACTIVE", "0", ""],
    ["HOME_SUCCESS", "1", ""],
    ["HOME_FAIL", "2", ""],

    # ["", "", ""],
]
xilinxList = \
[ \
    "skip register zero",

    ["XNOOP", "register 0"],

    "load control registers",

    ["XLDZCTL", "z control register"],
    ["XLDXCTL", "x control register"],
    ["XLDTCTL", "load taper control"],
    ["XLDPCTL", "position control"],
    ["XLDCFG", "configuration"],
    ["XLDDCTL", "load debug control"],
    ["XLDDREG", "load display reg"],
    ["XREADREG", "read register"],

    "status register",

    ["XRDSR", "read status register"],

    "phase counter",

    ["XLDPHASE", "load phase max"],

    "load z motion",

    ["XLDZFREQ", "load z frequency"],
    ["XLDZD", "load z initial d"],
    ["XLDZINCR1", "load z incr1"],
    ["XLDZINCR2", "load z incr2"],
    ["XLDZACCEL", "load z syn accel"],
    ["XLDZACLCNT", "load z syn acl cnt"],
    ["XLDZDIST", "load z distance"],
    ["XLDZLOC", "load z location"],

    "load x motion",

    ["XLDXFREQ", "load x frequency"],
    ["XLDXD", "load x initial d"],
    ["XLDXINCR1", "load x incr1"],
    ["XLDXINCR2", "load x incr2"],
    ["XLDXACCEL", "load x syn accel"],
    ["XLDXACLCNT", "load x syn acl cnt"],
    ["XLDXDIST", "load x distance"],
    ["XLDXLOC", "load x location"],

    "read z motion",

    ["XRDZSUM", "read z sync sum"],
    ["XRDZXPOS", "read z sync x pos"],
    ["XRDZYPOS", "read z sync y pos"],
    ["XRDZACLSUM", "read z acl sum"],
    ["XRDZASTP", "read z acl stps"],

    "read x motion",

    ["XRDXSUM", "read x sync sum"],
    ["XRDXXPOS", "read x sync x pos"],
    ["XRDXYPOS", "read x sync y pos"],
    ["XRDXACLSUM", "read x acl sum"],
    ["XRDXASTP", "read z acl stps"],

    "read distance",

    ["XRDZDIST", "read z distance"],
    ["XRDXDIST", "read x distance"],

    "read location",

    ["XRDZLOC", "read z location"],
    ["XRDXLOC", "read x location"],

    "read frequency and state",

    ["XRDFREQ",  "read encoder freq"],
    ["XCLRFREQ", "clear freq register"],
    ["XRDSTATE", "read state info"],

    "read phase",

    ["XRDPSYN", "read sync phase val"],
    ["XRDTPHS", "read tot phase val"],

    "phase limit info",

    ["XLDZLIM", "load z limit"],
    ["XRDZPOS", "read z position"],

    "test info",

    ["XLDTFREQ", "load test freq"],
    ["XLDTCOUNT", "load test count"],

    "read control regs",

    ["XRDZCTL", "read control regiisters"],
    ["XRDXCTL", "read control regiisters"]
]

xilinxBitList = \
[\
    "z control register",

    ["zCtl"],
    ["zReset",      1, 0, "reset flag"],
    ["zStart",      1, 1, "start z"],
    ["zSrc_Syn",    1, 2, "run z synchronized"],
    ["zSrc_Frq",    0, 2, "run z from clock source"],
    ["zDir_In",     1, 3, "move z in positive dir"],
    ["zDir_Pos",    1, 3, "move z in positive dir"],
    ["zDir_Neg",    0, 3, "move z in negative dir"],
    ["zSet_Loc",    1, 4, "set z location"],
    ["zBacklash",   1, 5, "backlash move no pos upd"],
    ["zWait_Sync",  1, 6, "wait for sync to start"],

    "x control register",

    ["xCtl"],
    ["xReset",      1, 0, "x reset"],
    ["xStart",      1, 1, "start x"],
    ["xSrc_Syn",    1, 2, "run x synchronized"],
    ["xSrc_Frq",    0, 2, "run x from clock source"],
    ["xDir_In",     1, 3, "move x in positive dir"],
    ["xDir_Pos",    1, 3, "x positive direction"],
    ["xDir_Neg",    0, 3, "x negative direction"],
    ["xSet_Loc",    1, 4, "set x location"],
    ["xBacklash",   1, 5, "x backlash move no pos upd"],

    "taper control register",

    ["tCtl"],
    ["tEna",     1, 0, "taper enable"],
    ["tZ",       1, 1, "one for taper z"],
    ["tX",       0, 1, "zero for taper x"],

    "position control register",

    ["pCtl"],
    ["pReset",    1, 0, "reset position"],
    ["pLimit",    1, 1, "set flag on limit reached"],
    ["pZero",     1, 2, "set flag on zero reached"],

    "configuration register",

    ["cCtl"],
    ["zStep_Pol",  1, 0, "z step pulse polarity"],
    ["zDir_Pol",   1, 1, "z direction polarity"],
    ["xStep_Pol",  1, 2, "x step pulse polarity"],
    ["xDir_Pol",   1, 3, "x direction polarity"],
    ["enc_Pol",    1, 4, "encoder dir polarity"],
    ["zPulse_Mult",1, 5, "enable pulse multiplier"],

    "debug control register",

    ["dCtl"],
    ["Dbg_Ena",    1, 0, "enable debugging"],
    ["Dbg_Sel",    1, 1, "select dbg encoder"],
    ["Dbg_Dir",    1, 2, "debug direction"],
    ["Dbg_Count",  1, 3, "gen count num dbg clks"],
    ["Dbg_Init",   1, 4, "init z modules"],
    ["Dbg_Rsyn",   1, 5, "running in sync mode"],
    ["Dbg_Move",   1, 6, "used debug clock for move"],

 "status register",

    ["stat"],
    ["s_Z_Done_Int", 1, 0, "z done interrrupt"],
    ["s_X_Done_Int", 1, 1, "x done interrupt"],
    ["s_Dbg_Done",   1, 2, "debug done"],
    ["s_Z_Start",    1, 3, "z start"],
    ["s_X_Start",    1, 4, "x start"],
    ["s_Enc_Dir_In", 1, 5, "encoder direction in"],

    ""
]
    
stateList =\
[\
    "z control states",

    "enum zStates",
    "{",
    ["ZIDLE", "idle"],
    ["ZWAITBKLS", "wait for backlash move complete"],
    ["ZSTARTMOVE", "start z move"],
    ["ZWAITMOVE", "wait for move complete"],
    ["ZDONE", "clean up state"],
    "};",
    
    "x control states",
    
    "enum xStates",
    "{",
    ["XIDLE", "idle"],
    ["XWAITBKLS", "wait for backlash move complete"],
    ["XSTARTMOVE", "start x move"],
    ["XWAITMOVE", "wait for move complete"],
    ["XDONE", "clean up state"],
    "};",
    
    "move control states",
    
    "enum M_STATES",
    "{",
    ["M_IDLE", "idle state"],
    ["M_WAIT_Z", "wait for z to complete"],
    ["M_WAIT_X", "wait for x to complete"],
    ["M_WAIT_SPINDLE", "wait for spindle start"],
    "};",

    "move control commands",
    
    "enum M_COMMANDS",
    "{",
    ["MOVE_Z", "move z"],
    ["MOVE_X", "move x"],
    ["SAVE_Z", "save z"],
    ["SAVE_X", "save x"],
    ["SAVE_Z_OFFSET", "save z offset"],
    ["SAVE_X_OFFSET", "save z offset"],
    ["SAVE_TAPER", "save taper"],
    ["MOVE_ZX", "move x in sync with z"],
    ["MOVE_XZ", "move z in sync with x"],
    ["TAPER_ZX", "taper x"],
    ["TAPER_XZ", "taper z"],
    ["START_SPINDLE", "spindle start"],
    ["STOP_SPINDLE", "spindle stop"],
    ["Z_SYN_SETUP", "z sync setup"],
    ["X_SYN_SETUP", "x sync setup"],
    ["PASS_NUM", "set pass number"],
    ["QUE_PAUSE", "pause queue"],
    ["SAVE_DIAMETER", "save turn diameter"],
    ["SAVE_FEED_TYPE", "save feed type"],
    ["Z_FEED_SETUP", "setup z feed"],
    ["X_FEED_SETUP", "setup x feed"],
    "};",

    "home control states",
    
    "enum H_STATES",
    "{",
    ["H_IDLE", "idle state"],
    ["H_CHECK_ONHOME", ""],
    ["H_WAIT_FINDHOME", ""],
    ["H_BACKOFF_HOME", ""],
    ["H_WAIT_BACKOFF", ""],
    ["H_WAIT_SLOWFIND", ""],
    # ["H_", ""],
    "};",
]
    
if __name__ == '__main__':
    import os
    from setup import createCommands, createParameters,\
        createCtlBits, createCtlStates, createXilinxReg, createXilinxBits

    # print os.path.realpath(__file__)
    # print os.getcwd()

    path = os.path.dirname(os.path.realpath(__file__))

    fData = True
    cLoc = path + '/../Lathe/include/'
    xLoc = path + '/../../Xilinx/LatheCtl/'

    print "creating interface files"
    createCommands(cmdList, cLoc, fData)
    createParameters(parmList, cLoc, fData)
    createCtlBits(regList, cLoc, fData)
    createCtlStates(stateList, cLoc, fData)
    createXilinxReg(xilinxList, cLoc, xLoc, fData)
    createXilinxBits(xilinxBitList, cLoc, xLoc, fData)
