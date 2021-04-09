#!/usr/bin/python3
''' requests url from arg and displays request id '''
import urllib.request
import urllib.parse
from sys import argv

if __name__ == "__main__":
    ''' main code '''
    url = argv[1]
    vals = {'email': argv[2]}

    data = urllib.parse.urlencode(vals)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
