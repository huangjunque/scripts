#!/usr/local/env python
import socket
import sys
import subprocess
from datetime import datetime

# Clear the screen
#subprocess.call('clear',shell=True)

# Ask for input
remoteServer = raw_input("Enter a remote host to scan:")
remoteServerIP = socket.gethostbyname(remoteServer)

# Print  a nice banner with information on which host we are about to scan
print "-" * 50
print "Please wait,scanning remote host",remoteServerIP
print "-" * 50

# Check what time the scan started

t1 = datetime.now()

#scans ports 

try:
    for port in range(1,65500):
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result ==0:
            print "Port{}:\t Open".format(port)
        sock.close()

except KeyboardInterrupt:
    print "You pressed Ctrl+C"
    sys.exit()

except socket.gaierror:
    print 'Hostname could not be resolved. Exiting'
    sys.exit()

except socket.error:
    print "Couldn't connect to server"
    sys.exit()

# Check the time again
t2 = datetime.now()

# Calculates the difference of time.
total = t2 -t1

print 'Scanning Completed in:',total




