#!/usr/bin/python3
"""
inserts a new State into the database hbtn_0e_6_usa
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

    # create new state object
    new_state = State(name="Louisiana")

    # add and commit to database
    session.add(new_state)
    session.commit()

    # print the new states id
    print(new_state.id)

    # close session
    session.close()
