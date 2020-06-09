#!/usr/bin/python3
"""
Rectangle Module
"""


from models.base import Base


def integer_validator(name, value):
    """ Validate value """
    if type(value) is not int:
        raise TypeError('{} must be an integer'.format(name))
    if value <= 0 and name in ['width', 'height']:
        raise ValueError('{} must be > 0'.format(name))
    if value < 0 and name in ['x', 'y']:
        raise ValueError('{} must be >= 0'.format(name))


class Rectangle(Base):
    """ Rectanggle Class """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        integer_validator('width', width)
        self.__width = width
        integer_validator('height', height)
        self.__height = height
        integer_validator('x', x)
        self.__x = x
        integer_validator('y', y)
        self.__y = y

    @property
    def width(self):
        """get the width """
        return self.__width

    @width.setter
    def width(self, value):
        """set the width """
        integer_validator('width', value)
        self.__width = value

    @property
    def height(self):
        """get the height """
        return self.__height

    @height.setter
    def height(self, value):
        """set the height """
        integer_validator('height', value)
        self.__height = value

    @property
    def x(self):
        """get the x """
        return self.__x

    @x.setter
    def x(self, value):
        """set the x """
        integer_validator("x", value)
        self.__x = value

    @property
    def y(self):
        """get the y """
        return self.__y

    @y.setter
    def y(self, value):
        """set the y """
        integer_validator("y", value)
        self.__y = value

    def area(self):
        """get the area of rectangle """
        return self.__width * self.__height

    def display(self):
        """Prints in stdout the rectangle """
        for i in range(self.__height):
            print('#' * self.__width)
