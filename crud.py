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




if __name__== '__main__':
    from server import app
    connect_to_db(app)