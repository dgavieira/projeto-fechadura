#Title: Biometric Lock User Interface
#Organization: Optima-UFAM
#Screen 5: Member Deleting Screen
#Description: Shows list of enrolled member for admin level user to delete one of them from database
#INPUTS: optima.db
#Especs: Touchscreen LCD 3,5" 480x320
#Autor: Diego Vieira

from tkinter import *
import sqlite3

def telaseis():
    class ScreenSix:
        def __init__(self, master = None):
            
            self.primeiroContainer = Frame(master)
            self.primeiroContainer.grid(row = 0, column = 0, rowspan = 2, columnspan = 2, sticky = NW)
            
            #elementos dos primeiro container
            self.lista = Listbox(self.primeiroContainer)
            self.lista["width"] = 30
            self.lista["height"] = 10
            self.lista["font"] = ('MS','12')
            self.scroll = Scrollbar(self.primeiroContainer)
            self.scroll["command"] = self.lista.yview
            self.lista.configure(yscrollcommand = self.scroll.set)
            self.lista.pack(side=LEFT)
            self.scroll.pack(side = RIGHT, fill = Y)
            
            #teste inserir elementos na listbox
            self.lista.delete(0,END)
            for rows in range(30):
                self.lista.insert(END, rows)
            
            self.fontePadrao = ("Arial","10")
            #elementos do segundo container
                
            self.BotaoUp = Button(master)
            self.BotaoUp["text"] = "UP"
            self.BotaoUp["font"] = self.fontePadrao
            self.BotaoUp["width"] = 18
            self.BotaoUp["height"] = 5
            self.BotaoUp.grid(row = 0, column = 2, sticky = NW)
            
            self.BotaoDown = Button(master)
            self.BotaoDown["text"] = "DOWN"
            self.BotaoDown["font"] = self.fontePadrao
            self.BotaoDown["width"] = 18
            self.BotaoDown["height"] = 5
            self.BotaoDown.grid(row = 1, column = 2, sticky = NW)
            
            #elementos do terceiro container
            self.BotaoLoad = Button(master)
            self.BotaoLoad["text"] = "LOAD"
            self.BotaoLoad["width"] = 18
            self.BotaoLoad["height"] = 3
            self.BotaoLoad["command"] = self.fetch_data
            self.BotaoLoad["font"] = self.fontePadrao
            self.BotaoLoad.grid(row = 2, column = 0, sticky = SW)
            
            self.BotaoBack = Button(master)
            self.BotaoBack["text"] = "BACK"
            self.BotaoBack["width"] = 18
            self.BotaoBack["height"] = 3
            self.BotaoBack["font"] = self.fontePadrao
            self.BotaoBack.grid(row = 2, column = 1, sticky = SW)
            
            self.BotaoDelete = Button(master)
            self.BotaoDelete["text"] = "DELETE"
            self.BotaoDelete["width"] = 18
            self.BotaoDelete["height"] = 3
            self.BotaoDelete["font"] = self.fontePadrao
            self.BotaoDelete.grid(row = 2, column = 2, sticky = SW)
            
        def fetch_data(self):
            conn = sqlite3.connect('optima.db')
            cursor = conn.cursor()
            conn.execute("SELECT * FROM optima")
            rows = conn.fetchall()
            conn.disconnect()
            return rows
            
            
    root = Tk()
    ScreenSix(root)
    root.title("Delete Screen")
    root.geometry('478x270')
    #root.overrideredirect(True)
    root.mainloop()