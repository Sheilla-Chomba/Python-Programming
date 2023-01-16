# Below is the programming exercise
# (Current time) Listing 2.7, ShowCurrentTime.py, gives a program that displays the
# current time in GMT. Revise the program so that it prompts the user to enter the
# time zone in hours away from (offset to) GMT and displays the time in the specified
# time zone.

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

print(int(actualHours),":",int(currentMinutes),":",int(currentSeconds))    # Prints out the actual Hour according to the GMT
