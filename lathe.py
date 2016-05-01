# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.7
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_lathe', [dirname(__file__)])
        except ImportError:
            import _lathe
            return _lathe
        if fp is not None:
            try:
                _mod = imp.load_module('_lathe', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _lathe = swig_import_helper()
    del swig_import_helper
else:
    import _lathe
del version_info
try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.


def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr_nondynamic(self, class_type, name, static=1):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    if (not static):
        return object.__getattr__(self, name)
    else:
        raise AttributeError(name)

def _swig_getattr(self, class_type, name):
    return _swig_getattr_nondynamic(self, class_type, name, 0)


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object:
        pass
    _newclass = 0



_lathe.INCLUDE_swigconstant(_lathe)
INCLUDE = _lathe.INCLUDE

_lathe.DBG_P_swigconstant(_lathe)
DBG_P = _lathe.DBG_P

_lathe.DBG_SETUP_swigconstant(_lathe)
DBG_SETUP = _lathe.DBG_SETUP

_lathe.JTIMEINITIAL_swigconstant(_lathe)
JTIMEINITIAL = _lathe.JTIMEINITIAL

_lathe.JTIMEINC_swigconstant(_lathe)
JTIMEINC = _lathe.JTIMEINC

_lathe.JTIMEMAX_swigconstant(_lathe)
JTIMEMAX = _lathe.JTIMEMAX
class T_AXIS(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, T_AXIS, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, T_AXIS, name)
    __repr__ = _swig_repr
    __swig_setmethods__["pitch"] = _lathe.T_AXIS_pitch_set
    __swig_getmethods__["pitch"] = _lathe.T_AXIS_pitch_get
    if _newclass:
        pitch = _swig_property(_lathe.T_AXIS_pitch_get, _lathe.T_AXIS_pitch_set)
    __swig_setmethods__["ratio"] = _lathe.T_AXIS_ratio_set
    __swig_getmethods__["ratio"] = _lathe.T_AXIS_ratio_get
    if _newclass:
        ratio = _swig_property(_lathe.T_AXIS_ratio_get, _lathe.T_AXIS_ratio_set)
    __swig_setmethods__["microSteps"] = _lathe.T_AXIS_microSteps_set
    __swig_getmethods__["microSteps"] = _lathe.T_AXIS_microSteps_get
    if _newclass:
        microSteps = _swig_property(_lathe.T_AXIS_microSteps_get, _lathe.T_AXIS_microSteps_set)
    __swig_setmethods__["motorSteps"] = _lathe.T_AXIS_motorSteps_set
    __swig_getmethods__["motorSteps"] = _lathe.T_AXIS_motorSteps_get
    if _newclass:
        motorSteps = _swig_property(_lathe.T_AXIS_motorSteps_get, _lathe.T_AXIS_motorSteps_set)
    __swig_setmethods__["accel"] = _lathe.T_AXIS_accel_set
    __swig_getmethods__["accel"] = _lathe.T_AXIS_accel_get
    if _newclass:
        accel = _swig_property(_lathe.T_AXIS_accel_get, _lathe.T_AXIS_accel_set)
    __swig_setmethods__["backlash"] = _lathe.T_AXIS_backlash_set
    __swig_getmethods__["backlash"] = _lathe.T_AXIS_backlash_get
    if _newclass:
        backlash = _swig_property(_lathe.T_AXIS_backlash_get, _lathe.T_AXIS_backlash_set)
    __swig_setmethods__["stepsInch"] = _lathe.T_AXIS_stepsInch_set
    __swig_getmethods__["stepsInch"] = _lathe.T_AXIS_stepsInch_get
    if _newclass:
        stepsInch = _swig_property(_lathe.T_AXIS_stepsInch_get, _lathe.T_AXIS_stepsInch_set)
    __swig_setmethods__["backlashSteps"] = _lathe.T_AXIS_backlashSteps_set
    __swig_getmethods__["backlashSteps"] = _lathe.T_AXIS_backlashSteps_get
    if _newclass:
        backlashSteps = _swig_property(_lathe.T_AXIS_backlashSteps_get, _lathe.T_AXIS_backlashSteps_set)

    def __init__(self):
        this = _lathe.new_T_AXIS()
        try:
            self.this.append(this)
        except:
            self.this = this
    __swig_destroy__ = _lathe.delete_T_AXIS
    __del__ = lambda self: None
T_AXIS_swigregister = _lathe.T_AXIS_swigregister
T_AXIS_swigregister(T_AXIS)

class T_ACCEL(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, T_ACCEL, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, T_ACCEL, name)
    __repr__ = _swig_repr
    __swig_setmethods__["minSpeed"] = _lathe.T_ACCEL_minSpeed_set
    __swig_getmethods__["minSpeed"] = _lathe.T_ACCEL_minSpeed_get
    if _newclass:
        minSpeed = _swig_property(_lathe.T_ACCEL_minSpeed_get, _lathe.T_ACCEL_minSpeed_set)
    __swig_setmethods__["maxSpeed"] = _lathe.T_ACCEL_maxSpeed_set
    __swig_getmethods__["maxSpeed"] = _lathe.T_ACCEL_maxSpeed_get
    if _newclass:
        maxSpeed = _swig_property(_lathe.T_ACCEL_maxSpeed_get, _lathe.T_ACCEL_maxSpeed_set)
    __swig_setmethods__["accel"] = _lathe.T_ACCEL_accel_set
    __swig_getmethods__["accel"] = _lathe.T_ACCEL_accel_get
    if _newclass:
        accel = _swig_property(_lathe.T_ACCEL_accel_get, _lathe.T_ACCEL_accel_set)
    __swig_setmethods__["pitch"] = _lathe.T_ACCEL_pitch_set
    __swig_getmethods__["pitch"] = _lathe.T_ACCEL_pitch_get
    if _newclass:
        pitch = _swig_property(_lathe.T_ACCEL_pitch_get, _lathe.T_ACCEL_pitch_set)
    __swig_setmethods__["stepsInch"] = _lathe.T_ACCEL_stepsInch_set
    __swig_getmethods__["stepsInch"] = _lathe.T_ACCEL_stepsInch_get
    if _newclass:
        stepsInch = _swig_property(_lathe.T_ACCEL_stepsInch_get, _lathe.T_ACCEL_stepsInch_set)
    __swig_setmethods__["taper"] = _lathe.T_ACCEL_taper_set
    __swig_getmethods__["taper"] = _lathe.T_ACCEL_taper_get
    if _newclass:
        taper = _swig_property(_lathe.T_ACCEL_taper_get, _lathe.T_ACCEL_taper_set)
    __swig_setmethods__["taperInch"] = _lathe.T_ACCEL_taperInch_set
    __swig_getmethods__["taperInch"] = _lathe.T_ACCEL_taperInch_get
    if _newclass:
        taperInch = _swig_property(_lathe.T_ACCEL_taperInch_get, _lathe.T_ACCEL_taperInch_set)
    __swig_setmethods__["stepsSec"] = _lathe.T_ACCEL_stepsSec_set
    __swig_getmethods__["stepsSec"] = _lathe.T_ACCEL_stepsSec_get
    if _newclass:
        stepsSec = _swig_property(_lathe.T_ACCEL_stepsSec_get, _lathe.T_ACCEL_stepsSec_set)
    __swig_setmethods__["stepsSec2"] = _lathe.T_ACCEL_stepsSec2_set
    __swig_getmethods__["stepsSec2"] = _lathe.T_ACCEL_stepsSec2_get
    if _newclass:
        stepsSec2 = _swig_property(_lathe.T_ACCEL_stepsSec2_get, _lathe.T_ACCEL_stepsSec2_set)
    __swig_setmethods__["time"] = _lathe.T_ACCEL_time_set
    __swig_getmethods__["time"] = _lathe.T_ACCEL_time_get
    if _newclass:
        time = _swig_property(_lathe.T_ACCEL_time_get, _lathe.T_ACCEL_time_set)
    __swig_setmethods__["steps"] = _lathe.T_ACCEL_steps_set
    __swig_getmethods__["steps"] = _lathe.T_ACCEL_steps_get
    if _newclass:
        steps = _swig_property(_lathe.T_ACCEL_steps_get, _lathe.T_ACCEL_steps_set)
    __swig_setmethods__["clocks"] = _lathe.T_ACCEL_clocks_set
    __swig_getmethods__["clocks"] = _lathe.T_ACCEL_clocks_get
    if _newclass:
        clocks = _swig_property(_lathe.T_ACCEL_clocks_get, _lathe.T_ACCEL_clocks_set)
    __swig_setmethods__["dist"] = _lathe.T_ACCEL_dist_set
    __swig_getmethods__["dist"] = _lathe.T_ACCEL_dist_get
    if _newclass:
        dist = _swig_property(_lathe.T_ACCEL_dist_get, _lathe.T_ACCEL_dist_set)
    __swig_setmethods__["remainder"] = _lathe.T_ACCEL_remainder_set
    __swig_getmethods__["remainder"] = _lathe.T_ACCEL_remainder_get
    if _newclass:
        remainder = _swig_property(_lathe.T_ACCEL_remainder_get, _lathe.T_ACCEL_remainder_set)
    __swig_setmethods__["initialCount"] = _lathe.T_ACCEL_initialCount_set
    __swig_getmethods__["initialCount"] = _lathe.T_ACCEL_initialCount_get
    if _newclass:
        initialCount = _swig_property(_lathe.T_ACCEL_initialCount_get, _lathe.T_ACCEL_initialCount_set)
    __swig_setmethods__["finalCount"] = _lathe.T_ACCEL_finalCount_set
    __swig_getmethods__["finalCount"] = _lathe.T_ACCEL_finalCount_get
    if _newclass:
        finalCount = _swig_property(_lathe.T_ACCEL_finalCount_get, _lathe.T_ACCEL_finalCount_set)
    __swig_setmethods__["isrCount"] = _lathe.T_ACCEL_isrCount_set
    __swig_getmethods__["isrCount"] = _lathe.T_ACCEL_isrCount_get
    if _newclass:
        isrCount = _swig_property(_lathe.T_ACCEL_isrCount_get, _lathe.T_ACCEL_isrCount_set)
    __swig_setmethods__["spindleSteps"] = _lathe.T_ACCEL_spindleSteps_set
    __swig_getmethods__["spindleSteps"] = _lathe.T_ACCEL_spindleSteps_get
    if _newclass:
        spindleSteps = _swig_property(_lathe.T_ACCEL_spindleSteps_get, _lathe.T_ACCEL_spindleSteps_set)
    __swig_setmethods__["spindleRem"] = _lathe.T_ACCEL_spindleRem_set
    __swig_getmethods__["spindleRem"] = _lathe.T_ACCEL_spindleRem_get
    if _newclass:
        spindleRem = _swig_property(_lathe.T_ACCEL_spindleRem_get, _lathe.T_ACCEL_spindleRem_set)
    __swig_setmethods__["cFactor"] = _lathe.T_ACCEL_cFactor_set
    __swig_getmethods__["cFactor"] = _lathe.T_ACCEL_cFactor_get
    if _newclass:
        cFactor = _swig_property(_lathe.T_ACCEL_cFactor_get, _lathe.T_ACCEL_cFactor_set)
    __swig_setmethods__["clocksStep"] = _lathe.T_ACCEL_clocksStep_set
    __swig_getmethods__["clocksStep"] = _lathe.T_ACCEL_clocksStep_get
    if _newclass:
        clocksStep = _swig_property(_lathe.T_ACCEL_clocksStep_get, _lathe.T_ACCEL_clocksStep_set)
    __swig_setmethods__["initialStep"] = _lathe.T_ACCEL_initialStep_set
    __swig_getmethods__["initialStep"] = _lathe.T_ACCEL_initialStep_get
    if _newclass:
        initialStep = _swig_property(_lathe.T_ACCEL_initialStep_get, _lathe.T_ACCEL_initialStep_set)
    __swig_setmethods__["finalStep"] = _lathe.T_ACCEL_finalStep_set
    __swig_getmethods__["finalStep"] = _lathe.T_ACCEL_finalStep_get
    if _newclass:
        finalStep = _swig_property(_lathe.T_ACCEL_finalStep_get, _lathe.T_ACCEL_finalStep_set)
    __swig_setmethods__["d"] = _lathe.T_ACCEL_d_set
    __swig_getmethods__["d"] = _lathe.T_ACCEL_d_get
    if _newclass:
        d = _swig_property(_lathe.T_ACCEL_d_get, _lathe.T_ACCEL_d_set)
    __swig_setmethods__["incr1"] = _lathe.T_ACCEL_incr1_set
    __swig_getmethods__["incr1"] = _lathe.T_ACCEL_incr1_get
    if _newclass:
        incr1 = _swig_property(_lathe.T_ACCEL_incr1_get, _lathe.T_ACCEL_incr1_set)
    __swig_setmethods__["incr2"] = _lathe.T_ACCEL_incr2_set
    __swig_getmethods__["incr2"] = _lathe.T_ACCEL_incr2_get
    if _newclass:
        incr2 = _swig_property(_lathe.T_ACCEL_incr2_get, _lathe.T_ACCEL_incr2_set)
    __swig_setmethods__["stepsCycle"] = _lathe.T_ACCEL_stepsCycle_set
    __swig_getmethods__["stepsCycle"] = _lathe.T_ACCEL_stepsCycle_get
    if _newclass:
        stepsCycle = _swig_property(_lathe.T_ACCEL_stepsCycle_get, _lathe.T_ACCEL_stepsCycle_set)

    def __init__(self):
        this = _lathe.new_T_ACCEL()
        try:
            self.this.append(this)
        except:
            self.this = this
    __swig_destroy__ = _lathe.delete_T_ACCEL
    __del__ = lambda self: None
T_ACCEL_swigregister = _lathe.T_ACCEL_swigregister
T_ACCEL_swigregister(T_ACCEL)

class T_MOVECTL(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, T_MOVECTL, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, T_MOVECTL, name)
    __repr__ = _swig_repr
    __swig_setmethods__["state"] = _lathe.T_MOVECTL_state_set
    __swig_getmethods__["state"] = _lathe.T_MOVECTL_state_get
    if _newclass:
        state = _swig_property(_lathe.T_MOVECTL_state_get, _lathe.T_MOVECTL_state_set)
    __swig_setmethods__["prev"] = _lathe.T_MOVECTL_prev_set
    __swig_getmethods__["prev"] = _lathe.T_MOVECTL_prev_get
    if _newclass:
        prev = _swig_property(_lathe.T_MOVECTL_prev_get, _lathe.T_MOVECTL_prev_set)
    __swig_setmethods__["cmd"] = _lathe.T_MOVECTL_cmd_set
    __swig_getmethods__["cmd"] = _lathe.T_MOVECTL_cmd_get
    if _newclass:
        cmd = _swig_property(_lathe.T_MOVECTL_cmd_get, _lathe.T_MOVECTL_cmd_set)
    __swig_setmethods__["stop"] = _lathe.T_MOVECTL_stop_set
    __swig_getmethods__["stop"] = _lathe.T_MOVECTL_stop_get
    if _newclass:
        stop = _swig_property(_lathe.T_MOVECTL_stop_get, _lathe.T_MOVECTL_stop_set)
    __swig_setmethods__["done"] = _lathe.T_MOVECTL_done_set
    __swig_getmethods__["done"] = _lathe.T_MOVECTL_done_get
    if _newclass:
        done = _swig_property(_lathe.T_MOVECTL_done_get, _lathe.T_MOVECTL_done_set)
    __swig_setmethods__["ctlreg"] = _lathe.T_MOVECTL_ctlreg_set
    __swig_getmethods__["ctlreg"] = _lathe.T_MOVECTL_ctlreg_get
    if _newclass:
        ctlreg = _swig_property(_lathe.T_MOVECTL_ctlreg_get, _lathe.T_MOVECTL_ctlreg_set)
    __swig_setmethods__["dir"] = _lathe.T_MOVECTL_dir_set
    __swig_getmethods__["dir"] = _lathe.T_MOVECTL_dir_get
    if _newclass:
        dir = _swig_property(_lathe.T_MOVECTL_dir_get, _lathe.T_MOVECTL_dir_set)
    __swig_setmethods__["dirChange"] = _lathe.T_MOVECTL_dirChange_set
    __swig_getmethods__["dirChange"] = _lathe.T_MOVECTL_dirChange_get
    if _newclass:
        dirChange = _swig_property(_lathe.T_MOVECTL_dirChange_get, _lathe.T_MOVECTL_dirChange_set)
    __swig_setmethods__["dist"] = _lathe.T_MOVECTL_dist_set
    __swig_getmethods__["dist"] = _lathe.T_MOVECTL_dist_get
    if _newclass:
        dist = _swig_property(_lathe.T_MOVECTL_dist_get, _lathe.T_MOVECTL_dist_set)
    __swig_setmethods__["loc"] = _lathe.T_MOVECTL_loc_set
    __swig_getmethods__["loc"] = _lathe.T_MOVECTL_loc_get
    if _newclass:
        loc = _swig_property(_lathe.T_MOVECTL_loc_get, _lathe.T_MOVECTL_loc_set)
    __swig_setmethods__["iniDist"] = _lathe.T_MOVECTL_iniDist_set
    __swig_getmethods__["iniDist"] = _lathe.T_MOVECTL_iniDist_get
    if _newclass:
        iniDist = _swig_property(_lathe.T_MOVECTL_iniDist_get, _lathe.T_MOVECTL_iniDist_set)
    __swig_setmethods__["maxDist"] = _lathe.T_MOVECTL_maxDist_set
    __swig_getmethods__["maxDist"] = _lathe.T_MOVECTL_maxDist_get
    if _newclass:
        maxDist = _swig_property(_lathe.T_MOVECTL_maxDist_get, _lathe.T_MOVECTL_maxDist_set)
    __swig_setmethods__["jogInc"] = _lathe.T_MOVECTL_jogInc_set
    __swig_getmethods__["jogInc"] = _lathe.T_MOVECTL_jogInc_get
    if _newclass:
        jogInc = _swig_property(_lathe.T_MOVECTL_jogInc_get, _lathe.T_MOVECTL_jogInc_set)

    def __init__(self):
        this = _lathe.new_T_MOVECTL()
        try:
            self.this.append(this)
        except:
            self.this = this
    __swig_destroy__ = _lathe.delete_T_MOVECTL
    __del__ = lambda self: None
T_MOVECTL_swigregister = _lathe.T_MOVECTL_swigregister
T_MOVECTL_swigregister(T_MOVECTL)
cvar = _lathe.cvar


def allStop():
    return _lathe.allStop()
allStop = _lathe.allStop

def clearAll():
    return _lathe.clearAll()
clearAll = _lathe.clearAll

def setup():
    return _lathe.setup()
setup = _lathe.setup

def spindleStart():
    return _lathe.spindleStart()
spindleStart = _lathe.spindleStart

def spindleStop():
    return _lathe.spindleStop()
spindleStop = _lathe.spindleStop

def spindleSetup():
    return _lathe.spindleSetup()
spindleSetup = _lathe.spindleSetup

def zStart():
    return _lathe.zStart()
zStart = _lathe.zStart

def zStop():
    return _lathe.zStop()
zStop = _lathe.zStop

def zSetup():
    return _lathe.zSetup()
zSetup = _lathe.zSetup

def zMoveSetup():
    return _lathe.zMoveSetup()
zMoveSetup = _lathe.zMoveSetup

def zSynSetup():
    return _lathe.zSynSetup()
zSynSetup = _lathe.zSynSetup

def zTaperSetup():
    return _lathe.zTaperSetup()
zTaperSetup = _lathe.zTaperSetup

def xStart():
    return _lathe.xStart()
xStart = _lathe.xStart

def xStop():
    return _lathe.xStop()
xStop = _lathe.xStop

def xSetup():
    return _lathe.xSetup()
xSetup = _lathe.xSetup

def xMoveSetup():
    return _lathe.xMoveSetup()
xMoveSetup = _lathe.xMoveSetup

def xSynSetup():
    return _lathe.xSynSetup()
xSynSetup = _lathe.xSynSetup

def xTaperSetup():
    return _lathe.xTaperSetup()
xTaperSetup = _lathe.xTaperSetup

def turnPitch(ac, pitch):
    return _lathe.turnPitch(ac, pitch)
turnPitch = _lathe.turnPitch

def threadTPI(ac, tpi):
    return _lathe.threadTPI(ac, tpi)
threadTPI = _lathe.threadTPI

def threadMetric(ac, pitch):
    return _lathe.threadMetric(ac, pitch)
threadMetric = _lathe.threadMetric

def turnCalc(ac):
    return _lathe.turnCalc(ac)
turnCalc = _lathe.turnCalc

def turnAccel(ac, accel):
    return _lathe.turnAccel(ac, accel)
turnAccel = _lathe.turnAccel

def accelCalc(accel):
    return _lathe.accelCalc(accel)
accelCalc = _lathe.accelCalc

def taperCalc(a0, a1, taper):
    return _lathe.taperCalc(a0, a1, taper)
taperCalc = _lathe.taperCalc

def zTaperInit(ac, dir):
    return _lathe.zTaperInit(ac, dir)
zTaperInit = _lathe.zTaperInit

def xTaperInit(ac, dir):
    return _lathe.xTaperInit(ac, dir)
xTaperInit = _lathe.xTaperInit

def tmp(x):
    return _lathe.tmp(x)
tmp = _lathe.tmp
# This file is compatible with both classic and new-style classes.


