# Below is the programming exercise
# (Check a number) Write a program that prompts the user to enter an integer and
# checks whether the number is divisible by both 5 and 6, divisible by 5 or 6, or just
# one of them (but not both)

# Prompts user to type in the any random number
number=eval(input("Type in any number: "))

if number%5==0 and number%6==0:
    print(f"Is {number} divisible by 5 and 6? ",number%5==0 and number%6==0)
else:
    print(f"Is {number} divisible by 5 and 6? ", number % 5 == 0 and number % 6 == 0)
    if number%5==0 or number%6==0:
        print(f"Is {number} divisible by 5 or 6? ", number % 5 == 0 or number % 6 == 0)
        print(f"Is {number} divisible by 5 or 6, but not both? ", number % 5 == 0 or number % 6 == 0)
    else:
        print(f"Is {number} divisible by 5 or 6? ", number % 5 == 0 or number % 6 == 0)