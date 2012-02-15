#!/usr/bin/env python

import gammu
import sys

sm = gammu.StateMachine()
if len(sys.argv) >= 2:
    sm.ReadConfig(Filename = sys.argv[1])
    del sys.argv[1]
else:
    sm.ReadConfig()
sm.Init()

sm.SetCallDiverts('AllTypes', 'All', '+420800123456')
diverts = sm.GetCallDiverts()

for x in diverts:
    print x
