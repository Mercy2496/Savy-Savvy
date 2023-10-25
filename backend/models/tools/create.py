#!/usr/bin/env python3

from .jumia import Jumia
from .scrape import Scrape
from ..item import Item

import requests, os

class Create_Item:
    """
    Create_Item class
    """
    url = ""

    def __init__(self, *args, **kwargs):
        """Initialization"""
        if args:
            for arg in args:
                self.url = arg
                break
        if kwargs:
            for key, val in kwargs.items():
                if key == "url":
                    self.url = val
                    break
        if not self.url:
            print("--A--(ABORT): No url Provided Aborting...")
            return

    def validate_data(self, data):
        val_state = ""
        new_data = {}
        if isinstance(data, dict):
            req = ["name", "category", "price"]
            if all(key in data.keys() for key in req):
                val_state = True
            if val_state:
                for key, val in data.items():
                    if key in req and not val:
                        val_state = False
                    if key == "category":
                        new_data[key] = val
                    elif key == "name" and val:
                        new_data[key] = val
                    elif key == "price" and val:
                        new_data[key] = val
                    elif key == "description":
                        new_data[key] = val
                    elif key == "image":
                        new_data[key] = val
                    elif key == "link":
                        new_data[key] = f"https://www.jumia.co.ke{val}"
            if val_state:
                # print(new_data)
                typ = self.url.split("=")[-1]
                if typ.lower() in str(new_data["category"]).lower():
                    new_data["type"] = typ
                else:
                    # print(f"--A--(ALRET): {typ} Item is not in {data['category']} Category")
                    new_data["type"] = typ

                return new_data
            else:
                print(f"--A--(ALERT): Data does not meet requrements: {data}")
                return False


    def new(self, url=""):
        """
        the magic hapens here
        """
        if url:
            self.url = url
        else:
            if not self.url:
                print("--A--(ABORT): No url Provided Aborting...")
                return

        count = 0
        jumia = Jumia()
        content = jumia.make_request(self.url)
        scrape = Scrape(content)
        articles = scrape.get_articles()
        for article in articles:
            # print(f"++++ : Len of article {len(article)}")
            data = scrape.get_data(article)
            data = self.validate_data(data)
            if data:
                if count == 0:
                    if "price" in list(data.keys()):
                        avg_prc = int(str(data["price"].split(" ")[1]).replace(",", ""))
                if count == 2:
                    if "image" in list(data.keys()):
                        if not os.path.exists("item_images"):
                            os.makedirs("item_images")
                        fl = f"/mnt/c/GIT/SIZ/Savy-Savvy/frontend/static/item_images/{data['type']}.jpg"
                        response = requests.get(data["image"])
                        if response.status_code == 200:
                            with open(fl, "wb") as f:
                                f.write(response.content)
                            print(f"\t{count} Img saved in {fl}")
                        else:
                            print(f"--A--(ALERT): Requested img status code: {response.status_code}")
                try:
                    # print("**"*50)
                    # print(data)
                    prc = int(str(data["price"].split(" ")[1]).replace(",", ""))
                    if prc < (avg_prc/2):
                        # print(f"{count}: {prc}{'-'*50}")
                        # print(data)
                        # print("-"*50)
                        pass
                    else:
                        # print(data)
                        new_item = Item(**data)
                        new_item.save()
                        # print(f"{count}: {prc}{'=='*50}")

                except Exception as e:
                    print(f"--E--(ERR): \n\t{e}")
            else:
                pass
                # print("--A--(ABORT): Data does not meet requrements")

            count = count + 1