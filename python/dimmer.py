# PWM1.py
# LED dimming

import RPi.GPIO as GPIO
import time

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
isIncreasing = True
while True:
    pwm.ChangeDutyCycle(duty)
    print ("D =", duty, "%")
    if isIncreasing:
        duty += 1
    else:
        duty -= 1
    if duty == 100:
        isIncreasing = False
    if duty == 0:
        isIncreasing = True
    time.sleep(0.01)