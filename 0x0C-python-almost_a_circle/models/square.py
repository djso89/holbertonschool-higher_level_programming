#!/usr/bin/python3
"""
Square module for square class
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square """
    def __init__(self, size, x=0, y=0, id=None):
        """initialize Square instances """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """overloading __str__ method for square """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.height)
