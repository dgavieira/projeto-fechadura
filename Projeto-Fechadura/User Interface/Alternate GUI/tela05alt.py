#Title: Biometric Lock User Interface
#Organization: Optima-UFAM
#Screen 4: Fingerprint Calibration
#Description: Shows the progress status for a fingerprint enrolling process on the database
#Especs: Touchscreen LCD 3,5" 480x320
#Autor: Diego Vieira

from tkinter import *
import sqlite3
import tela03alt

def telacinco():
    class ScreenFive:
        def __init__(self,master):
            self.widget1 = Frame(master)
            self.widget1.pack()
            
            self.msg = Label(self.widget1)
            self.msg["text"] = "Waiting for Fingerprint..."
            self.msg["font"] = ("Calibri","20","bold")
            self.msg.pack()
            
            self.button = Button(self.widget1)
            self.button["text"] = "OK"
            self.button["font"] = ("Calibri", "10")
            self.button["width"] = 10
            self.button["command"] = self.mudarTexto
            self.button.pack()
            
        def mudarTexto(self):
            if self.msg["text"] == "Waiting for Fingerprint...":
                self.msg["text"] = "Fingerprint registered"
                print("Fingerprint Registered")
                root.destroy()
                tela03alt.telatres()
            else:
                self.msg["text"] = "Waiting for Fingerprint"
            
    root = Tk()
    ScreenFive(root)
    root.title("Fingerprint Calibration Screen")
    root.geometry('478x270')
    #root.overrideredirect(True)
    root.mainloop()
