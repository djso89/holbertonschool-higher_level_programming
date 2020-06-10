#!/usr/bin/python3
"""
Unittesting for Class - Base
"""

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class BaseTest(unittest.TestCase):
    """clas Base unittest """
    def test_increment(self):
        """test to see if id increments """
        Base.__Base__nb_objects = 0

        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        self.assertEqual(b2.id, 2)
