# This is a case study for finding GCD for two integers

num1=eval(input("Enter the first integer: "))
num2=eval(input("Enter the second integer: "))
gcd=1
gcdanswer=1

while gcdanswer<=num1 and gcdanswer<=num2:
    if num1%gcdanswer==0 and num2%gcdanswer==0:
        gcd=gcdanswer
    gcdanswer+=1
print(f"The gcd is {gcd}")