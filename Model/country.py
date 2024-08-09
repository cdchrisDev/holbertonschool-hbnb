#!/usr/bin/python3
"""This module define the country entity"""
from base_model import BaseModel
from cities import Cities
from datetime import datetime


class Country(BaseModel):
    """This class define the country entity"""

    cities = []
    def add_city(self, city):
        """Insert new city to the list"""

        if isinstance(city, Cities) and city.city_name not in [c.city_name for c in self.cities]:
            self.cities.append(city)

    def get_cities(self):
        """retrieve a city from the list"""

        return self.cities
    def get_country_name(self):
        """Get a country from the list"""

        return self.country_name

    def to_dict(self):
        """Return the dict rep of obj"""

        base_dict = super().to_dict()
        base_dict.update({
            "country": self.country_name,
            "cities": [city.to_dict() for city in self.cities]
        })
        return base_dict
