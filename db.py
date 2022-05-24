import sqlite3
from sqlite3 import Error


class DB:
    """ Initialialise a database and creates a connection string"""

    @property
    def Conn(self):
        """ Returns connection to database"""
        return self.conn

    # @Conn.setter
    # def Conn(self, value):
    #     print("setter of x called")
    #     self.conn = value

    def __init__(self, filename) -> None:
        """ Creates a database during instance construction
        :param db_name: database filename
        :param conn: Connection to the database
        """
        self.db_name = filename
        self.conn = None
        self.create_connection(self.db_name)
    

    def create_connection(self, db_file):
        """ Create a database connection to the SQLite database specified by db_file
        :param db_file: name of database file
        """
        conn = None
        try:
            conn = sqlite3.connect(db_file)
        except Error as e:
            print(e)
        self.conn = conn


if __name__ == '__main__':
    print('Must be loaded as a module')
