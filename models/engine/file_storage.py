#!/usr/bin/python3
"""
FileStorage module
"""
import json  # module json for serialize and deserialize
from models.base_model import BaseModel  # import class model
from models.city import City  # import class City
from models.user import User  # import class User
from models.amenity import Amenity  # import class Amenity
from models.place import Place  # import class Place
from models.state import State  # import class State
from models.review import Review  # import class Review

class FileStorage:
    """
    Class FileStorage
    """

    __file_path = 'file.json'
    __objects = {}


    def __init__(self):
        """ Constructor """
        
    def all(self):
        """ Returns the dictionary __objects """
        return self.__objects
        
    def new(self, obj):
        """
        Sets in __objects the obj with 
        key <obj class name>.id
        """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj
        
    def save(self):
        """
        Serializes __objects to the
        JSON file (path: __file_path)
        """
        db = {key: val.to_dict() for key, val in self.__objects.items()}
        with open(self.__file_path, 'w', encoding='utf-8') as fp:
            json.dump(db, fp)

    def reload(self):
        """
        Deserializes the JSON file to __objects
        (only if the JSON file (__file_path)
        exists ; otherwise, do nothing. If the file doesn’t exist
        no exception should be raised)
        """
        try:
            with open(self.__file_path, 'r') as fp:
                db = json.load(fp)
                for val in db.values():
                    new = eval(val['__class__'])(**val)
                    self.new(new)
        except IOError:
            pass
