#!/usr/bin/python3
def element_at(mylist, idx):
    if idx < 0:
        return None
    if idx >= len(mylist):
        return None
    for i, val in enumerate(mylist):
        if i == idx:
            return val
