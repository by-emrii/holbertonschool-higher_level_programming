#!/usr/bin/python3
""" This is the "model_city.py" module """
from model_state import Base
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class City(Base):
    """ City class linked to the 'cities' table in MySQL """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)

    # relationship to State
    state = relationship("State", backref="cities")
