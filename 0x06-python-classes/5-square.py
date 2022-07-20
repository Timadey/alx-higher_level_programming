#!/usr/bin/python3
"""This module defines a class square"""


class Square:
    """The class square"""
    def __init__(self, size=0):
        """Square is initialized with a size, size.
        Args:
            size(int): size of the square
        """
        self.size = size

    @property
    def size(self):
        """size: the size of the square.
        Note:
            size must be of type int and greater than 0 else
            the program will throw TypeError and ValueError respectively
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
        """Calculates the area of the square
        Returns:
            the area of the square
        """
        return (self.__size ** 2)

    def my_print(self):
        """Prints the square with size x size
        """
        if (self.__size == 0):
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
