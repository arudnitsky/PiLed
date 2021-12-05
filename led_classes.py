#!/usr/bin/python3
import math
import sys
import time
import RPi.GPIO as GPIO

"""
class Led:
    duty_cycle
    _gpio_channel
    _pwm

    init(_gpio_channel):
        duty_cycle=0
        pwm=GPIO.PWM(gpio_channel, 100) # not sure what the 100 is. Hz?
        pwm.ChangeDutyCycle(duty_cycle)
        pwm.start()

    def set_brightness(brightness):
        # can I clamp brightness to 0..100?
        _duty_cycle = brightness
        if brightness = 0
            GPIO.
        pwm
"""

def ease_inout_quint(x):
    return 16 * math.pow(x, 5) if x < 0.5 else 1 - math.pow(-2 * x + 2, 5) / 2

def ease_in_expo(x):
    return 0 if x == 0 else math.pow(2, 10 * x - 10)

def ease_out_expo(x):
    return 1 if x == 1 else 1 - math.pow(2, -10 * x)

def ramp_down():
    duty_cycle=100
    while (duty_cycle != 0):
        time.sleep(.015)
        duty_cycle = duty_cycle - 1
        pwm.ChangeDutyCycle(duty_cycle)

def clean_up():
    global pwm
    pwm.stop()
    GPIO.output(pin, GPIO.LOW)
    GPIO.cleanup()

def blink():
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(.1)
    GPIO.output(pin, GPIO.LOW)
    time.sleep(.1)

def pulse():
    for rampIndex in range(100, 0, -1):
        global pwm
        dutyCycle = int(ease_in_expo(rampIndex/100) * 100)
        pwm.ChangeDutyCycle(dutyCycle)
        time.sleep(0.01)

def init(gpio_pin):
    global pin
    pin = gpio_pin
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)
    
def init_pwm():
    global pin
    global pwm
    pwm = GPIO.PWM(pin, 100)
    pwm.start(100)
    
if __name__ == '__main__':

    try:
        init(26)
        for _ in range(3):
            blink()
            time.sleep(.75)
        init_pwm()
        for _ in range(3):
            pulse()
            time.sleep(.1)

    except KeyboardInterrupt:
        print ("\r\n" + sys.argv[0] + " SIGINT received - exiting")

    clean_up()
    sys.exit()
