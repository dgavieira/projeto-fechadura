from tkinter import *
import sqlite3


class ScreenFive:
    def __init__(self,master):
        self.widget1 = Frame(master)
        self.widget1.pack()
        
        self.msg = Label(self.widget1)
        self.msg["text"] = "Waiting for Fingerprint"
        self.msg["font"] = ("Calibri","20","bold")
        self.msg.pack()
        
        self.button = Button(self.widget1)
        self.button["text"] = "ACTIVATE"
        self.button["font"] = ("Calibri","10")
        self.button["width"] = 10
        #self.button["command"] =
        self.button.pack()
        
root = Tk()
ScreenFive(root)
root.title("Fingerprint Calibration Screen")
root.geometry('478x270')
root.mainloop()
