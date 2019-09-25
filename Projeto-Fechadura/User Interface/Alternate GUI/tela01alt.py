#Title: Biometric Lock User Interface
#Organization: Optima-UFAM
#Screen 1: Main Screen
#Description: Main Screen for the User Interface
#Especs: Touchscreen LCD 3,5" 480x320
#Autor: Diego Vieira

#importa biblioteca tkinter
from tkinter import *

import tela02alt #importa tela seguinte

def telaum():
    class ScreenOne: #classe
        def __init__(self, master=None):
            #construtores
            self.widget1 = Frame(master, background = "yellow")
            self.widget1.pack(fill=X)
            
            self.button1 = Button(self.widget1, text = "OPTIONS")
            self.button1["font"]= ("Arial","24")
            self.button1["height"] = 2
            self.button1["command"] = doublefuncoptions
            self.button1.pack(side = TOP, fill=X)
            
            self.button2 = Button(self.widget1, text = "OPEN THE DOOR")
            self.button2["height"] = 2
            self.button2["font"]= ("Arial","24")
            self.button2.pack(side = TOP, fill=X)
            
            self.button3 = Button(self.widget1, text = "CANCEL")
            #self.button3["width"] = 50
            self.button3["height"] = 2
            self.button3["font"]= ("Arial","12")
            self.button3["command"] = fechar
            self.button3.pack(side = TOP, fill=X)

    #métodos
    def doublefuncoptions(): #chama transição para tela dois
        fechar()
        tela02alt.teladois()
        
    def fechar():
        root.destroy()

    #loop de inicialização da tela
    root = Tk()
    ScreenOne(root)
    root.title("Main Screen")
    root.geometry('478x270')
    #root.overrideredirect(True) #trava ponteiro do mouse e força app no primeiro plano
    root.mainloop()

if __name__ == "__main__": #permite executar esse script como principal
    telaum()