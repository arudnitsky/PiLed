import sys
import time
import RPi.GPIO as GPIO
import easings as ea

class Led:
    def __init__(self, pin):
        self.pin = pin
        self.dutyCycle = 0
        GPIO.setup(self.pin, GPIO.OUT, initial=GPIO.LOW)
        self.pwm = GPIO.PWM(pin, 100) # 100Hz

    def start(self):
        self.pwm.start(self.dutyCycle)

    def stop(self):
        self.pwm.stop()

    def shut_down(self):
        self.pwm.stop()
        GPIO.output(self.pin, GPIO.LOW)

    def set_brightness(self, brightness):
        self.dutyCycle = brightness
        if (self.dutyCycle == 0):
            self.pwm.stop()
            #GPIO.output(self.pin, GPIO.LOW)
        else:
            self.pwm.start(self.dutyCycle)
            self.pwm.ChangeDutyCycle(self.dutyCycle)

    def ramp_updown(self):
        for rampIndex in range(0, 101, 1):
            brightness = int(ea.ease_in_expo(rampIndex/100) * 100)
            self.set_brightness(brightness)
            time.sleep(0.01)
        for rampIndex in range(100, -1, -1):
            brightness = int(ea.ease_in_expo(rampIndex/100) * 100)
            self.set_brightness(brightness)
            time.sleep(0.01)

    def pulse(self):
        for rampIndex in range(100, 0, -1):
            brightness = int(ea.ease_in_expo(rampIndex/100) * 100)
            self.set_brightness(brightness)
            time.sleep(0.01)

if __name__ == '__main__':
    try:
        GPIO.setmode(GPIO.BCM)
        led = Led(26)
        led.start()
        led.pulse()
        led.set_brightness(0)
        time.sleep(2)

        for _ in range(30):
            led.ramp_updown();
            #led.pulse()

#        for brightness in [0, 25, 50, 75, 100, 75, 100, 75, 100, 75, 100]:
#            print("brightess:", brightness)
#            led.set_brightness(brightness)
#            time.sleep(.5)

#        for _ in range(3):
#            led.ramp_down()
#            time.sleep(.3)
#
        led.stop()

    except KeyboardInterrupt:
        print ("\r\n" + sys.argv[0] + " SIGINT received - exiting")

    GPIO.cleanup()
    sys.exit()
