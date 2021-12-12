import sys
import threading
import time
import RPi.GPIO as GPIO
from led import Led

class Controller:

    def __init__(self, pins):
        print("Controller init")
        self.leds = []
        print(self.leds)
        for pin in pins:
            led = Led(pin)
            self.leds.append(led)
            print("Added ", led.pin)

    def shut_down(self):
        for led in self.leds:
            led.shut_down()

    def test_pins(self):
        threads = list()
        for led in self.leds:
            x = threading.Thread(target=(lambda l: l.pulse()), args=(led,))
            threads.append(x)
            x.start()

        for index, thread in enumerate(threads):
            thread.join()

if __name__ == '__main__':

    pins = [ 4, 17, 27, 22, 5, 6, 13, 19, 26,
             21, 20, 16, 12, 25, 24, 23, 18, 15]
    GPIO.setmode(GPIO.BCM)

    controller = Controller(pins)

    print("Controller finished init")

    try:
        while True:
            controller.test_pins()
    except KeyboardInterrupt:
        print ("\r\n" + sys.argv[0] + " SIGINT received - exiting")

    controller.shut_down()
    GPIO.cleanup()
    sys.exit()

