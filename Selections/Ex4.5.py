# Below is the programming exercise
# (Find future dates) Write a program that prompts the user to enter an integer for
# today’s day of the week (Sunday is 0, Monday is 1, ..., and Saturday is 6). Also
# prompt the user to enter the number of days after today for a future day and display
# the future day of the week.

import time

print("Every day of the week will be represented by digits:"
      "\n\t 0 will be Sunday"
      "\n\t 1 will be Monday"
      "\n\t 2 will be Tuesday"
      "\n\t 3 will be Wednesday"
      "\n\t 4 will be Thursday"
      "\n\t 5 will be Friday"
      "\n\t 6 will be Saturday")
time.sleep(5)

# Prompts user to type in the value of today's day
day=eval(input("Type in the day today using the above instructions: "))

while day<0 or day>6:
    day = eval(input("Wrong input."
                     "\n Kindly read through the above instructions carefully and type in the day today using the above instructions: "))

daysElapsed=eval(input("How many days have elapsed since today: "))
while daysElapsed<0:
    daysElapsed = eval(input("Wrong input."
                     "\n Kindly type in days as from 0 onwards: "))


if (day+daysElapsed)%7==0:
    dayOfWeek="Sunday"
if (day+daysElapsed)%7==1:
    dayOfWeek="Monday"
if (day+daysElapsed)%7==2:
    dayOfWeek="Tuesday"
if (day+daysElapsed)%7==3:
    dayOfWeek="Wednesday"
if (day+daysElapsed)%7==4:
    dayOfWeek="Thursday"
if (day+daysElapsed)%7==5:
    dayOfWeek="Friday"
if (day + daysElapsed) % 7 == 6:
    dayOfWeek = "Saturday"

if day==0:
    day="Sunday"
if day == 1:
    day = "Monday"
if day == 2:
    day = "Tuesday"
if day==3:
    day="Wednesday"
if day == 4:
    day = "Thurday"
if day == 5:
    day = "Friday"
if day == 6:
    day = "Saturday"

print(f"Today is {day} and the future day is {dayOfWeek}")