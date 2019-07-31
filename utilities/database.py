import sqlite3

def create_talbe(conn):
    sql = "CREATE TABLE h84clickb8(" \
          "news_id INTEGER PRIMARY KEY," \
          "title TEXT," \
          "content TEXT" \
          ");"
    cur = conn.cursor()
    cur.execute(sql)
    return cur.lastrowid

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except:
        print("Error connecting to database")

    return None

def create_entry(conn, entry):
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """
    sql = "INSERT INTO h84clickb8(title,content) VALUES(?,?)"
    cur = conn.cursor()
    cur.execute(sql, entry)
    return cur.lastrowid
