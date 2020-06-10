#!/usr/bin/python3
"""
Unittesting for Class - Base
"""

import unittest
import sys
from io import StringIO
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class BaseTest(unittest.TestCase):
    """class Base unittest """
    def test_increment(self):
        """test to see if id increments """
        Base.__Base__nb_objects = 0

        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        self.assertEqual(b2.id, 2)

        b3 = Base()
        self.assertEqual(b3.id, 3)

        b4 = Base(-12)
        self.assertEqual(b4.id, -12)

    def test_rect_create(self):
        comp_dict =  {'id': 89, 'width': 1, 'height': 1, 'x': 0, 'y': 0}
        P = Rectangle.create(**{'id': 89})
        self.assertEqual(P.to_dictionary(), comp_dict)

    def test_save_to_file(self):
        r1 = Rectangle(1, 3, 4, 2, 8)
        d1 = r1.to_dictionary()
        r2 = Rectangle(1, 5)
        r3 = Rectangle(3, 5, 8, 2)
        Rectangle.save_to_file([r1, r2, r3])
        list_objs_rect = Rectangle.load_from_file()
        self.assertIsInstance(list_objs_rect[0], Rectangle)
        self.assertEqual(list_objs_rect[0].to_dictionary(), d1)

        Rectangle.save_to_file([])
        list_objs_rect = Rectangle.load_from_file()
        self.assertEqual(list_objs_rect, [])

    def test_save_to_file_None(self):
        Rectangle.save_to_file(None)
        list_objs_rect = Rectangle.load_from_file()
        self.assertEqual(list_objs_rect, [])
