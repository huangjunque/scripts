#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division
import os
file = open('/tmp/disk','a')
 
def disk_root():
        disk = os.statvfs('/')
        percent = (disk.f_blocks - disk.f_bfree) * 100 / (disk.f_blocks -disk.f_bfree + disk.f_bavail)
        return percent
 
def disk_backup():
        disk = os.statvfs('/home')
        percent = (disk.f_blocks - disk.f_bfree) * 100 / (disk.f_blocks -disk.f_bfree + disk.f_bavail)
        return percent
 
def disk_project():
        disk = os.statvfs('/boot')
        percent = (disk.f_blocks - disk.f_bfree) * 100 / (disk.f_blocks -disk.f_bfree + disk.f_bavail)
        return percent
 
def mem_stat():
        mem = {}
        f = open('/proc/meminfo')
        lines = f.readlines()
        f.close()
        for line in lines:
                name = line.split(':')[0]
                var = line.split(':')[1].split()[0]
                mem[name] = long(var)
        Mem = (100 - ((mem['MemFree'] + mem['Buffers'] + mem['Cached']) / mem['MemTotal']) * 100)
        return Mem
 
root = '/                   %0.f%%'%disk_root()+'\n'
backup = '/home            %0.f%%'%disk_backup()+'\n'
project = '/boot            %0.f%%'%disk_project()+'\n'
memory = 'memory           %0.2f%%'%mem_stat()+'\n'
 
file.writelines('Filesystem&Mem     Use%'+'\n'+'-----------------------'+'\n')
file.writelines(root)
file.writelines(backup)
file.writelines(project)
file.writelines(memory)
file.flush()
file.close()
