from send_tweet import *
import sqlite3

db = photoDB('photoDB.db')
collection = 'p16022coll175'

for i in range(0, 21899):
    db.cur.execute('''INSERT INTO photos (id, collection, record)
        VALUES (?, ?, ?)''', [collection+'_'+str(i), collection, i])

db.con.commit()
