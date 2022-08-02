#!/usr/bin/python3
"""A Square module
Imports:
    Rectangle
Attributes:
    Square
"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """A square class"""

    def __init__(self, size):
        """Initialise with @size"""

        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def __str__(self):
        """Return the string representation of the square"""

        return f"[Square] {self.__size}/{self.__size}"

    def area(self):
        """Returns the area of the square"""

        return super().area()
