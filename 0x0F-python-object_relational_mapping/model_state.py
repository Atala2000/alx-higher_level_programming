#!/usr/bin/python3
"""
Defines a state class
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    State class
    Attributes:
        __tablename__(str): the table name
        id (int): id
        name (str): state name
    """

    __tablename__ = "states"

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
