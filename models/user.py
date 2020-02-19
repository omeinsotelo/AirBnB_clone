#!/usr/bin/python3
"""
User module
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    Class User
    """

    first_name = ''
    last_name = ''
    email = ''
    password = ''
