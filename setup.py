from sys import stdout
# cmds = None
# parms = None
# xRegs = None

importList = []

def createConfig(configList):
    global config, configTable
    config = {}
    configTable = []
    for i, (name, comment) in enumerate(configList):
        config[name] = i
        if name in globals():
            print("createConfig %s already defined" % name)
        else:
            globals()[name] = i
            configTable.append(name)
            importList.append(name)
    return(config, configTable)

def createCommands(cmdList, cLoc, fData=False):
    if fData:
        cFile = open(cLoc + 'cmdList.h', 'w')
        cFile.write("enum COMMANDS\n{\n");
        # jFile = open(jLoc + 'Cmd.java', 'w')
        # jFile.write("package lathe;\n\n");
        # jFile.write("public enum Cmd\n{\n");
    global cmdTable
    # cmds = {}
    cmdTable = []
    index = 0
    for i in range(0, len(cmdList)):
        data = cmdList[i]
        # if not isinstance(data, basestring):
        if not isinstance(data, str):
            if (len(data) != 0):
                (regName, action, regComment) = data
                # if  isinstance(action, basestring):
                if len(action) == 0:
                    action = None
                if fData:
                    tmp = " %s, " % (regName)
                    cFile.write("%s/* 0x%02x %s */\n" % 
                                (tmp.ljust(32), index, regComment))
                    # jFile.write("%s/* 0x%02x %s */\n" % 
                    #             (tmp.ljust(32), index, regComment))
                # cmds[regName] = (index, action)
                cmdTable.append((regName, action))
                if regName in globals():
                    print("createCommands %s already defined" % regName)
                else:
                    # globals()[regName] = regName
                    globals()[regName] = index
                    importList.append(regName)
                index += 1
        else:
            if fData:
                if (len(data) > 0):
                    cFile.write("\n// %s\n\n" % (data))
                    # jFile.write("\n// %s\n\n" % (data))
                else:
                    cFile.write("\n")
                    # jFile.write("\n")
    if fData:
        cFile.write("};\n")
        cFile.close()
        # jFile.write("};\n")
        # jFile.close()
        # for key in cmds:
        #    print(key, cmds[key])

def createParameters(parmList, cLoc, fData=False):
    if fData:
        cFile = open(cLoc + 'parmList.h', 'w')
        cFile.write("enum PARM\n{\n")
        c1File = open(cLoc + 'remparm.h', 'w')
        c1File.write("T_PARM remparm[] =\n{\n")
        c2File = open(cLoc + 'remvardef.h', 'w')
        # jFile = open(jLoc + 'Parm.java', 'w')
        # jFile.write("package lathe;\n\n");
        # jFile.write("public enum Parm\n{\n")
    global parmTable, parmVars
    # parms = {}
    parmTable = []
    index = 0
    for i in range(0, len(parmList)):
        data = parmList[i]
        # if not isinstance(data, basestring):
        if not isinstance(data, str):
            (regName, regComment, varType) = data
            tmp = regName.split("_")
            if len(tmp) > 1:
                varName = ""
                first = True
                for s in tmp:
                    if first:
                        varName = s.lower()
                        first = False
                    else:
                        varName = varName + s[0].upper() + s[1:].lower()
            else:
                if regName.startswith('PRM'):
                    varName = regName[3:].lower()
                else:
                    varName = regName.lower()
            regAct = '0';
            if (len(data) >= 4):
                regAct = data[3]
            if fData:
                tmp = " %s, " % (regName)
                cFile.write("%s/* 0x%02x %s */\n" % 
                            (tmp.ljust(32), index, regComment))
                # tmp = " PARM(%s, %s), " % (varName, regAct)
                tmp = " PARM(%s), " % (varName)
                c1File.write("%s/* 0x%02x %s */\n" % 
                             (tmp.ljust(32), index, regComment))
                tmp = " EXT %s %s;" % (varType, varName)
                c2File.write("%s/* 0x%02x %s */\n" % 
                             (tmp.ljust(32), index, regComment))
                tmp = "  %s, " % (regName)
                # jFile.write("%s/* 0x%02x %s */\n" % 
                #             (tmp.ljust(32), index, regComment))
            # parms[regName] = (index, varType, varName)
            parmTable.append((regName, varType, varName))
            if regName in globals():
                print("createParameters %s already defined" % regName)
            else:
                # globals()[regName] = regName
                globals()[regName] = index
                importList.append(regName)
            index += 1
        else:
            if fData:
                cFile.write("\n// %s\n\n" % (data))
                c1File.write("\n// %s\n\n" % (data))
                c2File.write("\n// %s\n\n" % (data))
                # jFile.write("\n// %s\n\n" % (data))
    if fData:
        cFile.write("};\n")
        cFile.close()
        c1File.write("};\n")
        c1File.close()
        c2File.close()
        # jFile.write("};\n")
        # jFile.close()

    #for key in parms:
    #    print(key, parms[key])

def createCtlStates(stateList, cLoc, fData=False):
    if fData:
        cFile = open(cLoc + 'ctlstates.h', 'w')
        # jFile = open(jLoc + 'CtlStates.java', 'w')
        # jFile.write("package lathe;\n\n");
        # jFile.write("public class CtlStates\n{\n");
    val = 0
    for i in range(0, len(stateList)):
        data = stateList[i]
        # if not isinstance(data, basestring):
        if not isinstance(data, str):
            state = data[0]
            comment = data[1]
            if fData:
                tmp =  " %s, " % (state)
                cFile.write("%s/* %2d %s */\n" % 
                            (tmp.ljust(32), val, comment));
                # jFile.write('  "%-10s %s", \n' % (state, comment));
            if state in globals():
                print("createCtlStates %s already defined" % state)
            else:
                globals()[state] = val
                eval("%s.append('%s')" % (enum, state))
                importList.append(state)
            val += 1
        else:
            if data.startswith("enum"):
                tmp = data.split()
                if len(tmp) != 2:
                    print("enum failure")
                    stdout.flush()
                var = tmp[1]
                enum = tmp[1].replace('_', "") + "List"
                globals()[enum] = []
                importList.append(enum)
                if fData:
                    cFile.write("enum %s\n" % (var.upper()))
                    # tmp =  " public static final String[] %s = \n" % (var])
                    # jFile.write(tmp)
                    val = 0
            elif data.startswith("{") or data.startswith("}"):
                if fData:
                    cFile.write("%s\n" % (data))
                    # jFile.write(" %s\n" % (data))
            else:
                if fData:
                    cFile.write("\n// %s\n\n" % (data))
                    # jFile.write("\n // %s\n\n" % (data))
    if fData:
        cFile.close()
        # jFile.write("};\n")
        # jFile.close()

def createCtlBits(regList, cLoc, fData=False):
    if fData:
        cFile = open(cLoc + 'ctlbits.h', 'w')
        # jFile = open(jLoc + 'CtlBits.java', 'w')
        # jFile.write("package lathe;\n\n");
        # jFile.write("public class CtlBits\n{\n");
    for i in range(0, len(regList)):
        data = regList[i]
        # if not isinstance(data, basestring):
        if not isinstance(data, str):
            (var, val, comment) = data
            if fData:
                tmp =  "#define %-12s %s" % (var, val)
                bitVal = eval(val)
                cFile.write("%s /* 0x%02x %s */\n" % 
                            (tmp.ljust(32), bitVal, comment));
                tmp =  " public static final int %-10s = %s;" % (var, val)
                # jFile.write("%s /* %s */\n" % 
                #             (tmp, comment));
            if var in globals():
                print("createctlBits %s already defined" % var)
            else:
                globals()[var] = eval(val)
                importList.append(var)
        else:
            if fData:
                cFile.write("\n// %s\n\n" % (data))
                # jFile.write("\n// %s\n\n" % (data))
    if fData:
        cFile.close()
        # jFile.write("};\n")
        # jFile.close()

def createXilinxReg(xilinxList, cLoc, xLoc, fData=False):
    if fData:
        cFile = open(cLoc + 'xilinxreg.h', 'w')
        cFile.write("enum XILINX\n{\n");
        try:
            xFile = open(xLoc + 'RegDef.vhd', 'w')
        except (OSError, IOError) as e:
            xFile = None
        if xFile:
            xFile.write("library IEEE;\n")
            xFile.write("use IEEE.STD_LOGIC_1164.all;\n")
            xFile.write("use IEEE.NUMERIC_STD.ALL;\n\n")
            xFile.write("package RegDef is\n\n")
            xFile.write("constant opb : positive := 8;\n\n")
        # jFile = open(jLoc + 'Xilinx.java', 'w')
        # jFile.write("package lathe;\n\n");
        # jFile.write("public enum Xilinx\n {\n");
        # j1File = open(jLoc + 'XilinxStr.java', 'w')
        # j1File.write("package lathe;\n\n");
        # j1File.write("public class XilinxStr\n{\n");
        # j1File.write(" public static final String[] xilinxStr =\n {\n");
    # global xRegs
    global xRegTable
    # xRegs = {}
    xRegTable = []
    index = 0
    for i in range(0, len(xilinxList)):
        data = xilinxList[i]
        # if not isinstance(data, basestring):
        if not isinstance(data, str):
            (regName, regComment) = data
            if fData:
                tmp = " %s, " % (regName)
                cFile.write("%s/* 0x%02x %s */\n" % 
                            (tmp.ljust(32), index, regComment));
                if xFile:
                    xFile.write(('constant %-12s : unsigned(opb-1 downto 0) ' +
                                 ':= x"%02x"; -- %s\n') %
                                (regName, index, regComment))
                # tmp = "  %s, " % (regName)
                # jFile.write("%s/* 0x%02x %s */\n" % 
                #             (tmp.ljust(32), index, regComment));
                # tmp = "  \"%s\", " % (regName)
                # j1File.write("%s/* 0x%02x %s */\n" % 
                #             (tmp.ljust(32), index, regComment));
            # xRegs[regName] = index
            globals()[regName] = index
            xRegTable.append(regName)
            importList.append(regName)
            index += 1
        else:
            if fData:
                if (len(data) > 0):
                    cFile.write("\n// %s\n\n" % (data))
                    if xFile:
                        xFile.write("\n-- %s\n\n" % (data))
                    # jFile.write("\n// %s\n\n" % (data))
                else:
                    cFile.write("\n");
                    if xFile:
                        xFile.write("\n");
                    # jFile.write("\n");
    if fData:
        cFile.write("};\n")
        cFile.close()
        if xFile:
            xFile.write("\nend RegDef;\n\n")
            xFile.write("package body RegDef is\n\n")
            xFile.write("end RegDef;\n")
            xFile.close()
        # jFile.write("};\n")
        # jFile.close()
        # j1File.write(" };\n\n};\n")
        # jFile.close()

    # for key in xRegs:
    #     print("%-12s %02x" % (key, xRegs[key]))

def createXilinxBits(xilinxBitList, cLoc, xLoc, fData=False):
    if fData:
        cFile = open(cLoc + 'xilinxbits.h', 'w')
        try:
            xFile = open(xLoc + 'CtlBits.vhd', 'w')
        except IOError as e:
            xFile = None
        if xFile:
            xFile.write("library IEEE;\n")
            xFile.write("use IEEE.STD_LOGIC_1164.all;\n")
            xFile.write("use IEEE.NUMERIC_STD.ALL;\n\n")
            xFile.write("package CtlBits is\n")
        # jFile = open(jLoc + 'XilinxBits.java', 'w')
        # jFile.write("package lathe;\n\n");
        # jFile.write("public class XilinxBits\n{\n");
    regName = ""
    bitStr = []
    lastShift = -1
    for i in range(0, len(xilinxBitList)):
        data = xilinxBitList[i]
        # if not isinstance(data, basestring):
        if not isinstance(data, str):
            if len(data) == 1:
                xLst = []
                regName = data[0]
                maxShift = 0
            else:
                (var, bit, shift, comment) = data
                cVar = var.upper()
                xVar = var.replace("_", "")

                if fData:
                    tmp =  "#define %-12s  (%s << %s)" % (cVar, bit, shift)
                    cFile.write("%s/* 0x%03x %s */\n" % 
                                (tmp.ljust(32), bit << shift, comment));
                    if bit != 0:
                        if (shift != lastShift):
                            tmp =  "  \"%s\", " % (cVar)
                            bitStr.append("%s/* 0x%02x %s */\n" % 
                                          (tmp.ljust(32), bit << shift,
                                           comment))
                        xLst.append((" alias %-10s : std_logic is %sreg(%d); " +
                                     "-- x%02x %s\n") %
                                    (xVar, regName, shift, 1 << shift, comment))
                    # tmp =  (" public static final int %-10s = (%s << %s);" %
                    #         (cVar, bit, shift))
                    # jFile.write("%s /* %s */\n" % 
                    #             (tmp, comment));
                if (shift > maxShift):
                    maxShift = shift
                if cVar in globals():
                    print("createXilinxBits %s already defined" % cVar)
                else:
                    globals()[cVar] = bit << shift
                    importList.append(cVar)
                lastShift = shift
        else:
            if fData:
                if (len(regName) > 0):
                    var = "%s_size" % (regName)
                    tmp =  "#define %-12s %d" % (var, maxShift + 1)
                    cFile.write("%s\n" % (tmp))
                    if xFile:
                        xFile.write(" constant %s_size : integer := %d;\n" %
                                    (regName, maxShift + 1))
                        xFile.write(" signal %sReg : "\
                                    "unsigned(%s_size-1 downto 0);\n" %
                                    (regName, regName))
                    for i in range(0, len(xLst)):
                        if xFile:
                            xFile.write(xLst[i])
                    # if (len(bitStr) != 0):
                    #     jFile.write(("\n public static final " +
                    #                 "String[] %sBits =\n {\n") % (regName))
                    #     for i in range(0, len(bitStr)):
                    #         jFile.write(bitStr[i])
                    #     jFile.write(" };\n");
                    #     bitStr = []
                if (len(data) != 0):
                    cFile.write("\n// %s\n\n" % (data))
                    if xFile:
                        xFile.write("\n-- %s\n\n" % (data))
                    # jFile.write("\n// %s\n\n" % (data))
            else:
                if (len(regName) > 0):
                    var = "%s_size" % (regName)
                    if var in globals():
                        print("createXilinxBits %s already defined" % var)
                    else:
                        globals()[var] = maxShift + 1
                        importList.append(var)
    if fData:
        cFile.close()
        if xFile:
            xFile.write("\nend CtlBits;\n\n")
            xFile.write("package body CtlBits is\n\n")
            xFile.write("end CtlBits;\n")
            xFile.close()
            # jFile.write("};\n")
            # jFile.close()
