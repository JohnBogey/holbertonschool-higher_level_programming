#!/usr/bin/python3
''' takes in URL displays response or error '''
import requests
from sys import argv

if __name__ == "__main__":
    ''' main code '''
    q = '' if len(argv) < 2 else argv[1]
    url = 'http://0.0.0.0:5000/search_user'
    payload = {'q': q}
    try:
        answer = requests.post(url, data=payload).json()
    except:
        print("Not a valid JSON")
    else:
        if not answer:
            print("No result")
        else:
            print("[{}] {}".format(answer['id'], answer['name']))
