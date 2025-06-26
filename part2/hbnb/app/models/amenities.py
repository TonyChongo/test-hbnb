from .basemodel import BaseModel

class Amenity(BaseModel):
    def __init__(self, name):
        super().__init__()
        if len(name) > 50:
            raise ValueError("Amenity name must not exceed 50 characters.")
        self.name = name
