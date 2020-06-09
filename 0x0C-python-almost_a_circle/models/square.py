#!/usr/bin/python3
"""
Square module for square class
"""

from models.rectangle import Rectangle


def integer_validator(name, value):
    """ Validate value """
    if type(value) is not int:
        raise TypeError('{} must be an integer'.format(name))
    if value <= 0 and name in ['width', 'height']:
        raise ValueError('{} must be > 0'.format(name))
    if value < 0 and name in ['x', 'y']:
        raise ValueError('{} must be >= 0'.format(name))


class Square(Rectangle):
    """class Square """
    def __init__(self, size, x=0, y=0, id=None):
        """initialize Square instances """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """overloading __str__ method for square """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.height)

    @property
    def size(self):
        """get the size of square """
        return self.width

    @size.setter
    def size(self, value):
        """set size """
        integer_validator('width', value)
        self.height = value
        self.width = value
