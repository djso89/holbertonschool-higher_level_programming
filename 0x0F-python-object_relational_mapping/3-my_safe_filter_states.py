#!/usr/bin/python3
"""displays all values in the states table of hbtn_0e_0_usa """

import MySQLdb
from sys import argv

if __name__ == "__main__":
    data = MySQLdb.connect(host="localhost", user=argv[1],
                           passwd=argv[2], db=argv[3])
    current = data.cursor()
    arg = ("%{}%".format(argv[4]))
    current.execute("SELECT * FROM states WHERE states.name LIKE BINARY \
    %s ORDER BY states.id ASC", [arg])

    states = current.fetchall()

    for state in states:
        print(state)
    current.close()
    data.close()
