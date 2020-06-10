#!/usr/bin/python3
"""unittest for class rectangle """


import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class RectangleTest(unittest.TestCase):
    """Class rectangle unittest """
    def test_check_id(self):
        Base._Base__nb_objects = 0
        """test if id increments """
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)
        r2 = Rectangle(1, 6)
        self.assertEqual(r2.id, 2)
        r3 = Rectangle(2, 4)
        self.assertEqual(r3.id, 3)

    def tearDown(self):
        """ tearDown destroys any existing objects and processes """
        pass

    def test_type(self):
        """ Test type """
        r1 = Rectangle(1, 2)
        self.assertTrue(type(r1) is Rectangle)

    def test_check_input(self):
        """test if input id is able to set """
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)

    def test_check_width(self):
        """test width set of rectangle """
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.width, 10)

    def test_check_height(self):
        """test height set of rectangle """
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.height, 2)

    def test_check_x(self):
        """test x of rectangle """
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.x, 0)

        r2 = Rectangle(4, 3, 1, 2)
        self.assertEqual(r2.x, 1)

    def test_subclass_check(self):
        """check if Rectangle is sub of Base """
        self.assertEqual(issubclass(Rectangle, Base), True)

    def test_width_type(self):
        r1 = Rectangle(2, 7)
        self.assertEqual(r1.width, 2)