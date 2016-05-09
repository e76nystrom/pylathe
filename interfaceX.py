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
    
    ["CMD_PAUSE", "", "pause current operation"],
    ["CMD_RESUME", "", "resume current operation"],
    ["CMD_STOP", "", "stop current operation"],
    
    "setup operations",
    
    ["CMD_CLEAR", "", "clear all tables"],
    ["CMD_SETUP", "", "setup everything"],
    ["CMD_SPSETUP", "", "setup spindle"],

    ["CMD_ZSETUP", "zSetup", "setup z axis"],
    ["CMD_ZSYNSETUP", "", "setup z axis sync"],
    ["CMD_ZTAPERSETUP", "", "setup z axis taper"],

    ["CMD_XSETUP", "xSetup", "setup x axis"],
    ["CMD_XSYNSETUP", "", "setup z axis sync"],
    ["CMD_XTAPERSETUP", "", "setup z axis taper"],
    
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

    "encoder commands",

    ["ENCSTART", "", "encoder start"],
    ["ENCSTOP", "", "encoder stop"],

    "load operation parameters",

    ["LOADZPRM", "", "call load xilinx z parameters"],
    ["LOADXPRM", "", "call load xilinx x parameters"],
    ["LOADSPRM", "", "call load xilinx sync parameters"],
    ["LOADTPRM", "", "call load xilinx taper parameters"],
]

parmList = \
[\
    "phase parameters",

    ["PRMPHASE", "encoder counts per rev", "int16_t"],

    "z synchronized motion parameters",

    ["PRMSDX", "synchronized dx", "int32_t"],
    ["PRMSDYINI", "synchronized initial dy", "int32_t"],
    ["PRMSDY", "synchronized final dy", "int32_t"],
    ["PRMSD", "synchronized d", "int32_t"],
    ["PRMSINCR1", "synchronized incr1", "int32_t"],
    ["PRMSINCR2", "synchronized incr2", "int32_t"],
    ["PRMSACCEL", "synchronized accel rate", "int16_t"],
    ["PRMSACLCLKS", "synchronized accel clocks", "int32_t"],

    "taper parameters",

    ["PRMTDX", "taper dx", "int32_t"],
    ["PRMTDY", "taper dy", "int32_t"],
    ["PRMTD", "taper d", "int32_t"],
    ["PRMTINCR1", "taper incr1", "int32_t"],
    ["PRMTINCR2", "taper incr2", "int32_t"],

    "z move and location",

    ["PRMZLOCIN", "received z location", "int32_t"],
    ["PRMZDISTIN", "received z distance to move", "int32_t"],
    ["PRMZDIST", "z move distance", "int32_t"],
    ["PRMZLOC", "z location", "int32_t"],
    ["PRMZSTART", "z start", "int32_t"],
    ["PRMZEND", "z end", "int32_t"],
    ["PRMZCUR", "z current location", "int32_t"],
    ["PRMZREF", "z reference", "int32_t"],
    ["PRMZTOTFEED", "z total feed", "int32_t"],
    ["PRMZFEED", "z feed per pass", "int32_t"],
    ["PRMZRETRACT", "z retract value", "int32_t"],
    ["PRMZRTCLOC", "z retract location", "int32_t"],

    "z unsynchronized motion",

    ["PRMZFREQ", "z frequency count", "int32_t"],
    ["PRMZDX", "z move dx value", "int32_t"],
    ["PRMZD", "z move d value", "int32_t"],
    ["PRMZINCR1", "z move incr1 value", "int32_t"],
    ["PRMZINCR2", "z move incr2 value", "int32_t"],
    ["PRMZDYINI", "z move initial dy value", "int32_t"],
    ["PRMZDYJOG", "z move jog dy value", "int32_t"],
    ["PRMZDYMAX", "z move max dy value", "int32_t"],
    ["PRMZACCEL", "z move accel rate", "int32_t"],
    ["PRMZACLJOG", "z move jog accel clocks", "int32_t"],
    ["PRMZACLRUN", "z move run accel clocks", "int32_t"],
    ["PRMZACLMAX", "z move max accel clocks", "int32_t"],
    ["PRMZBACKLASH", "z backlash", "int32_t"],
    ["PRMZCTLREG", "z control register", "uint16_t"],

    "x move and location",

    ["PRMXLOCIN", "received x location", "int32_t"],
    ["PRMXDISTIN", "received x distance to move", "int32_t"],
    ["PRMXDIST", "x move distance", "int32_t"],
    ["PRMXLOC", "x location", "int32_t"],
    ["PRMXSTART", "x start", "int32_t"],
    ["PRMXEND", "x end", "int32_t"],
    ["PRMXCUR", "x current location", "int32_t"],
    ["PRMXREF", "x reference", "int32_t"],
    ["PRMXTOTFEED", "x total feed", "int32_t"],
    ["PRMXFEED", "x feed per pass", "int32_t"],
    ["PRMXRETRACT", "x retract value", "int32_t"],
    ["PRMXRTCLOC", "x retract location", "int32_t"],

    "x unsynchronized motion",

    ["PRMXFREQ", "x frequency count", "int32_t"],
    ["PRMXDX", "x move dx value", "int32_t"],
    ["PRMXDYINI", "x move initial dy value", "int32_t"],
    ["PRMXD", "x move d value", "int32_t"],
    ["PRMXINCR1", "x move incr1 value", "int32_t"],
    ["PRMXINCR2", "x move incr2 value", "int32_t"],
    ["PRMXDYJOG", "x move jog dy value", "int32_t"],
    ["PRMXDYMAX", "x move max dy value", "int32_t"],
    ["PRMXACCEL", "x move accel rate", "int32_t"],
    ["PRMXACLJOG", "x move jog accel clocks", "int32_t"],
    ["PRMXACLRUN", "x move run accel clocks", "int32_t"],
    ["PRMXACLMAX", "x move max accel clocks", "int32_t"],
    ["PRMXBACKLASH", "x backlash", "int32_t"],
    ["PRMXCTLREG", "x control register", "uint16_t"],

    "threading",

    ["PRMTHTAN", "tangent of thread angle", "int32_t"],
    ["PRMTHFEED", "threading feed", "int16_t"],
    ["PRMTHZOFFSET", "threading z offset", "int16_t"],

    "feed index",

    ["PRMFEEDIDX", "threading feed table index", "int16_t"],

    "pass count parameters",

    ["PRMPASSES", "total number of passes", "int16_t"],
    ["PRMSPASSINT", "spring pass interval", "int16_t"],
    ["PRMSPASSES", "number of spring passes", "int16_t"],

    "pass counters",

    ["PRMCURPASS", "current pass", "int16_t"],
    ["PRMSPASSCTR", "spring pass counter", "int16_t"],
    ["PRMSPRING", "current spring pass", "int16_t"],

    "feed direction",

    ["PRMFEEDDIR", "feed direction", "char"],
    ["PRMFEEDLIMIT", "feed limit", "char"],

    "control registers",

    ["PRMTRNCTL", "turn control register", "int16_t"],
    ["PRMTAPERCTLF", "taper control register", "int16_t"],
    ["PRMTHREADCTL", "thread control register", "int16_t"],

    "state variables",

    ["PRMZSTATE", "z state", "char"],
    ["PRMXSTATE", "x state", "char"],
    ["PRMTSTATE", "turn state", "char"],
    ["PRMFSTATE", "face state", "char"],

    "debug registers",

    ["PRMDBGREG", "debug register", "int16_t"],

    "limit registers",

    ["PRMZLIM", "", "int32_t"],
    ["PRMPSTATE", "", "int32_t"],

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

    ["ENC_PRE_SCALER", "encoder prescaler", "uint16_t"],
    ["ENC_TIMER", "encoder timer counts", "uint16_t"],
    ["ENC_RUN_COUNT", "encoder run count", "int"],

    "test encoder status variables",

    ["ENC_RUN", "encoder running flag", "char"],
    ["ENC_COUNTER", "encoder count in rev", "int16_t"],
    ["ENC_REV_COUNTER", "encoder revolution counter", "int32_t"],
 
    "measured spindle speed",

    ["RPM", "current rpm", "int16_t"],

    "measured spindle speed",

    ["xFrequency", "xilinx clock frequency", "int32_t"],
    ["freqMult", "frequency multiplier", "int16_t"],

    # ["", "", ""],
    # ["", "", ""],
    
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
    ["XLDTCOUNT", "load test count"]
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
    ["zPuls_Mult",  1, 7, "enable pulse multiplier"],
    ["zEnc_Dir",    1, 8, "z direction from encoder"],

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
