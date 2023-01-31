# Below is the programming exercise
# Palindrome number) Write a program that prompts the user to enter a three-digit
# integer and determines whether it is a palindrome number.

# Prompts user to type in a three digit integer to check whether it is a palindrome
number=eval(input("Enter any three digit number to check whether it is a palindrome: "))

while number<100 or number>999:
    number = eval(input("Wrong input. Enter any three digit number to check whether it is a palindrome: "))

digit1=number%10
remNum=number//10
digit2=remNum%10
digit3=remNum//10

if digit1==digit2==digit3:
    print(f"{number} is a palindrome.")
elif digit1==digit3:
    print(f"{number} is a palindrome.")
else:
    print(f"{number} is not a palindrome.")