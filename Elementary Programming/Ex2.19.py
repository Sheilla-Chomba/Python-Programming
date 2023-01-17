# Below is the programming exercise
# Financial application: calculate future investment value) Write a program that
# reads in an investment amount, the annual interest rate, and the number of years,
# and displays the future investment value

# Prompts user to type in the initial amount of investment, time for the investment and its interest rate
initialAmt=eval(input("Enter the initial amount of investment: "))
interestRate=eval(input("Enter the interest rate of the investment: "))
years=eval(input("Enter the years for the investment: "))

monthsRate=interestRate/1200
months=years*12

finalAmt=initialAmt*((1+monthsRate)**months)        # The formula

print(f"The accumulated value is: {finalAmt}")