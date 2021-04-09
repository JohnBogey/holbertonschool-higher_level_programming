#!/usr/bin/python3
''' requests url from arg and displays request id '''
import urllib.request
from sys import argv

if __name__ == "__main__":
    ''' main code '''
    req = urllib.request.Request(argv[1])
    with urllib.request.urlopen(req) as response:
        header = response.info()
        print(header['X-Request-Id'])
