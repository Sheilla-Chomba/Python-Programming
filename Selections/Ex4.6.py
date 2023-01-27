# Below is the programming exercise
# (Health application: BMI ) Revise Listing 4.6, ComputeBMI.py, to let users enter
# their weight in pounds and their height in feet and inches. For example, if a person
# is 5 feet and 10 inches, you will enter 5 for feet and 10 for inches.

import math
# Prompts user to type in their weight and height in imperial metrics
weight=eval(input("Enter your weight in pounds: "))
while weight<=0:
 weight = eval(input("Wrong input. Enter your weight in pounds: "))

print("\nType your height in feet and inches")
feet=eval(input("Feet: "))
while feet<=0:
 feet = eval(input("Wrong input. Feet: "))

inches=eval(input("Inches: "))
weightKgs=weight*0.45359237
feetToInches=feet*12
totInches=inches+feetToInches
heightMetres=totInches*0.0254

bmi=weightKgs/math.pow(heightMetres,2)

print("Your BMI is ",format(bmi,".2f"))
if bmi<18.5:
    print("You are underweight.")
elif bmi>=18.5 and bmi<25:
    print("You are healthy.")
elif bmi>=25 and bmi<30:
    print("You are overweight.")
else:
    print("You are obese.")