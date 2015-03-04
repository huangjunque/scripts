#!/usr/bin/env python
# coding=utf-8
import pickle

d = {'a':1, 'b':2}

f = open('datafile.pkl','wb')
pickle.dump(d,f)
f.close()

f=open('datafile.pkl','rb')
e=pickle.load(f)
print e
