import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """ Create a database connection to the SQLite database specified by db_file
    :param db_file: name of database file
    :return: Connection object of the database or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn

def check_table_exists(conn, table):
    """ Checks if the table exists in the database
    :param conn: Connection to the database
    :param table: The table name as a string to check
    :return: True is table exists, False if not
    """
    query = f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table}';"
    cursor = conn.execute(query)
    data = cursor.fetchall()
    if len(data) > 0:
        return True
    else:
        return False


def create_table(conn, table, query):
    """ Creates a table
    :param conn: Connection to the database
    :param table: Name of the table to check
    :param query: SQL query to create the table
    """
    conn.execute(query)
    if check_table_exists(conn, table):
        print(f'{table} Table created')
    else:
        print(f'ERROR: {table} table was not created')


def get_all_records(conn, table):
    """ Gets all the records from the table
    :param conn: Connection to database
    :param table: Table to retrieve records from
    :return : Results
    """
    query = f'SELECT * FROM {table}'
    cur = conn.cursor()
    cur.execute(query)
    data = cur.fetchall()
    return data


def create_record(conn, table, data):
    """ Creates a record into the table from the data provided
        :param conn: Connection to database
        :param table: Table to insert record into
        :param data: Data to insert into record
        :return : ID of the new record inserted into the table
    """
    query = f'INSERT INTO "{table}" ("FirstName", "Surname") VALUES (?,?);'
    cur = conn.cursor()
    cur.execute(query, data)
    conn.commit()
    return cur.lastrowid


def main():
    database = 'test.db'

    # create a database connection
    conn = create_connection(database)
    with conn:
        if not check_table_exists(conn, 'People'):
            query = """ CREATE TABLE "People" (
                        "id"	INTEGER NOT NULL UNIQUE,
                            "FirstName"	TEXT NOT NULL,
                                "Surname"	TEXT NOT NULL,
                                    PRIMARY KEY("id" AUTOINCREMENT)
                                        );
                    """
            create_table(conn, 'People', query)
        else:
            print('People table exists')

    # Uncomment to create a new record
    # record_id = create_record(conn, 'People', ('Nicky', 'Chambers'))
    # print(f'Record no: {record_id} created')

    print(get_all_records(conn, 'Test'))

if __name__ == '__main__':
    main()
