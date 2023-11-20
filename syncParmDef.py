
# parameters
SYNC_CYCLE           =   0	# 0x00
SYNC_OUTPUT          =   1	# 0x01
SYNC_PRESCALER       =   2	# 0x02
SYNC_ENCODER         =   3	# 0x03
SYNC_MAX_PARM        =   4	# 0x04

parmTable = ( \
    ("SYNC_CYCLE",     "uint16_t", "syncCycle"    ), # 0x00   0
    ("SYNC_OUTPUT",    "uint16_t", "syncOutput"   ), # 0x01   1
    ("SYNC_PRESCALER", "uint16_t", "syncPrescaler"), # 0x02   2
    ("SYNC_ENCODER",   "uint16_t", "syncEncoder"  ), # 0x03   3
    ("SYNC_MAX_PARM",  "int16_t",  "syncMaxParm"  ), # 0x04   4
    )
