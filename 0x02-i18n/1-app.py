#!/usr/bin/env python3
# This line makes sure your script is executed as a Python script.

""" doc doc doc """
# This is a docstring, it's used to describe what your module does.

from flask import Flask, render_template
# Here you're importing the Flask class and the render_template function from the flask module.

from flask_babel import Babel
# You're importing the Babel class from the flask_babel module. This is used for internationalization and localization.

class Config(object):
    """doc doc doc"""
    # This is a docstring, it's used to describe what your class does.

    LANGUAGES = ["en", "fr"]
    # This is a class variable that defines the languages your application will support.

    BABEL_DEFAULT_LOCALE = "en"
    # This is a class variable that sets the default locale for Babel.

    BABEL_DEFAULT_TIMEZONE = "UTC"
    # This is a class variable that sets the default timezone for Babel.

app = Flask(__name__)
# You're creating an instance of the Flask class.

app.config.from_object(Config)
# You're configuring your Flask application using the Config class you defined earlier.

babel = Babel(app)
# You're creating an instance of the Babel class and passing your Flask application to it.

@app.route("/")
# This decorator tells Flask what URL should trigger the function that follows.
def index():
    """doc doc doc"""
    # This is a docstring, it's used to describe what your function does.
    return render_template("1-index.html")
    # This function returns the rendered template "1-index.html".