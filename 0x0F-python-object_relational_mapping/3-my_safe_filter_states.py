#!/usr/bin/python3
"""lists all states from database hbtn_0e_0_usa filtered safely"""

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
    cur.execute("SELECT * FROM states\
                WHERE name=\"{}\" ORDER BY id ASC".format(argv[4]))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
