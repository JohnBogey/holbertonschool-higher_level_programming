#!/usr/bin/python3
''' takes in URL displays response or error '''
import requests
from sys import argv

if __name__ == "__main__":
    ''' main code '''
    url = "https://api.github.com/user"
    try:
        print(requests.get(url, auth=(argv[1], argv[2])).json()['id'])
    except:
        print("None")
