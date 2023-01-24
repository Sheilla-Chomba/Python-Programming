# Below is a case study to compute Body Mass Index(BMI)

import math
# Prompts user to type in their weight and height
weight=eval(input("Enter your weight in pounds: "))
while weight<=0:
    weight = eval(input("Wrong input. Enter your weight in pounds: "))

height=eval(input("Enter your height in inches: "))
while height<=0:
    height=eval(input("Wrong input. Enter your height in inches: "))

weightKgs=weight*0.45359237
heightMetres=height*0.0254
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