# Below is the programming exercise
# Write a program that prompts the user to enter the side of a pentagon and displays
# the area.

import math
# Prompts user to type in the length of the sides of the pentagon
side=eval(input("Enter the length of the side o the pentagon: "))

area=(5*(side**2))/(4*(math.tan(math.pi/5)))        # The formula

print("The area of the pentagon is ",format(area,".2f"))    # Prints out the formula