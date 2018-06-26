#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, json, request, session, url_for, escape, redirect, jsonify, make_response
from werkzeug import generate_password_hash, check_password_hash
from flask.ext.pymongo import PyMongo
import pymongo
from pymongo import MongoClient
from bson.son import SON
import pandas as pd
import config
from datetime import datetime
from datetime import timedelta

app     = Flask(__name__)
mongo   = PyMongo(app)

db      = config.get_db()
rubrics = db.rubrics

@app.route('/')
def homePage():
    return render_template('index.html')

@app.route('/<classID>', methods=["GET","POST"])
def classForm(classID):
    if request.method == "POST":
        # Do stuff
        evidenceOfPlanning  = int(request.form.get('evidenceOfPlanning'))
        availableMaterials  = int(request.form.get('availableMaterials'))
        punctuality         = int(request.form.get('punctuality'))
        circle              = int(request.form.get('circle'))
        clarity             = int(request.form.get('clarity'))
        democratic          = int(request.form.get('democratic'))
        inclusivity         = int(request.form.get('inclusivity'))
        conflictResolution  = int(request.form.get('conflictResolution'))
        promoteAdmiration   = int(request.form.get('promoteAdmiration'))
        prohibtsCriticism   = int(request.form.get('prohibtsCriticism'))
        timeManagement      = int(request.form.get('timeManagement'))
        openQuestions       = int(request.form.get('openQuestions'))
        wdwd                = int(request.form.get('wdwd'))
        photo               = int(request.form.get('photo'))
        rubrics.update({
              'id': int(1)
            },
            {
            '$set': {
                "updated_at"        : datetime.now(),
                "evidenceOfPlanning": evidenceOfPlanning,
                "availableMaterials": availableMaterials,
                "punctuality"       : punctuality,
                "circle"            : circle,
                "clarity"           : clarity,
                "democratic"        : democratic,
                "inclusivity"       : inclusivity,
                "conflictResolution": conflictResolution,
                "promoteAdmiration" : promoteAdmiration,
                "prohibtsCriticism" : prohibtsCriticism,
                "timeManagement"    : timeManagement,
                "openQuestions"     : openQuestions,
                "wdwd"              : wdwd,
                "photo"             : photo
                }
            }, upsert=False, multi=False)
    result = rubrics.find_one({})
    return render_template('rubric.html', rubric = result)

if __name__ == '__main__':
    app.run(debug=True)