#!/usr/bin/python3
"""Return list of available attributes and methods of an object"""


def lookup(obj):
    """The function"""

    return list(dir(obj))
