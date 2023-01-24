# Below is the programming exercise
# (Find the character of an ASCII code) Write a program that receives an ASCII
# code (an integer between 0 and 127) and displays its character. For example, if the
# user enters 97, the program displays the character a.

# Prompts user to type in the ASCII code to be converted
asciiCode=eval(input("Enter the ASCII code to be converted (Please type in from 0 to 127): "))

# The while loop ensures that incase user types in outside the range of 0-127, they will repeat the process again
while asciiCode>127 or asciiCode<0:
    asciiCode = eval(input("You entered the ASCII code wrongly. Please type in from 0 to 127: "))

convertedCode=chr(asciiCode)                    # converts ASCII code to character
print(f"The character represented by the ASCII code is: {convertedCode}")     # prints the converted value