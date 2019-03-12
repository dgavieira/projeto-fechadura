#Test purpose file which inserts the first data samples on optima schema database
#create_optima_data.py

import sqlite3

conn = sqlite3.connect('optima.db')
cursor = conn.cursor()

#inserting data into the schema
cursor.execute("""
INSERT INTO optima (first_name, last_name, title, admin)
VALUES ('Eduardo', 'Cotta', 'Coordenador', '1')
""")

cursor.execute("""
INSERT INTO optima (first_name, last_name, title, admin)
VALUES ('Leonardo', 'Arcanjo', 'Técnico', '1')
""")

conn.commit()

print('Dados inseridos com sucesso.')

conn.close()