#!/usr/bin/env python3
# This line makes sure your script is executed as a Python script.

"""doc doc doc"""
# This is a docstring, it's used to describe what your module does.

from flask import Flask, render_template
# Here you're importing the Flask class and the render_template function from the flask module.

app = Flask(__name__)
# You're creating an instance of the Flask class.

@app.route("/")
# This decorator tells Flask what URL should trigger the function that follows.
def index():
    """doc doc doc"""
    # This is a docstring, it's used to describe what your function does.
    return render_template("0-index.html")
    # This function returns the rendered template "0-index.html".

if __name__ == "__main__":
    # This conditional is used to check whether this script is being run directly or being imported.
    app.run(host="0.0.0.0", port="5000")
    # This line runs the application on the local development server.