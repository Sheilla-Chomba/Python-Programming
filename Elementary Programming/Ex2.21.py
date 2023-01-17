# Below is the programming exercise
# Write a program that prompts the user to enter a monthly saving amount and
# displays the account value after the sixth month.

# Prompts user to type in the monthly saving amount
savingAmt=eval(input("Enter the amount you are going to be saving on a monthly rate: "))

month1=savingAmt*(1+0.00417)            # Balance as of end of month 1
month2=(savingAmt+month1)*(1+0.00417)         # Balance as of end of month 2
month3=(savingAmt+month2)*(1+0.00417)         # Balance as of end of month 3
month4=(savingAmt+month3)*(1+0.00417)         # Balance as of end of month 4
month5=(savingAmt+month4)*(1+0.00417)         # Balance as of end of month 5
month6=(savingAmt+month5)*(1+0.00417)         # Balance as of end of month 6

print(f" As from 6 months, the value will be at: {month6}")     # Prints the value as at 6 months