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

