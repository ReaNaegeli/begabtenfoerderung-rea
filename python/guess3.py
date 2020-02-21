# import functions
import random
import RPi.GPIO as GPIO
import time

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
    
# define range of the number
randomNumber = random.randrange(0,10)

# print start text
print("Random number has been generated")

# define Variable         
guessed = False
startTime = time.time()
tries = 0
setup()

# start the Game
while guessed==False:
    tries += 1
    # read guess from player and check the input
    userInput = int(input("Your guess please: "))
    if userInput==randomNumber:
        guessed = True
        stopTime = time.time()
        usedTime = stopTime - startTime
        print("it took you ", (round(usedTime, 0)), "seconds")
        print ("you needed ",(tries),"attempts")
        print("Well done!")
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        setColor(r, g, b)
        time.sleep(1)
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        setColor(r, g, b)
        time.sleep(1)
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        setColor(r, g, b)
        time.sleep(1)
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        setColor(r, g, b)
        time.sleep(1)
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        setColor(r, g, b)
        time.sleep(1)
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        setColor(r, g, b)
        time.sleep(1)
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        setColor(r, g, b)
        time.sleep(1)
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        setColor(r, g, b)
        time.sleep(1)
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        setColor(r, g, b)
        time.sleep(1)
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        setColor(r, g, b)
        time.sleep(1)
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        setColor(r, g, b)
        time.sleep(1)
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        setColor(r, g, b)
        time.sleep(1)
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        setColor(r, g, b)
        time.sleep(1)
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        setColor(r, g, b)
        time.sleep(1)
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        setColor(r, g, b)
        time.sleep(1)
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        setColor(r, g, b)
        time.sleep(1)
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        setColor(r, g, b)
        time.sleep(1)
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        setColor(r, g, b)
        time.sleep(1)
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        setColor(r, g, b)
        time.sleep(1)
        r = random.randint(0, 255)                    
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        setColor(r, g, b)
        time.sleep(1)                    
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        setColor(r, g, b)
        time.sleep(0)
    elif userInput>10:
        print("Our guess range is between 0 and 10, please try a bit lower")
        setColor(255, 255, 255)
        time.sleep(0.1)
    elif userInput<0:
        print("Our guess range is between 0 and 10, please try a bit higher")
        setColor(0, 255, 100)
        time.sleep(0.1)
    elif userInput>randomNumber:
        print("Try one more time, a bit lower")
        setColor(225, 120, 0)
        time.sleep(0.1)
        #blinkLed(1)
    elif userInput < randomNumber:
        print("Try one more time, a bit higher")
        setColor(255, 0, 255)
        time.sleep(0.1)
        #blinkLed(2)

# finish the program
print("End of program")