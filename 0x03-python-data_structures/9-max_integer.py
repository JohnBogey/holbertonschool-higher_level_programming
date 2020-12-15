#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    thiccest = my_list[0]
    for number in my_list:
        thiccest = number if number > thiccest else thiccest
    return thiccest
