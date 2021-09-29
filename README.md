# LAB INFO

### Resources
* 0929 lab instructions: [click here](https://fellowship.hackbrightacademy.com/materials/serft8/lectures/sql-alchemy-1/)

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