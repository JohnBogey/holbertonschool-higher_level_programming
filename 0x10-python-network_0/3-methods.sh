#!/bin/bash
#cURL show methods
curl -sD - 0.0.0.0:5000/route_4 -o /dev/null | grep 'Allow:' | sed 's/^.*: //'