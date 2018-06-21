#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, json, request, session, url_for, escape, redirect, jsonify, make_response
from werkzeug import generate_password_hash, check_password_hash
from flask.ext.pymongo import PyMongo
import pymongo
from pymongo import MongoClient
from bson.son import SON
import pandas as pd

app     = Flask(__name__)
mongo   = PyMongo(app)

@app.route('/')
def homePage():
	return render_template('index.html')

@app.route('/<classID>')
def classForm(classID):
	cID = int(classID)
	classrooms = [
					{
						"id"		: 1,
						"students"	: [
										{ "firstName": "Anshu", "lastName": "Jain" },
										{ "firstName": "Raghav", "lastName": "Jain" },
										{ "firstName": "Shalini", "lastName": "Jain" }
									]
					},
					{
						"id"		: 2,
						"students"	: [
										{ "firstName": "Preeti", "lastName": "Gupta" },
										{ "firstName": "Tanya", "lastName": "Gupta" },
										{ "firstName": "Shantanu", "lastName": "Gupta" }
									]
					}
				]
	cr = pd.DataFrame(classrooms)
	cr = cr.loc[cr.id == cID]
	students = pd.DataFrame(list(cr.students)[0])
	return render_template('classroom.html', students = students)

if __name__ == '__main__':
    app.run(debug=True)