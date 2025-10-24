#!/usr/bin/python3
""" This is the "4-cities_by_state.py" module """
import MySQLdb
import sys


def list_all_cities(username, password, db):
    """
    Connects to MySQL and lists all cities
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
    SELECT cities.id, cities.name, states.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    ORDER BY cities.id ASC
    """
    cursor.execute(query)

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    list_all_cities(sys.argv[1], sys.argv[2], sys.argv[3])
