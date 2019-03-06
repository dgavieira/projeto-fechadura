#Title: Biometric Lock User Interface
#Organization: Optima-UFAM
#Screen 4: Fingerprint Calibration
#Description: Shows the progress status for a fingerprint enrolling process on the database
#Especs: Touchscreen LCD 3,5" 480x320
#Autor: Diego Vieira

from tkinter import *
from tkinter.ttk import *
import tela03alt

def telacinco():
    class ScreenFive():
        def __init__(self, master = None):
            self.fontePadrao = ("Arial", "10")
            self.primeiroContainer = Frame(master)
            self.primeiroContainer["padx"] = 20
            self.primeiroContainer.pack()
            
            self.primeiraSenhaLabel = Label(self.primeiroContainer, text="Senha", font=self.fontePadrao)
            self.primeiraSenhaLabel.pack(side=LEFT)
      
            self.primeirasenha = Entry(self.primeiroContainer)
            self.primeirasenha["width"] = 30
            self.primeirasenha["font"] = self.fontePadrao
            self.primeirasenha["show"] = "*"
            self.ṕrimeirasenha.pack(side=LEFT)
            
            self.chanceum = ttk.ProgressBar(master, orient = HORIZONTAL, length = 120)
            self.chanceum.pack()
            
            self.segundoContainer = Frame(master)
            self.segundoContainer["padx"] = 20
            self.segundoContainer.pack()
            
            self.segundaSenhaLabel = Label(self.segundoContainer, text="Senha", font=self.fontePadrao)
            self.segundaSenhaLabel.pack(side=LEFT)
      
            self.segundasenha = Entry(self.segundoContainer)
            self.segundasenha["width"] = 30
            self.segundasenha["font"] = self.fontePadrao
            self.segundasenha["show"] = "*"
            self.segundasenha.pack(side=LEFT)
            
            self.chancedois = ttk.ProgressBar(master, orient = HORIZONTAL, length = 120)
            self.chancedois.pack()
            
            self.terceiroContainer = Frame(master)
            self.terceiroContainer["padx"] = 20
            self.terceiroContainer.pack()
            
            self.terceiraSenhaLabel = Label(self.terceiroContainer, text="Senha", font=self.fontePadrao)
            self.terceiraSenhaLabel.pack(side=LEFT)
      
            self.terceirasenha = Entry(self.terceiroContainer)
            self.terceirasenha["width"] = 30
            self.terceirasenha["font"] = self.fontePadrao
            self.terceirasenha["show"] = "*"
            self.terceirasenha.pack(side=LEFT)
            
            self.chancetres = ttk.ProgressBar(master, orient = HORIZONTAL, length = 120)
            self.chancetres.pack()
            
    root = Tk()
    ScreenFive(root)
    root.title("Fingerprint Calibration Screen")
    root.geometry('478x270')
    #root.overrideredirect(True)
    root.mainloop()