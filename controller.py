import Led

class Controller:
    
    def __init__(self, pins):
        GPIO.setmode(GPIO.BCM)
        for pin in pins
            leds.append( Led(pin) );

   def __del__(self):
        for led in self.leds:
            GPIO.output(led.pin, GPIO.LOW)
        GPIO.cleanup()

if __name__ == '__main__':

    pins = [ 4, 17, 27, 22, 5, 6, 13, 19, 26,
            21, 20, 16, 12, 25, 24, 23, 18, 15]

    controller = Controller(pins)

    SLEEP_TIME = 0.050

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
