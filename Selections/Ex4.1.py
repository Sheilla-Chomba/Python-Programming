# Below is the programming exercise
# Write a program that prompts the user to enter values for a, b, and c and displays
# the result based on the discriminant. If the discriminant is positive, display two
# roots. If the discriminant is 0, display one root. Otherwise, display The equation
# has no real roots.

import math
# Prompts user to type in the value of a, b and c
a=eval(input("Enter the value of a: "))
b=eval(input("Enter the value of b: "))
c=eval(input("Enter the value of c: "))

discriminant=(math.pow(b,2))-(4*a*c)

if discriminant<0:
    print("The equation has no real root.")
elif discriminant==0:
    print("The equations root is 0")
else:
    root1=(-b+math.sqrt(math.pow(b,2)-(4*a*c)))/(2*a)
    root2 = (-b - math.sqrt(math.pow(b, 2) - (4 * a * c))) / (2 * a)
    print("The square root for the equation are: \n \t",format(root1,".2f"),"\n \t",format(root2,".2f"))