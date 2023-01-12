# Below is the programming exercise
# (Convert pounds into kilograms) Write a program that converts pounds into
# kilograms. The program prompts the user to enter a value in pounds, converts it to
# kilograms, and displays the result.

# Prompts user to type in weight in pounds
# It is better to use eval rather than all other data types because it might be hard to predict what the user types in
# The conversion is made because all that is typed in by user is presumed to be in string form
pounds=eval(input("Enter the weight in pounds: "))

# Converts the weight from pounds to kgs
kgs=pounds*0.454

# prints out the results of the conversion
print("The weight in Kilograms is: ",kgs)