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
            *
            FROM
                states
            WHERE
                name LIKE BINARY %(name)s
            ORDER BY
                states.id ASC
        """,
            {"name": sys.argv[4]},
        )

        rows = crs.fetchall()

    if rows is not None:
        for row in rows:
            print(row)
