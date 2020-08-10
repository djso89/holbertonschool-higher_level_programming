#!/usr/bin/python3
"""
a script that prints the first State object
from the database hbtn_0e_6_usa
"""

import sys
from model_state import Base, State

from sqlalchemy import (create_engine, Table, Integer,
                        String, Column)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)
    session = sessionmaker()
    session.configure(bind=engine)
    session__ = session()

    get_first = session__.query(State).order_by(State.id).first()

    if get_first is not None:
        print("{}: {}".format(get_first.id, get_first.name))
    else:
        print("Nothing")
