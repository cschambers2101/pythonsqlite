import sqlite3
from sqlite3 import Error
import db


def create_People_Table(conn):
    if not db.check_table_exists(conn, 'People'):
        query = """ CREATE TABLE "People" (
                        "id"	INTEGER NOT NULL UNIQUE,
                            "FirstName"	TEXT NOT NULL,
                                "Surname"	TEXT NOT NULL,
                                    PRIMARY KEY("id" AUTOINCREMENT)
                                        );
                    """
        db.create_table(conn, 'People', query)


def main():
    conn = db.create_connection('people.db')
    create_People_Table(conn)


if __name__ == '__main__':
    main()
