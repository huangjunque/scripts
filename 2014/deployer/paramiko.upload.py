#!/usr/bin/env python
# coding=utf-8
import paramiko
import os
import datetime

hostname='192.168.1.*'
username='root'
password='skateboard'
port=22
local_dir='/Users/junqueh/store'
remote_dir='/root/'
if __name__ == "__main__":
    try:
        t=paramiko.Transport((hostname,port))
        t.connect(username=username,password=password)
        sftp=paramiko.SFTPClient.from_transport(t)
        files=os.listdir(local_dir)
        for f in files:
            print ''
            print '#########################################'
            print 'Beginning to upload file %s ' % datetime.datetime.now()
            print 'Uploding file:',os.path.join(local_dir,f)

            sftp.put(os.path.join(local_dir,f),os.path.join(remote_dir,f))

            print 'upload file successful %s ' % datetime.datetime.now()
            print ''
            print '############################################'

        t.close()










