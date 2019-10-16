import sqlite3

#database

def create_table():
	conn = sqlite3.connect('book_info.db')
	cur = conn.cursor()
	cur.execute("CREATE TABLE IF NOT EXISTS store (id INTEGER PRIMARY KEY,title TEXT, author TEXT, year INTEGER , isbn_no INTEGER)")
	conn.commit()
	conn.close()

create_table()

def insert(title, author, year, isbn_no):
	conn = sqlite3.connect("book_info.db")
	cur = conn.cursor()
	cur.execute("INSERT INTO store VALUES (NULL, ?,?,?,?)",(title, author, year, isbn_no))
	conn.commit()
	conn.close()

def delete(id):
	#del through id
	conn= sqlite3.connect("book_info.db")#creates data base/ links to existing db
	cur= conn.cursor()
	cur.execute("DELETE FROM store WHERE id = ?",(id,))
	conn.commit()
	conn.close()

def update(id,title,author,year,isbn_no):
    conn= sqlite3.connect("book_info.db")#creates data base/ links to existing db
    cur= conn.cursor()
    cur.execute("UPDATE store SET title =?, author=?,year=?,isbn_no = ? WHERE id=?",(title,author,year,isbn_no,id))
    conn.commit()
    conn.close()

def view():
    conn= sqlite3.connect("book_info.db")#creates data base/ links to existing db

    cur= conn.cursor()

    cur.execute("SELECT * FROM store")
    rows=cur.fetchall()
    conn.close()
    return rows #returned as a lis

def search(title="",author="",year="",isbn_no=""):
	conn= sqlite3.connect("book_info.db")
	cur = conn.cursor()
	cur.execute("SELECT * FROM store WHERE title =? OR author=? OR year=? OR isbn_no=?",(title,author,year,isbn_no))
	rows = cur.fetchall()
	conn.close()

	return rows

	


create_table()

# insert("Title Book", "Charles",1996,1234)

print(view())
print("\n\n\n\n")

# update("OLD", "Tom",1234,9888887,2)

print(view())
