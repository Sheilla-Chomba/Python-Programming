# Below is the programming exercise
# Write a program that prompts the user to enter a year, month, and day of the
# month, and then it displays the name of the day of the week.

# Prompts user to type in the year, month and day of the month
year=eval(input("Type in year: "))
month=eval(input("Type in month ie. 1-12: "))
date=eval(input("Type in date: "))

century=year/100
yearCentury=year%100
day=(date+int((26*(month+1))/10)+yearCentury+int(yearCentury/4)+int(century/4)+(5*century))%7

if int(day)==0:
    dayWeek="Saturday"
    print(f"Day of the week is {dayWeek}")
if int(day)==1:
    dayWeek="Sunday"
    print(f"Day of the week is {dayWeek}")
if int(day)==2:
    dayWeek="Monday"
    print(f"Day of the week is {dayWeek}")
if int(day)==3:
    dayWeek="Tuesday"
    print(f"Day of the week is {dayWeek}")
if int(day)==4:
    dayWeek="Wednesday"
    print(f"Day of the week is {dayWeek}")
if int(day)==5:
    dayWeek="Thursday"
    print(f"Day of the week is {dayWeek}")
if int(day)==6:
    dayWeek="Friday"
    print(f"Day of the week is {dayWeek}")

# (Hint: [n]= n//1 for a positive n. January and February are counted as 13 and 14
# in the formula, so you need to convert the user input 1 to 13 and 2 to 14 for the
# month and change the year to the previous year.)