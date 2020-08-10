#!/usr/bin/python3
"""
 a script that adds the State object
 Louisiana to the database hbtn_0e_6_usa
"""

from sys import argv
from model_state import Base, State

from sqlalchemy import (create_engine, Table, Integer,
                        String, Column)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)
    session = sessionmaker()
    session.configure(bind=engine)
    session__ = session()

    add_state = State(name="Louisiana")
    session__.add(add_state)
    session__.flush()
    print(add_state.id)
    session__.commit()
