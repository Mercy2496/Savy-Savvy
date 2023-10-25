#!/usr/bin/python3
"""
test all
"""
import sys

sys.path.append("..")

from models.base import BaseModel, Base
from models.user import User
from models.item import Item
from models.tools.create import Create_Item
from models import *

kwargs = {"first_name": "Luc",
          "last_name": "Wangari",
          "email": "lucwangari@gmail.com",
          "password": "lucy2008",
          "dob": "14-02-2004",
          "gender": "Female"}

# lucy = User(**kwargs)

# print(lucy.to_dict(hide=False))
# lucy.save()

# print("="*30)
# lucys = User.get("wgdh", "uyeyfghdfj")
# print(lucys)

url = "https://www.jumia.co.ke/catalog/?q=honey"
create = Create_Item(url)
create.new()

# item = Item()

# item.get_item(**{"type": "jikokoa xtra"})
# unique_items = []
# my_item = Item()

# items = my_item.get_all_items()

# for item in items:
#     item = str(item.type).replace("+", " ")
#     if item not in unique_items:
#         unique_items.append(item)
# print(unique_items)

