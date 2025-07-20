from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
import logging
db = "ESEAStats"

class Player:
    def __init__(self, data):
        self.id = data['id']
        self.steamid = data['steamid']
        self.faceitid = data['faceitid']
        self.nickname = data['nickname']
        self.team = data['team']

class Team:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.faceitid = data['faceitid']
        self.logopath = data['logopath']

    @classmethod
    def check_team(cls, data):
        query = "SELECT id FROM teams WHERE faceitid = %(faceitid)s;"
        results = connectToMySQL(db).query_db(query, data)
        print(results)
        if len(results) > 0:
            return results[0]['id']
        else:
            return False

    @classmethod
    def create_team(cls, data):
        query = "INSERT INTO teams (name, faceitid, logopath) VALUES (%(name)s, %(faceitid)s, %(logopath)s);"
        return connectToMySQL(db).query_db(query, data)

class Match:
    def __init__(self, data):
        self.id = data['id']
        self.matchid = data['matchid']
        self.team1 = data['team1']
        self.team2 = data['team2']
        self.competition = data['competition']
        self.matchtime = data['matchtime']
        self.team1score = data['team1score']
        self.team2score = data['team2score']

    @classmethod
    def get_match_details(cls, data):
        query = "SELECT * FROM matches WHERE matchid = %(matchid)s"
        results = connectToMySQL(db).query_db(query, data)
        print(results)
        return Match(results[0])
    
    @classmethod
    def import_match_details(cls, data):
        query = "INSERT INTO matches (matchid, team1, team2, competition, matchtime, team1score, team2score, teams_id) VALUES" \
        " (%(matchid)s, %(team1)s, %(team2)s, %(competition)s, %(matchtime)s, %(team1score)s, %(team2score)s, %(teams_id)s);"
        return connectToMySQL(db).query_db(query, data)
    



