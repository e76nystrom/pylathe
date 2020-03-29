# fpga registers


# skip register zero

XNOOP            =  0           # register 0

# load control registers

XLDZCTL          =  1           # z control register
XLDXCTL          =  2           # x control register
XLDTCTL          =  3           # load taper control
XLDPCTL          =  4           # position control
XLDCFG           =  5           # configuration
XLDDCTL          =  6           # load debug control
XLDDREG          =  7           # load display reg
XREADREG         =  8           # read register

# status register

XRDSR            =  9           # read status register

# phase counter

XLDPHASE         = 10           # load phase max

# load z motion

XLDZFREQ         = 11           # load z frequency
XLDZD            = 12           # load z initial d
XLDZINCR1        = 13           # load z incr1
XLDZINCR2        = 14           # load z incr2
XLDZACCEL        = 15           # load z syn accel
XLDZACLCNT       = 16           # load z syn acl cnt
XLDZDIST         = 17           # load z distance
XLDZLOC          = 18           # load z location

# load x motion

XLDXFREQ         = 19           # load x frequency
XLDXD            = 20           # load x initial d
XLDXINCR1        = 21           # load x incr1
XLDXINCR2        = 22           # load x incr2
XLDXACCEL        = 23           # load x syn accel
XLDXACLCNT       = 24           # load x syn acl cnt
XLDXDIST         = 25           # load x distance
XLDXLOC          = 26           # load x location

# read z motion

XRDZSUM          = 27           # read z sync sum
XRDZXPOS         = 28           # read z sync x pos
XRDZYPOS         = 29           # read z sync y pos
XRDZACLSUM       = 30           # read z acl sum
XRDZASTP         = 31           # read z acl stps

# read x motion

XRDXSUM          = 32           # read x sync sum
XRDXXPOS         = 33           # read x sync x pos
XRDXYPOS         = 34           # read x sync y pos
XRDXACLSUM       = 35           # read x acl sum
XRDXASTP         = 36           # read z acl stps

# read distance

XRDZDIST         = 37           # read z distance
XRDXDIST         = 38           # read x distance

# read location

XRDZLOC          = 39           # read z location
XRDXLOC          = 40           # read x location

# read frequency and state

XRDFREQ          = 41           # read encoder freq
XCLRFREQ         = 42           # clear freq register
XRDSTATE         = 43           # read state info

# read phase

XRDPSYN          = 44           # read sync phase val
XRDTPHS          = 45           # read tot phase val

# phase limit info

XLDZLIM          = 46           # load z limit
XRDZPOS          = 47           # read z position

# test info

XLDTFREQ         = 48           # load test freq
XLDTCOUNT        = 49           # load test count

# read control regs

XRDZCTL          = 50           # read control regiisters
XRDXCTL          = 51           # read control regiisters
# fpga table

xRegTable = ( \
    "XNOOP",                            #   0
    "XLDZCTL",                          #   1
    "XLDXCTL",                          #   2
    "XLDTCTL",                          #   3
    "XLDPCTL",                          #   4
    "XLDCFG",                           #   5
    "XLDDCTL",                          #   6
    "XLDDREG",                          #   7
    "XREADREG",                         #   8
    "XRDSR",                            #   9
    "XLDPHASE",                         #  10
    "XLDZFREQ",                         #  11
    "XLDZD",                            #  12
    "XLDZINCR1",                        #  13
    "XLDZINCR2",                        #  14
    "XLDZACCEL",                        #  15
    "XLDZACLCNT",                       #  16
    "XLDZDIST",                         #  17
    "XLDZLOC",                          #  18
    "XLDXFREQ",                         #  19
    "XLDXD",                            #  20
    "XLDXINCR1",                        #  21
    "XLDXINCR2",                        #  22
    "XLDXACCEL",                        #  23
    "XLDXACLCNT",                       #  24
    "XLDXDIST",                         #  25
    "XLDXLOC",                          #  26
    "XRDZSUM",                          #  27
    "XRDZXPOS",                         #  28
    "XRDZYPOS",                         #  29
    "XRDZACLSUM",                       #  30
    "XRDZASTP",                         #  31
    "XRDXSUM",                          #  32
    "XRDXXPOS",                         #  33
    "XRDXYPOS",                         #  34
    "XRDXACLSUM",                       #  35
    "XRDXASTP",                         #  36
    "XRDZDIST",                         #  37
    "XRDXDIST",                         #  38
    "XRDZLOC",                          #  39
    "XRDXLOC",                          #  40
    "XRDFREQ",                          #  41
    "XCLRFREQ",                         #  42
    "XRDSTATE",                         #  43
    "XRDPSYN",                          #  44
    "XRDTPHS",                          #  45
    "XLDZLIM",                          #  46
    "XRDZPOS",                          #  47
    "XLDTFREQ",                         #  48
    "XLDTCOUNT",                        #  49
    "XRDZCTL",                          #  50
    "XRDXCTL",                          #  51
    )

importList = ( \
 xRegTable, \
 XNOOP, \
 XLDZCTL, \
 XLDXCTL, \
 XLDTCTL, \
 XLDPCTL, \
 XLDCFG, \
 XLDDCTL, \
 XLDDREG, \
 XREADREG, \
 XRDSR, \
 XLDPHASE, \
 XLDZFREQ, \
 XLDZD, \
 XLDZINCR1, \
 XLDZINCR2, \
 XLDZACCEL, \
 XLDZACLCNT, \
 XLDZDIST, \
 XLDZLOC, \
 XLDXFREQ, \
 XLDXD, \
 XLDXINCR1, \
 XLDXINCR2, \
 XLDXACCEL, \
 XLDXACLCNT, \
 XLDXDIST, \
 XLDXLOC, \
 XRDZSUM, \
 XRDZXPOS, \
 XRDZYPOS, \
 XRDZACLSUM, \
 XRDZASTP, \
 XRDXSUM, \
 XRDXXPOS, \
 XRDXYPOS, \
 XRDXACLSUM, \
 XRDXASTP, \
 XRDZDIST, \
 XRDXDIST, \
 XRDZLOC, \
 XRDXLOC, \
 XRDFREQ, \
 XCLRFREQ, \
 XRDSTATE, \
 XRDPSYN, \
 XRDTPHS, \
 XLDZLIM, \
 XRDZPOS, \
 XLDTFREQ, \
 XLDTCOUNT, \
 XRDZCTL, \
 XRDXCTL, \
)
