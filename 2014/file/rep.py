#!/usr/bin/env python
# coding=utf-8
# 功能：替换文件夹下面文件里面的某个字符
# 这次是把specialtopic下面所有的代码中删除掉cmonitor.字样
import os,re
 
# 获得所有的代码文件绝对路径列表
def get_allfiles(path):
    allfiles = []
    for parent,dirnames,filenames in os.walk(path):
        for filename in filenames:
            allfiles.append(os.path.join(parent,filename))  
    return allfiles
 
# 替换指定文件里面的字符
def replace(f):
    F = open(f)
    try:
        F_Text = F.read()
    finally:
        F.close()
    bak = F_Text.replace('cmonitor.','')
    open(f,'w').write(bak)
 
path = r"D:\work\svn\webmodules\cmonitor\tomas-flex-cmonitor\src\com\ultrapower\tomas\common"
for f in get_allfiles(path):
    replace(f)      

