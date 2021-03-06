import os
from sys import stdout
################################################################################

configTable = None
config = None
strTable = None
cmdTable = None
parmTable = None
enum = None
stringList = None
xRegTable = None

def fWrite(f, txt):
    f.write(txt.encode())
    
class Setup():
    def __init__(self):
        self.importList = []
        self.file = False

    def listImports(self, file, importList):
        line = "from %s import " % (file)
        for i in importList:
            if len(line) + len(i) > 72:
                print(line + "\\")
                line = "    %s, " % (i)
            else:
                line += i + ", "
        if line.endswith(", "):
            print(line[:-2])

    def createConfig(self, configList):
        global config, configTable
        config = {}
        configTable = []
        imports = []
        imports.append("config")
        imports.append("configTable")
        f = None
        if self.file:
            file = 'configDef'
            f = open(file + '.py', 'wb')
            fWrite(f, "# config table\n")
        index = 0
        for data in configList:
            if len(data) == 2:
                (name, comment) = data
                config[name] = index
                if name in globals():
                    print("createConfig %s already defined" % name)
                else:
                    globals()[name] = index
                    imports.append(name)
                    configTable.append(name)
                    if f is not None:
                        tmp = "%s = %3d" % (name.ljust(16), index)
                        fWrite(f, "%s# %s\n" % (tmp.ljust(32), comment))
                index += 1
            else:
                if f is not None:
                    fWrite(f, "\n# %s\n\n" % (data))
        if f is not None:
            fWrite(f, "\nconfig = { \\\n")
            for key in config:
                fWrite(f, "    '%s' : %d,\n" % (key, config[key]))
            fWrite(f, "    }\n")
            fWrite(f, "\nconfigTable = ( \\\n")
            for val in configTable:
                fWrite(f, "    '%s',\n" % (val))
            fWrite(f, "    )\n")
            # self.listImports(file, imports)
            f.close()
        self.importList += imports
        self.configImports = imports
        self.config = config
        self.confgTable = configTable
        return(config, configTable)

    def createStrings(self, strList):
        global strTable
        strTable = []
        imports = []
        imports.append("strTable")
        f = None
        if self.file:
            file = 'stringDef'
            f = open(file + '.py', 'wb')
            fWrite(f, "\n# string table\n\n")
        for i, (name, value) in enumerate(strList):
            config[name] = i
            if name in globals():
                print("createConfig %s already defined" % name)
            else:
                globals()[name] = i
                imports.append(name)
                strTable.append(value)
                if f is not None:
                    tmp = "%s = %2d" % (name.ljust(20), i)
                    fWrite(f, "%s# %s\n" % (tmp.ljust(32), value))
        if f is not None:
            fWrite(f, "\nstrTable = ( \\\n")
            for s in strTable:
                fWrite(f, "    \"%s\", \\\n" % (s))
            fWrite(f, "    )\n")
            # self.listImports(file, imports)
            f.close()
        self.strImports = imports
        self.importList += imports
        self.strTable = strTable
        return(strTable)

    def createCommands(self, cmdList, cLoc, fData=False, file='cmdDef'):
        global cmdTable
        imports = []
        imports.append("cmdTable")
        cmdTable = []
        if fData:
            cFile = open(cLoc + 'cmdList.h', 'wb')
            fWrite(cFile, "enum COMMANDS\n{\n");
            # jFile = open(jLoc + 'Cmd.java', 'wb')
            # fWrite(jFile, "package lathe;\n\n");
            # fWrite(jFile, "public enum Cmd\n{\n");
        f = None
        if self.file:
            f = open(file + '.py', 'wb')
            fWrite(f, "\n# commands\n")
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
                        fWrite(cFile, "%s/* 0x%02x %s */\n" % 
                                    (tmp.ljust(32), index, regComment))
                        # fWrite(jFile, "%s/* 0x%02x %s */\n" % 
                        #             (tmp.ljust(32), index, regComment))
                    cmdTable.append((regName, action))
                    if regName in globals():
                        print("createCommands %s already defined" % regName)
                    else:
                        globals()[regName] = index
                        imports.append(regName)
                        if f is not None:
                            fWrite(f, "%s = %3d\n" % (regName.ljust(20), index))
                    index += 1
            else:
                if fData:
                    if (len(data) > 0):
                        fWrite(cFile, "\n// %s\n\n" % (data))
                        # fWrite(jFile, "\n// %s\n\n" % (data))
                    else:
                        fWrite(cFile, "\n")
                        # fWrite(jFile, "\n")
                if f is not None:
                    fWrite(f, "\n# %s\n\n" % (data))
        if f is not None:
            fWrite(f, "\n# command table\n\n")
            fWrite(f, "cmdTable = ( \\\n")
            for index, (regName, action) in enumerate(cmdTable):
                if action is not None:
                    tmp = "    (\"%s\", \"%s\")," % (regName, action)
                else:
                    tmp = "    (\"%s\", %s)," % (regName, action)
                fWrite(f, "%s# %3d\n" % (tmp.ljust(40), index))
            fWrite(f, "    )\n")
            # self.listImports(file, imports)
            f.close()
        if fData:
            fWrite(cFile, "};\n")
            cFile.close()
            # fWrite(jFile, "};\n")
            # jFile.close()
            # for key in cmds:
            #    print(key, cmds[key])
        self.cmdImports = imports
        self.importList += imports
        self.cmdTable = cmdTable
        return(cmdTable)

    def createParameters(self, parmList, cLoc, fData=False, file='parmDef'):
        global parmTable
        parmTable = []
        imports = []
        imports.append("parmTable")
        if fData:
            cFile = open(cLoc + 'parmList.h', 'wb')
            fWrite(cFile, "enum PARM\n{\n")
            c1File = open(cLoc + 'remparm.h', 'wb')
            fWrite(c1File, "T_PARM remparm[] =\n{\n")
            c2File = open(cLoc + 'remvardef.h', 'wb')
            c3File = open(cLoc + 'remstruct.h', 'wb')
            fWrite(c3File, "#if !defined(REM_STRUCT)\n"\
                   "#define REM_STRUCT\n\n"\
                   "#include <stdint.h>\n\n"\
                   "typedef union uDataUnion\n{\n"\
                   " float t_float;\n"\
                   " int t_int;\n"\
                   " unsigned int t_unsigned_int;\n"\
                   " int32_t t_int32_t;\n"\
                   " int16_t t_int16_t;\n"\
                   " uint16_t t_uint16_t;\n"\
                   " char t_char;\n"\
                   "} T_DATA_UNION, *P_DATA_UNION;\n\n"\
                   "void setRemVar(int parm, T_DATA_UNION val);\n"\
                   "void getRemVar(int parm, P_DATA_UNION val);\n\n"\
                   "typedef struct sRemVar\n{\n")
            try:
                remFunc = []
                c4File = open(cLoc + '../lathe_src/remfunc.cpp', 'wb')
                fWrite(c4File,
                       "#include <stdint.h>\n"\
                       "#define NO_REM_MACROS\n"\
                       "#include \"parmList.h\"\n\n"\
                       "#include \"remstruct.h\"\n\n"\
                       "T_REM_VAR rVar;\n\n")
                fWrite(c4File,
                       "void setRemVar(int parm, T_DATA_UNION val);\n"\
                       "void getRemVar(int parm, P_DATA_UNION val);\n\n")
                fWrite(c4File,
                       "void setRemVar(int parm, T_DATA_UNION val)\n{\n"\
                       " switch(parm)\n {\n")
            except FileNotFoundError:
                c4File = None
            # jFile = open(jLoc + 'Parm.java', 'wb')
            # fWrite(jFile, "package lathe;\n\n");
            # fWrite(jFile, "public enum Parm\n{\n")
        f = None
        if self.file:
            f = open(file + '.py', 'wb')
            fWrite(f, "\n# parameters\n")
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
                    fWrite(cFile, "%s/* 0x%02x %s */\n" % 
                                (tmp.ljust(32), index, regComment))
                    # tmp = " PARM(%s, %s), " % (varName, regAct)
                    tmp = " PARM(%s), " % (varName)
                    fWrite(c1File, "%s/* 0x%02x %s */\n" % 
                                 (tmp.ljust(32), index, regComment))
                    tmp = " EXT %s %s;" % (varType, varName)
                    fWrite(c2File, "%s/* 0x%02x %s */\n" % 
                           (tmp.ljust(32), index, regComment))
                    tmp = " %s %s;" % (varType, varName)
                    fWrite(c3File, "%s/* 0x%02x %s */\n" % 
                                 (tmp.ljust(32), index, regComment))
                    if c4File is not None:
                        tmp = "case %s:" % (regName)
                        tmpType = varType.replace(' ', '_')
                        fWrite(c4File,
                               " %s/* %2d 0x%02x %s */\n"\
                               "  rVar.%s = val.t_%s;\n"\
                               "  break;\n\n" % (tmp.ljust(32), index, index, \
                                                 regComment, varName, tmpType))
                        remFunc.append((regName, index, regComment, \
                                        varName, tmpType))
                    tmp = "  %s, " % (regName)
                    # fWrite(jFile, "%s/* 0x%02x %s */\n" % 
                    #             (tmp.ljust(32), index, regComment))
                parmTable.append((regName, varType, varName))
                if regName in imports:
                    print("createParameters %s already defined" % regName)
                else:
                    # globals()[regName] = index
                    imports.append(regName)
                    if f is not None:
                        fWrite(f, "%s = %3d\n" % (regName.ljust(20), index))
                index += 1
            else:
                if fData:
                    fWrite(cFile, "\n// %s\n\n" % (data))
                    fWrite(c1File, "\n// %s\n\n" % (data))
                    fWrite(c2File, "\n// %s\n\n" % (data))
                    fWrite(c3File, "\n// %s\n\n" % (data))
                    if c4File is not None:
                        remFunc.append(data)
                    # fWrite(jFile, "\n// %s\n\n" % (data))
                if f is not None:
                    fWrite(f, "\n# %s\n\n" % (data))
        if f is not None:
            fWrite(f, "\nparmTable = ( \\\n")
            for val in parmTable:
                fWrite(f, "    ('%s', '%s', '%s'),\n" % (val))
            fWrite(f, "    )\n")
            # self.listImports(file, imports)
            f.close()
        if fData:
            fWrite(cFile, "};\n")
            cFile.close()
            fWrite(c1File, "};\n")
            c1File.close()
            c2File.close()
            fWrite(c3File, "} T_REM_VAR, *P_REM_VAR;\n\n")
            # if c4File is not None:
            #     fWrite(c3File, "#if !defined(NO_REM_MACROS)\n")
            #     for data in remFunc:
            #         if not isinstance(data, str):
            #             (regName, index, regComment, varName, tmpType) = data
            #             tmp = "#define %s rVar._%s" % (varName, varName)
            #             fWrite(c3File, "%s/* 0x%02x %s */\n" %
            #                    (tmp.ljust(40), index, regComment))
            #         else:
            #             fWrite(c3File, "\n// %s\n\n" % (data))
            # fWrite(c3File, "\n#endif /* NO_REM_MACROS */\n")
            fWrite(c3File,\
                   "extern T_REM_VAR rVar;\n\n"\
                   "#endif /* REM_STRUCT */\n")
            c3File.close()
            if c4File is not None:
                fWrite(c4File, " };\n}\n\n")
                fWrite(c4File,
                       "void getRemVar(int parm, P_DATA_UNION val)\n{\n"\
                       " switch(parm)\n {\n")
                for data in remFunc:
                    if not isinstance(data, str):
                        (regName, index, regComment, varName, tmpType) = data
                        tmp = "case %s:" % (regName)
                        fWrite(c4File,
                               " %s/* %2d 0x%02x %s */\n"\
                               "  val->t_%s = rVar.%s;\n"\
                               "  break;\n\n" % (tmp.ljust(32), index, index, \
                                                 regComment, tmpType, varName))
                fWrite(c4File, " };\n}\n")
                c4File.close()
            # fWrite(jFile, "};\n")
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
            # fWrite(jFile, "package lathe;\n\n");
            # fWrite(jFile, "public class CtlStates\n{\n");
        f = None
        if self.file:
            file = 'enumDef'
            f = open(file + '.py', 'wb')
            fWrite(f, "\n# enums\n")
        val = 0
        for i in range(len(enumList)):
            data = enumList[i]
            # if not isinstance(data, basestring):
            if not isinstance(data, str):
                state = data[0]
                comment = data[1]
                if fData:
                    tmp =  " %s, " % (state)
                    fWrite(cFile, "%s/* %2d x%02x %s */\n" % \
                                (tmp.ljust(32), val, val, comment));
                    # fWrite(jFile, '  "%-10s %s", \n' % (state, comment));
                if state in globals():
                    print("createCtlStates %s already defined" % state)
                else:
                    globals()[state] = val
                    imports.append(state)
                    eval("%s.append('%s')" % (enum, state))
                    stringList.append((state, comment))
                    if f is not None:
                        tmp = "%s = %2d" % (state.ljust(16), val)
                        fWrite(f, "%s# %s\n" % (tmp.ljust(32), comment))
                val += 1
            else:
                if data.startswith("enum"):
                    commentList = None
                    tmp = data.split()
                    if len(tmp) < 2:
                        print("enum failure")
                        stdout.flush()
                    var = tmp[1]
                    enum = tmp[1].replace('_', "") + "List"
                    if len(tmp) >= 3:
                        if tmp[2][0] == 'c':
                            commentList = []
                    globals()[enum] = []
                    imports.append(enum)
                    val = 0
                    stringList = []
                    if fData:
                        fWrite(cFile, "enum %s\n" % (var.upper()))
                        # tmp =  " public static final String[] %s = \n" % \
                        #    (var])
                        # fWrite(jFile, tmp)
                elif data.startswith("{") or data.startswith("}"):
                    if fData:
                        fWrite(cFile, "%s\n" % (data))
                        if data.startswith("}"):
                            fWrite(cFile, "\n#ifdef ENUM_%s\n\n" % \
                                   (var.upper()))
                            fWrite(cFile, "const char *%s[] = \n{\n" % (enum))
                            for index, (s, comment) in enumerate(stringList):
                                tmp =  " \"%s\", " % (s)
                                if commentList is not None:
                                    commentList.append(comment)
                                fWrite(cFile, "%s/* %2d x%02x %s */\n" % \
                                            (tmp.ljust(32), index, \
                                             index, comment))
                            fWrite(cFile, "};\n\n#else\n\n")
                            fWrite(cFile, "extern const char *%s[];\n" % (enum))
                            fWrite(cFile, "\n#endif\n")
                        # fWrite(jFile, " %s\n" % (data))
                    if data.startswith("}") and f is not None:
                        fWrite(f, "\n%s = ( \\\n" % (enum))
                        for s in eval(enum):
                            fWrite(f, "    \"%s\",\n" % (s))
                        fWrite(f, "    )\n")
                        if commentList is not None:
                            fWrite(f, "\n%s = ( \\\n" % \
                                   (enum.replace('List', 'Text')))
                            for c in commentList:
                                   fWrite(f, "    \"%s\",\n" % (c))
                            fWrite(f, "    )\n")
                else:
                    if fData:
                        fWrite(cFile, "\n// %s\n\n" % (data))
                        # fWrite(jFile, "\n // %s\n\n" % (data))
                    if f is not None:
                        fWrite(f, "\n# %s\n\n" % (data))
        if f is not None:
            # self.listImports(file, imports)
            f.close()
        if fData:
            cFile.close()
            # fWrite(jFile, "};\n")
            # jFile.close()
        self.enumImports = imports
        self.importList += imports

    def createCtlBits(self, regList, cLoc, fData=False):
        imports = []
        if fData:
            cFile = open(cLoc + 'ctlbits.h', 'wb')
            # jFile = open(jLoc + 'CtlBits.java', 'wb')
            # fWrite(jFile, "package lathe;\n\n");
            # fWrite(jFile, "public class CtlBits\n{\n");
        f = None
        if self.file:
            file ='ctlBitDef'
            f = open(file + '.py', 'wb')
            fWrite(f, "\n# bit definitions\n")
        for i in range(len(regList)):
            data = regList[i]
            # if not isinstance(data, basestring):
            if not isinstance(data, str):
                (var, val, comment) = data
                if fData:
                    tmp =  "#define %-12s %s" % (var, val)
                    if isinstance(val, int):
                        val = str(val)
                    bitVal = eval(val)
                    fWrite(cFile, "%s /* 0x%02x %s */\n" % 
                                (tmp.ljust(32), bitVal, comment));
                    tmp =  " public static final int %-10s = %s;" % (var, val)
                    # fWrite(jFile, "%s /* %s */\n" % 
                    #             (tmp, comment));
                if var in globals():
                    print("createctlBits %s already defined" % var)
                else:
                    globals()[var] = eval(val)
                    imports.append(var)
                    if f is not None:
                        tmp = "%s = %s" % (var.ljust(16), val)
                        fWrite(f, "%s# 0x%02x %s\n" % \
                               (tmp.ljust(32), bitVal, comment))
            else:
                if fData:
                    fWrite(cFile, "\n// %s\n\n" % (data))
                    # fWrite(jFile, "\n// %s\n\n" % (data))
                if f is not None:
                    fWrite(f, "\n# %s\n\n" % (data))
        if f is not None:
            f.close()
        if fData:
            # self.listImports(file, imports)
            cFile.close()
            # fWrite(jFile, "};\n")
            # jFile.close()
        self.enumImports = imports
        self.importList += imports

    def createFpgaReg(self, fpgaList, cLoc, xLoc, fData=False, \
                        pName="xRegDef", table="xRegTable", cName="xilinx", \
                        xName="RegDef"):
        global xRegTable
        xRegTable = []
        imports = []
        imports.append(table)
        if fData:
            path = os.path.join(cLoc, cName + 'Reg.h')
            cFile = open(path, 'wb')
            fWrite(cFile, "enum " + cName.upper() + "\n{\n");
            try:
                xPath = os.path.join(xLoc, xName + '.vhd')
                xFile = open(xPath , 'wb')
            except (OSError, IOError) as e:
                print("unable to open %s" % (xLoc,))
                xFile = None
            if xFile:
                fWrite(xFile, "library ieee;\n")
                fWrite(xFile, "use ieee.std_logic_1164.all;\n")
                fWrite(xFile, "use ieee.numeric_std.all;\n\n")
                fWrite(xFile, "package RegDef is\n\n")
                fWrite(xFile, "constant opb : positive := 8;\n\n")
            # jFile = open(jLoc + 'Xilinx.java', 'wb')
            # fWrite(jFile, "package lathe;\n\n");
            # fWrite(jFile, "public enum Xilinx\n {\n");
            # j1File = open(jLoc + 'XilinxStr.java', 'wb')
            # j1File.write("package lathe;\n\n");
            # j1File.write("public class XilinxStr\n{\n");
            # j1File.write(" public static final String[] xilinxStr =\n {\n");
        f = None
        if self.file:
            f = open(pName + '.py', 'wb')
            fWrite(f, "# fpga registers\n\n")
        index = 0
        table = None
        regTables = []
        for i in range(len(fpgaList)):
            data = fpgaList[i]
            # print(data)
            # if not isinstance(data, basestring):
            if not isinstance(data, str):
                if len(data) == 1:
                    (tblName,) = data
                    cmd = "%s = []" % (tblName)
                    exec(cmd)
                    table = eval(tblName)
                    regTables.append((tblName, table))
                    continue
                if len(data) == 2:
                    (regName, regComment) = data
                    size = 1
                else:
                    (regName, base, size, byteLen, regComment) = data
                    if base is not None:
                        index = 0
                if fData:
                    tmp = " %s, " % (regName)
                    fWrite(cFile, "%s/* 0x%02x %s */\n" % 
                                (tmp.ljust(32), index, regComment));
                    if xFile:
                        fWrite(xFile, ('constant %-18s : ' \
                                     'unsigned(opb-1 downto 0) ' \
                                     ':= x"%02x"; -- %s\n') %
                                    (regName, index, regComment))
                    # tmp = "  %s, " % (regName)
                    # fWrite(jFile, "%s/* 0x%02x %s */\n" % 
                    #             (tmp.ljust(32), index, regComment));
                    # tmp = "  \"%s\", " % (regName)
                    # j1File.write("%s/* 0x%02x %s */\n" % 
                    #             (tmp.ljust(32), index, regComment));
                globals()[regName] = index
                imports.append(regName)
                xRegTable.append(regName)
                if f is not None:
                    tmp = "%s = %2d" % (regName.ljust(16), index)
                    fWrite(f, "%s# %s\n" % (tmp.ljust(32), regComment))
                if size is None:
                    cmd = "%s = %d" % (regName, index)
                    exec(cmd)
                    table = None
                else:
                    stdout.flush()
                    if isinstance(size, str):
                        incTable = eval(size)
                        total = 0
                        for (tRegName, tIndex, tSize, tByteLen) in incTable:
                            table.append((regName + ", " + tRegName,
                                          index + tIndex, tSize, tByteLen))
                            total += 1
                        index += total
                    else:
                        if table is not None:
                            table.append((regName, index, size, byteLen))
                        index += size
            else:
                if fData:
                    if (len(data) > 0):
                        fWrite(cFile, "\n// %s\n\n" % (data))
                        if xFile:
                            fWrite(xFile, "\n-- %s\n\n" % (data))
                        # fWrite(jFile, "\n// %s\n\n" % (data))
                    else:
                        fWrite(cFile, "\n");
                        if xFile:
                            fWrite(xFile, "\n");
                        # fWrite(jFile, "\n");
                if f is not None:
                    fWrite(f, "\n# %s\n\n" % (data))

        if True and len(regTables) != 0:
            # for (name, table) in regTables:
            #     print(name)
            #     for (tRegName, tIndex, tSize, tByteLen) in table:
            #         print("%-48s %2d %2d %2d" % (
            #             tRegName, tIndex, tSize, tByteLen))
            #     print()
            (name, table) = regTables[-1]
            opLenTable = []
            for (tRegName, tIndex, tSize, tByteLen) in table:
                opLenTable.append(tByteLen)
            # print(xLoc, xName)
            self.hexFile(os.path.join(xLoc, xName + ".hex"), opLenTable)

        if f is not None:
            fWrite(f, "# fpga table\n\n")

            if len(regTables) == 0:
                fWrite(f, "xRegTable = ( \\\n")
                for i, regName in enumerate(xRegTable):
                    tmp = "    \"%s\"," % (regName)
                    fWrite(f, "%s# %3d\n" % (tmp.ljust(40), i))
                fWrite(f, "    )\n")
            else:
                fWrite(f, "xRegTable = ( \\\n")
                (name, table) = regTables[-1]
                for (tRegName, tIndex, tSize, tByteLen) in table:
                    regs = tRegName.split(',')
                    if len(regs) == 1:
                        tmp = "    \"%s\"," % (regs[0])
                    else:
                        tmp = "    \"%s-%s\"," % (regs[0].strip(), \
                                                  regs[-1].strip())
                    fWrite(f, "%s# %3d x%02x\n" % \
                           (tmp.ljust(40), tIndex, tIndex))
                fWrite(f, "    )\n")

                fWrite(f, "\nfpgaSizeTable = ( \\\n")
                (name, table) = regTables[-1]
                for (tRegName, tIndex, tSize, tByteLen) in table:
                    tmp = "    %d," % (tByteLen)
                    fWrite(f, "%s# %3d %-s\n" % \
                           (tmp.ljust(20), tIndex, tRegName))
                fWrite(f, "    )\n")

            fWrite(f, "\nimportList = ( \\\n")
            for val in imports:
                fWrite(f, " %s, \\\n" % val)
            fWrite(f, ")\n")

            f.close()

        if fData:
            fWrite(cFile, "};\n")
            cFile.close()
            if xFile:
                fWrite(xFile, "\nend RegDef;\n\n")
                fWrite(xFile, "package body RegDef is\n\n")
                fWrite(xFile, "end RegDef;\n")
                xFile.close()
            # print("%s closed" % (xPath))
            # fWrite(jFile, "};\n")
            # jFile.close()
            # j1File.write(" };\n\n};\n")
            # jFile.close()

        # for key in xRegs:
        #     print("%-12s %02x" % (key, xRegs[key]))
        self.xRegImports = imports
        self.importList += imports
        self.xRegTable = xRegTable
        return(xRegTable)

    def hexRecord(self, address, record):
        recType = 0
        outRec = ":%02x%04x%02x" % (len(record), address, recType)
        chkSum = len(record)
        chkSum += (address >> 8) & 0xff
        chkSum += address * 0xff
        for val in record:
            outRec += "%02x" % val
            chkSum += val
        outRec += "%02x" % ((~chkSum + 1) & 0xff)
        return outRec

    def hexFile(self, name, data):
        f = open(name, "wb")
        record = []
        address = 0
        for i in range(len(data)):
            record.append(int(data[i]))
            if len(record) == 16:
                outRec = self.hexRecord(address, record)
                fWrite(f, outRec + '\n')
                address += len(record)
                record = []
        if len(record) != 0:
            outRec = self.hexRecord(address, record)
            fWrite(f, outRec + '\n')

    def createFpgaBits(self, xilinxBitList, cLoc, xLoc, fData=False, \
                       pName="xBitDef", xName="xilinx", \
                       package="CtlBits", cName="xilinx"):
        imports = []
        if fData:
            path = os.path.join(cLoc, cName + 'Bits.h')
            cFile = open(path, 'wb')
            try:
                path = os.path.join(xLoc, xName + 'Bits.vhd')
                xFile = open(path , 'wb')
            except IOError as e:
                print("unable to open %s" % (xLoc,))
                xFile = None
            if xFile:
                fWrite(xFile, "library ieee;\n"
                "use ieee.std_logic_1164.all;\n"
                "use ieee.numeric_std.all;\n\n")
                fWrite(xFile, "package " + package + " is\n")
            # jFile = open(jLoc + 'XilinxBits.java', 'wb')
            # fWrite(jFile, "package lathe;\n\n");
            # fWrite(jFile, "public class XilinxBits\n{\n");
        regName = ""
        bitStr = []
        lastShift = -1
        f = None
        if self.file:
            f = open(pName + '.py', 'wb')
            fWrite(f, "# fpga bits\n")
        for i in range(len(xilinxBitList)):
            shiftType = None
            data = xilinxBitList[i]
            if not isinstance(data, str):
                if len(data) == 1:
                    xLst = []
                    cLst = []
                    regName = data[0]
                    maxShift = 0
                    # rec = [regName,]
                else:
                    if len(data) == 4:
                        (var, bit, shift, comment) = data
                    cVar = var.upper()
                    xVar = var.replace("_", "")

                    shiftType = type(shift)
                    if fData:
                        tmp =  "#define %-12s  (%s << %s)" % (cVar, bit, shift)
                        if shiftType != tuple:
                            fWrite(cFile, "%s/* 0x%03x %s */\n" % 
                                   (tmp.ljust(32), bit << shift, comment));
                            if (shift != lastShift):
                                tmp =  "  \"%s\", " % (cVar)
                                bitStr.append("%s/* 0x%02x %s */\n" % 
                                              (tmp.ljust(32), bit << shift,
                                               comment))
                            xLst.append((" alias %-12s : " \
                                         "std_logic is %sreg(%d); " \
                                         "-- x%02x %s\n") %
                                        (xVar, regName, shift, \
                                         1 << shift, comment))
                            cLst.append((" constant c_%-12s : " \
                                         "integer := %2d; " \
                                         "-- x%02x %s\n") %
                                        (xVar, shift, \
                                         1 << shift, comment))
                            # tmp =  (" public static final int %-10s = " \
                            #         "(%s << %s);" % (cVar, bit, shift))
                            # fWrite(jFile, "%s /* %s */\n" % 
                            #             (tmp, comment));
                        else:
                            (shift, start) = shift
                            if bit is None:
                                xLst.append(" alias %-12s : unsigned is " \
                                            "%sreg(%d downto %d); " \
                                            "-- x%02x %s\n" %
                                            (xVar, regName, shift, start, \
                                             1 << shift, comment))
                            else:
                                xLst.append(" constant %-12s : unsigned " \
                                            "(%d downto %d) " \
                                            ":= \"%s\"; -- %s\n" % \
                                            (xVar, shift, start, \
                                             '{0:03b}'.format(bit), comment))
                    if (shift > maxShift):
                        maxShift = shift
                    if cVar in globals():
                        print("createFpgaBits %s already defined" % cVar)
                    else:
                        if shiftType != tuple:
                            if bit is not None:
                                globals()[cVar] = bit << shift
                                imports.append(var)
                                if f is not None:
                                    tmp = "%s = 0x%02x" % \
                                        (var.ljust(12), bit << shift)
                                    fWrite(f, "%s# %s\n" % \
                                           (tmp.ljust(32), comment))
                        else:
                            if bit is not None:
                                globals()[cVar] = bit << start
                                imports.append(var)
                                if f is not None:
                                    tmp = "%s = 0x%02x" % \
                                        (var.ljust(12), bit << start)
                                    fWrite(f, "%s# %s\n" % \
                                           (tmp.ljust(32), comment))
                        lastShift = shift
            else:
                if fData:
                    if (len(regName) > 0):
                        var = "%sSize" % (regName)
                        tmp =  "#define %-12s %d" % (var, maxShift + 1)
                        fWrite(cFile, "%s\n" % (tmp))
                        if xFile:
                            fWrite(xFile, " constant %sSize : " \
                                        "integer := %d;\n" % \
                                        (regName, maxShift + 1))
                            fWrite(xFile, " signal %sReg : "\
                                        "unsigned(%sSize-1 downto 0);\n" %
                                        (regName, regName))
                            for i in range(len(xLst)):
                                fWrite(xFile, xLst[i])
                            fWrite(xFile, "\n")
                            for i in range(len(cLst)):
                                fWrite(xFile, cLst[i])
                        # if (len(bitStr) != 0):
                        #     fWrite(jFile, "\n public static final " +
                        #                 "String[] %sBits =\n {\n") % \
                        #                 (regName))
                        #     for i in range(len(bitStr)):
                        #         fWrite(jFile, bitStr[i])
                        #     fWrite(jFile, " };\n");
                        #     bitStr = []
                    if (len(data) != 0):
                        fWrite(cFile, "\n// %s\n\n" % (data))
                        if xFile:
                            fWrite(xFile, "\n-- %s\n\n" % (data))
                        # fWrite(jFile, "\n// %s\n\n" % (data))
                else:
                    if (len(regName) > 0):
                        var = "%sSize" % (regName)
                        if var in globals():
                            print("createFpgaBits %s already defined" % var)
                        else:
                            globals()[var] = maxShift + 1
                            imports.append(var)
                if len(data) != 0 and f is not None:
                    fWrite(f, "\n# %s\n\n" % (data))
        if f is not None:
            # self.listImports(file, imports)
            fWrite(f, "\nimportList = ( \\\n")
            for val in imports:
                fWrite(f, " %s, \\\n" % val)
            fWrite(f, ")\n")
            f.close()
            # print("%s closed" % (pName))
        if fData:
            cFile.close()
            if xFile:
                fWrite(xFile, "\nend %s;\n\n" % (package))
                fWrite(xFile, "package body %s is\n\n" % (package))
                fWrite(xFile, "end %s;\n" % (package))
                xFile.close()
                # fWrite(jFile, "};\n")
                # jFile.close()
        self.xBitImports = imports
        self.importList += imports
