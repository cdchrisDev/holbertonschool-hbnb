#!/usr/bin/python3
from app.models.user import User
print(User)

User.emails = ['juan@gmail', 'sara@gmail', 'carlos@hotmail']
User.add_unique_email('sara@gmail')
print(User.emails)