# Below is the programming exercise
# (Geometry: area of a pentagon) Write a program that prompts the user to enter the
# length from the center of a pentagon to a vertex and computes the area of the pentagon.

import math
# Prompts user to type in the length of the center of a pentagon
length=eval(input("Enter the length from the center a pentagon: "))

side=2*length*math.sin(math.pi/5)           # Formula for getting side of the pentagon
area=((3*(math.sqrt(3)))/2)*(side**2)       # Formula for getting area of the pentagon

print("The area of the pentagon is ",format(area,".2f"))