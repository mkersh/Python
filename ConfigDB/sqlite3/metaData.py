import sqlite3 as lite
import sys

def createCarsTable():
    con = lite.connect('test.db')

    # The with does a lot of magic, including committing the changes below
    with con:
        
        cur = con.cursor()
        cur.execute("DROP TABLE IF EXISTS Cars")  # IF EXISTS and IF NOT EXISTS clauses are useful
        cur.execute("DROP TABLE IF EXISTS Cars")   
        cur.execute("CREATE TABLE IF NOT EXISTS Cars(Id INT, Name TEXT, Price INT)")
        cur.execute("INSERT INTO Cars VALUES(1,'Audi',52642)")
        cur.execute("INSERT INTO Cars VALUES(2,'Mercedes',57127)")
        cur.execute("INSERT INTO Cars VALUES(3,'Skoda',9000)")
        cur.execute("INSERT INTO Cars VALUES(4,'Volvo',29000)")
        cur.execute("INSERT INTO Cars VALUES(5,'Bentley',350000)")
        cur.execute("INSERT INTO Cars VALUES(6,'Citroen',21000)")
        cur.execute("INSERT INTO Cars VALUES(7,'Hummer',41400)")
        cur.execute("INSERT INTO Cars VALUES(8,'Volkswagen',21600)")


def showMetaData():
    con = lite.connect('test.db')

    with con:
        
        cur = con.cursor()    
        
        cur.execute('PRAGMA table_info(Cars)')
        
        data = cur.fetchall()
        
        for d in data:
            print(d[0], d[1], d[2])

def printTableWithColumnNames():
    con = lite.connect('test.db')

    with con:
        
        cur = con.cursor()    
        cur.execute('SELECT * FROM Cars')
        
        col_names = [cn[0] for cn in cur.description]
        
        rows = cur.fetchall()
        
        print("%s %-10s %s" % (col_names[0], col_names[1], col_names[2]))

        for row in rows:    
            print("%2s %-10s %s" % row)

def main():
    createCarsTable()
    showMetaData()
    printTableWithColumnNames()

if __name__ == '__main__':
    main()