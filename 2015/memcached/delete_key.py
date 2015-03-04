#!/usr/bin/env python
# coding=utf-8
import memcache

def del_cache(hosts,del_keys):
    mem = memcache.Client(host,debug=0)
    for key in del_keys:
        mem.delete(key)

if __name__ == "__main__":
    cache_hosts = ['192.168.1.249:11211', '192.168.1.244:11211']
    keys = [
            'industrial_factory',
            'industrial_sxy_factory',
            'industrial_new_factory'
           ]

    del_cache(cache_hosts, keys)

