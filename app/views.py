from app import app
import os.path
import socket
import json
import urllib2
from flask import render_template, flash, redirect
from flask_autoindex import AutoIndex

files_index = AutoIndex(app, os.path.curdir + '/autoindex', add_url_rules=False)

@app.route("/")
@app.route("/index")
def index():
	return render_template('index.html', title='Home')

@app.route('/autoindex/', defaults={'path': ''})
@app.route('/autoindex/<path:path>')
def autoindex(path):
    return files_index.render_autoindex(path)
