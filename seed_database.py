"""Script to seed our db :)"""
# importing some modules and Libraries
import os
import json
from random import choice, randint
from datetime import datetime

# importing other files I wrote
import crud
import model
import server

# we write scriptt that makes python to run these commands
os.system('dropdb ratings')
os.system('createdb ratings')

# from model.py get these functions
model.connect_to_db(server.app)
model.db.create_all()

# load data from data/movies.json file & save it to a var
with open('data/movies.json') as f:
    movie_data = json.loads(f.read())


