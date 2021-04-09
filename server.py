"""Server for movie ratings app."""
# import libraries for flask 
from flask import (Flask, render_template, request, flash, session,
                   redirect)
                
# import other files I wrote :)   
from model import connect_to_db
import crud
from jinja2 import StrictUndefined

# configure the Flask instance and a secret key
app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined



# this is a route to the home page
@app.route('/')
def homepage():
    return render_template('homepage.html')

########################################################################################
# this route is for rendering a page that shows all movies
@app.route('/movies')
def all_movies():
    movies = crud.get_movies()

    return render_template('all_movies.html', movies=movies) #movies here is what
                                                            #i'm passing to jinja
########################################################################################
# this route will render a page of a single movie details
@app.route('/movies/<movie_id>')
def show_movie(movie_id): # ?????????????? 

    movie = crud.get_movie_by_id(movie_id)
    return render_template('movie_details.html', movie=movie)

########################################################################################


if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
