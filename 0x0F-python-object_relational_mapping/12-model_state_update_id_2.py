#!/usr/bin/python3
"""
script that changes the name of a State
object from the database hbtn_0e_6_usa
Change the name of the State where id = 2 to New Mexico
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

    update_state = session__.query(State).filter(State.id == 2).one_or_none()
    if update_state is not None:
        update_state.name = "New Mexico"
        session__.commit()
