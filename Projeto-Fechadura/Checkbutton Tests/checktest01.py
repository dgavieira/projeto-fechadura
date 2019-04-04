from tkinter import *
import sqlite3

conn = sqlite3.connect('optima.db')
cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS optima (
                member_id integer PRIMARY KEY,
                name TEXT NOT NULL UNIQUE,
                admin integer)"""
               )
conn.commit()
conn.close()

def telaquatro()
    class ScreenFour:
        def __init__(self, master = None)
            self.fontePadrao = ("Arial", "10")
            
            self.primeiroContainer = Frame(master)
            self.primeiroContainer["pady"] = 10
            self.primeiroContainer.pack()
            
            self.segundoContainer = Frame(master)
            self.segundoContainer["padx"] = 20
            self.segundoContainer.pack()
            
            self.terceiroContainer = Frame(master)
            self.terceiroContainer["padx"] = 20
            self.terceiroContainer.pack()
            
            #elemento do primeiro container
            self.titulo = Label(self.primeiroContainer)
            self.titulo["text"] = "ENROLL"
            self.titulo["font"] = ("Arial","10","bold")
            self.titulo.pack()
            
            #elemento do segundo container
            self.nameLabel = Label(self.segundoContainer)
            self.nameLabel["text"] = "Name"
            self.nameLabel["font"] = self.fontePadrao
            self.nameLabel.pack(side = LEFT)
            
            self.name = Entry(self.segundoContainer)
            self.name["width"] = 30
            self.name["font"] = self.fontePadrao
            self.name.pack(side = LEFT)
            
            #elemento do terceiro container
            self.var = IntVar()
            self.check = Checkbutton(self.terceiroContainer)
            self.check["font"] = self.fontePadrao
            self.check["text"] = "Administrador"
            self.check["variable"] = self.var
            self.check["onvalue"] = 1
            self.check ["offvalue"] = 0
            self.check.pack(side = LEFT)