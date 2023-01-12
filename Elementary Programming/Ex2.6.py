# Below is the programming exercise
# (Sum the digits in an integer) Write a program that reads an integer between 0 and
# 1000 and adds all the digits in the integer.

# Prompts user to type in the integer
number=eval(input("Enter any number from 0-999: "))

num1=number%10      # This helps us get the value of the last digit(ones value) in the number
remNum1=number//10  # This helps us get the remaining digits in the number without the last number. It basically eliminates the last number.

num2=remNum1%10     # This helps us get the value of the middle digit(tens value) in the number
remNum2=remNum1//10 # This helps us get the remaining digits in the number without the middle number. It basically eliminates the middle number.

num3=remNum2%10     # This helps us get the value of the first digit(hundreds value) in the number

results=num1+num2+num3 # This adds up the digits

# Prints the final results
print("The addition of the digits in the number is ",results)