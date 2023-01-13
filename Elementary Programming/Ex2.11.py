# Below is the programming exercise
# Write a program that prompts the user to enter final account value, annual interest
# rate in percent, and the number of years, and displays the initial deposit amount.

# Prompts user to type in the final account value, annual interest rate and number of years
finalAmt=eval(input("Enter the final amount of the investment: "))
annualInterest=eval(input("Enter the annual interest rate: "))
years=eval(input("Enter the number of years of investment: "))

monthlyInterest=annualInterest/12                       # Converting annual interest to monthly interest
months=years*12                                         # converting years to months

initialDeposit=finalAmt/((1+(monthlyInterest/100))**months)    # The formula to get initial deposit

print(f"The initial deposit of the investment is {initialDeposit}") # Prints out the initial deposit