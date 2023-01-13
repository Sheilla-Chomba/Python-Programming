# Below is the programming exercise
# Write a program that prompts the user to enter v in meters/second (m/s) and the
# acceleration a in meters/second squared and displays the minimum runway length.

# Prompts user to type in the speed and acceleration of the plane
speed=eval(input("Enter the speed of the plane in m/s: "))
acceleration=eval(input("Enter the acceleration of the plane in m/s^2: "))

length=(speed**2)/(2*acceleration)              # The formula

print(f"The minimum runway length is {length}") # The product of the calculation