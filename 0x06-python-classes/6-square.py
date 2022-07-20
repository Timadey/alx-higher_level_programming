#!/usr/bin/python3
"""This module defines a square"""


class Square:
    """A square class"""
    def __init__(self, size=0, position=(0, 0)):
        """This class is initialized with the size and position
        Args:
            size(int): size of the square
            position(tuple): position
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """size: size of the square
        Note:
            size must be of integer type and must be less than zero
        Raises:
            TypeError: if size is not of type (int)
            ValueError: if size is less than zero
        Returns:
            The size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        if (type(value) != int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """The position of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        if (type(value) != tuple or value[0] < 0 or value[1] < 1):
            raise TypeError("posiion must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculate the area of the square
        Returns:
            The area of the square
        """
        return (self.__size ** 2)

    def my_print(self):
        """ I don't understand
        will implement later """
