# Below is the programming exercise
# Write a program that prompts the user to enter the
# three points (x1, y1), (x2, y2), and (x3, y3) of a triangle and displays its area.

# Prompts user to type in the coordinates of the triangle
x1=eval(input("Enter x1 coordinates: "))
y1=eval(input("Enter y1 coordinates: "))
x2=eval(input("Enter x2 coordinates: "))
y2=eval(input("Enter y2 coordinates: "))
x3=eval(input("Enter x3 coordinates: "))
y3=eval(input("Enter y3 coordinates: "))

# Using the coordinates, we are now going to get the length of each side
side1=(((x2-x1)**2)+((y2-y1)**2))**0.5
side2=(((x3-x2)**2)+((y3-y2)**2))**0.5
side3=(((x1-x3)**2)+((y1-y3)**2))**0.5

Tsize=(side1+side2+side3)/2
# The formula for the area
area=(Tsize*(Tsize-side1)*(Tsize-side2)*(Tsize-side3))**0.5

print(f"The area of the triangle is: {area}")
