#!/usr/bin/env python
#by junqueh 2014/11/12
import subprocess

for i in range(201,241):
    address = "192.168.1.%d" %(i) 
    res = subprocess.call(['ping', '-c' '3', address])
    if res == 0:
        print "ping to", address, "OK"
    elif res == 2:
        print "no reply from", address
    else:
        print "ping to", address, "failed!"


