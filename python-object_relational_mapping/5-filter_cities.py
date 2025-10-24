#!/usr/bin/python3
""" This is the "5-filter_cities.py" module """
import MySQLdb
import sys


def list_all_cities(username, password, db, state_name):
    """
    Connects to MySQL and takes in the name of a state
    as an argument and lists all cities of that state
    SQL injection free
    """
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db
    )
    cursor = db.cursor()

    query = """
    SELECT cities.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE BINARY states.name = %s
    ORDER BY cities.id ASC
    """
    cursor.execute(query, (state_name,))

    rows = cursor.fetchall()
    print(", ".join([row[0] for row in rows]))

    cursor.close()
    db.close()


if __name__ == "__main__":
    list_all_cities(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
