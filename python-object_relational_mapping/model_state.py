#!/usr/bin/python3
""" This is the "model_state.py" module """
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine, Column, Integer, String

Base = declarative_base()


class State(Base):
    """ State class linked to the 'states' table in MySQL """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
