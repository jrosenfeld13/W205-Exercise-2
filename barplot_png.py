import sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

conn = psycopg2.connect(database="tcount",user="postgres",host="localhost",port="5432")
cur = conn.cursor()

cur.execute("SELECT word, count FROM tweetwordcount order by count desc limit 20")
records = cur.fetchall()
conn.commit()
conn.close()

words = [rec[0] for rec in records]
counts = [rec[1] for rec in records]

plt.bar(words,counts)
plt.ylabel('word counts')
plt.xlabel('words')
plt.title('Top 20 words')
plt.savefig('Plot.png')
