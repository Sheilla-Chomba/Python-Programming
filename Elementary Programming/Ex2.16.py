# Below is the programming exercise
# Write a program that prompts the user to enter the starting velocity v0 in
# meters/second, the ending velocity v1 in meters/second, and the time span t in
# seconds, and displays the average acceleration.

# Prompts user to type in the starting velocity, ending velocity and time spent
startVelocity=eval(input("Enter the starting velocity: "))
endVelocity=eval(input("Enter the ending velocity: "))
time=eval(input("Enter the time spent from starting velocity to ending velocity: "))

acceleration=(endVelocity-startVelocity)/time   # The formula

print(f"The acceleration of the object is: {acceleration}")     # Prints out the results