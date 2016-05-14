#!/cygdrive/c/Python27/Python.exe

cmdList = \
[\
    "z motion commands",

    ["ZMOVE", "", "start z movement"],
    ["ZJMOV", "", "start z jog"],
    ["ZSTOP", "", "stop z movement"],
    ["ZHOME", "", "set current z location as home"],
    ["ZSETLOC", "", "set current z location"],
    ["ZGOHOME", "", "z go to home position"],

    "x motion commands",

    ["XMOVE", "", "start x movement"],
    ["XJMOV", "", "start x jog"],
    ["XSTOP", "", "stop x movement"],
    ["XHOME", "", "set current x location as home"],
    ["XSETLOC", "", "set current x location"],
    ["XGOHOME", "", "x go to home position"],

    "spindle operations",
    
    ["SPINDLE_START", "spindleStart", "start spindle"],
    ["SPINDLE_STOP", "spindleStop", "stop spindle"],
    
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

    ["SENDMOVE", "", "send move command"],
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
    
    ["SPIN_STEPS", "spindle motor steps", "int16_t"],
    ["SPIN_MICRO", "spindle micro steps", "int16_t"],
    ["SPIN_MIN_RPM", "spindle minimum rpm", "float"],
    ["SPIN_MAX_RPM", "spindle maxmum rpm", "float"],
    ["SPIN_ACCEL_TIME", "spindle accel time", "float"],

    "z axis parameters",
    
    ["Z_PITCH", "z axis leadscrew pitch", "float"],
    ["Z_RATIO", "z axis ratio", "float"],
    ["Z_MICRO", "z axis micro steps", "int16_t"],
    ["Z_MOTOR", "z axis motor steps", "int16_t"],
    ["Z_ACCEL", "z axis acceleration", "float"],
    ["Z_BACKLASH", "z axis backlash", "float"],
    
    "x axis parameters",
    
    ["X_PITCH", "x axis leadscrew pitch", "float"],
    ["X_RATIO", "x axis ratio", "float"],
    ["X_MICRO", "x axis micro steps", "int16_t"],
    ["X_MOTOR", "x axis motor steps", "int16_t"],
    ["X_ACCEL", "x axis acceleration", "float"],
    ["X_BACKLASH", "x axis backlash", "float"],
     
    "z move parameters",
     
    ["Z_MOVE_MIN", "z move min speed", "float"],
    ["Z_MOVE_MAX", "z move max speed", "float"],
     
    "z jog parameters",
     
    ["Z_JOG_MIN", "z jog min speed", "float"],
    ["Z_JOG_MAX", "z jog max speed", "float"],
     
    "x move parameters",
     
    ["X_MOVE_MIN", "x move min speed", "float"],
    ["X_MOVE_MAX", "x move max speed", "float"],
     
    "x jog parameters",
     
    ["X_JOG_MIN", "x jog min speed", "float"],
    ["X_JOG_MAX", "x jog max speed", "float"],
     
    "pass information",
     
    ["TOTAL_PASSES", "total passes", "int16_t"],
    ["SPRING_PASSES", "spring passes", "int16_t"],
    ["SPRING_PASS_INT", "spring pass interval", "int16_t"],
    ["CURRENT_PASS", "current passes", "int16_t"],
     
    "axis move values",
     
    ["Z_MOVE_DIST", "z move distance", "float"],
    ["Z_JOG_DIR", "x jog direction", "int"],
    ["Z_SET_LOC", "z location to set", "float"],
    ["Z_LOC", "z location", "int"],
     
    ["X_MOVE_DIST", "x move distance", "float"],
    ["X_JOG_DIR", "x jog direction", "int"],
    ["X_SET_LOC", "x location to set", "float"],
    ["X_LOC", "x location", "int"],
     
    "z turn/face parameters",
     
    ["Z_START_LOC", "z start", "float"],
    ["Z_END_LOC", "z end", "float"],
    ["Z_RETRACT", "z retract", "float"],
    ["Z_FEED_PASS", "z feed per pass", "float"],
     
    "x turn/face parameters",
     
    ["X_START_LOC", "x start", "float"],
    ["X_END_LOC", "x end", "float"],
    ["X_RETRACT", "x retract", "float"],
    ["X_FEED_PASS", "x feed per pass", "float"],
     
    "feed parameters",
     
    ["FEED_DIR", "feed direction", "int16_t"],
    ["FEED_TYPE", "feed parameter type", "int16_t"],
    ["FEED", "feed parameter", "float"],
     
    "taper parameters",
     
    ["TAPER_Z", "z distance for taper", "float"],
    ["TAPER_X", "x distance for taper", "float"],
    ["TAPER_FLAG", "taper flag", "int16_t"],
     
    "general turn thread parameters",
     
    ["TURN_FLAG", "turn flag", "int16_t"],
    ["THREAD_DEPTH", "thread depth", "float"],
    ["THREAD_LAST_FEED", "thread last feed depth", "float"],
    ["THREAD_H_FACTOR", "height Factor", "float"],
    ["THREAD_ANGLE", "thread angle", "float"],
     
    ["INDEX_PRE_SCALER", "index prescaler", "int"],
    ["INDEX_PERIOD", "index period", "int"],

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
    # ["", "", ""],
    
    "max parameter number",

    ["MAX_PARM", "maximum parameter", "int16_t"]
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

    ["XRDCTL", "read control regiisters"]
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

stateList = \
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
    ["SAVE_TAPER", "save taper"],
    ["MOVE_ZX", "move x in sync with z"],
    ["MOVE_XZ", "move z in sync with x"],
    ["TAPER_ZX", "taper x"],
    ["TAPER_XZ", "taper z"],
    ["QUE_START", "spindle start"],
    ["QUE_STOP", "spindle stop"],
    ["PASS_NUM", "set pass number"],
    "};"
]

regList =\
[\
    "z move command bits",

    ["ZMSK", "(7 << 0)", "z move mask"],
    ["ZMOV", "(1 << 0)", "z a set distance"],
    ["ZJOG", "(2 << 0)", "z while cmd are present"],
    ["ZSYN", "(3 << 0)", "z dist sync to rotation"],
    ["ZMAX", "(4 << 0)", "z rapid move"],
    ["ZPOS", "(1 << 3)", "z in positive direction"],
    ["ZNEG", "(0 << 3)", "z in negative direction"],
    ["Z_SYN_START", "(1 << 4)", "start on sync pulse"],
    ["X_SYN_TAPER", "(1 << 5)", "taper on x"],

    "x move command bits",

    ["XMSK", "(7 << 0)", "xmove mask"],
    ["XMOV", "(1 << 0)", "x a set distance"],
    ["XJOG", "(2 << 0)", "x while cmd are present"],
    ["XSYN", "(3 << 0)", "x dist sync to rotation"],
    ["XMAX", "(4 << 0)", "x rapid move"],
    ["XPOS", "(1 << 3)", "x in positive direction"],
    ["XNEG", "(0 << 3)", "x in negative direction"],
    ["Z_SYN_TAPER", "(1 << 5)", "taper on z"],

    "feed types",
    
    ["FEED_PITCH", "0", "feed inch per rev"],
    ["FEED_TPI", "1", "feed threads per inch"],
    ["FEED_METRIC", "2", "feed mm per rev"],
    
    "turn control bits",

    ["TURNSYN", "(1 << 0)", "turn with sync motion"],
    ["TURNCONT", "(1 << 1)", "cont turning operation"],

    "taper control bits",

    ["TAPERX", "(1 << 0)", "taper x axis"],
    ["TAPERZ", "(1 << 1)", "taper z axis"],
    ["TAPEROUT", "(1 << 2)", "one taper out, zero in"],

    "thread control bits",

    ["THREAD", "(1 << 0)", "threading enabled"],
    ["TINTERNAL", "(1 << 1)", "internal threads"],

    "debug control bits",

    ["DBGPASS", "(1 << 0)", "pause before each pass"],
    ["DBGEND", "(1 << 1)", "pause at end of a pass"],
    ["DBGSEQ", "(1 << 2)", "generate sequence data"]
]

if __name__ == '__main__':
    import os
    from setup import createCommands, createParameters,\
        createCtlBits, createCtlStates, createXilinxReg, createXilinxBits

    path = os.path.dirname(os.path.realpath(__file__))

    fData = True
    cLoc = path + '/../LatheX/include/'
    xLoc = path + '/../../Xilinx/LatheCtl/'

    print "creating interface files"
    createCommands(cmdList, cLoc, fData)
    createParameters(parmList, cLoc, fData)
    createCtlBits(regList, cLoc, fData)
    createCtlStates(stateList, cLoc, fData)
    createXilinxReg(xilinxList, cLoc, xLoc, fData)
    createXilinxBits(xilinxBitList, cLoc, xLoc, fData)
