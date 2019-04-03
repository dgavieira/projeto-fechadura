from tkinter import *
import sqlite3

conn = sqlite3.connect('optima.db')
cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS optima (
                member_id integer PRIMARY KEY,
                name TEXT NOT NULL,
                admin integer)"""
               )
conn.commit()
conn.close()

def telaquatro()
    class ScreenFour:
        def __init__(self, master = None)