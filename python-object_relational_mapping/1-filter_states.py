#!/usr/bin/python3
""" This is the "1-filter_states.py" module """
import MySQLdb
import sys


def list_all_states_with_name_starting_N(username, password, database):
    """
    Connects to MySQL and list all the states
    in the database whose names start with N
    """
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )
    cursor = db.cursor()

    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    rows = cursor.fetchall()

    for row in rows:
        print(row)


if __name__ == "__main__":
    list_all_states_with_name_starting_N(sys.argv[1], sys.argv[2], sys.argv[3])
