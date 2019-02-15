#Programa: Interface Grafica Raspberry para Tranca Eletronica 
#Autor: Lucas Tribuzy
 
import RPi.GPIO as GPIO
import time
import example_new
import os
import example_enroll


#from Tkinter import  #Use esta linha para Python 2
from tkinter import * #Use esta linha para Python 3
from subprocess import call
from subprocess import Popen
 
GPIO.setmode(GPIO.BOARD)
 
#Definicao dos pinos do led RGB como saida
GPIO.setup(40, GPIO.OUT)
GPIO.setup(38, GPIO.OUT)
GPIO.setup(36, GPIO.OUT)
GPIO.setup(35, GPIO.OUT)
GPIO.setup(32, GPIO.OUT)
 
#Define o pino do sensor como entrada
 
#Ativa Anodo Led RGB
GPIO.output(32, 1)
 
#Alimentacao sensor
 
#Estado inicial dos leds
estado_1 = False
estado_2 = False
estado_3 = False
estado_4 = False 
#rotina para acender o led
def acendeled(pino_led):
    GPIO.output(pino_led, 0)
    return
 
#rotina para apagar o led
def apagaled(pino_led):
    GPIO.output(pino_led, 1)
    return
 
#Apaga o led
apagaled(40)
apagaled(38)
apagaled(36)
 
#Define o tamanho da tela
WINDOW_W = 478
WINDOW_H = 280
 
#Definicao de cores
BLACK          = '#000000'
BRIGHTRED      = '#ff0000'
RED            = '#9b0000'
BRIGHTGREEN    = '#00ff00'
GREEN          = '#28A828'
BRIGHTBLUE     = '#0000ff'
BLUE           = '#00009b'
WHITE          = '#ffffff'
YELLOW         = '#ffff00'

def createDisplay():
  global tk, canvas, light
  #Cria a janela tk
  tk = Tk()
  tk.title("LucasTribuzy")
   
  tk.overrideredirect(True)
  tk.config(cursor="none")
   
  #tk.geometry("{0}x{1}+0+0".format(tk.winfo_screenwidth(), tk.winfo_screenheight()))
   
  #Adiciona a area para desenho
  canvas = Canvas(tk, width=WINDOW_W, height=WINDOW_H, background=BLACK)
   
  #Desenha Botao1  
  obj1Id = canvas.create_rectangle(5,5,159,155,fill=BRIGHTRED, tags = "objt1Tag")
  obj2Id = canvas.create_text( 80, 80,  text="Delete", fill="white", font=("Helvetica", 30, "bold"))
 
  canvas.tag_bind(obj1Id, '<Button-1>', onObjectClick1)
  canvas.tag_bind(obj2Id, '<Button-1>', onObjectClick1)
 
  #Desenha Botao2
  obj3Id = canvas.create_rectangle(162, 5, 316, 155,fill=GREEN,tags = "objt3Tag")
  obj4Id = canvas.create_text(236, 80,  text="Enroll", fill="white", font=("Helvetica", 30, "bold"))
   
  canvas.tag_bind(obj3Id, '<Button-1>', onObjectClick2)
  canvas.tag_bind(obj4Id, '<Button-1>', onObjectClick2)
 
  #Desenha Botao3
  obj5Id = canvas.create_rectangle(319, 5, 473,155,fill=BRIGHTBLUE,tags = "objt5Tag")
  obj6Id = canvas.create_text(396, 80,  text="Search", fill="white", font=("Helvetica", 30, "bold"))
   
  canvas.tag_bind(obj5Id, '<Button-1>', onObjectClick3)
  canvas.tag_bind(obj6Id, '<Button-1>', onObjectClick3)
  
  #Desenho Botão 4
  obj7Id = canvas.create_rectangle(5,160, 473, 275,fill=YELLOW,tags = "objt7Tag")
  obj8Id = canvas.create_text(240, 220,  text="Liberar Porta", fill="BLACK", font=("Helvetica", 50, "bold"))
  
  canvas.tag_bind(obj7Id, '<Button-1>', onObjectClick4)
  canvas.tag_bind(obj8Id, '<Button-1>', onObjectClick4)
     
  canvas.pack()
 
  #Cria botao SAIR
  btn = Button(tk, height=1, text="Sair", font=("Arial", 12, "bold"), command=terminate)
  #btn = Button(tk, height=1, text="Sair", font=("Arial", 12, "bold"), command=example_enroll1.enroll)
  btn.pack()
  
  #btn1 = Button(tk, height=1, text="liberar Porta", font=("Arial", 20, "bold"), command=terminate)
  #btn1.pack()
  #Verifica se o sensor infravermelho foi acionado
  #tk.after(100, checkPort)
  tk.mainloop()
 
def onObjectClick1(event):
  #Clique no botao 1
  global estado_1
  estado_1 = not estado_1
  print("Programa Delete")
  
  if estado_1 == True:
      apagaled(38)
      apagaled(36)
      acendeled(40)
  if estado_1 == False:
      apagaled(40)
      
      
   
def onObjectClick2(event):
  #Clique no botao 2
  global estado_2
  estado_2 = not estado_2
  example_enroll.enroll()
  print("Programa Enroll")
  if estado_2 == True:
      apagaled(40)
      apagaled(36)
      acendeled(38)
  if estado_2 == False:
      apagaled(38)
 
def onObjectClick3(event):
  #Clique no botao 3
  global estado_3
  estado_3 = not estado_3
  print("Programa Search")
  #os.system('python example_new.py')
  #call(["python", "example_new.py"])
  Popen('python example_new.py')
  if estado_3 == True:
      apagaled(40)
      apagaled(38)
      acendeled(36)
  if estado_3 == False:
      apagaled(36)
 
def onObjectClick4(event):
  #Clique no Botão 4
  global estado_4
  estado_4 = not estado_4
  print("Programa Liberar Porta")
  if estado_4 == True:
      apagaled(40)
      apagaled(38)
      acendeled(36)
  if estado_4 == False:
      apagaled(36)
  
 
def terminate():
 #Acao do botao SAIR
  global tk
  tk.destroy()
  
def main():
  createDisplay()
          
try:
    if __name__ == '__main__': 
        main()
   
finally:
  #Libera as portas da GPIO
    GPIO.cleanup()