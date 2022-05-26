from db import DB
from People import PeopleTable
from person import Person

database = DB('test.db')
conn = database.Conn
people = PeopleTable(conn)
# people.create_table()

p = Person('Ellen', 'Chambers', 18)
people.update_Person_by_id(1, p)
# p = Person('Delete', 'This', 54)
# people.add_person_record(p)

# people.delete_Person(7)

print(people.get_Person_by_id(2))
# print(people.get_Person_by_surname('Chambers'))

print(people.get_People())
