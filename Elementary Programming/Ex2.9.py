# Below is the programming exercise
# Write a program that prompts the user to enter a temperature between -58°F and
# 41°F and a wind speed greater than or equal to 2 and displays the wind-chill temperature.

# Prompts user to type in the temperature and wind speed
outTemp=eval(input("Enter the temperature that is outside between -58 and 41 Fahrenheit: "))
windSpeed=eval(input("Enter the wind speed not less than 2mph: "))

# This is the formula to get the wind Temperature
windTemp=35.74 + (0.6215*outTemp) - (35.75*(windSpeed**0.16)) + (0.4275*outTemp*(windSpeed**0.16))

# Basically prints out the answer to the calculations
print(f"The wind chill index is {windTemp}")