import time
import sys
import RPi.GPIO as GPIO
from led import Led

class Controller:

    def __init__(self, pins):
        self.leds = []
        GPIO.setmode(GPIO.BCM)
        for pin in pins:
            self.leds.append(Led(pin))

    def shut_down(self):
        for led in self.leds:
            led.shut_down()
        GPIO.cleanup()

    def test_pins(self):
        for led in self.leds:
            led.start()
            led.pulse()
            led.stop()

if __name__ == '__main__':

    pins = [ 4, 17, 27, 22, 5, 6, 13, 19, 26,
            21, 20, 16, 12, 25, 24, 23, 18, 15]


    controller = Controller(pins)

    try:
        controller.test_pins()
    except KeyboardInterrupt:
        print ("\r\n" + sys.argv[0] + " SIGINT received - exiting")

    controller.shut_down()
    sys.exit()
