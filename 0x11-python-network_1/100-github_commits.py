#!/usr/bin/python3
''' Lists 10 most recent commits of repository '''
import requests
from sys import argv

if __name__ == "__main__":
    repo = argv[1]
    owner = argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(owner, repo)
    params = {'per_page': 10}

    r = requests.get(url, params=params).json()
    for item in r:
        print("{}: {}".format(item['sha'], item['commit']['author']['name']))
