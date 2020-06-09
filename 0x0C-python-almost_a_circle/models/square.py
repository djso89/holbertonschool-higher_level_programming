#!/usr/bin/python3
"""
Square module for square class
"""

from models.rectangle import Rectangle


def integer_validator(name, value):
    """ Validate value """
    if type(value) is not int:
        raise TypeError('{} must be an integer'.format(name))
    if value <= 0 and name in ['width']:
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

    def update(self, *args, **kwargs):
        """assigns an argument to each attributes """
        if args:
            attributes = ['id', 'size', 'x', 'y']
            for i, arg in enumerate(args):
                setattr(self, attributes[i], arg)
            return
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)

    def to_dictionary(self):
        """
        public method to get dictionary
        representation of Square
        """
        sq_dict = {}
        for key, value in self.__dict__.items():
            if key.startswith('_'):
                key = key[12:]
            if key.startswith('width') or key.startswith('height'):
                key = 'size'
            sq_dict[key] = value
        return sq_dict
