#!/cygdrive/c/Python37/Python.exe

configList = \
( \
  "system config",
  
    ('cfgCmdDis', 'config disable sending commands'),
    ('cfgDbgSave', 'config save debug info'),
    ('cfgDRO', 'config dro present'),
    ('cfgDraw', 'config draw paths'),
    ('cfgEncoder', 'config encoder counts per revolution'),
    ('cfgExtDro', 'config external digital readout'),
    ('cfgFcy', 'config microprocesssor clock frequency'),
    ('cfgFreqMult', 'config xilinx frequency multiplier'),
    ('cfgHomeInPlace', 'config home in place'),
    ('cfgInvEncDir', 'config xilinx invert encoder direction'),
    ('cfgLCD', 'config enable lcd'),
    ('cfgMPG', 'config enable manual pulse generator'),
    ('cfgPrbInv', 'config invert probe signal'),
    ('cfgRemDbg', 'config print remote debug info'),
    ('cfgSpEncCap', 'config encoder on capture interrupt'),
    ('cfgSpEncoder', 'config spindle encoder'),
    ('cfgSpSync', 'config spindle using timer'),
    ('cfgSpSyncBoard', 'config spindle sync board'),
    ('cfgSpUseEncoder', 'config use spindle encoder for threading'),
    ('cfgTaperCycleDist', 'config taper cycle distance'),
    ('cfgTestMode', 'conifg test mode'),
    ('cfgTestRPM', 'config xilinx test rpm value'),
    ('cfgTurnSync', 'config for turning synchronization'),
    ('cfgThreadSync', 'config for threading synchronization'),
    ('cfgXFreq', 'config xilinx frequency'),
    ('cfgXilinx', 'config xilinx interface present'),

  "communications config",

    ('commPort', 'comm port'),
    ('commRate', 'comm baud rate'),

  "cutoff config",

    ('cuPause', 'cutoff pause before cutting'),
    ('cuRPM', 'cutoff rpm'),
    ('cuToolWidth', 'cutoff tool width'),
    ('cuXEnd', 'cutoff x end'),
    ('cuXFeed', 'cutoff x feed'),
    ('cuXRetract', 'cutoff x retract'),
    ('cuXStart', 'cutoff x start'),
    ('cuZCutoff', 'cutoff offset to z cutoff'),
    ('cuZRetract', 'cutoff offset to z retract'),
    ('cuZStart', 'cutoff z location'),

  "dro position",

    ('droXPos', 'dro x position'),
    ('droZPos', 'dro z position'),

  "external dro",

    ('extDroPort', 'external dro port'),
    ('extDroRate', 'external dro baud Rate'),

  "face config",

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

  "jog config",

    ('jogInc', 'jog '),
    ('jogXPos', 'jog '),
    ('jogXPosDiam', 'jog '),
    ('jogZPos', 'jog '),

  "jog panel config",

    ('jpSurfaceSpeed', 'jogpanle fpm or rpm'),
    ('jpXDroDiam', 'jogpanel x dro diameter'),

  "jog time parameters",

    ('jogTimeInitial', 'jog time initial'),
    ('jogTimeInc', 'jog time increment'),
    ('jogTimeMax', 'jog time max'),

  "keypad",

    ('keypadPort', 'external dro port'),
    ('keypadRate', 'external dro baud Rate'),

  "main panel",

    ('mainPanel', 'name of main panel'),

  "spindle config",

    ('spAccel', 'spindle acceleration'),
    ('spAccelTime', 'spindle accelerationtime'),
    ('spCurRange', 'spindle current range'),
    ('spInvDir', 'spindle invert direction'),
    ('spJogAccelTime', 'spindle jog acceleration time'),
    ('spJogMax', 'spindle jog max speed'),
    ('spJogMin', 'spindle jog min speed'),
    ('spJTimeInc', 'spindle jog increment'),
    ('spJTimeInitial', 'spindle jog initial time '),
    ('spJTimeMax', 'spindle jog max'),
    ('spMaxRPM', 'spindle jog max rpm'),
    ('spMicroSteps', 'spindle micro steps'),
    ('spMinRPM', 'spindle minimum rpm'),
    ('spMotorSteps', 'spindle motor stpes per revolution'),
    ('spMotorTest', 'use stepper drive to test motor'),
    ('spPWMFreq', 'spindle pwm frequency'),

    ('spRangeMin1', 'spindle speed range 1 minimum'),
    ('spRangeMin2', 'spindle speed range 2 minimum'),
    ('spRangeMin3', 'spindle speed range 3 minimum'),
    ('spRangeMin4', 'spindle speed range 4 minimum'),
    ('spRangeMin5', 'spindle speed range 5 minimum'),
    ('spRangeMin6', 'spindle speed range 6 minimum'),

    ('spRangeMax1', 'spindle speed range 1 maximum'),
    ('spRangeMax2', 'spindle speed range 2 maximum'), 
    ('spRangeMax3', 'spindle speed range 3 maximum'),
    ('spRangeMax4', 'spindle speed range 4 maximum'),
    ('spRangeMax5', 'spindle speed range 5 maximum'),
    ('spRangeMax6', 'spindle speed range 6 maximum'),
  
    ('spRanges', 'spindle number of speed ranges'),
    ('spStepDrive', 'spindle stepper drive'),
    ('spSwitch', 'spindle off on switch'),
    ('spTestEncoder', 'spindle test generate encoder test pulse'),
    ('spTestIndex', 'spindle test generate internal index pulse'),
    ('spVarSpeed', 'spindle variable speed'),

  "sync communications config",

    ('syncPort', 'sync comm port'),
    ('syncRate', 'sync comm baud rate'),

  "threading config",

    ('thAddFeed', 'thread feed to add after done'),
    ('thAlternate', 'thread althernate thread flanks'),
    ('thAngle', 'thread hanlf angle of thread'),
    ('thFirstFeed', 'thread first feed for thread area calc'),
    ('thFirstFeedBtn', 'thread button to select first feed'),
    ('thInternal', 'thread internal threads'),
    ('thLastFeed', 'thread last feed for thread area calculation'),
    ('thLastFeedBtn', 'thread button to select last feed'),
    ('thLeftHand', 'thread left hand '),
    ('thMM', 'thread button for mm'),
    ('thPasses', 'thread number of passes'),
    ('thPause', 'thread pause between passes'),
    ('thRPM', 'thread speed for threading operation'),
    ('thRunout', 'thread runout for rh exit or lh entrance'),
    ('thSPInt', 'thread spring pass interval'),
    ('thSpring', 'thread number of spring passes at end'),
    ('thTPI', 'thread select thread in threads per inch'),
    ('thThread', 'thread field containing tpi or pitch'),
    ('thXDepth', 'thread x depth of thread'),
    ('thXRetract', 'thread x retract'),
    ('thXStart', 'thread x diameter'),
    ('thXTaper', 'thread x taper'),
    ('thZ0', 'thread z right end of thread left start'),
    ('thZ1', 'thread z right start left end'),
    ('thZRetract', 'thread z retract'),

  "taper config",

    ('tpAddFeed', 'tp '),
    ('tpAngle', 'tp '),
    ('tpAngleBtn', 'tp '),
    ('tpDeltaBtn', 'tp '),
    ('tpInternal', 'tp '),
    ('tpLargeDiam', 'tp '),
    ('tpPasses', 'tp '),
    ('tpPause', 'tp '),
    ('tpRPM', 'tp '),
    ('tpSPInt', 'tp '),
    ('tpSmallDiam', 'tp '),
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

  "turn config",
  
    ('tuAddFeed', 'turn '),
    ('tuInternal', 'turn internal'),
    ('tuPasses', 'turn '),
    ('tuPause', 'turn '),
    ('tuRPM', 'turn '),
    ('tuSPInt', 'turn '),
    ('tuSpring', 'turn '),
    ('tuXDiam0', 'turn '),
    ('tuXDiam1', 'turn '),
    ('tuXFeed', 'turn '),
    ('tuXRetract', 'turn '),
    ('tuZEnd', 'turn '),
    ('tuZFeed', 'turn '),
    ('tuZRetract', 'turn '),
    ('tuZStart', 'turn '),

  "x axis config",

    ('xAccel', 'x axis '),
    ('xBacklash', 'x axis '),
    ('xDoneDelay', 'x axis done to read dro delay'),
    ('xDroFinalDist', 'x dro final approach dist'),
    ('xDROInch', 'x axis '),
    ('xDROPos', 'x axis use dro to go to correct position'),
    ('xHomeBackoffDist', 'x axis '),
    ('xHomeDir', 'x axis '),
    ('xHomeDist', 'x axis '),
    ('xHomeEnd', 'x axis '),
    ('xHomeLoc', 'x axis '),
    ('xHomeSpeed', 'x axis '),
    ('xHomeStart', 'x axis '),
    ('xInvDRO', 'x axis invert dro'),
    ('xInvDir', 'x axis invert stepper direction'),
    ('xInvEnc', 'x axis '),
    ('xInvMpg', 'x axis invert mpg direction'),
    ('xJogMax', 'x axis '),
    ('xJogMin', 'x axis '),
    ('xMpgInc', 'x axis jog increment'),
    ('xMpgMax', 'x axis jog maximum'),
    ('xJogSpeed', 'x axis '),
    ('xMaxSpeed', 'x axis '),
    ('xMicroSteps', 'x axis '),
    ('xMinSpeed', 'x axis '),
    ('xMotorRatio', 'x axis '),
    ('xMotorSteps', 'x axis '),
    ('xParkLoc', 'x axis '),
    ('xPitch', 'x axis '),
    ('xProbeDist', 'x axis '),

  "x axis position config",

    ('xSvPosition', 'x axis '),
    ('xSvHomeOffset', 'x axis '),
    ('xSvDROPosition', 'x axis '),
    ('xSvDROOffset', 'x axis '),

  "z axis config",

    ('zAccel', 'z axis '),
    ('zBackInc', 'z axis distance to go past for taking out backlash'),
    ('zBacklash', 'z axis '),
    ('zDROInch', 'z axis '),
    ('zInvDRO', 'z axis '),
    ('zInvDir', 'z axis '),
    ('zInvEnc', 'z axis '),
    ('zInvMpg', 'z axis '),
    ('zJogMax', 'z axis '),
    ('zJogMin', 'z axis '),
    ('zMpgInc', 'z axis jog increment'),
    ('zMpgMax', 'z axis jog maximum'),
    ('zJogSpeed', 'z axis '),
    ('zMaxSpeed', 'z axis '),
    ('zMicroSteps', 'z axis '),
    ('zMinSpeed', 'z axis '),
    ('zMotorRatio', 'z axis '),
    ('zMotorSteps', 'z axis '),
    ('zParkLoc', 'z axis '),
    ('zPitch', 'z axis '),
    ('zProbeDist', 'z axis '),
    ('zProbeSpeed', 'z axis '),
    ('zDROPos', 'z axis use dro to go to correct position'),

  "z axis position config",

    ('zSvPosition', 'z axis '),
    ('zSvHomeOffset', 'z axis '),
    ('zSvDROPosition', 'z axis '),
    ('zSvDROOffset', 'z axis '),
)

strList = \
(\
 ("STR_OP_NOT_ACTIVE", "Operation Not Active"),
 ("STR_OP_IN_PROGRESS", "Operation In Progress"),
 ("STR_NOT_PAUSED", "Not Paused"),
 ("STR_NOT_SENT", "Data Not Sent"),
 ("STR_NO_ADD", "Cannot Add"),
 ("STR_PASS_ERROR", "Passcount Incorrect"),
 ("STR_NOT_HOMED", "X Not Homed"),
 ("STR_FIELD_ERROR", "Entry Field Error"),
 ("STR_READALL_ERROR", "ReadAll Error"),
 ("STR_TIMEOUT_ERROR", "Timeout Error"),
 ("STR_SIGN_ERROR", "X End and X Start do not have same sign"),
 ("STR_INTERNAL_ERROR", "X End < X Start"),
 ("STR_EXTERNAL_ERROR", "X End > X Start"),
 ("STR_CLR", ""),
)

cmdList = \
(\
    "z motion commands",
    
    ("ZMOVEABS", "zMoveAbs", "start z movement"),
    ("ZMOVEREL", "zMoveRel", "move z relative"),
    ("ZJMOV", "zJogMove", "start z jog"),
    ("ZJSPEED", "zJogSpeed", "start z jog at speed"),
    ("ZSTOP", "zStop", "stop z movement"),
    ("ZSETLOC", "", ""),
    
    "x motion commands",
    
    ("XMOVEABS", "xMoveAbs", "start x movement"),
    ("XMOVEREL", "xMoveRel", "move x relative"),
    ("XJMOV", "xJogMove", "start z jog"),
    ("XJSPEED", "xJogSpeed", "start x jog at speed"),
    ("XSTOP", "xStop", "stop x movement"),
    ("XSETLOC", "", ""),
    ("XHOMEAXIS", "xHomeAxis", "x home axis"),
    
    "spindle operations",
    
    ("SPINDLE_START", "spindleStart", "start spindle"),
    ("SPINDLE_JOG", "spindleJog", "spindle jog"),
    ("SPINDLE_JOG_SPEED", "spindleJogSpeed", "spindle jog at speed"),
    ("SPINDLE_STOP", "spindleStop", "stop spindle"),
    
    "end operations",
    
    ("CMD_PAUSE", "pauseCmd", "pause current operation"),
    ("CMD_RESUME", "resumeCmd", "resume current operation"),
    ("CMD_STOP", "stopCmd", "stop current operation"),
    ("CMD_MEASURE", "measureCmd", "stop at end of current pass"),
    
    "setup operations",
    
    ("CMD_CLEAR", "clearCmd", "clear all tables"),
    ("CMD_SETUP", "setup", "setup everything"),
    ("CMD_SPSETUP", "spindleSetup", "setup spindle"),

    ("CMD_SYNCSETUP", "syncSetup", "setup z and x axis synchronization"),

    ("CMD_ZSETUP", "zSetup", "setup z axis"),
    ("CMD_ZSYNSETUP", "", "setup z axis sync"),

    ("CMD_XSETUP", "xSetup", "setup x axis"),
    ("CMD_XSYNSETUP", "", "setup z axis sync"),
    
    "state information",
    
    ("READSTAT", "", "read status"),
    ("READISTATE", "", "read states of state machines"),
    
    "load processor and xilinx parameters",
    
    ("LOADVAL", "", "load parameters"),
    ("LOADMULTI", "", "load multiple parameters"),
    ("READVAL", "", "read parameters"),
    ("LOADXREG", "", "load xilinx registers"),
    ("READXREG", "", "read xilinx registers"),

    "move command operations",

    ("CLEARQUE", "clearQue", "clear move que"),
    ("QUEMOVE", "", "que move command"),
    ("MOVEQUESTATUS", "", "read move queue status"),
    
    "location and debug info",
    
    ("READALL", "readAll", "read all status info"),
    ("READDBG", "readDbg", "read debug message"),
    ("CLRDBG", "clearDbg", "clear debug message buffer"),

    "encoder commands",

    ("ENCSTART", "", "encoder start"),
    ("ENCSTOP", "", "encoder stop"),

)
    
syncCmdList = \
(\
 ("SYNC_SETUP", "", "setup sync routine"),
 ("SYNC_START", "", "start sync routine"),
 ("SYNC_STOP", "", "stop sync routine"),
 ("SYNC_LOADVAL", "", "load parameters"),
 ("SYNC_LOADMULTI", "", "load multiple parameters"),
 ("SYNC_READVAL", "", "read parameters"),
)

parmList = \
(\
    "spindle parameters",
    
    ("SP_STEPS", "spindle motor steps", "int16_t"),
    ("SP_MICRO", "spindle micro steps", "int16_t"),
    ("SP_MIN_RPM", "spindle minimum rpm", "float"),
    ("SP_MAX_RPM", "spindle maxmum rpm", "float"),
    ("SP_ACCEL_TIME", "spindle accel time", "float"),
    ("SP_ACCEL", "spindle accel rpm/sec^2", "float"),
    ("SP_JOG_MIN_RPM", "spindle jog minimum rpm", "float"),
    ("SP_JOG_MAX_RPM", "spindle jog maxmum rpm", "float"),
    ("SP_JOG_RPM", "spindle jog rpm", "float"),
    ("SP_JOG_ACCEL_TIME", "spindle jog accel time", "float"),
    ("SP_JOG_TIME_INITIAL", "spindle jog time initial", "float"),
    ("SP_JOG_TIME_INC", "spindle jog time increment", "float"),
    ("SP_JOG_TIME_MAX", "spindle jog timemax", "float"),
    ("SP_JOG_DIR", "spindle direction", "char"),
    ("SP_DIR_FLAG", "spindle invert direction", "char"),
    ("SP_TEST_INDEX", "generate test index pulse", "char"),
    ("SP_TEST_ENCODER", "generate encoder test pulse", "char"),
    
    "z axis parameters",
    
    ("Z_PITCH", "z axis leadscrew pitch", "float"),
    ("Z_RATIO", "z axis ratio", "float"),
    ("Z_MICRO", "z axis micro steps", "int16_t"),
    ("Z_MOTOR", "z axis motor steps", "int16_t"),
    ("Z_ACCEL_TIME", "z axis acceleration", "float"),
    ("Z_ACCEL", "z accel rpm/sec^2", "float"),
    ("Z_BACKLASH", "z axis backlash", "float"),
    ("X_STEP_FACTOR", "x steps inch factored", "int"),
    ("Z_DIR_FLAG", "z invert direction", "char"),
    ("Z_MPG_FLAG", "z invert mpg", "char"),
    
    "x axis parameters",
    
    ("X_PITCH", "x axis leadscrew pitch", "float"),
    ("X_RATIO", "x axis ratio", "float"),
    ("X_MICRO", "x axis micro steps", "int16_t"),
    ("X_MOTOR", "x axis motor steps", "int16_t"),
    ("X_ACCEL_TIME", "x axis acceleration", "float"),
    ("X_ACCEL", "z accel rpm/sec^2", "float"),
    ("X_BACKLASH", "x axis backlash", "float"),
    ("X_DIR_FLAG", "x invert direction", "char"),
    ("X_MPG_FLAG", "x invert mpg", "char"),
    ("X_DIAMETER", "x diameter", "int"),
    
    "z move parameters",
    
    ("Z_MOVE_MIN", "z move min speed", "float"),
    ("Z_MOVE_MAX", "z move max speed", "float"),
    
    "z jog parameters",
    
    ("Z_JOG_MIN", "z jog min speed", "float"),
    ("Z_JOG_MAX", "z jog max speed", "float"),
    ("Z_JOG_SPEED", "z jog speed", "float"),
    
    "x move parameters",
    
    ("X_MOVE_MIN", "x move min speed", "float"),
    ("X_MOVE_MAX", "x move max speed", "float"),
    
    "x jog parameters",
    
    ("X_JOG_MIN", "x jog min speed", "float"),
    ("X_JOG_MAX", "x jog max speed", "float"),
    ("X_JOG_SPEED", "x jog speed", "float"),
    
    "pass information",
    
    ("TOTAL_PASSES", "total passes", "int16_t"),
    ("CURRENT_PASS", "current passes", "int16_t"),
    ("MV_STATUS", "movement status", "int16_t"),
    
    "z axis move values",
    
    ("Z_MOVE_DIST", "z move distance", "float"),
    ("Z_MOVE_POS", "z move position", "float"),
    ("Z_JOG_DIR", "x jog direction", "int"),
    ("Z_SET_LOC", "z location to set", "float"),
    ("Z_LOC", "z dro location", "int"),
    ("Z_FLAG", "z move flag", "int"),
    ("Z_ABS_LOC", "z absolute location", "int"),
    ("Z_MPG_INC", "z man pulse gen incr", "int"),
    ("Z_MPG_MAX", "z man pulse max distance", "int"),
    
    "x axis move values",

    ("X_MOVE_DIST", "x move distance", "float"),
    ("X_MOVE_POS", "x move position", "float"),
    ("X_JOG_DIR", "x jog direction", "int"),
    ("X_SET_LOC", "x location to set", "float"),
    ("X_LOC", "x dro location", "int"),
    ("X_FLAG", "x move flag", "int"),
    ("X_ABS_LOC", "x absolute location", "int"),
    ("X_MPG_INC", "X man pulse gen incr", "int"),
    ("X_MPG_MAX", "x man pulse max distance", "int"),
    
    "common jog parameters",

    ("JOG_TIME_INITIAL", "jog time initial", "float"),
    ("JOG_TIME_INC", "jog time increment", "float"),
    ("JOG_TIME_MAX", "jog time max", "float"),

    "taper parameters",

    ("TAPER_CYCLE_DIST", "taperCycleDist", "float"),
 
    "index pulse variables",

    ("INDEX_PRE_SCALER", "index pre scaler", "int"),
    ("LAST_INDEX_PERIOD", "last index period", "unsigned int"),
    ("INDEX_PERIOD", "index period", "unsigned int"),
    ("REV_COUNTER", "revolution counter", "unsigned int"),

    "z home offset",

    ("Z_HOME_OFFSET", "z home offset", "int"),

    "z dro",

    ("Z_DRO_POS", "z dro location", "int"),
    ("Z_DRO_OFFSET", "z dro to zero", "int"),
    ("Z_DRO_COUNT_INCH", "z dro scale", "int"),
    ("Z_DRO_INVERT", "z dro invert", "int"),
    ("Z_USE_DRO", "z use dro for position", "char"),

    "x home parameters",

    ("X_HOME_SPEED", "x final homing speed", "float"),
    ("X_HOME_DIST", "x max homing distance", "float"),
    ("X_HOME_BACKOFF_DIST", "x home backoff dist", "float"),
    ("X_HOME_DIR", "x homing direction", "int"),

    "x home test parameters",

    ("X_HOME_LOC", "x home test location", "int"),
    ("X_HOME_START", "x start of home signal", "int"),
    ("X_HOME_END", "x end of home signal", "int"),

    # "x home offset",

    ("X_HOME_OFFSET", "x home offset", "int"),

    # "x dro",

    ("X_DRO_POS", "x dro location", "int"),
    ("X_DRO_OFFSET", "x dro to zero", "int"),
    ("X_DRO_COUNT_INCH", "x dro scale", "int"),
    ("X_DRO_FACTOR", "x dro counts inch factored", "int"),
    ("X_DRO_INVERT", "x dro invert", "int"),
    ("X_USE_DRO", "x use dro for position", "char"),
    ("X_DONE_DELAY", "x done to read dro delay", "int"),
    ("X_DRO_FINAL_DIST", "x final approach distance", "int"),

    "x home or probe status",

    ("X_HOME_DONE", "x home done", "int"),
    ("X_HOME_STATUS", "x home status", "int"),

    "Z home or probe status",

    ("Z_HOME_DONE", "z home done", "int"),
    ("Z_HOME_STATUS", "z home status", "int"),

    "probe configuration",
 
    ("PROBE_SPEED", "probe speed", "float"),
    ("PROBE_DIST", "probe test distance", "int"),
    ("PROBE_INV", "invert polarity of probe", "int"),

    "configuration",

    ("STEPPER_DRIVE", "stepper driven spindle", "char"),
    ("MOTOR_TEST", "use stepper drive to test motor", "char"),
    ("SPINDLE_ENCODER", "motor drive with spindle encoder", "char"),
    ("SPINDLE_SYNC_BOARD", "spindle sync board", "char"),
    ("TURN_SYNC", "synchronization type for turning", "char"),
    ("THREAD_SYNC", "synchronization type for threading", "char"),
    # ("SPINDLE_SYNC", "spindle sync direct", "char"),
    # ("USE_ENCODER", "config for use encoder interrupt directly", "char"),
    # ("ENCODER_DIRECT", "use encoder interrupt directly", "char"),
    ("CAP_TMR_ENABLE", "enable capture timer", "char"), 
    ("CFG_XILINX", "using xilinx", "char"),
    ("CFG_MPG", "manual pulse generator", "char"),
    ("CFG_DRO", "digital readout", "char"),
    ("CFG_LCD", "lcd display", "char"),
    ("CFG_FCY", "system clock speed", "int"),
    ("CFG_SWITCH", "spindle off on switch", "int"),
    ("CFG_VAR_SPEED", "spindle variable speed", "int"),

    "setup",

    ("SETUP_DONE", "setup done", "char"),

    "encoder counts per revolution",

    ("ENC_PER_REV", "spindle encoder counts per revolution", "uint16_t"),

    "test encoder setup variables",

    ("ENC_ENABLE", "encoder enable flag", "char"),
    ("ENC_PRE_SCALER", "encoder prescaler", "uint16_t"),
    ("ENC_TIMER", "encoder timer counts", "uint16_t"),
    ("ENC_RUN_COUNT", "encoder run count", "int"),

    "test encoder status variables",

    ("ENC_RUN", "encoder running flag", "char"),
    ("ENC_COUNTER", "encoder count in rev", "int16_t"),
    ("ENC_REV_COUNTER", "encoder revolution counter", "int32_t"),
 
    "measured spindle speed",

    ("RPM", "current rpm", "int16_t"),

    "xilinx frequency variables",

    ("X_FREQUENCY", "xilinx clock frequency", "int32_t"),
    ("FREQ_MULT", "frequency multiplier", "int16_t"),

    "xilinx configuration register",

    ("X_CFG_REG", "xilinx configuration register", "int16_t"),
 
    "sync parameters",
   
    ("L_SYNC_CYCLE", "sync cycle length", "uint16_t"),
    ("L_SYNC_OUTPUT", "sync outputs per cycle", "uint16_t"),
    ("L_SYNC_PRESCALER", "sync prescaler", "uint16_t"),

    "threading variables",

    ("TH_Z_START", "threading z start", "int32_t"),
    ("TH_X_START", "threading x start", "int32_t"),
    ("TAN_THREAD_ANGLE", "tangent of threading angle", "float"),
    ("X_FEED", "x feed", "int16_t"),
    ("RUNOUT_DISTANCE", "runout distance", "float"),
    ("RUNOUT_DEPTH", "runout depth", "float"),

     "jog debug",

    ("JOG_DEBUG", "jog interrupt debug", "char"),

    "motor and speed control",
 
    ("PWM_FREQ", "spindle speed pwm frequency", "int16_t"),
    ("MIN_SPEED", "minimum speed for current range", "int16_t"),
    ("MAX_SPEED", "maximum speed for current range", "int16_t"),

    "current operation",

    ("CURRENT_OP", "current operation", "char"),

    # ("", "", ""),
    # ("", "", ""),
    # ("", "", ""),

    ("MAX_PARM", "maximum parameter", "int16_t")
)
    
syncParmList = \
(\
 ("SYNC_CYCLE", "sync cycle length", "uint16_t"),
 ("SYNC_OUTPUT", "sync outputs per cycle", "uint16_t"),
 ("SYNC_PRESCALER", "sync prescaler", "uint16_t"),
 ("SYNC_ENCODER", "sync encoder pulses", "uint16_t"),
 ("SYNC_MAX_PARM", "sync maximum parameter", "int16_t")
)

regList =\
(\
    "common move command bits",
    
    ("CMD_MSK",    "(7 << 0)", "move mask"),
    ("CMD_MOV",    "(1 << 0)", "move a set distance"),
    ("CMD_JOG",    "(2 << 0)", "move while cmd are present"),
    ("CMD_SYN",    "(3 << 0)", "move dist synchronized to rotation"),
    ("CMD_MAX",    "(4 << 0)", "rapid move"),
    ("CMD_SPEED",  "(5 << 0)", "jog at speed"),
    ("JOGSLOW",    "(6 << 0)", "slow jog for home or probe"),

    ("SYN_START",  "(1 << 4)", "start on sync pulse"),
    ("SYN_LEFT",   "(1 << 5)", "start sync left"),
    ("SYN_TAPER",  "(1 << 6)", "taper on x"),
    ("AX_FIND_HOME",  "(1 << 7)", "find home"),
    ("AX_CLEAR_HOME", "(1 << 8)", "move off of home"),

    ("FIND_PROBE",  "(1 << 9)", "find home"),
    ("CLEAR_PROBE", "(1 << 10)", "move off of home"),
    ("DRO_POS",     "(1 << 11)", "use dro for moving"),
    ("DRO_UPD",     "(1 << 12)", "update internal position from dro"),
    
    "common definitions",

    ("DIR_POS", "1", "positive direction"),
    ("DIR_NEG", "-1", "negative direction"),

    "z move command bits",
    
    ("Z_SYN_START", "(1 << 4)", "start on sync pulse"),
    ("Z_SYN_LEFT",  "(1 << 5)", "start sync left"),
    ("X_SYN_TAPER", "(1 << 6)", "taper on x"),

    "z direction",
    
    ("ZPOS", "1", "z in positive direction"),
    ("ZNEG", "-1", "z in negative direction"),
    
    "x move command bits",
    
    ("X_SYN_START", "(1 << 4)", "start on sync pulse"),
    ("Z_SYN_TAPER", "(1 << 6)", "taper on z"),
    ("XFIND_HOME",  "(1 << 7)", "find home"),
    ("XCLEAR_HOME", "(1 << 8)", "move off of home"),
     
    "x direction",
    
    ("XPOS", "1",  "x in positive direction"),
    ("XNEG", "-1", "x in negative direction"),
 
    "feed types",
    
    ("FEED_PITCH",  "0", "feed inch per rev"),
    ("FEED_TPI",    "1", "feed threads per inch"),
    ("FEED_METRIC", "2", "feed mm per rev"),

    "home flag",

    ("FIND_HOME",  "(1 << 0)", ""),
    ("CLEAR_HOME", "(1 << 1)", ""),
    ("PROBE_SET",  "(1 << 2)", ""),
    ("PROBE_CLR",  "(1 << 3)", ""),
 
    "home status",
 
    ("HOME_ACTIVE",  "0", ""),
    ("HOME_SUCCESS", "1", ""),
    ("HOME_FAIL",    "2", ""),

    "probe status",

    ("PROBE_SUCCESS", "1", ""),
    ("PROBE_FAIL", "2", ""),

    "movement status",

    ("MV_PAUSE",       "(1 << 0)", "movement paused"),
    ("MV_READ_X",      "(1 << 1)", "pause x may change"),
    ("MV_READ_Z",      "(1 << 2)", "pause z may change"),
    ("MV_ACTIVE",      "(1 << 3)", "movement active"),
    ("MV_HOME_ACTIVE", "(1 << 4)", "home active"),
    ("MV_XHOME",       "(1 << 5)", "X home success"),
    ("MV_MEASURE",     "(1 << 6)", "pause for measurement"),

    "pause flags",

    ("PAUSE_ENA_Z_JOG", "(1 << 0)", "enable z job during pause"),
    ("PAUSE_ENA_X_JOG", "(1 << 1)", "enable x jog during pause"),
    ("DISABLE_JOG",     "(1 << 2)", "jogging disabled"),
    ("PAUSE_READ_X",    "(1 << 3)", "read x after pause"),
    ("PAUSE_READ_Z",    "(1 << 4)", "read z after pause"),

    "thread flags",

    ("TH_THREAD", "(1 << 0)", "threading"),
    ("TH_INTERNAL", "(1 << 1)", "internal threads"),
    ("TH_LEFT", "(1 << 2)", "left hand thread"),
    ("TH_RUNOUT", "(1 << 3)", "runout with thread"),

    "parameters for op_done",

    ("PARM_START", "0", "start of operation"),
    ("PARM_DONE", "1", "done operation"),

    "isr active flags",

    ("SYNC_ACTIVE_EXT", "(1 << 0)", "active for sync board"),
    ("SYNC_ACTIVE_TMR", "(1 << 1)", "active for internal timer"),
    ("SYNC_ACTIVE_ENC", "(1 << 2)", "active for encoder"),
    ("SYNC_ACTIVE_STEP", "(1 << 3)", "active for stepper"),
    ("SYNC_ACTIVE_TAPER", "(1 << 4)", "active for taper"),

    "encoder direct flags",

    ("Z_ENCODER_DIRECT", "(1 << 0)", "z sync directly from encoder"),
    ("X_ENCODER_DIRECT", "(1 << 1)", "x sync directly from encoder"),

    # ("", "()", ""),
    # ("", "", ""),
)

# ("", 0, 0, ""),
fpgaEncList = \
( \
  ("F_Noop",               0,    1, 0, "register 0"),

  ("F_Ld_Run_Ctl",         None, 1, 1, "load run control register"),
  ("F_Ld_Dbg_Ctl",         None, 1, 1, "load debug control register"),

  ("F_Ld_Enc_Cycle",       None, 1, 2, "load encoder cycle"),
  ("F_Ld_Int_Cycle",       None, 1, 2, "load internal cycle"),

  ("F_Rd_Cmp_Cyc_Clks",    None, 1, 4, "read cmp cycle clocks"),

  ("F_Ld_Dbg_Freq",        None, 1, 2, "load debug frequency"),
  ("F_Ld_Dbg_Count",       None, 1, 2, "load debug clocks"),
)

fpgaLatheList = \
( \
  "phase control",
  
  ("phaseCtl",),
  ("F_Ld_Phase_Len",    0,    1, 2,    "phase length"),
  ("F_Rd_Phase_Syn",    None, 1, 4,    "read phase at sync pulse"),
  ("F_Phase_Max",       None, None, 0, "number of phase registers"),

  "encoder",

  ("encoder",),
  ("F_Ld_Enc_Cycle",    0,    1, 2,    "load encoder cycle"),
  ("F_Ld_Int_Cycle",    None, 1, 2,    "load internal cycle"),
  ("F_Rd_Cmp_Cyc_Clks", None, 1, 4,    "read cmp cycle clocks"),
  ("F_Enc_Max",         None, None, 0, "number of encoder registers"),

  "debug frequency",

  ("dbgFreq",),
  ("F_Ld_Dbg_Freq",     0,    1, 2,    "debug frequency"),
  ("F_Ld_Dbg_Count",    None, 1, 4,    "debug count"),
  ("F_Dbg_Freq_Max",    None, None, 0, "number of debug frequency regs"),

  "sync accel",

  ("syncAccel",),
  ("F_Ld_D",           0,    1, 4,    "axis d"),
  ("F_Ld_Incr1",       None, 1, 4,    "axis incr1"),
  ("F_Ld_Incr2",       None, 1, 4,    "axis incr2"),
  ("F_Ld_Accel_Val",   None, 1, 4,    "axis accel value"),
  ("F_Ld_Accel_Count", None, 1, 4,    "axis accel count"),
  ("F_Rd_XPos",        None, 1, 4,    "axis x pos"),
  ("F_Rd_YPos",        None, 1, 4,    "axis y pos"),
  ("F_Rd_Sum",         None, 1, 4,    "axis sum"),
  ("F_Rd_Accel_Sum",   None, 1, 4,    "axis accel sum"),
  ("F_Rd_Accel_Ctr",   None, 1, 4,    "axis accel counter"),
  ("F_Sync_Max",       None, None, 0, "number of sync registers"),
  
  "distance registers",

  ("distCtr",),
  ("F_Ld_Dist",       0,    1, 4,    "axis distance"),
  ("F_Rd_Dist",       None, 1, 4,    "read axis distance"),
  ("F_Rd_Acl_Steps",  None, 1, 4,    "read accel steps"),
  ("F_Dist_Max",      None, None, 0, "number of distance registers"),

  "location registers",

  ("locCtr",),
  ("F_Ld_Loc",        0,    1, 4,    "axis location"),
  ("F_Rd_Loc",        None, 1, 4,    "read axis location"),
  ("F_Loc_Max",       None, None, 0, "number of location registers"),

  "axis",

  ("axisCtl",),
  ("F_Ld_Axis_Ctl",   0,    1, 1,              "axis control register"),
  ("F_Ld_Freq",       None, 1, 4,              "frequency"),
  ("F_Sync_Base",     None, "syncAccel", None, "sync registers"),
  ("F_Dist_Base",     None, "distCtr",   None, "distance registers"),
  ("F_Loc_Base",      None, "locCtr",    None, "location registers"),
  ("F_Axis_Max",      None, None, 0,           "number of axis registers"),

  "register definitions",

  ("regDef", ),
  ("F_Noop",        0,    1, 1,         "register 0"),

  "status registers",

  ("F_Rd_Status",   None, 1, 1,         "status register"),

  "control registers",

  ("F_Ld_Sync_Ctl", None, 1, 1,         "sync control register"),
  ("F_Ld_Cfg_Ctl",  None, 1, 1,         "config control register"),
  ("F_Ld_Clk_Ctl",  None, 1, 1,         "clock control register"),
  ("F_Ld_Dsp_Reg",  None, 1, 1,         "display register"),

  "debug frequency control",

  ("F_Dbg_Freq_Base", None, "dbgFreq", None, "dbg frequency"),

  "base for modules",

  ("F_Enc_Base",   None, "encoder", None,  "encoder registers"),
  ("F_Phase_Base", None, "phaseCtl", None, "phase registers"),
  ("F_ZAxis_Base", None, "axisCtl", None,  "z axis registers"),
  ("F_XAxis_Base", None, "axisCtl", None,  "x axis registers"),
  ("F_Cmd_Max",    None, None, None,       "number of commands"),
)

xilinxList = \
( \
    "skip register zero",

    ("XNOOP", "register 0"),

    "load control registers",

    ("XLDZCTL", "z control register"),
    ("XLDXCTL", "x control register"),
    ("XLDTCTL", "load taper control"),
    ("XLDPCTL", "position control"),
    ("XLDCFG", "configuration"),
    ("XLDDCTL", "load debug control"),
    ("XLDDREG", "load display reg"),
    ("XREADREG", "read register"),

    "status register",

    ("XRDSR", "read status register"),

    "phase counter",

    ("XLDPHASE", "load phase max"),

    "load z motion",

    ("XLDZFREQ", "load z frequency"),
    ("XLDZD", "load z initial d"),
    ("XLDZINCR1", "load z incr1"),
    ("XLDZINCR2", "load z incr2"),
    ("XLDZACCEL", "load z syn accel"),
    ("XLDZACLCNT", "load z syn acl cnt"),
    ("XLDZDIST", "load z distance"),
    ("XLDZLOC", "load z location"),

    "load x motion",

    ("XLDXFREQ", "load x frequency"),
    ("XLDXD", "load x initial d"),
    ("XLDXINCR1", "load x incr1"),
    ("XLDXINCR2", "load x incr2"),
    ("XLDXACCEL", "load x syn accel"),
    ("XLDXACLCNT", "load x syn acl cnt"),
    ("XLDXDIST", "load x distance"),
    ("XLDXLOC", "load x location"),

    "read z motion",

    ("XRDZSUM", "read z sync sum"),
    ("XRDZXPOS", "read z sync x pos"),
    ("XRDZYPOS", "read z sync y pos"),
    ("XRDZACLSUM", "read z acl sum"),
    ("XRDZASTP", "read z acl stps"),

    "read x motion",

    ("XRDXSUM", "read x sync sum"),
    ("XRDXXPOS", "read x sync x pos"),
    ("XRDXYPOS", "read x sync y pos"),
    ("XRDXACLSUM", "read x acl sum"),
    ("XRDXASTP", "read z acl stps"),

    "read distance",

    ("XRDZDIST", "read z distance"),
    ("XRDXDIST", "read x distance"),

    "read location",

    ("XRDZLOC", "read z location"),
    ("XRDXLOC", "read x location"),

    "read frequency and state",

    ("XRDFREQ",  "read encoder freq"),
    ("XCLRFREQ", "clear freq register"),
    ("XRDSTATE", "read state info"),

    "read phase",

    ("XRDPSYN", "read sync phase val"),
    ("XRDTPHS", "read tot phase val"),

    "phase limit info",

    ("XLDZLIM", "load z limit"),
    ("XRDZPOS", "read z position"),

    "test info",

    ("XLDTFREQ", "load test freq"),
    ("XLDTCOUNT", "load test count"),

    "read control regs",

    ("XRDZCTL", "read control regiisters"),
    ("XRDXCTL", "read control regiisters")
)

xilinxBitList = \
(\
    "z control register",

    ("zCtl",),
    ("zReset",      1, 0, "reset flag"),
    ("zStart",      1, 1, "start z"),
    ("zSrc_Syn",    1, 2, "run z synchronized"),
    ("zSrc_Frq",    0, 2, "run z from clock source"),
    ("zDir_In",     1, 3, "move z in positive dir"),
    ("zDir_Pos",    1, 3, "move z in positive dir"),
    ("zDir_Neg",    0, 3, "move z in negative dir"),
    ("zSet_Loc",    1, 4, "set z location"),
    ("zBacklash",   1, 5, "backlash move no pos upd"),
    ("zWait_Sync",  1, 6, "wait for sync to start"),

    "x control register",

    ("xCtl",),
    ("xReset",      1, 0, "x reset"),
    ("xStart",      1, 1, "start x"),
    ("xSrc_Syn",    1, 2, "run x synchronized"),
    ("xSrc_Frq",    0, 2, "run x from clock source"),
    ("xDir_In",     1, 3, "move x in positive dir"),
    ("xDir_Pos",    1, 3, "x positive direction"),
    ("xDir_Neg",    0, 3, "x negative direction"),
    ("xSet_Loc",    1, 4, "set x location"),
    ("xBacklash",   1, 5, "x backlash move no pos upd"),

    "taper control register",

    ("tCtl",),
    ("tEna",     1, 0, "taper enable"),
    ("tZ",       1, 1, "one for taper z"),
    ("tX",       0, 1, "zero for taper x"),

    "position control register",

    ("pCtl",),
    ("pReset",    1, 0, "reset position"),
    ("pLimit",    1, 1, "set flag on limit reached"),
    ("pZero",     1, 2, "set flag on zero reached"),

    "configuration register",

    ("cCtl",),
    ("zStep_Pol",  1, 0, "z step pulse polarity"),
    ("zDir_Pol",   1, 1, "z direction polarity"),
    ("xStep_Pol",  1, 2, "x step pulse polarity"),
    ("xDir_Pol",   1, 3, "x direction polarity"),
    ("enc_Pol",    1, 4, "encoder dir polarity"),
    ("zPulse_Mult",1, 5, "enable pulse multiplier"),

    "debug control register",

    ("dCtl",),
    ("Dbg_Ena",    1, 0, "enable debugging"),
    ("Dbg_Sel",    1, 1, "select dbg encoder"),
    ("Dbg_Dir",    1, 2, "debug direction"),
    ("Dbg_Count",  1, 3, "gen count num dbg clks"),
    ("Dbg_Init",   1, 4, "init z modules"),
    ("Dbg_Rsyn",   1, 5, "running in sync mode"),
    ("Dbg_Move",   1, 6, "used debug clock for move"),

    "status register",

    ("stat",),
    ("s_Z_Done_Int", 1, 0, "z done interrrupt"),
    ("s_X_Done_Int", 1, 1, "x done interrupt"),
    ("s_Dbg_Done",   1, 2, "debug done"),
    ("s_Z_Start",    1, 3, "z start"),
    ("s_X_Start",    1, 4, "x start"),
    ("s_Enc_Dir_In", 1, 5, "encoder direction in"),

    ""
)
    
fpgaEncBitList = \
(\
 "run control register",

 ("rCtl",),
 ("ctlReset", 1, 0, "reset"),
 ("ctlTestClock", 1, 1, "testclock"),
 ("ctlSpare", 1, 2, "spare"),

 "debug control register",

 ("dCtl",),
 ("DbgEna",    1, 0, "enable debugging"),
 ("DbgSel",    1, 1, "select dbg encoder"),
 ("DbgDir",    1, 2, "debug direction"),
 ("DbgCount",  1, 3, "gen count num dbg clks"),

 ""
)

fpgaLatheBitList = \
(\
 "status register",

 ("status",),
 ("zAxisEna",   1, 0, "z axis enable flag"),
 ("zAxisDone",  1, 1, "z axis done"),
 ("xAxisEna",   1, 2, "x axis enable flag"),
 ("xAxisDone",  1, 3, "x axis done"),
# ("",  , , ""),

 "axis control register",

 ("axisCtl",),
 ("ctlInit",       1, 0, "reset flag"),
 ("ctlStart",      1, 1, "start"),
 ("ctlBacklash",   1, 2, "backlash move no pos upd"),
 ("ctlWaitSync",   1, 3, "wait for sync to start"),
 ("ctlDir",        1, 4, "direction"),
 ("ctlDirPos",     1, 4, "move in positive dir"),
 ("ctlDirNeg",     0, 4, "move in negative dir"),
 ("ctlSetLoc",     1, 5, "set location"),
 ("ctlChDirect",   1, 6, "ch input direct"),
 ("ctlSlave",      1, 7, "slave controlled by other axis"),

 "configuration control register",

 ("cfgCtl",),
 ("cfgZDir",     1, 0, "z direction inverted"),
 ("cfgXDir",     1, 1, "x direction inverted"),
 ("cfgSpDir",    1, 2, "spindle directiion inverted"),
 ("cfgEncDir",   1, 3, "invert encoder direction"),
 ("cfgEnaEncDir", 1, 4, "enable encoder direction"),
 ("cfgGenSync",  1, 5, "no encoder generate sync pulse"),
 
 "clock control register",

 ("clkCtl",),
 ("zFreqSel",    7, 0, "z Frequency select"),
 ("zClkZFreq",   1, 0, ""),
 ("zClkCh",      2, 0, ""),
 ("zClkIntClk",  3, 0, ""),
 ("zClkXStep",   4, 0, ""),
 ("zClkXFreq",   5, 0, ""),
 ("zClkDbgFreq", 7, 0, ""),
 ("xFreqSel",    7, 3, "x Frequency select"),
 ("xClkXFreq",   1, 3, ""),
 ("xClkCh",      2, 3, ""),
 ("xClkIntClk",  3, 3, ""),
 ("xClkZStep",   4, 3, ""),
 ("xClkZFreq",   5, 3, ""),
 ("xClkDbgFreq", 7, 3, ""),
 ("clkDbgFreqEna",  1, 6, "enable debug frequency"),

 "sync control register",

 ("synCtl",),
 ("synPhaseInit",  1, 0, "init phase counter"),
 ("synEncInit",    1, 1, "init encoder"),
 ("synEncEna",     1, 2, "enable encoder"),

 "",
 # ("",),
 # ("",  , , ""),

 # "",
 # ("",),
 # ("",  , , ""),
)

enumList =\
(\
    "z control states",

    "enum z_States",
    "{",
    ("ZIDLE", "idle"),
    ("ZWAITBKLS", "wait for backlash move complete"),
    ("ZSTARTMOVE", "start z move"),
    ("ZWAITMOVE", "wait for move complete"),
    ("ZDONE", "clean up state"),
    "};",
    
    "x control states",
    
    "enum x_States",
    "{",
    ("XIDLE", "idle"),
    ("XWAITBKLS", "wait for backlash move complete"),
    ("XSTARTMOVE", "start x move"),
    ("XWAITMOVE", "wait for move complete"),
    ("XDELAY", "wait for position to settle"),
    ("XDONE", "clean up state"),
    "};",
    
    "axis control states",
    
    "enum axis_States",
    "{",
    ("AXIS_IDLE", "idle"),
    ("AXIS_WAIT_BACKLASH", "wait for backlash move complete"),
    ("AXIS_START_MOVE", "start axis move"),
    ("AXIS_WAIT_MOVE", "wait for move complete"),
    ("AXIS_DELAY", "wait for position to settle"),
    ("AXIS_DONE", "clean up state"),
    ("AXIS_STATES", "number of states"),
    "};",
    
    "move control states",
    
    "enum m_States",
    "{",
    ("M_IDLE", "idle state"),
    ("M_WAIT_Z", "wait for z to complete"),
    ("M_WAIT_X", "wait for x to complete"),
    ("M_WAIT_SPINDLE", "wait for spindle start"),
    ("M_WAIT_SYNC_READY", "wait for sync"),
    ("M_WAIT_SYNC_DONE", "wait for sync done"),
    ("M_WAIT_MEASURE_DONE", "wait for measurment done"),
    ("M_START_SYNC", "start sync"),
    ("M_WAIT_PROBE", "wait for probe to complete"),
    ("M_WAIT_MEASURE", "wait for measurement to complete"),
    ("M_WAIT_SAFE_X", "wait for move to safe x to complete"),
    ("M_WAIT_SAFE_Z", "wait for move to safe z to complete"),
    "};",

    "move control commands",
    
    "enum m_Commands",
    "{",
    ("MOVE_Z", "move z"),
    ("MOVE_X", "move x"),
    ("SAVE_Z", "save z"),
    ("SAVE_X", "save x"),
    ("SAVE_Z_OFFSET", "save z offset"),
    ("SAVE_X_OFFSET", "save x offset"),
    ("SAVE_TAPER", "save taper"),
    ("MOVE_ZX", "move x in sync with z"),
    ("MOVE_XZ", "move z in sync with x"),
    ("TAPER_ZX", "taper x"),
    ("TAPER_XZ", "taper z"),
    ("START_SPINDLE", "spindle start"),
    ("STOP_SPINDLE", "spindle stop"),
    ("Z_SYN_SETUP", "z sync setup"),
    ("X_SYN_SETUP", "x sync setup"),
    ("PASS_NUM", "set pass number"),
    ("QUE_PAUSE", "pause queue"),
    ("MOVE_Z_OFFSET", "move z offset"),
    ("SAVE_FEED_TYPE", "save feed type"),
    ("Z_FEED_SETUP", "setup z feed"),
    ("X_FEED_SETUP", "setup x feed"),
    ("SAVE_FLAGS", "save thread flags"),
    ("PROBE_Z", "probe in z direction"),
    ("PROBE_X", "probe in x direction"),
    ("SAVE_Z_DRO", "save z dro reading"),
    ("SAVE_X_DRO", "save x dro reading"),
    ("OP_DONE", "operation done"),
    "};",

    "move control operation",

    "enum operations",
    "{",
     ("OP_TURN", "turn"),
     ("OP_FACE", "face"),
     ("OP_CUTOFF", "cutoff"),
     ("OP_TAPER", "taper"),
     ("OP_THREAD", "thread"),
    "};",

    "home control states",
    
    "enum h_States",
    "{",
    ("H_IDLE", "idle state"),
    ("H_CHECK_ONHOME", ""),
    ("H_WAIT_FINDHOME", ""),
    ("H_BACKOFF_HOME", ""),
    ("H_WAIT_BACKOFF", ""),
    ("H_WAIT_SLOWFIND", ""),
    # ("H_", ""),
    "};",

    "debug message types",
    
    "enum d_Message",
    "{",
    ("D_PASS", "pass done"),
    ("D_DONE", "all operations done"),
    ("D_TEST", "test message"),

    ("D_XMOV",  "x move location"),
    ("D_XLOC",  "x location"),
    ("D_XDST",  "x distance"),
    ("D_XSTP",  "x steps"),
    ("D_XST",   "x state"),
    ("D_XBSTP", "x backlash steps"),
    ("D_XDRO",  "x dro location"),
    ("D_XPDRO", "x pass dro location"),
    ("D_XEXP",  "x expected location"),
    ("D_XWT",   "x wait"),
    ("D_XDN",   "x done"),
    ("D_XEST",  "x spindle encoder start count"),
    ("D_XEDN",  "x spindle encoder done count"),
    ("D_XX",    "x "),
    ("D_XY",    "x "),

    ("D_ZMOV",  "z move location"),
    ("D_ZLOC",  "z location"),
    ("D_ZDST",  "z distance"),
    ("D_ZSTP",  "z steps"),
    ("D_ZST",   "z state"),
    ("D_ZBSTP", "z backlash steps"),
    ("D_ZDRO",  "z dro location"),
    ("D_ZPDRO", "z pass dro location"),
    ("D_ZEXP",  "z expected location"),
    ("D_ZWT",   "z wait"),
    ("D_ZDN",   "z done"),
    ("D_ZEST",  "z spindle encoder start count"),
    ("D_ZEDN",  "Z spindle encoder done count"),
    ("D_ZX",    "z "),
    ("D_ZY",    "z "),
 
    ("D_HST", "home state"),

    ("D_MSTA", "move state"),
    ("D_MCMD", "move command"),
    "};",

    "pylathe update events",
    
    "enum ev_Events",
    "{",
     ("EV_ZLOC", "z location"),
     ("EV_XLOC", "x location"),
     ("EV_RPM", "rpm"),
     ("EV_READ_ALL", "all values"),
     ("EV_ERROR", "event error"),
     ("EV_MAX", "maximum event"),
    # ("EV_", ""),
    "};",
 
    "turning sync selector",
    
    "enum sel_Turn c",
    "{",
      ("SEL_TU_SPEED", "Motor Speed"),
      ("SEL_TU_STEP",  "Stepper"),
      ("SEL_TU_ENC",   "Encoder"),
      ("SEL_TU_ISYN",  "Int Syn"),
      ("SEL_TU_ESYN",  "Ext Syn"),
    "};",

    "threading sync selector",
    
    "enum sel_Thread c",
    "{",
      ("SEL_TH_NO_ENC",    "No Encoder"),
      ("SEL_TH_STEP",      "Stepper"),
      ("SEL_TH_ENC",       "Encoder Direct"),
      ("SEL_TH_ISYN_RENC", "Int Syn, Runout Enc"),
      ("SEL_TH_ESYN_RENC", "Ext Syn, Runout Enc"),
      ("SEL_TH_ESYN_RSYN", "Ext Syn, Runout Syn"),
    "};",
)
    
xilinxEncList = \
( \
    "skip register zero",

    ("XNOOP", "register 0"),

    "load control registers",
)

if __name__ == '__main__':
    import os
    from setup import Setup
    from sys import stderr, stdout

    # print os.path.realpath(__file__)
    # print os.getcwd()

    path = os.path.dirname(os.path.realpath(__file__))

    fData = True
    cLoc = path + '/../LatheCPP/include/'
    syncLoc = path + '/../SyncCPP/include/'

    xLoc = path + '/../../Xilinx/LatheCtl/'
    fEncLoc = path + '/../../Altera/Encoder/VHDL/'
    fLatheLoc = path + '/../../Altera/LatheNew/VHDL/'

    print("creating interface files")
    setup = Setup()
    setup.file = True
    setup.createConfig(configList)
    setup.createStrings(strList)
    setup.createCommands(cmdList, cLoc, fData)
    setup.createCommands(syncCmdList, syncLoc, fData, 'syncCmdDef')
    setup.createParameters(parmList, cLoc, fData)
    setup.createParameters(syncParmList, syncLoc, fData, 'syncParmDef')
    setup.createEnums(enumList, cLoc, fData)
    setup.createCtlBits(regList, cLoc, fData)

    setup.createFpgaReg(xilinxList, cLoc, xLoc, fData)
    setup.createFpgaBits(xilinxBitList, cLoc, xLoc, fData)

    setup.createFpgaReg(fpgaEncList, cLoc, fEncLoc, fData, \
                          pName="eRegDef", cName="fpgaEnc")
    setup.createFpgaBits(fpgaEncBitList, cLoc, fEncLoc, fData, \
                           pName="fpgaEnc", cName="fpgaEnc", \
                           package="FpgaEncBits", xName="FpgaEnc")

    setup.createFpgaReg(fpgaLatheList, cLoc, fLatheLoc, fData, \
                          pName="lRegDef", cName="fpgaLatheReg")
    setup.createFpgaBits(fpgaLatheBitList, cLoc, fLatheLoc, fData, \
                           pName="fpgaLathe", cName="fpgaLatheBits", \
                           package="FpgaLatheBits", xName="FpgaLathe")
    stdout.flush()
    stderr.flush()
    
    # xLoc = path + '/../../Xilinx/Spartan6LedTest/'

    # setup.createFpgaReg(xilinxEncList, cLoc, xLoc, fData, \
    #                       pName="xEncRegDef", \
    #                       table="encRegTable", \
    #                       cName="Enc", \
    #                       xName="encRegDef" )
    
    # setup.createFpgaBits(xilinxEncBitList, cLoc, xLoc, fData, \
    #                        pName="xEncBitDef", \
    #                        xName="xEnc", \
    #                        package="xEncBits", \
    #                        cName="xEnc")
