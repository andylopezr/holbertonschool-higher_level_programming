#!/usr/bin/python3
"""Unittest module for Square class"""
import unittest
import json
from io import StringIO
from contextlib import redirect_stdout
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


idct = 0
notintegers = [3.5, [], {}, {1, 2}, {1: 2, 3: 4}, "hi", b"hi", ()]


class TestSquare(unittest.TestCase):
    """Tests the square class"""

    def testbasicrect(self):
        """Makes a basic square with only valid width/height"""
        global idct
        a = Square(10)
        idct += 1
        self.assertEqual(a.id, idct)
        self.assertEqual(a.width, 10)
        self.assertEqual(a.height, 10)

    def testnegsize(self):
        """Tries a negative size"""
        with self.assertRaises(ValueError) as e:
            a = Square(-10)
        self.assertEqual(e.exception.args[0], "width must be > 0")

    def testzerosize(self):
        """Tries a zero width"""
        with self.assertRaises(ValueError) as e:
            a = Square(0)
        self.assertEqual(e.exception.args[0], "width must be > 0")

    def testsqwithx(self):
        """Make a square with only an x position"""
        global idct
        a = Square(10, 5)
        idct += 1
        self.assertEqual(a.id, idct)
        self.assertEqual(a.width, 10)
        self.assertEqual(a.height, 10)
        self.assertEqual(a.x, 5)

    def testsqwithy(self):
        """Make a square with x and y position"""
        global idct
        a = Square(10, 5, 3)
        idct += 1
        self.assertEqual(a.id, idct)
        self.assertEqual(a.width, 10)
        self.assertEqual(a.height, 10)
        self.assertEqual(a.x, 5)
        self.assertEqual(a.y, 3)

    def testnegx(self):
        """Tries a negative x"""
        with self.assertRaises(ValueError) as e:
            a = Square(10, -1)
        self.assertEqual(e.exception.args[0], "x must be >= 0")

    def testnegy(self):
        """Tries a negative y"""
        with self.assertRaises(ValueError) as e:
            a = Square(10, 1, -1)
        self.assertEqual(e.exception.args[0], "y must be >= 0")

    def testid(self):
        """Test square construction given an id"""
        a = Square(1, 2, 3, 4)
        self.assertEqual(a.id, 4)
        self.assertEqual(a.width, 1)
        self.assertEqual(a.height, 1)
        self.assertEqual(a.x, 2)
        self.assertEqual(a.y, 3)

    def testwidthtype(self):
        """Test invalid types for size"""
        for ele in notintegers:
            with self.subTest(type=type(ele)):
                with self.assertRaises(TypeError) as e:
                    Square(ele)
                self.assertEqual(e.exception.args[0],
                                 "width must be an integer")

    def testxtype(self):
        """Test invalid types for x"""
        for ele in notintegers:
            with self.subTest(type=type(ele)):
                with self.assertRaises(TypeError) as e:
                    Square(4, ele)
                self.assertEqual(e.exception.args[0],
                                 "x must be an integer")

    def testytype(self):
        """Test invalid types for y"""
        for ele in notintegers:
            with self.subTest(type=type(ele)):
                with self.assertRaises(TypeError) as e:
                    Square(4, 5, ele)
                self.assertEqual(e.exception.args[0],
                                 "y must be an integer")

    def testarea(self):
        """Tests rectangle area function"""
        global idct
        a = Square(4)
        idct += 1
        self.assertEqual(a.area(), 16)

    def testarea2(self):
        """tests rectangle area function"""
        a = Square(4, 100, 20, 10)
        self.assertEqual(a.area(), 16)

    def testprint(self):
        """Tests printing a basic square"""
        global idct
        a = Square(3)
        idct += 1
        out = StringIO()
        with redirect_stdout(out):
            a.display()
        self.assertEqual(out.getvalue(), "###\n###\n###\n")

    def testprint2(self):
        """Tests printing a square with offset"""
        a = Square(3, 3, 4, 10)
        out = StringIO()
        with redirect_stdout(out):
            a.display()
        self.assertEqual(out.getvalue(), "\n\n\n\n   ###\n   ###\n   ###\n")

    def teststr(self):
        """Tests stringing a basic square"""
        global idct
        a = Square(4)
        idct += 1
        self.assertEqual(str(a), "[Square] ({}) 0/0 - 4".format(idct))

    def teststr2(self):
        """Tests stringing a rectangle with offset"""
        a = Square(4, 6, 7, 3)
        self.assertEqual(str(a), "[Square] (3) 6/7 - 4")

    def testupdate(self):
        """Tests square update function with positional args"""
        a = Square(4, 6, 7, 3)
        a.update(10)
        self.assertEqual(str(a), "[Square] (10) 6/7 - 4")
        a.update(11, 12)
        self.assertEqual(str(a), "[Square] (11) 6/7 - 12")
        a.update(11, 12, 3)
        self.assertEqual(str(a), "[Square] (11) 3/7 - 12")
        a.update(11, 12, 3, 9)
        self.assertEqual(str(a), "[Square] (11) 3/9 - 12")

    def testupdatetoomany(self):
        """Tests square update function with extra positional args"""
        a = Square(4, 6, 7, 3)
        a.update(11, 5, 15, 12, [], "hello", ())
        self.assertEqual(str(a), "[Square] (11) 15/12 - 5")

    def testtodict(self):
        """Tests rectangle to dictionary function"""
        a = Square(4, 6, 7, 3)
        dictcomp = {"id": 3, "size": 4, "x": 6, "y": 7}
        self.assertEqual(a.to_dictionary(), dictcomp)
