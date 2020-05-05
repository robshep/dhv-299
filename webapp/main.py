# -*- coding: utf-8 -*-
import logging as log
log.basicConfig(filename="/tmp/webapp.log")

from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dhv299'

@app.route('/')
def index():
    return render_template('index.html', my_var='#299')

if __name__ == "__main__":
    app.run('0.0.0.0', 8081, debug=True)
