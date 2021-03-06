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
            self.segundoContainer.update_idletasks()
            
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
            self.runButton["command"] = self.runshell
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
            
        def get_info(self):
            print(self.prompt.get("1.0","current lineend"))
            
        def runshell(self):
            process = subprocess.Popen(['python3','fpsim.py'], stdout = subprocess.PIPE,
                                                               stderr = subprocess.PIPE,
                                                               stdin = subprocess.PIPE)
            
            stdin, stdout, stderr = process.communicate("input")
            line = process.stdout.readline()
            self.prompt.insert(END, line)
                
        '''def runshell(self):
            path = ''
            process = subprocess.Popen(['python3','fpsim.py'], stdout = subprocess.PIPE,
                                                               stderr = subprocess.PIPE,
                                                               stdin = subprocess.PIPE)
            self.prompt.delete(1.0,END)
            process.stdin.write(b'\n')
            process.stdin.flush()
            line = process.stdout.readline()
            msg = "Executing Fingerprint Enroll"
            #stdin, stdout, stderr = process.communicate()
            #stdout, stderr = process.communicate()
            #line = process.stdout.readline()
            self.prompt.insert(END, line)
            self.prompt.see(END)
            self.prompt.update_idletasks()'''
            
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