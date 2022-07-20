#!/usr/bin/python3
class Square:
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (type(value) != tuple or value[0] < 0 or value[1] < 1):
            raise TypeError("posiion must be a tuple of 2 positive integers")
        self.__position = value

    @size.setter
    def size(self, value):
        if (type(value) != int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return (self.__size ** 2)

    def my_print(self):
        """ I don't understand
        will implement later """
