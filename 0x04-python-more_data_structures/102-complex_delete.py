#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for key, val in enumerate(a_dictionary):
        if val == value:
            del a_dictionary[key]
    return a_dictionary
