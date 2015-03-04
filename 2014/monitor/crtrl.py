#!/usr/bin/env python
# coding=utf-8
import os,sys, time
while True:
    time.sleep(3)
try:
    ret = os.popen('ps -C apache -o pid,cmd').readlines()
    if len(ret) < 2:
        print 'apache 异常退出，3秒后重启动'
    time.sleep(3)
    os.system("service apache2 restart")
except:
    print "Error". sys.exc_info()[1]
