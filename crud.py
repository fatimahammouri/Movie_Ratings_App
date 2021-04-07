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



if __name__== '__main__':
    from server import app
    connect_to_db(app)