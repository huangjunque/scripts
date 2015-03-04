#!/usr/bin/env python
# coding=utf-8
f = open(sys.argv[1], "rb")
for i in itertools.count():
    record = f.read(16)
    if not record:
        break

print i

