#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
PyFingerprint
Copyright (C) 2015 Bastian Raschke <bastian.raschke@posteo.de>
All rights reserved.

"""
import RPi.GPIO as GPIO
import time 
import hashlib
from pyfingerprint.pyfingerprint import PyFingerprint

GPIO.setmode (GPIO.BOARD)
GPIO.setup (38,GPIO.OUT) ## led vermelho
GPIO.setup (40,GPIO.OUT) ## pino de ativação da trava
tempo=1

## Search for a finger
##

## Tries to initialize the sensor
def example_new():
    try:
        f = PyFingerprint('/dev/ttyUSB0', 57600, 0xFFFFFFFF, 0x00000000)

        if ( f.verifyPassword() == False ):
           raise ValueError('The given fingerprint sensor password is wrong!')
           GPIO.output(40,1)
           time.sleep(tempo)
           GPIO.output(40,0)
           time.sleep(tempo)
           GPIO.output(40,1)
           time.sleep(tempo)
           GPIO.output(40,0)

    except Exception as e:
        print('The fingerprint sensor could not be initialized!')
        print('Exception message: ' + str(e))
        exit(1)

## Gets some sensor information
print('Currently used templates: ' + str(f.getTemplateCount()) +'/'+ str(f.getStorageCapacity()))

## Tries to search the finger and calculate hash
try:
    print('Waiting for finger...')

    ## Wait that finger is read
    while ( f.readImage() == False ):
        pass

    ## Converts read image to characteristics and stores it in charbuffer 1
    f.convertImage(0x01)

    ## Searchs template
    result = f.searchTemplate()

    G

    positionNumber = result[0]
    accuracyScore = result[1]

    if ( positionNumber == -1 ):
        print('No match found!')
        GPIO.output(40,1)
        time.sleep(tempo)
        GPIO.output(40,0)
        time.sleep(tempo)
        GPIO.output(40,1)
        time.sleep(tempo)
        GPIO.output(40,0)
        
        exit(0)
        
    else: 
        GPIO.output(38,1)
        print('Found template at position #' + str(positionNumber))
        print('The accuracy score is: ' + str(accuracyScore))
        time.sleep(tempo)
        GPIO.output(38,0)

    ## OPTIONAL stuff
    ##

    ## Loads the found template to charbuffer 1
    f.loadTemplate(positionNumber, 0x01)

    ## Downloads the characteristics of template loaded in charbuffer 1
    characterics = str(f.downloadCharacteristics(0x01)).encode('utf-8')

    ## Hashes characteristics of template
    print('SHA-2 hash of template: ' + hashlib.sha256(characterics).hexdigest())

except Exception as e:
    print('Operation failed!')
    print('Exception message: ' + str(e))
    exit(1)

