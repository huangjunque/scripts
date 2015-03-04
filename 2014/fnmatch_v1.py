#!/usr/bin/env python
# coding=utf-8
import os
import fnmatch

for root, dir, files in os.walk("."):
    print root
    print ""
    for items in fnmatch.filter(files, "*.py"):
        print "..." + items
    print ""

