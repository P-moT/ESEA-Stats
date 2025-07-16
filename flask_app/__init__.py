from flask import Flask, url_for
import logging

class Config:
    ''


logging.basicConfig(filename='record.log', level=logging.INFO, filemode='w')
app = Flask(__name__)
app.secret_key = '1337'
app.config.from_object(Config)