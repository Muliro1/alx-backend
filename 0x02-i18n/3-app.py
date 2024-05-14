#!/usr/bin/env python3
"""
Module Docstring
A module level docstring.
"""

# Importing necessary modules from flask and flask_babel
from flask import Flask, render_template, request
from flask_babel import Babel


class Config(object):
    """
    Class Docstring
    A class for configuration settings.
    """
    # Supported languages
    LANGUAGES = ["en", "fr"]

    # Default locale and timezone
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


# Creating an instance of Flask class
app = Flask(__name__)

# Configuring the Flask application
app.config.from_object(Config)

# Creating an instance of Babel class
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """
    Function Docstring
    Function to determine the best match for supported languages.
    """
    # Returning the best language match from the accepted languages in the request
    return request.accept_languages.best_match(app.config["LANGUAGES"])
