#Title: Biometric Lock User Interface
#Organization: Optima-UFAM
#Screen 1: Main Screen
#Description: Main Screen for the User Interface
#Especs: Touchscreen LCD 3,5" 480x320
#Autor: Diego Vieira

from tkinter import *

import tela02alt, fechar

def telaum():
    class ScreenOne:
        def __init__(self, master=None):
            self.widget1 = Frame(master, background = "yellow")
            self.widget1.pack()
            
            self.button1 = Button(self.widget1, text = "OPTIONS")
            self.button1["font"]= ("Arial","24")
            self.button1["width"] = 30
            self.button1["height"] = 3
            self.button1["command"] = doublefuncoptions
            self.button1.pack()
            
            self.button2 = Button(self.widget1, text = "OPEN THE DOOR")
            self.button2["width"] = 30
            self.button2["height"] = 3
            self.button2["font"]= ("Arial","24")
            self.button2.pack()
            
            self.button3 = Button(self.widget1, text = "CANCEL")
            self.button3["width"] = 50
            self.button3["height"] = 2
            self.button3["font"]= ("Arial","12")
            self.button3["command"] = fechar
            self.button3.pack()
    
    def doublefuncoptions():
        fechar()
        tela02alt.teladois()
        
    def fechar():
        root.destroy()
            
    root = Tk()
    ScreenOne(root)
    root.title("Main Screen")
    root.geometry('478x270')
    #root.overrideredirect(True)
    root.mainloop()
    
    
