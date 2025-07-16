from flask_app import app
from flask import render_template,redirect,session,request,flash
from flask_app.models import players
from flask_bcrypt import Bcrypt
import logging
import json
import datetime
bcrypt = Bcrypt(app)


@app.route('/')
def home():
    return render_template("home.html")