#Title: Biometric Lock User Interface
#Organization: Optima-UFAM
#Screen 4: Enroll Screen
#Description: Screen for enroll a brand new lab member
#INPUTS: Name; Title; Button for Fingerprint Loop
#Especs: Touchscreen LCD 3,5" 480x320
#Autor: Diego Vieira

from tkinter import *
import tela05alt

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
            self.quartoContainer["pady"] = 20
            self.quartoContainer.pack()
      
            self.titulo = Label(self.primeiroContainer, text="ENROLL")
            self.titulo["font"] = ("Arial", "10", "bold")
            self.titulo.pack()
      
            self.nomeLabel = Label(self.segundoContainer,text="Name", font=self.fontePadrao)
            self.nomeLabel.pack(side=LEFT)
      
            self.nome = Entry(self.segundoContainer)
            self.nome["width"] = 30
            self.nome["font"] = self.fontePadrao
            self.nome.pack(side=LEFT)
      
            self.titleLabel = Label(self.terceiroContainer, text="Title", font=self.fontePadrao)
            self.titleLabel.pack(side=LEFT)
      
            self.title = Entry(self.terceiroContainer)
            self.title["width"] = 30
            self.title["font"] = self.fontePadrao
            self.title.pack(side=LEFT)
      
            self.botao = Button(self.quartoContainer)
            self.botao["text"] = "FINGERPRINT"
            self.botao["font"] = ("Calibri", "24")
            self.botao["command"] = tela05alt.telacinco
            self.botao["width"] = 30
            self.botao.pack()
            
    root = Tk()
    ScreenFour(root)
    root.title("Enroll Screen")
    root.geometry('478x270')
    #root.overrideredirect(True)
    root.mainloop()
            
