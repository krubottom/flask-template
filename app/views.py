from app import app
import os.path
import socket
import json
import urllib2
from flask import render_template, flash, redirect, url_for
from flask_autoindex import AutoIndex
from .forms import PageForm

# import sys
# sys.path.append('../python')
# import lib

files_index = AutoIndex(app, os.path.curdir + '/autoindex', add_url_rules=False)

@app.route("/")
@app.route("/index")
def index():
	return render_template('index.html', title='Home')

@app.route('/autoindex/', defaults={'path': ''})
@app.route('/autoindex/<path:path>')
def autoindex(path):
    return files_index.render_autoindex(path)

@app.route("/form", methods=['GET', 'POST'])
def form():
	form = PageForm()
	if form.validate_on_submit():
		# flash('IP Address: %s' % (form.FormCameraAddress.data))
		FormTextField = form.FormTextField.data
		return render_template('formreturn.html', title='Form Return', textfield=FormTextField)
	return render_template('formentry.html', title='Form Entry', form=form)

@app.route("/site-map")
def site_map():
	links = []
	for rule in app.url_map.iter_rules():
		# if len(rule.defaults) >= len(rule.arguments):
		# if autoindex not in url_for(rule.defaults):
			url = url_for(rule.endpoint, **(rule.defaults or {}))
			links.append((url, rule.endpoint))
	return render_template("site_map.html", links=links)
