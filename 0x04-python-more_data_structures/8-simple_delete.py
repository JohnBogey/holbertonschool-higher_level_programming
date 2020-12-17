#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    a_dictionary.popitem(key)
    return(a_dictionary)