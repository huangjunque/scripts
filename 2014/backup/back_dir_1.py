#!/usr/bin/python env
import os
import time

source = ['/root/bash']
target_dir = '/root/'

target = target_dir + time.strftime('%Y%m%d%H%M%S') + '.tar.gz2'
## tar.gz

tar_command = 'tar -zcvf %s %s' % (target,' '.join(source))
## 00

if os.system(tar_command) ==0:
    print 'Successful backup to',target
else:
    print 'Backup Failed!'
