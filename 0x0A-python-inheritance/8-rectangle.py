#!/usr/bin/python3
"""Module that uses BaseGeometry
imports:
    BaseGeometry
Attributes:
    Rectangle
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
