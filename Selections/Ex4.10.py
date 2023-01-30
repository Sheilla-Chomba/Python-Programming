# Below is the programming exercise
# (Game: multiplication quiz) Listing 4.4, SubtractionQuiz.py, randomly generates
# a subtraction question. Revise the program to randomly generate a multiplication
# question with two integers less than 100.

import random

number1=random.randint(0,99)
number2=random.randint(0,99)

# Prompts user to type in the answer to the question
answer=eval(input(f" What is {number1} * {number2} = "))

if answer==(number1*number2):
    print("You are correct.")
else:
    print("Incorrect. Try Again.")