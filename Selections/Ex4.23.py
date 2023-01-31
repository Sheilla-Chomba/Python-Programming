# Below is the programming exercise
# (Geometry: point in a rectangle?) Write a program that prompts the user to enter
# a point (x, y) and checks whether the point is within the rectangle centered at
# (0, 0) with width 10 and height 5.

import math
# Prompts user to type in the points to check whether they are inside the rectangle
x=eval(input("What is the x coordinate: "))
y=eval(input("What is the y coordinate: "))

horizontalDistance=math.sqrt(math.pow((x-0),2))
verticalDistance=math.sqrt(+math.pow((y-0),2))

if horizontalDistance<=(10/2):
    if verticalDistance<=(5/2):
        print(f"Point ({x}, {y}) is in the rectangle.")
    else:
        print(f"Point ({x}, {y}) is not in the rectangle.")

else:
    print(f"Point ({x}, {y}) is not in the rectangle.")