#!/usr/bin/python3
"""Unittest module for Rectangle class"""
import unittest
import json
from io import StringIO
from contextlib import redirect_stdout
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


idct = 0
notintegers = [3.5, [], {}, {1, 2}, {1: 2, 3: 4}, "hi", b"hi", ()]


class TestRectangle(unittest.TestCase):
    """Tests the rectangle class"""

    def testbasicrect(self):
        """Makes a basic rectangle with only valid width/height"""
        global idct
        a = Rectangle(10, 5)
        idct += 1
        self.assertEqual(a.id, idct)
        self.assertEqual(a.width, 10)
        self.assertEqual(a.height, 5)

    def testnegwidth(self):
        """Tries a negative width"""
        with self.assertRaises(ValueError) as e:
            a = Rectangle(-10, 5)
        self.assertEqual(e.exception.args[0], "width must be > 0")

    def testzerowidth(self):
        """Tries a zero width"""
        with self.assertRaises(ValueError) as e:
            a = Rectangle(0, 5)
        self.assertEqual(e.exception.args[0], "width must be > 0")

    def testnegheight(self):
        """Tries a negative height"""
        with self.assertRaises(ValueError) as e:
            a = Rectangle(10, -5)
        self.assertEqual(e.exception.args[0], "height must be > 0")

    def testzeroheight(self):
        """Tries a zero height"""
        with self.assertRaises(ValueError) as e:
            a = Rectangle(10, 0)
        self.assertEqual(e.exception.args[0], "height must be > 0")

    def testrectwithx(self):
        """Make a rectangle with only an x position"""
        global idct
        a = Rectangle(10, 5, 3)
        idct += 1
        self.assertEqual(a.id, idct)
        self.assertEqual(a.width, 10)
        self.assertEqual(a.height, 5)
        self.assertEqual(a.x, 3)

    def testrectwithy(self):
        """Make a rectangle with x and y position"""
        global idct
        a = Rectangle(10, 5, 3, 2)
        idct += 1
        self.assertEqual(a.id, idct)
        self.assertEqual(a.width, 10)
        self.assertEqual(a.height, 5)
        self.assertEqual(a.x, 3)
        self.assertEqual(a.y, 2)

    def testnegx(self):
        """Tries a negative x"""
        with self.assertRaises(ValueError) as e:
            a = Rectangle(10, 5, -1)
        self.assertEqual(e.exception.args[0], "x must be >= 0")

    def testnegy(self):
        """Tries a negative y"""
        with self.assertRaises(ValueError) as e:
            a = Rectangle(10, 5, 1, -1)
        self.assertEqual(e.exception.args[0], "y must be >= 0")

    def testid(self):
        """Test rectangle construction given an id"""
        a = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(a.id, 5)
        self.assertEqual(a.width, 1)
        self.assertEqual(a.height, 2)
        self.assertEqual(a.x, 3)
        self.assertEqual(a.y, 4)

    def testwidthtype(self):
        """Test invalid types for width"""
        for ele in notintegers:
            with self.subTest(type=type(ele)):
                with self.assertRaises(TypeError) as e:
                    Rectangle(ele, 4)
                self.assertEqual(e.exception.args[0],
                                 "width must be an integer")

    def testheighttype(self):
        """Test invalid types for height"""
        for ele in notintegers:
            with self.subTest(type=type(ele)):
                with self.assertRaises(TypeError) as e:
                    Rectangle(4, ele)
                self.assertEqual(e.exception.args[0],
                                 "height must be an integer")

    def testxtype(self):
        """Test invalid types for x"""
        for ele in notintegers:
            with self.subTest(type=type(ele)):
                with self.assertRaises(TypeError) as e:
                    Rectangle(4, 5, ele)
                self.assertEqual(e.exception.args[0],
                                 "x must be an integer")

    def testytype(self):
        """Test invalid types for y"""
        for ele in notintegers:
            with self.subTest(type=type(ele)):
                with self.assertRaises(TypeError) as e:
                    Rectangle(4, 5, 6, ele)
                self.assertEqual(e.exception.args[0],
                                 "y must be an integer")

    def testarea(self):
        """Tests rectangle area function"""
        global idct
        a = Rectangle(3, 4)
        idct += 1
        self.assertEqual(a.area(), 12)

    def testarea2(self):
        """tests rectangle area function"""
        a = Rectangle(4, 5, 100, 20, 10)
        self.assertEqual(a.area(), 20)

    def testprint(self):
        """Tests printing a basic rectangle"""
        global idct
        a = Rectangle(4, 3)
        idct += 1
        out = StringIO()
        with redirect_stdout(out):
            a.display()
        self.assertEqual(out.getvalue(), "####\n####\n####\n")

    def testprint2(self):
        """Tests printing a rectangle with offset"""
        a = Rectangle(4, 3, 3, 4, 10)
        out = StringIO()
        with redirect_stdout(out):
            a.display()
        self.assertEqual(out.getvalue(), "\n\n\n\n   ####\n   ####\n   ####\n")

    def teststr(self):
        """Tests stringing a basic rectangle"""
        global idct
        a = Rectangle(4, 3)
        idct += 1
        self.assertEqual(str(a), "[Rectangle] ({}) 0/0 - 4/3".format(idct))

    def teststr2(self):
        """Tests stringing a rectangle with offset"""
        a = Rectangle(4, 3, 6, 7, 3)
        self.assertEqual(str(a), "[Rectangle] (3) 6/7 - 4/3")

    def testupdate(self):
        """Tests rectangle update function with positional args"""
        a = Rectangle(4, 3, 6, 7, 3)
        a.update(10)
        self.assertEqual(str(a), "[Rectangle] (10) 6/7 - 4/3")
        a.update(11, 5)
        self.assertEqual(str(a), "[Rectangle] (11) 6/7 - 5/3")
        a.update(11, 5, 6)
        self.assertEqual(str(a), "[Rectangle] (11) 6/7 - 5/6")
        a.update(11, 5, 6, 15)
        self.assertEqual(str(a), "[Rectangle] (11) 15/7 - 5/6")
        a.update(11, 5, 6, 15, 12)
        self.assertEqual(str(a), "[Rectangle] (11) 15/12 - 5/6")

    def testupdatetoomany(self):
        """Test rectangle update function with extra args"""
        a = Rectangle(4, 3, 6, 7, 3)
        a.update(11, 5, 6, 15, 12, [], "hello", ())
        self.assertEqual(str(a), "[Rectangle] (11) 15/12 - 5/6")

    def testtodict(self):
        """Tests rectangle to dictionary function"""
        a = Rectangle(4, 3, 6, 7, 3)
        dictcomp = {"id": 3, "width": 4, "height": 3, "x": 6, "y": 7}
        self.assertEqual(a.to_dictionary(), dictcomp)
