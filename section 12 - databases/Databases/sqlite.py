import sqlite3

def create_table():
  cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
  conn.commit()

def insert_row(item, quantity, price):
  cur.execute("INSERT INTO store VALUES (?, ?, ?)", (item, quantity, price))
  conn.commit()

def get_rows():
  cur.execute("SELECT * FROM store")
  rows=cur.fetchall()
  return rows

def delete_row(item):
  cur.execute("DELETE FROM store WHERE item=?", (item,))
  conn.commit()

def update_row(quantity, price, item):
  cur.execute("UPDATE store SET quantity=?, price=? WHERE item=?", (quantity, price, item))
  conn.commit()

conn = sqlite3.connect("lite.db")
cur = conn.cursor()

create_table()
#cur.execute("INSERT INTO store VALUES ('Wine Glass', 8, 10.5)")
insert_row('Wine Glass', 8, 10.5)
insert_row('Water Glass', 7, 5.0)
insert_row('Coffee cup', 18, 2.5)

rows = get_rows()
print(rows)

delete_row('Coffee cup')
update_row(3, 5.0, 'Water Glass')

print(get_rows())

conn.close()
