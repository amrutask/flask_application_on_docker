
# RESTful web service in Python using Flask microframework

## Description:
The application uses:
* Flask framework to create REST APIs
* SQLAlchemy allows managing database using ORMs in python

### The application creates a sqlite database containing two tables:
#### 1.planets   [This can store information about the planets]
   ```
   planet_id (primary key)
   planet_name
   planet_type
   home_star
   mass
   radius
   distance
   ```
   
#### 2. users   [Users can manage the planets data by adding new planets, updating it or deleting with user authentication]
```
  user_id (primary key)
  first_name
  last_name
  email (unique)
  password
  ```