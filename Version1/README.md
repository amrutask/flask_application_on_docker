
# RESTful web service in Python using Flask microframework

## Description:
The application uses:
* Flask framework to create REST APIs
* SQLAlchemy to manage database using ORMs in python
* Docker to host the application

## Technologies
This project is created with:
 * Python version: 3.8
 * Flask version: 1.1.2
 * Flask-JWT-Extended version: 3.24.1
 * Flask-SQLAlchemy version: 2.4.1
 * SQLAlchemy version: 1.3.17
 * flask-marshmallow version: 0.12.0
 * marshmallow version: 3.6.0

## The application creates a sqlite database containing two tables:
#### 1.planets   [To store information about the planets]
   ```
   planet_id (primary key)
   planet_name
   planet_type
   home_star
   mass
   radius
   distance
   ```
   
#### 2. users   [To store Users information. Users can manage the planets data by adding new planets, updating it or deleting with user authentication]
  ```
  user_id (primary key)
  first_name
  last_name
  email (unique)
  password
  ```
  
  ## To run the application
  ### 1. Using docker-compose
  This command will build the application as well as execute it.
  
  `docker-compose up --build`
  
  ### 2. Using docker build and docker run
  
  `docker build -t flaskimage .`
  
   `docker run -p 5000:5000 flaskimage`
  
  ### 3. With no docker
   
   `python server.py`
