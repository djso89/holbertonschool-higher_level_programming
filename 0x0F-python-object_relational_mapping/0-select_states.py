#!/usr/bin/python3
# script that lists all states from the database
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    current = db.cursor()
    current.execute("SELECT * FROM states ORDER BY id")
    states = current.fetchall()
    for state in states:
        print(state)

    current.close()
    db.close()
