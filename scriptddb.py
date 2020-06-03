import psycopg2

def create_table():
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store(item TEXT,quantity INTEGER,price REAL)")
    cur.execute("INSERT INTO store values ('Wine Glass',8,10.5)")
    conn.commit()
    conn.close()
def insert(item,quantity,price):
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO store values(?,?,?)",(item,quantity,price))
    conn.commit()
    conn.close()
    insert("water bottle",10,9)
    # def view():
    # conn=sqlite3.connect("lite.db")
    # cur=conn.cursor()
    # cur.execute("SELECT * FROM store")
    # rows=cur.fetcha11()
    # conn.close()
    # return rows
    # print((view))
def view():
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM store")
    rows=cur.fetchall()
    conn.close()
    return
def delete(item):
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM store where item=?",(item,))
    conn.commit()
    conn.close()
def update(quantity,price):
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("update,store set price = ? ,quantity= ? where item=?",(quantity,price))
    conn.commit()
    conn.close
create_table()
    #delete("coffe table")
    #update("coffe table")
print(view())
    #inser