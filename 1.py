from db import DB
from People import PeopleTable
from person import Person

database = DB('test.db')
conn = database.Conn
people = PeopleTable(conn)
# people.create_table()

# p = Person('Nicky', 'Chambers', 54)
# people.add_person_record(p)
# p = Person('Delete', 'This', 54)
# people.add_person_record(p)

# people.delete_Person(7)

print(people.get_Person_by_id(2))
# print(people.get_Person_by_surname('Chambers'))

print(people.get_People())
