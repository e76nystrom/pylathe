#!/cygdrive/c/Python27/Python.exe

configList = \
( \
    ('cfgCmdDis', 'config disable sending commands'),
    ('cfgDbgSave', 'config save debug info'),
    ('cfgDRO', 'config dro present'),
    ('cfgDraw', 'config draw paths'),
    ('cfgEncoder', 'config xilinx encoder counts per revolution'),
    ('cfgFcy', 'config microprocesssor clock frequency'),
    ('cfgFreqMult', 'config xilinx frequency multiplier'),
    ('cfgInvEncDir', 'config xilinx invert encoder direction'),
    ('cfgLCD', 'config enable lcd'),
    ('cfgMPG', 'config enable manual pulse generator'),
    ('cfgPrbInv', 'config invert probe signal'),
    ('cfgTestMode', 'conifg test mode'),
    ('cfgTestRPM', 'config xilinx test rpm value'),
    ('cfgXFreq', 'config xilinx frequency'),
    ('cfgXilinx', 'config xilinx interface present'),

    ('commPort', 'comm port'),

    ('cuPause', 'cutoff pause before cutting'),
    ('cuRPM', 'cutoff rpm'),
    ('cuXEnd', 'cutoff x end'),
    ('cuXFeed', 'cutoff x feed'),
    ('cuXRetract', 'cutoff x retract'),
    ('cuXStart', 'cutoff x start'),
    ('cuZCutoff', 'cutoff offset to z cutoff'),
    ('cuZStart', 'cutoff z location'),

    ('faAddFeed', 'face '),
    ('faPasses', 'face '),
    ('faPause', 'face pause before cutting'),
    ('faRPM', 'face '),
    ('faSPInt', 'face '),
    ('faSpring', 'face '),
    ('faXEnd', 'face '),
    ('faXFeed', 'face '),
    ('faXRetract', 'face '),
    ('faXStart', 'face '),
    ('faZEnd', 'face '),
    ('faZFeed', 'face '),
    ('faZRetract', 'face '),
    ('faZStart', 'face '),

    ('jogInc', 'jog '),
    ('jogXPos', 'jog '),
    ('jogXPosDiam', 'jog '),
    ('jogZPos', 'jog '),

    ('mainPanel', 'name of main panel'),

    ('spAccel', 'spindle acceleration'),
    ('spAccelTime', 'spindle accelerationtime'),
    ('spInvDir', 'spindle invert direction'),
    ('spJogAccelTime', 'spindle jog acceleration time'),
    ('spJogMax', 'spindle jog max speed'),
    ('spJogMin', 'spindle jog min speed'),
    ('spMaxRPM', 'spindle jog max rpm'),
    ('spMicroSteps', 'spindle micro steps'),
    ('spMinRPM', 'spindle minimum rpm'),
    ('spMotorSteps', 'spindle motor stpes per revolution'),
    ('spStepDrive', 'spindle stepper drive'),
    ('spTestIndex', 'spindle test generate internal index pulse'),

    ('thAddFeed', 'thread '),
    ('thAngle', 'thread '),
    ('thExitRev', 'thread '),
    ('thHFactor', 'thread '),
    ('thInternal', 'thread '),
    ('thMM', 'thread '),
    ('thPasses', 'thread '),
    ('thPause', 'thread '),
    ('thPitch', 'thread '),
    ('thRPM', 'thread '),
    ('thSPInt', 'thread '),
    ('thSpring', 'thread '),
    ('thTPI', 'thread '),
    ('thXDepth', 'thread '),
    ('thXFirstFeed', 'thread '),
    ('thXLastFeed', 'thread '),
    ('thXRetract', 'thread '),
    ('thXStart', 'thread '),
    ('thXTaper', 'thread '),
    ('thZEnd', 'thread '),
    ('thZRetract', 'thread '),
    ('thZStart', 'thread '),

    ('tpAddFeed', 'tp '),
    ('tpAngle', 'tp '),
    ('tpAngleBtn', 'tp '),
    ('tpDeltaBtn', 'tp '),
    ('tpInternal', 'tp '),
    ('tpLargeDiam', 'tp '),
    ('tpLargeDiamText', 'tp '),
    ('tpPasses', 'tp '),
    ('tpPause', 'tp '),
    ('tpRPM', 'tp '),
    ('tpSPInt', 'tp '),
    ('tpSmallDiam', 'tp '),
    ('tpSmallDiamText', 'tp '),
    ('tpSpring', 'tp '),
    ('tpTaperSel', 'tp '),
    ('tpXDelta', 'tp '),
    ('tpXFeed', 'tp '),
    ('tpXFinish', 'tp '),
    ('tpXInFeed', 'tp '),
    ('tpXRetract', 'tp '),
    ('tpZDelta', 'tp '),
    ('tpZFeed', 'tp '),
    ('tpZLength', 'tp '),
    ('tpZRetract', 'tp '),
    ('tpZStart', 'tp '),
  
    ('tuAddFeed', 'turn '),
    ('tuPasses', 'turn '),
    ('tuPause', 'turn '),
    ('tuRPM', 'turn '),
    ('tuSPInt', 'turn '),
    ('tuSpring', 'turn '),
    ('tuXEnd', 'turn '),
    ('tuXFeed', 'turn '),
    ('tuXRetract', 'turn '),
    ('tuXStart', 'turn '),
    ('tuZEnd', 'turn '),
    ('tuZFeed', 'turn '),
    ('tuZRetract', 'turn '),
    ('tuZStart', 'turn '),

    ('xAccel', 'turn '),
    ('xBacklash', 'turn '),
    ('xDROInch', 'turn '),
    ('xHomeBackoffDist', 'x axis '),
    ('xHomeDir', 'x axis '),
    ('xHomeDist', 'x axis '),
    ('xHomeEnd', 'x axis '),
    ('xHomeLoc', 'x axis '),
    ('xHomeSpeed', 'x axis '),
    ('xHomeStart', 'x axis '),
    ('xInvDRO', 'x axis '),
    ('xInvDir', 'x axis '),
    ('xInvEnc', 'x axis '),
    ('xInvMpg', 'x axis '),
    ('xJogMax', 'x axis '),
    ('xJogMin', 'x axis '),
    ('xJogSpeed', 'x axis '),
    ('xMaxSpeed', 'x axis '),
    ('xMicroSteps', 'x axis '),
    ('xMinSpeed', 'x axis '),
    ('xMotorRatio', 'x axis '),
    ('xMotorSteps', 'x axis '),
    ('xPitch', 'x axis '),
    ('xProbeDist', 'x axis '),

    ('xSvDROPosition', 'x axis '),
    ('xSvDROOffset', 'x axis '),
    ('xSvHomeOffset', 'x axis '),

    ('zAccel', 'z axis '),
    ('zBacklash', 'z axis '),
    ('zDROInch', 'z axis '),
    ('zInvDRO', 'z axis '),
    ('zInvDir', 'z axis '),
    ('zInvEnc', 'z axis '),
    ('zInvMpg', 'z axis '),
    ('zJogMax', 'z axis '),
    ('zJogMin', 'z axis '),
    ('zJogSpeed', 'z axis '),
    ('zMaxSpeed', 'z axis '),
    ('zMicroSteps', 'z axis '),
    ('zMinSpeed', 'z axis '),
    ('zMotorRatio', 'z axis '),
    ('zMotorSteps', 'z axis '),
    ('zPitch', 'z axis '),
    ('zProbeDist', 'z axis '),
    ('zProbeSpeed', 'z axis '),

    ('zSvDROOffset', 'z axis '),
    ('zSvDROPosition', 'z axis '),
    ('zSvHomeOffset', 'z axis '),
)

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
    ["LOADMULTI", "", "load multiple parameters"],
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
    ["SP_JOG_DIR", "spindle direction", "char"],
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

    ["INDEX_PRE_SCALER", "index pre scaler", "int"],
    ["LAST_INDEX_PERIOD", "last index period", "int"],
    ["INDEX_PERIOD", "index period", "int"],
    ["REV_COUNTER", "revolution counter", "unsigned int"],

    "z home offsets",

    ["Z_HOME_OFFSET", "z offset home to zero", "float"],
    ["Z_PROBE_SPEED", "z probe speed", "float"],
    ["PROBE_INV", "invert polarity of probe", "int"],

    "z dro",

    ["Z_DRO_POS", "z dro location", "int"],
    ["Z_DRO_OFFSET", "z dro to zero", "float"],
    ["Z_DRO_INCH", "z dro scale", "int"],
    ["Z_DRO_DIR", "z dro direction", "int"],

    "x home parameters",

    ["X_HOME_SPEED", "x final homing speed", "float"],
    ["X_HOME_DIST", "x max homing distance", "float"],
    ["X_HOME_BACKOFF_DIST", "x home backoff dist", "float"],
    ["X_HOME_DIR", "x homing direction", "int"],

    "x home test parameters",

    ["X_HOME_LOC", "x home test location", "int"],
    ["PROBE_DIST", "probe test distance", "int"],
    ["X_HOME_START", "x start of home signal", "int"],
    ["X_HOME_END", "x end of home signal", "int"],

    # "x home offset",

    ["X_HOME_OFFSET", "x offset home to zero", "float"],

    # "x dro",

    ["X_DRO_POS", "x dro location", "int"],
    ["X_DRO_OFFSET", "x dro to zero", "float"],
    ["X_DRO_INCH", "x dro scale", "int"],
    ["X_DRO_DIR", "x dro direction", "int"],

    "x home or probe status",

    ["X_HOME_DONE", "x home done", "int"],
    ["X_HOME_STATUS", "x home status", "int"],

    "Z home or probe status",

    ["Z_HOME_DONE", "z home done", "int"],
    ["Z_HOME_STATUS", "z home status", "int"],

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

    ["ENC_MAX", "spindle encoder counts per revolution", "uint16_t"],

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
    "common move command bits",
    
    ["CMD_MSK", "(7 << 0)", "move mask"],
    ["CMD_MOV", "(1 << 0)", "move a set distance"],
    ["CMD_JOG", "(2 << 0)", "move while cmd are present"],
    ["CMD_SYN", "(3 << 0)", "move dist synchronized to rotation"],
    ["CMD_MAX", "(4 << 0)", "rapid move"],
    ["CMD_SPEED", "(5 << 0)", "jog at speed"],
    ["JOGSLOW", "(6 << 0)", "slow jog for home or probe"],

    "z move command bits",
    
    ["Z_SYN_START", "(1 << 4)", "start on sync pulse"],
    ["X_SYN_TAPER", "(1 << 5)", "taper on x"],
    
    "z direction",
    
    ["ZPOS", "1", "z in positive direction"],
    ["ZNEG", "-1", "z in negative direction"],
    
    "x move command bits",
    
    ["X_SYN_START", "(1 << 4)", "start on sync pulse"],
    ["Z_SYN_TAPER", "(1 << 5)", "taper on z"],
    ["XFIND_HOME", "(1 << 6)", "find home"],
    ["XCLEAR_HOME", "(1 << 7)", "move off of home"],

    ["FIND_PROBE", "(1 << 8)", "find home"],
    ["CLEAR_PROBE", "(1 << 9)", "move off of home"],
     
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
    ["PROBE_SET", "(1 << 2)", ""],
    ["PROBE_CLR", "(1 << 3)", ""],
    ["HOME_ACTIVE", "0", ""],
    ["HOME_SUCCESS", "1", ""],
    ["HOME_FAIL", "2", ""],
    ["PROBE_SUCCESS", "1", ""],
    ["PROBE_FAIL", "2", ""],

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
    
    "enum mStates",
    "{",
    ["M_IDLE", "idle state"],
    ["M_WAIT_Z", "wait for z to complete"],
    ["M_WAIT_X", "wait for x to complete"],
    ["M_WAIT_SPINDLE", "wait for spindle start"],
    ["M_WAIT_PROBE", "wait for probe to complete"],
    "};",

    "move control commands",
    
    "enum mCommands",
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
    ["SAVE_RUNOUT", "save thread runout"],
    ["SAVE_DEPTH", "save thread depth"],
    ["PROBE_Z", "porbe in z direction"],
    ["PROBE_X", "porbe in x direction"],
    ["OP_DONE", "operation done"],
    "};",

    "home control states",
    
    "enum hStates",
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

    print("creating interface files")
    createCommands(cmdList, cLoc, fData)
    createParameters(parmList, cLoc, fData)
    createCtlBits(regList, cLoc, fData)
    createCtlStates(stateList, cLoc, fData)
    createXilinxReg(xilinxList, cLoc, xLoc, fData)
    createXilinxBits(xilinxBitList, cLoc, xLoc, fData)
