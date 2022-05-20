import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def check_table_exists(conn, table):
    query = f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table}';"
    cursor = conn.execute(query)
    data = cursor.fetchall()
    if len(data) > 0:
        return True
    else:
        return False


def create_table(conn, table, query):
    conn.execute(query)
    if check_table_exists(conn, table):
        print(f'{table} Table created')
    else:
        print(f'ERROR: {table} Table was not created')


def create_record(conn, table, data):
    query = """ INSERT INTO "main"."People"
                ("FirstName", "Surname")
                    VALUES (?,?);"""
    cur = conn.cursor()
    cur.execute(query, data)
    conn.commit()
    return cur.lastrowid


def get_all_records(conn):
    query = """ SELECT * FROM People """
    cur = conn.cursor()
    cur.execute(query)
    data = cur.fetchall()
    print(data)


def get_records_that_match(conn, searchTerm):
    query = f' SELECT * FROM People WHERE FirstName = "{searchTerm}"'
    cur = conn.cursor()
    cur.execute(query)
    data = cur.fetchall()
    print(data)


def main():
    database = 'test.db'

    # create a database connection
    conn = create_connection(database)
    with conn:
        if not check_table_exists(conn, 'People'):
            query = """ CREATE TABLE "People" (
                    "id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                    "FirstName"	TEXT NOT NULL,
                    "Surname"	TEXT NOT NULL
                    );
                    """
            create_table(conn, 'People', query)
        else:
            print('People Table exists')

        # record_id = create_record(conn, 'People', ('Nicky', 'Chambers'))
        # print(f'Record no: {record_id} created')

        get_all_records(conn)
        get_records_that_match(conn, 'Craig')


if __name__ == '__main__':
    main()
