#Title: Biometric Lock User Interface
#Organization: Optima-UFAM
#Screen 4: Enroll Screen
#Description: Screen for enroll a brand new lab member
#INPUTS: Name; Title; Button for Fingerprint Loop
#Especs: Touchscreen LCD 3,5" 480x320
#Autor: Diego Vieira

from tkinter import *
import tela01alt, tela05alt

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
            
            self.quintoContainer = Frame(master)
            self.quintoContainer["pady"] = 20
            self.quintoContainer.pack()
            
            self.sextoContainer = Frame(master)
            self.sextoContainer["pady"] = 20
            self.sextoContainer.pack()
      
            self.titulo = Label(self.primeiroContainer, text="ENROLL")
            self.titulo["font"] = ("Arial", "10", "bold")
            self.titulo.pack()
      
            self.firstnameLabel = Label(self.segundoContainer,text="First Name", font=self.fontePadrao)
            self.firstnameLabel.pack(side=LEFT)
      
            self.firstname = Entry(self.segundoContainer)
            self.firstname["width"] = 30
            self.firstname["font"] = self.fontePadrao
            self.firstname.pack(side=LEFT)
      
            self.lastnameLabel = Label(self.terceiroContainer, text="Last Name", font=self.fontePadrao)
            self.lastnameLabel.pack(side=LEFT)
      
            self.lastname = Entry(self.terceiroContainer)
            self.lastname["width"] = 30
            self.lastname["font"] = self.fontePadrao
            self.lastname.pack(side=LEFT)
            
            self.titleLabel = Label(self.quartoContainer, text="Title", font=self.fontePadrao)
            self.titleLabel.pack(side=LEFT)
      
            self.titlename = Entry(self.quartoContainer)
            self.titlename["width"] = 30
            self.titlename["font"] = self.fontePadrao
            self.titlename.pack(side=LEFT)
      
            self.botao = Button(self.quintoContainer)
            self.botao["text"] = "FINGERPRINT"
            self.botao["font"] = ("Calibri", "24")
            self.botao["command"] = tela05alt.telacinco
            self.botao["width"] = 30
            self.botao.pack()
            
            self.home = Button(self.sextoContainer)
            self.home["text"] = "MAIN MENU"
            self.home["font"] = ("Calibri", "8")
            self.home["width"] = 12
            self.home["command"] = returntohome
            self.home.pack()
    
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
            
