# Below is the programming exercise
# (Compute the volume of a cylinder) Write a program that reads in the radius and
# length of a cylinder and computes the area and volume

# prompts user to type in the radius and length a cylinder
radius=float(input("Enter the radius of the cylinder: "))
length=float(input("Enter the length of the cylinder: "))

# Calculation of the area
PI=3.142    # Introduction of Pie
area=radius*radius*PI

# Calculation of volume
volume=area*length

# Prints out both the volume and area of the cylinder
print("The area of the cylinder is ",area," while its volume is ",volume)