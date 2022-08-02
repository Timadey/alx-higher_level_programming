#!/usr/bin/python3
"""Check if is kind of class"""


def is_kind_of_class(obj, a_class):
    """Returns `true` if the object is an instance of, or if the
    object is an instance of a class that inherited from, the specified
    class; otherwise `false`"""

    return isinstance(obj, a_class)
