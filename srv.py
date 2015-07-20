#!/usr/bin/env python
# -*- utf-8 -*-

from flask import render_template,Flask,request
from flask.ext.babel import gettext,Babel


app = Flask(__name__)
app.config.from_pyfile('mysettings.cfg')
babel = Babel(app)

@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(['ko','zh','ja', 'ja_JP', 'en'])

@app.route('/')
def hello_world():
    return gettext('Hello World!')

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


if __name__ == '__main__':
    app.debug=True
    app.run(host='0.0.0.0')
