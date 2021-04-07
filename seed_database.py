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



# create empty list 
movies_in_db = []

# loop over each movie from movies_data list we got from json file
# get it's values for the keys{title, overview...}
# call create_movie function from crud.py
# append this new movie to the empty List
for movie in movie_data:
    title, overview, poster_path = (movie['title'],
                                     movie['overview'], 
                                     movie['poster_path'])

    release_date = datetime.strptime(movie['release_date'],'%Y-%m-%d')

    db_movie = crud.create_movie(title, overview,release_date,poster_path)
    movies_in_db.append(db_movie)
