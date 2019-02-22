from tkinter import *

#Set the window size
WINDOW_W = 478
WINDOW_H = 280

#Color set HEX COLOR standards
BLACK          = '#000000'
BRIGHTRED      = '#ff0000'
RED            = '#9b0000'
BRIGHTGREEN    = '#00ff00'
GREEN          = '#28A828'
BRIGHTBLUE     = '#0000ff'
BLUE           = '#00009b'
WHITE          = '#ffffff'
YELLOW         = '#ffff00'

class LCDscreen:
    def __init__(self, master = None):
        self.fontePadrao = ("Arial","10")
        self.first = Frame(master)
        self.first.pack()
        
        self.second = Frame(master)
        self.second.pack()
        
        self.third = Frame(master)
        self.third.pack()
        
        self.canvas = Canvas(self.first, width=WINDOW_W, height=WINDOW_H, background=YELLOW)
        self.canvas.pack()
        
        self.titleLabel = Label(self.third, text = "Title", font = self.fontePadrao)
        self.titleLabel.pack(side=LEFT)
        
        self.title = Entry(self.third)
        self.title["width"] = 30
        self.title["font"] = self.fontePadrao
        self.title.pack(side=LEFT)
        
def createDisplay():
    global tk, canvas, light
    #Creates the tkinter window
    tk = Tk()
    tk.title("Enroll Screen")
    tk.overrideredirect(True)
    tk.config(cursor="none")
    LCDscreen(tk)
    master.mainloop()
   
if __name__ ==  'main':
    createDisplay()
        
