#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx > len(my_list) - 1 or idx < 0:
        return my_list
    my_list[:] = my_list[0:idx] + my_list[1 + idx:]
    return my_list
