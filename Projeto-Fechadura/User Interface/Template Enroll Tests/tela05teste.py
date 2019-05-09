from tkinter import *
import subprocess, sys, os
import sqlite3
from fpsimtest import main

def tela_cinco():
    class ScreenFive:
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
            
            self.quartoContainer = Frame(master)
            self.quartoContainer["padx"] = 20
            self.quartoContainer.pack()
            
            #elementos do primeiro Container
            self.titulo = Label(self.primeiroContainer)
            self.titulo["text"] = "FINGERPRINT ENROLL"
            self.titulo["font"] = ("Arial","20","bold")
            self.titulo.pack()
            
            #elementos do segundo Container
            self.prompt = Text(self.segundoContainer)
            self.prompt["relief"] = SUNKEN
            self.prompt["height"] = 8
            self.prompt.pack()
            
            self.fonteBotoes = ("Arial","10")
            #elementos do terceiro Container
            self.returnButton = Button(self.terceiroContainer)
            self.returnButton["text"] = "RETURN"
            self.returnButton["font"] = self.fonteBotoes
            self.returnButton["command"] = self.ret_screen_four
            self.returnButton["width"] = 10
            self.returnButton.pack(side = LEFT)
            
            self.runButton = Button(self.terceiroContainer)
            self.runButton["text"] = "RUN"
            self.runButton["font"] = self.fonteBotoes
            self.runButton["command"] = self.run_shell
            self.runButton["width"] = 10
            self.runButton.pack(side = LEFT)
            
            self.loadButton = Button(self.terceiroContainer)
            self.loadButton["text"] = "LOAD"
            self.loadButton["font"] = self.fonteBotoes
            #self.loadButton["command"] = self.load_db
            self.loadButton["width"] = 10
            self.loadButton.pack(side = LEFT)
                        
            #elementos do quarto container
            self.okButton = Button(self.quartoContainer)
            self.okButton["text"] = "OK"
            self.okButton["font"] = self.fonteBotoes
            self.okButton["command"] = self.conclude
            self.okButton["width"] = 10
            self.okButton.pack()
            
        def ret_screen_four(self):
            fechar()
            tela04teste.tela_quatro()
            
        def run_shell(self):
            self.prompt.delete(1.0,END)
            msg = "Executing Fingerprint Enroll"
            #path = '/home/pi/git-batch/pyfingerprint/src/files/examples/example_enroll.py'
            '''process = subprocess.Popen(['lxterminal','-e','python3', path],
                                                               stdout = subprocess.PIPE,
                                                               stderr = subprocess.PIPE,
                                                               stdin = subprocess.PIPE)'''
            process = subprocess.Popen(['lxterminal','-e','python3','fpsimtest.py'],
                                       stdout = subprocess.PIPE,
                                       stderr = subprocess.PIPE,
                                       stdin = subprocess.PIPE)
            
            self.prompt.insert(END, msg)
            process.stdin.write(b'\n')
            process.stdin.flush()
            stdout, stderr = process.communicate()
            #line = process.stdout.readline()
            #self.prompt.insert(END, line)
            #stdin, stdout, stderr = process.communicate()
            #stdout, stderr = process.communicate()
            #line = process.stdout.readline()
            flag = temp
            return flag
        
        def load_db(self):
            conn = sqlite3.connect('optima.db')
            cursor = conn.cursor()
            
            
        def conclude(self):
            fechar()
            #tela03alt.telatres()
            print("retornou a tela 03")
            
    def fechar():
        root.destroy()
        
    root = Tk()
    ScreenFive(root)
    root.title('Fingerprint Calibration Screen')
    root.geometry('478x270')
    #root.overrideredirect(True)
    root.mainloop()
    