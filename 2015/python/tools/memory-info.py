

#!/usr/bin/env python
#coding=utf-8
from __future__ import print_function
#from collections import OrderedDict

try:
    from colletcions import OrderedDict
except ImportError:
    from ordereddict import OrderedDict



def meminfo():
    ''' Return the information in /proc/meminfo
    as a dictionary '''
    meminfo=OrderedDict()

    with open('/proc/meminfo') as f:
        for line in f:
            meminfo[line.split(':')[0]] = line.split(':')[1].strip()
            #float(meminfo['MemTotal'])/(1024)
            #float(meminfo['MemFree'])/(1024)
    return meminfo

if __name__=='__main__':
    #print(meminfo())
    
    meminfo = meminfo()
    print('Total memory: {0}'.format(meminfo['MemTotal']/))
    print('Free memory: {0}'.format(meminfo['MemFree']))

