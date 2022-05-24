from dbclass import DB


def get_connection():
    database = DB('Test.db')
    conn = DB.Conn
    return conn


if __name__ == '__main__':
    conn = get_connection()
    print(conn)
