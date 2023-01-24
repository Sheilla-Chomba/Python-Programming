# Below is the programming exercise
# Write a program that prompts the user to enter the latitude and longitude of two
# points on the earth in degrees and displays its great circle distance.

import math
import time
# Prompts user to type in the latitudes and longitudes of point 1 and 2
print("Kindly enter the values of point 1 and point 2. ",
      "\nIf the values are in East and South, be sure to put negative symbol before the values.")
time.sleep(5)     # This lets the program wait for a few seconds before running the next codes
latitude1=eval(input("Enter the latitude of point 1: "))
longitude1=eval(input("Enter the longitude of point 1: "))
latitude2=eval(input("Enter the latitude of point 2: "))
longitude2=eval(input("Enter the longitude of point 2: "))

# The formula
distance=6371.01*math.acos((math.sin(math.radians(latitude1))*math.sin(math.radians(latitude2)))+(math.cos(math.radians(latitude1))*math.cos(math.radians(latitude2))*math.cos(math.radians(longitude1-longitude2))))

print(f"The distance between the two points is {distance} km")