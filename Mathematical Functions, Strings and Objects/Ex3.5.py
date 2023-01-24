# Below is the programming exercise
# Write a program that prompts the user to enter the
# number of sides and their length of a regular polygon and displays its area.

import math
# Prompts user to type in the length of the sides of the polygon and its number of sides
numberSides=eval(input("Enter the number of sides of the polygon: "))
lengthSides=eval(input("Enter the length of each side of the polygon: "))

# The formula
area=(numberSides*math.pow(lengthSides,2))/(4*math.tan(math.pi/numberSides))

print("The area of the polygon is ",format(area,".2f"))