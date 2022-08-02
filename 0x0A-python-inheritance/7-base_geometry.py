#!/usr/bin/python3
"""Geometry module

Attributes:
    BaseGeometry
"""


class BaseGeometry:
    """A Geometry class"""

    def area(self):
        """Raise exception"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates a value

        Raises:
            TypeError: `name` must be an integer if `value` is not integer
            ValueError: `name` must be greater than 0 if `value` is <= 0
        """

        if not type(value) == int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
