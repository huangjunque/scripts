#!/usr/bin/env python
# coding=utf-8
from subprocess import call
import sys

source = "/tmp/sos_A/"
target = "/tmp/sos_B"
rsync = "rsync"
arguments = "-avzP"
cmd ="%s %s %s %s" % (rsync,arguments,source,target)

def sync():
    pop = call(cmd,shell=True)
    if pop !=0:
        print "rsync failed"
sync()
