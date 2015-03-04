#!/usr/bin/env python
# coding=utf-8
import sys
import time

class displayFormat(object):
    def format_size(self,size): 
         '''''格式化流量单位''' 
        KB = 1024
        MB = 1048576
        GB = 1073741824
        TB = 1099511627776
        if size >=TB:
            size = str(size / TB ) + 'T'
        elif size < KB:
            size = str(size) + 'B'
        elif size >=GB and size < TB:
            size = str(size / GB) + 'G'
        elif size >= MB and size < GB:
            size = str(size / MB) + 'M'
        else:
            size = str(size / KB) + 'K'
        return size 


