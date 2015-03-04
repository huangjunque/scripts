#!/usr/bin/env python
# coding=utf-8
import fabric
import re
import os
import sys
import time

USER='root'
HOST= []
IP = []
PORT = '22'
PRI_KEY,PASSWORD,CMD,uSRC,uDST,dSRC,dDST='','','','','','',''
timeout=2

for in in range(1,len(argv)+1):
    if argv[i-1] == '-h' or len(argv)==1:
        print """
        usage:
       -u [user]       Use this argument to specify the user,default is 'root'
       -H [host]       The host that you want to connect
       -f [file]       The file content multiple ip address you want to connect
       -P [port]       The ssh port,default is 22
       -p [pwd|file]   You can specify password or a priviate key file to connect the host
       -c [command]    The command you want the host(s) to run
       -U [src,dst]    The local file that you want to upload to the remote host(s)
       -D [src,dst]    The remote file that you want to download to the local host
       -t [timeout]    The program running timeout,default is 1(s)
       -h              Print this help screen
       
     """


    if argv[i-1] =='-u':
        USER=argv[i]
        env.user='%s'%(USER)'
    else:
