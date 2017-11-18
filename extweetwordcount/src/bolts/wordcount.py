
from __future__ import absolute_import, print_function, unicode_literals

from collections import Counter
from streamparse.bolt import Bolt

import psycopg2

class WordCounter(Bolt):

    def initialize(self, conf, ctx):
        self.counts = Counter()

        #Connecting to tcount
        self.conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")



    def process(self, tup):
        word = tup.values[0]

        # Increment the local count
        self.counts[word] += 1
        self.emit([word, self.counts[word]])

        # Increment the word count in Postgres, using psycopg to interact
        # inserts counts into tweetword table
        try:
            #load the cursor
            cur = self.conn.cursor()

            if self.counts[word] == 1: ###if new word, insert into table
                cur.execute("INSERT INTO tweetwordcount (word, count) VALUES (%s, %s)", (word, self.counts[word]))
            else: ###if already in table, change count to new count
                cur.execute("UPDATE tweetwordcount SET count=%s WHERE word=%s",(self.counts[word], word))

            #commit the query
            self.conn.commit()
        except: #if you can't connect to the db
            self.log("missed db")

        # Log the count - just to see the topology running
        self.log('%s: %d' % (word, self.counts[word]))

