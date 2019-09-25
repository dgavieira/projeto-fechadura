import tkinter
import os
from subprocess import Popen, PIPE
#ip = '192.168.1.1'
def get_info(arg):
    print(tfield.get("1.0", "current lineend"))
    
root = tkinter.Tk()
tfield = tkinter.Text(root)
tfield.pack()
#f = os.popen('python3','fpsim.py')
f = Popen(['python3','fpsim.py'],stdin = PIPE, stdout = PIPE, stderr = PIPE)

for line in f:
    line = line.strip()
    if line:
        tfield.insert("end", line+"\n")
        # tfield.get("current linestart", "current lineend")
        
tfield.bind("<Return>", get_info)
root.mainloop()
f.close()