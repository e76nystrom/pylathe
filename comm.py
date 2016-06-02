from sys import stdout
from threading import Thread, Lock, Event
import serial

ser = None
timeout = False
commLock = Lock()

cmds = None
parms = None
xRegs = None
xDbgPrint = True
SWIG = False
importLathe = True

def openSerial(port, rate):
    global ser
    try:
        ser = serial.Serial(port, 57600, timeout=1)
    except IOError:
        print "unable to open port"
        stdout.flush()

class commTimeout(Exception):
    pass

def command(cmd):
    global SWIG, ser, cmds, commLock, timeout, xDbgPrint
    (cmdVal, action) = cmds[cmd]
    if SWIG and (action != None):
        global importLathe
        if importLathe:
            import lathe
            importLathe = False
        actionCmd = "lathe." + action + "()"
        eval(actionCmd)
        # action()
    cmdStr = '\x01%x ' % (cmdVal)
    if xDbgPrint:
        print "%-15s %s" % (cmd, cmdStr)
        stdout.flush()
    if ser is None:
        return(None);
    commLock.acquire(True)
    ser.write(cmdStr)
    rsp = ""
    while True:
        tmp = ser.read(1)
        if (len(tmp) == 0):
            commLock.release()
            if not timeout:
                timeout = True
                print "timeout %s" % (cmd)
                stdout.flush()
            raise commTimeout()
            break
        if (tmp == '*'):
            timeout = False
            break
        rsp = rsp + tmp;
    commLock.release()
    return(rsp.strip("\n\r"))

def setParm(parm, val):
    global ser, parms, cmds, commLock, timeout, xDbgPrint
    cmdInfo = parms[parm]
    parmIndex = cmdInfo[0]
    parmType = cmdInfo[1]
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
            print "ValueError %s" % (val)
            stdout.flush()
    else:
        valString = "x%x" % (int(val))
    cmd = '\x01%x %x %s ' % (cmds['LOADVAL'][0], parmIndex, valString)
    if True: # xDbgPrint:
        print "%-15s %s" % (parm, cmd)
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
                print "setParm timeout %s" % (parm)
                stdout.flush()
            raise commTimeout()
            break;
        if (tmp == '*'):
            timeout = False
            break
        rsp = rsp + tmp
    commLock.release()

def getParm(parm):
    global ser, cmds, parms, commLock, timeout
    if ser is None:
        return(None)
    cmd = '\x01%x %x ' % (cmds['READVAL'][0], parms[parm][0])
    commLock.acquire(True)
    ser.write(cmd)
    rsp = "";
    while True:
        tmp = ser.read(1)
        if len(tmp) == 0:
            commLock.release()
            if not timeout:
                timeout = True
                print "getParm timeout %s" % (parm)
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
                    print "getParm error on %s" % (result)
                    stdout.flush()
                    retVal = 0
                if retVal & 0x80000000:
                    retVal -= 0x100000000
                return(retVal)
        rsp = rsp + tmp;
    commLock.release()

def getString():
    global ser, cmds, parms, commLock, timeout
    if ser is None:
        return(None)
    cmd = '\x01%x ' % (cmds['READDBG'][0])
    commLock.acquire(True)
    ser.write(cmd)
    rsp = "";
    while True:
        tmp = ser.read(1)
        if len(tmp) == 0:
            commLock.release()
            if not timeout:
                timeout = True
                print "getString timeout"
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
    global ser, xRegs, cmds, comLock, timeout, xDbgPrint
    if not (reg in xRegs):
        print "invalid register " + reg
        stdout.flush()
        return
    val = int(val)
    if xDbgPrint:
        print "%-12s %2x %8x %12d" % (reg, xRegs[reg], val & 0xffffffff, val)
        stdout.flush()
    if ser is None:
        return
    cmd = '\x01%x %x %08x ' % (cmds['LOADXREG'][0], xRegs[reg], \
                               val & 0xffffffff)
    commLock.acquire(True)
    ser.write(cmd)
    rsp = "";
    while True:
        tmp = ser.read(1)
        if len(tmp) == 0:
            commLock.release()
            if not timeout:
                timeout = True
                print "timeout"
            raise commTimeout
            break;
        if (tmp == '*'):
            timeout = False
            break
        rsp = rsp + tmp;
    commLock.release()

def setXRegN(reg, val):
    global ser, xRegs, cmds, comLock, timeout, xDbgPrint
    if ser is None:
        return
    val = int(val)
    if xDbgPrint:
        print "%-12s %2x %8x %12d" % ("", reg, val & 0xffffffff, val)
    cmd = '\x01%x %x %08x ' % (cmds['LOADXREG'][0], reg, \
                               val & 0xffffffff)
    commLock.acquire(True)
    ser.write(cmd)
    rsp = "";
    while True:
        tmp = ser.read(1)
        if len(tmp) == 0:
            commLock.release()
            if not timeout:
                timeout = True
                print "timeout"
            raise commTimeout
            break;
        if (tmp == '*'):
            timeout = False
            break
        rsp = rsp + tmp;
    commLock.release()

def getXReg(reg):
    global ser, xRegs, cmds, commLock, timeout
    if ser is None:
        return(0)
    if not (reg in xRegs):
        print "invalid register " + reg
        return(0);
    cmd = '\x01%x %x ' % (cmds['READXREG'][0], xRegs[reg])
    commLock.acquire(True)
    ser.write(cmd)
    rsp = "";
    while True:
        tmp = ser.read(1)
        if (len(tmp) == 0):
            commLock.release()
            if not timeout:
                timeout = True
                print "timeout"
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

def sendMove(op, val):
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
        print "sendMove val invalid type"
        stdout.flush()
        return
    cmd = '\x01%x x%x %s ' % (cmds['SENDMOVE'][0], op, valStr)
    if xDbgPrint:
        print "cmd %3x %s" % (op, prtStr)
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
                print "sendMove timeout"
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
    cmd = '\x01%x ' % (cmds['MOVEQUESTATUS'][0])
    commLock.acquire(True)
    ser.write(cmd)
    rsp = "";
    while True:
        tmp = ser.read(1)
        if (len(tmp) == 0):
            commLock.release()
            if not timeout:
                timeout = True
                print "getQueStatus timeout"
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
