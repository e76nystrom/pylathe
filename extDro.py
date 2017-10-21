from __future__ import print_function
from sys import stdout
from threading import Thread, Lock, Event
import serial

class DroTimeout(Exception):
    pass

class ExtDro():
    def __init__(self):
        self.dro = None
        self.timeout = False
        self.droLock = Lock()

        self.xDbgPrint = True

    def openSerial(self, port, rate):
        try:
            self.dro = serial.Serial(port, rate, timeout=.5)
        except IOError:
            print("unable to open port %s" % (port))
            stdout.flush()

    def initDro(self):
        pass

    def flush(self):
        data = False
        rsp = ""
        while True:
            tmp = self.dro.read(1)
            print(tmp, end='')
            if len(tmp) == 0:
                if data:
                    print()
                    stdout.flush()
                return(rsp)
            rsp += tmp
            data = True

    def command(self, cmd, response=False, delimiter='\n'):
        self.droLock.acquire(True)
        self.dro.write(cmd)
        rsp = ""
        while response:
            tmp = str(self.dro.read(1))
            if len(tmp) == 0:
                self.droLock.release()
                if not self.timeout:
                    self.timeout = True
                    # print("timeout %s" % (cmd))
                    # stdout.flush()
                    raise DroTimeout()
            self.timeout = False
            rsp = rsp + tmp
            if rsp.endswith(delimiter):
                break
        self.droLock.release()
        return(rsp)
        
