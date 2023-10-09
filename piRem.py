#!/home/pi/p38/bin/python3

import socket
from socket import timeout
from threading import Thread
import spidev
import pickle
import lRegDef as rg
import fpgaLathe as bt
from time import time

# def ld(cmd, data, size, dbg=True):
#     s0 = rg.fpgaSizeTable[cmd]
#     if dbg:
#         print("ld %2d 0x%02x %d %10d %08x %s" % \
#               (cmd, cmd, s0, data, data&0xffffffff, rg.xRegTable[cmd]))
#     if spi is None:
#         return
#     data &= 0xffffffff
#     val = list(data.to_bytes(size, byteorder='big'))
#     msg = [cmd] + val
#     spi.xfer2(msg)

# def rd(cmd, dbg=False, ext=0x80000000, mask=0xffffffff):
#     global lastRdCmd, lastResult
#     if dbg:
#         if cmd != lastRdCmd:
#             print("rd %2d %s" % (cmd, rg.xRegTable[cmd]))
#             lastRdCmd = cmd
#     if spi is None:
#         return(0)
#     msg = [cmd]
#     spi.xfer2(msg)
#     val = spi.readbytes(4)
#     result = int.from_bytes(val, byteorder='big')
#     if result & ext:
#         result |= -1 & ~mask
#     if dbg:
#         if (cmd == rg.F_Rd_Status) and (result != lastResult):
#             print("status %08x" % result)
#             lastResult = result
#     # s0 = rg.fpgaSizeTable[cmd]
#     # if dbg:
#     #     print("ld 0x%02x %d %10d %08x %s" % \
#     #           (cmd, s0, result, result&0xffffffff, rg.xRegTable[cmd]), end=" ")
#     return(result)

FILTER_INPUT = True

RCV_IP = "192.168.42.65"
SEND_IP = "192.168.42.7"
UDP_PORT = 5555

def statusStr(status, txt):
    if status == 0:
        return ""

    sString = " "
    if (status & bt.zAxisEna) != 0:
        sString += "z Ena "
        sString += 'P' if (status & bt.zAxisCurDir) != 0 else 'N'
        sString += " "
    if (status & bt.zAxisDone) != 0:
        sString += "z Done "
    if (status & bt.xAxisEna) != 0:
        sString += "x Ena "
        sString += 'P' if (status & bt.xAxisCurDir) != 0 else 'N'
        sString += " "
    if (status & bt.xAxisDone) != 0:
        sString += "x Done "
    return sString

def axisCtlStr(axisCtl, axis):
    s = " " + axis + " "
    if (axisCtl & bt.ctlInit) != 0:
        s += "ctlInit "
    if (axisCtl & bt.ctlStart) != 0:
        s += "ctlStart "
        s += "P" if (axisCtl & bt.ctlDir) != 0 else "N"
        s += " "
    if (axisCtl & bt.ctlBacklash) != 0:
        s += "backlash "
    if (axisCtl & bt.ctlWaitSync) != 0:
        s += "waitSync "
    if (axisCtl & bt.ctlSetLoc) != 0:
        s += "setLoc "
    if (axisCtl & bt.ctlChDirect) != 0:
        s += "chDirect "
    if (axisCtl & bt.ctlSlave) != 0:
        s += "save "
    if (axisCtl & bt.ctlDroEnd) != 0:
        s += "droEnd "
    if (axisCtl & bt.ctlJogCmd) != 0:
        s += "jogCmd "
    if (axisCtl & bt.ctlJogMpg) != 0:
        s += "jogMpg "
    if (axisCtl & bt.ctlHome) != 0:
        s += "home "
    if (axisCtl & bt.ctlIgnoreLim) != 0:
        s += "ignoreLim "
    return s

def axisStatStr(axisStat, axis):
    s = " "
    if (axisStat & bt.axDoneDist) != 0:
        s += "doneDist"
    if (axisStat & bt.axDoneDro ) != 0:
        s += "doneDor"
    if (axisStat & bt.axDoneHome) != 0:
        s += "done Home"
    if (axisStat & bt.axDoneLimit) != 0:
        s += "done Limit"
    return s

zClkStr = ("zClkNone", "zClkZFreq", "zClkCh", "zClkIntClk", \
           "zClkFreq", "zClkXCh", "zClkSpindle", "zClkDbgFreq")

xClkStr = ("xClkNone", "xClkXFreq", "xClkCh", "xClkIntClk", \
           "xClkZFreq", "xClkZCh",  "xClkSpindle", "xClkDbgFreq")

def clkCtlStr(clkCtl, txt):
    s = " %s %s %s" % \
        (zClkStr[clkCtl & 7], xClkStr[(clkCtl >> 3) & 7],
         "dbgFreqEna" if (clkCtl & bt.clkDbgFreqEna) != 0 else "")
    return s

class Remote(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
        self.sock.bind((RCV_IP, UDP_PORT))

        self.last = [0 for i in range(len(rg.xRegTable))]
        if FILTER_INPUT:
            self.last[rg.F_Rd_Idx_Clks] = None
            self.last[rg.F_ZAxis_Base + rg.F_Sync_Base + rg.F_Rd_Dro] = None
            self.last[rg.F_XAxis_Base + rg.F_Sync_Base + rg.F_Rd_Dro] = None

        self.action = [None for i in range(len(rg.xRegTable))]
        self.action[rg.F_Rd_Status] = (statusStr, "")
        self.action[rg.F_Ld_Clk_Ctl] = (clkCtlStr, "")
        self.action[rg.F_ZAxis_Base + rg.F_Ld_Axis_Ctl] = (axisCtlStr, "zAxis")
        self.action[rg.F_XAxis_Base + rg.F_Ld_Axis_Ctl] = (axisCtlStr, "xAxis")
        self.action[rg.F_ZAxis_Base + rg.F_Rd_Axis_Status] = \
            (axisStatStr, "zAxis")
        self.action[rg.F_XAxis_Base + rg.F_Rd_Axis_Status] = \
            (axisStatStr, "xAxis")
        bus = 0
        device = 0
        self.spi = spidev.SpiDev()
        self.spi.open(bus, device)
        self.spi.max_speed_hz = 500000
        self.spi.mode = 0
        self.start()

    def run(self):
        lastTime = time()
        print("running")
        spi = self.spi
        sock = self.sock
        while True:
            # while True:
            #     try:
            #     except timeout:
            #         pass
            data, addr = self.sock.recvfrom(1024)
            msg = pickle.loads(data)
            cmd = msg[0]
            if (cmd & 0x100) == 0:
                data = int.from_bytes(msg[1:], byteorder='big', signed=True)
                # if cmd == (rg.F_ZAxis_Base + rg.F_Ld_Axis_Ctl):
                #     txt = axisCtlStr("zAxis", data)
                # elif cmd == (rg.F_XAxis_Base + rg.F_Ld_Axis_Ctl):
                #     txt = axisCtlStr("xAxis", data)
                # else:
                s0 = rg.fpgaSizeTable[cmd]
                action = self.action[cmd]
                if action is not None:
                    (func, actionStr) = action
                    txt = func(data, actionStr)
                else:
                    txt = ""
                t = time()
                delta = t - lastTime
                lastTime = t
                if delta > 2:
                    print()
                print("%8.3f ld %d %2d 0x%02x %10d 0x%08x %-32s%s" % \
                      (delta, len(msg), cmd, cmd, data, data&0xffffffff, \
                       rg.xRegTable[cmd], txt))
                spi.xfer2(msg)
            else:
                cmd &= 0xff
                msg = [cmd]
                spi.xfer2(msg)
                val = spi.readbytes(4)
                sock.sendto(pickle.dumps(val), addr)

                data = int.from_bytes(val, byteorder='big', signed=True)
                if self.last[cmd] is None:
                    continue
                if FILTER_INPUT:
                    if data == self.last[cmd]:
                         continue
                    self.last[cmd] = data
                # if cmd == rg.F_Rd_Status:
                #     txt = statusStr(data)
                # else:
                #     txt = ""
                t = time()

                txt = "%10d 0x%08x" % (data, data&0xffffffff)
                delta = t - lastTime
                lastTime = t
                action = self.action[cmd]
                if action is not None:
                    (func, actionStr) = action
                    txt += func(data, actionStr)
                s0 = rg.fpgaSizeTable[cmd]
                if delta > 2:
                    print()
                print("%8.3f rd %d %2d 0x%02x %21s %-32s->%s" % \
                      (delta, s0, cmd, cmd, "", \
                       rg.xRegTable[cmd], txt))

rem = Remote()
