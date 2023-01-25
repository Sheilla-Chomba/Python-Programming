# Below is a case study to determine whether an year is a leap year

# Prompts user to type in the year
year=eval(input("Enter the year you would like to enquire: "))

while year<1:
    year = eval(input("Wrong input. Kindly enter the right year you would like to enquire: "))

if year%4==0:
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")