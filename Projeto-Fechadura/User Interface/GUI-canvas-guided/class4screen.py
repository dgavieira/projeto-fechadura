from tkinter import *

class Application:
    def __init__(self, master=None):
        self.fontePadrao = ("Arial","10")
        
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["padx"] = 20
        self.primeiroContainer.pack()
        
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["padx"] = 20
        self.primeiroContainer.pack()
        
        self.nameLabel = Label(self.primeiroContainer, text = "Name", font = self.fontePadrao)
        self.nameLabel.pack(side=LEFT)
        
        self.name = Entry(self.primeiroContainer)
        self.name["width"] = 30
        self.name["font"] = self.fontePadrao
        self.name.pack(side=LEFT)
        
        self.titleLabel = Label(self.segundoContainer, text = "Title", font = self.fontePadrao)
        self.titleLabel.pack(side=LEFT)
        
        self.title = Entry(self.segundoContainer)
        self.title["width"] = 30
        self.title["font"] = self.fontePadrao
        self.title.pack(side=LEFT)
        
        
        