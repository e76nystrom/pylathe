cmds = None
parms = None
xRegs = None

def createCommands(cmdList, cLoc, fData=False):
    if fData:
        cFile = open(cLoc + 'cmdList.h', 'w')
        cFile.write("enum COMMANDS\n{\n");
        # jFile = open(jLoc + 'Cmd.java', 'w')
        # jFile.write("package lathe;\n\n");
        # jFile.write("public enum Cmd\n{\n");
    global cmds
    cmds = {}
    val = 0
    for i in range(0, len(cmdList)):
        data = cmdList[i]
        if not isinstance(data, basestring):
            if (len(data) != 0):
                (regName, action, regComment) = data
                # if  isinstance(action, basestring):
                if len(action) == 0:
                    action = None
                if fData:
                    tmp = " %s, " % (regName)
                    cFile.write("%s/* 0x%02x %s */\n" % 
                                (tmp.ljust(32), val, regComment))
                    # jFile.write("%s/* 0x%02x %s */\n" % 
                    #             (tmp.ljust(32), val, regComment))
                cmds[regName] = (val, action)
                val += 1
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
    #    print key, cmds[key]

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
    global parms, parmVars
    parms = {}
    val = 0
    for i in range(0, len(parmList)):
        data = parmList[i]
        if not isinstance(data, basestring):
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
                            (tmp.ljust(32), val, regComment))
                # tmp = " PARM(%s, %s), " % (varName, regAct)
                tmp = " PARM(%s), " % (varName)
                c1File.write("%s/* 0x%02x %s */\n" % 
                             (tmp.ljust(32), val, regComment))
                tmp = " EXT %s %s;" % (varType, varName)
                c2File.write("%s/* 0x%02x %s */\n" % 
                             (tmp.ljust(32), val, regComment))
                tmp = "  %s, " % (regName)
                # jFile.write("%s/* 0x%02x %s */\n" % 
                #             (tmp.ljust(32), val, regComment))
            parms[regName] = (val, varType, varName)
            val += 1
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
    #    print key, parms[key]

def createCtlStates(stateList, cLoc, fData=False):
    if fData:
        cFile = open(cLoc + 'ctlstates.h', 'w')
        # jFile = open(jLoc + 'CtlStates.java', 'w')
        # jFile.write("package lathe;\n\n");
        # jFile.write("public class CtlStates\n{\n");
    val = 0
    for i in range(0, len(stateList)):
        data = stateList[i]
        if not isinstance(data, basestring):
            state = data[0]
            comment = data[1]
            if fData:
                tmp =  " %s, " % (state)
                cFile.write("%s/* %2d %s */\n" % 
                            (tmp.ljust(32), val, comment));
                # jFile.write('  "%-10s %s", \n' % (state, comment));
            globals()[state] = val
            print "%8s %2x" % (state, val)
            val += 1
        else:
            if fData:
                if data.startswith("enum"):
                    tmp = data.split()
                    cFile.write("%s %s\n" % (tmp[0], tmp[1].upper()))
                    tmp =  " public static final String[] %s = \n" % (tmp[1])
                    # jFile.write(tmp)
                    val = 0
                elif data.startswith("{") or data.startswith("}"):
                    cFile.write("%s\n" % (data))
                    # jFile.write(" %s\n" % (data))
                else:
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
        if not isinstance(data, basestring):
            (var, val, comment) = data
            if fData:
                tmp =  "#define %-12s %s" % (var, val)
                cFile.write("%s /* %s */\n" % 
                            (tmp.ljust(32), comment));
                tmp =  " public static final int %-10s = %s;" % (var, val)
                # jFile.write("%s /* %s */\n" % 
                #             (tmp, comment));
            globals()[var] = eval(val)
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
        xFile = open(xLoc + 'RegDef.vhd', 'w')
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
    global xRegs
    xRegs = {}
    val = 0
    for i in range(0, len(xilinxList)):
        data = xilinxList[i]
        if not isinstance(data, basestring):
            (regName, regComment) = data
            if fData:
                tmp = " %s, " % (regName)
                cFile.write("%s/* 0x%02x %s */\n" % 
                            (tmp.ljust(32), val, regComment));
                xFile.write(('constant %-12s : unsigned(opb-1 downto 0) ' +
                             ':= x"%02x"; -- %s\n') %
                            (regName, val, regComment))
                # tmp = "  %s, " % (regName)
                # jFile.write("%s/* 0x%02x %s */\n" % 
                #             (tmp.ljust(32), val, regComment));
                # tmp = "  \"%s\", " % (regName)
                # j1File.write("%s/* 0x%02x %s */\n" % 
                #             (tmp.ljust(32), val, regComment));
            xRegs[regName] = val
            val += 1
        else:
            if fData:
                if (len(data) > 0):
                    cFile.write("\n// %s\n\n" % (data))
                    xFile.write("\n-- %s\n\n" % (data))
                    # jFile.write("\n// %s\n\n" % (data))
                else:
                    cFile.write("\n");
                    xFile.write("\n");
                    # jFile.write("\n");
    if fData:
        cFile.write("};\n")
        cFile.close()
        xFile.write("\nend RegDef;\n\n")
        xFile.write("package body RegDef is\n\n")
        xFile.write("end RegDef;\n")
        xFile.close()
        # jFile.write("};\n")
        # jFile.close()
        # j1File.write(" };\n\n};\n")
        # jFile.close()

    # for key in xRegs:
    #     print "%-12s %02x" % (key, xRegs[key])

def createXilinxBits(xilinxBitList, cLoc, xLoc, fData=False):
    if fData:
        cFile = open(cLoc + 'xilinxbits.h', 'w')
        xFile = open(xLoc + 'CtlBits.vhd', 'w')
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
        if not isinstance(data, basestring):
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
                    cFile.write("%s/* %s */\n" % 
                                (tmp.ljust(32), comment));
                    if bit != 0:
                        if (shift != lastShift):
                            tmp =  "  \"%s\", " % (cVar)
                            bitStr.append("%s/* 0x%02x %s */\n"
                                          % (tmp.ljust(32), bit << shift, comment))
                        xLst.append((" alias %-10s : std_logic is %sreg(%d); " +
                                     "-- x%02x %s\n") %
                                    (xVar, regName, shift, 1 << shift, comment))
                        if (shift > maxShift):
                            maxShift = shift
                    # tmp =  (" public static final int %-10s = (%s << %s);" %
                    #         (cVar, bit, shift))
                    # jFile.write("%s /* %s */\n" % 
                    #             (tmp, comment));
                globals()[cVar] = bit << shift
                lastShift = shift
        else:
            if fData:
                if (len(regName) > 0):
                    xFile.write(" constant %s_size : integer := %d;\n" %
                                (regName, maxShift + 1))
                    xFile.write(" signal %sReg : unsigned(%s_size-1 downto 0);\n" %
                                (regName, regName))
                    for i in range(0, len(xLst)):
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
                    xFile.write("\n-- %s\n\n" % (data))
                    # jFile.write("\n// %s\n\n" % (data))
    if fData:
        cFile.close()
        xFile.write("\nend CtlBits;\n\n")
        xFile.write("package body CtlBits is\n\n")
        xFile.write("end CtlBits;\n")
        xFile.close()
        # jFile.write("};\n")
        # jFile.close()
