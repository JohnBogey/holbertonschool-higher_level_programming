#!/usr/bin/python3
''' takes in URL displays response or error '''
import requests
from sys import argv

if __name__ == "__main__":
    ''' main code '''
    r = requests.get(argv[1])
    try:
        r.raise_for_status()
    except:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)
