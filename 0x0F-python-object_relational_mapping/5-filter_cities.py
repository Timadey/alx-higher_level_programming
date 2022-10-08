#!/usr/bin/python3
"""
 a script that takes in the name of a state as an argument
 and lists all cities of that state,
 using the database hbtn_0e_4_usa
"""
import MySQLdb as sql
import sys

if __name__ == '__main__':
    db = sql.connect(user=sys.argv[1],
                     passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name \
         FROM cities JOIN state ON states.id = cities.state_id \
         WHERE state.name = %s;", (sys.argv[4],))
    states = cur.fetchall()

    for state in states:
        print(state)
