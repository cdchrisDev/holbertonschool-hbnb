#!/usr/bin/python3
"""This module define the places entity"""
from datetime import datetime, timezone
from base_model import BaseModel
from user import User


class Place(BaseModel):
    """Define places entity"""

    def __init__(self, title, descrption, price, latutide, longitude, owner):
        super().__init__()
        self.title = title
        self.description = description
        self.country = Country(country_name)
        self.city = city_name
        self.latitude = latitude
        self.longitude = longitude
        self.number_of_rooms = number_of_rooms
        self.bathrooms = bathrooms
        self.price = price
        self.max_guests = max_guests
        self.amenities = [] #related amenities
        self.reviews = [] #related reviews
        self.owner = User()

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