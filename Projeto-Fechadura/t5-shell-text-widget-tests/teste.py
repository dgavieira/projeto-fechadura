from tkinter import *
import sys, os, subprocess

def enroll_screen():
    class EnrScrn():
        def __init__(self, master = None):
            self.primeiroContainer = Frame(master)
            self.primeiroContainer["pady"] = 10
            self.primeiroContainer.pack()
            
            self.segundoContainer = Frame(master)
            self.segundoContainer["padx"] = 20
            self.segundoContainer.pack(fill = X, expand = YES)
            
            self.terceiroContainer = Frame(master)
            self.terceiroContainer["padx"] = 20
            self.terceiroContainer.pack()
            
            #elementos do primeiro container
            self.titulo = Label(self.primeiroContainer)
            self.titulo["text"] = "FINGERPRINT ENROLL"
            self.titulo["font"] = ("Arial","20","bold")
            self.titulo.pack()
            
            #elementos do segundo container
            self.prompt = Text(self.segundoContainer)
            self.prompt["relief"] = SUNKEN
            self.prompt["height"] = 8
            self.prompt.pack()
            
            self.fonteBotoes = ("Arial","10")
            #elementos do terceiro container
            self.retButton = Button(self.terceiroContainer)
            self.retButton["text"] = "RETURN"
            self.retButton["font"] = self.fonteBotoes
            self.retButton["command"] = self.retscreenfour
            self.retButton["width"] = 10
            self.retButton.pack(side=LEFT)
            
            self.runButton = Button(self.terceiroContainer)
            self.runButton["text"] = "RUN"
            self.runButton["font"] = self.fonteBotoes
            self.runButton["command"] = self.run_process
            self.runButton["width"] = 10
            self.runButton.pack(side=LEFT)
            
            self.okButton = Button(self.terceiroContainer)
            self.okButton["text"] = "OK"
            self.okButton["font"] = self.fonteBotoes
            self.okButton["command"] = self.conclude
            self.okButton["width"] = 10
            self.okButton.pack(side=LEFT)
            
        def retscreenfour(self):
            self.prompt.delete(1.0,END)
            self.prompt.insert(END, "retornou à tela quatro")
            
        def runshell(self):
            f = open('fpsim.py','r')
            
        def run_process(self):
            self.prompt.delete(1.0,END)
            self.prompt.insert(INSERT, self.runshell())
            
        def conclude(self):
            self.prompt.delete(1.0,END)
            self.prompt.insert(END, "Fingerprint Registered")
    
    root = Tk()
    EnrScrn(root)
    root.title('Fingerprint Calibration Screen')
    root.geometry('478x270')
    #root.overrideredirect(True)
    root.mainloop()
    
def main():
    enroll_screen()

if __name__ == "__main__":
    main()