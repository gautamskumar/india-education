#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, json, request, session, url_for, escape, redirect, jsonify, make_response
from werkzeug import generate_password_hash, check_password_hash
from flask.ext.pymongo import PyMongo
import pymongo
from pymongo import MongoClient
from bson.son import SON

app     = Flask(__name__)
mongo   = PyMongo(app)

@app.route('/')
def homePage():
	return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)