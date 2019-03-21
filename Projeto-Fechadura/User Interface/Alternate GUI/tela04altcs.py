#Title: Biometric Lock User Interface
#Organization: Optima-UFAM
#Screen 4.2: Enroll Screen - Confirmation Step
#Description: Make Sure the Admin Level User wants to enrolls the correct info on database
#Especs: Touchscreen LCD 3,5" 480x320
#Autor: Diego Vieira

from tkinter import *
from tela04alt import *
import sqlite3

def telaquatrodois():
    
    conn = sqlite3.connect('optima.db')
    cursor = conn.cursor()

    #Enabling schema
    cursor.execute("""CREATE TABLE IF NOT EXISTS optima (
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                title TEXT NOT NULL)""")
    
    class ScreenFourConfStep(telaquatro):
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
            
            self.firstname = Label(self.widget2)
            self.firstname = tela04alt.telaquatro.ScreenFour.p_first_name
            self.firstname["font"] = ("Arial","10")
            self.firstname.pack()
            
            self.lastname = Label(self.widget3)
            self.lastname = tela04alt.telaquatro.ScreenFour.p_last_name
            self.lastname["font"] = ("Arial","10")
            self.lastname.pack()
            
            self.title = Label(self.widget4)
            self.title = tela04alt.telaquatro.ScreenFour.p_title
            self.title["font"] = ("Arial","10")
            self.title.pack()
                                      
            self.yes = Button(self.widget1, text = "YES")
            self.yes["font"] = self.fontePadrao
            self.yes["width"] = 12
            self.yes["command"] = self.enabledb
            self.yes.pack(side=LEFT)
            
            self.no = Button(self.widget1,text = "NO")
            self.no["font"] = self.fontePadrao
            self.no["width"] = 18
            self.no["command"] = returntelaquatro
            self.no.pack(side=RIGHT)
            
            self.widget2 = Frame(master)
            self.widget2.pack(side=BOTTOM)
            
            self.home = Button(self.widget2,text = "MAIN MENU")
            self.home["font"] = ("Calibri","8")
            self.home["width"] = 12
            self.home["command"] = returntohome
            self.home.pack(side=BOTTOM)
            
        def enabledb(self):
            cursor.execute("""
                INSERT INTO optima (first_name, last_name, title)
                VALUES (?, ?, ?)
                """, (p_first_name, p_last_name, p_title))
            conn.commit()
            print('Dados inseridos com sucesso.')
            conn.close()
            fechar()
            tela05alt.telacinco()
            
    def returntohome():
        fechar()
        tela01alt.telaum()
        
    def fechar():
        root.destroy()
    
    def returntelaquatro():
        fechar()
        tela04alt.telaquatro()
            
    root = Tk()
    ScreenFourConfStep(root)
    root.title("Verification Screen")
    root.geometry('478x270')
    #root.overrideredirect(True)
    root.mainloop()