#!/usr/bin/pyhon3
from app.persistence.repository import InMemoryRepository as repo

class HBnBFacade(repo):

    def create_user(self, user_data):
        pass

    def get_place(self, place_id):
        pass

    def get_user(self, user_id):
        pass

    def get_user_by_email(self, email):
        pass

class UserCns(HBnBFacade):
    """Define user console"""
    def __init__(self):
        user = User(**user_data)

    def create_user(self, user_data):
        self.add(user)
        return user

    def get_user(self, user_id):
        return self.get(user_id)

    def get_user_by_email(self, email):
        return self.get_by_attribute('email', email)
