from .basemodel import BaseModel
from .place import Place
from .user import User

class Review(BaseModel):
    def __init__(self, text, rating, place, user):
        super().__init__()
        if not text:
            raise ValueError("Review text is required.")
        if not (1 <= rating <= 5):
            raise ValueError("Rating must be between 1 and 5.")
        if not isinstance(place, Place):
            raise TypeError("Place must be a Place instance.")
        if not isinstance(user, User):
            raise TypeError("User must be a User instance.")

        self.text = text
        self.rating = rating
        self.place = place
        self.user = user
        place.add_review(self)
