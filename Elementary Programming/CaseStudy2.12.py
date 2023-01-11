# Below is a case study to show the current time in GMT

import time

# Returns time from 1/1/1970 in seconds
currentTime=time.time()

# Returns current Seconds
currentSeconds=currentTime%60

# Returns tha remaining seconds
remainSeconds=currentTime//60

# This indicates the current minutes
currentMin=remainSeconds%60

# This indicates the remaining minutes
remainMin=remainSeconds//60

# This indicates the current hours
currentHours=remainMin%60

print("The time in GMT is ",currentHours,":",currentMin,":",currentSeconds)