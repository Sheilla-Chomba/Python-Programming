# Below is the programming exercise
# (Game: scissor, rock, paper) Write a program that plays the popular scissor-rockpaper
# game. (A scissor can cut a paper, a rock can knock a scissor, and a paper can
# wrap a rock.) The program randomly generates a number 0, 1, or 2 representing
# scissor, rock, and paper. The program prompts the user to enter a number 0, 1, or
# 2 and displays a message indicating whether the user or the computer wins, loses,
# or draws.

import random
import time

print("...........We are playing Rock, Paper, Scissors.............")
time.sleep(1)
print("Rock will be represented as 0"
      "\nPaper will be represented as 1"
      "\nScissors will be represented as 2")
time.sleep(2)
# Prompts user to type in their choice
guess=eval(input("Type in your choice as per the instructions above: "))

while guess<0 or guess>2:
    guess = eval(input("Wrong input. Type in your choice as per the instructions above: "))

compGuess=random.randint(0,2)

if guess==0:
    if compGuess==0:
        print("The computer is rock. You are rock. It is a draw")
    if compGuess==1:
        print("The computer is paper. You are rock. The computer has won")
    if compGuess==2:
        print("The computer is scissors. You are rock. You have won")
if guess==1:
    if compGuess==0:
        print("The computer is rock. You are paper. You have won")
    if compGuess==1:
        print("The computer is paper. You are paper. It is a draw")
    if compGuess==2:
        print("The computer is scissors. You are paper. The computer has won")
if guess==2:
    if compGuess==0:
        print("The computer is rock. You are scissors. The computer has won")
    if compGuess==1:
        print("The computer is paper. You are scissors. You have won")
    if compGuess==2:
        print("The computer is scissors. You are scissors. It is a draw")
