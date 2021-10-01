"""Functions to restart database and auto-populate movie information."""

import os, json, crud, model, server
from random import choice, randint
from datetime import datetime

# Drop the database with dropdb
# Create the database with createdb
os.system('dropdb ratings')
os.system('createdb ratings')

# Use db.create_all to create tables

model.connect_to_db(server.app)
model.db.create_all()

movies_in_db = []
# Automatically populate the database with data:
with open('data/movies.json') as f:
    movie_data = json.loads(f.read())

    # Use data from data/movies.json to create movies
    
    for movie in movie_data:
        format = "%Y-%m-%d"  # %b 'Sep' vs %m '09'
        date = datetime.strptime(movie['release_date'], format)
        movie_obj = crud.create_movie(movie['title'], movie['overview'], date, movie['poster_path'])
        movies_in_db.append(movie_obj)

# Create 10 random users
# For each user, create 10 ratings on random movies with random scores

for n in range(10):
    email = f"user{n}@test.com"
    password = 'test'
    test_user = crud.create_user(email, password)

    for i in range(10):
        score = randint(1,5)
        movie = choice(movies_in_db)    # make sure it is unique, fixme later
        crud.create_rating(test_user.user_id, score, movie.movie_id)
