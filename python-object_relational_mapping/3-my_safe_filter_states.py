#!/usr/bin/python3
""" This is the "3-my_safe_filter_states.py" module """
import MySQLdb
import sys


def safe_filter_states(username, password, db, state_name_searched):
    """
    Connects to MySQL and lists states matching
    the given name safely
    """
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db
    )
    cursor = db.cursor()

    # parameterised query - safe from sql injection
    query = "SELECT * FROM states WHERE BINARY name = %s"
    cursor.execute(query, (state_name_searched,))

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    safe_filter_states(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
