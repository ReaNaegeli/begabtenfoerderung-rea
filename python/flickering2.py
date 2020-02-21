# PWM2.py
# Set RGB color

import RPi.GPIO as GPIO
import time
import random

P_RED = 11    # adapt to your wiring
P_GREEN = 13   # ditto
P_BLUE = 15    # ditto
fPWM = 50      # Hz (not higher with software PWM)

def setup():
    global pwmR, pwmG, pwmB
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(P_RED, GPIO.OUT)
    GPIO.setup(P_GREEN, GPIO.OUT)
    GPIO.setup(P_BLUE, GPIO.OUT)
    pwmR = GPIO.PWM(P_RED, fPWM)
    pwmG = GPIO.PWM(P_GREEN, fPWM)
    pwmB = GPIO.PWM(P_BLUE, fPWM)
    pwmR.start(0)
    pwmG.start(0)
    pwmB.start(0)
    
def setColor(r, g, b):
    pwmR.ChangeDutyCycle(int(r / 255 * 100))
    pwmG.ChangeDutyCycle(int(g / 255 * 100))
    pwmB.ChangeDutyCycle(int(b / 255 * 100))
    
print ("starting")
setup()
while True:
    r = random.randint(0, 200)
    g = random.randint(0, 100)
    b = random.randint(0, 0)
    print (r, g, b)
    setColor(r, g, b)
    time.sleep(0.2)