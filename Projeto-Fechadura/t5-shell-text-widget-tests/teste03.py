from tkinter import *
import os
import subprocess

root = Tk()
termf = Frame(root, height=400, width=500)

termf.pack(fill=BOTH, expand=YES)
wid = termf.winfo_id()
#os.system('xterm -into %d -geometry 40x20 -sb &' % wid)
#os.system('lxterminal -into %d -hold -geometry 300x400 -sb &' % wid)

root.mainloop()