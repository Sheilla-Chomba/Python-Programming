# Below is a case study for guessing number game

from random import randint

compNumber=randint(0,100)

# Prompts user to type in their guess number
guessNumber=eval(input("Enter any number of your choice from 0-100: "))

while guessNumber!=compNumber:
    if (compNumber<guessNumber):
        print("\nYour guess is too high")
        guessNumber = eval(input("Wrong guess , Try again. Enter any number of your choice from 0-100: "))

    if(compNumber>guessNumber):
        print("\nYour guess is too low")
        guessNumber = eval(input("Wrong guess , Try again. Enter any number of your choice from 0-100: "))

    if(compNumber==guessNumber):
        print("\nYou are correct")
