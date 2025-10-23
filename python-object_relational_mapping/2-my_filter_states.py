#!/usr/bin/python3
""" This is the "2-my_filter_states.py" module """
import MySQLdb
import sys


def list_all_states(username, password, db, state_name_searched):
    """
    Connects to MySQL and displays all values in the states table
    where state name searched matches the argument
    """
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db
    )
    cursor = db.cursor()
    query = (
        "SELECT * FROM states "
        "WHERE name = '{}'".format(state_name_searched))
    cursor.execute(query)

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    list_all_states(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
