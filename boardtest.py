import math
import sys
import time
import RPi.GPIO as GPIO

if __name__ == '__main__':

    def clean_up(): 
        for pin in pins:
            GPIO.output(pin, GPIO.LOW)
        GPIO.cleanup()

    pins = [ 4, 17, 27, 22, 5, 6, 13, 19, 26,
            21, 20, 16, 12, 25, 24, 23, 18, 15]

    GPIO.setmode(GPIO.BCM)

    SLEEP_TIME = 0.050

    for pin in pins:
        GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)
    try:
        for _ in range(1):
            for pin in pins:
                GPIO.output(pin, GPIO.HIGH)
                time.sleep(SLEEP_TIME)
                GPIO.output(pin, GPIO.LOW)
            for pin in reversed(pins):
                GPIO.output(pin, GPIO.HIGH)
                time.sleep(SLEEP_TIME)
                GPIO.output(pin, GPIO.LOW)
        clean_up()
    except KeyboardInterrupt:
        print ("\r\n" + sys.argv[0] + " SIGINT received - exiting")
        clean_up()
    sys.exit()
