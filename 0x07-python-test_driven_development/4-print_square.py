#!/usr/bin/python3
"""Prints a square with the character `#`
"""


def print_square(size):
    """Print a square of size `size` with `#`

    Args:
        size: size of the square

    Raises:
        TypeError: size must be integer
        ValueError: size must be >= 0
    """

    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        print("#" * size)
