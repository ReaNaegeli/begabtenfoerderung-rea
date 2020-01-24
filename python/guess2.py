# import functions
import random
import time;
# define range of the number
randomNumber = random.randrange(0,10)

# print start text
print("Random number has been generated")

# define Variable         
guessed = False
startTime = time.time()
tries = 0


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
    elif userInput>10:
        print("Our guess range is between 0 and 10, please try a bit lower")
    elif userInput<0:
        print("Our guess range is between 0 and 10, please try a bit higher")
    elif userInput>randomNumber:
        print("Try one more time, a bit lower")
    elif userInput < randomNumber:
        print("Try one more time, a bit higher")

# finish the program
print("End of program")