#!/usr/bin/python3
"""This module define the users entity"""
#import bcrypt
from base_model import BaseModel



class User(BaseModel):
    """A base user obj"""
    
    def __init__(self, id, first_name, last_name, email, is_admin = False):
        super().__init__()
        self.id = id
        self.first_name = first_name[:50]
        self.last_name = last_name[:50]
        self.email = email
        self.is_admin = is_admin


    def add_unique_email(self, email):
        if not isinstance(email, str):
            raise TypeError('wrong type')

        for e in emails:
            if e == email:
                raise EmailRegError()

        self.emails.append(email)

    #def hash_password(self, password):
    #    """Encrypt user password"""

    #    salt = bcrypt.gensalt()
    #    hashed_password = bcrypt.hashpw(_password.encode('utf-8'), salt)
    #    return hashed_password.decode('utf-8')
    
    def to_dict(self):
        """A dict rep of users obj"""
        
        data = {
            "first_name": self.firstName,
            "last_name": self.lastName,
            "email": self.email,
            "password": self._password,
            "created_at": self.created_at
        }


class Owner(User):
    def __init__(self, host_id):
        self.host_id = host_id


class Guest(User):
    def __init__(self, guest_id):
        self.guest_id = guest_id
