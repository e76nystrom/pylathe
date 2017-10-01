from sys import stdout

class Setup():
    def __init__(self):
        self.importList = []
        self.file = None

    def open(self, fileName):
        self.file = open(fileName, "w")

    def createConfig(self, configList):
        global config, configTable
        config = {}
        configTable = []
        imports = []
        imports.append("config")
        imports.append("configTable")
        f = self.file
        if not self.f is None:
            f.write("# configtable\n\n")
        for i, (name, comment) in enumerate(configList):
            config[name] = i
            if name in globals():
                print("createConfig %s already defined" % name)
            else:
                globals()[name] = i
                imports.append(name)
                configTable.append(name)
                if not f is None:
                    tmp = "%s = %2d" % (name, i)
                    f.write("%s # %s\n" % (tmp.ljust(32), comment))
        self.configImports = imports
        self.importList += imports
        self.config = config
        self.confgTable = configTable
        return(config, configTable)

    def createStrings(self, strList):
        global strTable
        strTable = []
        imports = []
        imports.append("strTable")
        for i, (name, value) in enumerate(strList):
            config[name] = i
            if name in globals():
                print("createConfig %s already defined" % name)
            else:
                globals()[name] = i
                imports.append(name)
                strTable.append(value)
        self.strImports = imports
        self.importList += imports
        self.strTable = strTable
        return(strTable)

    def createCommands(self, cmdList, cLoc, fData=False):
        global cmdTable
        imports = []
        imports.append("cmdTable")
        cmdTable = []
        if fData:
            cFile = open(cLoc + 'cmdList.h', 'wb')
            cFile.write("enum COMMANDS\n{\n");
            # jFile = open(jLoc + 'Cmd.java', 'wb')
            # jFile.write("package lathe;\n\n");
            # jFile.write("public enum Cmd\n{\n");
        index = 0
        for i in range(len(cmdList)):
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
                    cmdTable.append((regName, action))
                    if regName in globals():
                        print("createCommands %s already defined" % regName)
                    else:
                        globals()[regName] = index
                        imports.append(regName)
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
        self.cmdImports = imports
        self.importList += imports
        self.cmdTable = cmdTable
        return(cmdTable)

    def createParameters(self, parmList, cLoc, fData=False):
        global parmTable
        parmTable = []
        imports = []
        imports.append("parmTable")
        if fData:
            cFile = open(cLoc + 'parmList.h', 'wb')
            cFile.write("enum PARM\n{\n")
            c1File = open(cLoc + 'remparm.h', 'wb')
            c1File.write("T_PARM remparm[] =\n{\n")
            c2File = open(cLoc + 'remvardef.h', 'wb')
            # jFile = open(jLoc + 'Parm.java', 'wb')
            # jFile.write("package lathe;\n\n");
            # jFile.write("public enum Parm\n{\n")
        index = 0
        for i in range(len(parmList)):
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
                parmTable.append((regName, varType, varName))
                if regName in globals():
                    print("createParameters %s already defined" % regName)
                else:
                    globals()[regName] = index
                    imports.append(regName)
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
        self.parmImports = imports
        self.importList += imports
        self.parmTable = parmTable
        return(parmTable)

    def createEnums(self, enumList, cLoc, fData=False):
        imports = []
        if fData:
            cFile = open(cLoc + 'ctlstates.h', 'wb')
            # jFile = open(jLoc + 'CtlStates.java', 'wb')
            # jFile.write("package lathe;\n\n");
            # jFile.write("public class CtlStates\n{\n");
        val = 0
        for i in range(len(enumList)):
            data = enumList[i]
            # if not isinstance(data, basestring):
            if not isinstance(data, str):
                state = data[0]
                comment = data[1]
                if fData:
                    tmp =  " %s, " % (state)
                    cFile.write("%s/* %2d x%02x %s */\n" % \
                                (tmp.ljust(32), val, val, comment));
                    # jFile.write('  "%-10s %s", \n' % (state, comment));
                if state in globals():
                    print("createCtlStates %s already defined" % state)
                else:
                    globals()[state] = val
                    imports.append(state)
                    eval("%s.append('%s')" % (enum, state))
                    stringList.append((state, comment))
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
                    imports.append(enum)
                    val = 0
                    stringList = []
                    if fData:
                        cFile.write("enum %s\n" % (var.upper()))
                        # tmp =  " public static final String[] %s = \n" % (var])
                        # jFile.write(tmp)
                elif data.startswith("{") or data.startswith("}"):
                    if fData:
                        cFile.write("%s\n" % (data))
                        if data.startswith("}"):
                            cFile.write("\n#ifdef ENUM_%s\n\n" % (var.upper()))
                            cFile.write("char *%s[] = \n{\n" % (enum))
                            for index, (s, comment) in enumerate(stringList):
                                tmp =  " \"%s\", " % (s)
                                cFile.write("%s/* %2d x%02x %s */\n" % \
                                            (tmp.ljust(32), index, \
                                             index, comment))
                            cFile.write("};\n\n#endif\n")
                        # jFile.write(" %s\n" % (data))
                else:
                    if fData:
                        cFile.write("\n// %s\n\n" % (data))
                        # jFile.write("\n // %s\n\n" % (data))
        if fData:
            cFile.close()
            # jFile.write("};\n")
            # jFile.close()
        self.enumImports = imports
        self.importList += imports

    def createCtlBits(self, regList, cLoc, fData=False):
        imports = []
        if fData:
            cFile = open(cLoc + 'ctlbits.h', 'wb')
            # jFile = open(jLoc + 'CtlBits.java', 'wb')
            # jFile.write("package lathe;\n\n");
            # jFile.write("public class CtlBits\n{\n");
        for i in range(len(regList)):
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
                    imports.append(var)
            else:
                if fData:
                    cFile.write("\n// %s\n\n" % (data))
                    # jFile.write("\n// %s\n\n" % (data))
        if fData:
            cFile.close()
            # jFile.write("};\n")
            # jFile.close()
        self.enumImports = imports
        self.importList += imports

    def createXilinxReg(self, xilinxList, cLoc, xLoc, fData=False):
        global xRegTable
        xRegTable = []
        imports = []
        imports.append("xRegTable")
        if fData:
            cFile = open(cLoc + 'xilinxreg.h', 'wb')
            cFile.write("enum XILINX\n{\n");
            try:
                xFile = open(xLoc + 'RegDef.vhd', 'wb')
            except (OSError, IOError) as e:
                xFile = None
            if xFile:
                xFile.write("library IEEE;\n")
                xFile.write("use IEEE.STD_LOGIC_1164.all;\n")
                xFile.write("use IEEE.NUMERIC_STD.ALL;\n\n")
                xFile.write("package RegDef is\n\n")
                xFile.write("constant opb : positive := 8;\n\n")
            # jFile = open(jLoc + 'Xilinx.java', 'wb')
            # jFile.write("package lathe;\n\n");
            # jFile.write("public enum Xilinx\n {\n");
            # j1File = open(jLoc + 'XilinxStr.java', 'wb')
            # j1File.write("package lathe;\n\n");
            # j1File.write("public class XilinxStr\n{\n");
            # j1File.write(" public static final String[] xilinxStr =\n {\n");
        index = 0
        for i in range(len(xilinxList)):
            data = xilinxList[i]
            # if not isinstance(data, basestring):
            if not isinstance(data, str):
                (regName, regComment) = data
                if fData:
                    tmp = " %s, " % (regName)
                    cFile.write("%s/* 0x%02x %s */\n" % 
                                (tmp.ljust(32), index, regComment));
                    if xFile:
                        xFile.write(('constant %-12s : ' \
                                     'unsigned(opb-1 downto 0) ' \
                                     ':= x"%02x"; -- %s\n') %
                                    (regName, index, regComment))
                    # tmp = "  %s, " % (regName)
                    # jFile.write("%s/* 0x%02x %s */\n" % 
                    #             (tmp.ljust(32), index, regComment));
                    # tmp = "  \"%s\", " % (regName)
                    # j1File.write("%s/* 0x%02x %s */\n" % 
                    #             (tmp.ljust(32), index, regComment));
                globals()[regName] = index
                imports.append(regName)
                xRegTable.append(regName)
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
        self.xRegImports = imports
        self.importList += imports
        self.xRegTable = xRegTable
        return(xRegTable)

    def createXilinxBits(self, xilinxBitList, cLoc, xLoc, fData=False):
        imports = []
        if fData:
            cFile = open(cLoc + 'xilinxbits.h', 'wb')
            try:
                xFile = open(xLoc + 'CtlBits.vhd', 'wb')
            except IOError as e:
                xFile = None
            if xFile:
                xFile.write("library IEEE;\n")
                xFile.write("use IEEE.STD_LOGIC_1164.all;\n")
                xFile.write("use IEEE.NUMERIC_STD.ALL;\n\n")
                xFile.write("package CtlBits is\n")
            # jFile = open(jLoc + 'XilinxBits.java', 'wb')
            # jFile.write("package lathe;\n\n");
            # jFile.write("public class XilinxBits\n{\n");
        regName = ""
        bitStr = []
        lastShift = -1
        for i in range(len(xilinxBitList)):
            data = xilinxBitList[i]
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
                            xLst.append((" alias %-10s : " \
                                         "std_logic is %sreg(%d); " \
                                         "-- x%02x %s\n") %
                                        (xVar, regName, shift, \
                                         1 << shift, comment))
                        # tmp =  (" public static final int %-10s = " \
                        #         "(%s << %s);" % (cVar, bit, shift))
                        # jFile.write("%s /* %s */\n" % 
                        #             (tmp, comment));
                    if (shift > maxShift):
                        maxShift = shift
                    if cVar in globals():
                        print("createXilinxBits %s already defined" % cVar)
                    else:
                        globals()[cVar] = bit << shift
                        imports.append(cVar)
                    lastShift = shift
            else:
                if fData:
                    if (len(regName) > 0):
                        var = "%s_size" % (regName)
                        tmp =  "#define %-12s %d" % (var, maxShift + 1)
                        cFile.write("%s\n" % (tmp))
                        if xFile:
                            xFile.write(" constant %s_size : " \
                                        "integer := %d;\n" % \
                                        (regName, maxShift + 1))
                            xFile.write(" signal %sReg : "\
                                        "unsigned(%s_size-1 downto 0);\n" %
                                        (regName, regName))
                        for i in range(len(xLst)):
                            if xFile:
                                xFile.write(xLst[i])
                        # if (len(bitStr) != 0):
                        #     jFile.write(("\n public static final " +
                        #                 "String[] %sBits =\n {\n") % (regName))
                        #     for i in range(len(bitStr)):
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
                            imports.append(var)
        if fData:
            cFile.close()
            if xFile:
                xFile.write("\nend CtlBits;\n\n")
                xFile.write("package body CtlBits is\n\n")
                xFile.write("end CtlBits;\n")
                xFile.close()
                # jFile.write("};\n")
                # jFile.close()
        self.xBitImports = imports
        self.importList += imports
