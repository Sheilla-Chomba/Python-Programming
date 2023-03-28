# Reversing digit inputs using lists

number=input("Enter any number: ")

numberList=[]

for digit in number:
    numberList.append(digit)        # Adds the each input digit into the list

numberList.reverse()                # Reverses the order of the list

for dig in numberList:
    print(dig,end="")               # Prints out the digits in a reversed order as per the list and as a string