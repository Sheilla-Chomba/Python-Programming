# Below is the programming exercise
# (Game: heads or tails) Write a program that lets the user guess whether a flipped
# coin displays the head or the tail. The program randomly generates an integer 0 or
# 1, which represents head or tail. The program prompts the user to enter a guess
# and reports whether the guess is correct or incorrect.

import random
import time

print("We are going to play heads or tail."
      "\n Heads is represented by 0"
      "\n Tails is represented by 1")
time.sleep(2)

# Prompts user to type in their guess
guess=eval(input("Pick either heads or tail as per the instructions above: "))

while guess>1 or guess<0:
    guess = eval(input("Wrong input. Pick either heads or tail as per the instructions above: "))

gameGuess=random.randint(0,1)

if guess==gameGuess:
    print("You are correct.")
else:
    print("You are incorrect. Better luck next time.")