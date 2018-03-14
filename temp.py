# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 23:01:33 2018

@author: singh
"""

from flask import Flask
app = Flask(__name__)
@app.route("/")
def index():
    return "this is the homepage"

@app.route("/rit_input/<int:enter>")
def agasgsg(enter):
    return "<h2>Post id is %s<h2>" % enter


if __name__== ("__main__"):
    app.run(debug=True)