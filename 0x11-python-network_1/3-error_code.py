#!/usr/bin/python3
''' takes in URL displays response or error '''
import urllib.request
import urllib.parse
from urllib.error import HTTPError
from sys import argv

if __name__ == "__main__":
    ''' main code '''
    req = urllib.request.Request(argv[1])
    try:
        with urllib.request.urlopen(req) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print('Error code: {}'.format(e.code))
