import sqlite3
import psycopg2

def get_connection_info(id):
    dbname = ""
    user = ""
    password = ""
    host = ""
    port = ""

    try:
        sqlite_connection =  sqlite3.connect('db.sqlite3')
        cursor = sqlite_connection.cursor()
        print("Fetching fields from API")

        cursor.execute("select dbname from connection_connection where id = " + id + ";")
        dbname = str(cursor.fetchone())
        cursor.execute("select user from connection_connection where id = " + id + ";")
        user = str(cursor.fetchone())
        cursor.execute("select password from connection_connection where id = " + id + ";")
        password = str(cursor.fetchone())
        cursor.execute("select host from connection_connection where id = " + id + ";")
        host = str(cursor.fetchone())
        cursor.execute("select port from connection_connection where id = " + id + ";")
        port = str(cursor.fetchone())
        cursor.execute("select query from query_query where connection_id = " + id + ";")
        query = cursor.fetchone()
        cursor.close()
    except sqlite3.Error as error:
        print("Error while connecting to sqlite3", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("sqlite connection closed")
    
def query(dbname, user, password, host, port, query):
    connection = psycopg2.connect("dbname=" + dbname + " user=" + user)

    cursor = connection.cursor()
    cursor.execute(query)
    records = cursor.fetchall()
    return records