#!/bin/bash
#coding=utf-8

wget http://www.python.org/ftp/python/2.7.5/Python-2.7.5.tar.bz2
tar jxvf Python-2.7.5.tar.bz2
cd Python-2.7.5
./configure
make
make install

mv /usr/bin/python /usr/bin/python_old
ln -s /usr/local/bin/python2.7 /usr/bin/python

echo 'please modfiled /usr/bin/yum'
