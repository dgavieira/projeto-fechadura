from tkinter import *
import sys

class Display(Frame):
    def __init__(self,master=0):
        Frame.__init__(self,master)
        self.entry = Entry(self)
        self.entry.pack()
        
        self.doIt = Button(self)
        self.doIt["text"] = "Do It"
        self.doIt["command"] = self.onEnter
        self.doIt.pack()
        
        self.output = Text(self)
        self.output.pack()
        
        sys.stdout = self
        self.pack()
        
    def onEnter(self):
        print(eval(self.entry.get()))
        
    def write(self, txt):
        self.output.insert(END,str(txt))
        
if __name__ == '__main__':
    Display().mainloop()