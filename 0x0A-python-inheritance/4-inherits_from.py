#!/usr/bin/python3
"""Check if a class inherits from a class"""


def inherits_from(obj, a_class):
    """Return `true` if the object is an instance of a class that inherited
    (directly or indirectly) from the speified class; otherwise `false`"""

    if type(obj) is a_class:
        return False
    return isinstance(obj, a_class)
