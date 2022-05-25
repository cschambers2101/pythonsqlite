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

    def get_People(self):
        """Gets all the People from the Database
        :return : All people in database
        """
        query = 'SELECT * FROM People'
        self.cursor.execute(query)
        data = self.cursor.fetchall()
        return data

    def get_users(self):
        users = []
        try:
            self.conn.row_factory = sqlite3.Row
            cur = self.conn.cursor()
            cur.execute("SELECT * FROM People")
            rows = cur.fetchall()

            # convert row objects to dictionary
            for i in rows:
                user = {}
                user["id"] = i["id"]
                user["firstname"] = i["firstName"]
                user["surname"] = i["surname"]
                users.append(user)

        except Exception as ex:
            print(type(ex).__name__, ex.args)
            users = []

        return users

    def get_Person_by_id(self, id):
        """Gets a person by their id
        :param id: ID of the person to get
        :return : The person
        """
        query = f'SELECT * FROM People WHERE id={id};'
        self.cursor.execute(query)
        data = self.cursor.fetchone()
        return data

    def get_Person_by_surname(self, surname):
        """Gets a person by searching for everyone with the surname
        :param surname: Surname to search for
        :return : List of people matching surname
        """
        query = f'SELECT * FROM People WHERE surname="{surname}";'
        self.cursor.execute(query)
        data = self.cursor.fetchall()
        return data

    def delete_Person(self, id):
        """Deletes a person with matching ID
        :param id: ID of the person you wish to delete
        """
        query = f'DELETE FROM People WHERE id={id};'
        self.cursor.execute(query)
        self.conn.commit()
