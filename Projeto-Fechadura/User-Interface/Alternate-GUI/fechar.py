 #Método fechar tela
#!/usr/local/bin/python
# -*- coding: utf-8 -*-
try:
    # for Python2
    from Tkinter import *
except ImportError:
    # for Python3
    from tkinter import *
import tela01alt

def fechar():
    tela01alt.telaum.destroy(root)
    root.destroy()

    