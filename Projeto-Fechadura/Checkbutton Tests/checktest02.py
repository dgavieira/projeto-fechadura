from tkinter import *
import sqlite3

conn = sqlite3.connect('optima2.db')
cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS optima2(
                member_id integer PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE,
                admin integer)"""
    )
conn.commit()
conn.close()

def telaquatro():
    class ScreenFour:
        def __init__(self, master = None):
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
            
            self.quartoContainer = Frame(master)
            self.quartoContainer["padx"] = 20
            self.quartoContainer.pack()
            
            #elementos do primeiro container
            self.titulo = Label(self.primeiroContainer)
            self.titulo["text"] = "ENROLL"
            self.titulo["font"] = ("Arial","10","bold")
            self.titulo.pack(side = LEFT)
            
            #elementos do segundo container
            self.nameLabel = Label(self.segundoContainer)
            self.nameLabel["text"] = "Name"
            self.nameLabel["font"] = self.fontePadrao
            self.nameLabel.pack(side = LEFT)
            
            self.name = Entry(self.segundoContainer)
            self.name["width"] = 30
            self.name["font"] = self.fontePadrao
            self.name.pack()
            
            #elementos do terceiro container
            self.var = IntVar()
            self.check = Checkbutton(self.terceiroContainer)
            self.check["font"] = self.fontePadrao
            self.check["text"] = "Admin"
            self.check["variable"] = self.var
            self.check.pack(side = LEFT)
            
            #elementos do quarto container
            elf.botaoMainMenu = Button(self.quartoContainer)
            self.botaoMainMenu["text"] = "MAIN MENU"
            self.botaoMainMenu["font"] = self.fontePadrao
            #self.botaoMainMenu["command"] = returntohome
            self.botaoMainMenu["width"] = 10
            self.botaoMainMenu.pack(side = LEFT)
            
            self.botaoCancel = Button(self.quartoContainer)
            self.botaoCancel["text"] = "CANCEL"
            self.botaoCancel["font"] = self.fontePadrao
            #self.botaoCancel["command"] = self.eraseinput
            self.botaoCancel["width"] = 10
            self.botaoCancel.pack(side = LEFT)
            
            self.botaoFingerprint = Button(self.quartoContainer)
            self.botaoFingerprint["text"] = "FINGERPRINT"
            self.botaoFingerprint["font"] = self.fontePadrao
            self.botaoFingerprint["command"] = self.enabledb
            self.botaoFingerprint["width"] = 10
            self.botaoFingerprint.pack(side = LEFT)
            
        def enabledb(self):
            p_name = self.name.get()
            p_admin = self.var
            
            try:
                conn
            