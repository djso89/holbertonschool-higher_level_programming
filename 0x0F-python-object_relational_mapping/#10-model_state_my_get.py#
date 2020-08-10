#!/usr/bin/python3
"""
script that prints the State object with the name
passed as argument from the database hbtn_0e_6_usa
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

    state_found = (session__.query(State)
                   .order_by(State.id).filter(State.name == argv[4]).first())
    if state_found is None:
        print("Not found")
    else:
        print("{}".format(state_found.id))
