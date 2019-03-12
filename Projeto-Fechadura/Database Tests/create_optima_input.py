#Test purpose file which inserts the first data samples on optima schema database using input
#create_optima_input.py

import sqlite3

conn = sqlite3.connect('optima.db')
cursor = conn.cursor()

#asking for user input
p_first_name = input('Insert First Name: ')
p_last_name = input('Insert Last Name: ')
p_title = input('Insert Title: ')
pp_admin = input('Concede new member ADMIN access level? (y/n)')

if pp_admin == 'y':
    p_admin = 1
else:
    p_admin = 0
    
#insert data into the schema
    
cursor.execute("""
INSERT INTO optima (first_name, last_name, title, admin)
VALUES (?, ?, ?, ?)
""", (p_first_name, p_last_name, p_title, p_admin))

conn.commit()

print('Dados inseridos com sucesso.')
conn.close()