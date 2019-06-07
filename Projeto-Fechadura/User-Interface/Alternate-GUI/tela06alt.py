#Title: Biometric Lock User Interface
#Organization: Optima-UFAM
#Screen 5: Member Deleting Screen
#Description: Shows list of enrolled member for admin level user to delete one of them from database
#INPUTS: optima.db
#Especs: Touchscreen LCD 3,5" 480x320
#Autor: Diego Vieira
#!/usr/local/bin/python
# -*- coding: utf-8 -*-

try:
    # for Python2
    from Tkinter import *
except ImportError:
    # for Python3
    from tkinter import *
from pynput.keyboard import Key, Controller
import sqlite3, readline
import tela03alt

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
            self.lista["selectmode"] = BROWSE
            self.scroll = Scrollbar(self.primeiroContainer)
            self.scroll["command"] = self.lista.yview
            self.lista.configure(yscrollcommand = self.scroll.set)
            self.lista.pack(side=LEFT)
            self.scroll.pack(side = RIGHT, fill = Y)
            
            self.fontePadrao = ("Arial","10")
            #elementos do segundo container
                
            self.BotaoUp = Button(master)
            self.BotaoUp["text"] = "UP"
            self.BotaoUp["font"] = self.fontePadrao
            self.BotaoUp["width"] = 18
            self.BotaoUp["height"] = 5
            self.BotaoUp["command"] = self.ScrollUp
            self.BotaoUp.grid(row = 0, column = 2, sticky = NW)
            
            self.BotaoDown = Button(master)
            self.BotaoDown["text"] = "DOWN"
            self.BotaoDown["font"] = self.fontePadrao
            self.BotaoDown["width"] = 18
            self.BotaoDown["height"] = 5
            self.BotaoDown["command"] = self.ScrollDown
            self.BotaoDown.grid(row = 1, column = 2, sticky = NW)
            
            #elementos do terceiro container
            self.BotaoLoad = Button(master)
            self.BotaoLoad["text"] = "LOAD"
            self.BotaoLoad["width"] = 18
            self.BotaoLoad["height"] = 3
            self.BotaoLoad["command"] = self.fetch_data
            #self.BotaoLoad["command"] = self.fetch_data_test
            self.BotaoLoad["font"] = self.fontePadrao
            self.BotaoLoad.grid(row = 2, column = 0, sticky = SW)
            
            self.BotaoBack = Button(master)
            self.BotaoBack["text"] = "BACK"
            self.BotaoBack["width"] = 18
            self.BotaoBack["height"] = 3
            self.BotaoBack["font"] = self.fontePadrao
            self.BotaoBack["command"] = backtoenroll
            self.BotaoBack.grid(row = 2, column = 1, sticky = SW)
            
            self.BotaoDelete = Button(master)
            self.BotaoDelete["text"] = "DELETE"
            self.BotaoDelete["width"] = 18
            self.BotaoDelete["height"] = 3
            self.BotaoDelete["font"] = self.fontePadrao
            self.BotaoDelete.grid(row = 2, column = 2, sticky = SW)
        
        def fetch_data_test(self): #rotina de testes
            self.lista.delete(0,END)
            db = ["leo", "cotta", "diego", "thalisson", "kadu", "savio"]
            for item in db:
                self.lista.insert(END, item)
            self.lista.selection_set(self.lista.index(0))
            keyboard = Controller()
            keyboard.press(Key.tab)
            keyboard.release(Key.tab)
            
                        
        def fetch_data(self): #rotina oficial de obtencao do query do banco
            conn = sqlite3.connect('optima.db')
            cursor = conn.cursor()
            cursor.execute("""SELECT
                               first_name AS FIRST_NAME,
                               last_name AS LAST_NAME,
                               title AS TITLE,
                               admin AS ADMIN_LEVEL,
                               pos_number AS POSITION_NUMBER
                           FROM optima""")
            rows = cursor.fetchall()
            for row in rows:
                print(row)
            self.lista.delete(0,END)
            for row in rows:
                self.lista.insert(END, row)
            keyboard = Controller()
            keyboard.press(Key.tab)
            keyboard.release(Key.tab)
            
        def ScrollDown(self):
            keyboard = Controller()
            keyboard.press(Key.down)
            keyboard.release(Key.down)
            
        def ScrollUp(self):
            keyboard = Controller()
            keyboard.press(Key.up)
            keyboard.release(Key.up)
                
    def fechar():
        root.destroy()
        
    def backtoenroll():
        fechar()
        tela03alt.telatres()
            
    root = Tk()
    ScreenSix(root)
    root.title("Delete Screen")
    root.geometry('478x270')
    #root.overrideredirect(True)
    root.mainloop()