#!/usr/bin/env python
# coding=utf-8
from subprocess import call
import sys
import time

source = "/tmp/sos_A"
target = "/tmp/sos_B"
rsync = "rsync"
arguments = "-avzHp"
cmd = "%s %s %s %s" % (rsync,arguments,source,target)

def sync():
    while True:
        pop = call(cmd,shell=True)
        if pop !=0:
            print "resubmitting rsync"
            time.sleep(5)
        else:
            print "rsync copy file successful"
            cmd_mail="echo 'jobs done' | mail -s 'jobs done' junqueh@gmail.com"
            call(cmd_mail,shell=True)
            sys.exit(0)
sync()
