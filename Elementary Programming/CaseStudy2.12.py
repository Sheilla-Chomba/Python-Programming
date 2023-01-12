# Below is a case study to show the current time in GMT

import time

# Returns time from 1/1/1970 in seconds
currentTime=time.time()

# Returns current Seconds
currentSeconds=int(currentTime%60)

# Returns tha remaining seconds
remainSeconds=currentTime//60

# This indicates the current minutes
currentMin=int(remainSeconds%60)

# This indicates the remaining minutes
remainMin=remainSeconds//60

# This indicates the current hours
currentHours=int(remainMin%24)

print("The time in GMT is ",currentHours,":",currentMin,":",currentSeconds)