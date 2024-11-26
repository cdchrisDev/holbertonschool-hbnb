#!/usr/bin/python3
"""This module define the places entity"""
from datetime import datetime, timezone
from base_model import BaseModel
from user import User, Owner


class Place(BaseModel):
    """Define places entity"""

    def __init__(self, title, description, price, latitude, longitude, owner):
        super().__init__()
        self.title = title
        self.description = description
        self.latitude = latitude
        self.longitude = longitude
        self.price = price
        self.amenities = [] #related amenities
        self.reviews = [] #related reviews
        self.owner = Owner("asda")

    def add_review(self, review):
        """add review"""
        self.reviews.append(review)

    def add_amenities(self, amenity):
        """add amenity"""
        self.amenities.append(amenity)

    def to_dict(self):
        """Return dict rep of obj"""

        return {
            'place_name': self.place_name,
            'description': self.description,
            'address': self.address,
            'host_id': self.host_id,
            'id': self.place_id,
            'country': self.country,
            'city': self.city,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'number_of_rooms': self.number_of_rooms,
            'bathrooms': self.bathrooms,
            'price_per_night': self.price_per_night,
            'max_guests': self.max_guests,
            'amenities': [amenity.to_dict() for amenity in self.amenities],
            'created_at': str(self.created_at)
        }

    def __repr__(self) -> str:
        return f"<Place: {self.place_name}>"
