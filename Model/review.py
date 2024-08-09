#!/usr/bin/python3
from datetime import datetime, timezone
from place import Place
from user import User

class Review(User, Place):
    """Define a review"""

    def __init__(self, user_id, place_id, comment, rating):
        """Initialize a new Review instance."""
        super().__init__()
        self.user_id = user_id
        self.place_id = place_id
        # self.name = name
        self.comment = comment
        self.ratings = rating
        self.review_id = self.id
    
    def save(self):
        """Save the review only if the user is not the host of the place."""
        if self.user_id == self.place_id.host_id:
            raise ValueError("Host cannot review their own place.")
        super().save()


    def to_dict(self):
        """Return the dict rep of review instance"""
        return {
            'review_id': self.review_id,
            'user_id': self.user_id,
            'place_id': self.place_id,
            'comment': self.comment,
            'ratings': self.ratings,
            'created_at': str(self.created_at)
        }

    def __repr__(self) -> str:
        return f"<Review: {self.review_id}>"