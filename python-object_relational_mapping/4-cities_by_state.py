#!/usr/bin/python3
"""List cities together with their corresponding state names."""

import sys
import MySQLdb


def main():
    """Connect to MySQL and display all cities ordered by city ID."""
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cursor = db.cursor()
    query = (
        "SELECT cities.id, cities.name, states.name "
        "FROM cities INNER JOIN states "
        "ON cities.state_id = states.id "
        "ORDER BY cities.id ASC"
    )
    cursor.execute(query)

    for city in cursor.fetchall():
        print(city)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
