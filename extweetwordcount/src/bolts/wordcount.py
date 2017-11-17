
from __future__ import absolute_import, print_function, unicode_literals

from collections import Counter
from streamparse.bolt import Bolt

import psycopg2

#connect to database 
conn = psycopg2.connect(database="tcount",user="postgres",host="localhost",port="5432")

class WordCounter(Bolt):

    def initialize(self, conf, ctx):
        self.counts = Counter()

    def process(self, tup):
        word = tup.values[0]


        # Increment the local count
        self.counts[word] += 1
        self.emit([word, self.counts[word]])

        # Write codes to increment the word count in Postgres
        # Use psycopg to interact with Postgres
        # Database name: Tcount
        # Table name: Tweetwordcount
        # you need to create both the database and the table in advance.
        # create cursor and update tweetwordcount table with our increment words

        try:
            cur = conn.cursor()

            if self.counts[word] == 1: ###if new word, insert
                cur.execute("INSERT INTO tweetwordcount (word, count) VALUES (%s, %s)", (word, self.counts[word]))
            else: ###if already in table
                cur.execute("UPDATE tweetwordcount SET count=%s WHERE word=%s",(self.counts[word], word))
                
            conn.commit()
            conn.close()
	except:
            self.log("missed db")
        # Log the count - just to see the topology running
        self.log('%s: %d' % (word, self.counts[word]))

