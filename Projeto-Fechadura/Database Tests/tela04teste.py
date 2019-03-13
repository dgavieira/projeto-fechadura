from tkinter import *
import sqlite3

conn = sqlite3.connect()
cursor = conn.cursor()

#Enabling schema
cursor.execute("""CREATE TABLE IF NOT EXISTS optima (
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                title TEXT NOT NULL)""")

class ScreenFour:
    def __init__(self,master):
        self.fontepadrao = ("Arial", "10")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()
        
        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()
        
        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack()
        
        self.quartoContainer = Frame(master)
        self.quartoContainer["pady"] = 20
        self.quartoContainer.pack()
        
        self.quintoContainer = Frame(master)
        self.quintoContainer["pady"] = 20
        self.quintoContainer.pack()
        
        self.sextoContainer = Frame(master)
        self.sextoContainer["pady"] = 20
        self.sextoContainer.pack()
        
        self.titulo = Label(self.primeiroContainer)
        self.titulo["text"] = "ENROLL"
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()
        
        self.firstnameLabel = Label(self.segundoContainer)
        self.firstnameLabel["text"] = "First Name"
        self.firstnameLabel["font"] = self.fontepadrao
        self.firstnameLabel.pack(side=LEFT)
        
        self.firstname = Entry(self.segundoContainer)
        self.firstname["width"] = 30
        self.firstname["font"] = self.fontepadrao
        self.firstname.pack(side=LEFT)
        
        self.lastnameLabel = Label(self.terceiroContainer)
        self.lastnameLabel["text"] = "Last Name"
        self.lastnameLabel["font"] = self.fontepadrao
        self.lastnameLabel.pack(side=LEFT)
        
        self.titleLabel = Label(self.quartoContainer)
        self.titleLabel["text"] = "Title"
        self.titleLabel["font"] = self.fontepadrao
        self.titleLabel.pack(side=LEFT)
        
        self.title = Entry(self.quartoContainer)
        self.title["width"] = 30
        self.title["font"] = self.fontepadrao
        self.title.pack(side=LEFT)
        
        self.botao = Button(self.quintoContainer)
        self.botao["text"] = "FINGERPRINT"
        self.botao["font"] = self.fontepadrao
        self.botao["command"] =
        self.botao["width"] = 30
        self.botao.pack()
        
        self.home == Button(self.sextoContainer)
        