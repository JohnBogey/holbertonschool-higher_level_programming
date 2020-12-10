#!/usr/bin/python3
from sys import argv
argc = len(argv) - 1
argString = "argument"
if argc != 1:
    argString += "s"
else:
    argString += ""
if argc != 0:
    argString += ":"
else:
    argString += "."

print("{} {}".format(argc, argString))
for x in range(1, argc + 1):
      print("{}: {}".format(x, argv[x]))
