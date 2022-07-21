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

    def __eq__(self, other):
        """Return area when square instance are used in comparison also"""

        return self.size == other.size

    def __ne__(self, other):
        """not equals to"""

        return not(self.size == other.size)

    def __lt__(self, other):
        """less than"""

        return self.size < other.size

    def __le__(self, other):
        """less than or equals to"""

        return self.size <= other.size

    def __ge__(self, other):
        """greater than or equal to"""

        return self.size >= other.size

    def __gt__(self, other):
        """graeter than"""

        return self.size > other.size

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
