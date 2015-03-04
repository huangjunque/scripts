#!/usr/bin/env python
import os
import sys
import time

while True:
    time.sleep(3)
    try:
        ret = os.popen('ps -C nginx -o pid,cmd').readlines()
        if len(ret) <2:
            print "nginx process killed, please restart service in 3 seconds."
            time.sleep(3)
            os.system("service nginx restart")
    except:
        print "Error", sys.exc_info()[1]
