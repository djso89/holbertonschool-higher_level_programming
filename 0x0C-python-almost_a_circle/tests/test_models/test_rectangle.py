#!/usr/bin/python3
"""unittest for class rectangle """


import unittest
import sys
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
from io import StringIO


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

    def test_area(self):
        r1 = Rectangle(10, 2)
        rect_area = r1.area()
        self.assertEqual(rect_area, 20)

    def test_display_no_xy(self):
        out = StringIO()
        sys.stdout = out
        r1 = Rectangle(2, 3)
        r1.display()
        sys.stdout = sys.__stdout__
        assert out.getvalue() == "##\n##\n##\n"

    def test_display(self):
        out = StringIO()
        sys.stdout = out
        r1 = Rectangle(2, 3, 1, 2)
        r1.display()
        sys.stdout = sys.__stdout__
        assert out.getvalue() == "\n\n ##\n ##\n ##\n"

    def test_subclass_check(self):
        """check if Rectangle is sub of Base """
        self.assertEqual(issubclass(Rectangle, Base), True)

    def test_width_type_error(self):
        """test typeerror for width in rectangle """
        self.assertRaisesRegex(
            TypeError,
            'width must be an integer',
            Rectangle,
            'string', 2, 0, 0, 12
            )

    def test_width_type_error1(self):
        """another test for width in rectangle """
        self.assertRaisesRegex(
            TypeError,
            'width must be an integer',
            Rectangle,
            [2, 4, 9, 5], 2, 0, 1, 12
            )

    def test_width_negative(self):
        """test when width is negative """
        self.assertRaisesRegex(
            ValueError,
            'width must be > 0',
            Rectangle,
            -7, 2, 2, 1, 0
            )

    def test_update(self):
        """test for update """
        out = StringIO()
        sys.stdout = out
        r = Rectangle(12, 7, 2, 5)
        r.update(87)
        r.update(87, 2)
        r.update(87, 2, 3, 4)
        r.update(87, 2, 3, 4, 5)
        print(r)
        sys.stdout == sys.__stdout__
        assert out.getvalue() == "[Rectangle] (87) 4/5 - 2/3\n"

    def test_str_method(self):
        """test the __str__ public method """
        out = StringIO()
        sys.stdout = out
        r = Rectangle(2, 2, 2, 2, 12)
        print(r)
        sys.stdout = sys.__stdout__
        assert out.getvalue() == "[Rectangle] (12) 2/2 - 2/2\n"

    def test_height_number_str(self):
        """test if height is assigned as string number """
        self.assertRaisesRegex(
            TypeError,
            'height must be an integer',
            Rectangle,
            1, "2", 0, 0, 12
            )

    def test_x_number_str(self):
        """test if x is assigned as string number """
        self.assertRaisesRegex(
            TypeError,
            "x must be an integer",
            Rectangle,
            1, 2, "32"
            )

    def test_y_number_str(self):
        """test if y is assigned as string number """
        self.assertRaisesRegex(
            TypeError,
            "y must be an integer",
            Rectangle,
            1, 2, 3, "45"
            )

    def test_width_zero(self):
        """test if width is zero """
        self.assertRaisesRegex(
            ValueError,
            "width must be > 0",
            Rectangle,
            0, 2
            )

    def test_height_zero(self):
        """test if height is zero """
        self.assertRaisesRegex(
            ValueError,
            "height must be > 0",
            Rectangle,
            5, 0
            )

    def test_xy_negative(self):
        self.assertRaisesRegex(
            ValueError,
            "x must be >= 0",
            Rectangle,
            5, 4, -1
            )

        self.assertRaisesRegex(
            ValueError,
            "y must be >= 0",
            Rectangle,
            5, 1, 2, -4
            )

    def test_to_dict(self):
        r3 = Rectangle(1, 4, 2, 5, 32)
        comp_list = {'id': 32, 'width': 1, 'height': 4, 'x': 2, 'y': 5}
        r_list = r3.to_dictionary()
        self.assertEqual(r_list, comp_list)
