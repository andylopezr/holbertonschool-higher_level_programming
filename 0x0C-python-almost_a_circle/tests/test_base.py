#!/usr/bin/python3
"""Unittest module for Base class"""
import unittest
import json
from io import StringIO
from contextlib import redirect_stdout
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


idct = 0
notintegers = [3.5, [], {}, {1, 2}, {1: 2, 3: 4}, "hi", b"hi", ()]


class TestBase(unittest.TestCase):
    """Test cases for Base geometry class"""

    def testdefault(self):
        global idct
        a = Base()
        idct += 1
        self.assertEqual(a.id, idct)

    def testincrement(self):
        global idct
        a = Base()
        idct += 1
        self.assertEqual(a.id, idct)
        b = Base()
        idct += 1
        self.assertEqual(b.id, idct)
        c = Base()
        idct += 1
        self.assertEqual(c.id, idct)
        d = Base()
        idct += 1
        self.assertEqual(d.id, idct)

    def testspecific(self):
        global idct
        a = Base(19)
        self.assertEqual(a.id, 19)

    def testspecincrement(self):
        """Tests that setting a specific id does not mess up incrementer"""
        global idct
        a = Base()
        idct += 1
        self.assertEqual(a.id, idct)
        b = Base(19)
        self.assertEqual(b.id, 19)
        c = Base()
        idct += 1
        self.assertEqual(c.id, idct)
        d = Base()
        idct += 1
        self.assertEqual(d.id, idct)

    def testnonnum(self):
        """Tries some non-numbers to make sure it assigns that as id"""
        global idct
        astr = "hello"
        a = Base(astr)
        blist = [10, 14, 30]
        b = Base(blist)
        self.assertEqual(a.id, astr)
        self.assertEqual(b.id, blist)

    def testtojson(self):
        """Test Base to_json_string class method"""
        dicty = {"id": 5, "class": "string", "list": [], "set": {}}
        self.assertEqual(json.dumps([dicty]), Base.to_json_string([dicty]))

    def testtojson2(self):
        """Test Base to_json_string class method with multiple dicts"""
        dicty = {"id": 5, "class": "string", "list": [], "set": {}}
        self.assertEqual(json.dumps([dicty, dicty]),
                         Base.to_json_string([dicty, dicty]))

    def testtojsonempty(self):
        """Test Base to_json_string class method with empty list of dicts"""
        self.assertEqual("[]", Base.to_json_string([]))

    def testfromjson(self):
        """Test Base from_json_string class method. JSON to dict"""
        dicty = {"id": 5, "class": "string", "list": [], "set": {}}
        self.assertEqual([dicty], Base.from_json_string(json.dumps([dicty])))

    def testfromjson(self):
        """Test Base from_json_string class method
        Multiple dicts. JSON to dict.
        """
        dicty = {"id": 5, "class": "string", "list": [], "set": {}}
        self.assertEqual([dicty, dicty],
                         Base.from_json_string(json.dumps([dicty, dicty])))

    def testdicttorect(self):
        """Test making a rectangle from a dict"""
        dicty = {"id": 5, "width": 3, "height": 4, "x": 2, "y": 1}
        a = Rectangle(3, 4, 2, 1, 5)
        b = Rectangle.create(**dicty)
        self.assertEqual(a.id, b.id)
        self.assertEqual(a.width, b.width)
        self.assertEqual(a.height, b.height)
        self.assertEqual(a.x, b.x)
        self.assertEqual(a.y, b.y)

    def testdicttosq(self):
        """Test making a Square from a dict"""
        dicty = {"id": 5, "size": 3, "x": 2, "y": 1}
        a = Square(3, 2, 1, 5)
        b = Square.create(**dicty)
        self.assertEqual(a.id, b.id)
        self.assertEqual(a.width, b.width)
        self.assertEqual(a.height, b.height)
        self.assertEqual(a.x, b.x)
        self.assertEqual(a.y, b.y)
