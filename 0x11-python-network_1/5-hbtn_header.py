#!/usr/bin/python3
''' takes in URL displays response or error '''

if __name__ == "__main__":
    ''' main code '''
    import requests
    from sys import argv
    r = requests.get(argv[1])
    try:
        print(r.headers['X-Request-Id'])
    except:
        pass
