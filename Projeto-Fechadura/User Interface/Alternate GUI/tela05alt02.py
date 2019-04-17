#Title: Biometric Lock User Interface
#Organization: Optima-UFAM
#Screen 5: Fingerprint Enrolling Calibration Screen
#Description: Gets fingerprint data for the member previously enrolled
#INPUTS: example_enroll.py
#Especs: Touchscreen LCD 3,5" 480x320
#Autor: Diego Vieira

from tkinter import *
import tela04alt03, tela03alt

def telacinco():
    class ScreenFive:
        def __init__(self, master = None):
            
            self.primeiroContainer = Frame(master)
            self.primeiroContainer["pady"] = 10
            self.primeiroContainer.pack()
            
            self.segundoContainer = Frame(master)
            self.segundoContainer["padx"] = 20
            self.segundoContainer.pack(fill = X, expand = YES)
            
            self.terceiroContainer = Frame(master)
            self.terceiroContainer["padx"] = 20
            self.terceiroContainer.pack()
            
            #elementos do primeiro Container
            self.titulo = Label(self.primeiroContainer)
            self.titulo["text"] = "FINGERPRINT ENROLL"
            self.titulo["font"] = ("Arial","20","bold")
            self.titulo.pack()
            
            #elementos do segundo Container
            self.prompt = Text(self.segundoContainer)
            self.prompt["relief"] = SUNKEN
            self.prompt["height"] = 8
            self.prompt.pack()
            
            self.fonteBotoes = ("Arial","10")
            #elementos do terceiro Container
            self.returnButton = Button(self.terceiroContainer)
            self.returnButton["text"] = "RETURN"
            self.returnButton["font"] = self.fonteBotoes
            self.returnButton["command"] = self.retscreenfour
            self.returnButton["width"] = 10
            self.returnButton.pack(side = LEFT)
            
            self.runButton = Button(self.terceiroContainer)
            self.runButton["text"] = "RUN"
            self.runButton["font"] = self.fonteBotoes
            #self.runButton["command"] =
            self.runButton["width"] = 10
            self.runButton.pack(side = LEFT)
            
            self.okButton = Button(self.terceiroContainer)
            self.okButton["text"] = "OK"
            self.okButton["font"] = self.fonteBotoes
            self.okButton["command"] = self.conclude
            self.okButton["width"] = 10
            self.okButton.pack(side = LEFT)
            
        def retscreenfour(self):
            fechar()
            tela04alt03.telaquatro()
            
        def conclude(self):
            fechar()
            tela03alt.telatres()
            
    def fechar():
        root.destroy()
        
    root = Tk()
    ScreenFive(root)
    root.title('Fingerprint Calibration Screen')
    root.geometry('478x270')
    #root.overrideredirect(True)
    root.mainloop()
    