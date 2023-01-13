# Below is the programming exercise
# (Split digits) Write a program that prompts the user to enter a four-digit integer
# and displays the number in reverse order.

# Prompts user to type in the four digit number
number=eval(input("Enter any four digit number: "))

dig1=number//1000               # Helps us get the first digit in the number
remNumber1=number%1000          # Returns the remaining number after removing the first digit from the number

dig2=remNumber1//100            # Helps us get the second digit in the number
remNumber2=remNumber1%100       # Returns the remaining number after removing the first two digits from the number

dig3=remNumber2//10             # Helps us get the third digit in the number
dig4=remNumber3=remNumber2%10   # Helps us get the forth digit in the number after removing the first three digis from the number

print(f"{dig1}",f"\n{dig2}",f"\n{dig3}",f"\n{dig4}")    # Print each digit on its line