#Interface Gráfica Fechadura Biométrica
#Tela 1: Tela Inicial
#Especificações: Touchscreen LCD 3,5" 480x320
#Autor: Diego Vieira

import RPi.GPIO as GPIO
import time

from tkinter import *

GPIO.setmode(GPIO.BOARD)
 
#Definicao dos pinos do led RGB como saida
GPIO.setup(40, GPIO.OUT)
GPIO.setup(38, GPIO.OUT)
GPIO.setup(36, GPIO.OUT)
GPIO.setup(35, GPIO.OUT)
GPIO.setup(32, GPIO.OUT)
 
#Define o pino do sensor como entrada
GPIO.setup(37, GPIO.IN)
 
#Ativa Anodo Led RGB
GPIO.output(32, 1)
 
#Alimentacao sensor
GPIO.output(35, 1)
 
#Estado inicial dos leds
estado_1 = False
estado_2 = False
estado_3 = False
 
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

Define o tamanho da tela
WINDOW_W = 478
WINDOW_H = 280

#Definicao de cores padrao HEX COLOR
BLACK          = '#000000'
BRIGHTRED      = '#ff0000'
RED            = '#9b0000'
BRIGHTGREEN    = '#00ff00'
GREEN          = '#28A828'
BRIGHTBLUE     = '#0000ff'
BLUE           = '#00009b'
WHITE          = '#ffffff'
YELLOW         = '#ffff00'
