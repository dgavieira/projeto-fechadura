from tkinter import *
import sqlite3

conn = sqlite3.connect('optima.db')
cursor = conn.cursor()



def createscreen(master = None):
    fontePadrao = ("Arial", "10")
    primeiroContainer = Frame(master)
    primeiroContainer["pady"] = 10
    primeiroContainer.pack()
          
    segundoContainer = Frame(master)
    segundoContainer["padx"] = 20
    segundoContainer.pack()
          
    terceiroContainer = Frame(master)
    terceiroContainer["padx"] = 20
    terceiroContainer.pack()
          
    quartoContainer = Frame(master)
    quartoContainer["pady"] = 20
    quartoContainer.pack()
                
    quintoContainer = Frame(master)
    quintoContainer["pady"] = 20
    quintoContainer.pack()
                
    sextoContainer = Frame(master)
    sextoContainer["pady"] = 20
    sextoContainer.pack()
          
    titulo = Label(primeiroContainer, text="ENROLL")
    titulo["font"] = ("Arial", "10", "bold")
    titulo.pack()
          
    firstnameLabel = Label(segundoContainer,text="First Name", font=fontePadrao)
    firstnameLabel.pack(side=LEFT)
          
    firstname = Entry(segundoContainer)
    firstname["width"] = 30
    firstname["font"] = fontePadrao
    firstname.pack(side=LEFT)
          
    lastnameLabel = Label(terceiroContainer, text="Last Name", font=fontePadrao)
    lastnameLabel.pack(side=LEFT)
          
    lastname = Entry(terceiroContainer)
    lastname["width"] = 30
    lastname["font"] = fontePadrao
    lastname.pack(side=LEFT)
                
    titleLabel = Label(quartoContainer, text="Title", font=fontePadrao)
    titleLabel.pack(side=LEFT)
          
    titlename = Entry(quartoContainer)
    titlename["width"] = 30
    titlename["font"] = fontePadrao
    titlename.pack(side=LEFT)
                
    home = Button(sextoContainer)
    home["text"] = "OK"
    home["font"] = ("Calibri", "8")
    home["width"] = 12
    home["command"] = fechar
    home.pack()
            
p_first_name = firstname.get()
p_last_name = lastname.get()
p_title = title.get()
cursor.execute("""
    INSERT INTO optima (first_name, last_name, title)
    VALUES (?, ?, ?)
    """, (p_first_name, p_last_name, p_title))
conn.commit()
print('Dados inseridos com sucesso.')
conn.close()

def fechar():
    root.destroy()
    
root = Tk()                    
createscreen()
root.title("Enroll Screen")
root.geometry('478x270')
#root.overrideredirect(True)
root.mainloop()