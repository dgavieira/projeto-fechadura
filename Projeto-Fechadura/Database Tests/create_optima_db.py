#Test purpose file which enables a database connection
#create_optima_db.py

#Imports the sqlite3 module to python
import sqlite3

conn = sqlite3.connect('optima.db')

conn.close()