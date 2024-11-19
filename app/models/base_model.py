#!/usr/bin/python3
"""This module set the core of all obj
in the app, basically every obj must be
traceable with unique id
"""
import uuid
from datetime import datetime


time = "%Y-%m-%dT%H:%M:%S.%f"

class BaseModel:
    """Base Class for all obj"""
    
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()    

    def save(self):
        """Save obj state at datetime"""

        self.updated_at = datetime.now()

    def update(self, data):
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.save()

    def to_dict(self):
        """Return dict rep of obj"""

        return {
            'id': self.id,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }