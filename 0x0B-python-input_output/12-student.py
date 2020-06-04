#!/usr/bin/python3
"""student module """


class Student:
    """class Student """
    def __init__(self, first_name, last_name, age):
        """initialize Student object """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        new_dict = {}
        if attrs is not None:
            for key in attrs:
                if key in self.__dict__:
                    new_dict[key] = self.__dict__[key]
            return new_dict
        return self.__dict__
