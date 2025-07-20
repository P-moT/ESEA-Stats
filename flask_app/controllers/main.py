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

@app.route('/media')
def media():
    return render_template('media.html')

@app.route('/shop')
def shop():
    return render_template('shop.html')

@app.route('/teams')
def teams():
    return render_template('teams.html')

@app.route('/core')
def core():
    return render_template('core.html')

@app.route('/teams/core-black')
def core_black():
    return render_template('C0reBlack.html')

@app.route('/teams/core-white')
def core_white():
    return render_template('C0reWhite.html')

@app.route('/teams/core-red')
def core_red():
    return render_template('C0reRed.html')