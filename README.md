# LAB INFO

### Resources
* 0929 lab instructions: [click here](https://fellowship.hackbrightacademy.com/materials/serft8/lectures/sql-alchemy-1/)
* datetime from Python: [documentation](https://docs.python.org/3/library/datetime.html)


### Data Model
**users**
- fields:
    - id
    - email
    - password

**ratings**
- fields:
    - id: this rating item
    - userid
    - rating: the user's rating
    - movieid

**movies**
- fields:
    - id
    - title: movie title
    - rating: avg rating

MOVIES NOT YET RATED
```sql
SELECT movies.title FROM movies
  LEFT JOIN ratings ON (movies.id = ratings.movieid)
  WHERE ratings.userid <> :user_id;
```

MOVIES ALREADY RATED
```sql
SELECT movies.title FROM movies
  JOIN ratings ON (movies.id = ratings.movieid)
  WHERE ratings.userid = :user_id;
```

Twiddla
https://www.twiddla.com/f5vk6r

### NEXT STEPS!
Start testing with:
`createdb ratings`


### METHODS OF ADDING INFO USING FOREIGN KEYS
1. Flora's strange way (similar to #4):
```python
>>> test_rating = Rating(user_id=test_user.user_id, rating=4, movie_id=1)
>>> db.session.add(test_rating)
>>> db.session.commit()
```

2. Use the User object:
```python
>>> rat = Rating(rating=5, movie=movies[0])
>>> test_user.ratings.append(rat)
>>> db.session.commit()
```

3. Use the Movie object:
```python
>>> rat = Rating(rating=5, user=test_user)
>>> movies[0].ratings.append(rat)
>>> db.session.commit()
```

4. Use the Rating object:
```python
>>> rat = Rating(rating=5, user=test_user, movie=movies[0])
>>> db.session.add(rat)
>>> db.session.commit()
```

