#!/usr/bin/python3
"""Writes a class BaseModel with various attributes"""

import uuid
from datetime import datetime
from models import storage

class BaseModel:
    def __init__(self):
        """Defines BaseModel"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        """Update public instance attribute with current time"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns dictionary containing keys and values
        of __dict__ instance"""
        ret_dict = self.__dict__.copy()
        ret_dict['__class__'] = self.__class__.__name__
        ret_dict['updated_at'] = self.updated_at.isoformat()
        ret_dict['created_at'] = self.created_at.isoformat()
        return ret_dict

    def __str__(self):
        """Gets print representation of BaseModel"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def __init__(self, *args, **kwargs):
        if kwargs:
            if "__class__" in kwargs:
                del kwargs["__class__"]
            else:
                kwargs['created_at'] = datetime.datetime.strptime
                (kwargs['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
                kwargs['updated_at'] = datetime.datetime.strptime
                (kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.fromisoformat(value)
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            storage.new(self)
            storage.save()
