# Below is the programming exercise
# Game: learn addition) Write a program that generates two integers under 100 and
# prompts the user to enter the sum of these two integers. The program then reports
# true if the answer is correct, false otherwise. The program is similar to Listing 4.1.

import random

number1=random.randint(0,99)
number2=random.randint(0,99)
sum=number1+number2

# Prompts user to type in their answer
answer=eval(input(f"What is: \n\t {number1} + {number2} = "))

if answer==sum:
    print("True")

else:
    print("False")