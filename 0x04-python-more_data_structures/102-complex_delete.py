#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if not a_dictionary or value not in a_dictionary.values():
        return a_dictionary
    for key, val in enumerate(a_dictionary):
        if val == value:
            del a_dictionary[key]
    return a_dictionary
