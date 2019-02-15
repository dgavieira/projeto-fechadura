#!/usr/bin/env python
# -*- coding: utf-8 -*-
#parece ser o codigo do dedo
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
GPIO.setup (18,GPIO.OUT)
GPIO.setup (16,GPIO.OUT)
tempo=1.5

## Search for a finger
##

## Tries to initialize the sensor
try:
    f = PyFingerprint('/dev/ttyUSB0', 57600, 0xFFFFFFFF, 0x00000000)

    if ( f.verifyPassword() == False ):
        raise ValueError('The given fingerprint sensor password is wrong!')
        GPIO.output(16,1)
        time.sleep(tempo)
        GPIO.output(16,0)
        GPIO.output(16,1)
        time.sleep(tempo)
        GPIO.output(16,0)

except Exception as e:
    print('The fingerprint sensor could not be initialized!')
    print('Exception message: ' + str(e))
    GPIO.output(16,1)
    time.sleep(0.5)
    GPIO.output(16,0)
    time.sleep(0.5)
    GPIO.output(16,1)
    time.sleep(0.5)
    GPIO.output(16,0)
    
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

    positionNumber = result[0]
    accuracyScore = result[1]

    if ( positionNumber == -1 ):
        GPIO.output(16,1)
        time.sleep(tempo)
        GPIO.output(16,0)
        GPIO.output(16,1)
        time.sleep(tempo)
        GPIO.output(16,0)
 
        print('No match found!')
        exit(0)
        
    else: 
        GPIO.output(18,1)
        print('Found template at position #' + str(positionNumber))
        print('The accuracy score is: ' + str(accuracyScore))
        time.sleep(tempo)
        GPIO.output(18,0)

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