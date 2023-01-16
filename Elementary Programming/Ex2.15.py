# Below is the programming exercise
# (Geometry: area of a hexagon) Write a program that prompts the user to enter the
# side of a hexagon and displays its area.

# Prompts user to type in length of the sides in the hexagon
side=eval(input("Enter the length of the side of the hexagon: "))

# The formula
area=((((3)**0.5)*3)/2)*(side**2)

print(f"The area of the hexagon is: {area}")        # Prints out the results