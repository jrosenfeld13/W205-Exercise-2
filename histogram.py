from __future__ import print_function
import sys

import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

conn = psycopg2.connect(database="tcount",user="postgres",host="localhost",port="5432")
cur = conn.cursor()

if len(sys.argv) != 2:
    print("Indicate an upper and lower bound.")
else:

    lower, upper = sys.argv[1].split(",")
    cur.execute("SELECT word, count FROM tweetwordcount WHERE count BETWEEN %s AND %s order by count desc",(lower, upper))
    records = cur.fetchall()
    for rec in records:
	print(rec[0]+":", rec[1])

    conn.commit()
    conn.close()
