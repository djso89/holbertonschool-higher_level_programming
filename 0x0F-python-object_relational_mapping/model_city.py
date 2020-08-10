#!/usr/bin/python3
"""
model city module
"""


from model_state import Base, State
from sqlalchemy import Column, Integer, String, Foreignkey
from sqlalchemy.ext.declarative import declarative_base

Base = decalarative_base()


class City(Base):
    """City class"""
    __tablename__ = "cities"

    id = Column(Integer, autoincrement=True, unique=True, nullable=False,
                primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey(State.id), nullable=False)
