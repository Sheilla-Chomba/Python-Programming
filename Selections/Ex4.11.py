# Below is the programming exercise
# (Find the number of days in a month) Write a program that prompts the user to
# enter the month and year and displays the number of days in the month. For example,
# if the user entered month 2 and year 2000, the program should display that
# February 2000 has 29 days. If the user entered month 3 and year 2005, the program
# should display that March 2005 has 31 days.

import time
print("This program mainly displays the number of days in the month and year you would want to know.")
time.sleep(2)
print("You will be required to type in the month first then the year(1 A.C. continuous)")
time.sleep(2)
print("Months will be represented as follows: "
      "\n\t January - 1"
      "\n\t February - 2"
      "\n\t March - 3"
      "\n\t April - 4"
      "\n\t May - 5"
      "\n\t June - 6"
      "\n\t July - 7"
      "\n\t August - 8"
      "\n\t September - 9"
      "\n\t October - 10"
      "\n\t November - 11"
      "\n\t December - 12")
time.sleep(3)
# Prompts user to type in the month
month=eval(input("Kindly type in the month as per the instructions above: "))

while month<1 or month>12:
    month = eval(input("Wrong input. Kindly type in the month as per the instructions above: "))

# Prompts user to type in the year
year=eval(input("Kindly type in year as per the instructions above: "))

while year<1:
    year = eval(input("Wrong input. Kindly type in year as per the instructions above: "))

if month==1:
    days=31
    print(f"January of {year} has {days} days")
if month==2:
    if year%4==0:
        days=29
    else:
        days=28
    print(f"February of {year} has {days} days")
if month==3:
    days=31
    print(f"March of {year} has {days} days")
if month==4:
    days=30
    print(f"April of {year} has {days} days")
if month==5:
    days=31
    print(f"May of {year} has {days} days")
if month==6:
    days=30
    print(f"June of {year} has {days} days")
if month==7:
    days=31
    print(f"July of {year} has {days} days")
if month==8:
    days=31
    print(f"August of {year} has {days} days")
if month==9:
    days=30
    print(f"September of {year} has {days} days")
if month==10:
    days=31
    print(f"October of {year} has {days} days")
if month==11:
    days=30
    print(f"November of {year} has {days} days")
if month==12:
    days=31
    print(f"December of {year} has {days} days")