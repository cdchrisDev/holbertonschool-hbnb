#!/usr/bin/python3
from base_model import BaseModel
from datetime import datetime
import sys
import os


class Cities(BaseModel):
    """Defines city"""

    def __init__(self, city_name, country):
        self.city_name = city_name
        self.country = country

    def to_dict(self):
        """Return the dict rep of obj"""
        base_dict = ({
            "city_name": self.city_name,
            "country": self.country,
            "city_id": self.id
        })
        return base_dict