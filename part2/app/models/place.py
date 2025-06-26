from .basemodel import BaseModel
from .user import User
from .amenities import Amenity
from .reviews import Review

class Place(BaseModel):
    def __init__(self, title, description, price, latitude, longitude, owner):
        super().__init__()
        if len(title) > 100:
            raise ValueError("Title must not exceed 100 characters.")
        if price <= 0:
            raise ValueError("Price must be a positive number.")
        if not (-90.0 <= latitude <= 90.0):
            raise ValueError("Latitude must be between -90.0 and 90.0.")
        if not (-180.0 <= longitude <= 180.0):
            raise ValueError("Longitude must be between -180.0 and 180.0.")
        if not isinstance(owner, User):
            raise TypeError("Owner must be a User instance.")

        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner = owner
        self.reviews = []
        self.amenities = []

    def add_review(self, review):
        if not isinstance(review, Review):
            raise TypeError("Expected a Review instance.")
        self.reviews.append(review)

    def add_amenity(self, amenity):
        if not isinstance(amenity, Amenity):
            raise TypeError("Expected an Amenity instance.")
        self.amenities.append(amenity)
