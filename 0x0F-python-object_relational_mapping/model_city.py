#!/usr/bin/python3
"""
Defines a state class
"""
from model_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """
    State class
    Attributes:
        __tablename__(str): the table name
        id (int): id
        name (str): state name
    """

    __tablename__ = "cities"

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
