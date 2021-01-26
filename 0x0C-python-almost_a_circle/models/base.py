#!/usr/bin/python3
"""Module with Base geometry class
"""


import json
import csv


class Base:
    """Base geometry class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializing Base class"""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns a JSON string made out of dicts"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Returns dictionary representations of geometry objects from JSON"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Creates a geometry object from a dictionary"""
        from .rectangle import Rectangle
        from .square import Square
        if cls is Rectangle:
            newrect = Rectangle(1, 1, 0, 0, 0)
            newrect.update(**dictionary)
            return newrect
        elif cls is Square:
            newsquare = Square(1, 0, 0, 0)
            newsquare.update(**dictionary)
            return newsquare

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        from .rectangle import Rectangle
        from .square import Square
        listcpy = list_objs.copy()
        for idx in range(len(listcpy)):
            listcpy[idx] = listcpy[idx].to_dictionary()
        if cls is Rectangle:
            with open("Rectangle.json", "w") as f:
                f.write(Base.to_json_string(listcpy))
        elif cls is Square:
            with open("Square.json", "w") as f:
                f.write(Base.to_json_string(listcpy))

    @classmethod
    def load_from_file(cls):
        """Loads from JSON string"""
        from .rectangle import Rectangle
        from .square import Square
        if cls is Rectangle:
            with open("Rectangle.json", "r") as f:
                retlist = Base.from_json_string(f.read())
                if retlist == "":
                    return []
                for idx in range(len(retlist)):
                    retlist[idx] = Rectangle.create(**retlist[idx])
                return retlist
        elif cls is Square:
            with open("Square.json", "r") as f:
                retlist = Base.from_json_string(f.read())
                if retlist == "":
                    return []
                for idx in range(len(retlist)):
                    retlist[idx] = Square.create(**retlist[idx])
                return retlist

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes a list of Rectangles/Squares in CSV"""
        from .rectangle import Rectangle
        from .square import Square
        listcpy = list_objs.copy()
        for idx in range(len(listcpy)):
            listcpy[idx] = listcpy[idx].to_dictionary()
        if cls is Rectangle:
            with open("Rectangle.csv", "w") as f:
                csvwriter = csv.writer(f)
                for dicty in listcpy:
                    newlist = []
                    newlist.append(dicty["id"])
                    newlist.append(dicty["width"])
                    newlist.append(dicty["height"])
                    newlist.append(dicty["x"])
                    newlist.append(dicty["y"])
                    csvwriter.writerow(newlist)
        if cls is Square:
            with open("Square.csv", "w") as f:
                csvwriter = csv.writer(f)
                for dicty in listcpy:
                    newlist = []
                    newlist.append(dicty["id"])
                    newlist.append(dicty["size"])
                    newlist.append(dicty["x"])
                    newlist.append(dicty["y"])
                    csvwriter.writerow(newlist)

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes a list of Rectangles/Squares in CSV"""
        from .rectangle import Rectangle
        from .square import Square
        if cls is Rectangle:
            with open("Rectangle.csv", "r") as f:
                csvreader = csv.reader(f)
                retlist = []
                for row in csvreader:
                    newrect = Rectangle(int(row[1]), int(row[2]), int(row[3]),
                                        int(row[4]), row[0])
                    retlist.append(newrect)
                return retlist
        elif cls is Square:
            with open("Square.csv", "r") as f:
                csvreader = csv.reader(f)
                retlist = []
                for row in csvreader:
                    newsquare = Square(int(row[1]), int(row[2]),
                                       int(row[3]), row[0])
                    retlist.append(newsquare)
                return retlist
