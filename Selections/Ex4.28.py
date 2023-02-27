# Below is the programming exercise
# (Geometry: two rectangles) Write a program that prompts the user to enter the
# center x-, y-coordinates, width, and height of two rectangles and determines
# whether the second rectangle is inside the first or overlaps with the first

import math
# Prompts user to type in the coordinates of the center of the bigger rectangle, its width and its height
Xbig=eval(input("Enter the x coordinate of the center of the bigger rectangle: "))
Ybig=eval(input("Enter the y coordinate of the center of the bigger rectangle: "))
widthBig=eval(input("Enter the width of the bigger rectangle: "))
heightBig=eval(input("Enter the height of the bigger rectangle: "))

# Prompts user to type in the coordinates of the center of the smaller rectangle, its width and its height
Xsmall=eval(input("Enter the x coordinate of the center of the smaller rectangle: "))
Ysmall=eval(input("Enter the y coordinate of the center of the smaller rectangle: "))
widthSmall=eval(input("Enter the width of the smaller rectangle: "))
heightSmall=eval(input("Enter the height of the smaller rectangle: "))

horizontalDist=math.sqrt(math.pow((x-0),2))