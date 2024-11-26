#!/usr/bin/python3
from app.models.amenity import Amenity


def test_amenity_creation():
    amenity = Amenity(id="14135", name="Wi-Fi")
    assert amenity.name == "Wi-Fi"
    print("Amenity creation passed!")


test_amenity_creation()

