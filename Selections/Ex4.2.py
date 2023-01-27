# Below is the programming exercise
# (Game: add three numbers) The program in Listing 4.1 generates two integers and
# prompts the user to enter the sum of these two integers. Revise the program to generate
# three single-digit integers and prompt the user to enter the sum of these three
# integers.

import random

number1=random.randint(0,9)
number2=random.randint(0,9)
number3=random.randint(0,9)
sum=number1+number2+number3

# Prompts user to type in their answer
answer=eval(input(f"What is: \n\t {number1} + {number2} + {number3} = "))

if answer==sum:
    print("You are correct.")

else:
    print("Wrong answer. Kindly try again.")