from tkinter import *
import sqlite3

conn = sqlite3.connect('optima.db')
cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS optima (
                member_id integer PRIMARY KEY,
                first_name TEXT NOT NULL,
                last_name NOT NULL,
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
            
            self.admContainer = Frame(master)
            self.admContainer["padx"] = 20
            self.admContainer.pack()
            
            self.quintoContainer = Frame(master)
            self.quintoContainer["padx"] = 20
            self.quintoContainer.pack()
            
            self.sextoContainer = Frame(master)
            self.sextoContainer["padx"] = 40
            self.sextoContainer.pack(fill = X, expand = YES)
            
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
            self.titleLabel = Label(self.quartoContainer, text="Title \t", font=self.fontePadrao)
            self.titleLabel.pack(side=LEFT)
      
            self.title = Entry(self.quartoContainer)
            self.title["width"] = 30
            self.title["font"] = self.fontePadrao
            self.title.pack(side=LEFT)
            
            #elementos do adm container
            self.var = IntVar()
            self.check = Checkbutton(self.admContainer)
            self.check["font"] = self.fontePadrao
            self.check["text"] = "Administrador"
            self.check["variable"] = self.var
            self.check["onvalue"] = 1
            self.check["offvalue"] = 0
            self.check["state"] = NORMAL
            self.check.pack()
            
            #elementos do quinto container
            self.botao1 = Button(self.quintoContainer)
            self.botao1["text"] = "LOAD"
            self.botao1["font"] = self.fontePadrao
            self.botao1["command"] = self.showinput
            self.botao1["width"] = 30
            self.botao1.pack()
            
            #elementos do sexto container
            self.msg = Message(self.sextoContainer)
            self.msg["text"] = "First Name: \n Last Name: \n Title: "
            self.msg["relief"] = SUNKEN
            self.msg.pack(fill = X, expand = YES)
            
            #elementos do sétimo container
            self.botao2 = Button(self.setimoContainer)
            self.botao2["text"] = "MAIN MENU"
            self.botao2["font"] = self.fontePadrao
            self.botao2["command"] = returntohome
            self.botao2["width"] = 10
            self.botao2.pack(side = LEFT)
            
            self.botao3 = Button(self.setimoContainer)
            self.botao3["text"] = "CANCEL"
            self.botao3["font"] = self.fontePadrao
            self.botao3["command"] = self.eraseinput
            self.botao3["width"] = 10
            self.botao3.pack(side = LEFT)
            
            self.botao = Button(self.setimoContainer)
            self.botao["text"] = "FINGERPRINT"
            self.botao["font"] = self.fontePadrao
            self.botao["command"] = self.enabledb
            self.botao["width"] = 10
            self.botao.pack(side = LEFT)

        def showinput(self):
            p_first_name = self.firstname.get()
            p_last_name = self.lastname.get()
            p_title = self.title.get()
            
            if self.msg["text"] == "First Name: \n Last Name: \n Title: ":
                self.msg["text"] = "First Name: \t" + p_first_name + "\n Last Name:\t" + p_last_name + "\n Title: \t" + p_title
                self.botao1["state"] = DISABLED
            else:
                self.msg["text"] = "First Name: \n Last Name: \n Title: "
                
        def eraseinput(self):
            p_first_name = self.firstname.get()
            p_last_name = self.lastname.get()
            p_title = self.title.get()
            p_admin = self.var
            
            if self.msg["text"] == "First Name: \t" + p_first_name + "\n Last Name:\t" + p_last_name + "\n Title: \t" + p_title:
                self.msg["text"] = "First Name: \n Last Name: \n Title: "
                self.botao1["state"] = NORMAL
                self.firstname.delete(0, END)
                self.lastname.delete(0, END)
                self.title.delete(0, END)
                del(p_first_name)
                del(p_last_name)
                del(p_title)
            else:
                self.msg["text"] = "First Name: \t" + p_first_name + "\n Last Name:\t" + p_last_name + "\n Title: \t" + p_title
                
        def enabledb(self):
            conn = sqlite3.connect('optima.db')
            try:
                cursor = conn.cursor()
                
                p_first_name = self.firstname.get()
                p_last_name = self.lastname.get()
                p_title = self.title.get()
                p_admin = self.var
                
                cursor.execute("""
                    INSERT INTO optima (first_name, last_name, title, admin)
                    VALUES (?, ?, ?, ?)
                    """, (p_first_name, p_last_name, p_title, p_admin))
                conn.commit()
                print('Dados inseridos com sucesso.')
                conn.close()
                fechar()
                tela05alt.telacinco()
                
            except:
                if self.msg["text"] == "First Name: \n Last Name: \n Title: ":
                    self.msg["text"] = "DUPLICATA! O usuário inserido já está cadastrado no banco de dados! \n Favor inserir novos dados."
                    self.botao1["state"] = DISABLED
                    self.botao["state"] = DISABLED
                    self.firstname.delete(0, END)
                    self.lastname.delete(0, END)
                    self.title.delete(0, END)
                    del(p_first_name)
                    del(p_last_name)
                    del(p_title)
                    del(p_admin)
            else:
                self.msg["text"] = "First Name: \n Last Name: \n Title: "
            
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