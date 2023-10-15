#!/usr/bin/python3
"""
This is the app.py file where the program starts exceting
"""

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


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)