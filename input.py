led1 = 21
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(led1, GPIO.OUT)
GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_UP)
cnt=0
while cnt<5:
    if GPIO.input(20):
        GPIO.output(led1, True)
        time.sleep(0.2)
    else:
        GPIO.output(led1, False)
        cnt+=1
        print('Pressing switch')
        time.sleep(0.2)

print('ending program')

