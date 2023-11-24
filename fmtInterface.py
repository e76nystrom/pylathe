#!/cygdrive/c/Python310/Python.exe
from sys import stdout
from datetime import datetime
from shutil import copyfile, move
import re
# from icecream import ic


dateTime = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
inFile = "interface.py"
backupFile = "interface.py-" + dateTime
tmpFile = "intTemp.py"

copyfile(inFile, backupFile)

f = open(inFile, "r")

fOut = open(tmpFile, "wb")

fOut.flush()

find = False
group = []
groupLen = 0
items = 0
argMax = []

for l, line in enumerate(f):
    line = line.rstrip()
    # print(line)
    output = True
    if find:
        match = re.match(r"^\s*\((.*)\),?", line)
        if match is not None:
            result = match.groups()
            # print("%4d" % l, result[0].ljust(72), end="")

            findDQuote = False
            findSQuote = False
            findParen = False
            lastIndex = 0
            arg = []
            r = result[0]
            strLen = len(r)
            for i in range(strLen):
                ch = r[i]

                if findDQuote and (ch == '"'):
                    findDQuote = False
                    continue
                if findSQuote and (ch == "'"):
                    findSQuote = False
                    continue
                if findParen and (ch == ")"):
                    findParen = False
                    continue

                if ch == '(':
                    findParen = True
                    continue
                if ch == '"':
                    findDQuote = True
                    continue
                if ch == "'":
                    findSQuote = True
                    continue

                if  not (findDQuote or findSQuote or findParen):
                    if ch == ',':
                        arg.append(r[lastIndex:i].strip())
                        lastIndex = i + 1

            if lastIndex < strLen:
                arg.append(r[lastIndex:].strip())

            if len(arg) != 1:
                if groupLen == 0:
                    groupLen = len(arg)
                    argMax = [0 for i in range(len(arg))]
                if groupLen != len(arg):
                    print("length error", groupLen, len(arg))
                    print("%4d" % l, r)
                    exit()
                for i, val in enumerate(arg):
                    argMax[i] = max(argMax[i], len(val))
                items += 1
                group.append(tuple(arg))
            else:
                group.append(line)
            # print(len(arg), arg)
            # stdout.flush()
        else:
            if re.search(r"->", line):
                txt = "        # <- len %d items %d [" % (groupLen, items)
                for val in argMax:
                    txt += " %2d" % (val)
                txt += "]\n"
                fOut.write(txt.encode("utf-8"))
                
                find = False
                for i in range(groupLen-1):
                    argMax[i] += 2
                for arg in group:
                    if isinstance(arg, tuple):
                        txt = "        ("
                        for index in range(groupLen-1):
                            val = arg[index]
                            txt += (val + ",").ljust(argMax[index])
                        txt += arg[-1] + "),\n"
                        fOut.write(txt.encode("utf-8"))
                    else:
                        fOut.write((str(arg) + "\n").encode("utf-8"))
                fOut.write((line + "\n").encode("utf-8"))
                fOut.flush()
            else:
                group.append(line)
    else:
        if re.search(r"<-", line):
            group = []
            groupLen = 0
            items = 0
            find = True
        else:
            fOut.write((line + "\n").encode("utf-8"))
            fOut.flush()
fOut.close()

move(tmpFile, inFile)
        
