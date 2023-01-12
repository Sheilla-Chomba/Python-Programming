# Below is the programming exercise
# (Financial application: calculate tips) Write a program that reads the subtotal and
# the gratuity rate and computes the gratuity and total. For example, if the user
# enters 10 for the subtotal and 15% for the gratuity rate, the program displays 1.5
# as the gratuity and 11.5 as the total.

# Prompts user to type in subtotal and gratuity rate
subtotal= eval(input("Enter the subtotal: "))
gratuityRate=eval(input("Enter the gratuity rate: "))

# Calculation of the gratuity and total
gratuity= subtotal*(gratuityRate/100)
total=subtotal+gratuity

# Prints out the results of the calculations
print("The gratuity is ",gratuity," while the total is ",total)