#!/usr/bin/python3
"""
print the State object with the name passed
as argument from hbtn_0e_6_usa.
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
    name = sys.argv[4]

    # create connection between sqlalchemy to mysql server
    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost:3306/{database}",
        pool_pre_ping=True
        )

    # bind engine to a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # query first state
    state = (
        session.query(State)
        .filter(State.name == name)
        .first()
        )

    # print results in format
    if state is None:
        print("Not found")
    else:
        print(state.id)

    # close session
    session.close()
