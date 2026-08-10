#!/usr/bin/python3
"""List states whose names start with an uppercase N."""

import sys
import MySQLdb


def main():
    """Connect to MySQL and display states beginning with uppercase N."""
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cursor = db.cursor()
    cursor.execute(
        "SELECT id, name FROM states "
        "WHERE name LIKE 'N%' ORDER BY id ASC"
    )

    for state in cursor.fetchall():
        print(state)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
