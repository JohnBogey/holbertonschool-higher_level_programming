#!/usr/bin/python3
''' takes in URL displays response or error '''
import requests
from sys import argv

if __name__ == "__main__":
    ''' main code '''
    payload = {'email': argv[2]}
    print(requests.post(argv[1], data=payload).text)
