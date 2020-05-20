#!/usr/bin/python3
'''Define class Square '''


class Square:
    '''create square object'''
    def __init__(self, size=0):
        ''' initialize size'''
        self.__size = size

    def area(self):
        '''calculate the area of square '''
        return self.__size * self.__size

    @property
    def size(self):
        ''' retrieve the size'''
        return self.__size

    @size.setter
    def size(self, value):
        ''' set the value to size '''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
