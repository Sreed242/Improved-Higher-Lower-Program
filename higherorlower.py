# Welcome to my code

score = 0
end = False
import random

digInp = int(input("How many digits do you want?   "))
digFin = digInp 
# Error handling for 1 or illegal digit numbers
if digFin == 1 or digFin < 1:
    ranInt= random.randint(0,9)
    if digFin < 1:
        print("Illegal int detected, defauling to 1 digit")
# General random number generator
elif digFin != 0:
    digHan = 10 ** digFin
    highDig = digHan
    lowHan = digFin -1
    lowDig = 10 ** lowHan
    fhDig = highDig - 1
    ranInt = random.randint(lowDig,highDig)
# Game start
while end == False:
    userGuess = int(input("What is your guess?   "))
    if userGuess < ranInt:
        print("The number is higher, try again   ")
    elif userGuess > ranInt:
        print("The number is lower, try again   ")
    elif userGuess == ranInt:
        print("Congrats you won!!   ")
        break