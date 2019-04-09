#Title: Biometric Lock User Interface
#Organization: Optima-UFAM
#Screen 4: Enroll Screen
#Description: Screen for enroll a brand new lab member // Allows admin level user to confirm data before upload to database
#INPUTS: Name; Title; Button for Fingerprint Loop
#Especs: Touchscreen LCD 3,5" 480x320
#Autor: Diego Vieira

from tkinter import *
import tela01alt, tela05alt
import sqlite3

conn = sqlite3.connect('optima.db')
cursor = conn.cursor()

#Enabling schema
cursor.execute("""CREATE TABLE IF NOT EXISTS optima (
            member_id integer PRIMARY KEY,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            title TEXT NOT NULL,
            UNIQUE (first_name, last_name))"""
            )
conn.commit()
conn.close()

def telaquatro():
    class ScreenFour:
        def __init__(self, master = None):
            self.fontePadrao = ("Arial","10")
            
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
            
            self.quintoContainer = Frame(master)
            self.quintoContainer["padx"] = 20
            self.quintoContainer.pack()
            
            self.sextoContainer = Frame(master)
            self.sextoContainer["padx"] = 40
            self.sextoContainer.pack()
            
            self.setimoContainer = Frame(master)
            self.setimoContainer["padx"] = 60
            self.setimoContainer.pack(fill = X, expand = YES)
            
            self.oitavoContainer = Frame(master)
            self.oitavoContainer["padx"] = 60
            self.oitavoContainer.pack()
            
            #elementos do primeiro container
            self.titulo = Label(self.primeiroContainer, text="ENROLL")
            self.titulo["font"] = ("Arial", "10", "bold")
            self.titulo.pack()
            
            #elementos do segundo container
            self.firstnameLabel = Label(self.segundoContainer,text="First Name", font=self.fontePadrao)
            self.firstnameLabel.pack(side=LEFT)
            
            #elementos do terceiro container
            self.lastnameLabel = Label(self.terceiroContainer, text="Last Name", font=self.fontePadrao)
            self.lastnameLabel.pack(side=LEFT)
      
            self.lastname = Entry(self.terceiroContainer)
            self.lastname["width"] = 30
            self.lastname["font"] = self.fontePadrao
            self.lastname.pack(side=LEFT)
            
            #elementos do quarto container
            self.titleLabel = Label(self.quartoContainer, text="Title \t", font=self.fontePadrao)
            self.titleLabel.pack(side=LEFT)
      
            self.title = Entry(self.quartoContainer)
            self.title["width"] = 30
            self.title["font"] = self.fontePadrao
            self.title.pack(side=LEFT)
            
            #elementos do quinto container
            self.var = IntVar()
            self.check = Checkbutton(self.quintoContainer)
            self.check["font"] = self.fontePadrao
            self.check["text"] = "Admin"
            self.check["variable"] = self.var
            self.check.pack(side = LEFT)
            
            #elementos do sexto container
            self.botaoLoad = Button(self.sextoContainer)
            self.botaoLoad["text"] = "LOAD"
            self.botaoLoad["font"] = self.fontePadrao
            #self.botaoLoad["command"] = self.showinput
            self.botaoLoad["width"] = 30
            self.botaoLoad.pack()
            
            #elementos do sétimo container
            self.msg = Message(self.setimoontainer)
            self.msg["text"] = "First Name: \n Last Name: \n Title: \n Admin:"
            self.msg["relief"] = SUNKEN
            self.msg.pack(fill = X, expand = YES)
            
            #elementos do oitavo container
            self.botaoMainMenu = Button(self.quartoContainer)
            self.botaoMainMenu["text"] = "MAIN MENU"
            self.botaoMainMenu["font"] = self.fontePadrao
            self.botaoMainMenu["command"] = returntohome
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
            