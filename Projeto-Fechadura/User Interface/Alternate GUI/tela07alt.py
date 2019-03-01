#Title: Biometric Lock User Interface
#Organization: Optima-UFAM
#Screen 7: Verification Screen
#Description: Screen for make sure the ADMIN really wants to delete a member from the database
#Especs: Touchscreen LCD 3,5" 480x320
#Autor: Diego Vieira

from tkinter import *
import tela03alt

def telasete():
    class ScreenSeven:
        def __init__(self, master = None):
            self.fontePadrao = ("Arial","24")
            self.widget1 = Frame(master)
            self.widget1.pack()
            
            self.msg = Label(self.widget1, text = "ARE YOU SURE?")
            self.msg["font"] = self.fontePadrao
            self.msg["height"] = 5
            self.msg.pack()
            
            self.yes = Button(self.widget1, text = "YES")
            self.yes["font"] = self.fontePadrao
            self.yes["width"] = 12
            self.yes["command"] = tela03alt.telatres
            self.yes.pack(side=LEFT)
            
            self.no = Button(self.widget1,text = "NO")
            self.no["font"] = self.fontePadrao
            self.no["width"] = 18
            self.no.pack(side=RIGHT)
            
    root = Tk()
    ScreenSeven(root)
    root.title("Verification Screen")
    root.geometry('478x270')
    #root.overrideredirect(True)
    root.mainloop()
            
            
            
            
            