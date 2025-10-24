#!/usr/bin/python3
"""
lists all state objects from the database hbtn_0e_6_usa
that contain the letter 'a'
"""

from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import (create_engine)
from model_state import State, Base
import sys

Base = declarative_base()

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

    # query first state
    states = (
        session.query(State)
        .filter(State.name.like("%a%"))
        .order_by(State.id)
        .all())

    # print results in format
    for state in states:
        print(f"{state.id}: {state.name}")

    # close session
    session.close()
