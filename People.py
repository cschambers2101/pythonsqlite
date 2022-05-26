import sqlite3


class PeopleTable:
    """Interacts with the People table in the SQL Dtabase"""

    def __init__(self, conn) -> None:
        self.conn = conn
        self.cursor = conn.cursor()
        self.create_table()

    def create_table(self):
        """Creates the People table if it doesn't exist"""
        query = 'CREATE TABLE IF NOT EXISTS "People" ("id"	INTEGER NOT NULL UNIQUE,"FirstName"	TEXT NOT NULL,"Surname"	TEXT NOT NULL,"Age"	INTEGER NOT NULL,PRIMARY KEY("id" AUTOINCREMENT));'
        self.cursor.execute(query)

    def add_person_record(self, person):
        """Adds a person record to the People table"""
        query = 'INSERT INTO "People" ("FirstName", "Surname", "Age") VALUES (?,?,?);'
        self.cursor.execute(
            query, (person.firstName, person.surname, person.age))
        self.conn.commit()
        return self.cursor.lastrowid

    def sql_data_to_list_of_dicts(self, data):
        """Returns data from an SQL query as a list of dicts."""
        try:
            unpacked = [{k: item[k] for k in item.keys()} for item in data]
            return unpacked
        except Exception as e:
            print(f"Failed to uppack data with error:\n{e}")
            return []

    def get_Data(self, query):
        """ Runs query and returns data as a list of dictionaries
        :param query: SQL query to run on the database
        :return : result from query as list of dictionaries
        """
        try:
            self.conn.row_factory = sqlite3.Row
            cur = self.conn.cursor()
            cur.execute(query)
            rows = cur.fetchall()

            # convert row objects to dictionary
            data = self.sql_data_to_list_of_dicts(rows)
            return data
        except Exception as ex:
            print(type(ex).__name__, ex.args)

    def get_People(self):
        """ Lists all the people from the database
        :return : Dictionary of all people in the database
        """
        return self.get_Data('SELECT * FROM People')

    def get_Person_by_id(self, id):
        """Gets a person by their id
        :param id: ID of the person to get
        :return : The person
        """
        return self.get_Data(f'SELECT * FROM People WHERE id={id};')

    def get_Person_by_surname(self, surname):
        """Gets a person by searching for everyone with the surname
        :param surname: Surname to search for
        :return : List of people matching surname
        """
        return self.get_Data(f'SELECT * FROM People WHERE surname="{surname}";')

    def delete_Person(self, id):
        """Deletes a person with matching ID
        :param id: ID of the person you wish to delete
        """
        query = f'DELETE FROM People WHERE id={id};'
        self.cursor.execute(query)
        self.conn.commit()

    def update_Person_by_id(self, id, person):
        """Updates details pf person with the id given
        :param id: id of person to update
        :param person: Person instance to update information with
        """
        query = f"UPDATE People SET firstName = '{person.firstName}', surname= '{person.surname}' WHERE id = {id};"
        self.cursor.execute(query)
        self.conn.commit()
