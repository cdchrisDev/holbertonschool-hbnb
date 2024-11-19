#!/usr/bin/python3
from  . app.models.user import User


def test_user_creation():
    user = User(first_name='John', last_name='lopez', email='juan.feli.lopez@gmail.com')
    assert user.first_name == 'John'
    assert user.last_name == 'lopez'
    assert user.email == 'juan.feli.lopez@gmail.com'
    assert user.is_admin is False
    print('User creation test passed')

test_user_creation()