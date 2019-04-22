from tkinter import *
from subprocess import call

pyprog = 'fpsim.py'
def callpy(): call(['python3', '-i', pyprog] )

root = Tk()
Button(root, text='Run', command=callpy).pack()
root.mainloop()