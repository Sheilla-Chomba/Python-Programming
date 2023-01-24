# Below is the programming exercise
# (Reverse number) Write a program that prompts the user to enter a four-digit integer
# and displays the number in reverse order.

# Prompts user to type in any four digit number
number=eval(input("Enter any four digit number: "))

while number<1000 or number>9999:
    number = eval(input("Input was incorrect.Kindly enter any four digit number: "))

digit1=number//1000
remNum1=number%1000
digit2=remNum1//100
remNum2=remNum1%100
digit3=remNum2//10
digit4=remNum2%10

print(f"The reverse of the above number is {digit4}{digit3}{digit2}{digit1}")