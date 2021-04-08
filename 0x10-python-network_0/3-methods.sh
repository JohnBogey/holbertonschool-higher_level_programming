#!/bin/bash
#cURL show methods
curl $1 -sI | grep 'Allow:' | sed 's/^.*: //'
