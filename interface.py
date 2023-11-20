#!/cygdrive/c/Python310/Python.exe

n = None

configList = \
    (
        "arc panel",

        ('arcAddFeed', 'arc '),
        ('arcBallDist', 'arc '),
        ('arcCCW', 'arc '),
        ('arcDiam', 'arc '),
        ('arcFeed', 'arc '),
        ('arcFinish', 'arc '),
        ('arcLargeEnd', 'arc '),
        ('arcLargeStem', 'arc '),
        ('arcPasses', 'arc '),
        ('arcPause', 'arc '),
        ('arcRetract', 'arc '),
        ('arcRadius', 'arc '),
        ('arcRPM', 'arc '),
        ('arcSmallEnd', 'arc '),
        ('arcSmallStem', 'arc '),
        ('arcSPInt', 'arc '),
        ('arcSpring', 'arc '),
        ('arcToolAngle', 'arc '),
        ('arcToolRad', 'arc '),
        ('arcType', 'arc '),
        ('arcXFeed', 'arc '),
        ('arcZFeed', 'arc '),
        ('arcZStart', 'arc '),

        "system config",

        ('cfgCmdDis', 'config disable sending commands'),
        ('cfgCommonLimits', 'config all limit switches on one pin'),
        ('cfgLimitsEnabled', 'config limits enabled'),
        ('cfgCommonHome', 'config all switches on one pin'),
        ('cfgDbgSave', 'config save debug info'),
        ('cfgDRO', 'config dro present'),
        ('cfgDROStep', 'config step pulse controls dro'),
        ('cfgDraw', 'config draw paths'),
        ('cfgEncoder', 'config encoder counts per revolution'),
        ('cfgEStop', 'config estop enable'),
        ('cfgEStopInv', 'config estop invert'),
        ('cfgExtDro', 'config external digital readout'),
        ('cfgFcy', 'config microprocessor clock frequency'),
        ('cfgFpga', 'config fpga interface present'),
        ('cfgFpgaFreq', 'config fpga frequency'),
        ('cfgFreqMult', 'config fpga frequency multiplier'),
        ('cfgHomeInPlace', 'config home in place'),
        ('cfgIntSync', 'config internal sync'),
        ('cfgInvEncDir', 'config fpga invert encoder direction'),
        ('cfgLCD', 'config enable lcd'),
        ('cfgMega', 'config control link to mega'),
        ('cfgMPG', 'config enable manual pulse generator'),
        ('cfgPrbInv', 'config invert probe signal'),
        ('cfgRemDbg', 'config print remote debug info'),
        ('cfgSpEncCap', 'config encoder on capture interrupt'),
        ('cfgSpEncoder', 'config spindle encoder'),
        ('cfgSpSync', 'config spindle using timer'),
        ('cfgSpSyncBoard', 'config spindle sync board'),
        ('cfgSpUseEncoder', 'config use spindle encoder for threading'),
        ('cfgSyncSPI', 'config sync comm through spi'),
        ('cfgTaperCycleDist', 'config taper cycle distance'),
        ('cfgTestMode', 'conifg test mode'),
        ('cfgTestRPM', 'config fpga test rpm value'),
        ('cfgTurnSync', 'config for turning synchronization'),
        ('cfgThreadSync', 'config for threading synchronization'),

        "communications cxonfig",

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

        "mega config",

        ('cfgMegaVFD', 'mega vfd speed mode'),
        ('cfgMegaEncTest', 'mega encoder test'),
        ('cfgMegaEncLines', 'mega encoder lines'),
        # ('mega', 'mega'),

        "spindle config",

        ('spAccel', 'spindle acceleration'),
        ('spAccelTime', 'spindle acceleration time'),
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
        ('spMegaSim', 'spindle use mega to simulate index and encoder'),

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
        ('thAlternate', 'thread alternate thread flanks'),
        ('thAngle', 'thread half angle of thread'),
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
        ('tuManual', 'turn manual mode'),
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
        ('xBackInc', 'z axis distance to go past for taking out backlash'),
        ('xBacklash', 'x axis '),
        ('xDoneDelay', 'x axis done to read dro delay'),
        ('xDroFinalDist', 'x dro final approach dist'),
        ('xDROInch', 'x axis '),
        ('xDROPos', 'x axis use dro to go to correct position'),
        ('xHomeDir', 'x axis '),
        ('xHomeDist', 'x axis '),
        ('xHomeDistBackoff', 'x axis '),
        ('xHomeDistRev', 'x axis '),
        ('xHomeEna', 'x axis '),
        ('xHomeEnd', 'x axis '),
        ('xHomeInv', 'x axis '),
        ('xHomeLoc', 'x axis '),
        ('xHomeSpeed', 'x axis '),
        ('xHomeStart', 'x axis '),
        ('xInvDRO', 'x axis invert dro'),
        ('xInvDir', 'x axis invert stepper direction'),
        ('xInvEnc', 'x axis '),
        ('xInvMpg', 'x axis invert mpg direction'),
        ('xJogMax', 'x axis '),
        ('xJogMin', 'x axis '),
        ('xLimEna', 'x axis limits enable'),
        ('xLimNegInv', 'x axis negative limit invert'),
        ('xLimPosInv', 'x axis positive limit invert'),
        ('xMpgInc', 'x axis jog increment'),
        ('xMpgMax', 'x axis jog maximum'),
        ('xJogSpeed', 'x axis '),
        ('xMaxSpeed', 'x axis '),
        ('xMicroSteps', 'x axis '),
        ('xMinSpeed', 'x axis '),
        ('xMotorRatio', 'x axis '),
        ('xMotorSteps', 'x axis '),
        ('xRetractLoc', 'x axis '),
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
        ('zDoneDelay', 'z axis done to read dro delay'),
        ('zDroFinalDist', 'z dro final approach dist'),
        ('zDROPos', 'z axis use dro to go to correct position'),
        ('zDROInch', 'z axis '),
        ('zHomeDir', 'z axis '),
        ('zHomeDist', 'z axis '),
        ('zHomeDistRev', 'z axis '),
        ('zHomeDistBackoff', 'z axis '),
        ('zHomeEna', 'z axis '),
        ('zHomeEnd', 'z axis '),
        ('zHomeInv', 'z axis '),
        ('zHomeLoc', 'z axis '),
        ('zHomeSpeed', 'z axis '),
        ('zHomeStart', 'z axis '),
        ('zInvDRO', 'z axis '),
        ('zInvDir', 'z axis '),
        ('zInvEnc', 'z axis '),
        ('zInvMpg', 'z axis '),
        ('zJogMax', 'z axis '),
        ('zJogMin', 'z axis '),
        ('zMpgInc', 'z axis jog increment'),
        ('zMpgMax', 'z axis jog maximum'),
        ('zJogSpeed', 'z axis '),
        ('zLimEna', 'z axis limits enable'),
        ('zLimNegInv', 'z axis negative limit invert'),
        ('zLimPosInv', 'z axis positive limit invert'),
        ('zMaxSpeed', 'z axis '),
        ('zMicroSteps', 'z axis '),
        ('zMinSpeed', 'z axis '),
        ('zMotorRatio', 'z axis '),
        ('zMotorSteps', 'z axis '),
        ('zRetractLoc', 'z axis '),
        ('zPitch', 'z axis '),
        ('zProbeDist', 'z axis '),
        ('zProbeSpeed', 'z axis '),

        "z axis position config",

        ('zSvPosition', 'z axis '),
        ('zSvHomeOffset', 'z axis '),
        ('zSvDROPosition', 'z axis '),
        ('zSvDROOffset', 'z axis '),

        ('cfgJogDebug', 'debug jogging'),
    )

strList = \
    (
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
        ("STR_HOME_SUCCESS", "Home Success"),
        ("STR_HOME_FAIL", "Home Fail"),
        ("STR_PROBE_SUCCESS", "Probe Success"),
        ("STR_PROBE_FAIL", "Probe Fail"),
        ("STR_STOPPED", "Stopped"),
        ("STR_CLR", ""),
    )

cmdList = \
    (
        "z motion commands",

        ("C_Z_MOVE_ABS", "cZMoveAbs",  "start z movement"),
        ("C_Z_MOVE_REL", "cZMoveRel",  "move z relative"),
        ("C_Z_J_MOV",    "cZJogMove",  "start z jog"),
        ("C_Z_J_SPEED",  "cZJogSpeed", "start z jog at speed"),
        ("C_Z_STOP",     "cZStop",     "stop z movement"),
        ("C_Z_SET_LOC",  "",           ""),
        ("C_Z_HOME_FWD", "cZHomeFwd",  "z home from positive side"),
        ("C_Z_HOME_REV", "cZHomeRev",  "z home from negative side"),

        "x motion commands",

        ("C_X_MOVE_ABS", "cXMoveAbs",  "start x movement"),
        ("C_X_MOVE_REL", "cXMoveRel",  "move x relative"),
        ("C_X_J_MOV",    "cXJogMove",  "start z jog"),
        ("C_X_J_SPEED",  "cXJogSpeed", "start x jog at speed"),
        ("C_X_STOP",     "cXStop",     "stop x movement"),
        ("C_X_SET_LOC",  "",           ""),
        ("C_X_HOME_FWD", "cXHomeFwd",  "x home from positive side"),
        ("C_X_HOME_REV", "cXHomeRev",  "x home from negative side"),

        "spindle operations",

        ("C_SPINDLE_START",     "cSpindleStart",    "start spindle"),
        ("C_SPINDLE_STOP",      "cSpindleStop",     "stop spindle"),
        ("C_SPINDLE_UPDATE",    "cSpindleUpdate",   "update spindle speed"),
        ("C_SPINDLE_JOG",       "cSpindleJog",      "spindle jog"),
        ("C_SPINDLE_JOG_SPEED", "cSpindleJogSpeed", "spindle jog at speed"),

        "end operations",

        ("C_CMD_PAUSE",   "cPauseCmd",   "pause current operation"),
        ("C_CMD_RESUME",  "cResumeCmd",  "resume current operation"),
        ("C_CMD_STOP",    "cStopCmd",    "stop current operation"),
        ("C_CMD_DONE",    "cDoneCmd",    "done current operation"),
        ("C_CMD_MEASURE", "cMeasureCmd", "stop at end of current pass"),

        "setup operations",

        ("C_CMD_CLEAR",    "cClearCmd",     "clear all tables"),
        ("C_CMD_SETUP",    "cSetup",        "setup everything"),
        ("C_CMD_SP_SETUP", "cSpindleSetup", "setup spindle"),

        ("C_CMD_SYNC_SETUP", "cSyncSetup", "setup z and x axis synchronization"),

        ("C_CMD_Z_SETUP",     "cZSetup",  "setup z axis"),
        ("C_CMD_Z_SYN_SETUP", "",         "setup z axis sync"),
        ("C_CMD_Z_SET_LOC",   "cZSetLoc", "setup z location"),

        ("C_CMD_X_SETUP",     "cXSetup",  "setup x axis"),
        ("C_CMD_X_SYN_SETUP", "",         "setup x axis sync"),
        ("C_CMD_X_SET_LOC",   "cXSetLoc", "setup x location"),

        "state information",

        ("C_READ_STAT",    "", "read status"),
        ("C_READ_I_STATE", "", "read states of state machines"),

        "load processor and xilinx parameters",

        ("C_LOAD_VAL",   "", "load parameters"),
        ("C_LOAD_MULTI", "", "load multiple parameters"),
        ("C_READ_VAL",   "", "read parameters"),
        ("C_LOAD_X_REG", "", "load xilinx registers"),
        ("C_READ_X_REG", "", "read xilinx registers"),

        "move command operations",

        ("C_CLEAR_QUE",       "cClearQue", "clear move que"),
        ("C_QUE_MOVE",        "", "que move command"),
        ("C_MOVE_MULTI",      "", "que move command"),
        ("C_MOVE_QUE_STATUS", "", "read move queue status"),

        "location and debug info",

        ("C_READ_ALL", "cReadAll",  "read all status info"),
        ("C_READ_DBG", "cReadDbg",  "read debug message"),
        ("C_CLR_DBG",  "cClearDbg", "clear debug message buffer"),

        "encoder commands",

        ("C_ENC_START", "", "encoder start"),
        ("C_ENC_STOP",  "", "encoder stop"),

        " mega commands ",

        ("C_SET_MEGA_VAL",  "", "set mega value"),
        ("C_READ_MEGA_VAL", "", "get mega value"),

        ("C_SEND_DONE", "cSendDone", "send commands done"),
    )

syncCmdList = \
    (
        ("SYNC_SETUP", "", "setup sync routine"),
        ("SYNC_START", "", "start sync routine"),
        ("SYNC_STOP", "", "stop sync routine"),
        ("SYNC_LOADVAL", "", "load parameters"),
        ("SYNC_LOADMULTI", "", "load multiple parameters"),
        ("SYNC_READVAL", "", "read parameters"),
        ("SYNC_POLL", "", "poll sync board"),
    )

megaCmdList = \
    (
        ("MEGA_NONE", "", "no command"),
        ("MEGA_SET_RPM", "", "set pwm for rpm"),
        ("MEGA_GET_RPM", "", "get pwm value"),
        ("MEGA_POLL", "", "poll mega info"),
        ("MEGA_SET_VAL", "", "set mega value"),
        ("MEGA_READ_VAL", "", "read mega value"),
        ("MEGA_ENC_START", "", "start mega encoder"),
        ("MEGA_ENC_STOP", "", "stop mega encoder"),
        ("MEGA_UPDATE_RPM", "", "update rpm if active"),
        # ("MEGA_", "", ""),
    )

parmList = \
    (
        "spindle parameters",

        ("SP_STEPS", "spindle motor steps", "int16_t"),
        ("SP_MICRO", "spindle micro steps", "int16_t"),
        ("SP_MIN_RPM", "spindle minimum rpm", "float"),
        ("SP_MAX_RPM", "spindle maximum rpm", "float"),
        ("SP_RPM", "spindle rpm", "float"),  #
        ("SP_ACCEL_TIME", "spindle accel time", "float"),
        ("SP_ACCEL", "spindle accel rpm/sec^2", "float"),
        ("SP_JOG_MIN_RPM", "spindle jog minimum rpm", "float"),
        ("SP_JOG_MAX_RPM", "spindle jog maximum rpm", "float"),
        ("SP_JOG_RPM", "spindle jog rpm", "float"),
        ("SP_JOG_ACCEL_TIME", "spindle jog accel time", "float"),
        ("SP_JOG_TIME_INITIAL", "spindle jog time initl", "float"),
        ("SP_JOG_TIME_INC", "spindle jog time increment", "float"),
        ("SP_JOG_TIME_MAX", "spindle jog timemax", "float"),
        ("SP_JOG_DIR", "spindle direction", "char"),
        ("SP_DIR_INV", "spindle invert direction", "char"),
        ("SP_TEST_INDEX", "generate test index pulse", "char"),
        ("SP_TEST_ENCODER", "generate enc test pulse", "char"),

        "z axis parameters",

        ("Z_PITCH",       "z axis leadscrew pitch", "float"),
        ("Z_RATIO",       "z axis ratio", "float"),
        ("Z_MICRO",       "z axis micro steps", "int16_t"),
        ("Z_MOTOR",       "z axis motor steps", "int16_t"),
        ("Z_ACCEL_TIME",  "z axis acceleration", "float"),
        ("Z_ACCEL",       "z accel rpm/sec^2", "float"),
        ("Z_BACKLASH",    "z axis backlash", "float"),
        ("Z_STEP_FACTOR", "z steps inch factored", "int"),
        ("Z_DIR_INV",     "z invert direction", "char"),
        ("Z_MPG_INV",     "z invert mpg", "char"),

        "x axis parameters",

        ("X_PITCH", "x axis leadscrew pitch", "float"),
        ("X_RATIO", "x axis ratio", "float"),
        ("X_MICRO", "x axis micro steps", "int16_t"),
        ("X_MOTOR", "x axis motor steps", "int16_t"),
        ("X_ACCEL_TIME", "x axis acceleration", "float"),
        ("X_ACCEL", "x accel rpm/sec^2", "float"),
        ("X_BACKLASH", "x axis backlash", "float"),
        ("X_STEP_FACTOR", "x steps inch factored", "int"),
        ("X_DIR_INV", "x invert direction", "char"),
        ("X_MPG_INV", "x invert mpg", "char"),
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
        ("LAST_INDEX_PERIOD", "last index period", "uint_t"),
        ("INDEX_PERIOD", "index period", "uint_t"),
        ("REV_COUNTER", "revolution counter", "uint_t"),

        "z home offset",

        ("Z_HOME_OFFSET", "z home offset", "int"),

        "x home offset",

        ("X_HOME_OFFSET", "x home offset", "int"),

        "z home parameters",

        ("Z_HOME_SPEED", "z final homing speed", "float"),
        ("Z_HOME_DIST", "z max homing distance", "float"),
        ("Z_HOME_DIST_REV", "z max rev homing distance", "float"),
        ("Z_HOME_DIST_BACKOFF", "z home backoff dist", "float"),
        ("Z_HOME_DIR", "z homing direction", "int"),

        "x home parameters",

        ("X_HOME_SPEED", "x final homing speed", "float"),
        ("X_HOME_DIST", "x max homing distance", "float"),
        ("X_HOME_DIST_REV", "x max rev homing distance", "float"),
        ("X_HOME_DIST_BACKOFF", "x home backoff dist", "float"),
        ("X_HOME_DIR", "x homing direction", "int"),

        "x home test parameters",

        ("X_HOME_LOC", "x home test location", "int"),
        ("X_HOME_START", "x start of home signal", "int"),
        ("X_HOME_END", "x end of home signal", "int"),

        "z dro",

        ("Z_DRO_LOC", "z dro location", "int"),
        ("Z_DRO_OFFSET", "z dro to zero", "int"),
        ("Z_DRO_COUNT_INCH", "z dro scale", "int"),
        ("Z_DRO_FACTOR", "x dro counts inch factored", "int"),
        ("Z_DRO_INVERT", "z dro invert", "int"),
        ("Z_USE_DRO", "z use dro for position", "char"),
        ("Z_DONE_DELAY", "z done to read dro delay", "int"),
        ("Z_DRO_FINAL_DIST", "z final approach distance", "int"),

        "x dro",

        ("X_DRO_LOC", "x dro location", "int"),
        ("X_DRO_OFFSET", "x dro to zero", "int"),
        ("X_DRO_COUNT_INCH", "x dro scale", "int"),
        ("X_DRO_FACTOR", "x dro counts inch factored", "int"),
        ("X_DRO_INVERT", "x dro invert", "int"),
        ("X_USE_DRO", "x use dro for position", "char"),
        ("X_DONE_DELAY", "x done to read dro delay", "int"),
        ("X_DRO_FINAL_DIST", "x final approach distance", "int"),

        "x home or probe status",

        # ("X_HOME_DONE", "x home done", "int"),
        ("X_HOME_STATUS", "x home status", "int"),

        "Z home or probe status",

        # ("Z_HOME_DONE", "z home done", "int"),
        ("Z_HOME_STATUS", "z home status", "int"),

        "probe configuration",

        ("PROBE_SPEED", "probe speed", "float"),
        ("PROBE_DIST", "probe test distance", "int"),
        ("PROBE_INV", "invert polarity of probe", "int"),

        "configuration",

        ("STEPPER_DRIVE", "stepper driven spindle", "char"),
        ("MOTOR_TEST", "use stepper to test motor", "char"),
        ("SPINDLE_ENCODER", "motor with spindle enc", "char"),
        ("SPINDLE_SYNC_BOARD", "spindle sync board", "char"),
        ("SPINDLE_INTERNAL_SYNC", "spindle internal sync", "char"),
        ("TURN_SYNC", "sync type for turning", "char"),
        ("THREAD_SYNC", "sync type for threading", "char"),
        # ("SPINDLE_SYNC", "spindle sync direct", "char"),
        # ("USE_ENCODER", "config for use encoder interrupt directly", "char"),
        # ("ENCODER_DIRECT", "use encoder interrupt directly", "char"),
        ("CAP_TMR_ENABLE", "enable capture timer", "char"),
        ("CFG_FPGA", "using fpga", "char"),
        ("CFG_MEGA", "control link to mega", "char"),
        ("CFG_MPG", "manual pulse generator", "char"),
        ("CFG_DRO", "digital readout", "char"),
        ("CFG_LCD", "lcd display", "char"),
        ("CFG_FCY", "system clock speed", "uint_t"),
        ("CFG_SWITCH", "spindle off on switch", "int"),
        ("CFG_VAR_SPEED", "spindle variable speed", "int"),

        "setup",

        ("SETUP_DONE", "setup done", "char"),

        "encoder counts per revolution",

        ("ENC_PER_REV", "spindle enc counts per rev", "uint16_t"),

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

        ("RPM", "current measured rpm", "int16_t"),

        "fpga frequency variables",

        ("FPGA_FREQUENCY", "fpga clock frequency", "int32_t"),
        ("FREQ_MULT", "frequency multiplier", "int16_t"),

        "xilinx configuration register",

        ("X_CFG_REG", "xilinx cfg register", "int16_t"),

        "z sync parameters",

        ("L_SYNC_CYCLE", "sync cycle length", "uint16_t"),
        ("L_SYNC_OUTPUT", "sync outputs per cycle", "uint16_t"),
        ("L_SYNC_IN_PRESCALER", "input sync prescaler", "uint16_t"),
        ("L_SYNC_OUT_PRESCALER", "output sync prescaler", "uint16_t"),

        "x sync parameters",

        ("L_X_SYNC_CYCLE", "sync cycle length", "uint16_t"),
        ("L_X_SYNC_OUTPUT", "sync outputs per cycle", "uint16_t"),
        ("L_X_SYNC_IN_PRESCALER", "input sync prescaler", "uint16_t"),
        ("L_X_SYNC_OUT_PRESCALER", "output sync prescaler", "uint16_t"),

        "threading variables",

        ("TH_Z_START", "threading z start", "int32_t"),
        ("TH_X_START", "threading x start", "int32_t"),
        ("TAN_THREAD_ANGLE", "tan of threading angle", "float"),
        ("X_FEED", "x feed", "int32_t"),
        ("RUNOUT_DISTANCE", "runout distance", "float"),
        ("RUNOUT_DEPTH", "runout depth", "float"),

        "jog debug",

        ("JOG_DEBUG", "jog interrupt debug", "char"),

        "motor and speed control",

        ("PWM_FREQ", "spindle speed pwm frequency", "uint_t"),
        ("MIN_SPEED", "min speed for current range", "int16_t"),
        ("MAX_SPEED", "max speed for current range", "int16_t"),

        "current operation",

        ("CURRENT_OP", "current operation", "char"),

        "global limits and home",

        ("LIMIT_OVERRIDE", "override limit switches", "char"),
        ("COMMON_LIMITS", "all limit switches one pin", "char"),
        ("LIMITS_ENABLED", "limits enabled", "char"),
        ("COMMON_HOME", "all home switches one pin", "char"),

        "z limits and home",

        ("Z_LIM_ENA", "z limit enable", "char"),
        ("Z_LIM_NEG_INV", "z negative limit invert", "char"),
        ("Z_LIM_POS_INV", "z Positive limit Invert", "char"),

        ("Z_HOME_ENA", "z home enable", "char"),
        ("Z_HOME_INV", "z home invert", "char"),

        "x limits and home",

        ("X_LIM_ENA", "x limit enable", "char"),
        ("X_LIM_NEG_INV", "x negative limit invert", "char"),
        ("X_LIM_POS_INV", "x Positive limit Invert", "char"),

        ("X_HOME_ENA", "x home enable", "char"),
        ("X_HOME_INV", "x home invert", "char"),

        "e stop",

        ("E_STOP_ENA", "enable estop", "char"),
        ("E_STOP_INV", "invert estop signal", "char"),

        "command pause",

        ("CMD_PAUSED", "move commands paused", "char"),

        "arc parameters",

        ("ARC_RADIUS", "arc radius", "float"),
        ("ARC_X_CENTER", "arc x center", "int"),
        ("ARC_Z_CENTER", "arc z center", "int"),
        ("ARC_X_START", "arc x start", "int"),
        ("ARC_Z_START", "arc z start", "int"),
        ("ARC_X_END", "arc x center", "int"),
        ("ARC_Z_END", "arc z center", "int"),

        ("MEGA_VFD", "mega vfd speed mode", "char"),
        ("MEGA_SIM", "mega encoder lines", "char"),

        ("USB_ENA", "enable usb", "char"),

        ("DRO_STEP", "step pulse drives dro", "char"),
        # ("", "", ""),
        # ("", "", ""),

        ("MAX_PARM", "maximum parameter", "int16_t")
    )

syncParmList = \
    (
        ("SYNC_CYCLE", "sync cycle length", "uint16_t"),
        ("SYNC_OUTPUT", "sync outputs per cycle", "uint16_t"),
        ("SYNC_PRESCALER", "sync prescaler", "uint16_t"),
        ("SYNC_ENCODER", "sync encoder pulses", "uint16_t"),
        ("SYNC_MAX_PARM", "sync maximum parameter", "int16_t"),
    )

megaParmList = \
    (
        ("M_PARM_RPM", "rpm value", "int"),
        ("M_PARM_VFD_ENA", "", "char"),
        ("M_PARM_PWM_CFG", "", "char"),
        ("M_PARM_ENC_TEST", "", "char"),
        ("M_PARM_ENC_LINES", "", "int"),
        ("M_PARM_MAX_PARM", "mega maximum parameter", "char"),
        # ("M_PARM_", "", "char"),
    )

riscvParmList = \
    (
        ("R_MV_STATUS", "move status",              "uint32_t"),
        ("R_JOG_PAUSE", "jog pause",                "int"),
        ("R_CUR_PASS",  "current pass",             "int"),
        ("R_CFG_VAL",   "fpga configuration value", "int"),
        ("R_P_RPM",     "spindle rpm",              "int"),
        ("R_PWM_DIV",   "pwm divider",               "int"),
        ("R_PWM_CTR",   "pwm counter maxy",         "int"),
        ("R_P_X_LOC",   "", "int"),
        ("R_P_Z_LOC",   "", "int"),
        ("R_P_X_DRO",   "", "int"),
        ("R_P_Z_DRO",   "", "int"),
        ("R_X_JOG_INC", "", "int"),
        ("R_Z_JOG_INC", "", "int"),
        # (R_PARM_, "", ""),
        # (R_PARM_, "", ""),
        # (R_PARM_, "", ""),
    )

regList = \
    (
        "common move command bits",

        ("CMD_MSK",     "(7 << 0)", "move mask"),
        
        ("CMD_MOV",     "(1 << 0)", "move a set distance"),
        ("CMD_JOG",     "(2 << 0)", "move while cmd are present"),
        ("CMD_SYN",     "(3 << 0)", "move dist synchronized to rotation"),
        ("CMD_MAX",     "(4 << 0)", "rapid move"),
        ("CMD_SPEED",   "(5 << 0)", "jog at speed"),
        ("JOG_SLOW",    "(6 << 0)", "slow jog for home or probe"),

        ("SYN_START",   "(1 << 3)", "start on sync pulse"),
        ("SYN_LEFT",    "(1 << 4)", "start sync left"),
        ("SYN_TAPER",   "(1 << 5)", "taper on other axis"),

        ("DIST_MODE",   "(1 << 6)", "distance update mode"),        
        ("FIND_HOME",   "(1 << 7)", "find home"),
        ("CLEAR_HOME",  "(1 << 8)", "move off of home"),
        ("FIND_PROBE",  "(1 << 9)", "find probe"),
        ("CLEAR_PROBE", "(1 << 10)", "move off of probe"),
        ("DRO_POS",     "(1 << 11)", "use dro for moving"),
        ("DRO_UPD",     "(1 << 12)", "update internal position from dro"),

        "common definitions",

        ("DIR_POS", "1", "positive direction"),
        ("DIR_NEG", "-1", "negative direction"),

        "z direction",

        ("ZPOS", "1", "z in positive direction"),
        ("ZNEG", "-1", "z in negative direction"),

        "x direction",

        ("XPOS", "1", "x in positive direction"),
        ("XNEG", "-1", "x in negative direction"),

        "feed types",

        ("FEED_PITCH", "0", "feed inch per rev"),
        ("FEED_TPI", "1", "feed threads per inch"),
        ("FEED_METRIC", "2", "feed mm per rev"),

        "home flag",

        ("HOME_SET", "(1 << 0)", ""),
        ("HOME_CLR", "(1 << 1)", ""),
        ("PROBE_SET", "(1 << 2)", ""),
        ("PROBE_CLR", "(1 << 3)", ""),

        "home direction",

        ("HOME_FWD", "0", ""),
        ("HOME_REV", "1", ""),

        "home status",

        ("HOME_ACTIVE", "0", ""),
        ("HOME_SUCCESS", "1", ""),
        ("HOME_FAIL", "2", ""),

        "probe status",

        ("PROBE_SUCCESS", "1", ""),
        ("PROBE_FAIL", "2", ""),

        "movement status",

        ("MV_PAUSE",        "(1 << 0)",  "movement paused"),
        ("MV_READ_X",       "(1 << 1)",  "pause x may change"),
        ("MV_READ_Z",       "(1 << 2)",  "pause z may change"),
        ("MV_ACTIVE",       "(1 << 3)",  "movement active"),
        ("MV_DONE",         "(1 << 4)",  "movement active"),
        ("MV_XLIMIT",       "(1 << 5)",  "at limit switch"),
        ("MV_ZLIMIT",       "(1 << 6)",  "at limit switch"),
        ("MV_XHOME_ACTIVE", "(1 << 7)",  "x home active"),
        ("MV_XHOME",        "(1 << 8)",  "x home success"),
        ("MV_ZHOME_ACTIVE", "(1 << 9)",  "z home active"),
        ("MV_ZHOME",        "(1 << 10)", "z home success"),
        ("MV_MEASURE",      "(1 << 11)", "pause for measurement"),
        ("MV_ESTOP",        "(1 << 12)", "estop"),

        "pause flags",

        ("DISABLE_JOG",     "(1 << 0)", "jogging disabled"),
        ("PAUSE_ENA_Z_JOG", "(1 << 1)", "enable z job during pause"),
        ("PAUSE_ENA_X_JOG", "(1 << 2)", "enable x jog during pause"),
        ("PAUSE_READ_Z",    "(1 << 3)", "read z after pause"),
        ("PAUSE_READ_X",    "(1 << 4)", "read x after pause"),

        "thread flags",

        ("TH_THREAD", "(1 << 0)", "threading"),
        ("TH_INTERNAL", "(1 << 1)", "internal threads"),
        ("TH_LEFT", "(1 << 2)", "left hand thread"),
        ("TH_RUNOUT", "(1 << 3)", "runout with thread"),

        "parameters for op_done",

        ("PARM_START", "0", "start of operation"),
        ("PARM_DONE", "1", "done operation"),

        "isr active flags",

        ("ARC_SHIFT", (6), "shift for arc syn"),

        ("SYNC_ACTIVE_EXT", "(1 << 0)", "active for sync board"),
        ("SYNC_ACTIVE_TMR", "(1 << 1)", "active for internal timer"),
        ("SYNC_ACTIVE_ENC", "(1 << 2)", "active for encoder"),
        ("SYNC_ACTIVE_STEP", "(1 << 3)", "active for stepper"),
        ("SYNC_ACTIVE_TAPER", "(1 << 4)", "active for taper"),
        ("SYNC_ACTIVE_THREAD", "(1 << 5)", "active for threading"),
        ("ARC_ACTIVE_EXT", "(SYNC_ACTIVE_EXT << ARC_SHIFT)", "arc sync board"),
        ("ARC_ACTIVE_TMR", "(SYNC_ACTIVE_TMR << ARC_SHIFT)", "arc int tmr"),
        ("ARC_ACTIVE_ENC", "(SYNC_ACTIVE_ENC << ARC_SHIFT)", "arc encoder"),
        ("ARC_ACTIVE_STEP", "(SYNC_ACTIVE_STEP << ARC_SHIFT)", "arc stepper"),

        "encoder direct flags",

        ("Z_ENCODER_DIRECT", "(1 << 0)", "z sync directly from encoder"),
        ("X_ENCODER_DIRECT", "(1 << 1)", "x sync directly from encoder"),

        "point by point movement commands",

        ("PCMD_INCX_HLDZ_S1", "(0 << 0)", "step x hold z then step 1"),
        ("PCMD_INCX_HLDZ_SN", "(1 << 0)", "step x hold z 1 then step z"),
        ("PCMD_HLDX_S1_INCZ", "(2 << 0)", "step x hold z then step 1"),
        ("PCMD_HLDX_SN_INCZ", "(3 << 0)", "hold x 1 then step x increment z"),
        ("PCMD_EXTEND", "(4 << 0)", "extend command"),
        ("PCMD_SPARE_0", "(5 << 0)", "spare 0"),
        ("PCMD_SPARE_1", "(5 << 0)", "spare 1"),
        ("PCMD_SET_DIR", "(7 << 0)", "set direction"),

        ("PCMD_X_NEG", "(1 << 0)", "mov x negative"),
        ("PCMD_Z_NEG", "(1 << 1)", "mov z negative"),
        ("PCMD_DIR_FLAG", "(1 << 2)", "direction flag"),

        ("PCMD_CMD_MASK", "(7 << 0)", "command mask"),

        ("PCMD_RPT_SHIFT", "(3)", "repeat mask"),
        ("PCMD_RPT_SHORT", "(32)", "repeat short"),
        ("PCMD_RPT_MASK", "(0x1f << PCMD_RPT_SHIFT)", "repeat shift"),

        ("PEXT_OFFSET", "(8)", ""),
        ("PEXT_INCX", "(0 << 0)", "step x"),
        ("PEXT_INCZ", "(1 << 0)", "step z"),
        ("PEXT_INCX_INCZ", "(2 << 0)", "step x and z"),
        ("PEXT_INCX2_INCZ", "(3 << 0)", "step x 2 step z"),

        # ("", "()", ""),
        # ("", "", ""),
    )

# ("", 0, 0, ""),
fpgaEncList = \
    (
        ("F_Noop", 0, 1, 0, "register 0"),

        ("F_Ld_Run_Ctl",   n, 1, 1, "load run control register"),
        ("F_Ld_Dbg_Ctl",   n, 1, 1, "load debug control register"),

        ("F_Ld_Enc_Cycle", n, 1, 2, "load encoder cycle"),
        ("F_Ld_Int_Cycle", n, 1, 2, "load internal cycle"),

        ("F_Rd_Cmp_Cyc_C" , n, 1, 4, "read cmp cycle clocks"),

        ("F_Ld_Dbg_Freq",  n, 1, 2, "load debug frequency"),
        ("F_Ld_Dbg_Count", n, 1, 2, "load debug clocks"),
    )

fpgaLatheList = \
    (
        "phase control",

        ("phaseCtl",),
        ("F_Ld_Phase_Len", 0, 1, 2, "'LLN' phase length"),
        ("F_Rd_Phase_Syn", n, 1, 4, "'RSY' read phase at sync pulse"),
        ("F_Phase_Max",    n, n, 0, "number of phase registers"),

        "controller",

        ("controller",),
        ("F_Ld_Ctrl_Data", 0, 1, 0, "'LCD' load controller data"),
        ("F_Ctrl_Cmd",     n, 1, 1, "'CMD' controller command"),
        ("F_Ld_Seq",       n, 1, 1, "'LSQ' load sequence"),
        ("F_Rd_Seq",       n, 1, 4, "'RSQ' read sequence"),
        ("F_Rd_Ctr",       n, 1, 4, "'RCT' read counter"),
        ("F_Ctrl_Max",     n, n, 0, "number of controller registers"),

        "reader",

        ("reader",),
        ("F_Ld_Read_Data", 0, 1, 0, "'LDR' load reader data"),
        ("F_Read",         n, 1, 0, "'RD'  read data"),
        ("F_Read_Max",     n, n, 0, "number of reader registers"),

        "PWM",

        ("pwmCtl",),
        ("F_Ld_PWM_Max",  0, 1, 4, "'MAX' pwm counter maximum"),
        ("F_Ld_PWM_Trig", n, 1, 4, "'TRG' pwm trigger"),
        ("F_PWM_Max",     n, n, 0, "number of pwm registers"),

        "encoder",

        ("encoder",),
        ("F_Ld_Enc_Cycle", 0, 1, 2, "'LEC' load encoder cycle"),
        ("F_Ld_Int_Cycle", n, 1, 2, "'LIC' load internal cycle"),
        ("F_Rd_Cmp_Cyc_C", n, 1, 4, "'RCC' read cmp cycle clocks"),
        ("F_Enc_Max",      n, n, 0, "number of encoder registers"),

        "debug frequency",

        ("dbgFreq",),
        ("F_Ld_Dbg_Freq",  0, 1, 2, "'DBF' debug frequency"),
        ("F_Ld_Dbg_Count", n, 1, 4, "'DBC' debug count"),
        ("F_Dbg_Freq_Max", n, n, 0, "number of debug frequency regs"),

        "sync accel",

        ("syncAccel",),
        ("F_Ld_D",           0, 1, 4, "'LIS' axis initial sum"),
        ("F_Ld_Incr1",       n, 1, 4, "'LI1' axis incr1"),
        ("F_Ld_Incr2",       n, 1, 4, "'LI2' axis incr2"),
        ("F_Ld_Accel_Val",   n, 1, 4, "'LAV' axis accel value"),
        ("F_Ld_Accel_Count", n, 1, 4, "'LAC' axis accel count"),

        ("F_Rd_XPos",        n, 1, 4, "'RX'  axis x pos"),
        ("F_Rd_YPos",        n, 1, 4, "'RY'  axis y pos"),
        ("F_Rd_Sum",         n, 1, 4, "'RSU' axis sum"),
        ("F_Rd_Accel_Sum",   n, 1, 4, "'RAS' axis accel sum"),
        ("F_Rd_Accel_Ctr",   n, 1, 4, "'RAC' axis accel counter"),

        ("F_Ld_Dist",        n, 1, 4, "'LDS' axis distance"),
        ("F_Ld_Max_Dist",    n, 1, 4, "'LMD' jog maximum distance"),
        # ("F_Ld_Backlash",    n, 1, 4, "'LB'  jog backlash"),

        ("F_Rd_Dist",        n, 1, 4, "'RDS' read axis distance"),
        ("F_Rd_Accel_Steps", n, 1, 4, "'RAS' read accel steps"),

        ("F_Ld_Loc",         n, 1, 4, "'LLC' axis location"),
        ("F_Rd_Loc",         n, 1, 4, "'RLC' read axis location"),

        # ("F_Ld_Mpg_Delta",   n, 1, 4, "'LMD' Mpg delta values"),
        # ("F_Ld_Mpg_Dist",    n, 1, 4, "'LMS' Mpg dist values"),
        # ("F_Ld_Mpg_Div",     n, 1, 4, "'LMV' Mpg div values"),
        
        ("F_Ld_Dro",         n, 1, 4, "'LDR' axis dro"),
        ("F_Ld_Dro_End",     n, 1, 4, "'LDE' axis dro end"),
        ("F_Ld_Dro_Limit",   n, 1, 4, "'LDL' axis dro decel limit"),
        ("F_Rd_Dro",         n, 1, 4, "'RDR' read axis dro"),

        ("F_Sync_Max",       n, n, 0, "number of sync registers"),

        "jog registers",

        ("jog",),
        ("F_Ld_Jog_Ctl",  0, 1, 4, "'CT' jog control"),
        ("F_Ld_Jog_Inc",  n, 1, 4, "'IN' jog increment"),
        ("F_Ld_Jog_Back", n, 1, 4, "'JB' jog backlash increment"),
        ("F_Jog_Max",     n, n, 0, "number of jog registers"),

        "axis",

        ("axisCtl",),
        ("F_Rd_Axis_Status", 0, 1,           1, "'RAS' read axis status"),
        ("F_Ld_Axis_Ctl",    n, 1,           2, "'LAC' set axis control reg"),
        ("F_Rd_Axis_Ctl",    n, 1,           2, "'RAC' read axis control reg"),
        ("F_Ld_Freq",        n, 1,           4, "'LFR' frequency"),
        ("F_Sync_Base",      n, "syncAccel", n, "sync registers"),
        ("F_Axis_Max",       n, n,           0, "num of axis regs"),

        "spindle",

        ("spindle",),
        ("F_Ld_Sp_Ctl",    0, 1,           1, "'LCT' spindle control reg"),
        ("F_Ld_Sp_Freq",   n, 1,           4, "'LFR' freq for step spindle"),
        ("F_Sp_Jog_Base",  n, "jog",       n, "'J' spindle jog"),
        ("F_Sp_Sync_Base", n, "syncAccel", n, "spindle sync"),

        "register definitions",

        ("regDef",),
        ("F_Noop",         0, 1,             1, "'NO' reg 0"),

        "status registers",

        ("F_Rd_Status",    n, 1,            4, "'RSTS' status reg"),
        ("F_Rd_Inputs",    n, 1,            4, "'RINP' inputs reg"),

        "control registers",

        ("F_Ld_Run_Ctl",   n, 1,            1, "'LRUN' set run control reg"),
        ("F_Rd_Run_Ctl",   n, 1,            1, "'RRUN' read run control reg"),
        ("F_Ld_Sync_Ctl",  n, 1,            1, "'LSYN' sync control reg"),
        ("F_Ld_Cfg_Ctl",   n, 1,            3, "'LCFG' config control reg"),
        ("F_Ld_Clk_Ctl",   n, 1,            1, "'LCLK' clock control reg"),
        ("F_Ld_Out_Reg",   n, 1,            1, "'LDOU' output reg"),
        ("F_Ld_Dsp_Reg",   n, 1,            1, "'LDSP' display reg"),

        "controller",

        ("F_Ctrl_Base",    n, "controller", n, "'C' controller"),

        "reader",

        ("F_Read_Base",    n, "reader",     n, "'R' reader"),

        "debug frequency control",

        ("F_Dbg_Freq_Base", n, "dbgFreq",   n, "'D' dbg frequency"),

        "spindle speed",

        ("F_Rd_Idx_Clks",  n, 1,            4, "'RIDX' clocks per index"),

        "step spindle frequency generator",

        "pwm",

        ("F_PWM_Base",     n, "pwmCtl",     n, "'P' pwm control"),

        "base for modules",

        ("F_Enc_Base",      n, "encoder",  n, "'E' encoder registers"),
        ("F_Phase_Base",    n, "phaseCtl", n, "'H' phase registers"),
        ("F_ZAxis_Base",    n, "axisCtl",  n, "'Z' z axis registers"),
        ("F_XAxis_Base",    n, "axisCtl",  n, "'X' x axis registers"),
        ("F_Spindle_Base",  n, "spindle",  n, "'S' spindle registers"),
        ("F_Cmd_Max",       n, n,          n, "number of commands"),
    )

xilinxList = \
    (
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
        ("XRDZASTP", "read z acl steps"),

        "read x motion",

        ("XRDXSUM", "read x sync sum"),
        ("XRDXXPOS", "read x sync x pos"),
        ("XRDXYPOS", "read x sync y pos"),
        ("XRDXACLSUM", "read x acl sum"),
        ("XRDXASTP", "read z acl steps"),

        "read distance",

        ("XRDZDIST", "read z distance"),
        ("XRDXDIST", "read x distance"),

        "read location",

        ("XRDZLOC", "read z location"),
        ("XRDXLOC", "read x location"),

        "read frequency and state",

        ("XRDFREQ", "read encoder freq"),
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

        ("XRDZCTL", "read control registers"),
        ("XRDXCTL", "read control registers")
    )

xilinxBitList = \
    (
        "z control register",

        ("zCtl",),
        ("zReset", 1, 0, "reset flag"),
        ("zStart", 1, 1, "start z"),
        ("zSrc_Syn", 1, 2, "run z synchronized"),
        ("zSrc_Frq", 0, 2, "run z from clock source"),
        ("zDir_In", 1, 3, "move z in positive dir"),
        ("zDir_Pos", 1, 3, "move z in positive dir"),
        ("zDir_Neg", 0, 3, "move z in negative dir"),
        ("zSet_Loc", 1, 4, "set z location"),
        ("zBacklash", 1, 5, "backlash move no pos upd"),
        ("zWait_Sync", 1, 6, "wait for sync to start"),

        "x control register",

        ("xCtl",),
        ("xReset", 1, 0, "x reset"),
        ("xStart", 1, 1, "start x"),
        ("xSrc_Syn", 1, 2, "run x synchronized"),
        ("xSrc_Frq", 0, 2, "run x from clock source"),
        ("xDir_In", 1, 3, "move x in positive dir"),
        ("xDir_Pos", 1, 3, "x positive direction"),
        ("xDir_Neg", 0, 3, "x negative direction"),
        ("xSet_Loc", 1, 4, "set x location"),
        ("xBacklash", 1, 5, "x backlash move no pos upd"),

        "taper control register",

        ("tCtl",),
        ("tEna", 1, 0, "taper enable"),
        ("tZ", 1, 1, "one for taper z"),
        ("tX", 0, 1, "zero for taper x"),

        "position control register",

        ("pCtl",),
        ("pReset", 1, 0, "reset position"),
        ("pLimit", 1, 1, "set flag on limit reached"),
        ("pZero", 1, 2, "set flag on zero reached"),

        "configuration register",

        ("cCtl",),
        ("zStep_Pol", 1, 0, "z step pulse polarity"),
        ("zDir_Pol", 1, 1, "z direction polarity"),
        ("xStep_Pol", 1, 2, "x step pulse polarity"),
        ("xDir_Pol", 1, 3, "x direction polarity"),
        ("enc_Pol", 1, 4, "encoder dir polarity"),
        ("zPulse_Mult", 1, 5, "enable pulse multiplier"),

        "debug control register",

        ("dCtl",),
        ("Dbg_Ena", 1, 0, "enable debugging"),
        ("Dbg_Sel", 1, 1, "select dbg encoder"),
        ("Dbg_Dir", 1, 2, "debug direction"),
        ("Dbg_Count", 1, 3, "gen count num dbg clks"),
        ("Dbg_Init", 1, 4, "init z modules"),
        ("Dbg_Rsyn", 1, 5, "running in sync mode"),
        ("Dbg_Move", 1, 6, "used debug clock for move"),

        "status register",

        ("stat",),
        ("s_Z_Done_Int", 1, 0, "z done interrupt"),
        ("s_X_Done_Int", 1, 1, "x done interrupt"),
        ("s_Dbg_Done", 1, 2, "debug done"),
        ("s_Z_Start", 1, 3, "z start"),
        ("s_X_Start", 1, 4, "x start"),
        ("s_Enc_Dir_In", 1, 5, "encoder direction in"),

        ""
    )

fpgaEncBitList = \
    (
        "run control register",

        ("rCtl",),
        ("ctlReset",     1, 0, "reset"),
        ("ctlTestClock", 1, 1, "testclock"),
        ("ctlSpare",     1, 2, "spare"),

        "debug control register",

        ("dCtl",),
        ("DbgEna",   1, 0, "enable debugging"),
        ("DbgSel",   1, 1, "select dbg encoder"),
        ("DbgDir",   1, 2, "debug direction"),
        ("DbgCount", 1, 3, "gen count num dbg clks"),

        ""
    )

fpgaLatheBitList = \
    (
        "RiscV control register",
        
        ("riscvCtl",),
        ("riscvData",     1, 0,  "riscv data active"),
        ("riscvSPI",      1, 1,  "riscv spi active"),

        "status register",

        ("status",),
        ("zAxisEna",      1, 0,  "'ZE' z axis enable flag"),
        ("zAxisDone",     1, 1,  "'ZD' z axis done"),
        ("zAxisCurDir",   1, 2,  "'Zd' z axis current dir"),
        ("xAxisEna",      1, 3,  "'XE' x axis enable flag"),
        ("xAxisDone",     1, 4,  "'XD' x axis done"),
        ("xAxisCurDir",   1, 5,  "'Xd' x axis current dir"),
        ("stEStop",       1, 6,  "'ES' emergency stop"),
        ("spindleActive", 1, 7,  "'S+' spindle active"),
        ("queNotEmpty",   1, 8,  "'Q+' ctl queue not empty"),
        ("ctlBusy",       1, 9,  "'CB' controller busy"),
        ("syncActive",    1, 10, "'SA' sync active"),

        "input register",

        ("inputs",),
        ("inZHome",  1, 0,  "z home switch"),
        ("inZMinus", 1, 1,  "z limit minus"),
        ("inZPlus",  1, 2,  "z Limit Plus"),
        ("inXHome",  1, 3,  "x home switch"),
        ("inXMinus", 1, 4,  "x limit minus"),
        ("inXPlus",  1, 5,  "x Limit Plus"),
        ("inSpare",  1, 6,  "spare input"),
        ("inProbe",  1, 7,  "probe input"),
        ("inPin10",  1, 8,  "pin 10"),
        ("inPin11",  1, 9,  "pin 11"),
        ("inPin12",  1, 10, "pin 12"),
        ("inPin13",  1, 11, "pin 13"),
        ("inPin15",  1, 12, "pin 15"),

        "output register",
        ("outputs",),
        ("outPin1",   1, 0,  "pin 1"),
        ("outPin14",  1, 1,  "pin 14"),
        ("outPin17",  1, 2,  "pin 17"),
        # ("",  , , ""),
        
        "pin out signals",
        ("pinOut",),
        ("pinOut2",   1,  0, ""),
        ("pinOut3",   1,  1, ""),
        ("pinOut4",   1,  2, ""),
        ("pinOut5",   1,  3, ""),
        ("pinOut6",   1,  4, ""),
        ("pinOut7",   1,  5, ""),
        ("pinOut8",   1,  6, ""),
        ("pinOut9",   1,  7, ""),
        ("pinOut1",   1,  8, ""),
        ("pinOut14",  1,  9, ""),
        ("pinOut16",  1, 10, ""),
        ("pinOut17",  1, 11, ""),

        "run control register",
        ("run",),
        ("runEna",     1, 0, "run from controller data"),
        ("runInit",    1, 1, "initialize controller"),
        ("readerInit", 1, 2, "initialize reader"),

        # "command register",
        # ("cmd",),
        # ("cmdWaitZ",    1, 0, "wait for z done"),
        # ("cmdWaitX",    1, 1, "wait for x done"),

        "jog control register",
        ("jog",),
        ("jogContinuous", 1, 0, "jog continuous mode"),
        ("jogBacklash",   1, 1, "jog backlash present"),

        "axis control register",

        ("axisCtl",),
        ("ctlInit",      1, 0,  "reset flag"),
        ("ctlStart",     1, 1,  "start"),
        ("ctlBacklash",  1, 2,  "backlash move no pos upd"),
        ("ctlWaitSync",  1, 3,  "wait for sync to start"),
        ("ctlDir",       1, 4,  "direction"),
        ("ctlSetLoc",    1, 5,  "set location"),
        ("ctlChDirect",  1, 6,  "ch input direct"),
        ("ctlSlave",     1, 7,  "slave ctl by other axis"),
        ("ctlDroEnd",    1, 8,  "use dro to end move"),
        ("ctlDistMode",  1, 9,  "distance udpdate mode"),
        ("ctlJogCmd",    1, 10, "jog with commands"),
        ("ctlJogMpg",    1, 11, "jog with mpg"),
        ("ctlHome",      1, 12, "homing axis"),
        ("ctlUseLimits", 1, 13, "use limits"),

        "axis status register",

        ("axisStatus",),
        ("axDoneDist",  1, 0, "axis done distance"),
        ("axDoneDro",   1, 1, "axis done dro"),
        ("axDoneHome",  1, 2, "axis done home"),
        ("axDoneLimit", 1, 3, "axis done limit"),
        ("axDistZero",  1, 4, "axis distance zero"),

        "configuration control register",

        ("cfgCtl",),
        ("cfgZDirInv",   1, 0, "z dir inverted"),
        ("cfgXDirInv",   1, 1, "x dir inverted"),
        ("cfgZDroInv",   1, 2, "z dro dir inverted"),
        ("cfgXDroInv",   1, 3, "x dro dir inverted"),
        ("cfgZMpgInv",   1, 4, "z mpg dir inverted"),
        ("cfgXMpgInv",   1, 5, "x mpg dir inverted"),
        ("cfgSpDirInv",  1, 6, "spindle dir inverted"),

        ("cfgZHomeInv",  1, 7, "z home inverted"),
        ("cfgZMinusInv", 1, 8, "z minus inverted"),
        ("cfgZPlusInv",  1, 9, "z plus inverted"),

        ("cfgXHomeInv",  1, 10, "x home inverted"),
        ("cfgXMinusInv", 1, 11, "x minus inverted"),
        ("cfgXPlusInv",  1, 12, "x plus inverted"),

        ("cfgProbeInv",  1, 13, "probe inverted"),

        ("cfgEncDirInv", 1, 14, "invert encoder dir"),
        ("cfgEStopEna",  1, 15, "estop enable"),
        ("cfgEStopInv",  1, 16, "estop invert"),
        ("cfgEnaEncDir", 1, 17, "enable encoder dir"),
        ("cfgGenSync",   1, 18, "generate sync pulse"),
        ("cfgPwmEna",    1, 19, "pwm enable"),
        ("cfgDroStep",   1, 20, "step pulse to dro"),

        "clock control register",

        ("clkCtl",),
        ("zFreqSel", n, (2, 0), "z Frequency select"),
        ("xFreqSel", n, (5, 3), "x Frequency select"),

        ("zFreqShift", 0, 0, "z Frequency shift"),
        ("xFreqShift", 3, 0, "x Frequency shift"),
        ("clkMask",    7, 0, "clock mask"),

        # "clock selection values",

        ("clkNone",    0, (2, 0), ""),
        ("clkFreq",    1, (2, 0), ""),
        ("clkCh",      2, (2, 0), ""),
        ("clkIntClk",  3, (2, 0), ""),
        ("clkSlvFreq", 4, (2, 0), ""),
        ("clkSlvCh",   5, (2, 0), ""),
        ("clkSpindle", 6, (2, 0), ""),
        ("clkDbgFreq", 7, (2, 0), ""),

        # "z clock values",

        ("zClkNone",    0, (2, 0), ""),
        ("zClkZFreq",   1, (2, 0), ""),
        ("zClkCh",      2, (2, 0), ""),
        ("zClkIntClk",  3, (2, 0), ""),
        ("zClkXFreq",   4, (2, 0), ""),
        ("zClkXCh",     5, (2, 0), ""),
        ("zClkSpindle", 6, (2, 0), ""),
        ("zClkDbgFreq", 7, (2, 0), ""),

        # "x clock values",

        ("xClkNone",    0, (5, 3), ""),
        ("xClkXFreq",   1, (5, 3), ""),
        ("xClkCh",      2, (5, 3), ""),
        ("xClkIntClk",  3, (5, 3), ""),
        ("xClkZFreq",   4, (5, 3), ""),
        ("xClkZCh",     5, (5, 3), ""),
        ("xClkSpindle", 6, (5, 3), ""),
        ("xClkDbgFreq", 7, (5, 3), ""),

        ("clkDbgFreqEna", 1, 6, "enable debug frequency"),

        "sync control register",

        ("synCtl",),
        ("synPhaseInit", 1, 0, "init phase counter"),
        ("synEncInit",   1, 1, "init encoder"),
        ("synEncEna",    1, 2, "enable encoder"),

        "spindle control register",

        ("spCtl",),
        ("spInit",      1, 0, "spindle init"),
        ("spEna",       1, 1, "spindle enable"),
        ("spDir",       1, 2, "spindle direction"),
        ("spJogEnable", 1, 3, "spindle jog enable"),

        "",                     # end marker
        # ("",),
        # ("",  , , ""),

        # "",
        # ("",),
        # ("",  , , ""),
    )

enumList = \
    (
        # "z control states",

        # "enum z_States",
        # "{",
        # ("ZIDLE", "idle"),
        # ("ZWAITBKLS", "wait for backlash move complete"),
        # ("ZSTARTMOVE", "start z move"),
        # ("ZWAITMOVE", "wait for move complete"),
        # ("ZDELAY", "wait for position to settle"),
        # ("ZDONE", "clean up state"),
        # "};",

        # "x control states",

        # "enum x_States",
        # "{",
        # ("XIDLE", "idle"),
        # ("XWAITBKLS", "wait for backlash move complete"),
        # ("XSTARTMOVE", "start x move"),
        # ("XWAITMOVE", "wait for move complete"),
        # ("XDELAY", "wait for position to settle"),
        # ("XDONE", "clean up state"),
        # "};",

        "axis control states",

        "enum axis_States",
        "{",
        ("AXIS_IDLE = 0", "idle"),
        ("AXIS_WAIT_BACKLASH = 1", "wait for backlash move complete"),
        ("AXIS_START_MOVE = 2", "start axis move"),
        ("AXIS_WAIT_MOVE = 3", "wait for move complete"),
        ("AXIS_DELAY = 4", "wait for position to settle"),
        ("AXIS_DONE = 5", "clean up state"),
        ("AXIS_STATES = 6", "number of states"),
        "};",

        "move control states",

        "enum m_States",
        "{",
        ("M_IDLE", "idle state"),
        ("M_WAIT_Z", "wait for z to complete"),
        ("M_WAIT_X", "wait for x to complete"),
        ("M_WAIT_SPINDLE", "wait for spindle start"),
        ("M_WAIT_SYNC_PARMS", "wait for sync parameters"),
        ("M_WAIT_SYNC_CMD", "wait for sync command"),
        ("M_START_SYNC", "start sync"),
        ("M_WAIT_SYNC_READY", "wait for sync"),
        ("M_WAIT_SYNC_DONE", "wait for sync done"),
        ("M_WAIT_MEASURE_DONE", "wait for measurement done"),
        ("M_WAIT_PROBE", "wait for probe to complete"),
        ("M_WAIT_MEASURE", "wait for measurement to complete"),
        ("M_WAIT_SAFE_X", "wait for move to safe x to complete"),
        ("M_WAIT_SAFE_Z", "wait for move to safe z to complete"),
        ("M_WAIT_ARC", "wait for arc move to complete"),
        "};",

        "move control commands",

        "enum m_Commands",
        "{",
        ("Q_MOVE_Z", "move z"),
        ("Q_MOVE_X", "move x"),
        ("Q_SAVE_Z", "save z"),
        ("Q_SAVE_X", "save x"),
        ("Q_SAVE_Z_OFFSET", "save z offset"),
        ("Q_SAVE_X_OFFSET", "save x offset"),
        ("Q_SAVE_TAPER", "save taper"),
        ("Q_MOVE_Z_X", "move x in sync with z"),
        ("Q_MOVE_X_Z", "move z in sync with x"),
        ("Q_TAPER_Z_X", "taper x"),
        ("Q_TAPER_X_Z", "taper z"),
        ("Q_START_SPINDLE", "spindle start"),
        ("Q_STOP_SPINDLE", "spindle stop"),
        ("Q_Z_SYN_SETUP", "z sync setup"),
        ("Q_X_SYN_SETUP", "x sync setup"),
        ("Q_SEND_SYNC_PARMS", "send sync parameters"),
        ("Q_SYNC_COMMAND", "send sync command"),
        ("Q_PASS_NUM", "set pass number"),
        ("Q_QUE_PAUSE", "pause queue"),
        ("Q_MOVE_Z_OFFSET", "move z offset"),
        ("Q_SAVE_FEED_TYPE", "save feed type"),
        ("Q_Z_FEED_SETUP", "setup z feed"),
        ("Q_X_FEED_SETUP", "setup x feed"),
        ("Q_SAVE_FLAGS", "save thread flags"),
        ("Q_PROBE_Z", "probe in z direction"),
        ("Q_PROBE_X", "probe in x direction"),
        ("Q_SAVE_Z_DRO", "save z dro reading"),
        ("Q_SAVE_X_DRO", "save x dro reading"),
        ("Q_QUE_PARM", "save parameter in queue"),
        ("Q_MOVE_ARC", "move in an arc"),
        ("Q_OP_DONE", "operation done"),
        "};",

        "move control operation",

        "enum operations",
        "{",
        ("OP_TURN", "turn"),
        ("OP_FACE", "face"),
        ("OP_CUTOFF", "cutoff"),
        ("OP_TAPER", "taper"),
        ("OP_THREAD", "thread"),
        ("OP_ARC", "arc"),
        "};",

        "home control states",

        "enum h_States",
        "{",
        ("H_IDLE", "idle state"),
        ("H_HOME", "found home switch"),
        ("H_OFF_HOME", "off home switch"),
        ("H_BACKOFF", "backoff dist from switch"),
        ("H_SLOW", "found home slowly"),
        # ("H_", ""),
        "};",

        "debug axis message types",

        "enum D_Axis_Message",
        "{",
        ("D_BASE", "axis base"),        
        ("D_MVCM", "move command"),
        ("D_ACTL", "axisctl"),
        ("D_MOV",  "move location"),
        ("D_CUR",  "current location"),
        ("D_LOC",  "end location"),
        ("D_DST",  "distance"),
        ("D_STP",  "steps"),
        ("D_ST",   "state"),
        ("D_BSTP", "backlash steps"),
        ("D_DRO",  "dro location"),
        ("D_PDRO", "pass dro location"),
        ("D_EXP",  "expected location"),
        ("D_ERR",  "error with respect to dro"),
        ("D_WT",   "wait"),
        ("D_DN",   "done"),
        ("D_EST",  "spindle encoder start count"),
        ("D_EDN",  "spindle encoder done count"),
        ("D_X",    ""),
        ("D_Y",    ""),
        ("D_IDXD", "dro at index pulse"),
        ("D_IDXP", "position at index pulse"),
        ("D_AMAX", "axis maximum"),
        "};",

        "debug message types",

        "enum d_Message",
        "{",
        ("D_PASS",  "'PASS' pass done"),
        ("D_DONE",  "'DONE' all operations done"),
        ("D_TEST",  "'TEST' test message"),
        ("D_HST",   "'HST ' home state"),
        ("D_MSTA",  "'MSTA' move state"),
        ("D_MCMD",  "'MCMD' move command"),
        
        ("D_XBASE", "'XBAS' x base"),
        ("D_XMVCM", "'XMVC' x move command"),
        ("D_XACTL", "'XCTL' x axis ctl"),
        ("D_XMOV",  "'XMOV' x move to location"),
        ("D_XCUR",  "'XCUR' x current location"),
        ("D_XLOC",  "'XLOC' x end location"),
        ("D_XDST",  "'XDST' x distance"),
        ("D_XSTP",  "'XSTP' x steps"),
        ("D_XST",   "'XSTA' x state"),
        ("D_XBSTP", "'XBLS' x backlash steps"),
        ("D_XDRO",  "'XDRO' x dro location"),
        ("D_XPDRO", "'XPDR' x pass dro location"),
        ("D_XEXP",  "'XEXP' x expected location"),
        ("D_XERR",  "'XERR' x error with respect to dro"),
        ("D_XWT",   "'XWT ' x wait"),
        ("D_XDN",   "'XDN ' x done"),
        ("D_XEST",  "'XEST' x spindle encoder start count"),
        ("D_XEDN",  "'XEDN' x spindle encoder done count"),
        ("D_XX",    "'XX  ' x "),
        ("D_XY",    "'XY  ' x "),
        ("D_XIDXD", "'XIDR' x dro at index pulse"),
        ("D_XIDXP", "'XIPO' x position at index pulse"),

        ("D_ZBASE", "'ZBAS' Z base"),
        ("D_ZMVCM", "'ZMVC' z move command"),
        ("D_ZACTL", "'ZCTL' z axis ctl"),
        ("D_ZMOV",  "'ZMOV' z move location"),
        ("D_ZCUR",  "'ZCUR' x current location"),
        ("D_ZLOC",  "'ZLOC' z end location"),
        ("D_ZDST",  "'ZDST' z distance"),
        ("D_ZSTP",  "'ZSTP' z steps"),
        ("D_ZST",   "'ZSTA' z state"),
        ("D_ZBSTP", "'ZBLS' z backlash steps"),
        ("D_ZDRO",  "'ZDRO' z dro location"),
        ("D_ZPDRO", "'ZPDR' z pass dro location"),
        ("D_ZEXP",  "'ZEXP' z expected location"),
        ("D_ZERR",  "'ZERR' z error with respect to dro"),
        ("D_ZWT",   "'ZWT ' z wait"),
        ("D_ZDN",   "'ZDN ' z done"),
        ("D_ZEST",  "'ZEST' z spindle encoder start count"),
        ("D_ZEDN",  "'ZEDN' Z spindle encoder done count"),
        ("D_ZX",    "'ZX  ' z "),
        ("D_ZY",    "'ZY  ' z "),
        ("D_ZIDXD", "'ZIDR' z dro at index pulse"),
        ("D_ZIDXP", "'ZIPO' z position at index pulse"),
        ("D_MAX",   "'MAX ' debug maximum"),

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
        ("SEL_TU_STEP", "Stepper"),
        ("SEL_TU_ENC", "Encoder"),
        ("SEL_TU_ISYN", "Int Syn"),
        ("SEL_TU_ESYN", "Ext Syn"),
        ("SEL_TU_SYN", "Sync"),
        "};",

        "threading sync selector",

        "enum sel_Thread c",
        "{",
        ("SEL_TH_NO_ENC", "No Encoder"),
        ("SEL_TH_STEP", "Stepper"),
        ("SEL_TH_ENC", "Encoder"),
        ("SEL_TH_ISYN_RENC", "Int Syn, Runout Enc"),
        ("SEL_TH_ESYN_RENC", "Ext Syn, Runout Enc"),
        ("SEL_TH_ESYN_RSYN", "Ext Syn, Runout Syn"),
        ("SEL_TH_SYN", "Syn, Runout Syn"),
        "};",

        "arc config selector",

        "enum sel_Arc_Type c",
        "{",
        ("SEL_ARC_END", "End"),
        ("SEL_ARC_CORNER", "Corner"),
        ("SEL_ARC_SMALL", "Small Ball"),
        ("SEL_ARC_LARGE", "Large Ball"),
        ("SEL_ARC_SMALL_STEM", "Small Stem"),
        ("SEL_ARC_LARGE_STEM", "Large Stem"),
        "};",

        "mpg control states",
        
        "enum mpg_State c",
        "{",
        ("MPG_DISABLED",        "'DS' disabled"),
        ("MPG_CHECK_QUE",       "'CQ' check queue"),
        ("MPG_DIR_CHANGE_WAIT", "'DC' wait for direction change"),
        ("MPG_WAIT_BACKLASH",   "'WB' wait for backlash"),
        "};",

        "riscv actions",
        
        "enum riscv_Cmd c",
        "{",
        ("R_NONE",        "'NO' no operation"),
        ("R_OP_START",    "'OS' start"),
        ("R_OP_DONE",     "'OD' done"),
        ("R_SETUP",       "'SU' setup"),
        ("R_RESUME",      "'RE' resume"),
        ("R_STOP",        "'SP' stop"),
        ("R_STOP_X",      "'SX' stop x"),
        ("R_STOP_Z",      "'SZ' stop z"),
        ("R_DONE",        "'DN' done"),
        ("R_SEND_DONE",   "'ND' send data done"),

        ("R_SET_LOC_X",   "'LX' set x loc"),
        ("R_SET_LOC_Z",   "'LZ' set z loc"),

        ("R_PAUSE",       "'PA' pause"),
        ("R_START_SPIN",  "'S+' start spindle"),
        ("R_STOP_SPIN",   "'S-' stop spindle"),
        ("R_UPDATE_SPIN", "'US' update spindle speed"),
        # ("R_WAIT_Z",      "'WZ' wait z"),
        # ("R_WAIT_X",      "'WX' wait x"),

        ("R_PASS",        "'PS' pass"),

        ("R_SET_ACCEL",   "'SA' set accel parm"),
        ("R_SET_ACCEL_Q", "'SQ' set accel parm queued"),
        ("R_SET_DATA",    "'SD' set data"),
        ("R_GET_DATA",    "'GD' set data"),

        ("R_SAVE_Z",      "'VZ' save z"),
        ("R_SAVE_X",      "'VX' save x"),

        ("R_STEPS_Z",     "'IZ' save z steps inch"),
        ("R_STEPS_X",     "'IX' save x steps inch"),

        ("R_HOFS_Z",      "'HZ' home offset z"),
        ("R_HOFS_X",      "'HX' home offset x"),

        ("R_JOG_Z",       "'JZ' jog move z"),
        ("R_JOG_X",       "'JX' jog move x"),

        ("R_MOVE_Z",      "'MZ' move z"),
        ("R_MOVE_X",      "'MX' move x"),

        ("R_MOVE_REL_Z",  "'RZ' move rel z"),
        ("R_MOVE_REL_X",  "'RX' move rel x"),

        ("R_READ_ALL",    "'RA' read all status"),
        ("R_READ_DBG",    "'RD' read all status"),
        ("R_MAX_CMD",     "'MX' max value"),
        # ("R_", ""),
        # ("R_", ""),
        "};",

        "riscv axis name",

        "enum Riscv_Axis_Name_Type c",
        "{",
        ("RA_NONE", ""),
        ("RA_Z_AXIS", ""),
        ("RA_X_AXIS", ""),
        # ("RS_", ""),
        "};",

        "riscv data",
        
        "enum Riscv_Data_Type c",
        "{",
        ("RD_NONE", ""),
        ("RD_Z_BACKLASH", ""),
        ("RD_X_BACKLASH", ""),
        # ("RD_", ""),
        "};",

        "accel types",

        "enum accel_Type c",
        "{",
         ("A_TURN  = 0", "'TU'"),
         ("A_TAPER = 1", "'TP'"),
         ("A_MOVE  = 2", "'MV'"),
         ("A_JOG   = 3", "'JG'"),
         ("A_SLOW  = 4", "'JS'"),
        "};",

        "riscv accel types",

        "enum axis_Accel_Type c",
        "{",
         ("RP_Z_TURN  = 0", "'ZT'"),
         ("RP_Z_TAPER = 1", "'ZP'"),
         ("RP_Z_MOVE  = 2", "'ZM'"),
         ("RP_Z_JOG   = 3", "'ZJ'"),
         ("RP_Z_SLOW  = 4", "'ZS'"),
         ("RP_X_TURN  = 5", "'XT'"),
         ("RP_X_TAPER = 6", "'XP'"),
         ("RP_X_MOVE  = 7", "'XM'"),
         ("RP_X_JOG   = 8", "'XJ'"),
         ("RP_X_SLOW  = 9", "'XS'"),
         ("RP_MAX     = 10", ""),
        "};",

        "riscv accel axis base index",

        "enum accel_Base c",
        "{",
         ("RP_Z_BASE  = 0", ""),
         ("RP_X_BASE  = 5", ""),
        "};",

        "riscv axis states",

        "enum Riscv_Axis_State_Type c",
        "{",
        ("RS_IDLE",          ""),
        ("RS_WAIT_BACKLASH", ""),
        ("RS_WAIT",          ""),
        ("RS_WAIT_TAPER",    ""),
        # ("RS_", ""),
        "};",

        "riscv accel parameters",

        "enum Riscv_Sync_Parm_Type c",
        "{",
        ("RP_INITIAL_SUM", ""),
        ("RP_INCR1",       ""),
        ("RP_INCR2",       ""),
        ("RP_ACCEL_VAL",   ""),
        ("RP_ACCEL_COUNT", ""),
        ("RP_FREQ_DIV",    ""),
        # ("RP_", ""),
        "};",
        
        "riscv run wait states",

        "enum riscv_Run_Wait c",
        "{",
        ("RW_NONE",       "'NO' none"),
        ("RW_PAUSE",      "'PS' wait pause"),
        ("RW_SPIN_START", "'S+' wait spindle start"),
        ("RW_SPIN_STOP",  "'S-' wait spindle stop"),
        ("RW_WAIT_X",     "'WX' wait x done"),
        ("RW_WAIT_Z",     "'WZ' wait z done"),
        # ("RW_", "''"),
        "};",

        "commands in ctlbits",

        "enum move_Cmd c",
        "{",
        ("M_CMD_NONE  = 0", "no command"),
        ("M_CMD_MOV   = 1", "move a set distance"),
        ("M_CMD_JOG   = 2", "move while cmd are present"),
        ("M_CMD_SYN   = 3", "move dist synchronized to rotation"),
        ("M_CMD_MAX   = 4", "rapid move"),
        ("M_CMD_SPEED = 5", "jog at speed"),
        ("M_JOG_SLOW  = 6", "slow jog for home or probe"),
        "};",

        "riscv run wait states",

        "enum move_Bit c",
        "{",
        ("M_RSV_0       = 0",  "no command"),
        ("M_RSV_1       = 1",  "no command"),
        ("M_RSV_2       = 2",  "no command"),

        ("M_SYN_START   = 3",  "start on sync pulse"),
        ("M_SYN_LEFT    = 4",  "start sync left"),
        ("M_SYN_TAPER   = 5",  "taper on other axis"),

        ("M_DIST_MODE   = 6",  "distance update mode"),
        ("M_FIND_HOME   = 7",  "find home"),
        ("M_CLEAR_HOME  = 8",  "move off of home"),
        ("M_FIND_PROBE  = 9",  "find probe"),
        ("M_CLEAR_PROBE = 10", "move off of probe"),
        ("M_DRO_POS     = 11", "use dro for moving"),
        ("M_DRO_UPD     = 12", "update internal position from dro"),
        ("M_BIT_MAX     = 13", "number of bits"),
        "};",

        "movement status",

        "enum mv_Status_Bits c",
        "{",
        ("R_MV_PAUSE        = 0",  "'PA' movement paused"),
        ("R_MV_READ_X       = 1",  "'RX' pause x may change"),
        ("R_MV_READ_Z       = 2",  "'RZ' pause z may change"),
        ("R_MV_ACTIVE       = 3",  "'AC' movement active"),
        ("R_MV_DONE         = 4",  "'DN' movement active"),
        ("R_MV_XLIMIT       = 5",  "'XL' at limit switch"),
        ("R_MV_ZLIMIT       = 6",  "'ZL' at limit switch"),
        ("R_MV_XHOME_ACTIVE = 7",  "'XA' x home active"),
        ("R_MV_XHOME        = 8",  "'XH' x home success"),
        ("R_MV_ZHOME_ACTIVE = 9",  "'ZA' z home active"),
        ("R_MV_ZHOME        = 10", "'ZH' z home success"),
        ("R_MV_MEASURE      = 11", "'MS' pause for measurement"),
        ("R_MV_ESTOP        = 12", "'ES' estop"),
        ("R_MV_MAX          = 13", "number of bits"),
        "};",
        
        "pause flags",

        "enum pause_Bits c",
        "{",
        ("R_DISABLE_JOG     = 0", "'DJ' jogging disabled"),
        ("R_PAUSE_ENA_Z_JOG = 1", "'EZ' enable z job during pause"),
        ("R_PAUSE_ENA_X_JOG = 2", "'EX' enable x jog during pause"),
        ("R_PAUSE_READ_Z    = 3", "'RX' read z after pause"),
        ("R_PAUSE_READ_X    = 4", "'RZ' read x after pause"),
        ("R_PAUSE_MAX       = 5", "number of bits"),
        "};",
    )

megaEnumList = \
    (
        "mega poll response bits",

        "enum poll_Mega",
        "{",
        ("M_POLL_ESTOP_NO", "estop no in"),
        ("M_POLL_ESTOP_NC", "estop nc in"),
        ("M_POLL_SP_FWD", "spindle forward in"),
        ("M_POLL_SP_REV", "spindle reverse in"),
        ("M_POLL_ESTOP", "estop condition"),
        ("M_POLL_WD_ENA", "watchdog enabled"),
        ("M_POLL_CP_ACTIVE", "charge pump active"),
        ("M_POLL_PWM_ACTIVE", "pwm active"),
        ("M_POLL_STEP_DIS", "stepper disabled"),
        ("M_POLL_ESTOP_RLY", "estop relay"),
        ("M_POLL_ESTOP_PC", "estop pc"),
        # ("M_POLL_", ""),
        "};",

        "mega vfd speed selector",

        "enum vfdSpeed c",
        "{",
        ("MEGA_SLOW_PWM", "Slow PWM"),
        ("MEGA_FAST_PWM", "Fast PWM"),
        ("MEGA_DIRECT_RPM", "Set RPM"),
        "};",
    )

xilinxEncList = \
    (
        "skip register zero",

        ("XNOOP", "register 0"),

        "load control registers",
    )

if __name__ == '__main__':
    import os
    from os.path import join as osJoin
    from setup import Setup
    from sys import stderr, stdout
    from platform import system

    # print os.path.realpath(__file__)
    # print os.getcwd()

    R_PI = False
    WINDOWS = system() == 'Windows'
    if WINDOWS:
        # from pywinusb.hid import find_all_hid_devices
        # from comm import Comm, CommTimeout
        # from commPi import Comm, CommTimeout

        R_PI = True
    else:
        if not os.uname().machine.startswith('arm'):
            pass
            # from comm import Comm, CommTimeout
        else:
            pass
            # from commPi import Comm, CommTimeout

            R_PI = True

    fData = True
    # if WINDOWS:

    path = os.path.dirname(os.path.realpath(__file__))

    cLoc     = osJoin(path, '..', 'LatheCPP', 'include')
    syncLoc  = osJoin(path, '..', 'SyncCPP', 'include')
    megaLoc  = osJoin(path, '..', '..', 'Arduino', 'output')
    riscvLoc = osJoin(path, '..', '..', 'neorv32', 'sw', 'example', \
                      'LatheRiscV')

    xLoc      = osJoin(path, '..', '..', 'Xilinx', 'LatheCtl')
    fEncLoc   = osJoin(path, '..', '..', 'Altera', 'Encoder', 'VHDL')
    fLatheLoc = osJoin(path, '..', '..', 'Altera', 'LatheNew', 'VHDL')

    # else:
    #     path = os.path.dirname(os.path.realpath(__file__))

    #     cLoc     = osJoin(path, '..', 'LatheCPP', 'include')
    #     syncLoc  = osJoin(path, '..', 'SyncCPP', 'include')
    #     megaLoc  = osJoin(path, '..', '..', 'Arduino', 'output')
    #     riscvLoc = osJoin(path, '..', '..', 'neorv32', 'sw', 'examples', 'Lathe')

    #     xLoc      = osJoin(path, '..', 'Xilinx', 'LatheCtl')
    #     fEncLoc   = osJoin(path, '..', 'Altera', 'Encoder', 'VHDL')
    #     fLatheLoc = osJoin(path, '..', 'Altera', 'LatheNew', 'VHDL')

    # print("creating interface files")
    setup = Setup()
    setup.file = True
    setup.createConfig(configList)
    setup.createStrings(strList)

    setup.createCommands(cmdList, cLoc, fData)

    setup.createCommands(syncCmdList, cLoc, fData, prefix='sync')
    setup.createCommands(syncCmdList, syncLoc, fData,
                         pyFile=False, check=False, prefix='sync')

    setup.createCommands(megaCmdList, cLoc, fData, prefix='mega',
                         pyFile=False)
    setup.createCommands(megaCmdList, megaLoc, fData,
                         pyFile=False, check=False, prefix='mega')

    setup.createParameters(parmList, cLoc, fData)

    setup.createParameters(syncParmList, cLoc, fData, prefix='sync',
                           cSource=None)
    setup.createParameters(syncParmList, syncLoc, fData, pyFile=False,
                           cSource=osJoin('..', 'src'), prefix='sync')

    setup.createParameters(megaParmList, cLoc, fData, pyFile=False,
                           cSource=None, prefix='mega')
    setup.createParameters(megaParmList, megaLoc, fData, pyFile=True,
                           cSource='', prefix='mega')

    setup.createParameters(riscvParmList, cLoc, fData, pyFile=False,
                           cSource=None, prefix='riscv')
    setup.createParameters(riscvParmList, riscvLoc, fData, pyFile=True,
                           cSource='', prefix='riscv', cExt="c")

    setup.createEnums(enumList, cLoc, fData)

    setup.createEnums(megaEnumList, cLoc, fData, pyFile=True,
                      prefix="mega")
    setup.createEnums(megaEnumList, megaLoc, fData, pyFile=False,
                      prefix="mega")

    setup.createCtlBits(regList, cLoc, fData)

    # setup.createFpgaReg(xilinxList, cLoc, xLoc, fData)
    # setup.createFpgaBits(xilinxBitList, cLoc, xLoc, fData)

    setup.createFpgaReg(fpgaEncList, cLoc, fEncLoc, fData,
                        pName="eRegDef", cName="fpgaEnc")
    setup.createFpgaBits(fpgaEncBitList, cLoc, fEncLoc, fData,
                         pName="fpgaEnc", cName="fpgaEnc",
                         package="FpgaEncBits", xName="FpgaEnc")

    setup.createFpgaReg(fpgaLatheList, cLoc, fLatheLoc, fData,
                        pName="lRegDef", cName="fpgaLathe")
    setup.createFpgaBits(fpgaLatheBitList, cLoc, fLatheLoc, fData,
                         pName="fpgaLathe", cName="fpgaLathe",
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
