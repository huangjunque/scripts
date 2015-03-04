import subprocess 
import os
dest1 = '114.114.114.114'
dest2 = '124.207.104.18'
subprocess.call(["mtr --report -c 5 %s" % dest1])

