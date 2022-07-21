#!/usr/bin/python3
class MagicCalculation:
    def __init__(self, radius=1):
        if (type(radius) is not int and type(radius) is not float):
            raise TypeError("radius must be a number")
        else:
            self.radius = radius
            return None

    def area(self):
        return ((self.radius ** 2) * pi)

    def circumference(self):
        return ((2 * pi) * self.radius)
