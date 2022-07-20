#!/usr/bin/python3
"""This module defines a square"""


class Square:
    """The square has a size 'size'"""
    def __init__(self, size=0):
        """The class is initialized with size.
        If no size is given,, a default size of 0 is assigned.
        Args:
            size: size of the square
        """
        self.size = size

    @property
    def size(self):
        """size: size of the square
        Note:
            size must be of integer type and must be less than zero
        """
        return self.__size

    @size.setter
    def size(self, value):
        if (type(value) != int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates the area of the square.
        Returns:
            The area of the square
        """
        return (self.__size ** 2)
