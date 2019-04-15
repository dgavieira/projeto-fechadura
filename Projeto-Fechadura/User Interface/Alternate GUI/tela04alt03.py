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
            admin integer,
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
            self.titulo = Label(self.primeiroContainer)
            self.titulo["text"] = "ENROLL"
            self.titulo["font"] = ("Arial", "10", "bold")
            self.titulo.pack()
            
            #elementos do segundo container
            self.firstnameLabel = Label(self.segundoContainer)
            self.firstnameLabel["text"] = "First Name"
            self.firstnameLabel["font"] = self.fontePadrao
            self.firstnameLabel.pack(side=LEFT)
            
            self.firstname = Entry(self.segundoContainer)
            self.firstname["width"] = 30
            self.firstname["font"] = self.fontePadrao
            self.firstname.pack(side=LEFT)
            
            #elementos do terceiro container
            self.lastnameLabel = Label(self.terceiroContainer)
            self.lastnameLabel["text"] = "Last Name"
            self.lastnameLabel["font"] = self.fontePadrao
            self.lastnameLabel.pack(side=LEFT)
      
            self.lastname = Entry(self.terceiroContainer)
            self.lastname["width"] = 30
            self.lastname["font"] = self.fontePadrao
            self.lastname.pack(side=LEFT)
            
            #elementos do quarto container
            self.titleLabel = Label(self.quartoContainer)
            self.titleLabel["text"] = "Title\t"
            self.titleLabel["font"] = self.fontePadrao
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
            self.botaoLoad["command"] = self.showinput
            self.botaoLoad["width"] = 30
            self.botaoLoad.pack()
            
            #elementos do sétimo container
            self.msg = Message(self.setimoContainer)
            self.msg["text"] = "First Name: \n Last Name: \n Title: \n Admin:"
            self.msg["relief"] = SUNKEN
            self.msg.pack(fill = X, expand = YES)
            
            #elementos do oitavo container
            self.botaoMainMenu = Button(self.oitavoContainer)
            self.botaoMainMenu["text"] = "MAIN MENU"
            self.botaoMainMenu["font"] = self.fontePadrao
            self.botaoMainMenu["command"] = returntohome
            self.botaoMainMenu["width"] = 10
            self.botaoMainMenu.pack(side = LEFT)
            
            self.botaoCancel = Button(self.oitavoContainer)
            self.botaoCancel["text"] = "CANCEL"
            self.botaoCancel["font"] = self.fontePadrao
            self.botaoCancel["command"] = self.eraseinput
            self.botaoCancel["width"] = 10
            self.botaoCancel.pack(side = LEFT)
            
            self.botaoFingerprint = Button(self.oitavoContainer)
            self.botaoFingerprint["text"] = "FINGERPRINT"
            self.botaoFingerprint["font"] = self.fontePadrao
            self.botaoFingerprint["command"] = self.enabledb
            self.botaoFingerprint["width"] = 10
            self.botaoFingerprint.pack(side = LEFT)
            
        def showinput(self):
            p_first_name = self.firstname.get()
            p_last_name = self.lastname.get()
            p_title = self.title.get()
            p_admin = self.var.get()
            
            if self.msg["text"] == "First Name: \n Last Name: \n Title: \n Admin:":
                if p_admin == 1:
                    self.msg["text"] = "First Name: " + p_first_name + "\n Last Name: " + p_last_name + "\n Title: " + p_title + "\n Admin: YES"
                    self.botaoLoad["state"] = DISABLED
                if p_admin == 0:
                    self.msg["text"] = "First Name: " + p_first_name + "\n Last Name: " + p_last_name + "\n Title: " + p_title + "\n Admin: NO"
                    self.botaoLoad["state"] = DISABLED
            else:
                self.msg["text"] = "First Name: \n Last Name: \n Title: \n Admin:"
                
        def eraseinput(self):
            p_first_name = self.firstname.get()
            p_last_name = self.lastname.get()
            p_title = self.title.get()
            p_admin = self.var.get()
            
            if self.msg["text"] == "First Name: " + p_first_name + "\n Last Name: " + p_last_name + "\n Title: " + p_title + "\n Admin: YES":
                self.msg["text"] = "First Name: \n Last Name: \n Title: \n Admin:"
                self.botaoLoad["state"] = NORMAL
                self.check.toggle()
                self.firstname.delete(0,END)
                self.lastname.delete(0,END)
                self.title.delete(0,END)
                del(p_first_name)
                del(p_last_name)
                del(p_title)
                del(p_admin)
                self.botaoFingerprint["state"] = NORMAL
            elif self.msg["text"] == "First Name: \t" + p_first_name + "\n Last Name: \t" + p_last_name + "\n Title: \t" + p_title + "\n Admin: NO":
                self.msg["text"] = "First Name: \n Last Name: \n Title: \n Admin:"
                self.botaoLoad["state"] = NORMAL
                self.firstname.delete(0,END)
                self.lastname.delete(0,END)
                self.title.delete(0,END)
                del(p_first_name)
                del(p_last_name)
                del(p_title)
                del(p_admin)
                self.botaoFingerprint["state"] = NORMAL
            else:
                pass
        
        def enabledb(self):
            p_first_name = self.firstname.get()
            p_last_name = self.lastname.get()
            p_title = self.title.get()
            p_admin = self.var.get()
            try:
                conn = sqlite3.connect('optima.db')
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT INTO optima (first_name, last_name, title, admin)
                    VALUES (?, ?, ?, ?)
                    """, (p_first_name, p_last_name, p_title, p_admin)
                    )
                conn.commit()
                print("Dados inseridos com sucesso.")
                conn.close()
                fechar()
                tela05alt.telacinco()   
            except:
                if self.msg["text"] == "First Name: " + p_first_name + "\n Last Name: " + p_last_name + "\n Title: " + p_title + "\n Admin: YES":
                    self.msg["text"] = "O Nome inserido já está cadastrado. Insira novos dados."
                    self.botaoLoad["state"] = DISABLED
                    self.botaoFingerprint["state"] = DISABLED
                    self.check.toggle()
                    self.firstname.delete(0,END)
                    self.lastname.delete(0,END)
                    self.title.delete(0,END)
                    del(p_first_name)
                    del(p_last_name)
                    del(p_title)
                    del(p_admin)
                    self.botaoFingerprint["state"] = NORMAL
                    self.botaoLoad["state"] = NORMAL
                elif self.msg["text"] == "First Name: " + p_first_name + "\n Last Name: " + p_last_name + "\n Title: " + p_title + "\n Admin: NO":
                    self.msg["text"] = "O Nome inserido já está cadastrado. Insira novos dados."
                    self.botaoLoad["state"] = DISABLED
                    self.botaoFingerprint["state"] = DISABLED
                    self.firstname.delete(0,END)
                    self.lastname.delete(0,END)
                    self.title.delete(0,END)
                    del(p_first_name)
                    del(p_last_name)
                    del(p_title)
                    del(p_admin)
                    self.botaoFingerprint["state"] = NORMAL
                    self.botaoLoad["state"] = NORMAL
                else:
                    self.msg["text"] = "First Name: \n Last Name: \n Title: \n Admin:"
                    
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
            