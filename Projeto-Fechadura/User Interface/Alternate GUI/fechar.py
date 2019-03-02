 #Método fechar tela
from tkinter import *
import tela01alt

def fechar():
    tela01alt.telaum.destroy(root)
    global root
    root.destroy()

    