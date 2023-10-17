#!/usr/bin/python3
""" BaseModel unittests class is defined """

import unittest
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from datetime import datetime
import models


class TestBaseModel(unittest.TestCase):
    """ BaseModel class unittests suite """

    def test_new_instance_stored(self):
        self.assertIn(BaseModel(), models.storage.all().values())

    def test_created_at(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_init_method(self):
        self.assertTrue(hasattr(BaseModel, "__init__"))

    def test_save(self):
        self.assertTrue(hasattr(BaseModel, "save"))

    def test_to_dict(self):
        self.assertTrue(hasattr(BaseModel, "to_dict"))

    def test_id(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_docstring(self):
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)


if __name__ == "__main__":
    unittest.main()
