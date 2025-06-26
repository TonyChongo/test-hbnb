from .basemodel import BaseModel
from .user import User
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .place import Place

class Review(BaseModel):
    def __init__(self, text: str, rating: int, place: 'Place', user: 'User'):
        super().__init__()
        if not text:
            raise ValueError("Review text is required.")
        if not (1 <= rating <= 5):
            raise ValueError("Rating must be between 1 and 5.")
        if not isinstance(user, User):
            raise TypeError("User must be a User instance.")
        if place.__class__.__name__ != "Place":
            raise TypeError("Place must be a Place instance")


        self.text = text
        self.rating = rating
        self.place = place
        self.user = user
        place.add_review(self)
        
    def to_dict(self):
        data = super().to_dict()
        data.update({
            "text": self.text,
            "rating": self.rating,
            "user_id": self.user.id,
            "place_id": self.place.id
        })
        return data
