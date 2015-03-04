#!/usr/bin/python
#create by junqueh
import os
import socket
import sys
import re
import subprocess
from collections import Counter
import time


def FILE():
    if os.path.exists('/root/os_check'):
        FN ='/root/os_check+'+NOWTIME()
        return FN
    else:
        os.system('mkdir -pv /root/os_check')
        FN = '/root/os_check/os-'+NOWTIME()
        return FN

def NOWTIME():
    from datetime import date
    import time
    now = data.today()
    return now.strftime("%Y%b%d")+"_"+time.strftime('%H%M%S')


def getSN():
    getSN=[]
    getSN.append('dmidecode  -s  system-serial-number')
    getSN.append('dmidecode  -s system-product-name')
    FILENAME = FILE()
    for i in getSN:
        print(i)
        os.system("echo======================"+i+"===============>>"+FILENAME)
        os.system(i+" >> "+FILENAME)

def getCPU():
    openfile=file('/proc/cpuinfo','r')
    cpucount = 0
    phcpucount=0
    cpumodel=[]
    L1=[]
    for line in openfile.readlines():
        i=line.strip('\n')
        if re.match(r'^processor',i):
            cpucount=cpucount+1    
        elif re.match(r'^physical id',i):
            L1.append(i)
        elif re.findall('model name',i):
            cpumodel.append(i.split(':')[1])
        else:
            pass
    openfile.close()
    for num in Counter(L1).keys():
        phcpucount=phcpucount+1
    print "Processor number:",cpucount
    print "Physical CPU number:",phcpucount
    print "CPU Model:",cpumodel[0].strip(),"\n"


def getMem():
    m=os.popen('grep MemTotal  /proc/meminfo')
    max=os.popen('dmidecode  -t memory')
    swm=os.popen('grep SwapTotal /proc/meminfo')
    L=[]
    for line in max.readlines():
        R1=line.strip("\n")
        if re.findall('Maximum',R1):
            sw,se=R1.split(":")
            L.append(se)
    max.close()
    for line1 in swm.readlines():
        sw1,sw2,sw3=line1.split()
        L.append(sw2)
    for line2 in m.readlines():
        m1,m2,m3=line2.split()
        L.append(m2)
    print "Memory Total:",int(L[2])/1000/1000,"G"
    print "Swap Total:",int(L[1])/1024,"M"
    print "Max support Memory:",L[0]

def gethostname():
    print(socket.gethostname())

def getipaddress():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('google.com', 0))
    ipaddr=s.getsockname()[0]
    print  ipaddr


def getsystem():
    re=os.popen('cat /etc/redhat-release')
    u=os.popen('uname -r')
    red=re.readline().strip()
    us=u.readline().strip()
    re.close()
    u.close()
    print  "system os:",red
    print  "core version:",us,"\n"

def getdisk():
    part=os.popen('parted -l | grep -E "/dev/sda|/dev/sdb"')
    part_red=part.read().strip()
    
    part.close()
    print  "disk num:",part_red


if __name__ == '__main__':
    print "\x1b[0;34m+++++++++++Device SN+++++++++\x1b[0m" 
    getSN()
    print "\x1b[0;34m+++++++++++Cpu Info++++++++++\x1b[0m"
    getCPU()
    print "\x1b[0;34m+++++++++++Memory +++++++++++\x1b[0m"
    getMem()
    print "\x1b[0;34m+++++++++++Hostname+++++++++++\x1b[0m"
    gethostname()
    print "\x1b[0;34m+++++++++++Ipaddress+++++++++++\x1b[0m"
    getipaddress()
    print "\x1b[0;34m+++++++++++systeminfo+++++++++++\x1b[0m"
    getsystem()
    print "\x1b[0;34m+++++++++++diskinfo+++++++++++\x1b[0m"
    getdisk()
