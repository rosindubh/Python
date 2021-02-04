#!/usr/bin/env python

# notes and scripts from - Python Network Programming Cookbook.pdf
# phil welsby - 28 jan 2021
# script in python2 to find IP Address of a remote machine

import socket

def get_remote_machine_info():
    remote_host = 'www.python.org'
    try:
        print "IP address: %s" %socket.gethostbyname(remote_host)
    except socket.error, err_msg:
        print "%s: %s" %(remote_host, err_msg)
if __name__ == '__main__':
    get_remote_machine_info()
