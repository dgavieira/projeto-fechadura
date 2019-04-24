from tkinter import *
from Speedtest import ping_speed, download_speed, upload_speed

root = Tk()
text = Text(root)
text.insert(INSERT, ping_speed)
text.insert(END, download_speed)
text.pack()
mainloop()