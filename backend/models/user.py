#!/usr/bin/env python3
"""
THis is the user model
"""
from models.base import BaseModel, Base
from models import *

class User(BaseModel, Base):
    """
    user class
    """
    __tablename__ = "users"
    default = "- - -"
    first_name = Column(String(100), nullable=False, default=default)
    last_name = Column(String(100), nullable=False,         default=default)
    email = Column(String(60), nullable=False,
                   default=default)
    password = Column(String(60), nullable=False, default=default)
    dob = Column(String(60), nullable=False, default=default)
    gender = Column(String(28), nullable=False, default=default)

    def __init__(self, *args, **kwargs):
        """
        """
        super().__init__(*args, **kwargs)