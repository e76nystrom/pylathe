from __future__ import print_function
from sys import stdout

info = []
infoData = []
configTable = None

class InfoValue():
    def __init__(self, val):
        self.value = val

    def GetValue(self):
        return(self.value)

    def SetValue(self, val):
        self.value = val

def clrInfo(size):
    global info, infoData
    info = [None for i in range(size)]
    infoData = [None for i in range(size)]

def saveList(file, configTable, varList):
    global info
    f = open(file, 'w')
    for index in varList:
        name = configTable[index]
        val = info[index]
        writeConfig(f, name, val)
    f.close()

def saveInfo(file, configTable):
    global info
    f = open(file, 'w')
    # for key in sorted(config.keys()):
    #     index = config[key]
    #     val = info[index]
    for index, (val) in enumerate(info):
        name = configTable[index]
        writeConfig(f, name, val)
    f.close()

def writeConfig(f, name, val):
    valClass = val.__class__.__name__
    # print(name, valClass)
    # stdout.flush()
    if valClass == 'TextCtrl':
        f.write("%s=%s\n" % (name, val.GetValue()))
    elif valClass == 'RadioButton':
        f.write("%s=%s\n" % (name, val.GetValue()))
    elif valClass == 'CheckBox':
        f.write("%s=%s\n" % (name, val.GetValue()))
    elif valClass == 'ComboBox':
        f.write("%s=%s\n" % (name, val.GetValue()))
    elif valClass == 'InfoValue':
        f.write("%s=%s\n" % (name, val.GetValue()))
    elif valClass == 'StaticText':
        pass

def readInfo(file, config, configList=None):
    global info
    try:
        f = open(file, 'r')
        for line in f:
            line = line.rstrip()
            if len(line) == 0:
                continue
            [key, val] = line.split('=')
            if not key in config:
                print("readInfo invalid config value %s" % key)
                stdout.flush()
                continue
            index = config[key]
            if configList != None:
                if not index in configList:
                    continue
            if info[index] != None:
                func = info[index]
                funcClass = func.__class__.__name__
                # print(key, val, funcClass)
                if funcClass == 'TextCtrl':
                    func.SetValue(val)
                    infoData[index] = val
                elif funcClass == 'RadioButton':
                    val = val == 'True'
                    func.SetValue(val)
                    infoData[index] = val
                elif funcClass == 'CheckBox':
                    val = val == 'True'
                    func.SetValue(val)
                    infoData[index] = val
                elif funcClass == 'ComboBox':
                    func.SetValue(val)
                    infoData[index] = val
            else:
                func = InfoValue(val)
                info[index] = func
                infoData[index] = val
            # stdout.flush()
    except Exception as e:
        print(line, "readInfo error")
        print(e)
        stdout.flush()
    f.close()

def initInfo(key, val):
    global info
    if key in info:
        print("initInfo duplicate key %s" % (key))
        stdout.flush()
    info[key] = val

def newInfo(key, val):
    global info
    if key in info:
        print("newInfo duplicate key %s" % (key))
        stdout.flush()
    info[key] = InfoValue(val)
    infoData[key] = val

def setInfo(key, val):
    global info
    info[key].SetValue(val)
    infoData[key] = val

def setInfoData(key, val):
    global infoData
    infoData[key] = val

def getInfo(key):
    global info
    try:
        return(info[key].GetValue())
    except KeyError:
        print("getInfo KeyError %s" % (key))
    stdout.flush()
    return('')

def getInfoData(key):
    global infoData
    try:
        return(infoData[key])
    except KeyError:
        print("getInfo KeyError %s" % (key))
    stdout.flush()
    return('')

def getBoolInfo(key):
    global info
    try:
        # tmp = info[key].GetValue()
        # if tmp:
        val = infoData[key]
        if isinstance(val, bool):
            return(1 if val else 0)
        else:
            return(1 if val == 'True' else 0)
    except KeyError:
        print("getBoolInfo KeyError %s" % (key))
    stdout.flush()
    return(0)

def getFloatInfo(key):
    global info
    try:
        # val = info[key].GetValue()
        val = infoData[key]
        try:
            return(float(val))
        except ValueError:
            print("getFloatInfo ValueError key %d %s %s" % \
                  (key, configTable[key], val))
        except TypeError:
            print("getFloatInfo TypeError key %d %s %s" % \
                  (key, configTable[key], val))
    except KeyError:
        print("getFloatInfo KeyError %d" % (key))
    stdout.flush()
    return(0.0)

def getIntInfo(key):
    global info
    try:
        # val = info[key].GetValue()
        val = infoData[key]
        try:
            return(int(val))
        except ValueError as e:
            print("getIntInfo ValueError %s" % val)
            stdout.flush()
    except KeyError as e:
        print("getIntInfo KeyError %s" % (key))
        stdout.flush()
    return(0)

def infoSetLabel(key, val):
    info[key].SetLabel(val)

def getInitialInfo(key):
    global info
    try:
        tmp = info[key]
        return(tmp.GetValue() == 'True')
    except KeyError:
        print("getInitialInfo KeyError %s" % (key))
        stdout.flush()
return(False)
