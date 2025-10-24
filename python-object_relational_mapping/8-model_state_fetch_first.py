#!/usr/bin/python3
"""
lists first state object from the database hbtn_0e_6_usa
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
    state = session.query(State).first()

    # print results in format, handle empty table
    if state is None:
        print("Nothing")
    else:
        print(f"{state.id}: {state.name}")

    # close session
    session.close()
