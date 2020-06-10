#!/usr/bin/python3
"""unittest for class rectangle """


import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class RectangleTest(unittest.TestCase):
    """Class rectangle unittest """
    def test_check_id(self):
        """test if id increments """
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)
        r2 = Rectangle(1, 6)
        self.assertEqual(r2.id, 1)
