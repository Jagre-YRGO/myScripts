#!/usr/bin/python3
'''
Program som räknar knapptryckningar mha GPIO.add_event_detect och callbacks
samtidigt som en LED blinkar med 0.5 Hz- och 50% duty-cycle
'''
#Importera lämpliga bibliotek (copy/paste från tidigare program)
import RPi.GPIO as GPIO
import time

#Deklarerar callback-funktion som räknar och skriver ut antal knapptryckningar
numOfPushes = 0

def minCallback(channel):
   global numOfPushes
   numOfPushes += 1
   print(numOfPushes)

def ledOn():
   GPIO.output(24, GPIO.HIGH)

def ledOff():
   GPIO.output(24, GPIO.LOW)


#'main'-program
#-initiera GPIO in/ut (copy paste från tidigare program)
GPIO.setmode(GPIO.BCM)
GPIO.setup(24,GPIO.OUT)
GPIO.setup(23,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(23, GPIO.RISING, callback=minCallback, bouncetime=200)

#-initiera call-back funktion mha GPIO.add_event_detect (se GC länk)
#Gå in i oändlig loop som blinkar LED
try:
   while True:
      ledOn()
      time.sleep(1)
      ledOff()
      time.sleep(1)
except KeyboardInterrupt:
   GPIO.cleanup()
