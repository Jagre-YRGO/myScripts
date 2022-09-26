#!/usr/bin/python3

import RPi.GPIO as GPIO
import time



GPIO.setmode(GPIO.BCM)
GPIO.setup(24,GPIO.OUT) #använd GPIO24 för LED som ut-port
GPIO.setup(23,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.output(24,GPIO.HIGH)
time.sleep(1)
print('welcome!')
GPIO.output(24,GPIO.LOW)

try:
   while True:
      #om knapp tryckt -> tänd LED
      if GPIO.input(23) == GPIO.HIGH:
         GPIO.output(24,GPIO.HIGH)
      #annars -> släckt LED
      else:
         GPIO.output(24,GPIO.LOW)
except KeyboardInterrupt:
   GPIO.cleanup()



