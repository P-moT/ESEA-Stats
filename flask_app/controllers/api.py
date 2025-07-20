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
    with open('details.json', "w") as file:
        json.dump(match_details, file, indent=4)
    with open('stats.json', "w") as file:
        json.dump(match_stats, file, indent=4)
    teams_id = 0
    print(f'Team ID set to {teams_id}')
    org_teams = [1,2,3]
    team1id = match_details['teams']['faction1']['faction_id']
    team2id = match_details['teams']['faction2']['faction_id']
    data = {
        'faceitid': team1id
    }
    check_id = players.Team.check_team(data)
    if check_id in org_teams:
        teams_id = check_id
    if not players.Team.check_team(data):
        data = {
            'name': match_details['teams']['faction1']['name'],
            'faceitid': match_details['teams']['faction1']['faction_id'],
            'logopath': match_details['teams']['faction1']['avatar']
        }
        players.Team.create_team(data)
    data = {
        'faceitid': team2id
    }
    check_id = players.Team.check_team(data)
    if check_id in org_teams:
        teams_id = check_id
    if not players.Team.check_team(data):
        data = {
            'name': match_details['teams']['faction2']['name'],
            'faceitid': match_details['teams']['faction2']['faction_id'],
            'logopath': match_details['teams']['faction2']['avatar']
        }
        players.Team.create_team(data)
    print(teams_id)
    data = {
        'matchid': match_details['match_id'],
        'team1': match_stats['rounds'][0]['teams'][0]['team_stats']['Team'],
        'team2': match_stats['rounds'][0]['teams'][1]['team_stats']['Team'],
        'team1score': match_stats['rounds'][0]['teams'][0]['team_stats']['Final Score'],
        'team2score': match_stats['rounds'][0]['teams'][1]['team_stats']['Final Score'],
        'competition': match_details['competition_name'],
        'matchtime': datetime.date.fromtimestamp(match_details['started_at']),
        'teams_id': teams_id
    }
    players.Match.import_match_details(data)
    return redirect('/')
