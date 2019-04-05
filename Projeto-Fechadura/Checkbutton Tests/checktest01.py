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
            
            self.quartoContainer = Frame(master)
            self.quartoContainer["padx"] = 20
            self.quartoContainer.pack()
            
            self.quintoContainer = Frame(master)
            self.quintoContainer["padx"] = 20
            self.quintoContainer.pack()
            
            self.sextoContainer = Frame(master)
            self.sextoContainer["padx"] = 20
            self.sextoContainer.pack()
            
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
            self.check["text"] = "Admin"
            self.check["variable"] = self.var
            self.check["onvalue"] = 1
            self.check ["offvalue"] = 0
            self.check.pack(side = LEFT)
            
            #elemento do quarto container
            self.botaoLoad = Button(self.quartoContainer)
            self.botaoLoad["text"] = "LOAD"
            self.botaoLoad["font"] = self.fontePadrao
            self.botaoLoad["command"] = self.showinput
            self.botaoLoad["width"] = 30
            self.botaoLoad.pack()
            
            #elemento do quinto container
            self.msg = Message(self.quintoContainer)
            self.msg["text"] = "Name: \n Admin:"
            self.msg["relief"] = SUNKEN
            self.msg.pack(fill = X, expand = YES)

            #elemento do sexto container
            self.botaoMainMenu = Button(self.sextoContainer)
            self.botaoMainMenu["text"] = "MAIN MENU"
            self.botaoMainMenu["font"] = self.fontePadrao
            #self.botaoMainMenu["command"] ==
            self.botaoMainMenu["width"] = 10
            self.botao.pack(side = LEFT)
            
            self.botaoCancel = Button(self.sextoContainer)
            self.botaoCancel["text"] = "CANCEL"
            self.botaoCancel["font"] = self.fontePadrao
            self.botaoCancel["command"] = self.eraseinput
            self.botaoCancel["width"] = 10
            self.botao.pack(side = LEFT)
            
            self.botaoFingerprint = Button(self.sextoContainer)
            self.botaoFingerprint["text"] = "FINGERPRINT"
            self.botaoFingerprint["font"] = self.fontePadrao
            self.botaoFingeprint["command"] = self.enabledb
            self.botaoFingerprint["width"] = 10
            self.botao.pack(side = LEFT)
            
        def showinput(self):
            p_name = self.name.get()
            p_admin = self.var
            
            if self.msg["text"] == "Name: \n Admin:" and p_admin == 1:
                self.msg["text"] = "Name: " + p_name + "\n Admin: YES"
                self.botaoFingerprint["state"] = DISABLED
            elif self.msg["text"] == "Name: \n Admin:" and p_admin == 0:
                self.msg["text"] = "Name: " + p_name + "\n Aadmin: NO"
                self.botaoFingerprint["state"] = DISABLED
            else:
                self.msg["text"] = "Name: \n Admin:"
                
        def eraseinput(self);
            p_name = self.name.get()
            p_admin = self.var
            
            if self.msg["text"] == "Name: " + p_name + "\n Admin: YES" or self.msg["text"] == "Name: " + p_name + "\n Admin: NO":
                self.msg["text"] = "Name: \n Admin:"
                self.botaoLoad["state"] = NORMAL
                self.name.delete(0,END)
                del(p_name)
                del(p_admin)
            else:
                pass
            
        def enabledb(self):
            p_name = self.name.get()
            p_admin = self.var
            
            try:
                conn = sqlite3.connect('optima.db')
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT INTO optima (name, admin)
                    VALUES (?, ?)
                    """, (p_name, p_admin))
                conn.commit()
                print('Dados inseridos com sucesso')
                conn.close()
                
                print('Abriu tela de Fingerprint')
            except:
                