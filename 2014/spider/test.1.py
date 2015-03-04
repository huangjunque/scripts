#!/usr/bin/env python
# coding=utf-8
from urllib2 import Request, urlopen, URLError, HTTPError

old_url = 'http://rrurl.cn/b1UZuP'
req = Request(old_url)
resp = urlopen(req)
print 'Old url :' + old_url
print 'Real url :' + resp.geturl()
