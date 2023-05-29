
# parameters
M_PARM_RPM           =   0	# 0x00
M_PARM_VFD_ENA       =   1	# 0x01
M_PARM_PWM_CFG       =   2	# 0x02
M_PARM_ENC_TEST      =   3	# 0x03
M_PARM_ENC_LINES     =   4	# 0x04
M_PARM_MAX_PARM      =   5	# 0x05

parmTable = ( \
    ('M_PARM_RPM', 'int', 'mParmRpm'),
    ('M_PARM_VFD_ENA', 'char', 'mParmVfdEna'),
    ('M_PARM_PWM_CFG', 'char', 'mParmPwmCfg'),
    ('M_PARM_ENC_TEST', 'char', 'mParmEncTest'),
    ('M_PARM_ENC_LINES', 'int', 'mParmEncLines'),
    ('M_PARM_MAX_PARM', 'char', 'mParmMaxParm'),
    )
