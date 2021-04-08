#!/bin/bash
#cURL show methods
curl -sI $1 -o /dev/null | grep 'Allow:' | sed 's/^.*: //'