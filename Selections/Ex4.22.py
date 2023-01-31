# Below is the programming exercise
# (Geometry: point in a circle?) Write a program that prompts the user to enter a
# point (x, y) and checks whether the point is within the circle centered at (0, 0) with
# radius 10.

import math
# Prompts user to type in the points to check whether they are inside the circle
x=eval(input("What is the x coordinate: "))
y=eval(input("What is the y coordinate: "))

distance=math.sqrt(math.pow((x-0),2)+math.pow((y-0),2))

if distance<=10:
    print(f"Point ({x}, {y}) is in the circle.")

else:
    print(f"Point ({x}, {y}) is not in the circle.")