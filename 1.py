from db import DB
from People import PeopleTable
from person import Person

database = DB('test.db')
conn = database.Conn
people = PeopleTable(conn)
# people.create_table()

p = Person('Craig', 'Chambers', 54)
people.add_person_record(p)

print(people.get_People())

