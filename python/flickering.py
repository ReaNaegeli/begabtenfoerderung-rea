# PWM1.py
# LED dimming

import RPi.GPIO as GPIO
import time
import random

P_LED = 11 # adapt to your wiring
fPWM = 50  # Hz (not higher with software PWM)

def setup():
    global pwm
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(P_LED, GPIO.OUT)
    pwm = GPIO.PWM(P_LED, fPWM)
    pwm.start(0)
    
print ("starting")
setup()
duty = 0
#isIncreasing = True
while True:
    duty = random.randint(0, 90)
    sleeptime = random.randint(0, 15)
    pwm.ChangeDutyCycle(duty)
    print ("D =", duty, "%")
    #duty += 10
    
    time.sleep(sleeptime / 100)