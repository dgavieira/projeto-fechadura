#optimadb.py
import sqlite3

#conecting
conn = sqlite3.connect('optima.db')
#setting the cursor

cursor = conn.cursor()

#creating the table
conn.execute