#!/usr/bin/python3
"""This module set the amenities prop of places"""
from datetime import datetime, timezone


class Amenity(db.Model):
    """Defines an amenity."""

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'created_at': str(self.created_at),
            'updated_at': str(self.updated_at) if self.updated_at else None
        }

    def __repr__(self) -> str:
        return f"<Amenity: {self.name}>"
                          