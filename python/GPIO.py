import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

P_LED = 11 # adapt to GPIO 17


def blinkLed(count) :
    for i in range(0,count):    
        GPIO.output(17, 1)
        time.sleep (0.5)
        GPIO.output(17, 0)
        time.sleep (0.5)

blinkLed(3)
time.sleep(2)
blinkLed(3)
time.sleep (2)
blinkLed()


GPIO.cleanup()



