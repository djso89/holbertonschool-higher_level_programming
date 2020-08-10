#!/usr/bin/python3
"""
script that lists all states with a name starting
with N (upper N) from the database hbtn_0e_0_usa
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    data = MySQLdb.connect(host="localhost", user=argv[1],
                           passwd=argv[2], db=argv[3])
    current = data.cursor()
    current.execute("SELECT * FROM states WHERE states.name LIKE BINARY 'N%' \
    ORDER BY states.id ASC")

    states = current.fetchall()
    for state in states:
        print(state)
    current.close()
    data.close()
