#!/usr/bin/python3
"""
a state class
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """ state class """
    __tablename__ = "states"
    id = Column(Integerm primary_keuy=True, nullable=False, autoincrement=True)
    name = Column(string(128), nullable=False)
