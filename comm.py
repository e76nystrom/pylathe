from __future__ import print_function
from sys import stdout
from threading import Thread, Lock, Event
import serial

from setup import cmdTable, parmTable

ser = None
timeout = False
commLock = Lock()

# cmds = None
# parms = None
xRegs = None
xDbgPrint = True
SWIG = False
importLathe = True
lastCmd = ''

cmdOverhead = 8
parmList = []
cmdLen = cmdOverhead

def initGlobals(pyLathe):
    cmdTable = pyLathe('cmds')

def openSerial(port, rate):
    global ser
    try:
        ser = serial.Serial(port, 57600, timeout=1)
    except IOError:
        print("unable to open port") #, flush=True)
        stdout.flush()

class commTimeout(Exception):
    pass

def command(cmdVal):
    global SWIG, ser, cmdTable, commLock, timeout, xDbgPrint, \
        parmList, lastCmd
    if len(parmList) > 0:
        sendMulti()
    # (cmdVal, action) = cmds[cmd]
    (cmd, action) = cmdTable[cmdVal]
    if SWIG and (action != None):
        global importLathe
        if importLathe:
            import lathe
            importLathe = False
        actionCmd = "lathe." + action + "()"
        eval(actionCmd)
        # action()
    cmdStr = '\x01%x \r' % (cmdVal)
    if xDbgPrint:
        if cmd != lastCmd:
            lastCmd = cmd
            print("%-15s %s" % (cmd, cmdStr.strip('\x01\r'))) #, flush=True)
            stdout.flush()
    if ser is None:
        return(None);
    commLock.acquire(True)
    ser.write(str.encode(cmdStr))
    rsp = ""
    while True:
        tmp = str(ser.read(1))
        if (len(tmp) == 0):
            commLock.release()
            if not timeout:
                timeout = True
                print("timeout %s" % (cmd.strip('\x01\r'))) #, flush=True)
                stdout.flush()
            raise commTimeout()
            break
        if (tmp == '*'):
            timeout = False
            break
        rsp = rsp + tmp;
    commLock.release()
    return(rsp.strip("\n\r"))

def queParm(parmIndex, val):
    global parmTable, parmList, cmdLen
    # cmdInfo = parms[parm]
    # parmIndex = cmdInfo[0]
    cmdInfo = parmTable[parmIndex]
    parm = cmdInfo[0]
    parmType = cmdInfo[1]
    valString = "0"
    if SWIG and (len(cmdInfo) == 3):
        global importLathe
        if importLathe:
            import lathe
            importLathe = False
        parmVar = cmdInfo[2]
        if parmType == 'float':
            valString = "%5.6f" % (float(val))
        else:
            valString = "%d" % (int(val))
        cmd = "lathe.cvar.%s = %s" % (parmVar, valString)
        exec(cmd)
    if parmType == 'float':
        try:
            valString = "%5.6f" % (float(val))
            valString = valString.rstrip('0')
        except ValueError:
            valString = "0.0"
            print("ValueError queParm %s %s" % (parm, val)) #, flush=True)
            stdout.flush()
    else:
        try:
            val = int(val)
            if val < 10 :
                valString = "%d" % (val)
            else:
                valString = "x%x" % (val)
        except ValueError:
            valString = "0"
    cmd = ' %x %s' % (parmIndex, valString)
    if xDbgPrint:
        print("%-15s %s" % (parm, cmd.strip())) #, flush=True)
        stdout.flush()
    length = len(cmd)
    if cmdLen + length > 80:
        sendMulti()
    cmdLen += length
    parmList.append(cmd)

def sendMulti():
    global ser, parmList, cmdLen, cmdOverhead, cmds, commLock, timeout
    count = len(parmList)
    if count == 0:
        return
    # cmd = '\x01%x %x' %  (cmds['LOADMULTI'][0], count)
    cmd = '\x01%x %x' %  (LOADMULTI, count)
    for parm in parmList:
        cmd += parm
    cmd += ' \r';
    if xDbgPrint:
        print("cmdlen %d len(cmd) %d" % (cmdLen, len(cmd)))
    parmList = []
    cmdLen = cmdOverhead
    if xDbgPrint:
        print("%-15s %s" % ('LOADMULTI', cmd.strip('\x01\r'))) #, flush=True)
        stdout.flush()
    if ser is None:
        return
    commLock.acquire(True)
    ser.write(cmd)
    rsp = "";
    while True:
        tmp = ser.read(1)
        if (len(tmp) == 0):
            commLock.release()
            if not timeout:
                timeout = True
                print("setParm timeout %s" % (parm)) #, flush=True)
                stdout.flush()
            raise commTimeout()
            break;
        if (tmp == '*'):
            timeout = False
            break
        rsp = rsp + tmp
    commLock.release()

def setParm(parmIndex, val):
    global ser, parmTable, cmds, commLock, timeout, xDbgPrint
    # cmdInfo = parms[parm]
    # parmIndex = cmdInfo[0]
    cmdInfo = parmTable[parmIndex]
    parm = cmdInfo[0]
    parmType = cmdInfo[1]
    valString = "0"
    if SWIG and (len(cmdInfo) == 3):
        global importLathe
        if importLathe:
            import lathe
            importLathe = False
        parmVar = cmdInfo[2]
        if parmType == 'float':
            valString = "%5.6f" % (float(val))
        else:
            valString = "%d" % (int(val))
        cmd = "lathe.cvar.%s = %s" % (parmVar, valString)
        exec(cmd)
    if parmType == 'float':
        try:
            valString = "%5.6f" % (float(val))
            valString = valString.rstrip('0')
        except ValueError:
            valString = "0.0"
            print("ValueError setParm %s %s" % (parm, val)) #, flush=True)
            stdout.flush()
    else:
        try:
            valString = "x%x" % (int(val))
        except ValueError:
            valString = "0"
    # cmd = '\x01%x %x %s \r' % (cmds['LOADVAL'][0], parmIndex, valString)
    cmd = '\x01%x %x %s \r' % (LOADVAL, parmIndex, valString)
    if xDbgPrint:
        print("%-15s %s" % (parm, cmd.strip('\x01\r'))) #, flush=True)
        stdout.flush()
    if ser is None:
        return
    commLock.acquire(True)
    ser.write(cmd)
    rsp = "";
    while True:
        tmp = ser.read(1)
        if (len(tmp) == 0):
            commLock.release()
            if not timeout:
                timeout = True
                print("setParm timeout %s" % (parm)) #, flush=True)
                stdout.flush()
            raise commTimeout()
            break;
        if (tmp == '*'):
            timeout = False
            break
        rsp = rsp + tmp
    commLock.release()

def getParm(parmIndex, dbg=False):
    global ser, commLock, timeout
    if ser is None:
        return(None)
    # cmd = '\x01%x %x \r' % (cmds['READVAL'][0], parms[parm][0])
    cmd = '\x01%x %x \r' % (READVAL, parmIndex)
    if dbg:
        print("%-15s %s " % (parm, cmd.strip('\x01\r')), end="")
    commLock.acquire(True)
    ser.write(cmd)
    rsp = "";
    while True:
        tmp = ser.read(1)
        if len(tmp) == 0:
            commLock.release()
            if not timeout:
                timeout = True
                print("getParm timeout %s" % (parm)) #, flush=True)
                stdout.flush()
            raise commTimeout()
            break;
        if tmp == '*':
            timeout = False
            result = rsp.split()
            if len(result) == 3:
                commLock.release()
                try:
                    retVal = int(result[2], 16)
                except:
                    print("getParm error on %s" % (result)) #, flush=True)
                    stdout.flush()
                    retVal = 0
                if retVal & 0x80000000:
                    retVal -= 0x100000000
                if dbg:
                    print("%08x" % (retVal)) #, flush=True)
                    stdout.flush()
                return(retVal)
        rsp = rsp + tmp;
    commLock.release()

def getString():
    global ser, commLock, timeout
    if ser is None:
        return(None)
    # cmd = '\x01%x \r' % (cmds['READDBG'][0])
    cmd = '\x01%x \r' % (READDBG)
    commLock.acquire(True)
    ser.write(cmd)
    rsp = "";
    while True:
        tmp = ser.read(1)
        if len(tmp) == 0:
            commLock.release()
            if not timeout:
                timeout = True
                print("getString timeout") #, flush=True)
                stdout.flush()
            raise commTimeout()
            break;
        if tmp == '*':
            commLock.release()
            timeout = False
            if len(rsp) <= 3:
                return ""
            return(rsp[4:])
        rsp = rsp + tmp;
    commLock.release()

def setXReg(reg, val):
    global ser, xRegs, comLock, timeout, xDbgPrint
    if not (reg in xRegs):
        print("invalid register " + reg) #, flush=True)
        stdout.flush()
        return
    val = int(val)
    if xDbgPrint:
        print("%-12s %2x %8x %12d" % \
              (reg, xRegs[reg], val & 0xffffffff, val)) #, flush=True)
        stdout.flush()
    if ser is None:
        return
    # cmd = '\x01%x %x %08x \r' % (cmds['LOADXREG'][0], xRegs[reg], \
    #                            val & 0xffffffff)
    cmd = '\x01%x %x %08x \r' % (LOADXREG, xRegs[reg], val & 0xffffffff)
    commLock.acquire(True)
    ser.write(cmd)
    rsp = "";
    while True:
        tmp = ser.read(1)
        if len(tmp) == 0:
            commLock.release()
            if not timeout:
                timeout = True
                print("timeout")
            raise commTimeout
            break;
        if (tmp == '*'):
            timeout = False
            break
        rsp = rsp + tmp;
    commLock.release()

def setXRegN(reg, val):
    global ser, xRegs, comLock, timeout, xDbgPrint
    if ser is None:
        return
    val = int(val)
    if xDbgPrint:
        print("%-12s %2x %8x %12d" % ("", reg, val & 0xffffffff, val))
    # cmd = '\x01%x %x %08x \r' % (cmds['LOADXREG'][0], reg, \
    #                            val & 0xffffffff)
    cmd = '\x01%x %x %08x \r' % (LOADXREG, reg, val & 0xffffffff)
    commLock.acquire(True)
    ser.write(cmd)
    rsp = "";
    while True:
        tmp = ser.read(1)
        if len(tmp) == 0:
            commLock.release()
            if not timeout:
                timeout = True
                print("timeout")
            raise commTimeout
            break;
        if (tmp == '*'):
            timeout = False
            break
        rsp = rsp + tmp;
    commLock.release()

def getXReg(reg):
    global ser, xRegs, commLock, timeout
    if ser is None:
        return(0)
    if not (reg in xRegs):
        print("invalid register " + reg)
        return(0);
    # cmd = '\x01%x %x \r' % (cmds['READXREG'][0], xRegs[reg])
    cmd = '\x01%x %x \r' % (READXREG, xRegs[reg])
    commLock.acquire(True)
    ser.write(cmd)
    rsp = "";
    while True:
        tmp = ser.read(1)
        if (len(tmp) == 0):
            commLock.release()
            if not timeout:
                timeout = True
                print("timeout")
            raise commTimeout
            break;
        if (tmp == '*'):
            timeout = False
            result = rsp.split()
            if (len(result) == 3):
                val = int(result[2], 16)
                if val & 0x80000000:
                    val = -((val ^ 0xffffffff) + 1)
                commLock.release()
                return(val)
        rsp = rsp + tmp;


def dspXReg(reg, label=''):
    val = getXReg(reg)
    global xRegs, xDbgPrint
    if xDbgPrint:
        print ("%-12s %2x %8x %12d %s" %
               (reg, xRegs[reg], val & 0xffffffff, val, label))
    return(val)

def sendMove(opString, op, val):
    global ser, commLock, timeout
    if isinstance(val, float):
        valStr = "%0.4f" % (val)
        prtStr = "%7.4f" % (val)
    elif isinstance(val, int):
        valStr = "x%x" % (val)
        prtStr = "%7x" % (val)
    elif isinstance(val, str):
        valStr = val
        prtStr = str
    else:
        print("sendMove val invalid type") #, flush=True)
        stdout.flush()
        return
    # cmd = '\x01%x x%x %s \r' % (cmds['QUEMOVE'][0], op, valStr)
    cmd = '\x01%x x%x %s \r' % (QUEMOVE, op, valStr)
    if xDbgPrint:
        print("cmd %-14s %3x %s" % (opString, op, prtStr)) #, flush=True)
        stdout.flush()
    if ser is None:
        return
    commLock.acquire(True)
    ser.write(cmd)
    rsp = "";
    while True:
        tmp = ser.read(1)
        if (len(tmp) == 0):
            commLock.release()
            if not timeout:
                timeout = True
                print("sendMove timeout") #, flush=True)
                stdout.flush()
            raise commTimeout()
            break;
        if (tmp == '*'):
            timeout = False
            break
        rsp = rsp + tmp
    commLock.release()

def getQueueStatus():
    global ser, commLock, timeout
    if ser is None:
        return(None)
    # cmd = '\x01%x \r' % (cmds['MOVEQUESTATUS'][0])
    cmd = '\x01%x \r' % (MOVEQUESTATUS)
    commLock.acquire(True)
    ser.write(cmd)
    rsp = "";
    while True:
        tmp = ser.read(1)
        if (len(tmp) == 0):
            commLock.release()
            if not timeout:
                timeout = True
                print("getQueStatus timeout") #, flush=True)
                stdout.flush()
            raise commTimeout()
            break;
        if (tmp == '*'):
            timeout = False
            result = rsp.split()
            if (len(result) == 2):
                commLock.release()
                retVal = int(result[1], 16)
                if retVal & 0x80000000:
                    retVal -= 0x100000000
                return(retVal)
        rsp = rsp + tmp;
    commLock.release()
