#!/usr/bin/python
import sys
from time import sleep
import RPi.GPIO as GPIO

ledPin = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin,GPIO.OUT,initial=GPIO.LOW)

print sys.argv[0] + " starting"
try:
   while True:
      GPIO.output( ledPin ,GPIO.HIGH)
      sleep(.5)
      GPIO.output( ledPin ,GPIO.LOW)
      sleep(.5)
except KeyboardInterrupt:
   print "\r\n" + sys.argv[0] + " SIGINT received - exiting"
   GPIO.output( ledPin, GPIO.LOW)
   GPIO.cleanup()
 
