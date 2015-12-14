import sqlite3 as lite
import sys
import pdb
F
def createCarsTable():
    con = lite.connect('test.db')
    #pdb.set_trace() implicitly starts the debugger
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

def readCarsTable():
    con = lite.connect('test.db')

    with con:    
        
        cur = con.cursor()    
        cur.execute("SELECT * FROM Cars")

        rows = cur.fetchall()

        for row in rows:
            print(row)

def readCarsTableWithRowCursor():
    con = lite.connect('test.db')    
    
    with con:
        
        # This next line specifies a different type of cursor
        # This returns rows as dictionary objects
        con.row_factory = lite.Row
           
        cur = con.cursor() 
        cur.execute("SELECT * FROM Cars")

        rows = cur.fetchall()

        for row in rows:
            print("%s %s %s" % (row["Id"], row["Name"], row["Price"]))


def main():
    createCarsTable()
    #readCarsTable()
    readCarsTableWithRowCursor()

if __name__ == '__main__':
    main()