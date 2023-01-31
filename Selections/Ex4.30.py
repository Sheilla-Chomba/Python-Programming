# Below is the programming exercise
# (Current time) Revise Programming Exercise 2.18 to display the hour using a 12-
# hour clock.

import time                 # This imports the class time()

seconds=time.time()         # These are the current seconds from 1.1.1970, GMT
currentSeconds=seconds%60
minutes=seconds/60
currentMinutes=minutes%60
hours=minutes/60
currentHours=hours%24

# Prompts user to input their timezone
gmt=eval(input("Enter your timezone: "))
actualHours=currentHours+gmt

if int(actualHours)<1:
    actualHours = actualHours + 12
    print(int(actualHours), ":", int(currentMinutes), ":", int(currentSeconds), "PM the previous day")
if int(actualHours)>23:
    actualHours = actualHours - 12
    print(int(actualHours), ":", int(currentMinutes), ":", int(currentSeconds), "AM the next day")


if int(actualHours)//12==0:
    print(int(actualHours), ":", int(currentMinutes), ":", int(currentSeconds), "AM")

if int(actualHours)//12==1:
    actualHours=actualHours-12
    print(int(actualHours), ":", int(currentMinutes), ":", int(currentSeconds),"PM")



#print(int(actualHours),":",int(currentMinutes),":",int(currentSeconds))    # Prints out the actual Hour according to the GMT
print (currentHours)