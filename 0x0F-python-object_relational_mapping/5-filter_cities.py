#!/usr/bin/python3
"""
script that takes in the name of a state
as an argument and lists all cities of that state,
using the database hbtn_0e_4_usa
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    data = MySQLdb.connect(host="localhost", user=argv[1],
                           passwd=argv[2], db=argv[3])
    current = data.cursor()
    current.execute("SELECT cities.name \
    FROM cities LEFT JOIN states \
    ON cities.state_id = states.id \
    WHERE states.name=%s", (argv[4], ))

    cities = current.fetchall()

    list_cities = [city[0] for city in cities]

    print(", ".join(list_cities))
    current.close()
    data.close()
