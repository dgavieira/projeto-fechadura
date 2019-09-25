#Test purpose file which writes the optima database schema
#create_optima_schema.py

import sqlite3

#enabling the connection
conn = sqlite3.connect('optima.db')

#setting the cursor
cursor = conn.cursor()

#creating the schema
cursor.execute("""
CREATE TABLE optima (
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    title TEXT NOT NULL,
    admin BOOLEAN NOT NULL
    );
    """)
print('schema suscefully created')
#disconnecting...
conn.close()