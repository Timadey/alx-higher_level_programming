#!/usr/bin/python3
"""This module defines class magic calculation"""


class MagicClass:
    """Class magic"""
    def __init__(self, radius=1):
        """Initialized class with radius"""

        if (type(radius) is not int and type(radius) is not float):
            raise TypeError("radius must be a number")
        else:
            self.radius = radius
            return None

    def area(self):
        """Return the area"""

        return ((self.radius ** 2) * pi)

    def circumference(self):
        """Return thr circumference"""

        return ((2 * pi) * self.radius)
