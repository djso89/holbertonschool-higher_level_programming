#!/usr/bin/python3
"""Class Rectangle"""


class Rectangle:
    """Initialize an empty class"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize Rectangle"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """return the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set the width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """return the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set the height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """return the area"""
        return self.__height * self.__width

    def perimeter(self):
        """calculate the perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        rect_str = ""

        if self.__height == 0 or self.__width == 0:
            return ""
        for row in range(self.__height):
            for col in range(self.__width):
                rect_str += str(self.print_symbol)
            if row < self.__height - 1:
                rect_str += "\n"
        return rect_str

    def __repr__(self):
        """represent in string"""
        r = "Rectangle({}, {})"
        return r.format(str(self.__width), str(self.__height))

    def __del__(self):
        """delete rectangle"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
