from flask import Flask, jsonify
from db import DB
from People import PeopleTable
from person import Person
import json


database = DB('test.db')
conn = database.Conn
people = PeopleTable(conn)

app = Flask(__name__)


@app.route('/')
def index():
    return jsonify(people.get_People())


if __name__ == '__main__':
    app.run(debug=True)
