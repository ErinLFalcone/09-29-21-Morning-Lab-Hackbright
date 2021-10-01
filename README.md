# LAB INFO
**Date assigned:** 09/29/2021

**0929 lab instructions:** [click here](https://fellowship.hackbrightacademy.com/materials/serft8/exercises/ratings-v2/)

To be completed in 4 pair programming sessions.

### NEXT STEPS!
- [x] Start testing with: `createdb ratings`
- [x] Write the script in seed_database.py
  - [ ] how to display db.DateTime: want `2019-09-20 00:00:00` without the time at the end
- [ ] Part 3: [click here](https://fellowship.hackbrightacademy.com/materials/serft8/exercises/ratings-v2/index-3.html)

#

### RESOURCES
**LECTURES:**
* 0927 morning: [SQL I](https://fellowship.hackbrightacademy.com/materials/t3/lectures/sql-1/)
* 0927 afternoon: [SQL II](https://fellowship.hackbrightacademy.com/materials/t3/lectures/sql-2/)
* 0928 morning: [SQL III](https://fellowship.hackbrightacademy.com/materials/serft8/lectures/sql-3/)
* 0928 afternoon: [SQL & Python](https://fellowship.hackbrightacademy.com/materials/serft8/exercises/project-tracker-py/)
* 0929 morning: [SQLAlchemy I](https://fellowship.hackbrightacademy.com/materials/serft8/lectures/sql-alchemy-1/)
* 0929 afternoon: [SQLAlchemy II](https://fellowship.hackbrightacademy.com/materials/serft8/lectures/sql-alchemy-2/)
* 0930 afternoon: [Data Modeling](https://fellowship.hackbrightacademy.com/materials/serft8/lectures/data-modeling/)

**RELATED LABS:**
* 0927 Project Tracker: [click here](https://fellowship.hackbrightacademy.com/materials/serft8/exercises/project-tracker/)
* 0928 Project Tracker (Python): [click here](https://fellowship.hackbrightacademy.com/materials/serft8/exercises/project-tracker-py/)

**OTHER RESOURCES:**
* [Twiddla](https://www.twiddla.com/f5vk6r): drawing diagrams
* datetime from Python: [documentation](https://docs.python.org/3/library/datetime.html)
  * https://strftime.org
* dropdb: https://www.postgresql.org/docs/9.1/app-dropdb.html
#

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


#

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
```pythofirst
>>> rat = Rating(rating=5, user=test_user, movie=movies[0])
>>> db.session.add(rat)
>>> db.session.commit()
```
