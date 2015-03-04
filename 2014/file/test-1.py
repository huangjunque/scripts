#!/usr/bin/env python
# coding=utf-8
f = open('bigdata')

lines = [ line.strip() for line in f.readlines()]
print line 
print lines
f.close()
