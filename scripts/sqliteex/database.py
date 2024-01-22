import sqlite3

conn = sqlite3.connect('customer.db')

c = conn.cursor()

c.execute("INSERT INTO customers VALUES('Tim', 'Sawyer', 'timsawyer@gmail.com')")


print("Done!")
conn.commit()

conn.close()