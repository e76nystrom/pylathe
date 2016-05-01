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
    ["READDBG", "", "read debug message"]
]
    
# def createCommands(cLoc, fData=False):
#     if fData:
#         cFile = open(cLoc + 'cmdList.h','w')
#         cFile.write("enum COMMANDS\n{\n");
#         # jFile = open(jLoc + 'Cmd.java','w')
#         # jFile.write("package lathe;\n\n");
#         # jFile.write("public enum Cmd\n{\n");
#     global cmds
#     cmds = {}
#     val = 0
#     for i in range(0,len(cmdList)):
#         data = cmdList[i]
#         if not isinstance(data,basestring):
#             if (len(data) != 0):
#                 regName = data[0]
#                 regComment = data[1]
#                 if fData:
#                     tmp = " %s," % (regName)
#                     cFile.write("%s/* 0x%02x %s */\n" % 
#                                 (tmp.ljust(32),val,regComment))
#                     # jFile.write("%s/* 0x%02x %s */\n" % 
#                     #             (tmp.ljust(32),val,regComment))
#                 cmds[regName] = val
#                 val += 1
#         else:
#             if fData:
#                 if (len(data) > 0):
#                     cFile.write("\n// %s\n\n" % (data))
#                     # jFile.write("\n// %s\n\n" % (data))
#                 else:
#                     cFile.write("\n")
#                     # jFile.write("\n")
#     if fData:
#         cFile.write("};\n")
#         cFile.close()
#         # jFile.write("};\n")
#         # jFile.close()

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

    # ["", "", ""],
    # ["", "", ""],
    
    ["MAX_PARM", "maximum parameter", "int16_t"],
]
    
# def createParameters(cLoc, fData=False):
#     if fData:
#         cFile = open(cLoc + 'parmList.h','w')
#         cFile.write("enum PARM\n{\n")
    
#         c1File = open(cLoc + 'remparm.h','w')
#         c1File.write("T_PARM remparm[] =\n{\n")
    
#         c2File = open(cLoc + 'remvardef.h','w')
#         # jFile = open(jLoc + 'Parm.java','w')
#         # jFile.write("package lathe;\n\n");
#         # jFile.write("public enum Parm\n{\n")
#     global parms
#     parms = {}
#     val = 0
#     for i in range(0,len(parmList)):
#         data = parmList[i]
#         if not isinstance(data,basestring):
#             regName = data[0]
#             tmp = regName.split("_")
#             varName = ""
#             first = True
#             for s in tmp:
#                 if first:
#                     varName = s.lower()
#                     first = False
#                 else:
#                     varName = varName + s[0].upper() + s[1:].lower()
#             # varName = regName[3:].lower()
#             regComment = data[1]
#             varType = data[2]
#             if fData:
#                 tmp = "PRM_%s," % (regName)
#                 cFile.write("%s/* 0x%02x %s */\n" % 
#                             (tmp.ljust(32),val,regComment))
#                 tmp = "PARM(%s)," % (varName)
#                 c1File.write("%s/* 0x%02x %s */\n" % 
#                              (tmp.ljust(32),val,regComment))
#                 tmp = "EXT %s %s;" % (varType,varName)
#                 c2File.write("%s/* 0x%02x %s */\n" % 
#                              (tmp.ljust(32),val,regComment))
#                 # tmp = "  %s," % (regName)
#                 # jFile.write("%s/* 0x%02x %s */\n" % 
#                 #             (tmp.ljust(32),val,regComment))
#             parms[regName] = (val, varType)
#             val += 1
#         else:
#             if fData:
#                 cFile.write("\n// %s\n\n" % (data))
#                 c1File.write("\n// %s\n\n" % (data))
#                 c2File.write("\n// %s\n\n" % (data))
#                 # jFile.write("\n// %s\n\n" % (data))
#     if fData:
#         cFile.write("};\n")
#         cFile.close()
#         c1File.write("};\n")
#         c1File.close()
#         c2File.close()
#         # jFile.write("};\n")
#         # jFile.close()
    
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
    ["FEED_METRIC", "2", "feed mm per rev"],
    
    # ["", "", ""],
    
    "turn control bits",
    
    ["TURNSYN", "(1 << 0)", "turn with sync motion"],
    ["TURNADD", "(1 << 1)", "add pass to turn operation"],
    ["TAPERX", "(1 << 1)", "taper x axis"],
    ["TAPERZ", "(1 << 3)", "taper z axis"],
    ["TAPEROUT", "(1 << 4)", "one taper out, zero in"],
    ["THREAD", "(1 << 5)", "threading enabled"],
    ["TINTERNAL", "(1 << 6)", "internal threads"],
    ["TDIAMETER", "(1 << 7)", "diameter mode"],
    
    "debug control bits",
    
    ["DBGPASS", "(1 << 0)", "pause before each pass"],
    ["DBGEND", "(1 << 1)", "pause at end of a pass"],
    ["DBGSEQ", "(1 << 2)", "generate sequence data"]
]
    
# def createControlBits(cLoc, fData=False):
#     if fData:
#         cFile = open(cLoc + 'ctlbits.h','w')
#         # jFile = open(jLoc + 'CtlBits.java','w')
#         # jFile.write("package lathe;\n\n");
#         # jFile.write("public class CtlBits\n{\n");
#     for i in range(0,len(regList)):
#         data = regList[i]
#         if not isinstance(data,basestring):
#             var = data[0]
#             val = data[1]
#             comment = data[2]
#             if fData:
#                 tmp =  "#define %-12s %s" % (var,val)
#                 cFile.write("%s /* %s */\n" % 
#                             (tmp.ljust(32),comment));
#                 # tmp =  " public static final int %-10s = %s;" % (var,val)
#                 # jFile.write("%s /* %s */\n" % 
#                 #             (tmp,comment));
#             globals()[var] = eval(val)
#         else:
#             if fData:
#                 cFile.write("\n// %s\n\n" % (data))
#                 # jFile.write("\n// %s\n\n" % (data))
#     if fData:
#         cFile.close()
#         # jFile.write("};\n")
#         # jFile.close()

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
    
#  "turn control states",
    
#  "enum tStates",
#  "{",
#  ["TIDLE", "idle"],
#  ["TSTART", "Start"],
# # ["TCKRTC", "check for x retracted"],
# # ["TWTRTC0", "wait for x to retract"],
# # ["TCKSTR", "check for at start position"],
# # ["TWSTART", "wait for start position"],
#  ["TFEED", "feed x in"],
#  ["TWTFEED", "wait for x feed to complete"],
#  ["TTURN", "set up turn move"],
#  ["TWTTURN", "perform turn operation"],
#  ["TRTC", "retract x after turn"],
#  ["TWTRTC1", "wait for x retract to complete"],
#  ["TRTN", "return to start position"],
#  ["TWTRTN", "wait for return to start"],
#  ["TWTRTNB", "wait for return backlash "],
#  ["TUPDPASS", "update pass"],
#  ["TUPDSPRING", "update spring pass"],
#  ["TDONE", "clean up state"],
#  "};",
    
#  "facing control states",
    
#  "enum fStates",
#  "{",
#  ["FIDLE", "idle"],
#  ["FCKRTC", "check for z retracted"],
#  ["FWTRTC0", "wait for z to retract"],
#  ["FCKSTR", "check for x at start position"],
#  ["FWSTART", "wait for x start position"],
#  ["FFEED", "feed z in"],
#  ["FWTFEED", "wait for z feed to complete"],
#  ["FFACE", "set up facing move"],
#  ["FWTFACE", "perform facing operation"],
#  ["FRTC", "retract z after facing"],
#  ["FWTRTC1", "wait for z retract to complete"],
#  ["FRTN", "return to start position"],
#  ["FWTRTN", "wait for return to start"],
#  ["FWTRTNB", "wait for return backlash"],
#  ["FUPDPASS", "update pass"],
#  ["FUPDSPRING", "update spring pass"],
#  ["FDONE", "clean up state"],
#  "};",

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
    
# def createStateData(cLoc, fData=False):
#     if fData:
#         cFile = open(cLoc + 'ctlstates.h', 'w')
#         # jFile = open(jLoc + 'CtlStates.java', 'w')
#         # jFile.write("package lathe;\n\n");
#         # jFile.write("public class CtlStates\n{\n");
#     val = 0
#     for i in range(0, len(stateList)):
#         data = stateList[i]
#         if not isinstance(data, basestring):
#             state = data[0]
#             comment = data[1]
#             if fData:
#                 tmp =  " %s," % (state)
#                 cFile.write("%s/* %2d %s */\n" % 
#                             (tmp.ljust(32), val, comment));
#                 # jFile.write('  "%-10s %s", \n' % (state, comment));
#             globals()[state] = val
#             val += 1
#         else:
#             if fData:
#                 if data.startswith("enum"):
#                     tmp = data.split()
#                     cFile.write("%s %s\n" % (tmp[0], tmp[1].upper()))
#                     # tmp =  " public static final String[] %s = \n" % (tmp[1])
#                     # jFile.write(tmp)
#                     val = 0
#                 elif data.startswith("{") or data.startswith("}"):
#                     cFile.write("%s\n" % (data))
#                     # jFile.write(" %s\n" % (data))
#                 else:
#                     cFile.write("\n// %s\n\n" % (data))
#                     # jFile.write("\n // %s\n\n" % (data))
#     if fData:
#         cFile.close()
#         # jFile.write("};\n")
#         # jFile.close()

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
