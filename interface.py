#!/cygdrive/c/Python27/Python.exe

cmdList = \
[\
    "z motion commands",
    
    ["ZMOVE", "", "start z movement"],
    ["ZJMOV", "", "start z jog"],
    ["ZSTOP", "", "stop z movement"],
    ["ZHOME", "", "set current z location as home"],
    ["ZSETLOC", "", ""],
    ["ZGOHOME", "", "z go to home position"],
    
    "x motion commands",
    
    ["XMOVE", "", "start x movement"],
    ["XJMOV", "", "start z jog"],
    ["XSTOP", "", "stop x movement"],
    ["XHOME", "", "set current x location as home"],
    ["XSETLOC", "", ""],
    ["XGOHOME", "", "x go to home position"],
    
    "spindle operations",
    
    ["SPINDLE_START", "", "start spindle"],
    ["SPINDLE_STOP", "", "stop spindle"],
    
    "start operations",
    
    ["CMD_TURN", "", "start turn operation"],
    ["CMD_FACE", "", "start face operation"],
    ["CMD_TAPER", "", "start taper operation"],
    ["CMD_ARC", "", "start arc operation"],
    ["CMD_THREAD", "", "start threading operation"],
    
    "end operations",
    
    ["CMD_PAUSE", "", "pause current operation"],
    ["CMD_RESUME", "", "resume current operation"],
    ["CMD_STOP", "", "stop current operation"],
    
    "setup operations",
    
    ["CMD_CLEAR", "", "clear all tables"],
    ["CMD_SETUP", "", "setup everything"],
    ["CMD_SPSETUP", "", "setup spindle"],

    ["CMD_ZSETUP", "", "setup z axis"],
    ["CMD_ZSYNSETUP", "", "setup z axis sync"],
    ["CMD_ZTAPERSETUP", "", "setup z axis taper"],

    ["CMD_XSETUP", "", "setup x axis"],
    ["CMD_XSYNSETUP", "", "setup z axis sync"],
    ["CMD_XTAPERSETUP", "", "setup z axis taper"],
    
    "state information",
    
    ["READSTAT", "", "read status"],
    ["READISTATE", "", "read states of state machines"],
    
    "load processor and xilinx parameters",
    
    ["LOADVAL", "", "load parameters"],
    ["READVAL", "", "read parameters"],

    "move command operations",

    ["SENDMOVE", "", "send move command"],
    ["MOVEQUESTATUS", "", "read move queue status"],
    
    "location and debug info",
    
    ["READLOC", "", "read location"],
    ["READDBG", "", "read debug message"],
    ["CLRDBG", "", "clear debug message buffer"]
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
    
    ["FEED_TYPE", "feed parameter type", "int16_t"],
    ["FEED", "feed parameter", "float"],
    
    "index pulse variables",

    ["INDEX_PRE_SCALER", "index prescaler", "int"],
    ["INDEX_PERIOD", "index period", "int"],

    # ["", "", ""],
    
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
    ["Z_SYN_TAPER", "(1 << 5)", "taper on z"],
     
    "x direction",
    
    ["XPOS", "1", "x in positive direction"],
    ["XNEG", "-1", "x in negative direction"],
    
    "feed types",
    
    ["FEED_PITCH", "0", "feed inch per rev"],
    ["FEED_TPI", "1", "feed threads per inch"],
    ["FEED_METRIC", "2", "feed mm per rev"]
    
    # ["", "", ""],
]
    
stateList =\
[\
    
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
    
if __name__ == '__main__':
    import os
    from setup import createCommands, createParameters,\
        createCtlBits, createCtlStates

    # print os.path.realpath(__file__)
    # print os.getcwd()

    path = os.path.dirname(os.path.realpath(__file__))

    fData = True
    cLoc = path + '/../Lathe/include/'

    print "creating interface files"
    createCommands(cmdList, cLoc, fData)
    createParameters(parmList, cLoc, fData)
    createCtlBits(regList, cLoc, fData)
    createCtlStates(stateList, cLoc, fData)
