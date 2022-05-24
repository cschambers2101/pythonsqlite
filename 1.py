from db import DB
from People import PeopleTable


database = DB('test.db')
conn = database.Conn
people = PeopleTable(conn)
people.create_table()
