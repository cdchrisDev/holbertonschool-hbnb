#!/usr/bin/python3
from app.models.place import Place
from app.models.user import User, Owner, Guest
from app.models.review import Review


def test_place_creation():
    user = User(id="341", first_name="juan", last_name="smith", email="juan@gmail.com")
    place = Place(title="Cozy Apartment", description="A nice place to stay", price=100, latitude=37.8843, longitude=-122.4194, owner=Owner)

    review = Review(id="1", text="Great stay!", rating=5, place=place, user=Guest)
    place.add_review(review)

    assert place.title == "Cozy Apartment"
    assert place.price == 100
    assert len(place.reviews) == 1
    assert place.reviews[0].text == "Great stay!"
    print("Place creation and relationshipp test passed!")

test_place_creation()

