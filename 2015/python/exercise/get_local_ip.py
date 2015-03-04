#!/usr/bin/env python
# coding=utf-8
import socket
def Get_local_ip():

    try:
        csock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        csock.connect(('114.114.114.114', 80))
        (addr, port) = csock.getsockname()
        csock.close()
        return addr
    except socket.error:
        return "127.0.0.1"

if __name__ == "__main__":
    local_IP = Get_local_ip()
    print local_IP
