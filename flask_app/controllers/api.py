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

PROD_API_URL = "https://open.faceit.com/data/v4"

@app.route('/api/player', methods=['POST'])
def get_player():
    headers = {
        "Authorization" : "Bearer " + os.environ.get("API_KEY")
    }
    player_id = request.form['playerid']
    url = PROD_API_URL + f'/players/{player_id}'
    response = requests.get(url=url,headers=headers)
    with open('output.json', "w") as file:
        json.dump(response.json(), file, indent=4)
    data = response.json()
    print(data['nickname'])
    print(data['steam_id_64'])
    return redirect('/')

@app.route('/api/stats', methods=['POST'])
def get_stats():
    headers = {
        "Authorization" : "Bearer " + os.environ.get("API_KEY")
    }
    match_id = request.form['ID']
    match_details_url = PROD_API_URL + f'/matches/{match_id}'
    match_details = (requests.get(url=match_details_url, headers=headers)).json()
    match_stats_url = PROD_API_URL + f'/matches/{match_id}/stats'
    match_stats = (requests.get(url=match_stats_url, headers=headers)).json()
    teams = []
    for key in match_details['teams']:
        teams.append(match_details['teams'][key]['name'])
        print(f'{key} is {match_details['teams'][key]['name']}')
    session['team_list'] = teams
    return redirect(f'/match/{match_id}')