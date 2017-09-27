from __future__ import print_function
from sys import stdout

class InfoValue():
    def __init__(self, val):
        self.value = val

    def GetValue(self):
        val = self.value
        if isinstance(val, str):
            return(val)
        elif isinstance(val, float):
            return("%0.4f" % (val))
        elif isinstance(val, int):
            return(str(val))
        else:
            return("")

    def SetValue(self, val):
        self.value = val

class ConfigInfo():
    def __init__(self, configTable):
        self.info = []
        self.infoData = []
        self.configTable = configTable

    def clrInfo(self, size):
        info = [None for i in range(size)]
        self.infoData = [None for i in range(size)]

    def saveList(self, file, varList):
        f = open(file, 'w')
        for index in varList:
            name = self.configTable[index]
            val = self.info[index]
            str = self.formatConfig(name, val)
            if str != None:
                f.write(str)
        f.close()

    def saveInfo(self, file)
        f = open(file, 'w')
        for index, (val) in enumerate(info):
            name = self.configTable[index]
            str = self.formatConfig(name, val)
            if str != None:
                f.write(str)
        f.close()

    def updateFieldInfoData(self, fields):
        for (label, index, fmt) in fields:
            self.infoData[index] = self.info[index].GetValue()

    def updateFormatInfoData(self, formatList):
        for (index, fmt) in formatList:
            self.infoData[index] = self.info[index].GetValue()

    def formatConfig(self, name, val):
        valClass = val.__class__.__name__
        # print(name, valClass)
        # stdout.flush()
        if valClass == 'TextCtrl':
            return("%s=%s\n" % (name, val.GetValue()))
        elif valClass == 'RadioButton':
            return("%s=%s\n" % (name, val.GetValue()))
        elif valClass == 'CheckBox':
            return("%s=%s\n" % (name, val.GetValue()))
        elif valClass == 'ComboBox':
            return("%s=%s\n" % (name, val.GetValue()))
        elif valClass == 'InfoValue':
            return("%s=%s\n" % (name, val.GetValue()))
        else:
            return(None)

    def readInfo(self, file, config, configList=None):
        print("readInfo %s" % (file))
        stdout.flush()
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
                if self.info[index] != None:
                    func = self.info[index]
                    funcClass = func.__class__.__name__
                    # print(key, val, funcClass)
                    if funcClass == 'TextCtrl':
                        func.SetValue(val)
                        self.infoData[index] = val
                    elif funcClass == 'RadioButton':
                        val = val == 'True'
                        func.SetValue(val)
                        self.infoData[index] = val
                    elif funcClass == 'CheckBox':
                        val = val == 'True'
                        func.SetValue(val)
                        self.infoData[index] = val
                    elif funcClass == 'ComboBox':
                        func.SetValue(val)
                        self.infoData[index] = val
                else:
                    func = InfoValue(val)
                    self.info[index] = func
                    self.infoData[index] = val
                # stdout.flush()
        except Exception as e:
            print(line, "readInfo error")
            print(e)
            stdout.flush()
        f.close()

    def initInfo(self, index, val):
        if self.info[index] != None:
            print("initInfo duplicate index %s" % (index))
            stdout.flush()
        self.info[index] = val

    def newInfo(self, index, val):
        if self.info[index] != None:
            print("newInfo duplicate index %s" % (index))
            stdout.flush()
        self.info[index] = InfoValue(val)
        self.infoData[index] = val

    def getInfoInstance(self, index):
        try:
            return(self.info[index])
        except IndexError:
            print("getInfoInstance indexError %s" % (index))
        return(None)

    # info is used where infoData has not been updated

    def setInfo(self, index, val):
        self.info[index].SetValue(val)
        self.infoData[index] = val

    def getInfo(self, index):
        try:
            return(self.info[index].GetValue())
        except IndexError:
            print("getInfo IndexError %s" % (index))
        stdout.flush()
        return('')

    def getBoolInfo(self, index):
        try:
            val = self.infoData[index]
            if isinstance(val, bool):
                return(1 if val else 0)
            else:
                return(1 if val == 'True' else 0)
        except IndexError:
            print("getBoolInfo IndexError %s" % (index))
        stdout.flush()
        return(0)

    def getIntInfo(self, index):
        try:
            val = self.info[index].GetValue()
            try:
                return(int(val))
            except ValueError as e:
                print("getIntInfo ValueError index %d %s %s" % \
                      (index, self.configTable[index], val))
        except IndexError as e:
            print("getIntInfo IndexError %s" % (index))
        stdout.flush()
        return(0)

    def getFloatInfo(self, index):
        try:
            val = self.info[index].GetValue()
            try:
                return(float(val))
            except ValueError:
                print("getFloatInfo ValueError index %d %s %s" % \
                      (index, self.configTable[index], val))
            except TypeError:
                print("getFloatInfo TypeError index %d %s %s" % \
                      (index, self.configTable[index], val))
        except IndexError:
            print("getFloatInfo IndexError %d" % (index))
        stdout.flush()
        return(0.0)

    # infoData is used because calling info[index].GetValue will hang when
    # it is called from a non wx thread

    def setInfoData(self, index, val):
        self.infoData[index] = val

    def getInfoData(index):
        try:
            return(self.infoData[index])
        except IndexError:
            print("getInfoData IndexError %s" % (index))
        stdout.flush()
        return('')

    def getBoolInfoData(self, index):
        try:
            val = self.infoData[index]
            if isinstance(val, bool):
                return(1 if val else 0)
            else:
                return(1 if val == 'True' else 0)
        except IndexError:
            print("getBoolInfoData IndexError %s" % (index))
        stdout.flush()
        return(0)

    def getIntInfoData(self, index):
        try:
            val = self.infoData[index]
            try:
                return(int(val))
            except ValueError as e:
                print("getIntInfo ValueError index %d %s %s" % \
                      (index, self.configTable[index], val))
        except IndexError as e:
            print("getIntInfo IndexError %s" % (index))
        stdout.flush()
        return(0)

    def getFloatInfoData(self, index):
        try:
            val = self.infoData[index]
            try:
                return(float(val))
            except ValueError:
                print("getFloatInfoData ValueError index %d %s %s" % \
                      (index, self.configTable[index], val))
            except TypeError:
                print("getFloatInfo TypeError index %d %s %s" % \
                      (index, self.configTable[index], val))
        except IndexError:
            print("getFloatInfo IndexError %d" % (index))
        stdout.flush()
        return(0.0)

    def infoSetLabel(self, index, val):
        self.info[index].SetLabel(val)

    def getInitialBoolInfo(self, index):
        try:
            tmp = self.info[index]
            return(tmp.GetValue() == 'True')
        except IndexError:
            print("getInitialInfo IndexError %s" % (index))
            stdout.flush()
        return(False)
