#!/usr/bin/env python3
'''
Basic Babel setup
'''

from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    '''
    Configuration Class for Babel
    '''

    DEBUG = True
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    '''
    Function get_locale for a webpage

    Args: N/A

    Returns: Language best match to config
    '''
    locale = request.args.get('locale', None)

    if locale and locale in app.config['LANGUAGES']:
        return locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    '''
    Default app route

    Args: N/A

    Returns: HTML page
    '''
    return render_template("4-index.html")


if __name__ == "__main__":
    app.run()
