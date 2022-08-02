#!/usr/bin/python3
"""Module that uses BaseGeometry
imports:
    BaseGeometry
Attributes:
    BaseGeometry, Rectangle
"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """A Rectangle class that uses the Basegeometry"""

    def __init__(self, width, height):
        """instatiation of rectangle with width and height
        Attributes:
            width, height
        """

        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def __str__(self):
        """return a string representation of the class"""

        return f"[Rectangle] {self.__width}/{self.__height}"

    def area(self):
        """Calculates the area of the rectangle"""

        return self.__width * self.__height

    def print(self):
        """prints a string representation of the class"""

        print(f"[Rectangle] {self.__width}/{self.__height}")
