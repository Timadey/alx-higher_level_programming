#!/usr/bin/python3
"""
lists all cities from the database hbtn_0e_4_usa
"""
import sys
import MySQLdb as sql

if __name__ == '__main__':
    db = sql.connect(user=sys.argv[1],
                     passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    states = cur.execute("SELECT cities.id, cities.name, states.name \
         FROM cities JOIN state USING ON \
            states.id = cities.state_id;").fetchall()

    for state in states:
        print(state)
