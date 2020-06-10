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

    @classmethod
    def save_to_file(cls, list_objs):
        """write the JSON string rep. of list_obj to a file """
        if not list_objs:
            objects = []
        else:
            objects = [obj.to_dictionary() for obj in list_objs]
        with open(cls.__name__ + ".json", "w+") as jf:
            jf.write(cls.to_json_string(objects))

    @staticmethod
    def from_json_string(json_string):
        if json_string is None:
            return []
        if type(json_string) != str:
            raise TypeError("json_string must be string")
        return json.loads(json_string)
