#!/usr/bin/python3
"""
Script that lists all states from database
Scripts safe from sql injection
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

    with db.cursor() as crs:
        crs.execute(
            """
        SELECT
            cities.id, cities.name
            FROM
                cities
            JOIN
                states
            ON
                cities.state_id = states.id
            WHERE
                states.name LIKE BINARY %(state_name)s
            ORDER BY
                cities.id ASC
        """,
            {"state_name": sys.argv[4]},
        )

        rows = crs.fetchall()

    if rows is not None:
        print(", ".join([row[1] for row in rows]))
