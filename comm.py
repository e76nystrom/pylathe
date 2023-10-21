from ctypes import c_int32
from sys import stdout
from threading import Lock

import serial

from remParmDef import parmTable
# from configDef import cfgFpga
from remCmdDef import cmdTable, C_LOADMULTI, \
    C_LOADVAL, C_READVAL, C_LOADXREG, C_READXREG, C_QUEMOVE, C_MOVEMULTI, \
    C_MOVEQUESTATUS, C_SET_MEGA_VAL, C_READ_MEGA_VAL
from megaParmDef import parmTable as megaParmTable
    
CMD_OVERHEAD = 8
MOVE_OVERHEAD = 8
MAX_CMD_LEN = 80

class CommTimeout(Exception):
    pass

def getResult(rsp, index):
    result = rsp.split()
    print("getResult %s index %d %s" % (rsp, index, result))
    if index < len(result):
        retVal = int(result[index], 16)
        retVal = c_int32(retVal).value
        # if retVal & 0x80000000:
        #     retVal -= 0x100000000
        return retVal
    return 0

class Comm():
    def __init__(self):
        self.ser = None
        self.timeout = False
        self.commLock = Lock()

        self.xDbgPrint = True
        self.SWIG = False
        self.importLathe = True
        self.lastCmd = ''

        self.parmList = []
        self.cmdLen = CMD_OVERHEAD

        self.loadMulti = C_LOADMULTI
        self.loadVal = C_LOADVAL
        self.readVal = C_READVAL

        self.moveList = []
        self.moveLen = MOVE_OVERHEAD

        self.cmdTable = cmdTable
        self.parmTable = parmTable
        self.rpi = None
    def setDbgDispatch(self, _):
        pass

    def setPostUpdate(self, _):
        pass

    def setupCmds(self, loadMulti, loadVal, readVal):
        self.loadMulti = loadMulti
        self.loadVal = loadVal
        self.readVal = readVal

    def setupTables(self, cmdTbl, parmTbl):
        self.cmdTable = cmdTbl
        self.parmTable = parmTbl

    def enableXilinx(self):
        pass
        # from setup import xRegTable

    def openSerial(self, port, rate):
        if port is None or rate is None:
            return
        if (len(port) == 0) or (len(rate) == 0):
            return
        try:
            rate = int(rate)
        except ValueError:
            return
        try:
            self.ser = serial.Serial(port, rate, timeout=2)
        except IOError:
            print("unable to open port %s" % (port))
            stdout.flush()

    def closeSerial(self):
        if self.ser is not None:
            self.ser.close()
            self.ser = None

    def send(self, cmd):
        if cmd[1:3] != "2f":
            print("cmd", cmd.strip('\x01\r'))
        if self.ser is None:
            return
        self.commLock.acquire(True)
        self.ser.write(cmd.encode())
        rsp = self.ser.read(3).decode('utf8')
        if len(rsp) == 0:
            self.commLock.release()
            if not self.timeout:
                self.timeout = True
                print("timeout")
                stdout.flush()
            raise CommTimeout()

        length = int(rsp[1:3], 16)
        rsp += self.ser.read(length).decode('utf8')
        if rsp[3:5] != "2f":
            print("rsp", rsp)
        if rsp[-1] == '*':
            self.timeout = False
        self.commLock.release()
        return rsp

    def command(self, cmdVal, silent=False):
        if len(self.parmList) > 0:
            self.sendMulti()
        (cmd, action) = self.cmdTable[cmdVal]
        cmdStr = '\x01%x \r' % (cmdVal)
        if (not silent) and self.xDbgPrint:
            if cmd != self.lastCmd:
                self.lastCmd = cmd
                print("%-20s %s" % (cmd, cmdStr.strip('\x01\r')))
                stdout.flush()
        rsp = self.send(cmdStr)
        # print(rsp)
        return rsp.strip("\n\r")

    def encodeParm(self, parmIndex, val):
        cmdInfo = self.parmTable[parmIndex]
        parm = cmdInfo[0]
        parmType = cmdInfo[1]
        if parmType == 'float':
            try:
                valString = "%5.6f" % (float(val))
                valString = valString.rstrip('0')
            except ValueError:
                valString = "0.0"
                print("ValueError float queParm %s %s" % (parm, val))
                stdout.flush()
            except TypeError:
                valString = "0.0"
                print("TypeError float queParm %s %s" % (parm, val))
                stdout.flush()
        else:
            try:
                val = int(val)
                # if val < 10:
                #     valString = "%d" % (val)
                # else:
                valString = "%x" % (val)
            except ValueError:
                valString = "0"
                print("ValueError int queParm %s %s" % (parm, val))
                stdout.flush()
        return parm, valString

    def setParm(self, parmIndex, val):
        parm, valString = self.encodeParm(parmIndex, val)

        cmd = '\x01%x %x %s \r' % (self.loadVal, parmIndex, valString)
        if self.xDbgPrint:
            print("%-20s %s" % (parm, cmd.strip('\x01\r')))
            stdout.flush()

        self.send(cmd)

    def queParm(self, parmIndex, val):
        parm, valString = self.encodeParm(parmIndex, val)

        cmd = ' %x %s' % (parmIndex, valString)
        if self.xDbgPrint:
            print("%-20s %s" % (parm, cmd.strip()))
            stdout.flush()
        length = len(cmd)
        if self.cmdLen + length > 80:
            self.sendMulti()
        self.cmdLen += length
        self.parmList.append(cmd)

    def sendMulti(self):
        count = len(self.parmList)
        if count == 0:
            return
        cmd = '\x01%x %x' % (self.loadMulti, count)
        for parm in self.parmList:
            cmd += parm
        cmd += ' \r'
        if self.xDbgPrint:
            print("cmdLen %d len(cmd) %d" % (self.cmdLen, len(cmd)))
        self.parmList = []
        self.cmdLen = CMD_OVERHEAD
        if self.xDbgPrint:
            print("%-20s %s" % ('load multi', cmd.strip('\x01\r')))
            stdout.flush()
        self.send(cmd)

    def getParm(self, parmIndex, dbg=False):
        if self.ser is None:
            return(None)
        cmd = '\x01%x %x \r' % (self.readVal, parmIndex)
        if dbg:
            print("%-20s %s" % \
                  (self.parmTable[parmIndex], cmd.strip('\x01\r')), end="")
            stdout.flush()
        rsp = self.send(cmd)
        return getResult(rsp, 1)

    def getString(self, command, parm=None):
        if self.ser is None:
            return(None)
        arg = "" if parm is None else " %x" % parm
        cmd = '\x01%x%s \r' % (command, arg)
        cmdLen = len(cmd) - 1
        rsp = self.send(cmd)
        if len(rsp) <= 3:
            return ""
        return rsp[cmdLen]

    def setXRegN(self, reg, val):
        if self.ser is None:
            return
        val = int(val)
        if self.xDbgPrint:
            print("%-12s %2x %8x %12d" % ("", reg, val & 0xffffffff, val))
        cmd = '\x01%x %x %08x \r' % (C_LOADXREG, reg, val & 0xffffffff)
        if self.xDbgPrint:
            pass
        self.send(cmd)

    def getXReg(self, reg):
        if self.ser is None:
            return(0)
        cmd = '\x01%x %x \r' % (C_READXREG, reg)
        if self.xDbgPrint:
            pass
        rsp = self.send(cmd)
        return getResult(rsp, 2)

    def setMegaParm(self, parm, val):
        stdout.flush()
        val = int(val)
        if self.xDbgPrint:
            print("%-20s %4x %6d" % \
                  (megaParmTable[parm][0], val & 0xffffffff, val))
            stdout.flush()
        if self.ser is None:
            return
        cmd = '\x01%x %x %08x \r' % (C_SET_MEGA_VAL, parm, val & 0xffffffff)
        self.send(cmd)
    
    def readMegaParm(self, parm):
        if self.ser is None:
            return(0)
        cmd = '\x01%x %x \r' % (C_READ_MEGA_VAL, parm)
        if self.xDbgPrint:
            pass
        rsp = self.send(cmd)
        return getResult(rsp, 2)

    def moveCommand(self, opString, op, val):
        if isinstance(val, float):
            valStr = "%0.4f" % (val)
            prtStr = "%7.4f" % (val)
            valStr = valStr.rstrip('0')
        elif isinstance(val, int):
            valStr = "%x" % (val)
            prtStr = "%7x" % (val)
        elif isinstance(val, str):
            valStr = val
            prtStr = val
        else:
            print("sendMove val invalid type")
            stdout.flush()
            return

        cmd = '%x %s ' % (op, valStr)
        if self.xDbgPrint:
            print("cmd %-18s %6x %s" % (opString, op, prtStr))
            stdout.flush()
        return cmd

    def queMove(self, opString, op, val):
        cmd = self.moveCommand(opString, op, val)
        length = len(cmd)
        if (self.moveLen + length) > MAX_CMD_LEN:
            self.sendMultiMove()
        self.moveList.append(cmd)
        self.moveLen += len(cmd)

    def sendMove(self, opString, op, val):
        cmd = self.moveCommand(opString, op, val)
        cmd += "\x01%x %s \r" % (C_QUEMOVE, cmd)
        self.send(cmd)

    def sendMultiMove(self):
        count = len(self.moveList)
        if count == 0:
            return
        cmd = '\x01%x %x ' % (C_MOVEMULTI, count)
        for m in self.moveList:
            cmd += m
        cmd += '\r'
        if self.xDbgPrint:
            print("%-23s %s" % ('move multi', cmd.strip('\x01\r')))
            stdout.flush()
        self.send(cmd)
        self.moveList = []
        self.moveLen = MOVE_OVERHEAD

    def getQueueStatus(self):
        if self.ser is None:
            return(None)
        cmd = '\x01%x \r' % (C_MOVEQUESTATUS)
        rsp = self.send(cmd)
        return getResult(rsp, 1)
