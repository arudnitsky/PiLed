#!/usr/bin/python
import sys
from time import sleep
import RPi.GPIO as GPIO

LED_PIN = 32

GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED_PIN,GPIO.OUT,initial=GPIO.LOW)

print(sys.argv[0] + " starting")
try:
    while True:
        GPIO.output( LED_PIN ,GPIO.HIGH)
        sleep(.5)
        GPIO.output( LED_PIN ,GPIO.LOW)
        sleep(.5)
except KeyboardInterrupt:
    print("\r\n" + sys.argv[0] + " SIGINT received - exiting")
    GPIO.output( LED_PIN, GPIO.LOW)
    GPIO.cleanup()

