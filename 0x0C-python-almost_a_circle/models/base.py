#!/usr/bin/python3
"""Base module """

import json


class Base:
    """Base Class """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON String representation
        of list_dictionaries
        """
        if not list_dictionaries:
            return "[]"
        if type(list_dictionaries) != list:
            raise TypeError("list_dictionaries must be a list of dictionaries")
        return json.dumps(list_dictionaries)
