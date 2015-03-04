#!/usr/bin/env python
# coding=utf-8
import socket
for i in range(201,241):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex(('192.168.1.%d' %(i),22))
if result == 0:
    print "'192.168.1.%d' %(i), Port in open"
else:
    print "Port is not open"
