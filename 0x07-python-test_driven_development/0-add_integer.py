#!/usr/bin/python3
"""Module to add two integers
    Attributes:
        add_integer: adds two integer
"""

def add_integer(a, b=98):
    """Add two integer
    Args:
        a: first number
        b: second number
    Note: 
        a and b will be casted to int if they're float
        b default value is 98
    Raises:
        TypeError, if the numbers are not integers
    Return:
        the sum of the two
    """

    if type(a) == float:
        a = (int)(a)
    if type(b) == float:
        b = (int)(b)
    if type(a) != int:
        raise TypeError("a must be an integer")
    if type(b) != int:
        raise TypeError("b must be an integer")
    return a + b
