#!/usr/bin/python3
"""
Python module that contains imports
"""


from sqlalchemy import Column, Integer, String, Sequence, ForeignKey
from relationship_state import Base, State


class City(Base):
    """
    Links class
    """

    __tablename__ = "cities"

    id = Column(Integer, Sequence("state_id_seq"),
                primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
