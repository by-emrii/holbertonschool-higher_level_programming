#!/usr/bin/python3
"""
deletes all State objects with a name containing
the letter a from the database hbtn_0e_6_usa
"""

from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import (create_engine)
from model_state import State, Base
import sys


if __name__ == "__main__":
    # CLI arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # create connection between sqlalchemy to mysql server
    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost:3306/{database}",
        pool_pre_ping=True
        )

    # bind engine to a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # query states with the letter a
    states = (
        session.query(State)
        .filter(State.name.like("%a%"))
        .all())

    # delete each state using loop
    for state in states:
        session.delete(state)
    session.commit()

    # close session
    session.close()
