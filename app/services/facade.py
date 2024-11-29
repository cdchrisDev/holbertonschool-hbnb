#/usr/bin/pyhon3
from app.persistence.repository import InMemoryRepository as repo

class UserCns(repo):
    """Define user console"""
    def __init__(self):
        user = User(**user_data)

    def create_user(self, user_data):
        self.add(user)
        return user

    def get_user(self, user_id):
        return self.get(user_id)

    def get_user_by_email(self, email):
        self.get_by_attribute('email', email)
        return email

class AmenityCnt(repo):
    """DEfine the amenity controls"""

    def create_amenity(self, amenity_data):
        pass

    def get_amenity(self, amenity_id):
        pass

    def get_all_amenities(self):
        pass

    def update_amenity(self, amenity_id, amenity_data):
        pass

class PlaceCnt(repo):
    def create_place(self, place_data):
        if place_data.price <= 0:
            return {'error': 'Invalid price'}
        if place_data.latitude < -90 and place_data.latitude > 90:
            return {'error': 'Invalid coordenates'}
        if place_data.longitude < -180 and place_data.latitude > 180:
            return {'error': 'Invalid coordenates'}
        pass

    def get_place(self, place_id):
        pass

    def get_all_places(self):
        pass

    def update_place(self, place_id, place_data):
        pass


class ReviewCnt(repo):
    def create_review(self, review_data):
        pass

    def get_review(self, review_id):
        pass

    def get_all_reviews(self):
        pass

    def get_reviews_by_place(self, place_id):
        pass

    def update_review(self, review_id, review_data):
        pass

    def delete_review(self, review_id):
        pass

