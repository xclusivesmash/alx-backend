#!/usr/bin/env python3
"""
module: 1-app
description: a simple fask application
"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """Babel configuration class
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel()
babel.init_app(app)


@babel.localeselector
def get_locale() -> str:
    """get locale from languages attribute."""
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/")
def index() -> str:
    """ renders an html page to the home path.
    """
    return render_template("0-index.html")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
