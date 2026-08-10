#!/usr/bin/python3
"""Display states matching a name supplied by the user."""

import sys
import MySQLdb


def main():
    """Connect to MySQL and display the state matching the given name."""
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cursor = db.cursor()
    query = "SELECT id, name FROM states WHERE name = '{}' ORDER BY id ASC"
    query = query.format(sys.argv[4])
    cursor.execute(query)

    for state in cursor.fetchall():
        print(state)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
