#Title: Biometric Lock User Interface
#Organization: Optima-UFAM
#Screen 2: Search Screen for ADM users
#Description:Starts the Fingerprint search loop only for ROOT ADM users
#Especs: Touchscreen LCD 3,5" 480x320
#Autor: Diego Vieira

import RPi.GPIO as GPIO
import time

from tkinter import *

GPIO.setmode(GPIO.BOARD)
 
#RGB LED pin set as output
GPIO.setup(40, GPIO.OUT)
GPIO.setup(38, GPIO.OUT)
GPIO.setup(36, GPIO.OUT)
GPIO.setup(35, GPIO.OUT)
GPIO.setup(32, GPIO.OUT)
 
#sets sensor pin as input
GPIO.setup(37, GPIO.IN)
 
#Turns LED RGB anode on
GPIO.output(32, 1)
 
#Sensor source
GPIO.output(35, 1)
 
#LEDs initial state
estado_1 = False
estado_2 = False
estado_3 = False
 
#LED turn on loop
def acendeled(pino_led):
    GPIO.output(pino_led, 0)
    return
 
#LED turn off loop
def apagaled(pino_led):
    GPIO.output(pino_led, 1)
    return
 
#LED turn off
apagaled(40)
apagaled(38)
apagaled(36)

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

def createDisplay():
  global tk, canvas, light
  #Creates the tkinter window
  tk = Tk()
  tk.title("Admin Access")
   
  tk.overrideredirect(True)
  tk.config(cursor="none")
   
  #tk.geometry("{0}x{1}+0+0".format(tk.winfo_screenwidth(), tk.winfo_screenheight()))
   
  #Adds the canvas area
  canvas = Canvas(tk, width=WINDOW_W, height=WINDOW_H, background=BLACK)
  
  #Shows "Master Finger" Text
  text = canvas.create_text( 239, 140,  text="OPTIONS", fill="white", font=("Helvetica", 30, "bold"))
  
  canvas.pack()
 
  #Creates exit BUTTON outside the canvas area
  btn = Button(tk, height=1, text="exit", font=("Arial", 12, "bold"), command=terminate)
  btn.pack()
   
  #Retangulo mensagem sensor infravermelho
  #canvas.create_rectangle(5,160, 473, 275,fill=WHITE)
 
  #Verifica se o sensor infravermelho foi acionado
  #tk.after(100, checkPort)
   
  tk.mainloop()
  
def onObjectClick1(event):
  #Clique no botao 1
  global estado_1
  estado_1 = not estado_1
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
  if estado_3 == True:
      apagaled(40)
      apagaled(38)
      acendeled(36)
  if estado_3 == False:
      apagaled(36)
 
def checkPort():
    #Verifica se o sensor infravermelho foi acionado
    if GPIO.input(37) == False:
        #Cria retangulo em amarelo e exibe mensagem
        canvas.create_rectangle(10,165, 468, 270,fill=YELLOW)
        canvas.create_text(240, 220,  text="Liberar Porta", fill="BLACK", font=("Arial", 50, "bold"))
    if GPIO.input(37) == True:
        #Cria retangulo branco
        canvas.create_rectangle(5,160, 473, 275,fill=WHITE)
        canvas.create_text(240, 220,  text="Liberar Porta", fill='#E5E4E2', font=("Arial", 50, "bold"))
    tk.after(200,checkPort)
 
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