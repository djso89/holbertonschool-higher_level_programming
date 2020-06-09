#!/usr/bin/python3
"""
Rectangle Module
"""


from models.base import Base


class Rectangle(Base):
    """ Rectanggle Class """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    def integer_validator(self, name, value):
        """ Validate value """
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0 and name in ['width', 'height']:
            raise ValueError('{} must be > 0'.format(name))
        if value < 0 and name in ['x', 'y']:
            raise ValueError('{} must be >= 0'.format(name))

    @property
    def width(self):
        """get the width """
        return self.__width

    @width.setter
    def width(self, value):
        """set the width """
        self.integer_validator('width', value)
        self.__width = value

    @property
    def height(self):
        """get the height """
        return self.__height

    @height.setter
    def height(self, value):
        """set the height """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        self.__height = value

    @property
    def x(self):
        """get the x """
        return self.__x

    @x.setter
    def x(self, value):
        """set the x """
        self.integer_validator("x", value)
        self.__x = value

    @property
    def y(self):
        """get the y """
        return self.__y

    @y.setter
    def y(self, value):
        """set the y """
        self.integer_validator("y", value)
        self.__y = value
