#!/usr/bin/python3
"""
"""
import json  # module json for serialize and deserialize


class FileStorage:
    """
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
        key = "{}.{}".format(obj["__class__"], obj["id"])
        self.__objects[key] = obj
        
    def save(self):
        """
        Serializes __objects to the
        JSON file (path: __file_path)
        """
        db = {key: val.to_dict for key, val in self.__objects.items()}
        with open(self.__file_path, 'w') as fp:
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
                for key, val in db.items():
                    new = eval(val['__class__'])(**val)
                    self.__objects[key] = new
        except IOError:
            pass
