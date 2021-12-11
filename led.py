import math
import sys
import time
import RPi.GPIO as GPIO

def ease_inout_quint(x):
    return 16 * math.pow(x, 5) if x < 0.5 else 1 - math.pow(-2 * x + 2, 5) / 2

def ease_in_expo(x):
    return 0 if x == 0 else math.pow(2, 10 * x - 10)

def ease_out_expo(x):
    return 1 if x == 1 else 1 - math.pow(2, -10 * x)

class Led:
    def __init__(self, pin):
        print(f'constructor call with arg {pin}' )
        self.pin = pin
        GPIO.setup(self.pin, GPIO.OUT, initial=GPIO.LOW)
        self.pwm = GPIO.PWM(pin, 100)
        self.pwm.start(0)

    def __del__(self):
        self.stop()

    def stop(self):
        self.pwm.stop()
        GPIO.output(self.pin, GPIO.LOW)

    def ramp_down(self):
        self.duty_cycle=100
        while (self.duty_cycle != 0):
            time.sleep(.015)
            self.duty_cycle = self.duty_cycle - 1
            self.pwm.ChangeDutyCycle(self.duty_cycle)

    def set_brightness(self, brightness):
        self.dutyCycle = brightness
        if (self.dutyCycle == 0):
            GPIO.output(self.pin, GPIO.LOW)
            self.pwm.stop
        else:
            self.pwm.ChangeDutyCycle(self.dutyCycle)

    def pulse(self):
        for rampIndex in range(100, 0, -1):
            brightness = int(ease_in_expo(rampIndex/100) * 100)
            self.set_brightness(brightness)
            time.sleep(0.01)

if __name__ == '__main__':
    try:
        GPIO.setmode(GPIO.BCM)
        led = Led(26)
        for _ in range(3):
            led.pulse()
            time.sleep(.3)

    except KeyboardInterrupt:
        print ("\r\n" + sys.argv[0] + " SIGINT received - exiting")

    GPIO.cleanup()
    sys.exit()
