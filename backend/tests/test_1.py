#!/usr/bin/python3
"""
test all
"""
import sys

sys.path.append("..")

from models.base import BaseModel, Base
from models.user import User
from models import *

kwargs = {"first_name": "Lucy",
          "last_name": "Wang'ari",
          "email": "lucyywangari@gmail.com",
          "password": "lucy2005",
          "dob": "14-02-2005",
          "gender": "Female"}

lucy = User(**kwargs)

print(lucy.to_dict(hide=False))
lucy.save()
