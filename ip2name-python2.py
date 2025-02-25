#!/usr/bin/env python

import re
import fileinput
import socket

_dnscache = {'127.0.0.1':'localhost'}

def resolve(m):
    ip = m.group(0)
    if ip in _dnscache:
        return '[%s]' % _dnscache[ip]

    try:
        name = socket.gethostbyaddr(ip)[0]
    except socket.herror, socket.timeout:
        name = ip
    _dnscache[ip] = name
    return '[%s]' % name


ipregex = re.compile(
        r'\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b'
          )


if __name__ == "__main__":
    for line in fileinput.input():
        print re.sub(ipregex, resolve, line),
