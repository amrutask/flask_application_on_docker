from flask import jsonify
# import json
from config import db, jwt
from model import User, Planet, UserSchema, PlanetSchema

# Handling all the db requests and 
# serialization of the result using Marshmallow schemas: UserSchema and PlanetSchema

def get_all_planets():
    planets = Planet.query.all()
    planets_schema = PlanetSchema(many=True)      # instatiating PlanetSchema for multiple planet instances using 'many' option
    data = planets_schema.dump(planets)
    return jsonify(data), 200

    '''
    #OR this using json                    # This can be used if not marshmallow
    result =[]
    for planet in planets:
        new_planet = {
            "planet_id":planet.planet_id,
            "planet_name":planet.planet_name,
            "planet_type":planet.planet_type,
            "home_star":planet.home_star,
            "mass":planet.mass,
            "radius":planet.radius,
            "distance":planet.distance
        }
        result.append(new_planet)

    return json.dumps(result)'''


def add_user(first_name, last_name, email, password):
    test = User.query.filter_by(email=email).first()

    if test:
        return jsonify(message='The email already exists'), 409

    else:
        new_user = User(first_name=first_name, last_name=last_name, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()

        return jsonify(message='User added successfully'), 201    


def search_planet(id):
    planet = Planet.query.filter_by(planet_id = id).first()

    if planet:

        planet_schema = PlanetSchema()               # instatiating PlanetSchema for a single planet instance
        return jsonify(planet_schema.dump(planet)), 200

        '''
        #Or this using json                 # This can be used if not marshmallow
        result = {
            "planet_id":test.planet_id,
            "planet_name":test.planet_name,
            "planet_type":test.planet_type,
            "home_star":test.home_star,
            "mass":test.mass,
            "radius":test.radius,
            "distance":test.distance
        }

        return json.dumps(result), 200'''
   
    else:
        return jsonify(message=f"Planet with Id {id} does not exist"), 404


def user_login(email, password):

    user = User.query.filter_by(email=email, password=password).first()

    if user:
        access_token = jwt._create_access_token(identity=email)
        return jsonify(message="Login Successful!", token = access_token)

    else:
        return jsonify(message="Bad Email or Password"), 401


def add_new_planet(planet_name, planet_type, home_star, mass, radius, distance):
    check_planet = Planet.query.filter_by(planet_name=planet_name).first()

    if check_planet:
        return jsonify(message=f"The planet named {planet_name} already exists"), 409

    else:
        new_planet = Planet(planet_name = planet_name, 
                             planet_type = planet_type,
                             home_star=home_star,
                             mass = float(mass),
                             radius = float(radius),
                             distance = float(distance))

        db.session.add(new_planet)
        db.session.commit()

        return jsonify(message="The planet was successfully added"), 201                         


def update_planet(planet_id, planet_name, planet_type, home_star, mass, radius, distance):
    planet = Planet.query.filter_by(planet_id = int(planet_id)).first()

    if planet:
        planet.planet_name = planet_name
        planet.planet_type = planet_type
        planet.home_star = home_star
        planet.mass = float(mass)
        planet.radius = float(radius)
        planet.distance = float(distance)

        db.session.commit()
        return jsonify(message="planet updated successfully!"), 202
    
    else:
        return jsonify(message=f"Sorry, planet with ID {planet_id} does not exist"), 404


def delete_planet(planet_id):

    planet = Planet.query.filter_by(planet_id = planet_id).first()

    if planet:
        db.session.delete(planet)
        db.session.commit()
        return jsonify(message=f"Planet {planet.planet_name} removed successfully!"), 202

    else:
        return jsonify(message=f"Sorry, planet with ID {planet_id} does not exist"), 404