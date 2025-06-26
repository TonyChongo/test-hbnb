import re
from .basemodel import BaseModel

class User(BaseModel):
    emails = set()

    def __init__(self, first_name, last_name, email, is_admin=False):
        super().__init__()
        if len(first_name) > 50 or len(last_name) > 50:
            raise ValueError("First and last names must not exceed 50 characters.")
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise ValueError("Invalid email format.")
        if email in User.emails:
            raise ValueError("Email must be unique.")
        
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_admin = is_admin
        User.emails.add(email)
