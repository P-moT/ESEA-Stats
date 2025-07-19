from flask_app import app
from flask import render_template,redirect,session,request,flash,request
from flask_app.models import players
from flask_bcrypt import Bcrypt
import logging
import json, os, requests
import datetime
import dotenv
from os.path import dirname
bcrypt = Bcrypt(app)

@app.route('/')
def home():
    
    return render_template("home.html")

@app.route('/match/<match_id>/')
def match_page(match_id):
    list = session['team_list']
    team1 = list[0]
    team2 = list[1]
    session.clear()
    return render_template("scoreboard.html", team1 = team1, team2 = team2)