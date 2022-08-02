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
        """Instantiate with @size"""

        super().__init__(size, size)
