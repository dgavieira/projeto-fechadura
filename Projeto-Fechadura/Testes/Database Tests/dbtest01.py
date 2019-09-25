import sqlite3
conn = sqlite3.connect('example.db')

#Allow to invoke sql commands
c = conn.cursor()

#Create Table
c.execute('''CREATE TABLE stocks
                (Name, Title)''')

#save the changes
conn.commit()

#close the Connection with remote server
conn.close