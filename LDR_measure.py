import RPi.GPIO as GPIO
import time

port = 21

GPIO.setmode(GPIO.BCM)

while True:
    GPIO.setup(port, GPIO.OUT)
    GPIO.output(port, False)
    time.sleep(1)
    t1 = time.time()
    GPIO.setup(port, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    while GPIO.input(port) == False:
        print('reading')
    t2 = time.time()
    print('The time to charge the capacitor was: ', t2-t1)
    time.sleep(1)
    
    