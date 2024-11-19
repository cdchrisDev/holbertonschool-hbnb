# Business logic and API implementation
## BaseModel
To start developing our classes that will be the core of our app, we need to design the
commun dominator of our logic.

1. Each class should be unique identified and must record the time when was created and updated
```python
#!/usr/bin/python3
import uuid
from datetime import datetime


time = "%Y-%m-%dT%H:%M:%S.%f" ### time formating

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
```
2. Now, inheriting from `BaseModel` the remaining entities have to deal their own business
**PLACE**
```python
#!/usr/bin/python3
"""This module define the places entity"""
from datetime import datetime, timezone
from base_model import BaseModel


class Place(BaseModel):
    """Define places entity"""

    def __init__(self,
                 title: str = None, 
                 description: str = None, 
                 address: str = None, 
                 country: str = None, 
                 city: str = None, 
                 latitude: float = None, 
                 longitude: float = None, 
                 number_of_rooms: int = None, 
                 bathrooms: int = None, 
                 price_per_night: float = None, 
                 max_guests: int = None, 
                 amenities: list = None):
        super().__init__()
        
        self.title = title
        self.description = description
        self.country = Country(country_name)
        self.city = city_name
        self.latitude = latitude
        self.longitude = longitude
        self.number_of_rooms = number_of_rooms
        self.bathrooms = bathrooms
        self.price_per_night = price_per_night
        self.max_guests = max_guests
        self.amenities = []
        self.reviews = []

    def add_review(self, review):
        """add review"""
        self.reviews.append(review)

    def add_amenities(self, amenity):
        """add amenity"""
        self.amenities.append(amenity)
```

3. 