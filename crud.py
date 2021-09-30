"""Functions to perform CRUD operations."""

from model import db, User, Movie, Rating, connect_to_db


def create_user(input_email, input_password):
    """Create and return a new user."""

    user = User(email=input_email, password=input_password)

    db.session.add(user)
    db.session.commit()

    return user


def create_movie(input_title, input_overview, input_release_date, input_poster_path):
    """Create and return a new movie."""
    
    movie = Movie(title=input_title, overview=input_overview, release_date=input_release_date, poster_path=input_poster_path)

    db.session.add(movie)
    db.session.commit()

    return movie


def create_rating(input_user_id, input_rating, input_movie_id):
    """Create and return a new rating."""
    
    rating = Rating(user_id=input_user_id, rating=input_rating, movie_id=input_movie_id)
    
    db.session.add(rating)
    db.session.commit()

    return rating
    

if __name__ == "__main__":
    from server import app
    connect_to_db(app)