#!/usr/bin/python3
"""
script that deletes all State objects with
a name containing the letter a from the database hbtn_0e_6_usa
"""

from sys import argv
from model_state import Base, State
from model_city import City
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

    res = session__.query(State, City).filter(City.state_id == State.id).\
    order_by(City.id).all()

    for get in res:
        print("{}: ({}) {}".format(get.State.name, get.City.id, get.City.name))
    session__.close()
