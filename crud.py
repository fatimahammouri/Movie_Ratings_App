"""C R U D Operation Functions"""

from model import db, Movie, User, Rating, connect_to_db


def create_user(email, password):
    """Create & return a New User
        Soo... I will write this function to insantiate a user
        from the Class User and add it to the session and commit
        it to the db then return that user back to us :)"""

    user = User(email=email, password=password)

    db.session.add(user)
    db.session.commit()

    return user

def create_movie(title, overview, release_date, poster_path):
    """Create & Return a new Movie 
        Soo... I will write  this function to instantiate a user
        from the Class Movie, add it to the session and commit
        it to the db then return that movie back to us :)"""

    movie = Movie(title=title, overview=overview,
                    release_date=release_date, poster_path=poster_path)
    
    db.session.add(movie)
    db.session.commit()

    return movie


# after we wrote a function to create a movie
# now, let's write a function to return ALL movies
def get_movies():
    """this function is to retorn ALL movies"""
    return Movie.query.all()

# this function is to help us get a specific Movie by it's id 
# so we can use it in the /movie/<movie_id> route 
def get_movie_by_id(movie_id):
    """this function is to get a specific Movie by it's id"""
    return Movie.query.get(movie_id)


def create_rating(user, movie, score):
    """Create & return a New Rating
        Soo... This function will instantiate a rating 
        from the Class Rating, add it to the session and commit
        it to the db then return that rating back to us :)"""

    rating = Rating(user=user, movie=movie, score=score)

    db.session.add(rating)
    db.session.commit()

    return rating



if __name__== '__main__':
    from server import app
    connect_to_db(app)