#Title: Biometric Lock User Interface
#Organization: Optima-UFAM
#Screen 5: Member Deleting Screen
#Description: Shows list of enrolled member for admin level user to delete one of them from database
#INPUTS: optima.db
#Especs: Touchscreen LCD 3,5" 480x320
#Autor: Diego Vieira

from tkinter import *

def telaseis():
    class ScreenSix:
        def __init__(self, master = None):
            
            self.primeiroContainer = Frame(master)
            self.primeiroContainer.grid(row = 0, column = 0, rowspan = 2, columnspan = 2, sticky = NW)
            
            self.segundoContainer = Frame(master)
            self.segundoContainer.grid(row = 0, column = 2, rowspan = 2, sticky = NE)
            
            self.terceiroContainer = Frame(master)
            self.terceiroContainer.grid(row = 2, column = 0, rowspan = 3, sticky = S)
            
            #elementos dos primeiro container
            self.lista = Listbox(self.primeiroContainer)
            self.scroll = Scrollbar(self.primeiroContainer)
            self.scroll["command"] = lista.yview