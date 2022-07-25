
#!/usr/bin/python3
"""Defines a Rectangle class"""

class Rectangle:
    """Defines a rectangle"""

    # Magic methods

    def __init__(self, width=0, height=0):
        """Initiates the rectangle
        Args:
            width: optional, width of the rectangle
            height: optional, height of the rectangle
        """

        self.width = width
        self.height = height
    
    
    def __str__(self):
        """prints the rectangle with the character #"""

        if self.__height == 0 or self.__width == 0:
            return ""

        rec = ""
        for h in range(self.__height):
            for w in range(self.__width):
                rec += "#"
            if h != self.__height - 1:
                rec += '\n'
        return rec

    
    def __repr__(self):
        """Return a string representation of the rectangle"""

        return f"Rectangle({self.__width}, {self.__height})"

    
    def __del__(self):
        """Prints to the screen when a rectangle is deleted"""

        print("Bye rectangle...")

    
    # Properties and setters

    @property
    def width(self):
        """Get the width of a rectangle
        Args:
            value: value to set a rectangle width

        Raises:
            TypeError: "width must be an integer" if width is not int type
            ValueError: "width must be >= 0" if width is less than 0

        Returns: The width of the rectangle
        """

        return self.__width

    
    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value
    
    
    @property
    def height(self):
        """Get the height of a rectangle
        Args:
            value: value to set a rectangle width

        Raises:
            TypeError: "height must be an integer" if height is not int type
            ValueError: "height must be >= 0" if height is less than 0

        Returns: The height of the rectangle
        """

        return self.__height

    
    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value


    # Methods

    def area(self):
        """Returns the area of a rectangle"""

        return self.__width * self.__height

    
    def perimeter(self):
        """Returns the perimeter of a rectangle"""

        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__width + self.__height)

    
    def print(self):
        """prints the rectangle with the character #"""

        if self.__height == 0 or self.__width == 0:
            return ""

        for h in range(self.__height):
            for w in range(self.__width):
                print("#", end="")
            if h != self.__height:
                print()
