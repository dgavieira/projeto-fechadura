#Title: Biometric Lock User Interface
#Organization: Optima-UFAM
#Screen 3: ADM level menu screen
#Description: shows options on ADM level access to subscribe or delete lab members from the software database
#Especs: Touchscreen LCD 3,5" 480x320
#Autor: Diego Vieira
#!/usr/local/bin/python
# -*- coding: utf-8 -*-

#tratamento de excecao para portabilidade do tkinter
try:
    # for Python2
    from Tkinter import *
except ImportError:
    # for Python3
    from tkinter import *
#importa telas que interagem com a atual
import tela01alt, tela02alt, tela04alt03, tela06alt


def telatres():
    class ScreenThree: 
        def __init__(self, master=None): #construtor da classe referente a tela 03
            #constroi "moldura"
            self.widget1 = Frame(master)
            self.widget1.pack()

            #construtor do botao ENROLL
            self.button1 = Button(self.widget1, text = "ENROLL")
            self.button1["font"]= ("Arial","24")
            self.button1["width"] = 30
            self.button1["height"] = 3
            self.button1["command"] = doublefuncenroll
            self.button1.pack()

            #construtor do botao DELETE
            self.button2 = Button(self.widget1, text = "DELETE")
            self.button2["font"]= ("Arial","24")
            self.button2["height"] = 3
            self.button2["width"] = 30
            self.button2["command"] = gotodelete
            self.button2.pack()

            #construtor do botao EXIT
            self.button3 = Button(self.widget1, text = "EXIT")
            self.button3["font"]= ("Arial","24")
            self.button3["width"] = 30
            self.button2["height"] = 2
            self.button3["command"] = doublefuncexit
            self.button3.pack()
            
    #metodos da tela 03 - destroem tela atual e abrem tela referente de acordo com o fluxo da UI
            
    def doublefuncenroll():
        fechar()
        tela04alt03.telaquatro()
        
    def doublefuncexit():
        fechar()
        tela01alt.telaum()
        
    def fechar():
        root.destroy()
        
    def gotodelete():
        fechar()
        tela06alt.telaseis()

    #execucao da tela
    root = Tk()
    ScreenThree(root)
    root.title("ADM Level Menu Screen")
    root.geometry('478x270')
    #root.overrideredirect(True)
    root.mainloop()
