#Title: Biometric Lock User Interface
#Organization: Optima-UFAM
#Screen 3: ADM level menu screen
#Description: shows options on ADM level access to subscribe or delete lab members from the software database
#Especs: Touchscreen LCD 3,5" 480x320
#Autor: Diego Vieira

from tkinter import *
import tela01alt, tela02alt, tela04alt

def telatres():
    class ScreenThree:
        def __init__(self, master=None):
            self.widget1 = Frame(master, background = "yellow")
            self.widget1.pack()
            
            '''self.canvas = Canvas(self.widget1, background = "yellow")
            self.canvas.place()'''
            
            self.button1 = Button(self.widget1, text = "ENROLL")
            self.button1["font"]= ("Arial","24")
            self.button1["width"] = 30
            self.button1["command"] = doublefuncenroll
            self.button1.pack()
            
            self.button2 = Button(self.widget1, text = "DELETE")
            self.button2["font"]= ("Arial","24")
            self.button2["width"] = 30
            self.button2.pack()
            
            self.button3 = Button(self.widget1, text = "EXIT")
            self.button3["font"]= ("Arial","24")
            self.button3["width"] = 30
            self.button3["command"] = doublefuncexit
            self.button3.pack()
            
    def doublefuncenroll():
        fechar()
        tela04alt.telaquatro()
        
    def doublefuncexit():
        fechar()
        tela01alt.telaum()
        
    def fechar():
        root.destroy()
        
    root = Tk()
    ScreenThree(root)
    root.title("ADM Level Menu Screen")
    root.geometry('478x270')
    #root.overrideredirect(True)
    root.mainloop()
