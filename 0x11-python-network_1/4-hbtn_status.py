#!/usr/bin/python3
''' takes in URL displays response or error '''
import requests

if __name__ == "__main__":
    ''' main code '''
    r = requests.get('https://intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))
