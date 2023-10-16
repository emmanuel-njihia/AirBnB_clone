#!/usr/bin/python3
"""unittest of base_model.py"""
import unittest
import os
from models.base_model import BaseModel
from models.engine.file_storage import storage
from datetime import datetime
import uuid
import json


class TestBaseModel(unittest.TestCase):
    def test_attributes(self):
        my_model = BaseModel()
        self.assertTrue(hasattr(my_model, 'id'))
        self.assertTrue(hasattr(my_model, 'created_at'))
        self.assertTrue(hasattr(my_model, 'updated_at'))

    def test_id_uniqueness(self):
        id_list = []
        for _ in range(100):
            my_model = BaseModel()
            self.assertIsInstance(my_model.id, str)
            self.assertNotIn(my_model.id, id_list)
            id_list.append(my_model.id)

    def test_created_and_updated(self):
        my_model = BaseModel()
        self.assertIsInstance(my_model.created_at, datetime)
        self.assertIsInstance(my_model.updated_at, datetime)
        self.assertEqual(my_model.created_at, my_model.updated_at)

    def test_save_method(self):
        my_model = BaseModel()
        original_updated_at = my_model.updated_at
        my_model.save()
        self.assertNotEqual(original_updated_at, my_model.updated_at)

    def test_to_dict(self):
        my_model = BaseModel()
        my_model_dict = my_model.to_dict()
        self.assertIsInstance(my_model_dict, dict)
        self.assertEqual(my_model_dict['__class__'], 'BaseModel')
        self.assertIsInstance(my_model_dict['created'], str)
        self.assertIsInstance(my_model_dict['updated'], str)
        self.assertEqual(my_model_dict['id'], my_model.id)

    def test_to_dict_and_from_dict(self):
        original_model = BaseModel()
        original_model.name = "My_First_Model"
        original_model.value = 89

        model_dict = original_model.__dict__

        new_model = BaseModel()
        new_model.__dict__.update(model_dict)

        self.assertEqual(new_model.__dict__, original_model.__dict__)

    def test_identity_check(self):
        model1 = BaseModel()
        model2 = BaseModel()

        self.assertFalse(model1 is model2)


class TestFileStorage(unittest.TestCase):
    def config_file(self):
        """create new filestorage instance"""
        self.storage = FileStorage()
        self.storage.reload()

    def remove(self):
        """Remove json file that had been used to test"""
        try:
            os.remove(self.storage._FileStorage__file_path)
        except FileNotFoundError:
            pass

    def test_all(self):
        obj = self.storage.all()
        self.assertIsInstance(obj, dict)

    def test_new(self):
        my_model = BaseModel()
        self.storage.new(my_model)
        obj = self.storage.all()
        self.assertIn(f"BaseModel.{my_model.id}", obj)

    def test_save_and_reload(self):
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        self.storage.save()
        self.storage.reload()
        obj = self.storage.all()

        self.assertIn(f"BaseModel.{my_model.id}", obj)
        reloaded_model = obj[f"BaseModel.{my_model.id}"]
        self.assertIsInstance(reloaded_model, BaseModel)
        self.assertEqual(reloaded_model.name, "My_First_Model")
        self.assertEqual(reloaded_model.my_number, 89)
        self.assertIsInstance(reloaded_model.created_at, datetime)
        self.assertIsInstance(reloaded_model.updated_at, datetime)


if __name__ == '__main__':
    unittest.main()
