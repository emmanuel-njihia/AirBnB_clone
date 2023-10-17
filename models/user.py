#!/usr/bin/python3
"""This model creates a class called user"""
from models.base_model import BaseModel


class User(BaseModel):
    """Class for managing user class objects"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
