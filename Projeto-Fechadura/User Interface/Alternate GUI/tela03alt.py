# Title: Biometric Lock User Interface
# Organization: Optima-UFAM
# Screen 3: ADM level menu screen
# Description: shows options on ADM level access to subscribe or delete lab members from the software database
# Especs: Touchscreen LCD 3,5" 480x320
# Autor: Diego Vieira

# importa bibliotecas
from tkinter import *
# importa telas que interagem com a tela tres
import tela01alt, tela02alt, tela04alt03


def telatres():
    class ScreenThree:  # classe
        def __init__(self, master=None):
            # construtores de containeres
            self.widget1 = Frame(master, background="yellow")
            self.widget1.pack()

            # construtor dos objetos
            self.button1 = Button(self.widget1, text="ENROLL")
            self.button1["font"] = ("Arial", "24")
            self.button1["width"] = 30
            self.button1["height"] = 3
            self.button1["command"] = doublefuncenroll
            self.button1.pack()

            self.button2 = Button(self.widget1, text="DELETE")
            self.button2["font"] = ("Arial", "24")
            self.button2["height"] = 3
            self.button2["width"] = 30
            self.button2.pack()

            self.button3 = Button(self.widget1, text="EXIT")
            self.button3["font"] = ("Arial", "24")
            self.button3["width"] = 30
            self.button2["height"] = 2
            self.button3["command"] = doublefuncexit
            self.button3.pack()

    # funcao de avançar para proxima tela
    def doublefuncenroll():
        fechar()
        tela04alt03.telaquatro()

    # funcao de retornar para tela inicial
    def doublefuncexit():
        fechar()
        tela01alt.telaum()

    def fechar():
        root.destroy()

    # loop de inicialização da tela
    root = Tk()
    ScreenThree(root)
    root.title("ADM Level Menu Screen")
    root.geometry('478x270')
    # root.overrideredirect(True)
    root.mainloop()


if __name__ == "__main__":  # permite executar esse script como principal
    telatres()
