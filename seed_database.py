"""Functions to restart database and auto-populate movie information."""

import os, json, crud, model, server
from random import choice, randint
from datetime import datetime

# Drop the database with dropdb
# Create the database with createdb
os.system('dropdb ratings')
os.system('createdb ratings')

# Use db.create_all to create tables

# Automatically populate the database with data:

# Use data from data/movies.json to create movies

# Create 10 random users; for each user, create 10 ratings on random movies with random scores
