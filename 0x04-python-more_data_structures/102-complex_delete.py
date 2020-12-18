#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for key, data in list(a_dictionary.items()):
        if value == data:
            del a_dictionary[key]
    return a_dictionary
