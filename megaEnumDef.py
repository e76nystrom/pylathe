
# enums

# mega poll response bits

M_POLL_ESTOP_NO  =  0           # estop no in
M_POLL_ESTOP_NC  =  1           # estop nc in
M_POLL_SP_FWD    =  2           # spindle forward in
M_POLL_SP_REV    =  3           # spindle reverse in
M_POLL_ESTOP     =  4           # estop condition
M_POLL_WD_ENA    =  5           # watchdog enabled
M_POLL_CP_ACTIVE =  6           # charge pump active
M_POLL_PWM_ACTIVE =  7          # pwm active
M_POLL_STEP_DIS  =  8           # stepper disabled
M_POLL_ESTOP_RLY =  9           # estop relay
M_POLL_ESTOP_PC  = 10           # estop pc

pollMegaList = ( \
    "M_POLL_ESTOP_NO",
    "M_POLL_ESTOP_NC",
    "M_POLL_SP_FWD",
    "M_POLL_SP_REV",
    "M_POLL_ESTOP",
    "M_POLL_WD_ENA",
    "M_POLL_CP_ACTIVE",
    "M_POLL_PWM_ACTIVE",
    "M_POLL_STEP_DIS",
    "M_POLL_ESTOP_RLY",
    "M_POLL_ESTOP_PC",
    )

pollMegaText = ( \
    "estop no in",
    "estop nc in",
    "spindle forward in",
    "spindle reverse in",
    "estop condition",
    "watchdog enabled",
    "charge pump active",
    "pwm active",
    "stepper disabled",
    "estop relay",
    "estop pc",
    )

# mega vfd speed selector

MEGA_SLOW_PWM    =  0           # Slow PWM
MEGA_FAST_PWM    =  1           # Fast PWM
MEGA_DIRECT_RPM  =  2           # Set RPM

vfdSpeedList = ( \
    "MEGA_SLOW_PWM",
    "MEGA_FAST_PWM",
    "MEGA_DIRECT_RPM",
    )

vfdSpeedText = ( \
    "Slow PWM",
    "Fast PWM",
    "Set RPM",
    )
