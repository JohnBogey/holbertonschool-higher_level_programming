#!/usr/bin/python3
from sys import argv
sum = 0
for x in range(1, len(argv)):
      sum += int(argv[x])
print(sum)
