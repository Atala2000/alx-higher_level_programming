#!/usr/bin/python3
"""
Script that lists all states from database
"""
import MySQLdb
import sys

if __name__ == "__main__":
    """
    Allows access to the database
    """
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
    )

    cur = db.cursor()
    cur.execute("SELECT * FROM states")
    x = cur.fetchall()

for results in x:
    print(f"{results}")
