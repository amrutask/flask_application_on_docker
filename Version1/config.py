from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager
import os

#Creating a Flask instance for the application
app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

#setting database URI for sqlite database
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + os.path.join(basedir ,"planet_database.db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

#creating SQLAlchemy database instance
db = SQLAlchemy(app)

#To generate JWT tokens for API security
app.config['JWT_SECRET_KEY'] = 'super-secret'
jwt = JWTManager(app)


