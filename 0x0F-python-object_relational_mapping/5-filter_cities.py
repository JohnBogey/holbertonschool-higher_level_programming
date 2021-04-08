#!/usr/bin/python3
"""lists all cities by states from database hbtn_0e_4_usa"""

import MySQLdb
import re
from sys import argv

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost",
                           port=3306,
                           user=argv[1],
                           passwd=argv[2],
                           db=argv[3],
                           charset="utf8")
    cur = conn.cursor()
    argv[4] = re.sub("[^a-zA-Z0-9]", "", argv[4])
    cur.execute("SELECT cities.name\
                FROM cities\
                LEFT JOIN states\
                ON cities.state_id=states.id\
                WHERE states.name=\'{}\'\
                ORDER BY cities.id ASC".format(argv[4]))
    query_rows = cur.fetchall()
    for i in range(len(query_rows)):
        if i != 0:
            print(", ", end='')
        print("{}".format(query_rows[i][0]), end='')
    print()
    cur.close()
    conn.close()
