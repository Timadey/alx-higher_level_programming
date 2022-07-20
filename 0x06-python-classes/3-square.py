#!/usr/bin/python3
"""This module only defines a class Square"""


class Square:
    """A square has a size size"""
    def __init__(self, size=0):
        """The square is initialized with size.
        Size must be int and less than zero or the program will raise
        TypeError and ValueError respectively.
        """
        if (type(size) != int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        #: size: size of the square, must be int and less than 0
        self.__size = size

    def area(self):
        """Returns the area of the square"""
        return (self.__size ** 2)
