from tkinter import *
import os

root = Tk()
termf = Frame(root, height=200, width=400)
termf.pack(fill=BOTH, expand=YES)
wid = termf.winfo_id()
os.system('xterm -into %d -geometry 400x200 -e /root/.bashrc&' % wid)

root.mainloop()