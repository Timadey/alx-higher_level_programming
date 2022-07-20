#!/usr/bin/python3
"""This module defines a class Square"""


class Square:
    """Square has a default size of 0"""
    def __init__(self, size=0):
        """Square is initialized with size.
        Raises a TypeError if size is not int and raises
        ValueError if size is less than 0.

        Args:
            size(int): the size of the square
        """
        if (type(size) != int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size
