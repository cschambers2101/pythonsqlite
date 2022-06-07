from logging import exception
from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os


# init flask app
app = Flask(__name__)

# get the directory of our app
basedir = os.path.abspath(os.path.dirname(__file__))
# set the path to the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + 'db.sqlite'
# required to stop some warnings in the console
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# init SQL Alchemy
db = SQLAlchemy(app)
# init Marshmallow
ma = Marshmallow(app)

# creates the database model for the table


class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    surname = db.Column(db.String(100))

    def __init__(self, firstname, surname):
        self.first_name = firstname
        self.surname = surname

# creates the schema for marshmallow to use


class PeopleSchema(ma.Schema):
    class Meta:
        fields = ('id', 'first_name', 'surname')


# creates an instance of the schema
person_schema = PeopleSchema()  # single person
people_schema = PeopleSchema(many=True)  # people

# C.R.U.D. operations for API
# Creates a new person in the databse


@app.route('/people', methods=['POST'])
def add_person():
    firstname = request.json['first_name']
    surname = request.json['surname']

    new_person = People(firstname, surname)
    db.session.add(new_person)
    db.session.commit()

    return person_schema.jsonify(new_person)


# Gets all people in the database
@app.route('/people', methods=['GET'])
def get_people():
    all_people = People.query.all()
    result = people_schema.dump(all_people)
    return jsonify(result)


# Gets a single person by ID
@app.route('/people/<id>', methods=['GET'])
def get_person(id):
    person = People.query.get(id)
    return person_schema.jsonify(person)


# Updates a person with the id
@app.route('/people/<id>', methods=['PUT'])
def update_person(id):
    person = People.query.get(id)
    first_name = request.json['first_name']
    surname = request.json['surname']

    person.first_name = first_name
    person.surname = surname

    db.session.commit()
    return person_schema.jsonify(person)


# Deletes the person with the id
@app.route('/people/<id>', methods=['DELETE'])
def delete_person(id):
    person = People.query.get(id)
    if person == None:
        abort(404)
        
    db.session.delete(person)
    db.session.commit()
    return person_schema.jsonify(person)
        


# Main program loop
if __name__ == '__main__':
    app.run()
