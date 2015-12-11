import sqlite3 as lite
import sys

con = lite.connect('test.db')

# With the with keyword, the Python interpreter automatically releases the resources. It also provides error handling
# Nice!!
with con:
    
    cur = con.cursor()    
    cur.execute('SELECT SQLITE_VERSION()')
    
    data = cur.fetchone()
    
    print("SQLite version: %s" % data) 