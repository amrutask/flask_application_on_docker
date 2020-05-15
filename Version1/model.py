from config import db
from marshmallow import Schema, fields

#Adding ORMs
class Planet(db.Model):
    __tablename__ = 'planets'

    planet_id = db.Column(db.Integer, primary_key=True)
    planet_name = db.Column(db.String, nullable=False)
    planet_type = db.Column(db.String)
    home_star = db.Column(db.String)
    mass = db.Column(db.Float)
    radius = db.Column(db.Float)
    distance = db.Column(db.Float)


class User(db.Model):
    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)


#Using marshmallow for serialization
class PlanetSchema(Schema):
    planet_id = fields.Int()
    planet_name = fields.Str()
    planet_type = fields.Str()
    home_star= fields.Str()
    mass = fields.Float()
    radius = fields.Float()
    distance = fields.Float()


class UserSchema(Schema):
    user_id = fields.Int()
    first_name = fields.Str()
    last_name = fields.Str()
    email = fields.Str()
    password = fields.Str()
