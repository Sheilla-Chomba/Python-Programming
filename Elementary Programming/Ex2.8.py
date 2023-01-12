# Below is the programming exercise
# (Science: calculate energy) Write a program that calculates the energy needed to
# heat water from an initial temperature to a final temperature. Your program should
# prompt the user to enter the amount of water in kilograms and the initial and final
# temperatures of the water.

# Prompts user to type in the amount of water in kilograms, the initial temperature
# and the final temperature
weightWater=eval(input("Enter the weight of water in Kilograms: "))
initialTemp=eval(input("Enter the initial temperature of the water: "))
finalTemp=eval(input("Enter the final temperature of the water: "))

energy=weightWater*(finalTemp-initialTemp)*4184 # The formula to get the energy used

print(f"The energy needed to heat the water is {energy}") # Prints out the results