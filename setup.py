################################################################################

# import os
from os.path import join as osJoin
from sys import stdout
import re

configTable = None
config = []
strTable = None
cmdTable = None
parmTable = None
enum = None
stringList = None
xRegTable = None

def fWrite(f, txt):
    if f is not None:
        f.write(txt.encode())
    
def cVarName(var):
    cVar = ""
    last = False
    for j in range(len(var)):
        ch = var[j]
        if ch.isupper():
            if last:
                cVar += "_"
            last = False
        else:
            last = True
        cVar += ch.upper()
    return cVar

class Setup():
    def __init__(self):
        self.importList = []
        self.outputFile = True

    # noinspection PyMethodMayBeStatic
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
        imports = ["config", "configTable"]
        f = None
        if self.outputFile:
            fName = 'configDef'
            f = open(fName + '.py', 'wb')
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
        self.configTable = configTable
        return(config, configTable)

    def createStrings(self, strList):
        global strTable
        strTable = []
        imports = ["strTable"]
        f = None
        if self.outputFile:
            fName = 'stringDef'
            f = open(fName + '.py', 'wb')
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

    def createCommands(self, cmdList, cLoc, fData=False, pyFile=True, \
                       check=True, prefix="rem"):
        global cmdTable
        imports = ["cmdTable"]
        cmdTable = []
        maxCmd = 0
        maxAct = 0
        cFile = None
        gName = ""
        if fData:
            name = prefix + "CmdList"
            cFile = open(osJoin(cLoc,  name + ".h"), 'wb')
            gName = cVarName(name)
            fWrite(cFile, "#if !defined(%s)\n"\
                   "#define %s\n\n" % (gName, gName))
            fWrite(cFile, "enum " + prefix.upper() + "_COMMANDS\n{\n")
        f = None
        if self.outputFile and pyFile:
            f = open(prefix + 'CmdDef.py', 'wb')
            fWrite(f, "\n# commands\n")
        index = 0
        for i in range(len(cmdList)):
            data = cmdList[i]
            # if not isinstance(data, basestring):
            if not isinstance(data, str):
                if (len(data) != 0):
                    (cmdName, action, cmdComment) = data
                    # if  isinstance(action, basestring):
                    if len(action) == 0:
                        action = None
                    if fData:
                        tmp = " %s, " % (cmdName)
                        fWrite(cFile, "%s/* 0x%02x %s */\n" % 
                                    (tmp.ljust(32), index, cmdComment))
                    maxCmd = max(maxCmd, len(cmdName))
                    if action is not None:
                        maxAct = max(maxAct, len(action))
                    cmdTable.append((cmdName, action))
                    if check and (cmdName in globals()):
                        print("createCommands %s already defined" % cmdName)
                    else:
                        globals()[cmdName] = index
                        imports.append(cmdName)
                        if f is not None:
                            fWrite(f, "%s = %3d\t# 0x%02x\n" % \
                                   (cmdName.ljust(20), index, index))
                    index += 1
            else:
                if fData:
                    if (len(data) > 0):
                        fWrite(cFile, "\n// %s\n\n" % (data))
                    else:
                        fWrite(cFile, "\n")
                if f is not None:
                    fWrite(f, "\n# %s\n\n" % (data))
        if f is not None:
            fWrite(f, "\n# command table\n\n")
            fWrite(f, "cmdTable = ( \\\n")
            maxCmd += 3
            maxAct += 2
            for index, (cmdName, action) in enumerate(cmdTable):
                cmdStr = ('"%s",' % cmdName).ljust(maxCmd)
                if action is not None:
                    actStr = ('"%s"' % action).ljust(maxAct)
                else:
                    actStr = 'None'.ljust(maxAct)
                fWrite(f, "    (%s %s), # 0x%02x %2d\n" % \
                       (cmdStr, actStr, index,  index))
            fWrite(f, "    )\n")
            # self.listImports(file, imports)
            f.close()
        if fData:
            fWrite(cFile, "};\n"\
                   "\n#endif  /* %s */\n" % (gName))
            cFile.close()
        self.cmdImports = imports
        self.importList += imports
        self.cmdTable = cmdTable
        return(cmdTable)

    def createParameters(self, parmList, cLoc, fData=False, pyFile=True, \
                         cSource='../lathe_src/', prefix='rem', cExt="cpp"):
        global parmTable
        parmTable = []
        maxRName = 0
        maxVType = 0
        maxVName = 0
        imports = ["parmTable"]
        preCap = prefix.capitalize()
        preUC = prefix.upper()
        remFunc = None
        cFile = None
        c1File = None
        c2File = None
        gName = ""
        if fData:
            cName = osJoin(cLoc, prefix + 'Parm.h')
            cFile = open(cName, 'wb')
            gName = cVarName(prefix + "Parm")
            fWrite(cFile, "#if !defined(%s)\n"\
                   "#define %s\n" % (gName, gName))

            fWrite(cFile, "/* defines */\n\n"\
                   "#define FLT (0x80)\n"\
                   "#define SIZE_MASK (0x7)\n\n"\
                   "enum " + preUC + "_PARM_DEF\n{\n")
            if cSource is not None:
                c1File = open(osJoin(cLoc, prefix + 'Struct.h'), 'wb')
                fWrite(c1File, "#if !defined(" + preUC + "_STRUCT)\n"\
                       "#define " + preUC + "_STRUCT\n\n"\
                       "#include <stdint.h>\n\n"\
                       "#if !defined(__DATA_UNION__)\n"\
                       "#define __DATA_UNION__\n\n"\
                       "#define uint_t unsigned int\n\n"\
                       "typedef union uDataUnion\n{\n"\
                       " float    t_float;\n"\
                       " int      t_int;\n"\
                       " uint_t   t_uint_t;\n"\
                       " int32_t  t_int32_t;\n"\
                       " uint32_t t_uint32_t;\n"\
                       " int16_t  t_int16_t;\n"\
                       " uint16_t t_uint16_t;\n"\
                       " char     t_char;\n"\
                       "} T_DATA_UNION, *P_DATA_UNION;\n\n"\
                       "#endif  /* __DATA_UNION__ */\n\n"\
                       "void set" + preCap + \
                       "Var(int parm, T_DATA_UNION val);\n"\
                       "void get" + preCap + \
                       "Var(int parm, P_DATA_UNION val);\n\n"\
                       "typedef struct s" + preCap + "Var\n{\n")
                try:
                    remFunc = []
                    c2File = open(osJoin(cLoc, cSource + prefix +
                                  'Func.' + cExt), 'wb')
                    fWrite(c2File,
                           "#include <stdint.h>\n"\
                           "#define NO_REM_MACROS\n"\
                           "#include \"" + prefix + "Parm.h\"\n"\
                           "#include \"" + prefix + "Struct.h\"\n\n"\
                           "T_" + preUC + "_VAR " + prefix[0] + "Var;\n\n")

                    fWrite(c2File, "#define FLT (0x80)\n")
                    fWrite(c2File, "#define SIZE_MASK (0x7)\n\n")
                    fWrite(c2File, "unsigned char " + prefix + "Size[] =\n{\n")
                except FileNotFoundError:
                    c2File = None
        f = None
        if self.outputFile and pyFile:
            f = open(prefix + 'ParmDef.py', 'wb')
            fWrite(f, "\n# parameters\n")
        index = 0
        for i in range(len(parmList)):
            data = parmList[i]
            # if not isinstance(data, basestring):
            if not isinstance(data, str):
                (regName, varType, regComment) = data
                tmp = regName.split("_")
                if len(tmp) > 1:
                    varName = ""
                    first = True
                    for s in tmp:
                        if first:
                            varName = s.lower()
                            first = False
                        else:
                            varName = varName + s.capitalize()
                else:
                    if regName.startswith('PRM'):
                        varName = regName[3:].lower()
                    else:
                        varName = regName.lower()
                # regAct = '0'
                # if (len(data) >= 4):
                #     regAct = data[3]
                if fData:
                    tmp = " %s, " % (regName)
                    fWrite(cFile, "%s/* 0x%02x %s */\n" % 
                                (tmp.ljust(32), index, regComment))
                    if c2File is not None:
                        if varType == "float":
                            tmp = " sizeof(%sVar.%s) | FLT, " % \
                                  (prefix[0], varName)
                        else:
                            tmp = " sizeof(%sVar.%s), " % (prefix[0], varName)
                        fWrite(c2File, "%s/* 0x%02x %s */\n" %
                                     (tmp.ljust(40), index, regComment))
                    if c1File is not None:
                        tmp = " %s %s;" % (varType, varName)
                        fWrite(c1File, "%s/* 0x%02x %-16s %s */\n" %
                                     (tmp.ljust(24), index, \
                                      regName, regComment))
                    if c2File is not None:
                        tmpType = varType.replace(' ', '_')
                        remFunc.append((regName, index, regComment, \
                                        varName, tmpType))
                maxRName = max(maxRName, len(regName))
                maxVType = max(maxVType, len(varType))
                maxVName = max(maxVName, len(varName))
                parmTable.append((regName, varType, varName))
                if regName in imports:
                    print("createParameters %s already defined" % regName)
                else:
                    # globals()[regName] = index
                    imports.append(regName)
                    if f is not None:
                        fWrite(f, "%s = %3d\t# 0x%02x\n" % \
                               (regName.ljust(20), index, index))
                index += 1
            else:
                if fData:
                    fWrite(cFile, "\n// %s\n\n" % (data))
                    if c1File is not None:
                        fWrite(c2File, "\n// %s\n\n" % (data))
                        # fWrite(c2File, "\n// %s\n\n" % (data))
                        fWrite(c1File, "\n// %s\n\n" % (data))
                    if c2File is not None:
                        remFunc.append(data)
                if f is not None:
                    fWrite(f, "\n# %s\n\n" % (data))
        if f is not None:
            fWrite(f, "\nparmTable = ( \\\n")
            maxRName += 3
            maxVType += 3
            maxVName += 2
            for index, (regName, varType, varName) in enumerate(parmTable):
                rNameStr = ('"%s",' % regName).ljust(maxRName)
                vTypeStr = ('"%s",' % varType).ljust(maxVType)
                vNameStr = ('"%s"' % varName).ljust(maxVName)
                fWrite(f, "    (%s %s %s), # 0x%02x %3d\n" % \
                       (rNameStr, vTypeStr, vNameStr, index, index))
            fWrite(f, "    )\n")
            # self.listImports(file, imports)
            f.close()
            f = open(prefix + "Parm.py", "wb")
            fWrite(f, "class " + preCap + "Parm():\n")
            fWrite(f, "    def __init__(self):\n")
            for (varIndex, varType, varName) in parmTable:
                fWrite(f, "        self.%s = None\n" % (varName))
            f.close()
        if fData:
            fWrite(cFile, "};\n" \
                   "\n#endif  /* %s */\n" % (gName))
            cFile.close()
            fWrite(c2File, "};\n\n")

            if c1File is not None:
                fWrite(c1File, "} T_" + preUC + \
                       "_VAR, *P_" + preUC + "_VAR;\n\n")
                fWrite(c1File,\
                       "extern unsigned char " + prefix + "Size[];\n"\
                       "extern T_" + preUC + "_VAR " + prefix[0] + "Var;\n\n"\
                       "#endif /* " + preUC + "_STRUCT */\n")
                c1File.close()
            if c2File is not None:
                fWrite(c2File,
                       "void set" + preCap + \
                       "Var(const int parm, const T_DATA_UNION val)\n{\n"\
                       " switch(parm)\n {\n"\
                       " default:\n"\
                       "  break;\n\n")

                for data in remFunc:
                    if not isinstance(data, str):
                        (regName, index, regComment, varName, tmpType) = data
                        tmp = "case %s:" % (regName)
                        fWrite(c2File,
                               (" %s/* %2d 0x%02x %s */\n"\
                               "  " + prefix[0] + "Var.%s = val.t_%s;\n"\
                               "  break;\n\n") % (tmp.ljust(32), index, index, \
                                                 regComment, varName, tmpType))

                fWrite(c2File, " }\n}\n\n")
                fWrite(c2File,
                       "void get" + preCap + \
                       "Var(const int parm, const P_DATA_UNION val)\n{\n"\
                       " switch(parm)\n {\n"\
                           " default:\n"\
                           "  break;\n\n")

                for data in remFunc:
                    if not isinstance(data, str):
                        (regName, index, regComment, varName, tmpType) = data
                        tmp = "case %s:" % (regName)
                        fWrite(c2File,
                               (" %s/* %2d 0x%02x %s */\n"\
                               "  val->t_%s = " + prefix[0] + "Var.%s;\n"\
                               "  break;\n\n") % \
                               (tmp.ljust(32), index, index, \
                                regComment, tmpType, varName))
                fWrite(c2File, " }\n}\n")
                c2File.close()

        #for key in parms:
        #    print(key, parms[key])
        self.parmImports = imports
        self.importList += imports
        self.parmTable = parmTable
        return(parmTable)

    def createEnums(self, enumList, cLoc, fData=False, pyFile=True,
                    prefix=""):
        global enum, stringList
        imports = []
        var = None
        cFile = None
        gName = ""
        if fData:
            fName = 'ctlStates.h'
            if len(prefix) != 0:
                fName = prefix + fName.capitalize()
            cFile = open(osJoin(cLoc, fName), 'wb')
            gName = "CTL_STATES_INC"
            fWrite(cFile, "#if !defined(%s)\n"\
                   "#define %s\n" % (gName, gName))
        f = None
        if self.outputFile and pyFile:
            fName = 'enum'
            if len(prefix) != 0:
                fName = prefix + fName.capitalize()
            fName += 'Def'
            f = open(fName + '.py', 'wb')
            fWrite(f, "\n# enums\n")
        val = 0
        for i in range(len(enumList)):
            data = enumList[i]
            if not isinstance(data, str):
                state = data[0]
                tmp = state.split('=')
                if len(tmp) == 2:
                    state = tmp[0].strip()
                    val = int(tmp[1])
                comment = data[1]
                if fData:
                    tmp =  " %s = %s, " % (state, val)
                    fWrite(cFile, "%s/* %2d x%02x %s */\n" % \
                                (tmp.ljust(32), val, val, comment))

                if pyFile:
                    if state in globals():
                        print("createCtlStates %s already defined" % state)
                    else:
                        globals()[state] = val
                        imports.append(state)
                        eval("%s.append('%s')" % (enum, state))
                        stringList.append((state, val, comment))
                        if f is not None:
                            tmp = "%s = %2d" % (state.ljust(16), val)
                            fWrite(f, "%s# %s\n" % (tmp.ljust(32), comment))
                val += 1
            else:
                commentList = []
                if data.startswith("enum"):
                    tmp = data.split()
                    if len(tmp) < 2:
                        print("enum failure")
                        stdout.flush()
                    var = tmp[1]
                    enum = tmp[1].replace('_', "") + "List"
                    globals()[enum] = []
                    imports.append(enum)
                    val = 0
                    stringList = []
                    if fData:
                        fWrite(cFile, "enum %s\n" % (var.upper()))
                elif data.startswith("{") or data.startswith("}"):
                    if fData:
                        fWrite(cFile, "%s\n" % (data))
                        if data.startswith("}"):
                            fWrite(cFile, "\n#ifdef ENUM_%s\n\n" % \
                                   (var.upper()))
                            fWrite(cFile, "const char *%s[] = \n{\n" % (enum))
                            lastVal = -1
                            for index, (s, val, comment) in enumerate(stringList):
                                if val == lastVal:
                                    continue
                                lastVal = val
                                tmp =  " \"%s\", " % (s)
                                if commentList is not None:
                                    commentList.append(comment)
                                fWrite(cFile, "%s/* %2d x%02x %s */\n" % \
                                            (tmp.ljust(32), val, \
                                             val, comment))
                            fWrite(cFile, "};\n\n#else\n\n")
                            fWrite(cFile, "extern const char *%s[];\n" % (enum))
                            fWrite(cFile, "\n#endif\n")
                            
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

                            if commentList[0].startswith("'"):
                                cLen = 0
                                c = commentList[0]
                                match = re.match("\'([ \w+\-]*)\'", c)
                                if match is not None:
                                    result = match.groups()
                                    regCode = result[0]
                                    cLen = len(regCode)
                                sName = enum.replace("List", "")
                                # print(sName)
                                path = osJoin(cLoc, sName + 'Str.h')
                                sFile = open(path, 'wb')
                                uVar = var.upper()
                                fWrite(sFile, "#if !defined(INC_%s)\n" \
                                       "#define INC_%s\n\n" \
                                       "struct S_%s\n" \
                                       "{\n char c0;\n char c1;\n" % \
                                       (uVar, uVar, uVar))

                                if cLen == 4:
                                    fWrite(sFile, " char c2;\n char c3;\n")

                                fWrite(sFile, "};\n\n" \
                                       "struct S_%s %sStr[] =\n{\n" % \
                                       (var.upper(), sName))
                                for j, c in enumerate(commentList):
                                    match = re.match("\'([ \w+\-]*)\'([\s\w]*)", c)
                                    regCode = ''
                                    rComment = ''
                                    if match is not None:
                                        result = match.groups()
                                        regCode = result[0]
                                        if len(result) >= 2:
                                            rComment = result[1]
                                    sReg = ""
                                    for k in range(len(regCode)):
                                        sReg += "'" + regCode[k]  + "', "
                                    sReg = sReg[:-1]
                                    sReg = '{' + sReg + '},'
                                    txt = " %s/* %2x %2d %s */\n" % \
                                        (sReg.ljust(24), j, j, rComment)
                                    fWrite(sFile, txt)
                                fWrite(sFile, "};\n\n" \
                                       "#endif  /* %s */\n" % (uVar))
                                sFile.close()
                else:
                    if fData:
                        fWrite(cFile, "\n// %s\n\n" % (data))
                    if f is not None:
                        fWrite(f, "\n# %s\n\n" % (data))
        if f is not None:
            f.close()
        if fData:
            fWrite(cFile, "\n#endif  /* %s */\n" % (gName))
            cFile.close()
        self.enumImports = imports
        self.importList += imports

    def createCtlBits(self, regList, cLoc, fData=False):
        imports = []
        cFile = None
        bitVal = None
        gName = ""
        if fData:
            cFile = open(osJoin(cLoc, 'ctlBits.h'), 'wb')
            gName = "CTL_BITS_INC"
            fWrite(cFile, "#if !defined(%s)\n"\
                   "#define %s\n" % (gName, gName))
        f = None
        if self.outputFile:
            fName ='ctlBitDef'
            f = open(fName + '.py', 'wb')
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
                                (tmp.ljust(32), bitVal, comment))
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
                if f is not None:
                    fWrite(f, "\n# %s\n\n" % (data))
        if f is not None:
            f.close()
        if fData:
            fWrite(cFile, "\n#endif  /* %s */\n" % (gName))
            cFile.close()
        self.enumImports = imports
        self.importList += imports

    def createFpgaReg(self, fpgaList, cLoc, xLoc, fData=False, \
                        pName="xRegDef", table="xRegTable", cName="xilinx", \
                        xName="RegDef"):
        global xRegTable
        xRegTable = []
        imports = [table]
        cFile = None
        c1File = None
        xFile = None
        byteLen = 0
        gName = ""
        if fData:
            path = osJoin(cLoc, cName + 'Reg.h')
            cFile = open(path, 'wb')
            gName = cVarName(cName)
            fWrite(cFile, "#if !defined(%s)\n"\
                   "#define %s\n\n" % (gName, gName))
            fWrite(cFile, "enum " + cName.upper() + "\n{\n")
            path = osJoin(cLoc, cName + 'Str.h')
            c1File = open(path, 'wb')
            fWrite(c1File, "typedef struct S_CHR\n"\
                           "{\n char c0;\n char c1;\n"
                           " char c2;\n char c3;\n} T_CH4, *P_CH4;\n\n"\
                   "T_CH4 fpgaOpStr[] =\n{\n")
            try:
                xPath = osJoin(xLoc, xName + '.vhd')
                xFile = open(xPath , 'wb')
            except (OSError, IOError):
                print("unable to open %s" % (xLoc,))
                xFile = None
            if xFile:
                fWrite(xFile, "library ieee;\n")
                fWrite(xFile, "use ieee.std_logic_1164.all;\n")
                fWrite(xFile, "use ieee.numeric_std.all;\n\n")
                fWrite(xFile, "package RegDef is\n\n")
                fWrite(xFile, "constant opb : positive := 8;\n\n")
        f = None
        if self.outputFile:
            f = open(pName + '.py', 'wb')
            fWrite(f, "# fpga registers\n\n")
        index = 0
        table = None
        regTables = []
        for i in range(len(fpgaList)):
            data = fpgaList[i]

            if not isinstance(data, str):
                if len(data) == 1: 	# create new list
                    tblName= data[0]
                    # print("***new list***", tblName)
                    globals()[tblName] = []
                    table = globals()[tblName]
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
                    tmp = " %-18s = %s, " % (regName, index)
                    fWrite(cFile, "%s/* 0x%02x %s */\n" % 
                                (tmp.ljust(32), index, regComment))
                    if xFile:
                        fWrite(xFile, ('constant %-18s : ' \
                                     'unsigned(opb-1 downto 0) ' \
                                     ':= x"%02x"; -- %s\n') %
                                    (regName, index, regComment))

                globals()[regName] = index
                imports.append(regName)
                xRegTable.append(regName)
                
                if f is not None:
                    tmp = "%s = %2d" % (regName.ljust(16), index)
                    fWrite(f, "%s# %s\n" % (tmp.ljust(32), regComment))
                    # print(regComment)

                if size is None:
                    # print("***%s*** = %d" % (regName, index))
                    globals()[regName] = index
                    table = None
                else:
                    stdout.flush()
                    if isinstance(size, str): # if ref to another table
                        incName = size
                        # print("+++incName+++", incName)
                        incTable = globals()[incName]
                        # print(incTable)
                        total = 0
                        match = re.match("\'([\w+\-]*)\'", regComment)
                        regCode = ''
                        if match is not None:
                            result = match.groups()
                            if len(result) >= 1:
                                regCode = match.group(1)

                        for (tRegName, tIndex, tSize, tByteLen,
                             tRegCode) in incTable:
                            (tRegCode, tRegComment) = tRegCode
                            tRegCode = regCode + tRegCode
                            table.append((regName + ", " + tRegName,
                                          index + tIndex, tSize,
                                          tByteLen, (tRegCode, tRegComment)))
                            total += 1
                        index += total
                    else:
                        if table is not None:
                            match = re.match("\'([\w+\-]*)\'([\s\w]*)",
                                             regComment)
                            regCode = ''
                            if match is not None:
                                result = match.groups()
                                if len(result) >= 1:
                                    regCode = match.group(1)
                                    #print(match.group(1))
                                    if len(result) >= 2:
                                        regComment = match.group(2)
                            table.append((regName, index, size,
                                          byteLen, (regCode, regComment)))
                            # print(table[-1])
                        index += size
            else:
                if fData:
                    if (len(data) > 0):
                        fWrite(cFile, "\n// %s\n\n" % (data))
                        if xFile:
                            fWrite(xFile, "\n-- %s\n\n" % (data))
                    else:
                        fWrite(cFile, "\n")
                        if xFile:
                            fWrite(xFile, "\n")
                if f is not None:
                    try:
                        fWrite(f, "\n# %s\n\n" % (data))
                    except TypeError:
                        print(data)

        if True and len(regTables) != 0:
            # for (name, table) in regTables:
            #     print(name)
            #     for (tRegName, tIndex, tSize, tByteLen) in table:
            #         print("%-48s %2d %2d %2d" % (
            #             tRegName, tIndex, tSize, tByteLen))
            #     print()

            (name, table) = regTables[-1]
            opLenTable = []
            for (tRegName, tIndex, tSize, tByteLen, tRegCode) in table:
                opLenTable.append(tByteLen)
            self.hexFile(osJoin(xLoc, xName + ".hex"), opLenTable)

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
                for (tRegName, tIndex, tSize, tByteLen, tRegCode) in table:
                    regs = tRegName.split(',')
                    if len(regs) == 1:
                        tmp = "    \"%s\"," % (regs[0])
                    else:
                        tmp = "    \"%s+%s\"," % (regs[0].strip(), \
                                                  regs[-1].strip())
                    fWrite(f, "%s# %3d x%02x\n" % \
                           (tmp.ljust(40), tIndex, tIndex))
                fWrite(f, "    )\n")

                fWrite(f, "\nfpgaSizeTable = ( \\\n")
                (name, table) = regTables[-1]
                for (tRegName, tIndex, tSize, tByteLen, tRegCode) in table:

                    (tRegCode, tRegComment) = tRegCode
                    tRegCode = tRegCode.strip()
                    if len(tRegCode) < 4:
                        tRegCode = tRegCode.ljust(4)
                    sReg = "{"
                    for i in range(len(tRegCode)):
                        sReg += "'" + tRegCode[i]  + "', "
                    sReg = sReg[:-1] + '}'
                    txt = (" %s, /* %02x %3d %-24s %s */\n" % \
                           (sReg, tIndex, tIndex, tRegComment.strip(),
                            tRegName))
                    fWrite(c1File, txt)

                    tmp = "    %d," % (tByteLen)
                    fWrite(f, "%s# %3d %-s\n" % \
                           (tmp.ljust(20), tIndex, tRegName))
                fWrite(f, "    )\n")

            fWrite(f, "\nimportList = ( \\\n")
            for val in imports:
                fWrite(f, " %s, \\\n" % val)
            fWrite(f, ")\n")

            fWrite(c1File, "};\n")
            f.close()
            c1File.close()

        if fData:
            fWrite(cFile, "};\n" \
                   "\n#endif  /* %s */\n" % (gName))
            cFile.close()
            if xFile:
                fWrite(xFile, "\nend RegDef;\n\n")
                fWrite(xFile, "package body RegDef is\n\n")
                fWrite(xFile, "end RegDef;\n")
                xFile.close()

        # for key in xRegs:
        #     print("%-12s %02x" % (key, xRegs[key]))
        self.xRegImports = imports
        self.importList += imports
        self.xRegTable = xRegTable
        return(xRegTable)

    # noinspection PyMethodMayBeStatic
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

    def createFpgaBits(self, bitList, cLoc, xLoc, fData=False, \
                       pName="xBitDef", xName="xilinx", \
                       package="CtlBits", cName="xilinx"):
        # var = None
        # shift = None
        # bit = None
        cFile = None
        xFile = None
        rFile = None
        fFile = None
        body = None
        # comment = None
        xLst = []
        cLst = []
        rData = []
        rCLst = []
        sLst = []
        maxShift = None
        start = None
        imports = []
        gName = ""
        if fData:
            path = osJoin(cLoc, cName + 'Bits.h')
            cFile = open(path, 'wb')
            gName = cVarName(cName) + "_BITS"
            fWrite(cFile, "#if !defined(%s)\n"\
                   "#define %s\n" % (gName, gName))
            try:
                path = osJoin(xLoc, xName + 'Bits.vhd')
                xFile = open(path , 'wb')
                fWrite(xFile, "library ieee;\n\n"
                "use ieee.std_logic_1164.all;\n"
                "use ieee.numeric_std.all;\n\n")
                fWrite(xFile, "package " + package + " is\n")
            except IOError:
                print("unable to open %s" % (xLoc,))
                xFile = None

            try:
                path = osJoin(xLoc, xName + 'Rec.vhd')
                rFile = open(path , 'wb')
                fWrite(rFile, "library ieee;\n\n"
                "use ieee.std_logic_1164.all;\n"
                "use ieee.numeric_std.all;\n\n")
                fWrite(rFile, "package " + package + "Rec is\n\n")
            except IOError:
                print("unable to open %s" % (xLoc,))
                rFile = None

            try:
                path = osJoin(xLoc, xName + 'Func.vhd')
                fFile = open(path , 'wb')
                fWrite(fFile, "library ieee;\n\n"
                "use ieee.std_logic_1164.all;\n"
                "use ieee.numeric_std.all;\n\n")
                fWrite(fFile, "use work.%sRec.all;\n\n" % (package))
                fWrite(fFile, "package " + package + "Func is\n\n")

                body = "package body " + package + "Func is\n\n"
            except IOError:
                print("unable to open %s" % (xLoc,))
                fFile = None

        regName = ""
        bitStr = []
        lastShift = -1
        f = None
        if self.outputFile:
            f = open(pName + '.py', 'wb')
            fWrite(f, "# fpga bits\n")
        for i in range(len(bitList)):
            # shiftType = None
            data = bitList[i]
            if not isinstance(data, str):
                if len(data) == 1:
                    if len(sLst) != 0:
                        path = osJoin(cLoc, regName + 'RegStr.h')
                        sFile = open(path, 'wb')
                        fWrite(sFile, "struct S_%s\n" \
                                      "{\n char c0;\n char c1;\n};\n\n" \
                               "struct S_%s %sRegStr[] =\n{\n" % \
                               (regName.upper(), regName.upper(), regName))
                        for (cVar, shift, regCode, rComment) in sLst:
                            # if len(regCode) < 2:
                            #     tregCode = regCode.ljust(2)
                            sReg = ""
                            for j in range(len(regCode)):
                                sReg += "'" + regCode[j]  + "', "
                            sReg = sReg[:-1]
                            txt = " {%s}, /* %4x %2d %-16s %s */\n" % \
                                (sReg, 1<<shift, shift, cVar, rComment)
                            fWrite(sFile, txt)
                        fWrite(sFile, "};\n")
                        sFile.close()
                    # sLst = []
                    xLst = []
                    cLst = []
                    rData = []
                    sLst = []
                    regName = data[0]
                    maxShift = 0
                else:
                    #if len(data) == 4:
                    (var, bit, shift, comment) = data[:4]
                    cVar = cVarName(var)
                    xVar = var.replace("_", "")

                    # shiftType = type(shift)
                    if fData:
                        # if shiftType != tuple:
                        if not isinstance(shift, tuple):
                            tmp =  "#define %-18s (%s << %s)" % (cVar, bit, shift)
                            fWrite(cFile, "%s/* 0x%03x %s */\n" % 
                                   (tmp.ljust(40), bit << shift, comment))

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

                            match = re.match("\'([\w+\-]*)\'([\s\w]*)",
                                             comment)
                            if match is not None:
                                result = match.groups()
                                if len(result) >= 1:
                                    regCode = result[0]
                                    rComment = ''
                                    if len(result) >= 2:
                                        rComment = result[1]
                                    sLst.append((cVar, shift, regCode,
                                                 rComment.strip()))

                            rData.append((xVar, shift, comment))

                        else:
                            (shift, start) = shift
                            if bit is None:
                                x = 1
                                for j in range(start, shift):
                                    x = (x << 1) + 1
                                tmp =  "#define %-18s (0x%x << %s)" % (cVar, x, start)
                                fWrite(cFile, "%s/* 0x%03x %s */\n" % 
                                       (tmp.ljust(40), x << start, comment))

                                xLst.append(" alias %-14s : unsigned is " \
                                            "%sreg(%d downto %d); " \
                                            "-- x%02x %s\n" %
                                            (xVar, regName, shift, start, \
                                             1 << shift, comment))
                                rData.append((xVar, (shift, start), comment))
                            else:
                                tmp =  "#define %-18s (%s << %s)" % (cVar, bit, start)
                                fWrite(cFile, "%s/* 0x%03x %s */\n" % 
                                       (tmp.ljust(40), bit << shift, comment))

                                xVal = (" constant %-12s : unsigned " \
                                        "(%d downto %d) " \
                                        ":= \"%s\"; -- %s\n" % \
                                        (xVar, shift-start, 0, \
                                        '{0:03b}'.format(bit), comment))
                                xLst.append(xVal)
                                
                                cVal = (" constant %-12s : std_logic_vector " \
                                        "(%d downto %d) " \
                                        ":= \"%s\"; -- %s\n" % \
                                        (xVar, shift-start, 0, \
                                        '{0:03b}'.format(bit), comment))
                                rCLst.append(cVal)
                                
                    if (shift > maxShift):
                        maxShift = shift
                    if cVar in globals():
                        print("createFpgaBits %s already defined" % cVar)
                    else:
                        # if shiftType != tuple:
                        if not isinstance(shift, tuple):
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
                        tmp =  "#define %-18s %d" % (cVarName(var), maxShift + 1)
                        fWrite(cFile, "%s\n" % (tmp))
                        if xFile:
                            fWrite(xFile, " constant %sSize : " \
                                        "integer := %d;\n" % \
                                        (regName, maxShift + 1))
                            fWrite(xFile, " signal %sReg : "\
                                        "unsigned(%sSize-1 downto 0);\n" %
                                        (regName, regName))
                            fWrite(xFile, " --variable %sReg : "\
                                        "unsigned(%sSize-1 downto 0);\n" %
                                        (regName, regName))
                            for k in range(len(xLst)):
                                fWrite(xFile, xLst[k])
                            fWrite(xFile, "\n")
                            for k in range(len(cLst)):
                                fWrite(xFile, cLst[k])

                        if rFile is not None:
                            body += rOut(rFile, fFile, rCLst, rData,
                                         regName, maxShift)
                            rCLst = []

                    if (len(data) != 0):
                        fWrite(cFile, "\n// %s\n\n" % (data))
                        if xFile:
                            fWrite(xFile, "\n-- %s\n\n" % (data))
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
            fWrite(f, "\nimportList = ( \\\n")
            for val in imports:
                fWrite(f, " %s, \\\n" % val)
            fWrite(f, ")\n")
            f.close()
            
        if fData:
            fWrite(cFile, "\n#endif  /* %s */\n" % (gName))
            cFile.close()
            if xFile:
                fWrite(xFile, "\nend %s;\n\n" % (package))
                fWrite(xFile, "package body %s is\n\n" % (package))
                fWrite(xFile, "end %s;\n" % (package))
                xFile.close()

            if rFile:
                fWrite(rFile, "end package %sRec;\n" % (package))
                rFile.close()
                fWrite(fFile, "end %sFunc;\n\n" % (package))
                fWrite(fFile, body)
                fWrite(fFile, "end package body %sFunc;\n" % (package))

        self.xBitImports = imports
        self.importList += imports

def rOut(rFile, fFile, rCLst, rData, regName, maxShift):
    maxLen = 0
    for val in rData:
        l = len(val[0])
        if l > maxLen:
            maxLen = l

    fWrite(rFile, "type %sRec is record\n" % (regName))

    num = len(rData)
    fmt = "-- %2d 0x%0" + ("%d" % (int((num + 3) / 4))) + "x %s\n"
    for k in range(num-1, -1, -1):
        (name, shift, comment) = rData[k]
        name = name.ljust(maxLen)
        # if type(shift) != tuple:
        if not isinstance(shift, tuple):
            tmp = (" %s : std_logic;" % (name))
            tmp = tmp.ljust(32) + \
                (fmt % (shift, 1 << shift, comment))
        else:
            (shift, start) = shift
            tmp = (" %s : std_logic_vector(%d downto 0);" % \
                   (name, shift - start))
            tmp = tmp.ljust(32) + ("-- %d-%d %s\n" % (shift, start, comment))
        fWrite(rFile, tmp)

    fWrite(rFile, "end record %sRec;\n\n" % (regName))

    if len(rCLst) != 0:
        for tmp in rCLst:
            fWrite(rFile, tmp)
        fWrite(rFile, "\n")

    tmp = ("constant %sSize : integer := %d;\n" % \
           (regName, maxShift + 1))
    tmp += ("subType %sVec is " \
            "std_logic_vector(%sSize-1 downto 0);\n" %
           (regName, regName))
    tmp += ("constant %sZero : %sVec := (others => '0');\n\n" % \
    (regName, regName))
    tmp += ("function %sToVec(val : %sRec)\n " \
            "return %sVec;\n\n" %
           (regName, regName, regName))

    #tmp += ("function %sToRec(val : std_logic_vector(%sSize-1 downto 0))\n " \
    #        "return %sVec;\n\n" %
    #       (regName, regName, regName))
    fWrite(fFile, tmp)

    body = ("function %sToVec(val : %sRec) " \
            "return %sVec is\n" %
           (regName, regName, regName))

    body += " variable rtnVec : %sVec;\n" % (regName)
    body += "begin\n"

    tmp = " rtnVec :="
    startLen = len(tmp)
    l = len(tmp)
    for i in range(num-1, -1, -1):
        data = " val.%s &" % (rData[i][0].ljust(maxLen))
        dataLen = len(data)
        if (l + dataLen) >= 76:
            l = 4
            tmp += "\n" + (" " * startLen)
        l += dataLen
        tmp += data
    tmp = tmp[0:-2].rstrip()
    tmp += ";\n"
    body += tmp

    body += " return rtnVec;\n"
    body += "end function;\n\n"

    fWrite(fFile, ("function %sToRec(val : %sVec)\n" \
                   "return %sRec;\n\n" %
                   (regName, regName, regName)))

    body += ("function %sToRec(val : %sVec) " \
            "return %sRec is\n" %
           (regName, regName, regName))
    body += " variable rtnRec : %sRec;\n" % (regName)
    body += "begin\n"
    for i in range(num-1, -1, -1):
        (name, shift, comment) = rData[i]
        name = name.ljust(maxLen)
        # if type(shift) != tuple:
        if not isinstance(shift, tuple):
            body += " rtnRec.%s := val(%s);\n" % (name, shift)
        else:
            (shift, start) = shift
            body += (" rtnRec.%s := val(%s downto %s);\n" %
                     (name, shift, start))
    body += "\n return rtnRec;\n"
    body += "end function;\n\n"

    fWrite(fFile, ("function %sToRecS(val : std_logic_vector(%sSize-1 downto 0))\n" \
                   "return %sRec;\n\n" %
                   (regName, regName, regName)))

    body += ("function %sToRecS(val : std_logic_vector(%sSize-1 downto 0))\n" \
            " return %sRec is\n" %
           (regName, regName, regName))
    body += " variable rtnRec : %sRec;\n" % (regName)
    body += "begin\n"
    for i in range(num-1, -1, -1):
        (name, shift, comment) = rData[i]
        name = name.ljust(maxLen)
        # if type(shift) != tuple:
        if not isinstance(shift, tuple):
            body += " rtnRec.%s := val(%s);\n" % (name, shift)
        else:
            (shift, start) = shift
            body += (" rtnRec.%s := val(%s downto %s);\n" %
                     (name, shift, start))
    body += "\n return rtnRec;\n"
    body += "end function;\n\n"

    return body
