#!/usr/bin/python3
'''Tests for Review class'''
import models
import os
import os.path
import unittest
from models.review import Review
from models.engine import file_storage
from models.engine.file_storage import FileStorage


class TestReview(unittest.TestCase):
    '''Tests for Review class'''

    def setUp(self):
        '''Object Review created'''
        self.obj = Review()

    def test_docstring(self):
        '''Check if methods, classes
        and modules have docstring'''
        msj = "Module doesn't have docstring"
        self.assertIsNotNone(models.review.__doc__, msj)  # Modules
        msj = "Class doesn't have docstring"
        self.assertIsNotNone(Review.__doc__, msj)  # Classes

    def test_executable_file(self):
        '''Check if file have permissions to execute'''
        # Check for read access
        is_read_true = os.access('models/review.py', os.R_OK)
        self.assertTrue(is_read_true)
        # Check for write access
        is_write_true = os.access('models/review.py', os.W_OK)
        self.assertTrue(is_write_true)
        # Check for execution access
        is_exec_true = os.access('models/review.py', os.X_OK)
        self.assertTrue(is_exec_true)

    def test_instance(self):
        '''Check if obj is an instance of Review'''
        self.assertIsInstance(self.obj, Review)

    def test_id(self):
        '''Compare if id of two instances are different'''
        review1 = Review()
        review2 = Review()
        self.assertNotEqual(review1.id, review2.id)

    def test_str(self):
        '''Check if the output of str is in the correct format'''
        _dict = self.obj.__dict__
        string1 = "[Review] ({}) {}".format(self.obj.id, _dict)
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
            check = 0
            if dict_obj['__class__'] == 'Review':
                check += 1
            self.assertTrue(check == 1)
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
        obj_kwargs = Review(**obj_json)
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
