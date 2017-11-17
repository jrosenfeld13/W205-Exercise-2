from __future__ import print_function
import sys

import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

conn = psycopg2.connect(database="tcount",user="postgres",host="localhost",port="5432")
cur = conn.cursor()

if len(sys.argv) != 2:
    cur.execute("SELECT word, count FROM tweetwordcount order by word")
    records = cur.fetchall()
    for rec in records:
        print(rec[0], rec[1])

else:
    word = sys.argv[1]
    cur.execute("SELECT word, count FROM tweetwordcount WHERE word LIKE %s",(word,))
    records = cur.fetchall()
    try:    
	print("Total number of occurrences of", records[0][0]+":", records[0][1]) 
    except:
	print("Please try another word.")
    conn.commit()
    conn.close()

