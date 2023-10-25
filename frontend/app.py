#!/usr/bin/python3
"""
This is the app.py file where the program starts exceting
"""
import sys
sys.path.append("/mnt/c/GIT/SIZ/Savy-Savvy/backend")
from models.item import Item
from datetime import datetime

from flask import Flask, render_template
from flask_cors import CORS


app = Flask(__name__)

@app.route("/", strict_slashes=False)
@app.route("/index", strict_slashes=False)
def home():
    """
    This is the home page for a Landing page
    """
    return render_template("index.html")

@app.route("/about", strict_slashes=False)
def about():
    """
    This is the official about page
    """
    return render_template("about.html")

@app.route("/display", strict_slashes=False)
def display():
    """
    This is the items display page
    """
    unique_items = []
    my_item = Item()

    items = my_item.get_all_items()

    for item in items:
        item = str(item.type).replace("+", " ")
        if item not in unique_items:
            unique_items.append(item)
    now = datetime.now()


    return render_template("display.html", available_items=unique_items, items=items, time=now)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)