#!/usr/bin/python3
"""
Rectangle module
"""
Rectangle = __import__('9-rectangle').Rectangle


"""Class Square """


class Square(Rectangle):
    """Square class """
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """return the area """
        return self.__size ** 2
