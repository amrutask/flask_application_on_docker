from flask import request, jsonify
from flask_jwt_extended import jwt_required
# local modules
from config import app, jwt
import handle_db_requests

# handling all the API endpoints here

@app.route('/')           
def study_planets():
    return jsonify(message='Welcome, lets learn about planets!!'), 200


@app.route('/planets', methods=['GET'])
def get_planets():
    return handle_db_requests.get_all_planets()


@app.route('/register', methods=['POST'])
def add_user():
    return handle_db_requests.add_user(request.form['first_name'], request.form['last_name'], request.form['email'], request.form['password']) 


@app.route('/login', methods=['POST'])
def login():
    if request.is_json:
        email = request.json['email']
        password = request.json['email']
    else:
        email = request.form['email']
        password = request.form['password']

    return handle_db_requests.user_login(email, password)
    

@app.route('/planet/<int:id>', methods=['GET'])
def get_planet(id:int):
    return handle_db_requests.search_planet(id)    


@app.route('/add_planet', methods=['POST'])
@jwt_required                                             # User authenication using JWT 
def add_planet():
    planet_name = request.json['planet_name']
    planet_type = request.json['planet_type']
    home_star = request.json['home_star']
    mass = request.json['mass']
    radius = request.json['radius']
    distance = request.json['distance']

    return handle_db_requests.add_new_planet(planet_name, planet_type, home_star, mass, radius, distance)


@app.route('/update_planet', methods=['POST', 'PUT'])
@jwt_required
def update_planet():
    planet_id  = request.json['planet_id']
    planet_name = request.json['planet_name']
    planet_type = request.json['planet_type']
    home_star = request.json['home_star']
    mass = request.json['mass']
    radius = request.json['radius']
    distance = request.json['distance']

    return handle_db_requests.update_planet(planet_id, planet_name, planet_type, home_star, mass, radius, distance)


@app.route('/remove_planet/<int:id>', methods=['DELETE'])
@jwt_required
def remove_planet(id:int):
    return handle_db_requests.delete_planet(id)



if __name__ == '__main__':

    # Run the flask application
    app.run(host='0.0.0.0', debug=True)