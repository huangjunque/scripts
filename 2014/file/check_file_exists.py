#!/usr/local/env python
import subprocess
import pipes
ssh_host = 'root@192.168.1.18'
file = '/root/c'

resp = subprocess.call(['ssh',ssh_host,'test -e ' + pipes.quote(file)])

if resp == 0:
    print ('%s exists' % file)
else:
    print ('%s does not exists' % file)
