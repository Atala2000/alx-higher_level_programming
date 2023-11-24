#!/usr/bin/env python3
import MySQLdb
import sys

db = MySQLdb.connect(
    host="localhost",
    port=3306,
    user=sys.argv[1],
    passwd=sys.argv[2],
    db=sys.argv[3],
)

if __name__ == "__main__":
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    x = cur.fetchall()

    print(f"{type(x)}")

    db.close()
