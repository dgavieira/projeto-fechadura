#Title: Biometric Lock User Interface
#Organization: Optima-UFAM
#Screen 2: Search Screen for ADM users
#Description:Starts the Fingerprint search loop only for ROOT ADM users
#Especs: Touchscreen LCD 3,5" 480x320
#Autor: Diego Vieira

from tkinter import *
import tela01alt, tela03alt

def teladois():
    class ScreenTwo:
        def __init__(self, master = None):
            '''self.screen = Frame(master)
            self.screen.pack()
        
            self.canvas = Canvas(self.screen, width=478, height=270, background="yellow")
            self.text = self.canvas.create_text( 239, 140,  text="MASTER FINGER", fill="black", font=("Helvetica", 30, "bold"))
            self.canvas.pack()'''
            
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
            self.quartoContainer["pady"] = 20
            self.quartoContainer.pack()
      
            self.titulo = Label(self.primeiroContainer, text="MASTER FINGER")
            self.titulo["font"] = ("Arial", "10", "bold")
            self.titulo.pack()
    
            self.nomeLabel = Label(self.segundoContainer,text="Nome", font=self.fontePadrao)
            self.nomeLabel.pack(side=LEFT)
      
            self.nome = Entry(self.segundoContainer)
            self.nome["width"] = 30
            self.nome["font"] = self.fontePadrao
            self.nome.pack(side=LEFT)
      
            self.senhaLabel = Label(self.terceiroContainer, text="Senha", font=self.fontePadrao)
            self.senhaLabel.pack(side=LEFT)
      
            self.senha = Entry(self.terceiroContainer)
            self.senha["width"] = 30
            self.senha["font"] = self.fontePadrao
            self.senha["show"] = "*"
            self.senha.pack(side=LEFT)
      
            self.autenticar = Button(self.quartoContainer)
            self.autenticar["text"] = "LOGIN"
            self.autenticar["font"] = ("Calibri", "8")
            self.autenticar["width"] = 12
            self.autenticar["command"] = self.verificaSenha
            self.autenticar.pack()
      
            self.mensagem = Label(self.quartoContainer, text="", font=self.fontePadrao)
            self.mensagem.pack()
      
        #Método verificar senha
        def verificaSenha(self):
            usuario = self.nome.get()
            senha = self.senha.get()

            if usuario == "cotta" and senha == "admin" or usuario == "leonardo" and senha == "admin":
                self.mensagem["text"] = "Access Granted"
                fechar()
                tela03alt.telatres()
            else:
                self.mensagem["text"] = "Access Denied"
                #fechar()
        
    def fechar():
        root.destroy()

    root = Tk()
    ScreenTwo(root)
    root.title("Admin Access")
    root.geometry('478x270')
    #root.overrideredirect(True)
    root.mainloop()
    
    