#!/usr/bin/python3
"""Unittesting for Class Square"""

import unittest
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test Class Square"""

    def setUp(self):
        """Resets objects"""
        Base._Base__nb_objects = 0

    def test_base(self):
        """Test if inherits"""
        r = Square(23)
        r1 = Square(12)
        self.assertEqual(r.id, 1)
        self.assertEqual(r1.id, 2)
        self.assertEqual(issubclass(Square, Base), True)
