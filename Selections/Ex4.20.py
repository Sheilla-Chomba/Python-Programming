# Below is the programming exercise
# (Science: wind-chill temperature) Exercise 2.9 gives a formula to compute the
# wind-chill temperature. The formula is valid for temperatures in the range
# between -58°F and 41°F and for wind speed greater than or equal to 2. Write a
# program that prompts the user to enter a temperature and a wind speed. The program
# displays the wind-chill temperature if the input is valid; otherwise, it displays
# a message indicating whether the temperature and/or wind speed is invalid.

# Prompts user to type in the temperature and wind speed
outTemp=eval(input("Enter the temperature that is outside between -58 and 41 Fahrenheit: "))
if outTemp<-58 or outTemp>41:
    print("This is not valid. Please try again.")
else:
    windSpeed=eval(input("Enter the wind speed not less than 2mph: "))
    if windSpeed<2:
        print("This is not valid. Please try again.")
    else:
        # This is the formula to get the wind Temperature
        windTemp = 35.74 + (0.6215 * outTemp) - (35.75 * (windSpeed ** 0.16)) + (0.4275 * outTemp * (windSpeed ** 0.16))

        # Basically prints out the answer to the calculations
        print(f"The wind chill index is {windTemp}")
