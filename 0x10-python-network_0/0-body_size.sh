#!/bin/bash
#cURL body size
curl $1 -sw '%{size_download}\n' -o /dev/null
