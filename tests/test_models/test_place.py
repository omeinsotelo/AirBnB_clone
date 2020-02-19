#!/usr/bin/python3
'''Tests for Place class'''
import models
import os
import os.path
import unittest
from models.place import Place
from models.engine import file_storage
from models.engine.file_storage import FileStorage


class TestPlace(unittest.TestCase):
    '''Tests for Place class'''

    def setUp(self):
        '''Object Place created'''
        self.obj = Place()

    def test_docstring(self):
        '''Check if methods, classes
        and modules have docstring'''
        msj = "Module doesn't have docstring"
        self.assertIsNotNone(models.place.__doc__, msj)  # Modules
        msj = "Class doesn't have docstring"
        self.assertIsNotNone(Place.__doc__, msj)  # Classes

    def test_executable_file(self):
        '''Check if file have permissions to execute'''
        # Check for read access
        is_read_true = os.access('models/place.py', os.R_OK)
        self.assertTrue(is_read_true)
        # Check for write access
        is_write_true = os.access('models/place.py', os.W_OK)
        self.assertTrue(is_write_true)
        # Check for execution access
        is_exec_true = os.access('models/place.py', os.X_OK)
        self.assertTrue(is_exec_true)

    def test_instance(self):
        '''Check if obj is an instance of Place'''
        self.assertIsInstance(self.obj, Place)

    def test_id(self):
        '''Compare if id of two instances are different'''
        place1 = Place()
        place2 = Place()
        self.assertNotEqual(place1.id, place2.id)

    def test_str(self):
        '''Check if the output of str is in the correct format'''
        _dict = self.obj.__dict__
        string1 = "[Place] ({}) {}".format(self.obj.id, _dict)
        string2 = str(self.obj)
        self.assertEqual(string1, string2)

    def test_save(self):
        '''Check if the attribute updated_at (date) is updated for
        the same object with the current date'''
        first_updated = self.obj.updated_at
        self.obj.save()
        second_updated = self.obj.updated_at
        self.assertNotEqual(first_updated, second_updated)
        os.remove("file.json")

    def test_to_dict(self):
        '''Check if to_dict returns a correct dictionary of the class.'''
        dict_obj = self.obj.to_dict()
        self.assertIsInstance(dict_obj, dict)
        for key, value in dict_obj.items():
            self.assertEqual('Place', value['__class__'])
            # flag = 0
            # if dict_obj['__class__'] == 'Place':
            #     flag += 1
            # self.assertTrue(flag == 1)
        for key, value in dict_obj.items():
            if key == 'created_at':
                self.assertIsInstance(value, str)
            if key == 'updated_at':
                self.assertIsInstance(value, str)

    def test_kwargs(self):
        '''Check when a dictionary is sent as **kwargs argument'''
        self.obj.name = "Betty"
        self.obj.my_number = 89
        obj_json = self.obj.to_dict()
        obj_kwargs = Place(**obj_json)
        self.assertNotEqual(obj_kwargs, self.obj)

    def test_using_json(self):
        '''Check serialization and deserialization json file'''
        storage = FileStorage()
        all_objs = storage.all()
        self.assertIsInstance(all_objs, dict, "es diccionario")  # Test all
        self.obj.name = "Betty"
        self.obj.my_number = 89
        self.obj.save()
        with open("file.json", "r", encoding='utf-8') as f:
            self.assertTrue(self.obj.name in f.read())  # Test save
