# Below is the programming exercise
# Write a program that prompts
# the user to enter a weight in pounds and height in inches and displays the BMI.

# Prompts user to type in weight in pounds and inches
weightPounds=eval(input("Enter your weight in pounds: "))
heightInches=eval(input("Enter your height in inches: "))

# Converting height to metres and pounds to kilograms
weightKgs=weightPounds*0.45359237
heighMetres=heightInches*0.0254

bmi=weightKgs/(heighMetres**2)      # The formula

print(f"Your BMI is: {bmi}")        # prints out the results