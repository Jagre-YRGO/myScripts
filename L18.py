#!/usr/bin/python3

import RPi.GPIO as GPIO
import time
import threading
import queue

GPIO_PORT24 = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_PORT24,GPIO.OUT)

q = queue.Queue()

def blinkFunktion():
   try:
      while True:
         time.sleep(0.25)
         GPIO.output(GPIO_PORT24, GPIO.HIGH)
         time.sleep(0.25)
         GPIO.output(GPIO_PORT24, GPIO.LOW)
         #om kö ej tom
         #kontrollera om en nolla mottagits - avbryt isf loop
         if not(q.empty()):
            if ('0' == q.get()):
               break
    
   except KeyboardInterrupt:
      GPIO.cleanup()

def keyboardInput():
   try:
      while True:
         myString = input("Just type something!")
         print(myString)
         #om myString är en nolla - meddela blinkFunktion och avbryt loop
         q.put(myString)
         if myString == '0':
            break
   except KeyboardInterrupt:
      GPIO.cleanup()

t1 = threading.Thread(target=blinkFunktion)
t2 = threading.Thread(target=keyboardInput)

t1.start()
t2.start()

t1.join()
t2.join()
