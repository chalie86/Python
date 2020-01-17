import sqlite3
	
def connectdb(dbname):
    conn=sqlite3.connect(dbname)
    cur=conn.cursor()
    return (cur,conn)
 
def disconndb(conn):
    conn.commit()
    conn.close()
 
def create_table():
    dbcur, dbcon = connectdb("lite.db")
    dbcur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    disconndb(dbcon)
 
def insert(item,quantity,price):
    dbcur, dbcon = connectdb("lite.db")
    dbcur.execute("INSERT INTO store values(?,?,?)",(item,quantity,price))
    disconndb(dbcon)
	
def view():
    dbcur, dbcon = connectdb("lite.db")
    dbcur.execute("SELECT * FROM store")
    rows=dbcur.fetchall()
    disconndb(dbcon)
    return rows
	
	
def delete(item):
    dbcur, dbcon = connectdb("lite.db")
    dbcur.execute("DELETE FROM store where item=?",(item,))
    dbcur.commit()
    disconndb(dbcon)
def update(quantity,price):
    dbcur, dbcon = connectdb("lite.db")
    dbcur.execute("update,store set price = ? ,quantity= ? where item=?",(quantity,price))
    dbcur.commit()
    disconndb(dbcon)
create_table()
insert("coffe table",10,9)
    #delete("coffe table") 
    #update("coffe table")
print(view())
    #insert("coffe table",10,9)