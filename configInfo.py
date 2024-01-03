from sys import stdout
import wx

from configDef import CFG_STR_LEN
from comboBox import ComboBox

class InfoValue():
    def __init__(self, val):
        self.SetValue(val)

    def GetValue(self):
        val = self.value
        if isinstance(val, str):
            return(val)
        elif isinstance(val, float):
            return("%0.4f" % (val))
        elif isinstance(val, int):
            return(str(val))
        elif isinstance(val, bool):
            return(val)
        else:
            return("")

    def SetValue(self, val):
        if val == "True":
            self.value = True
        elif val == "False":
            self.value = False
        else:
            self.value = val
        return(self.value)

class ConfigInfo():
    def __init__(self, configTable):
        self.info = []
        self.infoData = []
        self.configTable = configTable
        self.maxLen = CFG_STR_LEN

    def clrInfo(self, size):
        self.info = [None for _ in range(size)]
        self.infoData = [None for _ in range(size)]

    def saveList(self, file, varList):
        cfgFormat = "%-" + str(self.maxLen) + "s = %s\n"
        f = open(file, 'wb')
        for index in varList:
            name = self.configTable[index]
            val = self.info[index]
            saveVal = self.readConfig(name, val)
            string = cfgFormat % (name, saveVal)
            if string is not None:
                f.write(string.encode())
        f.close()

    def saveInfo(self, file):
        cfgFormat = "%-" + str(self.maxLen) + "s = %s\n"
        f = open(file, 'wb')
        for index, (val) in enumerate(self.info):
            name = self.configTable[index]
            saveVal = self.readConfig(name, val)
            string = cfgFormat % (name, saveVal)
            if string is not None:
                f.write(string.encode())
        f.close()

    def updateFieldInfoData(self, fields):
        for (label, index, fmt) in fields:
            self.infoData[index] = self.info[index].GetValue()

    def updateFormatInfoData(self, formatList):
        for (index, fmt) in formatList:
            self.infoData[index] = self.info[index].GetValue()

    @staticmethod
    def readConfig(name, val):
        # valClass = val.__class__.__name__
        if isinstance(val, wx.TextCtrl):
            result = val.GetValue()
        elif isinstance(val, wx.RadioButton):
            result = val.GetValue()
        elif isinstance(val, wx.CheckBox):
            result = val.GetValue()
        elif isinstance(val, ComboBox):
            result = val.GetValue()
        elif isinstance(val, InfoValue):
            result = val.GetValue()
        else:
            result = None
        # print(f"{name:<20} {valClass:<14} {str(result)}")
        # stdout.flush()
        return result

    def readInfo(self, file, config, configList=None):
        print("readInfo %s" % (file))
        stdout.flush()
        line = 0
        try:
            f = open(file, 'r')
            for line in f:
                line = line.rstrip()
                if len(line) == 0:
                    continue
                [key, val] = line.split('=')
                key = key.strip()
                val = val.strip()
                if not key in config:
                    print("readInfo invalid config value %s" % key)
                    stdout.flush()
                    continue
                index = config[key]
                if configList is not None:
                    if not index in configList:
                        continue
                if self.info[index] is not None:
                    func = self.info[index]
                    # funcClass = func.__class__.__name__
                    # print(key, val, funcClass)
                    if isinstance(func, wx.TextCtrl):
                        func.SetValue(val)
                        self.infoData[index] = val
                    elif isinstance(func, wx.RadioButton):
                        val = val == 'True'
                        func.SetValue(val)
                        self.infoData[index] = val
                    elif isinstance(func, wx.CheckBox):
                        val = val == 'True'
                        func.SetValue(val)
                        self.infoData[index] = val
                    elif isinstance(func, ComboBox):
                        func.SetValue(val)
                        self.infoData[index] = val
                    elif isinstance(func, InfoValue):
                        self.infoData[index] = func.SetValue(val)
                else:
                    func = InfoValue(val)
                    self.info[index] = func
                    self.infoData[index] = func.GetValue()
                # stdout.flush()
            f.close()
        except Exception as e:
            print(line, "readInfo error")
            print(e)
            stdout.flush()

    def initInfo(self, index, obj):
        if self.info[index] is not None:
            pass
            # print("initInfo duplicate index %3d %s" %
            #       (index, self.configTable[index]))
            # stdout.flush()
        # funcClass = obj.__class__.__name__
        # print(f"initInfo {index:3d} {self.configTable[index]:<20} " \
        #       f"{funcClass}")
        self.info[index] = obj

    def newInfo(self, index, val):
        if self.info[index] is not None:
            print("newInfo duplicate index %d %s" %
                  (index, self.configTable[index]))
            stdout.flush()
        # print(f"newInfo {index:3d} {self.configTable[index]:<20}")
        self.info[index] = info = InfoValue(val)
        self.infoData[index] = val
        return(info)

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
            except ValueError:
                print("getIntInfo ValueError index %d %s %s" % \
                      (index, self.configTable[index], val))
            except TypeError:
                print("getIntInfo TypeError index %d %s %s" % \
                      (index, self.configTable[index], val))
        except IndexError:
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

    def getInfoData(self, index):
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
            except ValueError:
                print("getIntInfoData ValueError index %d %s %s" % \
                      (index, self.configTable[index], val))
            except TypeError:
                print("getIntInfoData TypeError index %d %s %s" % \
                      (index, self.configTable[index], val))
        except IndexError:
            print("getIntInfo IndexError %s" % (index))
        stdout.flush()
        return(0)

    def getFloatInfoData(self, index):
        try:
            val = self.infoData[index]
            if val == "None":
                val = 0.0
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

    def getDistInfoData(self, index, digits=None):
        try:
            val = self.infoData[index]
            val = val.lower()
            metric = val.endswith('mm')
            if metric:
                val = val[:-2]
            try:
                val = float(val)
                if metric:
                    val /= 25.4
                    if digits is not None:
                        fmt = "%%0.%df" % (digits,)
                        val = fmt % (val,)
                return(val)
            except ValueError:
                print("getDistInfoData ValueError index %d %s %s" % \
                      (index, self.configTable[index], val))
            except TypeError:
                print("getDistInfo TypeError index %d %s %s" % \
                      (index, self.configTable[index], val))
        except IndexError:
            print("getDistInfo IndexError %d" % (index))
        stdout.flush()
        return(0.0)

    def infoSetLabel(self, index, val):
        self.info[index].SetLabel(val)

    def getInitialBoolInfo(self, index):
        try:
            tmp = self.info[index]
            if tmp is not None:
                return(tmp.GetValue() == 'True')
        except IndexError:
            print("getInitialInfo IndexError %s" % (index))
            stdout.flush()
        return(False)
