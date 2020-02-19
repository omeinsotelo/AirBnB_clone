#!/usr/bin/python3
'''Tests for FileStorage class'''
import models
from models.engine.file_storage import FileStorage
import os
import unittest


class TestFile_Storage(unittest.TestCase):
    '''Tests for FileStorage class'''

    def test_docstring(self):
        '''Check if methods, classes
        and modules have docstring'''
        msj = "Module doesn't have docstring"
        obj = models.engine.file_storage.__doc__
        self.assertIsNotNone(obj, msj)  # Modules
        msj = "Class doesn't have docstring"
        self.assertIsNotNone(obj, msj)  # Classes

    def test_executable_file(self):
        '''Check if file have permissions to execute'''
        # Check for read access
        is_read_true = os.access('models/engine/file_storage.py', os.R_OK)
        self.assertTrue(is_read_true)
        # Check for write access
        is_write_true = os.access('models/engine/file_storage.py', os.W_OK)
        self.assertTrue(is_write_true)
        # Check for execution access
        is_exec_true = os.access('models/engine/file_storage.py', os.X_OK)
        self.assertTrue(is_exec_true)

    def test_instance(self):
        '''Check if storage is an instance of FileStorage'''
        storage = FileStorage()
        self.assertIsInstance(storage, FileStorage)
