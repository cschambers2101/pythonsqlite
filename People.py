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
        self.cursor.execute(query, (person.firstName, person.surname, person.age))
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

    def delete_Person(self, id):
        """Deletes a person with matching ID
        :param id: ID of the person you wish to delete
        """
        query = f''
        self.cursor.execute(query)
        self.conn.commit()
        