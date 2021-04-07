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
# Replace this with routes and view functions!


if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
