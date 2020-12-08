#!/usr/bin/python3
def uppercase(str):
    for element in str:
        if ord(element) in range(ord('a'), ord('z') + 1):
            c = ord(element) - 32
        else:
            c = ord(element)
        print("{:c}".format(c), end="")
    print()
