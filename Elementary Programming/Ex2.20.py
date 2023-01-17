# Below is the programming exercise
# Write a program that reads the balance and the annual percentage interest rate
# and displays the interest for the next month.

# Prompts user to type in the balance and annual interest rate
balance=eval(input("Enter the balance left in the investment account: "))
annualInterest=eval(input("Enter the annual Interest Rate: "))

interest=balance*(annualInterest/1200)      # The formula

print(f"The interest is: {interest}")       # Prints out the results