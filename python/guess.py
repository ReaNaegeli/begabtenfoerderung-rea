# Imports
from random import *

# Start and first message
print("Herzlich wilkommen zum Spiel Zahlenraten")

# generate random number
toGuess = randint(1, 20)

# debugging
print (toGuess)

# Userimput
print("Bitte gebe eine Zahl zwischen 1 und 20 ein")
guess = int(input(">> "))

# debugging
# print (guess)

# if toGuess = guess
if toGuess == guess:
    print ("Super du hast die Zahl erraten!")