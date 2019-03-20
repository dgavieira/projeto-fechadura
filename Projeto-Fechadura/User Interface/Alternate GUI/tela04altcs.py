#Title: Biometric Lock User Interface
#Organization: Optima-UFAM
#Screen 4.2: Enroll Screen - Confirmation Step
#Description: Make Sure the Admin Level User wants to enrolls the correct info on database
#Especs: Touchscreen LCD 3,5" 480x320
#Autor: Diego Vieira

from tkinter import *
import tela04alt
import sqlite3

def telaquatrodois():
    class ScreenFourConfStep(ScreenFour):
        def __init__(self, master = None):
            self.fontePadrao = ("Arial","24")
            self.widget1 = Frame(master)
            self.widget1.pack()
            
            self.widget2 = Frame(master)
            self.widget2.pack()
            
            self.widget3 = Frame(master)
            self.widget3.pack()
            
            self.widget4 = Frame(master)
            self.widget4.pack()
            
            
            self.msg = Label(self.widget1, text = "ARE YOU SURE?")
            self.msg["font"] = self.fontePadrao
            self.msg["height"] = 5
            self.msg.pack()
            
            self.firstname = Label(self.
            
            self.yes = Button(self.widget1, text = "YES")
            self.yes["font"] = self.fontePadrao
            self.yes["width"] = 12
            #self.yes["command"] = tela03alt.telatres
            self.yes.pack(side=LEFT)
            
            self.no = Button(self.widget1,text = "NO")
            self.no["font"] = self.fontePadrao
            self.no["width"] = 18
            #self.no.["command"] = 
            self.no.pack(side=RIGHT)
            
            self.widget2 = Frame(master)
            self.widget2.pack(side=BOTTOM)
            
            self.home = Button(self.widget2,text = "MAIN MENU")
            self.home["font"] = ("Calibri","8")
            self.home["width"] = 12
            self.home["command"] = returntohome
            self.home.pack(side=BOTTOM)
            
    def returntohome():
        fechar()
        tela01alt.telaum()
        
    def fechar():
        root.destroy()
            
    root = Tk()
    ScreenFourConfStep(root)
    root.title("Verification Screen")
    root.geometry('478x270')
    #root.overrideredirect(True)
    root.mainloop()