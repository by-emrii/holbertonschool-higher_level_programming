#!/usr/bin/python3
"""
prints all City objects from the database hbtn_0e_14_usa
"""

from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import (create_engine)
from model_state import State, Base
import sys
from model_city import City


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
    cities = (
        session.query(City)
        .order_by(City.id).all()
    )

    # print each city with state name, ordered by id
    for city in cities:
        state_name = city.state.name
        print(f"{state_name}: ({city.id}) {city.name}")

    # close session
    session.close()
