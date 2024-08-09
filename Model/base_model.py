#!/usr/bin/python3
"""This module set the core of all obj
in the app, basically every obj must be
traceable with unique id
"""
import uuid
from datetime import datetime


class BaseModel:
    """Base Class for all obj"""
    
    def __init__(self):
        self.id = uuid.uuid4().hex
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        """Save obj state at datetime"""

        self.updated_at = datetime.now()

    def to_dict(self):
        """Return dict rep of obj"""

        return {
            'id': self.id,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }