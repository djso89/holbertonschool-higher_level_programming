#!/usr/bin/python3
'''defining class Square'''


class Square:
    '''initializing private attribute'''
    def __init__(self, size=0):
        '''assign the size'''
        self.__size = size
        '''check if the size is integer'''
        if not isinstance(size, int):
            '''raise the Type Error'''
            raise TypeError("size must be an integer")
        ''' check if size is negative number'''
        elif size < 0:
            '''raise value error '''
            raise ValueError("size must be >= 0")
