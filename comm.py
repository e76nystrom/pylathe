from ctypes import c_int32
from sys import stdout
from threading import Lock

import serial

from remParmDef import parmTable
# from configDef import cfgFpga
from remCmdDef import cmdTable, LOADMULTI, \
    LOADVAL, READVAL, LOADXREG, READXREG, QUEMOVE, MOVEMULTI, \
    MOVEQUESTATUS, SET_MEGA_VAL, READ_MEGA_VAL
from megaParmDef import parmTable as megaParmTable
    
CMD_OVERHEAD = 8
MOVE_OVERHEAD = 8
MAX_CMD_LEN = 80

class CommTimeout(Exception):
    pass

def enableXilinx():
    pass
    # from setup import xRegTable

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

        self.loadMulti = LOADMULTI
        self.loadVal = LOADVAL
        self.readVal = READVAL

        self.moveList = []
        self.moveLen = MOVE_OVERHEAD

        self.cmdTable = cmdTable
        self.parmTable = parmTable

    def setupCmds(self, loadMulti, loadVal, readVal):
        self.loadMulti = loadMulti
        self.loadVal = loadVal
        self.readVal = readVal

    def setupTables(self, cmdTbl, parmTbl):
        self.cmdTable = cmdTbl
        self.parmTable = parmTbl

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
        if self.ser is None:
            return
        self.commLock.acquire(True)
        self.ser.write(cmd.encode())
        rsp = ""
        while True:
            tmp = self.ser.read(1).decode('utf8')
            if len(tmp) == 0:
                self.commLock.release()
                if not self.timeout:
                    self.timeout = True
                    print("timeout")
                    stdout.flush()
                raise CommTimeout()

            if tmp == '*':
                self.timeout = False
                break
            rsp = rsp + tmp
        self.commLock.release()
        return rsp

    def getResult(self, rsp, index):
        result = rsp.split()
        if len(result) > index:
            self.commLock.release()
            retVal = int(result[index], 16)
            retVal = c_int32(retVal).value
            # if retVal & 0x80000000:
            #     retVal -= 0x100000000
            return retVal
        return 0

    def command(self, cmdVal, silent=False):
        if len(self.parmList) > 0:
            self.sendMulti()
        (cmd, action) = self.cmdTable[cmdVal]
        # if self.SWIG and (action is not None):
        #     if self.importLathe:
        #         import lathe
        #         self.importLathe = False
        #     actionCmd = "lathe." + action + "()"
        #     eval(actionCmd)
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
        valString = "0"
        # if self.SWIG and (len(cmdInfo) == 3):
        #     if self.importLathe:
        #         import lathe
        #         self.importLathe = False
        #     parmVar = cmdInfo[2]
        #     if parmType == 'float':
        #         valString = "%5.6f" % (float(val))
        #     else:
        #         valString = "%d" % (int(val))
        #     cmd = "lathe.cvar.%s = %s" % (parmVar, valString)
        #     exec(cmd)
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
                if val < 10:
                    valString = "%d" % (val)
                else:
                    valString = "x%x" % (val)
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
            print("cmdlen %d len(cmd) %d" % (self.cmdLen, len(cmd)))
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
        return self.getResult(rsp, 2)

        # result = rsp.split()
        # if len(result) >= 3:
        #     try:
        #         retVal = int(result[2], 16)
        #         retVal = c_int32(retVal).value
        #     except ValueError:
        #         print("getParm error on %s" % (result))
        #         stdout.flush()
        #         retVal = 0
        #         if dbg:
        #             print("%08x" % (retVal))
        #             stdout.flush()
        #         return(retVal)

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

    # def setXReg(self, reg, val):
    #     if not (reg in xRegs):
    #         print("invalid register " + reg)
    #         stdout.flush()
    #         return
    #     val = int(val)
    #     if self.xDbgPrint:
    #         print("%-12s %2x %8x %12d" % \
    #               (reg, xRegs[reg], val & 0xffffffff, val))
    #         stdout.flush()
    #     if self.ser is None:
    #         return
    #     cmd = '\x01%x %x %08x \r' % (LOADXREG, xRegs[reg], val & 0xffffffff)
    #     self.send(cmd)

    def setXRegN(self, reg, val):
        if self.ser is None:
            return
        val = int(val)
        if self.xDbgPrint:
            print("%-12s %2x %8x %12d" % ("", reg, val & 0xffffffff, val))
        cmd = '\x01%x %x %08x \r' % (LOADXREG, reg, val & 0xffffffff)
        if self.xDbgPrint:
            pass
        self.send(cmd)

    def getXReg(self, reg):
        if self.ser is None:
            return(0)
        cmd = '\x01%x %x \r' % (READXREG, reg)
        if self.xDbgPrint:
            pass
        rsp = self.send(cmd)
        return self.getResult(rsp, 2)

        # result = rsp.split()
        # if len(result) == 3:
        #     val = int(result[2], 16)
        #     val = c_int32(val).value
        #     # if val & 0x80000000:
        #     #     val = -((val ^ 0xffffffff) + 1)
        #     self.commLock.release()
        #     return val
        # return 0

    # def dspXReg(self, reg, val, label=''):
    #     if self.xDbgPrint:
    #         print ("%-12s %2x %8x %12d %s" %
    #                (xRegTable[reg], reg, val & 0xffffffff, val, label))
    #     return(val)

    def setMegaParm(self, parm, val):
        stdout.flush()
        val = int(val)
        if self.xDbgPrint:
            print("%-20s %4x %6d" % \
                  (megaParmTable[parm][0], val & 0xffffffff, val))
            stdout.flush()
        if self.ser is None:
            return
        cmd = '\x01%x %x %08x \r' % (SET_MEGA_VAL, parm, val & 0xffffffff)
        self.send(cmd)
    
    def readMegaParm(self, parm):
        if self.ser is None:
            return(0)
        cmd = '\x01%x %x \r' % (READ_MEGA_VAL, parm)
        if self.xDbgPrint:
            pass
        rsp = self.send(cmd)
        return self.getResult(rsp, 2)

        # result = rsp.split()
        # if len(result) >= 3:
        #     val = int(result[2], 16)
        #     val = c_int32(val).value
        #     # if val & 0x80000000:
        #     #     val = -((val ^ 0xffffffff) + 1)
        #     self.commLock.release()
        #     return val
        # return 0

    def moveCommand(self, opString, op, val):
        if isinstance(val, float):
            valStr = "%0.4f" % (val)
            prtStr = "%7.4f" % (val)
        elif isinstance(val, int):
            valStr = "x%x" % (val)
            prtStr = "%7x" % (val)
        elif isinstance(val, str):
            valStr = val
            prtStr = val
        else:
            print("sendMove val invalid type")
            stdout.flush()
            return
        if '.' in valStr:
            valStr = valStr.rstrip('0')
        cmd = 'x%x %s ' % (op, valStr)
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
        cmd += "\x01%x %s \r" % (QUEMOVE, cmd)
        self.send(cmd)

    def sendMultiMove(self):
        count = len(self.moveList)
        if count == 0:
            return
        cmd = '\x01%x %x ' % (MOVEMULTI, count)
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
        cmd = '\x01%x \r' % (MOVEQUESTATUS)
        rsp = self.send(cmd)
        return self.getResult(rsp, 1)
