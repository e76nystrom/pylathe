from ctypes import c_int32
from sys import stdout
from threading import Lock

import enumDef as en
import lRegDef as rg

import serial

CMD_OVERHEAD = 8
MOVE_OVERHEAD = 8
MAX_CMD_LEN = 80

dbgFile = None
def trace(txt):
    global dbgFile
    if dbgFile is None:
        dbgFile = open("riscCmd.txt", "wb")
    dbgFile.write((txt + "\n").encode())
    dbgFile.flush()

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

class CommRiscv():
    def __init__(self, trace):
        self.ser = None
        self.timeout = False
        self.commLock = Lock()
        self.trace = trace

        self.xDbgPrint = True
        self.lastCmd = ''

        self.cmdLen = CMD_OVERHEAD

        self.cmdQue = []
        self.cmdLen = 0
        self.cmdStr = ""

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

    def send(self):
        if self.cmdLen == 0:
            return
        # if self.ser is None:
        #     return
        prefix = '\x01%02x' % (self.cmdLen + 1)
        cmd = prefix + self.cmdStr + '\r'
        print("cmdLen %d" % (len(cmd)))
        stdout.flush()
        trace(cmd.strip('\x01\r'))
        self.cmdLen = 0
        self.cmdStr = ""

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
        trace(rsp)
        print("rsp", rsp)
        if rsp[-1] == '*':
            self.timeout = False
        self.commLock.release()
        return rsp

    def command(self, cmd, arg=None):
        cmdStr = '%x' % (cmd)
        data = ""
        if arg is not None:
            argType = type(arg)
            if argType != tuple:
                cmdStr += " %x" % (arg)
            elif argType == tuple:
                for val in arg:
                    cmdStr += " %x" % (val)
                if cmd == en.R_SEND_ACCEL:
                    x0 = arg[0] >> 8
                    x1 = arg[0] & 0xff
                    data = "%10d %d %-10s %d %-14s" % \
                        (arg[1] ,x0, en.RiscvAccelTypeList[x0],
                         x1, en.RiscvSyncParmTypeList[x1])
            else:
                pass
        txt = "%-16s %-16s%s" % (en.selRiscvTypeList[cmd],
                                 cmdStr.strip('\x01\r'), data)
        cmdLen = len(cmdStr)
        if (self.cmdLen + cmdLen) < MAX_CMD_LEN:
            if self.cmdLen != 0:
                self.cmdStr += '|'
                self.cmdLen += 1
            self.cmdStr += cmdStr
            self.cmdLen += cmdLen
        else:
            self.send()
            self.cmdLen = cmdLen
            self.cmdStr = cmdStr
        trace(txt)
        self.trace(txt)
        print(txt)
        stdout.flush()
            
