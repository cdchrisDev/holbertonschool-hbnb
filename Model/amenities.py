#!/usr/bin/python3
"""This module set the amenities prop of places"""
from datetime import datetime, timezone
from base_model import BaseModel

class Amenity(BaseModel):
    """Defines an amenity."""

    def __init__(self, name):
        super().__init__()
        self.name = name

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'created_at': str(self.created_at),
            'updated_at': str(self.updated_at) if self.updated_at else None
        }

    def __repr__(self) -> str:
        return f"<Amenity: {self.name}>"
                          