#!/usr/bin/python3
'''defining class Square'''


class Square:
    '''initializing private attribute'''
    def __init__(self, size=0):
        '''assign the size'''
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
