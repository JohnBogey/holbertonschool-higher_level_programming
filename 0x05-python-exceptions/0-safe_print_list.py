#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    for i in range(x):
        try:
            print(my_list[i])
        except IndexError:
            return i
    return i + 1
