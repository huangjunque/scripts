#!/usr/bin/env python
import urllib2
from multiprocessing.dummy import Pool as ThreadPool

urls = [
	'http://www.python.org', 
    'http://www.python.org/about/',
    'http://www.onlamp.com/pub/a/python/2003/04/17/metaclasses.html',
    'http://www.python.org/doc/',
    'http://www.python.org/download/',
    'http://www.python.org/getit/',
    'http://www.python.org/community/',
    'https://wiki.python.org/moin/',
    'http://planet.python.org/',
    'https://wiki.python.org/moin/LocalUserGroups',
    'http://www.python.org/psf/',
    'http://docs.python.org/devguide/',
    'http://www.python.org/community/awards/'
	]

pool = ThreadPool(4)
#Open the urls in their own threads
results = pool.map(urllib2.urlopen, urls)
#close the pool and wait for the work of finish
pool.close()
pool.join()

