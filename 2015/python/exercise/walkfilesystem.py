#!/usr/bin/env python
# coding=utf-8

import os

os.system("clear")
print "-" * 80
print "OS Walk Program"
print "-" * 80
print "\n"

print "Root prints out directories only from what you specifiled"
print "-" * 70

print "Dirs prints out sub-directories from root"
print "-" * 70

print "Files prints out all files from root and directories"
print "-" * 70

print "This Program will do an os.walk on the folder that you specify"
print "-" * 70

path = raw_input("Specify a folder that want to perform an 'os.walk' on: >>")

for root,dirs,files in os.walk(path):

    print root 
    print "--------------"

    print dirs 
    print "---------------"

    print files
    print "---------------"

