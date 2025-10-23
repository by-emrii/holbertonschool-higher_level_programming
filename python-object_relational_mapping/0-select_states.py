#!/usr/bin/python3
""" This is the "0-select_states.py" module """
import MySQLdb
import sys


def list_all_states(username, password, database):
    """ list all the states in the database """
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )
    cursor = db.cursor()

    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cursor.fetchall()

    for row in rows:
        print(row)


if __name__ == "__main__":
    list_all_states(sys.argv[1], sys.argv[2], sys.argv[3])
