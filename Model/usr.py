#!/usr/bin/python3
"""This module define the users entity"""
import bcrypt
from base_model import BaseModel



class User(BaseModel):
    """A base user obj"""
    
    emails = []
    user_places = []
    users = {}


    def __init__(self, firstName, lastName, password, email):
        """This func init the basic user data, every user
        must have it to be able to exist in database
        """

        self.firstName = firstName
        self.lastName = lastName
        self._password = self.hash_password(password)
        self.email = email

    def hash_password(self, password):
        """Encrypt user password"""

        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(_password.encode('utf-8'), salt)
        return hashed_password.decode('utf-8')
    
    def to_dict(self):
        """A dict rep of users obj"""
        
        data = {
            "first_name": self.firstName,
            "last_name": self.lastName,
            "email": self.email,
            "password": self._password,
            "created_at": self.created_at
        }
        return data
    