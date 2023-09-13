# __init__.py
#this file within our flask app brings in an instance of flask
#Kind of like a class constructor
from flask import Flask
app = Flask(__name__)
#if the name of our app is equal to the main instance of our app, then run
app.secret_key = "ninjasss"