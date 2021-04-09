#!/usr/bin/python3
''' takes in URL displays response or error '''
import requests
from sys import argv

if __name__ == "__main__":
    ''' main code '''
    r = requests.get(argv[1])
    print(r.headers['X-Request-Id'])
