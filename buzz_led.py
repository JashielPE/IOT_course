led1 = 21
buzz = 20

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(led1, GPIO.OUT)
GPIO.setup(buzz, GPIO.OUT)
while True:
    GPIO.output(led1, True)
    time.sleep(0.4)
    GPIO.output(led1, False)
    time.sleep(0.4)
    GPIO.output(buzz, True)
    time.sleep(3)
    GPIO.output(buzz, False)
    time.sleep(2)