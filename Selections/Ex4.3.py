# Below is the programming exercise
# Write a program that prompts the user to enter a, b, c, d, e, and f and display the
# result. If ad – bc is 0, report that The equation has no solution.

# Prompts user to type in the value of a, b, c, d, e and f
a=eval(input("Type in the value of a: "))
b=eval(input("Type in the value of b: "))
c=eval(input("Type in the value of c: "))
d=eval(input("Type in the value of d: "))
e=eval(input("Type in the value of e: "))
f=eval(input("Type in the value of f: "))

if ((a*d)-(b*c))==0:
    print("The equation has no solution.")
else:
    x=((e*d)-(b*f))/((a*d)-(b*c))
    y=((a*f)-(e*c))/((a*d)-(b*c))
    print(f"The value of x is {x} and that of y is {y}")