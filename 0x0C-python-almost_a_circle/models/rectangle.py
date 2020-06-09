#!/usr/bin/python3
"""
Rectangle Module
"""

from models.base import Base


def Rectangle(base):
    """ Rectanggle Class """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y =y

    @property
    def width(self):
        """get the width """
        return self.width

    @width.setter
    def width(self, value):
        """set the width """
        self.width = value

    @property
    def height(self):
        """get the height """
        return self.height

    @height.setter
    def height(self, value):
        """set the height """
        self.height = value

    @property
    def x(self):
        """get the x """
        return self.x

    @x.setter
    def x(self, value):
        """set the x """
        self.x = value

    @property
    def y(self):
        """get the y """
        return self.y

    @x.setter
    def y(self, value):
        """set the y """
        self.y = value
