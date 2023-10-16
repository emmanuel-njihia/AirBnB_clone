#!/usr/bin/python3
"""Imports BaseModel class so it is easily
accessed when importing models package"""
from models.engine.file_storage import FileStorage

"""create a unique FileStorage instance for your application"""
storage = FileStorage()
storage.reload()
