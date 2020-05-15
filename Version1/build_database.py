import os
from config import db
from model import User, Planet

if os.path.exists("planet_database.db"):
    os.remove("planet_database.db")

# creating the sqlite database
db.create_all()

# These are just for examples, ignore the information if it is incorrect
mercury = Planet(planet_name = "Mercury",
                 planet_type="Class D",
                 home_star = "Sol",
                 mass = 3.258e23,
                 radius = 1516,
                 distance = 35.98e6)    

venus = Planet(planet_name = "Venus",
                planet_type="Class K",
                home_star = "Sol",
                mass = 4.867e24,
                radius = 3760,
                distance = 67.24e6)

earth = Planet(planet_name = "Earth",
                planet_type="Class M",
                home_star = "Sol",
                mass = 5.972e24,
                radius = 3959,
                distance = 92.96e6) 

# adding 3 different planets
db.session.add(mercury)
db.session.add(venus)
db.session.add(earth)

# Commit the chnages to the database
db.session.commit()   





