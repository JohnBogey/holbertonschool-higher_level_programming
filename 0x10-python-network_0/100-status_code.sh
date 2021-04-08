#!/bin/bash
#curl display status code
curl $1 -sw '%{http_code}' -o /dev/null
