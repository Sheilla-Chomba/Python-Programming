# Below is the programming exercise
# Write a program that prompts the user to enter a point with
# x- and y-coordinates and determines whether the point is inside the triangle.

import math
# Prompts user to type in the points to check whether they are inside the triangle
x=eval(input("What is the x coordinate: "))
y=eval(input("What is the y coordinate: "))

horizontalDistance=math.sqrt(math.pow((x-0),2))
verticalDistance=math.sqrt(+math.pow((y-0),2))

if verticalDistance<=100:
    if horizontalDistance<=2*(100-verticalDistance):
        print(f"Point ({x}, {y}) is in the triangle.")
    else:
        print(f"Point ({x}, {y}) is not in the triangle.")

else:
    print(f"Point ({x}, {y}) is not in the triangle.")
