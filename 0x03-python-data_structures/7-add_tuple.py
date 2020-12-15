#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == 0:
        list_a = [0, 0]
    elif len(tuple_a) == 1:
        list_a = [tuple_a[0], 0]
    else:
        list_a = [tuple_a[0], tuple_a[1]]
    if len(tuple_b) == 0:
        list_b = [0, 0]
    elif len(tuple_b) == 1:
        list_b = [tuple_b[0], 0]
    else:
        list_b = [tuple_b[0], tuple_b[1]]
    tuple_c = list_a[0] + list_b[0], list_a[1] + list_b[1]
    return tuple_c
