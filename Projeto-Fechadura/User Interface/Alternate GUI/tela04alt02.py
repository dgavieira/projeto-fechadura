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
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            title TEXT NOT NULL)""")

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
            self.sextoContainer["padx"] = 20
            self.sextoContainer.pack()
            
            self.setimoContainer = Frame(master)
            self.setimoContainer["padx"] = 60
            self.setimoContainer.pack()
            
            #elementos do primeiro container
            self.titulo = Label(self.primeiroContainer, text="ENROLL")
            self.titulo["font"] = ("Arial", "10", "bold")
            self.titulo.pack()
            
            #elementos do segundo container
            self.firstnameLabel = Label(self.segundoContainer,text="First Name", font=self.fontePadrao)
            self.firstnameLabel.pack(side=LEFT)
      
            self.firstname = Entry(self.segundoContainer)
            self.firstname["width"] = 30
            self.firstname["font"] = self.fontePadrao
            self.firstname.pack(side=LEFT)
            
            #elementos do terceiro container
            self.lastnameLabel = Label(self.terceiroContainer, text="Last Name", font=self.fontePadrao)
            self.lastnameLabel.pack(side=LEFT)
      
            self.lastname = Entry(self.terceiroContainer)
            self.lastname["width"] = 30
            self.lastname["font"] = self.fontePadrao
            self.lastname.pack(side=LEFT)
            
            #elementos do quarto container
            self.titleLabel = Label(self.quartoContainer, text="Title", font=self.fontePadrao)
            self.titleLabel.pack(side=LEFT)
      
            self.title = Entry(self.quartoContainer)
            self.title["width"] = 30
            self.title["font"] = self.fontePadrao
            self.title.pack(side=LEFT)
            
            #elementos do quinto container
            self.botao = Button(self.quintoContainer)
            self.botao["text"] = "LOAD"
            self.botao["font"] = self.fontePadrao
            #self.botao["command"] = 
            self.botao["width"] = 30
            self.botao.pack()
            
            #elementos do sexto container
            self.msg = Message(self.sextoContainer)
            self.msg["text"] = "First Name: \n Last Name: \n Title: "
            self.msg["relief"] = GROOVE
            self.msg["width"] = 100
            self.msg.pack()
            
            #elementos do sétimo container
            self.botao = Button(self.setimoContainer)
            self.botao["text"] = "MAIN MENU"
            self.botao["font"] = self.fontePadrao
            self.botao["command"] = returntohome
            self.botao["width"] = 10
            self.botao.pack(side = LEFT)
            
            self.botao = Button(self.setimoContainer)
            self.botao["text"] = "CANCEL"
            self.botao["font"] = self.fontePadrao
            #self.botao["command"] = 
            self.botao["width"] = 10
            self.botao.pack()
            
            self.botao = Button(self.setimoContainer)
            self.botao["text"] = "FINGERPRINT"
            self.botao["font"] = self.fontePadrao
            self.botao["command"] = self.enabledb
            self.botao["width"] = 10
            self.botao.pack(side = RIGHT)
            
        def getter(self):
            p_first_name = self.firstname.get()
            p_last_name = self.lastname.get()
            p_title = self.title.get()
                
        def enabledb(self):
            cursor.execute("""
                INSERT INTO optima (first_name, last_name, title)
                VALUES (?, ?, ?)
                """, (p_first_name, p_last_name, p_title))
            conn.commit()
            print('Dados inseridos com sucesso.')
            conn.close()
            
            fechar()
            tela05alt.telacinco()
            
    def returntohome():
        fechar()
        tela01alt.telaum()
        
    def fechar():
        root.destroy()               
            
    root = Tk()
    ScreenFour(root)
    root.title("Enroll Screen")
    root.geometry('478x270')
    #root.overrideredirect(True)
    root.mainloop()