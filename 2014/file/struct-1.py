#!/usr/bin/env python
# coding=utf-8

import struct
f = open('data.bin', 'wb')
data = struct.pack('hh1', 1, 2, 3)
f.write(data)
f.close()

f = open('data.bin','rb')
data = f.read()
values = struct.unpack('hh1',data)
print values
