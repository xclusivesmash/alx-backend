#!/usr/bin/env python3
"""
module: 0-app
description: a simple fask application
"""
from flask import Flask, render_template


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def index() -> str:
    """ renders an html page to the home path.
    """
    return render_template("0-index.html")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
