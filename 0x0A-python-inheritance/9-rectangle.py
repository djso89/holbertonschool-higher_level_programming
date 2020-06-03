#!/usr/bin/python3
"""
BaseGeometry module
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


"""Class Rectangle """


class Rectangle(BaseGeometry):
    """Rectangle class """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        return "[Rectangle] 3/5 " + str(self.__width) + "/" + str(self.__height)
    def area(self):
        return self.__height * self.__width
