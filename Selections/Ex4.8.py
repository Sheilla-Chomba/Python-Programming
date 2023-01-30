# Below is the programming exercise
# (Sort three integers) Write a program that prompts the user to enter three integers
# and displays them in increasing order.

# Prompts user to type in three digit integer
number=eval(input("Kindly type in a three digit integer: "))

while number<100 or number>999:
    number = eval(input("Wrong input. Kindly type in a three digit integer: "))

dig1=number%10
remNum=number//10
dig2=remNum%10
dig3=remNum//10

if dig1==dig2==dig3:
    print(dig1)
    print(dig2)
    print(dig3)
if dig1<dig2 and dig1<dig3:
    print(dig1)
    if dig2<=dig3:
        print(dig2)
        print(dig3)
    else:
        print(dig3)
        print(dig2)
if dig2<dig1 and dig2<dig3:
    print(dig2)
    if dig1 <= dig3:
        print(dig1)
        print(dig3)
    else:
        print(dig3)
        print(dig1)
if dig3<dig2 and dig3<dig1:
    print(dig3)
    if dig2 <= dig1:
        print(dig2)
        print(dig1)
    else:
        print(dig1)
        print(dig2)