#!/usr/bin/python3
"""This module set the amenities prop of places"""
from datetime import datetime, timezone
from base_model import BaseModel

class Amenity(BaseModel):

    def __init__(self, id, name=''):
        super().__init__()
        self.id = id
        self.name = name
    """Defines an amenity
    amen = {
        'tv': None,
        'bathroom_num': 0,
        'backyard': None,
        'basement': None,
        'bedroom_num': 0,
        'laundry_ser': None,
        'dish_washer_and_dryer': None,
        'security': [1..5],
        'Control_atmosfere': ['heating', 'ventilation',
        'air_condition'],
        'hot_water': None,
        'fireplace': None,
        'WIFI': None,
        'kitchen': None,
        'swimming_pool': None,
        'self_check-in': None,
        'furniture_vovers': None,
        'high_chair': None,
        'entretainment': ['videogames', 'pool', 'ping-pong'.
        'park', 'stereo'],
        'fridge': None,
        'view_balcony': None
    }
    """

    def __init__(self, name, AmenList):
        """set the amenities available on place"""

        self.name = name
        self.AmenList = []


    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'created_at': str(self.created_at),
            'updated_at': str(self.updated_at) if self.updated_at else None
        }

    def __repr__(self) -> str:
        return f"<Amenity: {self.name}>"
                          